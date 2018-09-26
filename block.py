import json
import os
import hashlib


blockchain_dir = os.curdir + '/blockchain/'


def get_hash(filename):
    file = open(filename, 'rb').read()

    return hashlib.md5(file).hexdigest()


def get_files():
    files = os.listdir(blockchain_dir)

    return sorted([int(i) for i in files])


def check_integrity():
    files = get_files()
    results = []

    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']
        prev_file = blockchain_dir + str(file-1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        results.append({'block': prev_file, 'result': res})

    return results


def write_block(name, amount, to):
    files = get_files()

    if len(files) > 0:
        last_file = files[-1]

        filename = blockchain_dir + str(last_file + 1)
        prev_hash = get_hash(blockchain_dir + str(last_file))
    else:
        filename = blockchain_dir + str(0)
        prev_hash = ''

    data = {'name': name,
            'amount': amount,
            'to': to,
            'hash': prev_hash}

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block(name='Test Name', amount=25, to='To Test Name')
    print(check_integrity())


if __name__ == '__main__':
    main()

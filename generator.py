import hashlib

PATH = 'result.txt'


def generator_md5(file_path):
    file = open(file_path, encoding='utf-8')
    for line in file:
        md5_hash = hashlib.md5(line.strip().encode('utf-8'))
        yield md5_hash.hexdigest()


if __name__ == '__main__':
    for item in generator_md5(PATH):
        print(item)

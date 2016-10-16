import hashlib


def hash_file(filename):
    h = hashlib.sha1()

    # открываем файл в бинарном виде.
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            # читаем кусочками по 1024 байта
            chunk = file.read(1024)
            h.update(chunk)

    # hex-представление полученной суммы.
    return h.hexdigest()


path = "/tmp/example.txt"
f = open(path, "w")
f.write("Технопарк\n")
f.close()

import ipdb
ipdb.set_trace()

result = hash_file(path)
print(result)

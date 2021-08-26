# conding=utf8
import os
import sys
import hashlib
path = sys.argv[1]


def outputShareCode(path, name):
    with open(path, 'rb') as f:
        # 获取 sha1
        sha1obj = hashlib.sha1()
        for chunk in iter(lambda: f.read(2 ** 20), b""):
            sha1obj.update(chunk)
        hash = sha1obj.hexdigest()
        # 获取 文件大小
        fSize = os.path.getsize(path)
        print('aliyunpan://' + name + '|' + str(hash) + '|' + str(fSize) + '|')

# 传入文件
if os.path.isfile(path):
    name = os.path.basename(path)
    outputShareCode(path, name)
# 传入文件夹
elif os.path.exists(path):
    g = os.walk(path)
    for path, dir_list, file_list in g:
        for file_name in file_list:
            outputShareCode(os.path.join(path, file_name), file_name)
else:
    print("error argv")

import bz2
import os
dirpath = os.path.dirname(os.path.realpath(__file__))
files = []
for file in os.listdir(dirpath):
    if file.endswith(".bz2"):
        files.append(file)

for filename in files:
    filepath = os.path.join(dirpath, filename)
    newfilepath = os.path.join(dirpath, filename.replace('.bz2', '') )
    with open(newfilepath, 'wb') as new_file, bz2.BZ2File(filepath, 'rb') as file:
        for data in iter(lambda : file.read(100 * 1024), b''):
            new_file.write(data)

from zipfile import ZipFile

zip_ = ZipFile('resources/file.zip.zip')
print(zip_.namelist())

text = zip_.read('Æ« τΓ« ¡πª¡« ßñÑ½áΓ∞ ñ½∩ üÄ.txt')
print(text)
zip_.close()


with ZipFile('resources/file.zip.zip') as yzip:
    yzip.extract('Æ« τΓ« ¡πª¡« ßñÑ½áΓ∞ ñ½∩ üÄ.txt')


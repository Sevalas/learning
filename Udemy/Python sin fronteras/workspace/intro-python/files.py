import os

file1 = open('test.properties','w+')
# segundo parametro de open()
# w = write
# w+ = write + read + create
# a = append
# a+ = append + read
# r = read
# x = create

# print(file1.read())
# print(file1.readline())
# print(file1.readline())
# print(file1.readline())
# print(file1.readline())
for line in file1:
    print(line)
file1.close()

file2 = open('test.properties', 'a+')

# \n = new line

file2.write('\nadd a new line')
print('--------------------------')
file2.seek(0)
print(file2.read())
file2.close()

# remove file
if os.path.exists('test.properties'):
    os.remove('test.properties')
else:
    print('file not found :o')

# remove directory
if os.path.exists('myFolder'):
    os.rmdir('myFolder')
else:
    print('folder not found :o')
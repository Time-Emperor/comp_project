from read_file import open_file


def read_data(path):
    file = open_file(path,'r')
    print(file.read())
    file.close()
    read_data('file.txt')
    read_data('new.txt')
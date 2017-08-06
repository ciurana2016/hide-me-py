import os
import sys
import gzip
import shutil
import binascii

from random import choice


NUM_FOLDERS = 10


def random_string(length):
    return binascii.b2a_hex(os.urandom(length))


def random_list(items, length):
    return [random_string(length) for _ in xrange(items)]


def error(string):
    print '\nError: %s\n' % string


def makefile(path, size):
    f = open(path, 'wb')
    f.write(os.urandom(size))
    f.close()


def gzip_file(path):
    with open(path, 'rb') as file_in:
        with gzip.open('%s.gz' % path, 'wd') as file_out:
            shutil.copyfileobj(file_in, file_out)
    os.remove(path)


def main():
    if len(sys.argv) == 1:
        return error('Give me a file boy!')

    file_path = sys.argv[1]
    file_size = os.path.getsize(file_path)
    folder_list = random_list(NUM_FOLDERS, 10)

    # Generate a parten folder so its easy to remove all
    # the output later by just deleting it
    parent_folder = 'output-%s' % random_string(10)
    os.makedirs(parent_folder)

    # Add parent folder to the list of folders
    folder_list = ['%s/%s' % (parent_folder,f) for f in folder_list]

    # Generate NUM_FOLDERS with 10 files inside 
    # each file has the same size as the original one
    for folder in folder_list:
        subfolder = folder
        os.makedirs(subfolder)

        for n in xrange(10):
            new_file_path = '%s/%s' % (subfolder, random_string(10))
            makefile(new_file_path, file_size)
            gzip_file(new_file_path)

    # Select a random folder to move our file there
    random_folder = choice(folder_list)
    random_file = choice(os.listdir( random_folder))
    final_path = '%s/%s' % (random_folder, random_file)

    # Remove selected choice
    os.remove(final_path)

    # Move the file
    final_path = final_path.replace('.gz','')
    os.rename(file_path, final_path)

    # Compress the file
    gzip_file(final_path)

    print 'Your file is now under %s.gz' % final_path


if __name__ == '__main__':
    main()

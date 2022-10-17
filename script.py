import os
import shutil
from datetime import datetime
import tarfile


dir_name = '/home/darik/Desktop/log'  # here you can specify the path to the required directory
date_of_creating = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Exact creation time without microseconds


def gzip():  # To compress a file or folder
    # the path where the compressed folder will be located
    tar = tarfile.open(f"/home/darik/Desktop/ziplog/{date_of_creating}GzipFiles.tar.gz", "w:gz")
    tar.add(dir_name, arcname="Data")
    tar.close()


def clear():  # To delete a file or folder inside dir_name
    # This method returns a list containing the names of the entries in the directory given by path.
    for file_or_directory_name in os.listdir(dir_name):
        path = os.path.join(dir_name, file_or_directory_name)  # get absolute path to file or folder
        if os.path.isfile(path) or os.path.islink(path):
            print('Deleting file', path)
            os.unlink(path)
        elif os.path.isdir(path):
            print('Deleting dir', path)
            shutil.rmtree(path)
        else:
            raise ValueError("Path {} is not a file or dir.".format(path))


gzip()
clear()

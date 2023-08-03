import os
import shutil
from tkinter import filedialog


def show_all_files(dir):
    """
    given the file_folder path, using the Treeview to show all the files in the subfolder

    :param dir: the path of the directory
    :return:the list of all the files in the directory
    """
    lis= []
    for home, subdirs, files in os.walk(dir):
        for idx, dire in enumerate(subdirs):
            sub_path = home+"/"+dire
            show_all_files(sub_path)
        for idx, fil in enumerate(files):
            lis.append(home+"/"+fil)
    return lis


def bulk_change(dir, new_path):
    """

    :param dir: the directory of the ws file
    :param new_path: the new-path of the txt file
    :return:
    """
    lis = show_all_files(dir)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    for i in lis:
        tp = i.split(".")
        filename = i.split("/")[-1]
        new_filename = filename.replace("ws", "txt")
        if tp[-1] == "ws":
            shutil.copyfile(i, new_path+"/"+filename)
            os.rename(new_path+"/"+filename, new_path+"/"+new_filename)
            with open(new_path+"/"+new_filename, encoding="utf8", errors='ignore') as f:
                lines = f.readlines()
            f.close()
            os.remove(new_path+"/"+new_filename)
            with open(new_path+"/"+new_filename, "w+", encoding="UTF-8") as output_file:
                count = 0
                for r in lines:
                    print(count)
                    if count == 0:
                        count = count + 1
                        continue
                    else:
                        output_file.write(r)
                        output_file.write("\n")
                    count = count + 1


def directory_path_selection():
    filename = filedialog.askdirectory()
    return filename


directory_path = directory_path_selection()+"/preservation"   # the path of the directory in which are all the ws files in search.
new_file_folder_path = directory_path_selection()+"/access_ws"  # the new path of the file folder in which you will put the new txt files in.
bulk_change(directory_path, new_file_folder_path)


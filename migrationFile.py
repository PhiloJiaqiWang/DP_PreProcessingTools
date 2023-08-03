import os


def target_items_finding(the_directory, the_condition):
    """
     detect all the files that fit the requirements (e.g. for renaming process to rename every ‘$’ into ‘’, it will
     first detect all the files whose filenames include ‘$’), the path to the filenames will all be stored in a list.

    :return:
    >>> target_items_finding("C:/Users/jiaqi17/Desktop/test", "mushroom")
    """
    this_path = the_directory + "/access"
    if not os.path.exists(this_path):
        return False
    else:
        all_files = all_files_under(this_path)
        target_list = []
        for path, filename in all_files.items():
            if the_condition in filename:
                target_list.append(path)
        return target_list


def all_files_under(the_directory):
    """
    show all the files under this directory

    :param the_directory:
    :return: a list
    """
    all_files = {}
    for home, subdirs, files in os.walk(the_directory):
        for idx, dire in enumerate(subdirs):
            sub_path = home + "/" + dire
            all_files_under(sub_path)
        for idx, fil in enumerate(files):
            all_files[home + "/" + fil] = fil
    return all_files


def migration_folder_creating(the_collection_directory):
    """
     detect all the files that fit the requirements (e.g. for renaming process to rename every ‘$’ into ‘’, it will
     first detect all the files whose filenames include ‘$’), the path to the filenames will all be stored in a list.

    :return:
    >>> migration_folder_creating("C:/Users/jiaqi17/Desktop/test")
    """
    this_path = the_collection_directory + "/access"
    if not os.path.exists(this_path):
        return False
    else:
        newpath = the_collection_directory + "/migration"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            return True

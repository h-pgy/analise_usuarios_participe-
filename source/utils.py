import os


def solve_folder(folder, parent_folder=None):

    if parent_folder:
        folder = os.path.join(parent_folder, folder)

    if not os.path.exists(folder):

        os.mkdir(folder)

    folder = os.path.abspath(folder)

    return folder

def solve_fpath(fname, folder):

    folder = solve_folder(folder)

    return os.path.join(folder, fname)


def list_files(folder, extension=None):

    folder=  solve_folder(folder)

    if extension:
        return [solve_fpath(file, folder) for file in 
        os.listdir(folder) if file.endswith(extension)]

    return [solve_fpath(file, folder) for file 
            in os.listdir(folder)]



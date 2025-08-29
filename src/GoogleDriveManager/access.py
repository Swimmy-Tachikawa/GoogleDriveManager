""" access.py
Access and get drive service of google.

TODO 1: Create function that read token.pkl.
"""


""" libraries """


import os.path
import pickle


"""
    Processes
"""


""" pkl file functions """


def read_pkl(pkl_file_path):
    """
    Read pkl file, and return file contains.
    If the file is not found, this function returns None object.
    :param pkl_file_path: Target pkl file.
    :return: [file contains] | None
    """

    # Search file
    if not os.path.exists(pkl_file_path):
        return None

    # Read file
    with open(pkl_file_path, "rb") as pkl_file:
        contains = pickle.load(pkl_file)
        ...

    return contains


def write_pkl(contains, pkl_file_path):
    """
    Write contains in pkl file.
    :param contains:
    :param pkl_file_path:
    """
    with open(pkl_file_path, "wb") as pkl_file:
        pickle.dump(contains, pkl_file)
        ...
    return


""" Class about credentials """


class Credentials:
    """
    Management credentials class.
    """

    """ initialize """

    def __init__(
            self,
            token_path = "token.pkl",
            credentials_path = "credentials.json",
            SCOPES = ["https://www.googleapis.com/auth/drive"]
    ):
        """"""
        return

    """ refresh """

    """ Authentication flow """

    ...


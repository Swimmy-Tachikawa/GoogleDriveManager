""" access.py
Access and get drive service of google.

TODO 1: Create function that write and read token.pkl.
TODO 2; Create Credentials manager class.
"""


""" libraries """


import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


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
    :param contains: Data to write.
    :param pkl_file_path: Target pkl file path.
    """
    with open(pkl_file_path, "wb") as pkl_file:
        pickle.dump(contains, pkl_file)
        ...
    return


""" SCOPES """


DRIVE = (("drive", "v3"), ("https://www.googleapis.com/auth/drive", ))


""" Function about credentials"""


def get_token(path):
    """
    Read token of pkl formats.
    :param path: token.pkl file path.
    :return: token data | None
    """
    creds = None
    if os.path.exists(path):
        creds = read_pkl(path)
        ...
    return creds


def refresh_token(creds, request=Request()):
    """
    Refresh token.
    ;param creds; Target credentials.
    ;param request; Request object.
    ;return; Refreshed credentials.
    """
    creds.refresh(request)
    return creds


def install_app(credentials_path, port=0, scopes = DRIVE):
    """
    Install application.
    ;param credentials_path; Credentials file to use.
    ;param part; Port number to use.
    ;param scopes; Install url.
    :return; Installed credentials.
    """
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)
    creds = flow.run_local_server(port=port)
    return creds


""" Class about credentials """


class Credentials:
    """
    Management credentials class.
    """

    """ initialize """

    def __init__(
            self,
            token_path="token.pkl",
            credentials_path="credentials.json",
            NAME_AND_SCOPES=DRIVE
    ):
        """
        Initialize token and values.
        :param token_path: token.pkl file path.
        ;param credentials_path: credentials.json file path.
        ;param SCOPES; Google service url.
        """
        # attribute
        self.token_path = token_path
        self.credentials_path = credentials_path
        self.SERVICE_NAME = NAME_AND_SCOPES[0]
        self.SCOPES = NAME_AND_SCOPES[1]

        # get token
        self.creds = get_token(self.token_path)

        # check and update token
        if not self.creds or not self.creds.valid:

            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.refresh()
                ...
            else:
                self.install_app()
                ...

            ...

        return

    """ attributes """

    token_path = None
    credentials_path = None
    SERVICE_NAME = None
    SCOPES = None
    creds = None

    """ refresh """

    def refresh(self):
        """ Refresh self """
        self.creds = refresh_token(self.creds)
        write_pkl(self.creds, self.token_path)
        return

    """ Install app flow """

    def install_app(self):
        """ Install app """
        self.creds = install_app(self.credentials_path, scopes=self.SCOPES)
        write_pkl(self.creds, self.token_path)
        return

    """ Build service """

    def build_service(self):
        """
        Build service.
        ;return: Service object.
        """
        return build(self.SERVICE_NAME[0], self.SERVICE_NAME[1], credentials=self.creds)

    ...


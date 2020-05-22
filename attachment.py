import os
from pathlib import Path, PurePath


class Attachment:
    def __init__(self, folder='cv'):
        self.folder = folder

    def attachments(self):
        """Scan folder and save paths


        :returns Dict
        fp - filepath

            {
                'Lastname Name': ['fp', 'profession'],
                'Lastname2 Name2': ['fp2', 'profession2'],
                ...
            }

        """
        result = {}
        for address, dirs, files in os.walk(self.folder):
            if files:
                files = self._remove_tempfiles()
                for file in files:
                    key = Path(file.stem)  # prepare key 'Lastname Firstname' for dict
                    fp = Path(file).resolve()  # prepare filepath
                    position = PurePath(address).parts[-1]  # prepare position of candidate
                    result[key] = [fp, position]
        return result

    def _prepare_filename(self, filename: str):
        """Create 'Lastname Firstname' identifier

        For simplicity we assume that filename will consists of only three or two words
        """

        filename = Path(filename).stem  # remove suffix like .pdf
        filename = filename.split(' ')

        if len(filename) == 3:
            lastname_firstname = ' '.join(filename[0:2])
            middlename = filename[2]
            return lastname_firstname, middlename
        elif len(filename) == 2:
            lastname_firstname = ' '.join(filename[0:2])
            middlename = None
            return lastname_firstname, middlename
        else:
            return filename, None

    def _is_tempfile(self, filename: str):
        return filename.startswith(prefix=('.', '~', 'lock'))

    def _remove_tempfiles(self, files):
        """Create new list without tempfiles"""
        return [file for file in files if self._is_tempfile(file)]

    def add_attachment(self, candidates):
        __attachments = self.attachments()
        for candidate in candidates:
            if candidate.lastname_firstname in __attachments:
                candidate.lastname_firstname = __attachments[]
                pass


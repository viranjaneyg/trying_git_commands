from pathlib import Path
import zipfile, fnmatch, os

tableau_file_path = Path("/Users/viranjaney.g/PycharmProjects/tableau_to_ts/tableau_files/")


def twbx_to_zip(file_path):
    for f in file_path.iterdir():
        if f.is_file() and f.suffix in ['.twbx']:
            f.rename(f.with_suffix('.zip'))


def extract_tableau_zip(file_path):
    pattern = '*.zip'
    for root, dirs, files in os.walk(file_path):
        for filename in fnmatch.filter(files, pattern):
            zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))

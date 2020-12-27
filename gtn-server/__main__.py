"""GTN

Usage:
  gtn <input_gtm_file>
  gtn (-h | --help)
  gtn --version

Options:
  -h --help         Show this screen.
  --version         Show version.
"""

from docopt import docopt
import os
import tempfile
import zipfile


def main():

    args = docopt(__doc__, version='0.0.1')

    # Extract the .gtm file and get the file list
    with tempfile.TemporaryDirectory() as tmp_dirname:
        gtm_files = {} # file list
        with zipfile.ZipFile(args['<input_gtm_file>'], 'r') as zip_ref:
            zip_ref.extractall(tmp_dirname)
            for root, dirs, files in os.walk(tmp_dirname):
                name = 'gtm' if root == tmp_dirname else os.path.basename(os.path.normpath(root))
                gtm_files[name] = []
                for item in files:
                    gtm_files[name].append(os.path.join(root, item))

        # ... and here we can go throught the files and read them for saving usefull information to our database
        # for future usage
        print(gtm_files)


if __name__ == '__main__':
    main()

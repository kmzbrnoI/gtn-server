"""GTN

Usage:
  gtn <input_gtm_file> <output_directory>
  gtn (-h | --help)
  gtn --version

Options:
  -h --help         Show this screen.
  --version         Show version.
"""

from docopt import docopt
import zipfile


def main():

    args = docopt(__doc__, version='0.0.1')

    with zipfile.ZipFile(args['<input_gtm_file>'], 'r') as zip_ref:
        zip_ref.extractall(args['<output_directory>'])



if __name__ == '__main__':
    main()

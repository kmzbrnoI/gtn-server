"""GTN

Usage:
  gtn <input_gtm_file>
  gtn (-h | --help)
  gtn --version

Options:
  -h --help         Show this screen.
  --version         Show version.
"""

import json
from core.gtm_parser import GTMParser
from docopt import docopt


def main():

    args = docopt(__doc__, version='0.0.1')

    gtm_parser = GTMParser(args['<input_gtm_file>'])
    gtm_data = gtm_parser.get_data()
    print(json.dumps(gtm_data, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()

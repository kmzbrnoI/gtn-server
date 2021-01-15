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
import json
import xml.etree.ElementTree as ET


def get_element_text(root, tag):

    items = []
    for id_element in root.iter(tag):
        items.append(id_element.text)

    if len(items) != 1:
        print("Error: {} has {} test values".format(tag, len(items)))
    return items[0]


def parse_engine_class_file(engine_class_file):

    engine_class = {'type': 'engine_class'}

    tree = ET.parse(engine_class_file)
    root = tree.getroot()

    engine_class['id'] = get_element_text(root, 'id')
    engine_class['name'] = get_element_text(root, 'name')
    engine_class['speed'] = get_element_text(root, 'speed')

    return engine_class


def main():

    args = docopt(__doc__, version='0.0.1')

    # Extract the .gtm file and get the file list
    with tempfile.TemporaryDirectory() as tmp_dirname:
        gtm_files = {}  # file list
        with zipfile.ZipFile(args['<input_gtm_file>'], 'r') as zip_ref:
            zip_ref.extractall(tmp_dirname)
            for root, dirs, files in os.walk(tmp_dirname):
                name = 'gtm' if root == tmp_dirname else os.path.basename(os.path.normpath(root))
                gtm_files[name] = []
                for item in files:
                    gtm_files[name].append(os.path.join(root, item))

        # ... and here we can go throught the files and read them for saving usefull information to our database
        # for future usage

        gtm_data = {'engine_classes': []}

        for engine_class_file in gtm_files['engine_classes']:
            gtm_data['engine_classes'].append(parse_engine_class_file(engine_class_file))

        print(json.dumps(gtm_data, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()

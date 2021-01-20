import xml.etree.ElementTree as ET

from core.utils import extract_zip


def get_element_text(root, tag):

    items = []
    for id_element in root.iter(tag):
        items.append(id_element.text)

    if len(items) != 1:
        # TODO: Proper logging
        print("Error: {} has {} test values".format(tag, len(items)))
    return items[0]


def parse_engine_class(content):

    engine_class = {'type': 'engine_class'}

    root = ET.fromstring(content)
    engine_class['id'] = get_element_text(root, 'id')
    engine_class['name'] = get_element_text(root, 'name')
    engine_class['speed'] = get_element_text(root, 'speed')

    return engine_class


class GTMParser:

    def __init__(self, gtm_file):
        self._gtm_file = gtm_file
        self._data = {}

        self._parse_gtm_file()

    def _parse_gtm_file(self):

        self._data = {'engine_classes': []}

        content = extract_zip(self._gtm_file)
        for item in content:
            if 'engine_classes' in item:
                self._data['engine_classes'].append(parse_engine_class(content[item]))

    def get_data(self):
        return self._data

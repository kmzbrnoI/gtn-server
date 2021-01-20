import zipfile


def extract_zip(zip_file):
    content = {}

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        content = {name: zip_ref.read(name) for name in zip_ref.namelist()}

    return content

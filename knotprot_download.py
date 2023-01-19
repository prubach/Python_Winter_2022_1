import shutil
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request
from time import time
from PIL import Image

SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?set=True&bridgeType=probab&slipknotTypes=%2B31&raw=1'
#SEARCH_STRING = 'https://knotprot.cent.uw.edu.pl/browse/?set=False&bridgeType=probab&slipknotTypes=%2B31&array=0&raw=1'
DOWNLOAD_LINK = 'https://knotprot.cent.uw.edu.pl/static/knot_data/{0}/{1}/{0}_{1}.png'

logger = logging.getLogger(__name__)

def get_proteins(search_string=SEARCH_STRING):
    req = Request(search_string, method='GET')
    proteins = []
    with urlopen(req) as resp:
        data = resp.read().decode('utf-8')
        for line in data.splitlines():
            if len(line) > 4 and not line.startswith('#'):
                cells = line.strip().split(';')
                proteins.append((cells[0], cells[1]))
    return proteins


def download_link(directory, protein):
    download_path = os.path.join(directory, os.path.basename('{0}_{1}.png'.format(protein[0],protein[1])))
    link = DOWNLOAD_LINK.format(protein[0], protein[1])
    with urlopen(link) as image, open(download_path, 'wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if download_dir.exists():
        shutil.rmtree('images', ignore_errors=True)
    if not download_dir.exists():
        download_dir.mkdir()
    return str(download_dir)


def time_it(proc, dir=None):
    t0 = time()
    proc(dir) if dir else proc()
    t = time()-t0
    print('Done {0} in {1} s.'.format(proc.__name__, round(t, 3)))


#time_it(print, 'Hello')


##########

def create_thumbnail(size, path):
    """
    Creates a thumbnail of an image with the same name as image but with
    _thumbnail appended before the extension. E.g.:

    >>> create_thumbnail((128, 128), 'image.jpg')

    A new thumbnail image is created with the name image_thumbnail.jpg

    :param size: A tuple of the width and height of the image
    :param path: The path to the image file
    :return: None
    """
    path = Path(path)
    name = path.stem + '_thumbnail' + path.suffix
    thumbnail_path = path.with_name(name)
    image = Image.open(path)
    image.thumbnail(size)
    image.save(thumbnail_path)

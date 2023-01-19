from concurrent.futures import ProcessPoolExecutor

from knotprot_download import *
from multiprocessing import Pool
from functools import partial

logger = logging.getLogger(__name__)

def run_seq(my_dir):
    i = 0
    for p in get_proteins():
        #print(p)
        i+=1
        download_link(my_dir, p)
    print(f'structures: {i}')


def run_multiprocessing(my_dir):
    proteins = get_proteins()
    download = partial(download_link, my_dir)
    with Pool(16) as pl:
        pl.map(download, proteins)

def thumbnails_seq():
    for image_path in Path('images').iterdir():
        print(image_path)
        create_thumbnail((256, 256), image_path)


def thumbnails_parallel():
    create_thumb = partial(create_thumbnail, (256, 256))
    with ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(create_thumb, Path('images').iterdir())


if __name__ == '__main__':
    setup_download_dir()
    #time_it(run_seq, 'images')
    time_it(run_multiprocessing, 'images')
    time_it(thumbnails_parallel)
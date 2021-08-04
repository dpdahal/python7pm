from os.path import dirname, basename, isfile, join
import glob

allFileLoad = glob.glob(join(dirname(__file__), '*.py'))

__all__ = [
    basename(file)[:-3] for file in allFileLoad
    if isfile(file) and not file.endswith('__init__.py')
]

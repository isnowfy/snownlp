import os
import sys
import subprocess

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    from distutils.util import convert_path

    def _find_packages(where='.', exclude=()):
        """Return a list all Python packages found within directory 'where'

        'where' should be supplied as a "cross-platform" (i.e. URL-style)
        path; it will be converted to the appropriate local path syntax.
        'exclude' is a sequence of package names to exclude; '*' can be used
        as a wildcard in the names, such that 'foo.*' will exclude all
        subpackages of 'foo' (but not 'foo' itself).
        """
        out = []
        stack = [(convert_path(where), '')]
        while stack:
            where, prefix = stack.pop(0)
            for name in os.listdir(where):
                fn = os.path.join(where, name)
                if ('.' not in name and os.path.isdir(fn) and
                        os.path.isfile(os.path.join(fn, '__init__.py'))):
                    out.append(prefix+name)
                    stack.append((fn, prefix + name + '.'))
        for pat in list(exclude)+['ez_setup', 'distribute_setup']:
            from fnmatch import fnmatchcase
            out = [item for item in out if not fnmatchcase(item, pat)]

PUBLISH_CMD = 'python setup.py register sdist upload'

if 'publish' in sys.argv:
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='snownlp',
    version='0.12.3',
    description='Python library for processing Chinese text',
    author='isnowfy',
    url='https://github.com/isnowfy/snownlp',
    packages=find_packages(exclude=('test*', )),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',

    ],
    package_data={'': ['*.md', '*.txt', '*.marshal', '*.marshal.3']},
    include_package_data=True,
)

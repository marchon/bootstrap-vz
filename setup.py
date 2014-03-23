from setuptools import setup
import os.path


def find_version(path):
	import re
	version_file = open(path).read()
	version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
	if version_match:
		return version_match.group(1)
	raise RuntimeError("Unable to find version string.")

setup(name='bootstrap-vz',
      version=find_version(os.path.join(os.path.dirname(__file__), 'bootstrapvz/__init__.py')),
      packages=['bootstrapvz', 'bootstrapvz.base'],
      entry_points={'console_scripts': ['bootstrap-vz = bootstrapvz.base:main']},
      install_requires=['termcolor >= 1.1.0',
                        'fysom >= 1.0.15',
                        'jsonschema >= 2.3.0',
                        ],

      license='Apache License, Version 2.0',
      description='Bootstrap Debian images for virtualized environments',
      long_description='''bootstrap-vz is a bootstrapping framework for Debian.
It is is specifically targeted at bootstrapping systems for virtualized environments.
bootstrap-vz runs without any user intervention and generates ready-to-boot images for
a number of virtualization platforms.
Its aim is to provide a reproducable bootstrapping process using manifests
as well as supporting a high degree of customizability through plugins.''',
      author='Anders Ingemann',
      author_email='anders@ingemann.de',
      url='http://www.python.org/sigs/distutils-sig/',
      )

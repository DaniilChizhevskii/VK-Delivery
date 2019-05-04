from distutils.core import setup
import setuptools

def read (filename):
  file = open(filename)
  text = file.read()
  file.close()
  return text

setup(
  name = 'vkdelivery',
  version = '1.0',
  description = 'Module for sending to users of Vkontakte communities.',
  long_description=read('README.rst'),
  packages=setuptools.find_packages(),
  author = 'Daniil Chizhevskij',
  author_email = 'daniilchizhevskij@gmail.com',
  url = 'https://github.com/DaniilChizhevskii/vkdelivery',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
  ],
)
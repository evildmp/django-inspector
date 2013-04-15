from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Django Inspector',
    version='0.0.1',
    author='Daniele Procida',
    author_email='daniele@vurt.org',
    packages=find_packages(), 
    include_package_data=True,
    zip_safe = False,
    license='LICENSE.txt',
    description='Inspects and reports on Django sites',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    install_requires=[
        'BeautifulSoup',
    ]
)
 

import pathlib

from setuptools import setup
from setuptools import find_packages

# The directory containing this file
CDIR = pathlib.Path(__file__).parent

# The text of the README file
#README = (CDIR / "README.md").read_text()


setup(name='COVID-19-ANALYSIS',
      version='2019.7',
      description='...',
      author='Jozef Budzinski',
      author_email='jozef.budzinski@gmail.com',
      url='https://github.com/joebud/covid-19-analyses',
#      download_url='...',
#      license='Proprietary',



#      keywords="...",
#      project_urls={
#        "Bug Tracker": "...",
#        "Documentation": "...",
#        "Source Code": "...",
#      },
  
#      install_requires=['numpy>=1.9.1',
#                        'scipy>=0.14',
#                        'six>=1.9.0',
#                        'pyyaml'],
#      extras_require={
#          'h5py': ['h5py'],
#          'visualize': ['pydot>=1.2.0'],
#          'tests': ['pytest',
#                    'pytest-pep8',
#                    'pytest-xdist',
#                    'pytest-cov',
#                    'pandas'],
#      },
#      scripts=['....py'],
      include_package_data=True, #False, # True,
      package_data={
            # If any package contains *.txt or *.rst files, include them:
            '': ['*.txt', '*.rst', '*.ini'],
            # And include any *.msg files found in the pack_1 package, too:
#            'pack_1': ['*.msg'],
      },
#      entry_points={"console_scripts": ["realpython=reader.__main__:main"]},

     




      classifiers=[
#          'Development Status :: 5 - Production/Stable',
#          'Intended Audience :: Developers',
#          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
#          'Programming Language :: Python :: 2',
#          'Programming Language :: Python :: 2.7',
#          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages(exclude=("tests.*", "tests","latest","docs","figs","bin","dumps","tex","misc",))
      )
      
      

      

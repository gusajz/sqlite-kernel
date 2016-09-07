from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='sqlite-kernel',
      version='0.1',
      description='Sqlite kernel for Jupyter',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
      ],
      keywords='sqlite jupyter sql',
      url='https://github.com/gusajz/sqlite-kernel',
      author='Gustavo Ajzenman',
      author_email='gustavoajz@gmail.com',
      license='MIT',
      packages=['sqlite_kernel'],
      install_requires=[
          'pysqlite==2.8.3',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          # 'console_scripts': ['install-sqlite-kernel=sqlite_kernel.install:main'],
      },
      include_package_data=True,
      zip_safe=False)
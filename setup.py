from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = ''.join(f.readlines())


setup(
    name='distributedapp',
    version='0.1',
    description='Service to showcase detecting termination of distributed computations using markers',
    long_description=long_description,
    author='Jan Sokol',
    author_email='sokolja2@fit.cvut.cz',
    keywords='distributed,system,termination',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],

    zip_safe=False,
)
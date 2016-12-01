from setuptools import setup
def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name = "20H",
    version = 1.0,
    description = "A simple python app based on the 20 Hour Rule",
    author = "Ganesh Kumar M",
    author_email = "ganeshkumarm.1996@gmail.com",
    license = "GPLv2",
    url = "https://github.com/GaneshmKumar/20H",
    packages = ["20H"],
    install_requires=['termcolor'],
    entry_points={
        'console_scripts':[
            '20H = 20H.20H:main'
            ]
        },
    long_description=readme(),
)

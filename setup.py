from setuptools import setup, find_packages

setup(
    name='ponchi',
    version='0.2',
    author='D00dleman',
    license='MIT',
    description='Python Telegram bot framework',
    url='https://github.com/D00dleman/ponchi'
    packages=['ponchi', 'ponchi.clear_app'],
    long_description=open('README.md').read(),
    install_requires=[
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'idna==2.10',
        'pony==0.7.14',
        'PyMySQL==1.0.1',
        'pyTelegramBotAPI==3.7.4',
        'requests==2.25.1',
        'urllib3==1.26.2',
    ]

)

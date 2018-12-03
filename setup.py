from setuptools import setup, find_packages

version = '0.0.1'
setup(
    name='selenium_boilerplate',
    version=version,
    description='Sample Python Testing Project with Selenium',
    classifiers=[
        'Intended Audience :: Automation Engineers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    author='Vignesh Jeyaraj',
    author_email='vicky.008@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'selenium>=3.14', 'page_objects=1.1.0'
    ],
)

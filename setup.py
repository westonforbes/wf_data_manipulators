from setuptools import setup, find_packages

setup(
    name='wf_data_manipulators',
    version='0.0.4',
    packages=find_packages(),
    install_requires=[
        'wf_console @ git+https://github.com/westonforbes/wf_console.git',
        'pandas',
        'pillow',
        'numpy'
    ],
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Weston Forbes',
    url='https://github.com/westonforbes/wf_data_manipulators.git',
    python_requires='>=3.11.2',
)

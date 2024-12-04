from setuptools import find_packages, setup



setup(
    name='mlproject',
    version='0.0.1'
    author='Emmanuel'
    author_email='omanoyeemmanuel@gmail.com',
    package_data=find_packages(),
    install_requires=['pandas', 'seaborn', 'numpy']
)
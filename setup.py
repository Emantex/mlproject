from setuptools import find_packages, setup


HYPEN_DOT = '-e .'
def get_requirements(filepth)->List(str):
    '''
    This function will  return a list of the requirements
    '''
    requirements=[]
    with open(filepth) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n', '')for req in requirements]

        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
            return  requirements 
          
setup(
    name='mlproject',
    version='0.0.1',
    author='Emmanuel',
    author_email='omanoyeemmanuel@gmail.com',
    package_data=find_packages(),
    install_requires=get_requirements('get_requirements')
)
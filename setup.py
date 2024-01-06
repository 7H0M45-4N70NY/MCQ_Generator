from setuptools import find_packages,setup

setup(
    name='MCQ_Generator',
    version='0.0.1',
    author='7H0M45-4NTONY',
    author_email='thomasantony14@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
from setuptools import setup, find_packages

setup(
    name='intent_chatbot',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'python-dotenv',
        'wolframalpha',
        'PyGithub'
    ],
    entry_points='''
        [console_scripts]
        intent=chatbot.intent_chatbot:chatbot
    ''',
)


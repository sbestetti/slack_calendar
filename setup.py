from setuptools import find_packages, setup

setup(
    name='calbot',
    version='0.1',
    author="Sergio Bestetti",
    author_email="sergio@bestetti.net",
    description="Google Calendar bot for Slack",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'google-auth',
        'google-auth-httplib2',        
        'google-api-python-client',
        'oauth2client'
    ],
)
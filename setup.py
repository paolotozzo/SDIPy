from distutils.core import setup

packages=[
    'sdipy',
]

requiredPackages=[]

setup(
    name='SDIPy',
    version='0.2',
    author='Charles Fracchia',
    author_email='charlesfracchia@gmail.com',
    packages=packages,
    scripts=[],
    url='',
    license='LICENSE',
    description='Python library for the Sensor Data Interoperability Protocol',
    long_description=open('README.md').read(),
    requires=requiredPackages,
    provides=packages,
)

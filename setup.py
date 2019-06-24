import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='e-simples',
    version='0.0.1',
    url='bth.com.br',
    license='Proprietary',
    maintainer='Fabio Gerasimenko',
    maintainer_email='gerasimenko2@gmail.com',
    description='BTH E-Simples',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'marshmallow',
        'requests',
        'python-dotenv'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
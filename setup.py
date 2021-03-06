from setuptools import setup, find_packages
from bootstrapform.meta import VERSION

setup(
    name='Main form for filter',
    version=str(VERSION),
    description="kkkkkk info ",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    keywords='bootstrap,django',
    author='tzangms',
    author_email='tzangms@gmail.com',
    url='http://github.com/tzangms/django-bootstrap-form',
    license='MIT',
    test_suite='runtests.runtests',
    install_requires = [
        "django>=1.5",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

from setuptools import find_packages, setup

from aldryn_search import __version__


REQUIREMENTS = [
    'lxml',
    'lxml-html-clean',
    'setuptools',
    'packaging',
    'django-appconf',
    'django-cms>=3.11,<3.12',
    'django-haystack>=3.3.0',
    'django-spurl',
    'aldryn-common>=1.0.2',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Framework :: Django',
    'Framework :: Django :: 4.2',
    'Framework :: Django CMS :: 3.11',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='aldryn-search',
    version=__version__,
    author='Benjamin Wohlwend',
    author_email='piquadrat@gmail.com',
    url='https://github.com/divio/aldryn-search',
    license='BSD',
    description='An extension to django CMS to provide multilingual Haystack indexes',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    python_requires='>=3.9',
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
)

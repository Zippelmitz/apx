#!/usr/bin/env %{__python2}
# - coding: utf-8 -
import distutils.command.install
import os
import platform
import sys

from setuptools import setup

DATADIR = os.path.join(sys.prefix, "share", "apx")
class install(distutils.command.install.install):

    def finalize_options(self):
        special_cases = ('debian', 'ubuntu')
        if (platform.system() == 'Linux' and
                platform.linux_distribution()[0].lower() in special_cases):
            # Maintain an explicit install-layout, but use deb by default
            specified_layout = getattr(self, 'install_layout', None)
            self.install_layout = specified_layout or 'deb'

        distutils.command.install.install.finalize_options(self)



setup(
    name = "apx",
    version = "0.1",
    author = "Toms Bauģis",
    author_email = "toms.baugis@gmail.com",
    description = "A playful QIX clone.",
    license = "MIT",
    keywords = "game arcade python",
    url = "https://github.com/projecthamster/apx",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
    ],


    packages=['apx', 'apx.lib'],
    scripts=['bin/apx'],
    data_files= [
        ('share/apx/icons', ['data/apx.svg']),
        ('share/fonts/04b03', ['data/04b03.ttf', 'data/04b03_LICENSE',]),
        ('data', ['data/apx.sqlite']),
        ('share/appdata', ['data/apx.appdata.xml']),
        ('share/applications', ['data/apx.desktop']),
    ],

    cmdclass={
        "install": install,
    },
)
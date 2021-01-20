# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

executables = [Executable('__main__.py',
                          targetName='Sushi.exe',
                          base='Win32GUI',
                          icon='Sushi.ico')]

excludes = []

options = {
    'build.exe': {
    'includes': [

    ]
    }
}


setup(
    name='Sushi',
    version='1.0',
    description='Sushi_salon',
    options=options,
    executables=executables,
    options=options)



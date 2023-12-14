import sys
import os
from cx_Freeze import setup, Executable

configuracao = Executable(
    script='app.py',
    icon='Home Office Simulator.ico'
)

setup(
    name='Home Office Simulator',
    version='1.0',
    description='Este programa deixa seu mouse se movendo aleatoriamente pelo tempo que você determinar',
    author='Lucas Alcoléa Oue',
    options={'build_exe': {'include_msvcr': True}},
    executables=[configuracao],
)

import sys
import os
from cx_Freeze import setup, Executable

configuracao = Executable(
    script='app.py',
    icon='Home Office Simulator.ico'
)

setup(
    name='Home Office Simulator',
    version='1.0',
    description='Este programa deixa seu mouse se movendo aleatoriamente pelo tempo que você determinar',
    author='Lucas Alcoléa Oue',
    options={'build_exe': {'include_msvcr': True}},
    executables=[configuracao],
)

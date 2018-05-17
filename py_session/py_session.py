# -*- coding: utf-8 -*-

"""Main module."""

import sys

def py_session(include_na=False):

    modules_print = []
    for module in sys.modules:
        if '.' not in module and not module.startswith('_'):
            try:
                modules_print += [f'{module:15}\t{sys.modules[module].__version__}']
            except:
                try:
                    if type(modules[module].version) is str:
                        modules_print += [f'{module:15}\t{sys.modules[module].version}']
                    else:
                        modules_print += [f'{module:15}\t{sys.modules[module].version()}']
                except:
                    try:
                        modules_print += [f'{module:15}\t{sys.modules[module].VERSION}']
                    except:
                        if include_na:
                            modules_print += [f'{module:15}\tNA']
    for a,b,c in zip(modules_print[::3], modules_print[1::3], modules_print[2::3]):
        print(f'{a:30}{b:30}{c}')

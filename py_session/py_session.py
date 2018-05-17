# -*- coding: utf-8 -*-

"""Main module."""

import sys

def py_session(include_na=False, return_list=False):

    modules_print = []
    for module in sys.modules:
        if '.' not in module and not module.startswith('_'):
            try:
                modules_print += [f'{module:20}\t{sys.modules[module].__version__}']
            except:
                try:
                    if type(modules[module].version) is str:
                        modules_print += [f'{module:20}\t{sys.modules[module].version}']
                    else:
                        modules_print += [f'{module:20}\t{sys.modules[module].version()}']
                except:
                    try:
                        modules_print += [f'{module:20}\t{sys.modules[module].VERSION}']
                    except:
                        if include_na:
                            modules_print += [f'{module:20}\tNA']
    modules_print = sorted(modules_print)
    modules_len = len(modules_print)
    print(f'{modules_len} modules found')
    col_len = modules_len // 3
    add = modules_len % 3
    if add > 0:
        col_len += 1
    for a,b,c in zip(modules_print[:col_len],
                     modules_print[col_len:2*col_len],
                     modules_print[2*col_len:]):
        print(f'{a:45}{b:45}{c:}')
    if add > 0:
        for i in range(add):
            print(f'{modules_print[(i+1)*col_len-1]:45}', end='')
    if return_list:
        return modules_print

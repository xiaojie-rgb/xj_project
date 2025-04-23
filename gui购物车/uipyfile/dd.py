import os

path_qt = os.path.abspath(r'../qtfile')

lst = os.listdir(path_qt)
path_py = os.path.abspath(r'.')

for i in lst:
    path_x = path_qt + '\\' + i
    path_y = path_py + '\\' + i.split('.')[0] + '.py'

    str1 = f'pyuic5 -x {path_x} -o {path_y}'
    print(str1)
    # os.system(str1)


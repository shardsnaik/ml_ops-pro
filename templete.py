from pathlib import Path
import os
import logging
pro_name = 'CnnClasifier'


list_of_files = [

    '.github/workflows/.gitkeep',
    f'src/{pro_name}/__init__.py',
    f'src/{pro_name}/compo/__init__.py',
    f'src/{pro_name}/utils/__init__.py',
    f'src/{pro_name}/cofig/__init__.py',
    f'src/{pro_name}/cofig/configuration.py',
    f'src/{pro_name}/pipeline/__init__.py',
    f'src/{pro_name}/entity/__init__.py',
    f'src/{pro_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requir.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',
    '.gitignore'
]



for files in list_of_files:
    files = Path(files)
    print(files)
    file_dir, file_name = os.path.split(files)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok= True)
        logging.info(f'creating directory of {file_dir} of the file name of {file_name}')

    if (not os.path.exists(files)) or (os.path.getsize == 0):
        with open(files, 'w') as f:
            pass
        logging.info(f'creating emptu file of path {files}')

    else:
        logging.info(f'{files} it already exists')
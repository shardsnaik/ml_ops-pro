import os
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from src.CnnClasifier import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from  typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) ->ConfigBox:
    '''
    Reads the yaml files and returnd

    Args: 
    paath to_yaml (str) : PAth like input 

    Raises: 
    Valueerror if any yaml file is missing

    returns : ConfigBox type

    '''
    try:
        with open(path_to_yaml) as op:
            content = yaml.safe_load(op)
            logger.info(f'yaml file {path_to_yaml} is loaded succesfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is emp ty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_dirs:list, verbose=True):
    '''
    create the list of directorres

    '''
    for path in path_to_dirs:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f'created directory at: {path}')


@ensure_annotations
def save_json(path: Path, data:dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path)->ConfigBox:
    '''
    load the json data file
    Args:
        path(pPath) to the json data
    return: ConfigBox: data as class attribute instead of dict

    '''
    with open(path) as f:
        content = json.load(f)

    logger.info(f'json file has loaded succesfully from path {path}')
    return ConfigBox(content)
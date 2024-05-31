import os
from box.exceptions import BoxValueError
import yaml
from textSummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type

    d = {"key":'value',"key1":'value1'}
    d['key'] ----------'value'
    d.key ------------- AttributeError Traceback (most recent call last)
                       Cell In[3], line 1
                       ----> 1 d.key
                        AttributeError: 'dict' object has no attribute 'key'

    from box import ConfigBox
    d2 = ConfigBox({"key":'value',"key1":'value1'})
    d2.key ---------- 'value'
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    
    def get_product(x:int, y:int) -> int:
    return x*y

    get_product(x=2, y=4) ------ 8
    get_product(x=2, y="4") ------ "44"


    from ensure import ensure_annotations

    @ensure_annotations
    def get_product(x:int, y:int) -> int:
    return x*y

    get_product(x=2, y=4) ------ 8
    get_product(x=2, y="4") ------ EnsureError: Argument y of type <class 'str'> to <function get_product at 0x00000220094AA700> does not match annotation type <class 'int'>
    
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
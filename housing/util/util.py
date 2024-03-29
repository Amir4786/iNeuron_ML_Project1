import yaml

def read_yaml_file(file_path:str)->dict:
    try:

        with open(config_file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
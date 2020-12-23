import yaml


def load_config(filename):
    """
    Load the YAML configuration for the Inferno Cop.
    :param filename: The file name of the config.
    :return: The loaded config dictionary.
    """
    with open(filename, 'r') as file:
        return yaml.full_load(file)

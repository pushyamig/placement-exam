import os
import yaml
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.dirname(os.path.abspath(__file__)) + "/.env")


def main():
    placement_exam = os.getenv('placement_exam')
    path_properties = os.getenv('path_properties')
    print(f"Path to properties {path_properties}")
    print(f"Placement exam: {placement_exam}")
    with open(path_properties, 'r') as yml_file:
        sf = yaml.load(yml_file, Loader=yaml.FullLoader)
    print(sf[placement_exam]['id'])


if __name__ == '__main__':
    main()

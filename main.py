import os
import yaml
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.dirname(os.path.abspath(__file__)) + "/.env")


def main():
    placement_exam = os.getenv('placement_exam')
    with open('properties.yaml', 'r') as yml_file:
        sf = yaml.load(yml_file, Loader=yaml.FullLoader)
    print(sf[placement_exam]['id'])


if __name__ == '__main__':
    main()

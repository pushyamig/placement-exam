import os

import pkg_resources
import yaml
from dotenv import load_dotenv
from umich_api.api_utils import ApiUtil

load_dotenv(dotenv_path=os.path.dirname(os.path.abspath(__file__)) + "/.env")


def main():
    placement_exam = os.getenv('placement_exam')
    path_properties = os.getenv('path_properties')
    path_persistence = os.getenv('path_persistence')
    print(f"Path to properties {path_properties}")
    print(f"Placement exam: {placement_exam}")
    persistance_file=f"{path_persistence}persistence_{placement_exam}.txt"
    print(f"Persistance file: {persistance_file}")
    with open(path_properties, 'r') as yml_file:
        sf = yaml.load(yml_file, Loader=yaml.FullLoader)
    print(sf['course'][placement_exam]['id'])
    client_ = sf['api']['client']
    secret_ = sf['api']['secret']
    url_ = sf['api']['url']
    print(client_)
    print(secret_)
    print(url_)
    api_json: str = pkg_resources.resource_filename(__name__, 'apis.json')
    api_handler = ApiUtil(url_, client_, secret_, api_json)
    print(api_handler.get_access_token('aa/oauth2/token','spanishplacementscores'))

    with open(f'{path_persistence}/{placement_exam}.txt') as f:
        latest_exam_date: str = f.read()
        print(latest_exam_date)


if __name__ == '__main__':
    main()

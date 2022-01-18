import shutil
import argparse
import os
import time
from distutils.dir_util import copy_tree
import json

# Configuration
config = {
    'output': 'build'
}

def read_config():
    with open('datapack.config', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split('=')
            key = line[0]
            value = line[1]
            if key == 'PACK_FORMAT':
                value = value.split(';')
            config[key.lower()] = value

def make_version(format):
    print(f'Building format {format}...')
    with open('dptemp\pack.mcmeta', 'w') as f:
        packdata = {
            "pack": {
                "pack_format": int(format),
                "description": config["description"]
            }
        }
        f.write(json.dumps(packdata))
    shutil.make_archive(f'dpetemp\{config["name"]}-{config["version"]}-pf{format}', "zip", "dptemp")
    move_to_output(f'{config["name"]}-{config["version"]}-pf{format}.zip')
    shutil.rmtree('dpetemp')

def build():
    os.mkdir('dptemp')
    copy_tree('src', 'dptemp')
    if os.path.exists('pack.png'):
        shutil.copy2('pack.png', 'dptemp')
    for format in config['pack_format']:
        make_version(format)
    shutil.rmtree('dptemp')
  

def move_to_output(file):
    if os.path.exists(f'{config["output"]}\{file}'):
        os.remove(f'{config["output"]}\{file}')
    shutil.move(f'dpetemp\{file}', config["output"])


def ready_output():
    if not os.path.exists(config["output"]):
        os.mkdir(config['output'])


def parse_args():
    parser = argparse.ArgumentParser(description='Build a new release.')
    parser.add_argument('-o', '--output', help='The output directory.')

    args = parser.parse_args()

    if not args.output:
        print(f'No output directory specified. Using config defined or default ({config["output"]}).')
    else:
        config["output"] = args.output


def main():
    read_config()
    print(f'Starting build of {config["name"]} version {config["version"]}...')
    time_start = time.time()
    parse_args()
    ready_output()
    build()
    time_end = time.time()
    print(f'Finished build in {time_end - time_start}!')


if __name__ == "__main__":
    main()
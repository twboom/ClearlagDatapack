import shutil
import argparse
import os

parser = argparse.ArgumentParser(description='Build a new release.')
parser.add_argument('-v', '--version', help='The version to build.')
parser.add_argument('-o', '--output', help='The output directory.')

args = parser.parse_args()

if not args.version:
    print('Please specify a version to build.')
    exit(1)

if not args.output:
    print('Building in this folder.')

print(f'Starting build of Clearlag with version {args.version}')
shutil.make_archive(f'Clearlag-{args.version}', "zip", "src")
print(f'Finished build')

if args.output:
    print('Moving build to desired location')
    if os.path.exists(args.output):
        os.remove(f'{args.output}\Clearlag-{args.version}.zip')
    shutil.move(f'Clearlag-{args.version}.zip', args.output)
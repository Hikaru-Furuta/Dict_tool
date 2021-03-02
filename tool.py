import argparse
from My_dict import Dict

parser = argparse.ArgumentParser('Example program')
parser.add_argument('-p','--arg1')
parser.add_argument(
    '-d',
    '--timeIndex',
    action='store_true',
    )
cmd_args = parser.parse_args()
print(cmd_args.arg1)
if cmd_args.timeIndex:
    print('Opening the dictionary......')
    Dict.dictionary()
from utils.flask import app, quick_start
from utils.db.initialize import Initializer

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='dev')
    args = parser.parse_args()
    
    qstart_ret_args = quick_start(mode=args.mode)
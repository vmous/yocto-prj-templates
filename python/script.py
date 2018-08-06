#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import sys
import traceback

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO, datefmt='%Y-%m-%d %I:%M:%S')
logger = logging.getLogger(__name__)
logger.info("Logging Configured")


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.dd_argument('-d', '--do-sth', nargs=2, metavar=('input-file','output-file'), help='does something')
    parser.add_argument('-s', '--switch', action='store_true', help='switches on functionality')
    args = parser.parse_args(args)
    return args

def main():
    args = parse_args(sys.argv[1:])

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        pass
    except (ValueError, IOError) as e:
        sys.stderr.write('%s: %s' % (type(e).__name__, e))
        print(e)
    except Exception as e: # 2.7
        # print a stack trace for unexpected errors
        sys.stderr.write('Unexpected %s:\n%s' % (type(e).__name__, traceback.format_exc()))
        print(e)

    sys.exit(1)

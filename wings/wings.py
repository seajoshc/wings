#!/usr/bin/env python3
"""
wings
Dead simple CI/CD for your AWS projects.
"""
import argparse
import os
import sys
from wings.__version__ import __version__
from wings.aws import Toolchain
from wings.validate_config import ValidateConfig


def main():
    """ Main function for wings """
    print("Starting wings...")
    args = parse_args()

    if args.up:
        config = ValidateConfig(os.getcwd() + "/wings.toml").config
        print(config)
        toolchain = Toolchain(config)
        toolchain.build_toolchain()

    print("Success!")
    sys.exit(0)


def parse_args():
    """ Setup argument parser """
    parser = argparse.ArgumentParser()

    parser.add_argument("up",
                        help="Reads a wings.toml file to create or update "
                             "CI/CD toolchains.",
                        type=str)

    parser.add_argument("-v", "--version",
                        action='version',
                        help="Prints the version of wings you are using.",
                        version="wings {}".format(__version__))

    return parser.parse_args()


if __name__ == "__main__":
    """ Your favorite wrapper's favorite wrapper """
    main()

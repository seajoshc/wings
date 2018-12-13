#!/usr/bin/env python3
"""
wings
Dead simple CI/CD for your AWS projects.
"""
import argparse
import os
import boto3
from .validate_config import ValidateConfig


def main():
    """ """
    config = ValidateConfig(os.getcwd() + "/wings.toml").config
    print(config)


if __name__ == "__main__":
    """ Your favorite wrapper's favorite wrapper """
    main()

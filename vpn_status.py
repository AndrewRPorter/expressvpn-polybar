#!/usr/bin/env python

import argparse
import re
import subprocess


def get_status():
    res = subprocess.check_output("expressvpn status".split())
    res = res.decode("utf-8")

    if "Connected to" in res:
        print("Connected")
    else:
        print("Not Connected")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--status", action="store_true")
    args = parser.parse_args()

    if args.status:
        get_status()

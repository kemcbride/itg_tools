#!/usr/bin/env python

import os
from argparse import ArgumentParser

from file_size import patch_audio_quality


def main(path):
    for song in os.listdir(path):
        patch_audio_quality('/'.join([path, song]))


if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument('path', type=str, help="")
    args = ap.parse_args()

    main(args.path)

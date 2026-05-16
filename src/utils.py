# src/utils.py

import os


def create_directories():
    folders = ['models']

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

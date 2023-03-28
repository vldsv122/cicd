import os
import argparse


argparse = argparse.ArgumentParser()
argparse.add_argument("-f", "--filter", )

def get_file_path(filename=None):
    if filename:
        return os.path.join(os.path.dirname(__file__), filename)
    return os.path.dirname(__file__)

def get_file_content(filename=None):
    if filename:
        with open(get_file_path(filename), "r") as f:
            return f.read()
    return None



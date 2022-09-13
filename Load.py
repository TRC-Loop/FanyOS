from halo import Halo
import updater
updater.updateNow()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_libs():
    spinner = Halo(text=f'{bcolors.HEADER}Loading Libraries...', spinner='line')
    spinner.start()
    import time
    import timeit
    import datetime
    import prompt_toolkit
    import rich
    import alive_progress
    import re
    import array
    import asyncio
    import base64
    import calendar
    import colorama
    import csv
    import ctypes
    import numpy
    import zipfile
    import string
    import difflib
    import textwrap
    import unicodedata
    import stringprep
    import struct
    import codecs
    import zoneinfo
    import collections
    import collections.abc
    import heapq
    import bisect
    import weakref
    import types
    import copy
    import pprint
    import reprlib
    import enum
    import grapheme
    import matplotlib
    import math
    import numbers
    import cmath
    import decimal
    import fractions
    import random
    import statistics
    import binascii
    import itertools
    import functools
    import operator
    import pathlib
    import os.path
    import os
    import sys
    import platform
    import fileinput
    import stat
    import filecmp
    import tempfile
    import glob
    import updater
    import fnmatch
    import linecache
    import shutil
    import pickle
    import copyreg
    import shelve
    import marshal
    import dbm
    import sqlite3
    import zlib
    import gzip
    import bz2
    import lzma
    import tarfile
    import configparser
    import netrc
    import plistlib
    import hashlib
    import getpass
    import json
    import hmac
    import secrets
    import io
    import argparse
    import getopt
    import socket
    import logging
    import errno
    import threading
    import concurrent
    import subprocess
    import sched
    import queue
    import contextvars
    import _thread
    import ssl
    import select
    import selectors
    import signal
    import mmap
    import email
    import mailbox
    import mimetypes
    import quopri
    import html
    import urllib
    import xml
    import webbrowser
    import wave
    import wsgiref
    import http
    import ftplib
    import poplib
    import imaplib
    import smtplib
    import uuid
    import socketserver
    import xmlrpc
    import ipaddress
    import colorsys
    import gettext
    import locale
    import turtle
    import cmd
    import shlex
    import tkinter
    import zipapp
    import venv
    import distutils
    import ensurepip
    import gc
    import inspect
    import abc
    import contextlib
    import code
    import zipimport
    import pkgutil
    import modulefinder
    import runpy
    import importlib
    import ast
    import symtable
    import keyword
    import py_compile
    import pickletools
    import requests
    import multiprocessing
    spinner.stop_and_persist(symbol=f"{bcolors.HEADER}[{bcolors.OKGREEN}OK{bcolors.HEADER}]")
  
load_libs()
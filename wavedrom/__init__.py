#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright wavedrompy contributors.
# SPDX-License-Identifier: MIT


"""Wavedrompy  is a python module and command line fully compatible with WaveDrom,
 which is originally implemented in JavaScript.
 It is useful if you want to generate wavedrom diagrams from a python environment
 or simply don't want to install the Node.js environment just to use WaveDrom as simple command line.
"""

__title__ = "wavedrompy"
__description__ = "This tool is a direct translation of original Javascript file WaveDrom.js to Python."


import argparse
import json
import yaml
import os
import sys

from .waveform import WaveDrom
from .assign import Assign
#from .version import version
from .bitfield import BitField

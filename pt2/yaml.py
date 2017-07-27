#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from pprint import pprint

with open('fruit.json') as godfather_file:
    movie = yaml.load(godfather_file, Loader=yaml.Loader)
    pprint(movie)

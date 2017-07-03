#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

with open('fruit.json') as godfather_file:
    movie = json.load(godfather_file)
    pprint(movie)

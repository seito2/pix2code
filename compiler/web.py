#!/usr/bin/env python
from __future__ import print_function
__author__ = 'Tony Beltramelli - www.tonybeltramelli.com'

import sys
import glob

from os.path import basename
from classes.Utils import *
from classes.Compiler import *

listFiles = glob.glob("../code/*.gui");

for input_file in listFiles:
    try:
        FILL_WITH_RANDOM_TEXT = True
        TEXT_PLACE_HOLDER = "[]"

        dsl_path = "assets/web-dsl-mapping.json"
        compiler = Compiler(dsl_path)


        def render_content_with_text(key, value):
            if FILL_WITH_RANDOM_TEXT:
                if key.find("btn") != -1:
                    value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text())
                elif key.find("title") != -1:
                    value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text(length_text=5, space_number=0))
                elif key.find("text") != -1:
                    value = value.replace(TEXT_PLACE_HOLDER,
                                            Utils.get_random_text(length_text=56, space_number=7, with_upper_case=False))
            return value

        file_uid = basename(input_file)[:basename(input_file).find(".")]
        path = input_file[:input_file.find(file_uid)]

        input_file_path = "{}{}.gui".format(path, file_uid)
        output_file_path = "{}{}.html".format(path, file_uid)

        print(input_file_path, output_file_path)

        compiler.compile(input_file_path, output_file_path, rendering_function=render_content_with_text)
    except:
        continue
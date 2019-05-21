#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# make commas happen / can also be used to swap commas for decimals
def commaValue(num):
    """Helper function for thousand separators"""
    return "{:,}".format(int(num)).replace(',', ',')
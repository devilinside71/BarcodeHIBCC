# -*- coding: utf-8 -*-
"""
This module deals with HIBCC barcode.
"""
# TODO Copyright info, functions, substring, length, unittest

import logging
import sys
import argparse


logger = logging.getLogger('program')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
logger_fh = logging.FileHandler('hibcc.log')

# create console handler with a higher log level
logger_ch = logging.StreamHandler()
logger_ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                      )
logger_fh.setFormatter(formatter)
logger_ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(logger_fh)
logger.addHandler(logger_ch)

# HIBCC character chart
hibcc_chart_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
    '-': 36,
    '.': 37,
    ' ': 38,
    '$': 39,
    '/': 40,
    '+': 41,
    '%': 42
}

# HIBCC reverse character chart
hibcc_reverse_chart_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K',
    21: 'L',
    22: 'M',
    23: 'N',
    24: 'O',
    25: 'P',
    26: 'Q',
    27: 'R',
    28: 'S',
    29: 'T',
    30: 'U',
    31: 'V',
    32: 'W',
    33: 'X',
    34: 'Y',
    35: 'Z',
    36: '-',
    37: '.',
    38: ' ',
    39: '$',
    40: '/',
    41: '+',
    42: '%'
}


def parse_arguments():
    """
    Parse program arguments.

    @return arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-cc', '--catalogcode', help='catalog barcode')
    parser.add_argument('-cn', '--catalognumber', help='catalog number')
    parser.add_argument('-lc', '--lotcode', help='LOT barcode')
    parser.add_argument('-ln', '--lotnumber', help='LOT number')
    parser.add_argument('-li', '--lic', help='LIC identifier')
    parser.add_argument('-um', '--unitofmeasure', help='Unit of Measure')
    parser.add_argument('-f', '--function', help='function to execute',
                        type=str, choices=['get_lic', 'check_lic_length',
                                           'check_lic_first_char',
                                           'check_code_start',
                                           'get_catalog_number',
                                           'get_unit_of_measure',
                                           'get_sum_of_digits',
                                           'calculate_checkdigit',
                                           'get_checkdigit',
                                           'create_catalog_code',
                                           'check_lot_code_start',
                                           'get_lot_number',
                                           'get_link_char_from_catalog_code',
                                           'get_link_char'
                                           ])
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase output verbosity')
    return parser.parse_args()


def execute_program():
    """Execute the program by arguments.
    """

    args = parse_arguments()
    if args.function == 'get_lic':
        res = str(get_lic(args.catalogcode))
        if args.verbose:
            print("LIC: " + res)
        else:
            print(res)
    if args.function == 'check_lic_length':
        res = str(check_lic_length(args.catalogcode))
        if args.verbose:
            print("LIC length valid: " + res)
        else:
            print(res)
    if args.function == 'check_lic_first_char':
        res = str(check_lic_first_char(args.catalogcode))
        if args.verbose:
            print("LIC first character valid: " + res)
        else:
            print(res)
    if args.function == 'check_code_start':
        res = str(check_code_start(args.catalogcode))
        if args.verbose:
            print("Barcode character valid: " + res)
        else:
            print(res)
    if args.function == 'get_catalog_number':
        res = str(get_catalog_number(args.catalogcode))
        if args.verbose:
            print("Catalog number: " + res)
        else:
            print(res)
    if args.function == 'get_unit_of_measure':
        res = str(get_unit_of_measure(args.catalogcode))
        if args.verbose:
            print("Unit of Measure: " + res)
        else:
            print(res)
    if args.function == 'get_sum_of_digits':
        res = str(get_sum_of_digits(args.catalogcode))
        if args.verbose:
            print("SUM of digits: " + res)
        else:
            print(res)
    if args.function == 'calculate_checkdigit':
        res = str(calculate_checkdigit(args.catalogcode))
        if args.verbose:
            print("Calculated CheckDigit: " + res)
        else:
            print(res)
    if args.function == 'get_checkdigit':
        res = str(get_checkdigit(args.catalogcode))
        if args.verbose:
            print("Get CheckDigit: " + res)
        else:
            print(res)
    if args.function == 'create_catalog_code':
        res = str(create_catalog_code(
            args.lic, args.catalognumber, args.unitofmeasure))
        if args.verbose:
            print("Generated catalog barcode: " + res)
        else:
            print(res)
    if args.function == 'check_lot_code_start':
        res = str(check_lot_code_start(args.lotcode))
        if args.verbose:
            print("LOT first characters valid: " + res)
        else:
            print(res)
    if args.function == 'get_lot_number':
        res = str(get_lot_number(args.lotcode, False))
        if args.verbose:
            print("Get LOT number: " + res)
        else:
            print(res)
    if args.function == 'get_link_char_from_catalog_code':
        res = str(get_link_char_from_catalog_code(args.catalogcode))
        if args.verbose:
            print("Link charcter from catalog code: " + res)
        else:
            print(res)
    if args.function == 'get_link_char':
        res = str(get_link_char(args.lotcode))
        if args.verbose:
            print("Link charcter: " + res)
        else:
            print(res)


def get_lic(code):
    """Get LIC Labeler Identification Code.

    Arguments:
        code {str} -- catalog barcode

    Returns:
        str -- LIC code
    """

    ret = code[1:5]
    return ret


def check_lic_length(code):
    """Check LIC code.

    Arguments:
        code {str} -- catalog barcode

    Returns:
        bool -- Wether LIC code length is 4
    """

    ret = False
    lic = get_lic(code)
    if len(lic) == 4:
        ret = True
    return ret


def check_lic_first_char(code):
    """Check LIC first character.

    Arguments:
        code {str} -- catalog barcode

    Returns:
        bool -- Wether LIC first character is A-Z
    """

    ret = False
    char_to_check = code[0]
    if hibcc_chart_dict[char_to_check] >= 10 and \
            hibcc_chart_dict[char_to_check] < 36:
        ret = True
    return ret


def check_code_start(code):
    """Check first character of the barcode.

    Arguments:
        code {str} -- barcode

    Returns:
        bool -- Wether first character is +
    """

    ret = False
    if code[0] == "+":
        ret = True
    return ret


def get_catalog_number(code):
    """Get catalog number.

    Arguments:
        code {str} -- catalog barcode

    Returns:
        str -- catalog number
    """
    ret = code[5:len(code)-2]
    return ret


def get_unit_of_measure(code):
    """Get unit of measure.

    Arguments:
        code {str} -- catalog barcode

    Returns:
        str -- unit of measure
    """

    lic_length = 5
    cat_length = len(get_catalog_number(code))
    ret = code[lic_length+cat_length:len(code)-1]
    return ret


def get_sum_of_digits(code):
    """Get SUM of digits.

    Arguments:
        code {str} -- barcode

    Returns:
        int -- SUM of digits according to HIBCC table
    """

    ret = 0
    code_without_checkdigit = code[:-1]
    for i in range(len(code)-1):
        ret = ret+hibcc_chart_dict[code_without_checkdigit[i:i+1]]
    return ret


def calculate_checkdigit(code):
    """Calculate the CheckDigit.

    Arguments:
        code {str} -- barcode

    Returns:
        str -- calculated CheckDigit
    """

    sum_of_digits = get_sum_of_digits(code)
    mod43 = sum_of_digits % 43
    ret = hibcc_reverse_chart_dict[mod43]
    return ret


def get_checkdigit(code):
    """Get CheckDigit.

    Arguments:
        code {str} -- barcode

    Returns:
        str -- CheckDigit
    """

    ret = ""
    ret = code[-1:]
    return ret


def create_catalog_code(lic, catalog_number, unit_of_measure="1"):
    """Create catalog barcode.

    Arguments:
        lic {str} -- LIC
        catalog_number {str} -- catalog number

    Keyword Arguments:
        unit_of_measure {str} -- Unit of Measure (default: {"1"})

    Returns:
        str -- catalog barcode
    """

    ret = ""
    ret = "+" + lic + catalog_number + unit_of_measure
    ret = ret + calculate_checkdigit(ret+"X")
    return ret


def check_lot_code_start(lot_code):
    """Check the firs characters of the LOT barcode.

    Arguments:
        lot_code {str} -- LOT barcode

    Returns:
        bool -- Wether the LOT barcode starts with +$
    """

    ret = False
    if lot_code[0:2] == "+$":
        ret = True
    return ret


def get_lot_number(lot_code, no_trailing_zeros=False):
    """Get LOT number.

    Arguments:
        lot_code {str} -- LOT barcode

    Keyword Arguments:
        no_trailing_zeros {bool} -- cut trailing zeros (default: {False})

    Returns:
        str -- LOT number
    """

    ret = lot_code[2: len(lot_code)-2]
    if no_trailing_zeros:
        ret = ret.rstrip('0')
    return ret


def get_link_char_from_catalog_code(code):
    """Get link charachter from catalog code.

    Arguments:
        code {str} -- catalog code

    Returns:
        str -- link character
    """

    return get_checkdigit(code)


def get_link_char(lot_code):
    """Get link character.

    Arguments:
        lot_code {str} -- LOT barcode

    Returns:
        str -- link character
    """

    ret = lot_code[len(lot_code)-2:len(lot_code)-1]
    return ret


if __name__ == '__main__':
    logger.debug('Start program')
    execute_program()
    logger.debug('Exit program')
    sys.exit()

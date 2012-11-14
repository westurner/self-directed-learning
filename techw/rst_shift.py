#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
ReStructuredText Utility for modifying ReStructuredText headings by the
specified shift offset.

For example::

    ==========
    Title
    ==========

    Heading 1
    =========
    Heading 2
    ---------
    Heading 3
    ~~~~~~~~~

Shifted by 1::

    Title
    ======
    Heading 1
    ----------
    Heading 2
    ~~~~~~~~~~
    Heading 3
    '''''''''

"""
import re
import optparse
import logging

RE_TITLE = re.compile(r'^([\=|\-|\~]+)\n(.*)\n^([\=|\-|\~]+)\n', re.MULTILINE)
RE_HEADING = re.compile(r'^(?:[\=|\-|\~]?)(?:[\n]?)(.*)\n^([\=|\-|\~]+)\n',
                                                                 re.MULTILINE)
STANDARD_HEADINGS = {
 0: '==',
 1: '=',
 2: '-',
 3: '~',
 4: "'",
 5: '"',
 6: '`',
 7: '^',
 8: '_',
 9: '*',
 10: '+',
 11: '#',
 12: '<',
 13: '>'}

log = logging.getLogger()

def rst_shift(input_file, shiftby):
    """

    Shift the headings of a restructuredtext document

    :param input_file: ReStructuredText file to read
    :type input_file: str
    :param shiftby: offset to shift headings by
    :type shiftby: signed int
    """

    shiftfactor = shiftby


    f = input_file # open(input_file,'r+')
    lines = f.read()


    depthcount = 0
    headings = {}
    sections = []

    # Special case for title
    title_obj = RE_TITLE.search(lines)

    (overline, title, underline) = (
            hasattr(title_obj,'groups') and title_obj.groups()
            or ('=','','='))
    #if len(overline) == len(underline):
    headings[overline[0]*2] = 0

    #print 0, title
    log.debug(title)
    #sections.append((0, '\n'.join([overline, title, underline])))

    # Extract section headings and existing section heading numbering
    for g in RE_HEADING.finditer(lines):
        (text, line) = g.groups()
        underline_char = line[0]
        depth = headings.get(underline_char)
        if not depth:
            depthcount += 1
            headings[underline_char] = depthcount

        heading_level = headings[underline_char]
        sections.append(
            (heading_level, underline_char, '\n'.join((text, line))))
        #print heading_level,
        log.debug("%s%s" % (heading_level * '   ', text))

    STD_HEADINGS = STANDARD_HEADINGS.values()

    # Expand headings with elements from STD_HEADINGS
    for char in sorted(headings.keys()):
        STD_HEADINGS.remove(char)
    for n in xrange(len(STD_HEADINGS)):
        dest = depthcount + ((((shiftby > 0) and 1 or -1)) * n)
        headings[STD_HEADINGS[n]] = dest

    # TODO
    headings_by_n = dict(
        (x[1], x[0]) for x in headings.items(),
    )

    #output = copy.copy(lines)
    output = lines

    # Perform underline replacements
    for section in sections:
        (level, char, text) = section
        newlevel = level + shiftby
        newchar = headings_by_n[newlevel]
        section, underline = text.split('\n',1)
        newtext = '\n'.join((section, underline.replace(char, newchar)))

        output = output.replace(text, newtext, 1)

    return output


import unittest
class Test_rst_shift(unittest.TestCase):
    def test_rst_shift(self):
        pass


def main():
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./%prog : args")

    prs.add_option('-i','--input-file',
                    dest='input_file',
                    action='store',
                    help='ReStructuredText file to reindent')
    prs.add_option('-s','--shiftby',
                    dest='shiftby',
                    action='store',
                    default=0,
                    help='Heading shift factor (-5, 5)')

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        exit(unittest.main())

    (opts,args) = prs.parse_args()

    if not (opts.input_file and opts.shiftby or opts.shiftby is 0):
        raise Exception("Must specify both --input-file and --shiftby")
        exit(0)

    if opts.input_file == '-':
        opts.input_file = sys.stdin
    else:
        opts.input_file = open(opts.input_file,'r+')

    # TODO?
    print( rst_shift(opts.input_file, int(opts.shiftby)) )



if __name__ == "__main__":
    main()




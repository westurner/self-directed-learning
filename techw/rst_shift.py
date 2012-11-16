#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
ReStructuredText Utility for modifying ReStructuredText headings by the
specified shift offset.

"""
import re
import optparse
import logging
from collections import namedtuple, OrderedDict
from StringIO import StringIO

RGX_TITLE = re.compile(r'^([\=|\-|\~]+)\n(.*)\n^([\=|\-|\~]+)\n', re.MULTILINE)
RGX_HEADING = re.compile(r'^(?:[\=|\-|\~]?)(?:[\n]?)(.*)\n^([\=|\-|\~]+)\n',
                                                                 re.MULTILINE)


RGX_TITLE = re.compile(r'^([\=|\-|\~]+)\n(.*)\n^([\=|\-|\~]+)\n', re.MULTILINE)
RGX_HEADING = re.compile(r'^(?:[\=|\-|\~]?)(?:[\n]?)(.*)\n^([\=|\-|\~]+)\n',
                                                                 re.MULTILINE)

STANDARD_HEADINGS = OrderedDict((
(0, '=='),
(1, '='),
(2, '-'),
(3, '~'),
(4, "'"),
(5, '"'),
(6, '`'),
(7, '^'),
(8, '_'),
(9, '*'),
(10, '+'),
(11, '#'),
(12, '<'),
(13, '>'),
))

log = logging.getLogger()

def rst_shift(input_file, shiftby, shift_title=True):
    """

    Shift the headings of a restructuredtext document

    :param input_file: ReStructuredText file to read
    :type input_file: str
    :param shiftby: offset to shift headings by
    :type shiftby: signed int
    """

    f = input_file # open(input_file,'r+')
    lines = f.read()

    depthcount = 0
    headings = OrderedDict()
    log.debug("document headings: %s" % headings)
    sections = []

    # Special case for title
    title_obj = RGX_TITLE.search(lines)

    (overline, title, underline) = ('=','','=')
    title = None
    if title_obj:
        (overline, title, underline) = title_obj.groups()
        if not len(overline) == len(underline):
            log.error( (overline, title, underline) )
            raise Exception("is this a malformed title?")
        else:
            underline_char = overline[0]*2 # Because it is a header
            headings[underline_char] = 0
            log.debug("document headings: %s" % headings)


            #print 0, title
            log.debug(title)
            text = title
            depth = 0
            log.debug("%d\t%s%s" % (depth, depth * '   ', text))
            sections.append((0, underline_char, '\n'.join([overline, title, underline])))

    # Extract section headings and existing section heading numbering

    # for each heading in the document
    for g in RGX_HEADING.finditer(lines):
        (text, line) = g.groups()
        if text in title and line == underline:
            continue # TODO
        underline_char = line[0]
        # check if this heading type is already in the document
        depth = headings.get(underline_char)
        if not depth:
            depthcount += 1
            headings[underline_char] = depthcount
            depth = depthcount
        #log.debug(depth)

        heading_level = headings[underline_char]
        sections.append(
            (heading_level, underline_char, '\n'.join((text, line))))
        #print heading_level,
        log.debug("%d\t%s%s" % (depth, heading_level * '   ', text))

    log.debug("document headings: %s" % headings)

    STD_HEADINGS = STANDARD_HEADINGS.values()

    log.debug( ' '.join(STD_HEADINGS))


    # TODO
    # Expand headings with elements from STD_HEADINGS
    #for char in sorted(headings.keys()):
    #    STD_HEADINGS.remove(char)
    # TODO
    headings_by_n = dict(
        (x[1], x[0]) for x in headings.iteritems(),
    )

    for n in xrange(len(STD_HEADINGS)):
        dest = depthcount + n # ((((shiftby > 0) and 1 or -1)) * n)
        headings[STD_HEADINGS[n]] = dest
        log.debug("document headings: %s" % headings)

    log.debug("document headings: %s" % headings)
    log.debug( ' '.join(STD_HEADINGS))
    log.debug( ' '.join(str(x) for x in headings_by_n.values()))


    # TODO

    #output = copy.copy(lines)
    output = lines

    # Perform underline replacements
    for section in sections:
        (depth, char, text) = section
        newdepth = depth + shiftby
        newchar = headings_by_n[newdepth]
        newtext = None

        section, underline = text.split('\n',1)

        # special case for title header
        if shiftby != 0:
            if depth == 0 and len(char) > 1:
                char = char[0]
                newchar = newchar[0]
            elif depth == 1 and text.startswith('\n'):
                newtext = '\n'


        newtext = newtext or '\n'.join((section, underline.replace(char, newchar)))

        log.error( (depth, newdepth, text, newtext) )
        output = output.replace(text, newtext, 1)

    return output

TestTuple = namedtuple('TestTuple', ('input','shiftkey','output',))

# (input,

_RST_TEST_INPUT_1="""
=====
Title
=====
title_content
Heading 1
=========
Heading 1.1
-----------
Heading 1.1.1
~~~~~~~~~~~~~
Heading 2
=========
"""

RST_TESTS = (
    TestTuple(_RST_TEST_INPUT_1, 0, _RST_TEST_INPUT_1),
    TestTuple(_RST_TEST_INPUT_1, 1,"""

Title
=====
title_content
Heading 1
---------
Heading 1.1
~~~~~~~~~~~
Heading 1.1.1
\"\"\"\"\"\"\"\"\"\"\"\"\"
Heading 2
---------
"""),
)

#RST_TEST_DICT = OrderedDict(
#    ((t.input,t.shiftkey), t.output) for t in RST_TESTS
#)

import itertools
def _compare_test_output(_input, _output, expected_output):
    formatstr="%-20s %-20s %-20s"

    log.error("%-20s %-20s %-20s" % ("input", "output", "expected output"))
    log.error("="*60)
    for n in itertools.izip_longest(
                _input.split('\n'),
                _output.split('\n'),
                expected_output.split('\n')):
        log.error("%-20s %-20s %-20s" % (n))


import unittest
class Test_rst_shift(unittest.TestCase):
    def test_rst_1(self):
        for test_input, shift, expected_output in RST_TESTS:
            input_ = StringIO(test_input)
            output = rst_shift(input_, shift)
            try:
                self.assertEqual(expected_output, output)
            except Exception, e:
                log.exception(e)
                log.error("# shift = %r" % shift)
                _compare_test_output(test_input, output, expected_output)
                pass
               #raise
        raise Exception()


def main():
    import optparse
    import logging
    import sys

    prs = optparse.OptionParser(
            usage="./%prog : -s <int> -i <input_file> -o <output_file>",
            description="Shift reStructuredText headings by -s")

    prs.add_option('-s','--shiftby',
                    dest='shiftby',
                    action='store',
                    default=0,
                    help='Heading shift factor (-5, 5)')
    prs.add_option('-i','--input-file',
                    dest='input_file',
                    action='store',
                    help='Input ReStructuredText file to shift headings')
    prs.add_option('-o','--output-file',
                    dest='output_file',
                    action='store',
                    default=sys.stdout,
                    help='Output file to shift headings')

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',
                    help="Show debugging output")
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',
                    help="Disable logging")
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',
                    help="Run unit tests.")

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
    elif opts.input_file is not None:
        opts.input_file = open(opts.input_file,'r+')

        opts.output_file.write(
            rst_shift(opts.input_file, int(opts.shiftby))
        )
    else:
        if args:
            log.error("Could not parse commandline arguments: %r" % args)
        prs.print_help()
        exit(1)

if __name__ == "__main__":
    main()





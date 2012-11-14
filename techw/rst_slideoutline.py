from collections import OrderedDict
from itertools import count
from pprint import pprint

import networkx

# edge types
# document -> hasSection -> Section
# item -> hasSection -> Section
# item -> hasKw -> kw
# item -> hasWord -> word


def parse_slide_outline(filename):

    g = networkx.Graph()

    items = OrderedDict()
    sectionkeys = OrderedDict()
    sections = OrderedDict()
    keywords = OrderedDict()

    keyset = count()

    indentlen = 3
    indent = ' ' * indentlen

    with file(filename) as f:
        section = None
        for i, l in enumerate(f):
            l = l.rstrip()
            if not l:
                continue
            key = keyset.next()
            items[key] = l.lstrip()
            #g.add_node(key, title=l.strip()) ...
            if l.startswith(indent):
                if l[indentlen:indentlen+indentlen] != indent:
                    section = l.strip()
                    print section
                    g.add_node(section, key=key, type='section')
                    #yield (filename, section, {'_type': 'hasSection'})
                    g.add_edge(filename, section, type='hasSection')
                    sections[section] = list()
                    sectionkeys[key] = section
                else:
                    terms = [t.strip() for t in l.split(':')]
                    kwset, heading = terms[:-1], terms[-1]
                    print kwset, heading
                    g.add_node(heading, key=key, type='heading')
                    sections[section].append( (key, kwset,heading) )
                    #yield (section, heading, {'_type': 'hasItem'})
                    g.add_edge(section, heading, type='hasItem')
                    for kw in kwset:
                        kwlist = keywords.setdefault(kw, list())
                        if kw not in g:
                            g.add_node(kw, type='key')
                        kwlist.append( (key, section, kw) )
                        #yield (heading, kw, {'_type': 'hasKw'})
                        g.add_edge(heading, kw, type='hasKW')
                        g.add_edge(section, kw, type='hasKW')

    return g

    #pprint(dict(sections))
    #pprint(dict(keywords))
    #pprint(dict(items))

g = parse_slide_outline('./slides.rst')
for e in g:
    print e

#for edge in parse_slide_outline('./slides.rst'):
#    print edge


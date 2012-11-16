
Glossary
+++++++++
.. note:: The terms listed in this :doc:`glossary`
   are listed in the :ref:`genindex`.

.. contents:
..   :class: handout

Sequence Development
--------------------

.. glossary::

   sequencing
      developing :term:`paths <path>` of :term:`edges <edge>` between
      :term:`node <vertex>` :term:`resources <resource>`.

      Often augmented with :term:`authoring tools`

   authoring
      Creating and synthesizing :term:`sequences <sequencing>`
      of :term:`resources <Resource>` like:

      * :term:`documents <Document>`
      * :term:`learning objects <Learning Object>`

   naming
      assigning unique identifiers to concepts, objects, and categories



   namespacing
      TODO

      ::

         # Dots:     path.to.resource
         # Slashes:  path/to/resource
         # Hahes:                    #url_fragment``

   tagging
      adding attribute :term:`edges <edge>` between :term:`resources
      <resource>` and tag strings, which can be :term:`namespaced
      <namespace>` :term:`URLs <URL>`.
      Tags can denote :term:`categories <category>`

      Example in :term:`JSON`
      
      .. code-block:: javascript

         {
            "url": "http://example.com/ns/products/XYZ_123",
            "title": "XYZ_123",
            "tags": ["Widgets", "XYZ_Widgets"]
         }

      Often augmented with :term:`annotation tools <Annotation Tool>`

   linking
      Adding :term:`edges <edge>` between :term:`nodes <vertex>` of 
      :term:`resources <Resource>`

      Often augmented with :term:`authoring tools`

      **software development**
      
      Bundling required :term:`resources <resource>`
      and :term:`components <component>`



   optimizing
      finding optima for making decisions that better achieve objectives

   publishing
      sharing :term:`document` and :term:`Linked Data` 
      :term:`resources <resource>` in order to benefit from
      :term:`collaborative <collaboration>` :term:`feedback`

   interfacing
      requesting and sharing :term:`resources <resource>`


Graphs
--------
.. glossary::

   Graph
      A network of :term:`vertices <vertex>` and :term:`edges <edge>`.
      May have a :term:`name <naming>` 

   Category
      TODO

   Schema
      A set of :term:`categories <category>`
      and :term:`attributes <attribute>`

      Examples:

      * :term:`XSD`
      * :term:`RDF`
      * :term:`Markup Languages <Markup Language>`

   Vertex
      A node in a :term:`graph`

   Edge
      A connection between :term:`vertices <vertex>`. Also called a
      :term:`link`.

   Path
      A sequence of :term:`edges <edge>` between :term:`vertices <vertex>`
      of a graph

   Feedback
      TODO

Web Standards
--------------
.. glossary:: 

   Resource
      TODO. An object with content, a :term:`URL`,
      and :term:`metadata`

      Examples:

      * :term:`HTML`
      * :term:`Document`
      * :term:`Web Video`

   WWW
      World Wide Web. :term:`Graph` of
      :term:`HTML` :term:`Document <document>` 
      and :term:`Resource <Resource>`
      :term:`Vertices <Vertex>` with
      :term:`URL <URL>` :term:`Edges <edge>`
      shared over :term:`HTTP`

   Web
      See: :term:`WWW`

   W3C
      `World Wide Web Consortium <http://w3c.org>`_.
      The main international standards organization for the :term:`WWW`.

   Web Standard
      TODO. Standard defined by a standards-making body such as 
      :term:`W3C`

   SGML
      Standard Generalized Markup Language

   PDF
      Portable Document Format

   URL
      Uniform Resource Locator

   URI
      Uniform Resource Indicator

   HTTP
      Hypertext Transfer Protocol. Standard :term:`request <HTTP Request>`
      /:term:`response <HTTP Response>`
      protocol for the :term:`web`.


   HTTP Request
      :term:`HTTP` Request with a type, headers, and a body

      Types:

      * GET
      * POST
      * PUT
      * DELETE

      Example:

      .. code-block:: html

         GET /ns/products/XYZ_123 HTTP/1.1
         User-Agent: browsername
         Host: example.org
         Accept: application/json

   HTTP Response
      :term:`HTTP` Response with a response code, headers, and a body

      Example Response Codes:

      * 200: OK
      * 404: Not Found
      * 500: Server Error

      Example Response:

      .. code-block:: html

         HTTP/1.1 200 OK
         Server: servername
         Content-Type: application/json
         Content-Length: 172
         Connection: keep-alive

         {"title":"Document Title", "author": ... }

      TODO:cite

   HTML
      Hyptertext Markup Language.
      
      Derived from :term:`SGML`

      Often served over :term:`HTTP`

      Example
      
      .. code-block:: html

         TODO: doctype
         <html>
            <head>
               <title>Document Title</title>
               <meta author="Document Author"/>
            </head>
            <body>
               <h1>Document Title</h1>
               <p>... Document Content ...</p>
            </body>
         </html>

   XML
      Extensible Markup Language. Derived from :term:`SGML` and
      :term:`HTML`

      Example
      
      .. code-block:: xml

         TODO: XMLNS
         <object>
            <dc:title>Document Title</dc:title>
            <dc:author>Document Author>/dc:author>
            <content>... Document Content ...</content>
            <year>2012</year>
         </object>

   XHTML
      :term:`XML`-compliant :term:`HTTP`

   Namespace
      A :term:`URL` for a set of :term:`resources` within a
      :term:`schema`.

      Examples in :term:`Turtle` syntax
      
      .. code-block:: turtle

         @prefix rdfs: http://TODO/TODO/TODO
         @prefix ex: http://example.org/ns/example/
         @prefix products: http://example.com/ns/products/

      Examples in :term:`XHTML` syntax::

         TODO

   JSON
      :term:`JavaScript` Object Notation.

      Example

      .. code-block:: javascript

         [
          { 'dc:title':    'Document Title',
            'dc:author':   'Document Author',
            'content':     '... Document Content ...',
            'year':        2012},
          {'dc:title':'Document N','content':'Hello World', 'year':2012}
         ]


   Web Hooks
      :term:`HTTP` Push Notifications   

Linked Data Science
---------------------

.. glossary::

   Data Science
      TODO



   Metadata
      Data about data: :term:`attributes <attribute>` and 
      :term:`edges <edge>`

      Examples:

      * ``dc:title`` -- Dublin Core Title Attribute
      * ``dc:author`` -- Dublin Core Author Attribute
      * ``last_modified``

   Key
      A hashable identifier for a record :term:`value`.

      Example::

         key = http://example.org/ns/products/XYZ_123

   Value
      A value stored with a :term:`key`

      Example
      
      .. code-block:: python

         database = {
            'http://example.org/ns/products/XYZ_123':   # KEY
               {
               'type':'ex:Widget',                       # VALUE
               'rdfs:label':  "Product XYZ_123"
               'ex:linksWith': [ ex:XYZ_Widgets ],
               },
         }
         database.get('http://example.org/ns/products/XYZ_123')
         database['http://example.org/ns/products/XYZ_123']

   Entity Attribute Value
      A flexible data storage pattern.

      <:term:`entity <subject>`> <:term:`attribute <predicate>`> 
      <:term:`value <value>`>

   Triple
      Data-model of :term:`RDF`

      <:term:`subject`> <:term:`predicate`> <:term:`object`>

   Subject
      :term:`URL` Subject of a triple. Also: :term:`Key` and
      :term:`Entity <subject>`

   Predicate
      :term:`URL` predicate of a triple. Also: :term:`Key`

   Object
      Object or :term:`value` of a triple.

   Attribute
      A factual assertion about a :term:`Resource`.

      A :term:`predicate` and an :term:`object` about a :term:`subject`

      Example with :term:`Triples <Triple>` in :term:`Turtle` syntax::

         @prefix rdfs: http://TODO/TODO/TODO
         @prefix ex: http://example.org/ns/example/
         @prefix products: http://example.com/ns/products/

         products:XYZ_123
            a ex:Widget ;
            ex:linksWith ex:XYZ_Widgets ;
            rdfs:label "Product XYZ_123" ;
            .

   Ontology
      A structured set of :term:`Attributes <Attribute>` and
      :term:`edges <edge>` between :term:`concepts <concept>` in a
      :term:`named graph <graph>`

   RDF
      Resource Description Framework.
      :term:`W3C` :term:`triples` metadata data-model.
      Often expressed as :term:`XML`

   Turtle
      Lightweight syntax for expressing :term:`RDF` :term:`triples`
      (:term:`.ttl <turtle>`, :term:`.n3 <n3>` )

   TriG
      Syntax extension for expressing :term:`named graphs` in
      :term:`turtle`

   Microdata
      TODO. :term:`Markup syntax <Markup Language>` for expressing 
      structured data.

   FOAF
      Friend of a Friend :term:`RDF` :term:`ontology`

   DOAP
      Description of a Project :term:`RDF` :term:`ontology`

   OEMBED
      Authoring feature for automatically identifying and
      :term:`linking` to
      :term:`resource <resource>` :term:`URLs <URL>`
      on sites that support :term:`microdata` :term:`metadata`

   Linked Data
      Data :term:`resources <Resource>` linked through the :term:`WWW` using
      :term:`structured attributes <attribute>` of various
      :term:`ontologies <ontology>`

   Linked Open Data
      :term:`Linked Data` shared as :term:`Data sets` 
      with :term:`Open License` terms

      Examples:

      * http://dbpedia.org
      *

      TODO:Cite LODCloud

Education
----------
.. glossary::


   STEM
      Science, Technology, Engineering and Mathematics

   Curriculum
      A course or courses of study required for meeting objectives

   Theory
      TODO



   Process
      TODO

   Knowledge
      TODO

   Wisdom
      TODO

Learning
----------
.. glossary::

   Online Learning
      Learning delivered over :term:`web` :term:`channels`

   Learning Object
      "Any entity, digital or non-digital, that may be used for
      learning, education, or training"
      --`IEEE 1484.12-1-2002  <http://ltsc.ieee.org/wg12/files/LOM_1484_12_1_v1_Final_Draft.pdf>`_

      A learning :term:`resource`.

   Learning Activity
      TODO

   Learning Assessment
      Documenting educational progress

   LMS
      Learning Management System.
      An application for creating and delivering courses and training.
      "Limbs"

      Examples:

      * http://blackboard.com
      * TODO: http://moodle.org
      * TODO: http://sakaiproject.org

   LCMS
      Learning Content Management System. Authoring and publishing
      workflows to support content for a :term:`Learning Management
      System <LMS>`
      
   ADL
      Advanced Distributed Learning Initiative

   SCORM
      Sharable Content Object Reference Model. Based on :term:`XML`

   CLCIMS
      Computer Learning Content Information Management System: 
      :term:`SCORM`-compliant.

   TinCan
      TinCAN API
      
      "Next Generation :term:`SCORM`"

      :term:`Web Hooks` for :term:`learning activity` metrics

   LRS
      Learning Record Store. A repository for :term:`TinCan`
      :term:`learning activity` records.

      Can integrate with an :term:`LMS` or :term:`LCMS`

   OpenCourseWare
      TODO

   MOOC
      Massive Open Online Course. Large scale :term:`distance learning`
      course offered :term:`at scale <scalability>`
      through the :term:`WWW`

      Examples:

      * :term:`Coursera`
      * :term:`EdX`

   Scalability
      TODO 

Tools
------
.. glossary::

   Browser
      An application for retrieving, presenting and traversing 
      :term:`web`
      :term:`resources <resource>`
      like :term:`HTML`
      :term:`Documents <document>`
      over :term:`HTTP`.
      
      Responsible for processing :term:`JavaScript`.

   Web Server
      Software for handling :term:`HTTP` requests over the :term:`web`
      
      Often placed in front of a :term:`Web Application Server`

   Web Application Server
      Software service for hosting web applications that serve
      :term:`resources <Resource>` over :term:`HTTP` :term:`APIs <API>`
      as content types like ``text/html``, ``application/json``,
      ``text/xml``. TODO

      Interface Standards:

      * :term:`WSGI`
      * :term:`OSGI`

   Service
      **Business Service**

      TODO 

      **Information Systems**

      A locally or remotely hosted application for solving part of a
      process.

      **API**

      An :term:`API` web service.

   API
      TODO Programming Interface. 
      
      An application that responds to a standard set of 
      :term:`requests <HTTP Request>` and
      returns a standard set of :term:`responses <HTTP Response>`

      Elements:

      * Authentication Keys
      * Authorization
      * :term:`Error Codes <HTTP Response>`
      * :term:`Resource` Schema
      * :term:`Web Service`  Definitions
     
   Repository
      A :term:`version-controlled <Version Control System>` folder of
      file :term:`resources <resource>`

   Version Control System
      System for storing changesets to a :term:`Repository`
      Also :term:`Revision Control System (RCS)`

      Examples:

      * :term:`Distributed Version Control System <DVCS>`


   DVCS
      Distributed `Version Control System`.

      Advantages:

      * Branching
      * Tagging
      * Offline

      Examples:

      * :term:`Git`
      * :term:`Mercurial`

   Git
      :term:`Version Control System`

      * TODO http://github.com/mirror/kernel
      * TODO http://

   Mercurial
      :term:`Version Control System` written in :term:`Python`

      * http://hg.python.org
      * http://hg.mozilla.org

   Version Control Service
      Hosted :term:`Version Control System` for storing
      :term:`Repositories <Repository>`

      Examples:

      * http://github.com
      * http://bitbucket.org

   Scripting Language
      Third generation programming language.

      Examples:

      * :term:`JavaScript` (:term:`.js <JavaScript>`)
      * :term:`Python` (:term:`.py <Python>`)
      * :term:`Ruby` (:term:`.rb <Ruby>`)
      * :term:`Perl` (:term:`.pl <Perl>`)

   JavaScript
      A :term:`scripting language` which can be interpreted
      client-side in a :term:`Browser`
      locally as a :term:`script`
      or server-side in a :term:`Web Application Server`.
      (:term:`.js <Javascript>`)

   Python
      A :term:`scripting language` which is compiled and/or interpreted
      locally as a :term:`script`
      or server-side in an :term:`Web Application Server`


Research Tools
-----------------



Authoring Tools
-----------------

.. glossary::

   Authoring Tools

      Examples:
      
      * :term:`Text Editor`
      * :term:`Markup Language`

   Document
      TODO. A :term:`resource <resource>` :term:`vertex <vertex>` in a 
      :term:`resource <resource>` :term:`graph <graph>` containing
      textual content often stored in a structured :term:`markup language`.

      Examples:

      * :term:`HTML` (:term:`.html <HTML>`)


   Markup Language
      Textual Markup Language for expressing
      :term:`documents <document>`
      with :term:`content`
      and :term:`presentation`.

      Examples:
         
      * :term:`ReStructuredText` (:term:`.rst <ReStructuredText>`)
      * :term:`LaTeX` (:term:`.tex <LaTeX>`)
      * :term:`BibTeX <BibTeX>`
      * :term:`PDF` (:term:`.pdf <PDF>`)
      * :term:`HTML` (:term:`.html <HTML>`)
      * :term:`XHTML` (:term:`.xhtml <XHTML>`)
      * :term:`HTML5`
      * :term:`Markdown` (:term:`.md <MarkDown>`)
      * :term:`MediaWiki Syntax <MediaWiki>`
      * :term:`JSON`
      * :term:`XML` (:term:`.xml <XML>`)
      * :term:`DocBook` (:term:`.xml <XML>`)
      * :term:`OpenDocument (OpenOffice) <ODF>` (:term:`.odf <ODF>`)
      * :term:`OpenXML (MS Word) <OpenXML>` (:term:`.docx <OpenXML>`) # TODO

   Text Editor

      Examples:

      * :term:`vim`
      * :term:`emacs`
      * :term:`gedit`
      * :term:`notepad`
      * :term:`notepad++`

   ReStructuredText
      A lightweight :term:`Markup Language`.
      Also: :term:`ReST <ReStructuredText>` and
      :term:`RST<ReStructuredText>`. (:term:`.rst <ReStructuredText>`)

      Example:

      .. code-block:: restructuredtext

         .. header:: Document Header
         .. meta::
            :description lang=en: Document Description
            :author: Document Author

         .. contents:: Table of Contents
            :depth: 1
         
         Intro
         ======
         .. note: This is a `note directive <note_directive>`_

         .. _note_directive: http://docutils.sf.net/

         Background
         -----------
         .. Document Content ...

         Glossary
         =========
         .. glossary::

            ReStructuredText
               A lightweight :term:`Markup Language`

      SeeAlso:
         * http://docutils.sf.net/docs/user/rst/demo.txt
         * http://docutils.sf.net/docs/user/demo.rst

   LaTeX
      Plaintext typesetting :term:`Markup Language`

      Example::

         TODO

   BibTeX
      Language and system for managing Bibliographic References in
      :term:`LaTeX <latex>` syntax

      .. code-block:: latex

         @techreport{this,
            author      = "Wesley {Turner}",
            title       = "Self-Directed Learning with Online Resources",
            institution = "WRD",
            year        =  2012,
            address     = "Omaha, NE, USA",
         }

   PDF
      Portable Document Format

   rst2pdf
      :term:`ReStructuredText` :term:`PDF` publisher.

      Output formats:

      * :term:`PDF`

   Sphinx
      :term:`RestructuredText` documentation publisher.

      Output Formats:
      
      * :term:`HTML`
      * :term:`JSON`
      * :term:`PDF`
      * :term:`LaTeX`

      Examples:

      * http://docs.python.org
      * http://packages.python.org
      * http://readthedocs.org
      * http://sphinxdoc.org

      TODO:cite

Review Tools
--------------

.. glossary::

   

UI/UX Design
--------------
.. glossary::

   Interface
      TODO

   UI
      User Interface

   UX
      User Experience

Cloud
-------
.. glossary::

   Cloud
      TODO

   Grid
      TODO

   Stack
      TODO

   Distributed Computing
      TODO 


Collaboration Engineering
---------------------------
.. glossary::

   Collaboration
      working together to create, share, and improve
      :term:`resources <resource>`

   Collaboration Engineering

      TODO

   Six Patterns of Collaboration
      1. :term:`Generate`: Fewer to more concepts
      2. :term:`Reduce`: Many concepts -> focus
      3. :term:`Clarify`: Less -> More Shared Understanding
      4. :term:`Organize`:
      5. :term:`Evaluate`: Less -> More Value Understanding
      6. :term:`Build Consensus`: Less -> More Willingness to Commit

      TODO:Cite

   Generate
      Fewer to more concepts.

      :term:`Six Patterns of Collaboration` #1

   Reduce
      Many concepts -> focus

      :term:`Six Patterns of Collaboration` #2

   Clarify
      Less -> More Shared Understanding
      
      :term:`Six Patterns of Collaboration` #3

   Organize
      TODO

      :term:`Six Patterns of Collaboration` #4

   Evaluate
      Less -> More Value Understanding

      :term:`Six Patterns of Collaboration` #5

   Build Consensus
      Less -> More Willingness to Commit

      :term:`Six Patterns of Collaboration` #6


   Seven Layer Model
      1. :term:`Goals <goal>`
      2. :term:`Products <product>`
      3. :term:`Activities <activity>`
      4. :term:`Patterns <pattern>`
      5. :term:`Techniques <technique>`
      6. :term:`Tools <tool>`
      7. :term:`Scripts <script>`

   Goal
      TODO

   Product
      TODO

   Activity
      TODO
      See :term:`Learning Activity`

   Pattern
      TODO

   Technique
      TODO

   Tool
      TODO

   Script
      TODO

   Comparison Scheme for Collaborative Technology
      * :term:`Core Functionality`
      * :term:`Access Controls`
      * :term:`Alerts/Interrupts`
      * :term:`Content`
      * :term:`Actions`
      * :term:`Synchronicity`
      * :term:`Identifiability`
      * :term:`Relationships`
      * :term:`Persistence`

   Core Functionality
      TODO

   Access Controls
      TODO

   Alerts/Interrupts
      TODO

   Content
      TODO

   Actions
      TODO

      See also: :term:`activities <activity>`

   Synchronicity
      TODO

   Identifiability
      TODO

   Relationships
      TODO

   Persistence
      TODO

   Creative Process
      * :term:`Problem Identification`
      * :term:`Information Search`
      * :term:`Idea/Solution Generation`
      * :term:`Idea/Solution Evaluation and Selection`
      * :term:`Implementation Planning`

   Problem Identification
      TODO

   Information Search
      TODO

   Idea/Solution Generation
      TODO

   Idea/Solution Evaluation and Selection
      TODO

   Implementation Planning
      TODO

   Goal Attainment Paradigm

      * Understand Problem
      * Develop alternate solutions
      * Evaluate solutions
      * Make choices
      * Make plans
      * Take action
      * Review

   Six Sigma
      TODO

   DMAIC
      :term:`Six Sigma` process

      * Define
      * Measure
      * Analyze
      * Implement
      * Control

   Define
      TODO

   Measure
      TODO

   Analyze
      TODO

   Implement
      TODO

   Control
      TODO


   Feature Matrix
      TODO

      ::
    
         Feature:
            Label
            Description
            Value

         Choice:
            Label
            Description
            {Version}

         Choice-Feature:
            Feature
            Choice
            --
            Score
            Reason
            Reference URIs
            Cost
            Cost URIs

         Display Algorithm:
            for f in sorted(features):
               print(feature)
               for c in sorted(choices):
                     print(choice_features((feature,choice)))

      .. note:: Categorically enumerated heat map/contour plot
         with combinatorially optimized feature islands

      .. note:: max-flow algorithms



TODO:cite

Index
-------
.. note:: These terms are listed in the :ref:`Index <genindex>`.






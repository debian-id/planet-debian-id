#!/usr/bin/env python

import unittest
from planet.foaf import foaf2config
from ConfigParser import ConfigParser

blogroll = 'http://journal.dajobe.org/journal/2003/07/semblogs/bloggers.rdf'
testfeed = "http://dannyayers.com/feed/rdf"
test_foaf_document = '''
<rdf:RDF
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:rss="http://purl.org/rss/1.0/"
  xmlns:dc="http://purl.org/dc/elements/1.1/">

<foaf:Agent rdf:nodeID="id2245354"> 
<foaf:name>Danny Ayers</foaf:name> 
<rdf:type rdf:resource="http://xmlns.com/foaf/0.1/Person"/> 
<foaf:weblog> 
<foaf:Document rdf:about="http://dannyayers.com/"> 
<dc:title>Raw Blog by Danny Ayers</dc:title> 
<rdfs:seeAlso> 
<rss:channel rdf:about="http://dannyayers.com/feed/rdf"> 
<foaf:maker rdf:nodeID="id2245354"/> 
<foaf:topic rdf:resource="http://www.w3.org/2001/sw/"/> 
<foaf:topic rdf:resource="http://www.w3.org/RDF/"/> 
</rss:channel> 
</rdfs:seeAlso> 
</foaf:Document> 
</foaf:weblog> 
<foaf:interest rdf:resource="http://www.w3.org/2001/sw/"/> 
<foaf:interest rdf:resource="http://www.w3.org/RDF/"/> 
</foaf:Agent> 

</rdf:RDF> 
'''.strip()

class FoafTest(unittest.TestCase):
    """
    Test the foaf2config function
    """

    def setUp(self):
        self.config = ConfigParser()
        self.config.add_section(blogroll)

    #
    # Tests
    #

    def test_foaf_document(self):
        foaf2config(test_foaf_document, self.config)
        self.assertEqual('Danny Ayers', self.config.get(testfeed, 'name'))

    def test_no_foaf_name(self):
        test = test_foaf_document.replace('foaf:name','foaf:title')
        foaf2config(test, self.config)
        self.assertEqual('Raw Blog by Danny Ayers',
           self.config.get(testfeed, 'name'))

    def test_no_weblog(self):
        test = test_foaf_document.replace('rdfs:seeAlso','rdfs:seealso')
        foaf2config(test, self.config)
        self.assertFalse(self.config.has_section(testfeed))

    def test_invalid_xml_before(self):
        test = '\n<?xml version="1.0" encoding="UTF-8"?>' + test_foaf_document
        foaf2config(test, self.config)
        self.assertFalse(self.config.has_section(testfeed))

    def test_invalid_xml_after(self):
        test = test_foaf_document.strip()[:-1]
        foaf2config(test, self.config)
        self.assertEqual('Danny Ayers', self.config.get(testfeed, 'name'))

# these tests only make sense if libRDF is installed
try:
    import RDF
except:
    for key in FoafTest.__dict__.keys():
        if key.startswith('test_'): delattr(FoafTest, key)

if __name__ == '__main__':
    unittest.main()

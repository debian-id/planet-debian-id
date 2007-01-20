import string

try:
    frozenset
except NameError:
    # Import from the sets module for python 2.3
    from sets import Set as set
    from sets import ImmutableSet as frozenset

EOF = None

contentModelFlags = {
    "PCDATA":0,
    "RCDATA":1,
    "CDATA":2,
    "PLAINTEXT":3
}

scopingElements = frozenset((
    "button",
    "caption",
    "html",
    "marquee",
    "object",
    "table",
    "td",
    "th"
))

formattingElements = frozenset((
    "a",
    "b",
    "big",
    "em",
    "font",
    "i",
    "nobr",
    "s",
    "small",
    "strike",
    "strong",
    "tt",
    "u"
))

specialElements = frozenset((
    "address",
    "area",
    "base",
    "basefont",
    "bgsound",
    "blockquote",
    "body",
    "br",
    "center",
    "col",
    "colgroup",
    "dd",
    "dir",
    "div",
    "dl",
    "dt",
    "embed",
    "fieldset",
    "form",
    "frame",
    "frameset",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "head",
    "hr",
    "iframe",
    "image",
    "img",
    "input",
    "isindex",
    "li",
    "link",
    "listing",
    "menu",
    "meta",
    "noembed",
    "noframes",
    "noscript",
    "ol",
    "optgroup",
    "option",
    "p",
    "param",
    "plaintext",
    "pre",
    "script",
    "select",
    "spacer",
    "style",
    "tbody",
    "textarea",
    "tfoot",
    "thead",
    "title",
    "tr",
    "ul",
    "wbr"
))

spaceCharacters = frozenset((
    u"\t",
    u"\n",
    u"\u000B",
    u"\u000C",
    u" "
))

tableInsertModeElements = frozenset((
    "table",
    "tbody",
    "tfoot", 
    "thead", 
    "tr"
))

asciiLowercase = frozenset(string.ascii_lowercase)
asciiLetters = frozenset(string.ascii_letters)
digits = frozenset(string.digits)
hexDigits = frozenset(string.hexdigits)

asciiUpper2Lower = dict([(ord(c),ord(c.lower()))
    for c in string.ascii_uppercase])

# Heading elements need to be ordered 
headingElements = (
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6"
)

# XXX What about event-source and command?
voidElements = frozenset((
    "base",
    "link",
    "meta",
    "hr",
    "br",
    "img",
    "embed",
    "param",
    "area",
    "col",
    "input"
))

# entitiesWindows1252 has to be _ordered_ and needs to have an index. It
# therefore can't be a frozenset.
entitiesWindows1252 = (
    8364,  # 0x80  0x20AC  EURO SIGN
    65533, # 0x81          UNDEFINED
    8218,  # 0x82  0x201A  SINGLE LOW-9 QUOTATION MARK
    402,   # 0x83  0x0192  LATIN SMALL LETTER F WITH HOOK
    8222,  # 0x84  0x201E  DOUBLE LOW-9 QUOTATION MARK
    8230,  # 0x85  0x2026  HORIZONTAL ELLIPSIS
    8224,  # 0x86  0x2020  DAGGER
    8225,  # 0x87  0x2021  DOUBLE DAGGER
    710,   # 0x88  0x02C6  MODIFIER LETTER CIRCUMFLEX ACCENT
    8240,  # 0x89  0x2030  PER MILLE SIGN
    352,   # 0x8A  0x0160  LATIN CAPITAL LETTER S WITH CARON
    8249,  # 0x8B  0x2039  SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    338,   # 0x8C  0x0152  LATIN CAPITAL LIGATURE OE
    65533, # 0x8D          UNDEFINED
    381,   # 0x8E  0x017D  LATIN CAPITAL LETTER Z WITH CARON
    65533, # 0x8F          UNDEFINED
    65533, # 0x90          UNDEFINED
    8216,  # 0x91  0x2018  LEFT SINGLE QUOTATION MARK
    8217,  # 0x92  0x2019  RIGHT SINGLE QUOTATION MARK
    8220,  # 0x93  0x201C  LEFT DOUBLE QUOTATION MARK
    8221,  # 0x94  0x201D  RIGHT DOUBLE QUOTATION MARK
    8226,  # 0x95  0x2022  BULLET
    8211,  # 0x96  0x2013  EN DASH
    8212,  # 0x97  0x2014  EM DASH
    732,   # 0x98  0x02DC  SMALL TILDE
    8482,  # 0x99  0x2122  TRADE MARK SIGN
    353,   # 0x9A  0x0161  LATIN SMALL LETTER S WITH CARON
    8250,  # 0x9B  0x203A  SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    339,   # 0x9C  0x0153  LATIN SMALL LIGATURE OE
    65533, # 0x9D          UNDEFINED
    382,   # 0x9E  0x017E  LATIN SMALL LETTER Z WITH CARON
    376    # 0x9F  0x0178  LATIN CAPITAL LETTER Y WITH DIAERESIS
)

entities = {
    "AElig": u"\u00C6",
    "Aacute": u"\u00C1",
    "Acirc": u"\u00C2",
    "Agrave": u"\u00C0",
    "Alpha": u"\u0391",
    "Aring": u"\u00C5",
    "Atilde": u"\u00C3",
    "Auml": u"\u00C4",
    "Beta": u"\u0392",
    "Ccedil": u"\u00C7",
    "Chi": u"\u03A7",
    "Dagger": u"\u2021",
    "Delta": u"\u0394",
    "ETH": u"\u00D0",
    "Eacute": u"\u00C9",
    "Ecirc": u"\u00CA",
    "Egrave": u"\u00C8",
    "Epsilon": u"\u0395",
    "Eta": u"\u0397",
    "Euml": u"\u00CB",
    "Gamma": u"\u0393",
    "Iacute": u"\u00CD",
    "Icirc": u"\u00CE",
    "Igrave": u"\u00CC",
    "Iota": u"\u0399",
    "Iuml": u"\u00CF",
    "Kappa": u"\u039A",
    "Lambda": u"\u039B",
    "Mu": u"\u039C",
    "Ntilde": u"\u00D1",
    "Nu": u"\u039D",
    "OElig": u"\u0152",
    "Oacute": u"\u00D3",
    "Ocirc": u"\u00D4",
    "Ograve": u"\u00D2",
    "Omega": u"\u03A9",
    "Omicron": u"\u039F",
    "Oslash": u"\u00D8",
    "Otilde": u"\u00D5",
    "Ouml": u"\u00D6",
    "Phi": u"\u03A6",
    "Pi": u"\u03A0",
    "Prime": u"\u2033",
    "Psi": u"\u03A8",
    "Rho": u"\u03A1",
    "Scaron": u"\u0160",
    "Sigma": u"\u03A3",
    "THORN": u"\u00DE",
    "Tau": u"\u03A4",
    "Theta": u"\u0398",
    "Uacute": u"\u00DA",
    "Ucirc": u"\u00DB",
    "Ugrave": u"\u00D9",
    "Upsilon": u"\u03A5",
    "Uuml": u"\u00DC",
    "Xi": u"\u039E",
    "Yacute": u"\u00DD",
    "Yuml": u"\u0178",
    "Zeta": u"\u0396",
    "aacute": u"\u00E1",
    "acirc": u"\u00E2",
    "acute": u"\u00B4",
    "aelig": u"\u00E6",
    "agrave": u"\u00E0",
    "alefsym": u"\u2135",
    "alpha": u"\u03B1",
    "amp": u"\u0026",
    "AMP": u"\u0026",
    "and": u"\u2227",
    "ang": u"\u2220",
    "apos": u"\u0027",
    "aring": u"\u00E5",
    "asymp": u"\u2248",
    "atilde": u"\u00E3",
    "auml": u"\u00E4",
    "bdquo": u"\u201E",
    "beta": u"\u03B2",
    "brvbar": u"\u00A6",
    "bull": u"\u2022",
    "cap": u"\u2229",
    "ccedil": u"\u00E7",
    "cedil": u"\u00B8",
    "cent": u"\u00A2",
    "chi": u"\u03C7",
    "circ": u"\u02C6",
    "clubs": u"\u2663",
    "cong": u"\u2245",
    "copy": u"\u00A9",
    "COPY": u"\u00A9",
    "crarr": u"\u21B5",
    "cup": u"\u222A",
    "curren": u"\u00A4",
    "dArr": u"\u21D3",
    "dagger": u"\u2020",
    "darr": u"\u2193",
    "deg": u"\u00B0",
    "delta": u"\u03B4",
    "diams": u"\u2666",
    "divide": u"\u00F7",
    "eacute": u"\u00E9",
    "ecirc": u"\u00EA",
    "egrave": u"\u00E8",
    "empty": u"\u2205",
    "emsp": u"\u2003",
    "ensp": u"\u2002",
    "epsilon": u"\u03B5",
    "equiv": u"\u2261",
    "eta": u"\u03B7",
    "eth": u"\u00F0",
    "euml": u"\u00EB",
    "euro": u"\u20AC",
    "exist": u"\u2203",
    "fnof": u"\u0192",
    "forall": u"\u2200",
    "frac12": u"\u00BD",
    "frac14": u"\u00BC",
    "frac34": u"\u00BE",
    "frasl": u"\u2044",
    "gamma": u"\u03B3",
    "ge": u"\u2265",
    "gt": u"\u003E",
    "GT": u"\u003E",
    "hArr": u"\u21D4",
    "harr": u"\u2194",
    "hearts": u"\u2665",
    "hellip": u"\u2026",
    "iacute": u"\u00ED",
    "icirc": u"\u00EE",
    "iexcl": u"\u00A1",
    "igrave": u"\u00EC",
    "image": u"\u2111",
    "infin": u"\u221E",
    "int": u"\u222B",
    "iota": u"\u03B9",
    "iquest": u"\u00BF",
    "isin": u"\u2208",
    "iuml": u"\u00EF",
    "kappa": u"\u03BA",
    "lArr": u"\u21D0",
    "lambda": u"\u03BB",
    "lang": u"\u2329",
    "laquo": u"\u00AB",
    "larr": u"\u2190",
    "lceil": u"\u2308",
    "ldquo": u"\u201C",
    "le": u"\u2264",
    "lfloor": u"\u230A",
    "lowast": u"\u2217",
    "loz": u"\u25CA",
    "lrm": u"\u200E",
    "lsaquo": u"\u2039",
    "lsquo": u"\u2018",
    "lt": u"\u003C",
    "LT": u"\u003C",
    "macr": u"\u00AF",
    "mdash": u"\u2014",
    "micro": u"\u00B5",
    "middot": u"\u00B7",
    "minus": u"\u2212",
    "mu": u"\u03BC",
    "nabla": u"\u2207",
    "nbsp": u"\u00A0",
    "ndash": u"\u2013",
    "ne": u"\u2260",
    "ni": u"\u220B",
    "not": u"\u00AC",
    "notin": u"\u2209",
    "nsub": u"\u2284",
    "ntilde": u"\u00F1",
    "nu": u"\u03BD",
    "oacute": u"\u00F3",
    "ocirc": u"\u00F4",
    "oelig": u"\u0153",
    "ograve": u"\u00F2",
    "oline": u"\u203E",
    "omega": u"\u03C9",
    "omicron": u"\u03BF",
    "oplus": u"\u2295",
    "or": u"\u2228",
    "ordf": u"\u00AA",
    "ordm": u"\u00BA",
    "oslash": u"\u00F8",
    "otilde": u"\u00F5",
    "otimes": u"\u2297",
    "ouml": u"\u00F6",
    "para": u"\u00B6",
    "part": u"\u2202",
    "permil": u"\u2030",
    "perp": u"\u22A5",
    "phi": u"\u03C6",
    "pi": u"\u03C0",
    "piv": u"\u03D6",
    "plusmn": u"\u00B1",
    "pound": u"\u00A3",
    "prime": u"\u2032",
    "prod": u"\u220F",
    "prop": u"\u221D",
    "psi": u"\u03C8",
    "quot": u"\u0022",
    "QUOT": u"\u0022",
    "rArr": u"\u21D2",
    "radic": u"\u221A",
    "rang": u"\u232A",
    "raquo": u"\u00BB",
    "rarr": u"\u2192",
    "rceil": u"\u2309",
    "rdquo": u"\u201D",
    "real": u"\u211C",
    "reg": u"\u00AE",
    "REG": u"\u00AE",
    "rfloor": u"\u230B",
    "rho": u"\u03C1",
    "rlm": u"\u200F",
    "rsaquo": u"\u203A",
    "rsquo": u"\u2019",
    "sbquo": u"\u201A",
    "scaron": u"\u0161",
    "sdot": u"\u22C5",
    "sect": u"\u00A7",
    "shy": u"\u00AD",
    "sigma": u"\u03C3",
    "sigmaf": u"\u03C2",
    "sim": u"\u223C",
    "spades": u"\u2660",
    "sub": u"\u2282",
    "sube": u"\u2286",
    "sum": u"\u2211",
    "sup": u"\u2283",
    "sup1": u"\u00B9",
    "sup2": u"\u00B2",
    "sup3": u"\u00B3",
    "supe": u"\u2287",
    "szlig": u"\u00DF",
    "tau": u"\u03C4",
    "there4": u"\u2234",
    "theta": u"\u03B8",
    "thetasym": u"\u03D1",
    "thinsp": u"\u2009",
    "thorn": u"\u00FE",
    "tilde": u"\u02DC",
    "times": u"\u00D7",
    "trade": u"\u2122",
    "uArr": u"\u21D1",
    "uacute": u"\u00FA",
    "uarr": u"\u2191",
    "ucirc": u"\u00FB",
    "ugrave": u"\u00F9",
    "uml": u"\u00A8",
    "upsih": u"\u03D2",
    "upsilon": u"\u03C5",
    "uuml": u"\u00FC",
    "weierp": u"\u2118",
    "xi": u"\u03BE",
    "yacute": u"\u00FD",
    "yen": u"\u00A5",
    "yuml": u"\u00FF",
    "zeta": u"\u03B6",
    "zwj": u"\u200D",
    "zwnj": u"\u200C"
}
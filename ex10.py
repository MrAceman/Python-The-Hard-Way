tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

escape_sequences = """
\a \\a ASCII bell (BEL)
\b \\b ASCII backspace (BS)
\f \\f ASCII formfeed (FF)
\n \\n ASCII linefeed (LF)
\N{name} \\N{name} Character named name in the Unicode database (Unicode only)
\r \\r ASCII carriage return (CR)
\t \\t ASCII horizontal tab (TAB)
\uxxxx \\uxxxx Character with 16-bit hex value xxxx (Unicode only)
\Uxxxxxxxx \\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only)
\v \\v ASCII vertical tab (VT)
\000 \\000 Character with octal value 00
\\xhh Chacter with hex value hh
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print escape_sequences

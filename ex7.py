print "Mary had a little lamb." #This prints the line in quotes.
print "Its fleece was white as %s." % 'snow' #This prints the line in quotes and replaces the %s with the first string available... in this case, snow
print "And everywhere that Mary went." #This prints the line in quotes
print "." * 10 # what'd that do? #This prints the . character 10 times

end1 = "C" #The following 12 lines assign the string value to the variable
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happs
print end1 + end2 + end3 + end4 + end5 + end6, #This concats variables 1 through 6.  The comma (,) adds a space and continues on the same line versus doing a line break.
print end7 + end8 + end9 + end10 + end11 + end12 #This concats variables 7 through 12.

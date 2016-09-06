#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import glob

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    filenames = glob.glob("*.html")

  # +++your code here+++
      
    for files in filenames:
        finallist = []
        f = open(files,'r')
        
        for lines in f:
            yearmatch = re.search(r'(Popularity in) (\d\d\d\d)',lines)
            ranknamematch = re.search(r'(<tr align="right"><td>)(\d)(</td><td>)(\w+)(</td><td>)(\w+)(</td>)',lines)
            if yearmatch:
    #            print(yearmatch.group(2))
                finallist.append(yearmatch.group(2))
            if ranknamematch:   
    #            print(ranknamematch.group(2)+" "+ranknamematch.group(4)+" "+ranknamematch.group(6))
                finallist.append(ranknamematch.group(4)+" "+ranknamematch.group(2))
            
            
    #        if ranknamematch.group(4) in hashtab.keys():
    #            hashtab[ranknamematch.group(4)] = hashtab[ranknamematch.group(4)] + 1
    #        else:
    #            hashtab[ranknamematch.group(4)] = 1
    #    
                
        if yearmatch:
            print(yearmatch.group())
            
            
        print(sorted(finallist))


def main():
    filename = sys.argv[2]
    print(filename)
    extract_names(filename)
    
'''
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
'''
if __name__ == '__main__':
  main()

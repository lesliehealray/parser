#!/usr/bin/env python
# allows ./ name of file instead of writing python. So, ./pmlparser.py
#commonly used with file and directory paths
import os
#To inspect the arguments when we run the script
import sys

from bs4 import BeautifulSoup

#main execution/entry point for independent scripts
if __name__ == "__main__":
    # used debugger for interactive programming.
    # import ipdb;ipdb.set_trace()

    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            #the with opens the file and assigns it to the variable f
            with open(path, "rb") as f:
                # Don't add head/body tags if they aren't present.
                # Default parser is the best available on the system.
                # 3 types lxml, html5lib, built in html parser.
                # Specify parser
                soup = BeautifulSoup(f, 'html.parser')
            # get all PML elements and iterate on them
            for tag in soup.find_all('pml'):
                # had to iterate through in this manner to preserve child tags
                # as strings
                code_snippet = ''.join([str(x) for x in tag.contents])
                lines = code_snippet.splitlines()
                normalized_lines = []
                dedent = 0
                # Iterate and remove ws prefix from each line
                for line in lines:
                    if line:
                        if not dedent:
                            dedent = len(line) - len(line.lstrip())
                        # slice the extra ws, if any
                        line = line[dedent:]
                        normalized_lines.append(line)

                # Construct executable code snippet
                code_snippet = '\n'.join(normalized_lines)
                code = compile(code_snippet, '<string>', 'exec')
                exec code

                replacement_tag = BeautifulSoup(pml, 'html.parser')
                tag.replace_with(replacement_tag)

            print soup
        else:
            print "Supplied path does not exist"
    else:
        print "Please supply a path to a file"

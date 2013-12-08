#!/usr/bin/env python

import os
import sys


from bs4 import BeautifulSoup
import ipdb;ipdb.set_trace()

def check_args(sys_args):
    if len(sys_args) > 1:
        path = sys_args[1]
        if not os.path.exists(path):
            print 'Supplied path does not exist'
        else:
            return path
    else:
        print "Please supply a path to a file"
        return None

def parse_html(path):
    with open(path, "rb") as f:
        soup = BeautifulSoup(f, 'html.parser')
    for tag in soup.find_all('pml'):
        code_snippet = ''.join([str(x) for x in tag.contents])
        lines = code_snippet.splitlines()
        normalized_lines = []
        dedent = 0
        for line in lines:
            if line:
                if not dedent:
                    dedent = len(line) - len(line.lstrip())
                line = line[dedent:]
                normalized_lines.append(line)
        code_snippet = '\n'.join(normalized_lines)
        code = compile(code_snippet, '<string>', 'exec')
        exec code

        replacement_tag = BeautifulSoup(pml, 'html.parser')
        tag.replace_with(replacement_tag)

    return soup


if __name__ == "__main__":
    path = check_args(sys.argv)
    soup = parse_html(path)
    print soup


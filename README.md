Instructions:


Install Beautiful Soup 4 with pip install or easy install.

easy_install beautifulsoup4
pip install beautifulsoup4

To execute the script you must provide a path to the html file. 
python pmlparser.py /path/to/test.html

Assumptions:
The first arg is a path to a file on the local file system.
Parser must handle invalid html since the example doesn't provide proper html formatting (head, body).

The final variable from each PML snippet is the substitution variable. 
I had to have a consistent way to make the substitution value available post code snippet compilation.

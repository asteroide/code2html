#!/usr/bin/env python3

import sys
import os
from jinja2 import Template

DIR = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]))
ROOT_DIR = os.path.dirname(DIR)
TEMPLATE = """<span class="NameHighlights" onMouseOver="javascript:this.className='NameHighlightsHover'" """ +\
           """onMouseOut="javascript:this.className='NameHighlights'"><a class="button" href="#">#info</a>""" + \
           """<div class="popup">{}</div></span>"""


def code2html(raw_code):
    output = ""
    for line in raw_code.splitlines():
        if "##" in line:
            index = line.index("##")
            comment = line[index+3:]
            line = line[:index-1] + TEMPLATE.format(comment)
        output += line + "\n"
    output += "\n\n\n\n\n"
    return output


def main():
    template = Template(open(os.path.join(ROOT_DIR, "templates", "base.html")).read())
    for filename in sys.argv[1:]:
        html_code = code2html(open(filename).read())
        output = template.render(
            title="Exemple de code",
            code=html_code,
            language="python",
        )
        open(filename+".html", "wt").write(output)
        print("Writing {}".format(filename+".html"))

if __name__ == "__main__":
    main()

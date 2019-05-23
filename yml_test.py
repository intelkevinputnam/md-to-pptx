import yaml
import markdown

from docutils.core import publish_doctree, publish_from_doctree
import urllib
from bs4 import BeautifulSoup

with open("testing.yml", 'r') as stream:
    try:
        yamlObject = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

html = """
<html>
  <head>
    <style>
        body {
            font-family: arial, sans-serif;
        }
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }
        td, th {
            border: 1px solid #000000;
            text-align: center;
            padding: 8px;
        }
        tr:nth-child(even) {
            background-color: #dddddd;
        }
    </style>
  </head>
  <body>"""

if 'md' in yamlObject['additional_content']:
    html += markdown.markdown(yamlObject['additional_content']['md'])

if 'rst' in yamlObject['additional_content']:
    rstContent = yamlObject['additional_content']['rst']
    tree = publish_doctree(rstContent)
    htmlOutput = publish_from_doctree(tree, writer_name='html').decode()
    soup = BeautifulSoup(htmlOutput, features='lxml')
    body = soup.find('body')
    htmlOutput = body.findChildren()
    html += str(htmlOutput[0])


html += """  </body>
</html>""" 

with open("testing.html", 'w') as f:
    f.write(html)
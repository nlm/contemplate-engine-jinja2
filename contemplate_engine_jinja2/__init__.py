from __future__ import absolute_import, print_function
from contemplate.engine import TemplateEngine
from jinja2 import Environment
import json


class Jinja2Engine(TemplateEngine):

    def __init__(self):
        pass

    def render(self, template, **kwargs):
        extensions = ['jinja2.ext.do',
                      'jinja2.ext.loopcontrols',
                      'jinja2.ext.with_',
                      'jinja2.ext.autoescape']
        env = Environment(extensions=extensions)
        env.filters['jsonify'] = json.dumps
        return env.from_string(template).render()


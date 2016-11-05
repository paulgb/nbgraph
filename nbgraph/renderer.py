
import json
import random
import string

from IPython.display import HTML
from jinja2 import Environment, PackageLoader

ENV = Environment(loader=PackageLoader('nbgraph', 'client'))


def _prepare_notebook_html(confirm_load=True):
    return ENV.get_template(
        'prepare_notebook.html').render(
            confirm_load=confirm_load, container_id=_generate_uid())


def _graph_html(graph):
    return ENV.get_template(
        'graph.html').render(container_id=_generate_uid(),
                             data=json.dumps(graph.as_dict()))


def _generate_uid():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))


def prepare_notebook(quiet=False):
    return HTML(_prepare_notebook_html(not quiet))


def generate_html(graph):
    return ''.join((
        _prepare_notebook_html(False),
        _graph_html(graph)))

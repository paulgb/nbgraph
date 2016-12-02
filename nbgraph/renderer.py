
import json
import random
import string

from IPython.display import HTML, display
from jinja2 import Environment, PackageLoader

ENV = Environment(loader=PackageLoader('nbgraph', 'client'))


def prepare_notebook(quiet=False):
    '''Adds JavaScript code to the notebook to support interactive graphs.
    This is required when calling .show() on a NotebookGraph instance unless
    include_scripts=True is passed to show. If you use multiple graphs in the
    same notebook, especially one intended for publication as HTML, using .show
    and prepare_notebook() will cut down on the file size considerably. See
    README.md for details.

    PARAMS:
        quiet               Whether or not to show a message indicating success

    Always returns None, but has the side-effect of adding JavaScript to the
    running notebook.
    '''
    display(HTML(_prepare_notebook_html(not quiet)))


def generate_html(graph, include_scripts=True, config=None):
    '''For a given NotebookGraph, generate the HTML to add it to a notebook.

    PARAMS:
        graph               A NotebookGraph instance representing the graph to
                            render.
        include_scripts     If True, all required JavaScript is included in the
                            output HTML.
        config              Dict of config params for rendering.
    '''
    contents = list()
    if include_scripts:
        contents.append(_prepare_notebook_html(False))
    contents.append(_graph_html(graph, config))
    return ''.join(contents)


def display_notebook(graph, include_scripts=True, config=None):
    '''Wrapper for generate_html that has the side-effect of causing the
    notebook to render the resulting HTML. Returns None.

    PARAMS: see generate_html
    '''
    display(HTML(generate_html(graph, include_scripts, config)))


def _prepare_notebook_html(confirm_load=True):
    return ENV.get_template(
        'prepare_notebook.html').render(
            confirm_load=confirm_load, container_id=_generate_uid())


def _graph_html(graph, config=None):
    if config is None:
        config = dict()
    return ENV.get_template(
        'graph.html').render(container_id=_generate_uid(),
                             data=json.dumps(graph.as_dict()),
                             config=json.dumps(config))


def _generate_uid():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

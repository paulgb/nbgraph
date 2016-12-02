
if (!('sigma' in window)) {
    {% include 'js/sigma.min.js' %}
    {% include 'js/sigma.layout.forceAtlas2.min.js' %}
}

if (typeof window.nbgraph != 'undefined') {
    document.getElementById('nbgraph_confirm_{{container_id}}').innerHTML =
        'WARNING: nbgraph javascript loaded multiple times. Use ' +
        '<samp>renderer.prepare_notebook()</samp> ' +
        'and call <samp>.show()</samp> on graphs to reduce notebook file size.';
}
{% include 'js/nbgraph.js' %}
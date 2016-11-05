
if (!('sigma' in window)) {
    {% include 'js/sigma.min.js' %}
    {% include 'js/sigma.layout.forceAtlas2.min.js' %}
}

{% include 'js/nbgraph.js' %}
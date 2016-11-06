
var nbgraph = {};

nbgraph.Graph = class {
    constructor(graph, container_id) {
        this.running = false;
        this.graph = graph;
        this.container = document.getElementById(container_id);
        this.buildElements();
        this.startSigma();
        this.resetGraph();
        this.toggleForce();
    }

    buildElements() {
        /* Toolbar */
        var toolbar = document.createElement('div');
        toolbar.style.marginBottom = '4px';
        this.container.appendChild(toolbar);

        /* Toggle Button */
        this.toggleForceButton = document.createElement('button');
        this.toggleForceButton.textContent = 'Stop';
        this.toggleForceButton.onclick = () => this.toggleForce();
        this.toggleForceButton.style.marginRight = '4px';
        toolbar.appendChild(this.toggleForceButton);

        /* Reset Button */
        var resetButton = document.createElement('button');
        resetButton.textContent = 'Reset';
        resetButton.onclick = () => this.resetGraph();
        toolbar.appendChild(resetButton);

        /* Outer Graph Container */
        var outerContainer = document.createElement('div');
        outerContainer.style.border = '1px solid #eee';
        this.container.appendChild(outerContainer);

        /* Inner Graph Container */
        this.graphContainer = document.createElement('div');
        this.graphContainer.style.height = '400px';
        outerContainer.appendChild(this.graphContainer);
    }

    startSigma() {
        this.sigma = new sigma({
            graph: this.graph,
            container: this.graphContainer
        });
        this.sigma.settings({
            edgeColor: 'default',
            defaultEdgeColor: '#bbb',
            nodeColor: 'default',
            defaultNodeColor: '#800'
        });
    }

    startForce() {
        this.sigma.startForceAtlas2();
        this.toggleForceButton.textContent = 'Stop';
        this.running = true;
    }

    endForce() {
        this.sigma.stopForceAtlas2();
        this.toggleForceButton.textContent = 'Resume';
        this.running = false;
    }

    toggleForce() {
        if (this.running) {
            this.endForce();
        } else {
            this.startForce();
        }
    }

    resetGraph() {
        this.sigma.killForceAtlas2();
        var nodes = this.sigma.graph.nodes();
        for (var i = 0; i < nodes.length; i++) {
            nodes[i].size = 1;
            nodes[i].x = Math.random();
            nodes[i].y = Math.random();
        }
        this.sigma.refresh();
        if (this.running) {
            this.sigma.startForceAtlas2();
        } else {
            this.toggleForceButton.textContent = 'Start'
        }
    }
}
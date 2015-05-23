r"""
==============
NetworkX-METIS
==============

This Add-on facilitates graph partitioning using METIS.

Installation
------------

Using pip
~~~~~~~~~

::

    pip install networkx-metis

Using GitHub
~~~~~~~~~~~~

::

    git clone https://github.com/networkx/networkx-metis
    cd networkx-metis
    python setup.py install

Usage
-----

.. code:: python

    >>> import networkx as nx
    >>> from networkx.addons import metis
    >>> G = nx.complete_graph(10)
    >>> metis.partition(G, 2)
    (25, [[0, 1, 2, 3, 6], [4, 5, 7, 8, 9]])

"""

try:
	from networkx_metis import *
except ImportError:
	print("Please install networkx-metis to use this add-on.")

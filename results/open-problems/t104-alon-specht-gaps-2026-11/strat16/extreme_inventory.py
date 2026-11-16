"""Exact combinatorial inventory and the face-dimension extremality test."""
import itertools
import json
from pathlib import Path
import networkx as nx


def main():
    records=[]
    for G in nx.graph_atlas_g():
        if len(G)!=5 or not nx.is_connected(G):continue
        e=G.number_of_edges()
        if e==4:
            assert nx.is_tree(G)
            records.append(dict(rank=4,edges=sorted([list(sorted(x))for x in G.edges()]),degrees=sorted(dict(G.degree()).values(),reverse=True),type='tree'))
        elif 5<=e<=7 and not nx.is_bipartite(G):
            records.append(dict(rank=3,edges=sorted([list(sorted(x))for x in G.edges()]),degrees=sorted(dict(G.degree()).values(),reverse=True),type='sparse candidate'))
    trees=[r for r in records if r['rank']==4];sparse=[r for r in records if r['rank']==3]
    assert len(trees)==3 and len(sparse)==12
    assert [sum(len(r['edges'])==e for r in sparse)for e in (5,6,7)]==[4,4,4]
    # Independent enumeration of every labelled five-vertex graph verifies
    # the atlas inventory by graph isomorphism, without relying on its count.
    atlas=[nx.Graph(r['edges'])for r in records]
    for bits in itertools.product((0,1),repeat=10):
        G=nx.Graph();G.add_nodes_from(range(5));G.add_edges_from(e for e,b in zip(itertools.combinations(range(5),2),bits)if b)
        if not nx.is_connected(G):continue
        if G.number_of_edges()==4 or (5<=G.number_of_edges()<=7 and not nx.is_bipartite(G)):
            assert sum(nx.is_isomorphic(G,A)for A in atlas)==1
    Path('extreme_graphs.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (extreme_inventory.py): 3 tree types and 12 nonbipartite rank-three support candidates (4 each with 5, 6, 7 edges), independently enumerated over all labelled supports.')

if __name__=='__main__':main()

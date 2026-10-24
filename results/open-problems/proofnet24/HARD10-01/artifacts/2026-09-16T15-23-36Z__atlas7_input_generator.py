import networkx as nx
from pathlib import Path
out=Path('/mnt/data/atlas7_codes.txt')
vals=[]
for g in nx.graph_atlas_g():
    if len(g)!=7: continue
    h=nx.convert_node_labels_to_integers(g, ordering='sorted')
    code=0; bit=0
    for j in range(1,7):
        for i in range(j):
            if h.has_edge(i,j): code |= 1<<bit
            bit+=1
    vals.append(code)
assert len(vals)==1044
out.write_text(''.join(f'{x}\n' for x in vals))
print('rows',len(vals),'unique_raw',len(set(vals)),'networkx',nx.__version__)

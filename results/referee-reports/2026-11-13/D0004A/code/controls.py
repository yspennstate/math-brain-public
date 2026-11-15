#!/usr/bin/env python3
"""Known mixable uniform controls for the transport and RA implementation."""
import json
from pathlib import Path
import experiments as E

E.segments=lambda n,floor=False:[(0.,1.,1.,0.)]
rows=[]
for n in (3,4):
    for m in (20,40):
        row=E.transport_lp(n,False,m,True)
        assert row['status']==0,row
        assert row['residual']<1e-8,row
        rows.append(row)
    row=E.rearrangement(n,False,1000)
    rows.append(row)
Path(E.ROOT/'data/controls.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))

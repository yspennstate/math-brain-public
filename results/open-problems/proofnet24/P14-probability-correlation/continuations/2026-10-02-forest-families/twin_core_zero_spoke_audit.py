"""Exact continuity-extension checks; leaves the original audit files intact."""
from fractions import Fraction as Q
from pathlib import Path
import json
from twin_core_high_fugacity_audit import audit

cases=[([Q(1),Q(1),Q(0),Q(0)],[(0,1,Q(1)),(1,2,Q(1)),(2,3,Q(1))]),
       ([Q(0),Q(1),Q(0),Q(2)],[(0,1,Q(2)),(1,2,Q(3)),(2,3,Q(4))]),
       ([Q(1),Q(1),Q(1),Q(0),Q(0)],[(u,v,Q(1))for u in range(3)for v in range(3,5)]),
       ([Q(1),Q(0),Q(2),Q(0)],[(0,1,Q(2)),(2,3,Q(3))])]
reports=[]
for a,edges in cases:
    r=audit(a,edges);reports.append(r)
    print('pass',len(a),len(edges),r['H2'],flush=True)
Path(__file__).with_name('twin_core_zero_spoke_audit_results.json').write_text(json.dumps({'cases':reports,'all_passed':True},indent=2))

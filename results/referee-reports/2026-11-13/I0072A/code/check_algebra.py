#!/usr/bin/env python3
"""Exact arithmetic checks for the report; no simulation or numerical PDE."""
from fractions import Fraction as F
from pathlib import Path
import json, os
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
root=Path(__file__).resolve().parents[1]
checks={}
checks['g_order_at_quadratic_drift']=str((F(2)+1)/2)
checks['g_order_at_literal_h_3_over_2']=str((F(3,2)+1)/2)
assert checks['g_order_at_quadratic_drift']=='3/2'
assert checks['g_order_at_literal_h_3_over_2']=='5/4'
rows=[]
for d in range(1,9):
    D=F(d+2)
    threshold=D/2
    # q_new > q iff 2/q - 2/D < 1/q, equivalently q > D/2.
    for q in [F(2),F(9,4),F(5,2),F(11,4)]:
        invnew=2/q-2/D
        if invnew>0:
            assert (1/invnew>q)==(q>threshold)
    rows.append({'d':d,'q_threshold_strict':str(threshold),
                 'epsilon_threshold_for_q_2_plus_epsilon_strict':str(threshold-2)})
checks['bootstrap']=rows
# A second derivation of the drift critical initial smoothness.
# s = 2-delta-2(1+kappa)/p, using equality in Assumption 8.4(4i).
for d,q,delta,h in [(5,F(3),F(6,5),F(2)),(3,F(2),F(11,10),F(3))]:
    kappa_ratio=h/(h-1)-(delta+F(d)/q)/2
    s=2-delta-2*kappa_ratio
    assert s==F(d)/q-2/(h-1)
checks['trace_scaling_identity']='verified exactly'
# Transfer reaction: directly sum y_i f_i, and independently use uv(u-v).
for R in [1,2,3,10]:
    u,v=F(2*R),F(R)
    f1,f2=u*v,-u*v
    direct=u*f1+v*f2
    assert f1+f2==0 and direct==u*v*(u-v)==2*R**3
checks['transfer_reaction_energy']='sum_i y_i f_i = 2 R^3 at (2R,R); total reaction zero'
# Ito square expansion: diffusion dissipation minus transport trace has the P margin.
nu,mu,grad=F(3),F(1),F(2)
b2=2*nu-mu
assert nu*grad**2-F(1,2)*b2*grad**2==mu/2*grad**2
checks['ito_margin']='nu |grad|^2 - (2nu-mu)|grad|^2/2 = mu |grad|^2/2'
(root/'data'/'algebra_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print('Exact arithmetic checks passed; results in data/algebra_checks.json')

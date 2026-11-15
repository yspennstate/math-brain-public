#!/usr/bin/env python3
"""Tiny rational checks of signed-mass topplings versus odometer conventions.

This is a deterministic normalization check, not an asymptotic simulation.
The finite interval is only a computational window; at time <= 5 its origin
cannot depend on scenery farther than distance 4.
"""
from fractions import Fraction as F
from pathlib import Path
import json

radius, horizon = 6, 5
sites = range(-radius, radius+1)
fields = [
    {x: F(1 if x % 2 else -1) for x in sites},
    {x: F(-7 if x == 0 else 1) for x in sites},
    {x: F((x*x+3*x+1) % 7-3, 3) for x in sites},
]
records=[]
for case, eta in enumerate(fields):
    mass=eta.copy(); emitted={x:F(0) for x in sites}
    total_rule=emitted.copy(); per_neighbor=emitted.copy()
    trace=[]
    for step in range(1,horizon+1):
        outgoing={x:max(mass[x],F(0)) for x in sites}
        mass={x:mass[x]-outgoing[x]+(outgoing.get(x-1,F(0))+outgoing.get(x+1,F(0)))/2 for x in sites}
        emitted={x:emitted[x]+outgoing[x] for x in sites}
        total_rule={x:max(eta[x]+(total_rule.get(x-1,F(0))+total_rule.get(x+1,F(0)))/2,F(0)) for x in sites}
        per_neighbor={x:max(eta[x]/2+(per_neighbor.get(x-1,F(0))+per_neighbor.get(x+1,F(0)))/2,F(0)) for x in sites}
        assert emitted==total_rule
        assert all(total_rule[x]==2*per_neighbor[x] for x in sites)
        trace.append({'time':step,'origin_total_emission':str(emitted[0]),'origin_per_neighbor':str(per_neighbor[0])})
    records.append({'configuration':case,'trace':trace})
Path('data/normalization-check.json').write_text(json.dumps({'dimension':1,'radius':radius,'horizon':horizon,'cases':records,'assertions':'passed'},indent=2)+'\n')
print('Passed: three deterministic rational fields, five rounds each; physical flow = cumulative recursion = 2 × per-neighbor convention.')

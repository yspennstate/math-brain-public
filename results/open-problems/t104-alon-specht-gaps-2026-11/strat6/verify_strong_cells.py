"""PROVED: standard-library replay of stronger rational weight-moment cells."""
import json
from fractions import Fraction as F
from moment_bounds import vertices, check

verts = vertices()
assert len(verts) == 19
records = json.load(open('strong_moment_cells.json'))
for rec in records:
    assert check(rec,verts) == F(rec['margin'])
print('PROVED:',len(verts),'vertices independently enumerated;',len(records),'rational cells verified.')
for lower,upper in [(F(15,100),F(2,10)),(F(2,10),F(4,10)),(F(4,10),F(6,10)),
                    (F(6,10),F(8,10)),(F(8,10),F(9,10)),(F(9,10),F(95,100)),(F(95,100),F(1))]:
    relevant=[c for c in records if F(c['rlo'])<upper and F(c['rhi'])>lower]
    if not relevant:
        continue
    cursor=lower
    for c in relevant:
        assert F(c['rlo'])<=cursor
        cursor=max(cursor,F(c['rhi']))
    assert cursor>=upper
    print('PROVED: ratios',lower,'through',upper,'scale ceiling',min(F(c['ahi']) for c in relevant))

from pathlib import Path
p=Path(__file__).resolve().parent
with (p/'check_exterior.py').open(encoding='utf-8',newline='') as f:s=f.read()
pairs=[
('    ck(nonneg(add((1,{2:4*d}),(-1,D))))','    # Canonical current-influence bound is deliberately excluded in v2; negative controls retain its failure.'),
('E=4*block(vals,range(nz))','E=Q(0)\n for pair in [(0,1),(2,3)]:\n  left=[i for i in pair if i in zr]\n  if len(left)==2:E+=4*block(vals,[zr.index(i) for i in left])\n  elif len(left)==1:E+=2'),
('ck(len(zs_all)==74)','zs_all=list(product([None,0,1],repeat=4))\nck(len(zs_all)==81)'),
('if t and zs[orig^1] is not None:continue',''),
('ck(E-(acs[0][4]+acs[1][4])/2==4*d)','own_drop=E-(acs[0][4]+acs[1][4])/2\n    ck(own_drop>=2)\n    ck(nonneg(add((1,{2:own_drop}),(-1,D))))'),
("('pilot.json' if pilot else 'validation.json')","('pair_pilot.json' if pilot else 'pair_validation.json')"),
('ck(d==Q(1,2)+t*(1-mu))','ck(d==(Q(1,2)+t*(1-mu) if zs[orig^1] is None else t*(1-mu)))')]
for old,new in pairs:
 assert s.count(old)==1,repr(old)
 s=s.replace(old,new)
compile(s,'check_pair.py','exec')
with (p/'check_pair.py').open('w',encoding='utf-8',newline='') as f:f.write(s)
print('derived pair checker; seven anchors verified; compilation PASS')

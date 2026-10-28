from pathlib import Path
exec((Path(__file__).with_name('check.py')).read_text(encoding='utf-8').split("mode=sys.argv")[0])
rows=0
for mask in range(64):
 es=[e for i,e in enumerate(itertools.combinations(range(4),2)) if mask>>i&1]
 if rank(4,es)!=4:continue
 b=phase(4,es)
 for aff in range(32):
  t=tuple(v*(-1)**(((x&(aff>>1)).bit_count()+(aff&1))%2) for x,v in enumerate(b))
  ck(set(spec(t))=={F(1,16)});ck(inf(t)==2);rows+=1
ck(rows==896)
(R/'out/AFFINE.json').write_text(json.dumps({'cases':rows,'exact_assertions':checks,'seconds':time.monotonic()-start,'conclusion':'flatness and root influence depend on polar rank only; new two-edit theorem admits arbitrary affine terms'},indent=2),encoding='utf-8')
print('affine guard PASS',rows,checks)

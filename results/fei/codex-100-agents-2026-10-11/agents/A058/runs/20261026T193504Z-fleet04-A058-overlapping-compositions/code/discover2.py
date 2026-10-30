exec(__import__('pathlib').Path(__file__).with_name('discover.py').read_text(encoding='utf-8').split('rows=[];')[0])
rows=[]; start=time.monotonic()
for n in range(4,17):
    N=1<<n; k=round(N*(math.sqrt(5)-1)/2)
    w=walsh([-1 if x<k else 1 for x in range(N)])
    p=k/N; H=ent([x*x/(N*N) for x in w]); I=sum(x*x/(N*N)*j.bit_count() for j,x in enumerate(w))
    for d in range(31):
        rows.append(dict(n=n,k=k,depth=d,variables=n*(1<<d),H=H,I=I,ratio=H/I if I else 0,excess=H-6*I))
        v=4*p*(1-p); m=1-2*p*p
        H=ent([m*m,p*p*v,p*p*v,v*v/4])+2*p*(H-ent([(1-2*p)**2,v]))
        I=2*p*I; p=1-p*p
assert len(rows)==403
eligible=[r for r in rows if 0<r['excess']<2.6]
out={'elapsed_s':time.monotonic()-start,'eligible':eligible,'best':max(rows,key=lambda r:r['ratio'])}
(root/'out'/'DISCOVERY2.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'eligible':eligible[:4],'best':out['best']}))

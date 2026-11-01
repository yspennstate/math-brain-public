from pathlib import Path
exec((Path(__file__).with_name('check.py')).read_text(encoding='utf-8').split("mode=sys.argv")[0])
n=4;m=2;d=F(1,16);graphs=states=edges_count=0
for mask in range(64):
 es=[e for i,e in enumerate(itertools.combinations(range(4),2)) if mask>>i&1]
 if rank(n,es)!=4:continue
 graphs+=1;b0=phase(n,es);b=b0+b0;c=list(b);c[0]*=-1;c=tuple(c);qc=spec(c)
 Ix=(inf(b)+inf(c))/2;hg=H(spec(b+c));rr=sub((2*Ix,2*Ix),hg)
 ck(Ix==m+F(2*m+1,2)*d);ck(rr[0]>d/8)
 for maskq in range(32):
  t=c;q=qc;labs=list(range(5));j=0
  for lab in range(5):
   if maskq>>lab&1:
    ix=labs.index(lab);t=res(t,ix,0);q=marg(q,ix);labs.pop(ix);j+=1
  p=spec(t);ck(all(pp<=2**j*qq for pp,qq in zip(p,q)));states+=1
  for ix,lab in enumerate(labs):
   qm=marg(q,ix);pt=H(p);pq=CE(p,q);hh=(F(0),F(0));cq=(F(0),F(0))
   influence=F(sum(t[x]!=t[x^(1<<ix)] for x in range(len(t))),len(t))
   for v in [0,1]:
    tt=res(t,ix,v);pp=spec(tt);hh=add(hh,scale(H(pp),F(1,2)));cq=add(cq,scale(CE(pp,qm),F(1,2)))
   ld=sub(pq,cq)
   if lab!=4:ck(ld[1]<2)
   else:
    ew=scale(sub(ld,(4*influence,4*influence)),F(1,2**(j+1)))
    ck(ew[1]<d*(m-F(1,6)))
   edges_count+=1
ck(graphs==28);ck(states==896);ck(edges_count==2240)
result={'assertions':checks,'graphs':graphs,'states':states,'local_queries':edges_count,'seconds':time.monotonic()-start,'verdict':'HOLDS at stated scope; scalar ancestor contributor conflict disclosed'}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))

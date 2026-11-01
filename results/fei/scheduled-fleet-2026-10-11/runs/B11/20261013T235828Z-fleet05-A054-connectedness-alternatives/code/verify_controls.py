from pathlib import Path
import hashlib
path=Path(__file__).with_name('projection_and_phi.py')
source=path.read_text(encoding='utf-8').split('cases=paid=isolating=0')[0]
exec(compile(source,str(path),'exec'))
controls=[]
for d,c in [(4,3),(5,4)]:
 N=1<<(d+c);A=(1<<d)-1
 a=tuple(int((x&A).bit_count()<=1) for x in range(N));b=tuple(int(x==A) for x in range(N));g=tuple(x+y for x,y in zip(a,b))
 ck(len(components(g))==2);ck(spec(g)==direct(g));ck(energy(g,N-1)==edges(g,N-1))
 gap=add((raw(g),1),(raw(a),-1),(raw(b),-1));lo,hi=interval(gap)
 ck(lo>0)
 if d==4:
  ck(3**45*5**25>2**128);ck(2**23552>3**1620*23**2645*41**1681)
  nonneg(add(({2:4*energy(a,N-1)},1),(raw(a),-1)))
  nonneg(add((raw(g),1),({2:4*energy(g,N-1)},-1)))
  f=tuple(1-2*x for x in g);ch=children(f,A)
  ck(sum(energy(v,len(v)-1)>0 for v in ch)==1)
  pd=ch[15];ck(pd==( -1,1,1,1,1,1,1,1))
  deficit=add((raw(pd),1),(raw(f),-energy(pd,7)/energy(f,N-1)))
  nonneg(deficit)
 else:ck(lo>F(1,5000))
 controls.append(dict(n=d+c,component_sizes=[sum(a),sum(b)],positive_raw_excess_natural_interval=[lo,hi],energy=energy(g,N-1)))
save('MANDATORY_CONTROLS.json',dict(status='PASS',assertions=checks,seconds=time.perf_counter()-start,helper_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),controls=controls))
print(json.dumps(dict(status='PASS',assertions=checks,seconds=time.perf_counter()-start),indent=2))

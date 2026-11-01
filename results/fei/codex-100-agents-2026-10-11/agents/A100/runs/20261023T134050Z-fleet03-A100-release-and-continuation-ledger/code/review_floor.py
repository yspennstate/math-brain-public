import exact as e
from exact import F,ck,fft,spectrum,wrapper,reference,children,marginal,erasure,ce,linear,logform,controller
import json,time,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
import hashlib
assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==spec['checker_sha256']
pilot='--pilot' in sys.argv
a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
beta=controller(a)[3];ck(beta==F(3,8))
def seed(L):
 out=[]
 for x in range(1<<(3*L)):
  bits=[((x>>(j*L))&((1<<L)-1)).bit_count()%2 for j in range(3)]
  out.append(-1 if bits[0]==bits[1]==bits[2] else 1)
 return tuple(out)
def influence(v):
 n=len(v).bit_length()-1
 return sum(F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v)) for j in range(n))
nodes=terminals=postchildren=0; cases=[]
for L in ([1] if pilot else [1,2,3]):
 h=seed(L);p=spectrum(h);ck(sum(z for z in p if z)==1);ck(sorted(z for z in p if z)==[F(1,4)]*4)
 ck(influence(h)==F(3*L,2))
 for sigma in [-1,1]:
  G=wrapper(a,h,sigma);PG=spectrum(G);c0=ce(PG,PG)
  ck(sum(z>0 for z in PG)<=64)
  expected=(F(13,8) if sigma==1 else F(15,8))+F(9*L,16)
  ck(influence(G)==expected);ck(F(35,4)<=4*expected)
  front=[h]
  for depth in range(L+1):
   nxt=[]
   for hb in front:
    nodes+=1;gb=wrapper(a,hb,sigma);pb=spectrum(gb);ph=spectrum(hb)
    ck(ce(pb,pb)==c0);ck(F(sum(hb),len(hb))==F(1,2));ck(sorted(z for z in ph if z)==[F(1,4)]*4)
    ck(reference(a,hb,sigma,ph)==pb)
    if depth<L:
     ck(fft(hb)[1]==0);ck(ph[1]==0);ck(erasure(pb,4)==())
     ch=children(hb,0);pcs=[spectrum(z) for z in ch]
     ck(pcs[0]==pcs[1]==marginal(ph,0))
     for hh in ch:
      ck(spectrum(wrapper(a,hh,sigma))==marginal(pb,4))
     nxt.extend(ch)
    else:
     terminals+=1
     # Distinguished remaining union is the last frequency index.
     ck(ph[0]==ph[-1]==F(1,4))
     q=tuple(F(1,4) if j==0 else F(1,3) if j==len(ph)-1 else F(5,24) if ph[j] else F(0) for j in range(len(ph)))
     ck(sum(q)==1);Q=reference(a,hb,sigma,q)
     delta=linear((F(3,32),logform(F(27,25))))
     ck(linear((1,ce(pb,Q)),(-1,ce(pb,pb)))==delta)
     # True physical query, all inherited reference atoms retained, both children.
     qm=marginal(Q,4);bills=[]
     for gc in children(gb,4):
      postchildren+=1;pc=spectrum(gc);bills.append(ce(pc,qm))
     charge=linear((1,erasure(pb,4)),(F(1,2),bills[0]),(F(1,2),bills[1]),(-1,ce(pb,Q)))
     # Conditional occupancy KL reconstructed independently including vacuum.
     kl=[]
     for j in range(len(pb)//2):
      pairp=[pb[e.ins(j,4,b)] for b in (0,1)];pairq=[Q[e.ins(j,4,b)] for b in (0,1)]
      for u,v in zip(pairp,pairq):
       if u:kl.append((u,logform(u*sum(pairq)/(sum(pairp)*v))))
     ck(charge==linear(*[(-w,l) for w,l in kl]))
   front=nxt
  ck(F(35,4)-F(1,4)-6-F(3,32)==F(77,32));ck(25<27<50)
  cases.append({'L':L,'sigma':sigma,'influence':str(expected),'source_support':sum(z>0 for z in PG),'source_entropy_prime_log':[(p,str(k)) for p,k in c0]})
# Nonuniform-event profiles and a reference-only atom: exact KL chain-rule.
floorcases=0
for r in [F(0),F(1,4),F(1,2)]:
 t=1-r
 for alpha in [F(1,4),F(1,3),F(1,2)]:
  av=t*alpha;p=(r,av/3,2*av/3,t-av,F(0))
  for w in [F(1,4),F(1,2),F(3,4)]:
   ell=av+(t-av)*w;q=(r,ell/3,2*ell/3,t-ell,F(0));floorcases+=1
   d=linear((1,ce(p,q)),(-1,ce(p,p)))
   ck(d==linear((av,logform(av/ell)),(t-av,logform((t-av)/(t-ell)))))
   for z in [ell,(ell+t)/2]:
    # Allocate a positive ghost in A's complement; its hidden price must remain.
    qq=(r,z/4,3*z/4,(t-z)*F(3,4),(t-z)/4)
    actual=linear((1,ce(p,qq)),(-1,ce(p,p)))
    coarse=linear((av,logform(av/z)),(t-av,logform((t-av)/(t-z))))
    within=linear((av/3,logform(F(4,3))),(2*av/3,logform(F(8,9))),(t-av,logform(F(4,3))))
    ck(actual==linear((1,coarse),(1,within)))
result={'status':'PASS','pilot':pilot,'checks':e.checks,'prefix_nodes':nodes,'complete_admission_terminals':terminals,'post_admission_children':postchildren,'floor_profiles':floorcases,'family_cases':cases,'runtime_seconds':round(time.perf_counter()-e.start,6),'arithmetic':'Fraction plus exact prime-log cancellation; continuum proved analytically; no approximate sign tests','full_FEI':'OPEN'}
(R/'out'/('PILOT.json' if pilot else 'FLOOR_REVIEW.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='family_cases'}))

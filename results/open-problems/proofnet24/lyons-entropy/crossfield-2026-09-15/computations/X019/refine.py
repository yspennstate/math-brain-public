from explore import *

def physical(v):
 C,aa,bb,cc,ee=v
 if C<abs(aa):return False
 A=aa*aa+3*ee*ee;B=2*(C*aa-bb*cc);Z=C*C-bb*bb-cc*cc-3*ee*ee
 vals=[A-B+Z,A+B+Z]
 if A and -2*A<=B<=2*A:vals.append(Z-B*B/(4*A))
 return min(vals)>=0

def norm(v):
 x=next(z for z in v if z);return tuple(z/abs(x) for z in v)

if __name__=='__main__':
 T,data=coeff(); H,k,labs=constraints(T)
 cons={norm(tuple([z,*(-h)])):('initial',i) for i,(h,z) in enumerate(zip(H,k))}
 cuts=[]
 for iteration in range(20):
  H=np.array([[-x for x in v[1:]] for v in cons],dtype=object); k=np.array([v[0] for v in cons],dtype=object)
  vs=vertices(H,k);bad=[]
  print('iteration',iteration,'constraints',len(k),'vertices',len(vs),flush=True)
  for p in vs:
   r,b=lp(T,p)
   if not r.success:
    rr=linprog(b,A_ub=-D.T,b_ub=np.zeros(90),bounds=[(-1,1)]*50,method='highs')
    y=np.array([F(float(x)).limit_denominator(10000) for x in rr.x],dtype=object)
    assert all(z>=0 for z in D.T@y)
    v=tuple(T.T@y)
    if not physical(v):
     print('NONVALID',p,v,flush=True);raise SystemExit(1)
    bad.append((p,y,v))
  print('bad',len(bad),flush=True)
  if not bad:
   json.dump({'coeff':[[str(x) for x in r] for r in T], 'constraints':[[str(x) for x in v] for v in cons], 'vertices':[[str(x) for x in p] for p in vs], 'cuts':[{k:([str(x) for x in v] if k!='y' else [str(x) for x in v]) for k,v in cut.items()} for cut in cuts]},open('computations/X019/refined.json','w'),indent=2)
   break
  count=0
  for p,y,v in bad:
   for sg in itertools.product([-1,1],repeat=3):
    tr=[F(1),F(sg[0]*sg[1]),F(sg[1]*sg[2]),F(sg[0]*sg[2]),F(math.prod(sg))]
    vv=norm(tuple(v[i]*tr[i] for i in range(5)))
    if vv not in cons:
     cons[vv]=('dual',len(cuts));count+=1
     cuts.append({'v':vv,'y':tuple(y),'sign':tr})
  print('new',count,flush=True)
  assert count
  json.dump({'iteration':iteration,'constraints':[[str(x) for x in v] for v in cons], 'cuts':[{k:[str(x) for x in v] for k,v in cut.items()} for cut in cuts]},open('computations/X019/checkpoint.json','w'),indent=2)

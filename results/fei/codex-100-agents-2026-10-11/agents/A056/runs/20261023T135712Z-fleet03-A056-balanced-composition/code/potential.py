from prior import *
def mp(p):
 out={}
 for s,q in enumerate(p):
  for j in range(2,s.bit_count()+1):out=add(out,log(j-1),q/Q(j))
 return out
def degree(d):
 out={}
 for j in range(2,d+1):out=add(out,log(j-1),Q(1,j))
 return out
def hb(d):return add(log(d),log(d-1),-Q(d-1,d))
def get(a):return {int(p):Q(v) for p,v in a.items()}
t=time.perf_counter();count=0;trees=[];degrees=[]
c=scale(add(add(log(5),log(3),Q(1,4)),{2:Q(11,15)}),Q(1,5))
assert 5**240>2**524*3**15
assert 5**310>3**285*2**256
assert 5**60*3**15<2**166
for d in range(2,65):
 m=degree(d);w=add(log(d),m)
 assert w==add({} if d==2 else add(log(d-1),degree(d-1)),hb(d))
 assert nonnegative(add(scale(c,Q(d)),w,-1))
 assert (add(scale(c,Q(d)),w,-1)=={})==(d==5)
 degrees.append({'degree':d,'M':ser(m),'W':ser(w),'maximum_ratio_gap':ser(add(scale(c,Q(d)),w,-1))})
 count+=3
for lane in range(4):
 data=json.loads((R/'out'/f'lane{lane}.json').read_text(encoding='utf-8'))
 for record in data['trees']:
  f=table(3,record['code']);p=prob(f);m=mp(p)
  assert get(record['reselection_entropy_total'])==m
  # Compute L independently, then check the complete combined bill overhead.
  ll={}
  for s,q in enumerate(p):
   if s:ll=add(ll,log(s.bit_count()),q)
  assert nonnegative(add(scale(c,influence(f)),add(ll,m),-1))
  for i in range(3):
   child=scale(add(mp(prob(restrict(f,i,0))),mp(prob(restrict(f,i,1)))),Q(1,2))
   rho={}
   for s,q in enumerate(p):
    d=s.bit_count()
    if s>>i&1 and d>=2:rho=add(rho,log(d-1),q/d)
   assert add(m,child,-1)==rho
   count+=1
  trees.append({'code':record['code'],'uniform':record['uniform'],'M_root':ser(m),'rho_tree_total':record['reselection_entropy_total'],'combined_overhead':ser(add(ll,m))})
  count+=2
out={'status':'PASS','helper':'A056-mark-randomness-exact-potential-v1','degree_cases':degrees,'tree_cases':trees,'assertions_executed':count+3,'sharp_constant_prime_log':ser(c),'decimal_for_orientation_only':0.690300410681,'upper_bound':'7/10, proved by5^60*3^15<2^166','guards':['5^240>2^524*3^15','5^310>3^285*2^256','5^60*3^15<2^166'],'runtime_seconds':time.perf_counter()-t,'full_FEI':'OPEN'}
(R/'out'/'POTENTIAL_CERTIFICATES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['degree_cases','tree_cases']},indent=2))

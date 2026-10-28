from prior import *
from math import comb
import hashlib

N=0
def ck(ok):
 global N
 N+=1
 assert ok

def entlaw(p):return ce(p,p)
def tilt(p):
 v=1-p[0];ii=sum((j.bit_count()*q for j,q in enumerate(p)),Q(0))
 return tuple(p) if not v else (p[0],)+tuple(v*j.bit_count()*p[j]/ii for j in range(1,len(p)))

def per_set_joint(p):
 atoms=[p[0]] if p[0] else [];over={};ii=Q(0)
 for j,q in enumerate(p):
  if j and q:
   d=j.bit_count();group=[q/d]*d;ck(sum(group)==q);atoms.extend(group);over=add(over,log(d),q);ii+=d*q
 ck(sum(atoms)==1);h=entlaw(atoms)
 ck(h==add(entlaw(p),over));ck(nonnegative(add({2:ii-(1-p[0])},over,-1)))
 return h,over

def truth(k,m):
 # The first k coordinates form the point guard; z has index k.
 out=[]
 for x in range(1<<(k+1+m)):
  y=x>>(k+1);z=-1 if (x>>k)&1 else 1
  out.append((-1 if y.bit_count()%2 else 1) if not x&((1<<k)-1) else z)
 return tuple(out)

def amplitude(k,m):
 a=[Q(0)]*(1<<(k+1+m));d=Q(1,1<<k);z=1<<k;ymask=((1<<m)-1)<<(k+1)
 a[z]=1-d
 for s in range(1,1<<k):a[z|s]=-d
 for s in range(1<<k):a[ymask|s]=d
 return tuple(a)

def direct(k,m):
 f=truth(k,m);a=amplitude(k,m);d=Q(1,1<<k);p=tuple(q*q for q in a);ii=1+d*(m+k-1)
 ck(spectrum(f)==a);ck(sum(p)==1);ck(mean(f)==0);ck(influence(f)==ii)
 for j in range(k+1+m):ck(edge_inf(f,j)==(1-d if j==k else d))
 # Independent direct character sums for all nonzero asserted amplitudes.
 for j,q in enumerate(a):
  if q:ck(Q(sum(y*(-1 if (x&j).bit_count()%2 else 1) for x,y in enumerate(f)),len(f))==q)
 s=tilt(p);ck(sum(s)==1);hs=entlaw(s);hp=entlaw(p);debt=add(ce(p,s),hp,-1)
 ck(nonnegative(debt));ck(nonnegative(add({2:ii},debt,-1)))
 ck(nonnegative(add({2:Q(3,2)*ii},hp,-1)));ck(nonnegative(add(hs,{2:-Q(k,1)/ii})))
 # The pointed witness and its index label are explicitly normalized.
 pointed=[];per_set=[];overhead={}
 for j,q in enumerate(p):
  if q:
   for coord in range(k+1+m):
    if j>>coord&1:pointed.append(q/ii);per_set.append(q/j.bit_count())
   overhead=add(overhead,log(j.bit_count()),q)
 ck(sum(pointed)==1);hw=entlaw(pointed);ck(nonnegative(add(hw,hs,-1)))
 ck(sum(per_set)==1);hi=entlaw(per_set)
 hi2,over2=per_set_joint(p);ck(hi2==hi);ck(over2==overhead)
 ck(hi==add(hp,overhead));ck(nonnegative(add({2:ii-1},overhead,-1)))
 ck(nonnegative(add({2:Q(5,2)*ii-1},hi,-1)))
 idx=[edge_inf(f,j)/ii for j in range(k+1+m)]
 ck(sum(idx)==1);ck(nonnegative(add(entlaw(idx),{2:-Q(k,1)/ii})))
 children=[restrict(f,0,b) for b in [0,1]]
 cp=[prob(c) for c in children];cr=[tilt(q) for q in cp]
 ck(all(mean(c)==0 and influence(c)>0 for c in children))
 ck(children[1]==tuple(1 if (x>>(k-1))&1==0 else -1 for x in range(len(children[1]))))
 ck(ii==d+sum((influence(c) for c in children),Q(0))/2)
 oldterm=scale(add(entlaw(cp[0]),entlaw(cp[1])),Q(1,2));olddebit=add(hp,oldterm,-1);ck(nonnegative(olddebit))
 full=scale(add(ce(cp[0],cr[0]),ce(cp[1],cr[1])),Q(1,2))
 debts=[add(ce(q,r),entlaw(q),-1) for q,r in zip(cp,cr)]
 ck(all(nonnegative(x) for x in debts));ck(add(olddebit,full)==add(hp,scale(add(*debts),Q(1,2))))
 ck(nonnegative(add({2:Q(5,2)*ii},add(olddebit,full),-1)))
 terminal_ref_H=scale(add(entlaw(cr[0]),entlaw(cr[1])),Q(1,2))
 iplus=1+2*d*(m+k-2)
 if k>=2:ck(nonnegative(add(terminal_ref_H,{2:-Q(k-1,1)/iplus})))
 zrows=[]
 for bit in [0,1]:
  g=restrict(f,k,bit);pg=prob(g);sg=tilt(pg);mg=(1 if bit==0 else -1)*(1-d);v=1-mg*mg
  ck(mean(g)==mg);ck(pg[0]==mg*mg);ck(sg[0]==pg[0]);ck(sum(sg)==1)
  ck(influence(g)==d*(m+k));ck(entlaw(pg)==hp);ck(nonnegative(add({2:Q(3)},entlaw(sg),-1)))
  hj,oj=per_set_joint(pg)
  zrows.append({'sign':1 if bit==0 else -1,'mean':str(mg),'variance':str(v),'I':str(influence(g)),'fresh_reference_entropy':ser(entlaw(sg)),'per_set_witness_H':ser(hj),'per_set_witness_overhead':ser(oj)})
 return {'k':k,'m':m,'input_bits':k+1+m,'truth_entries':len(f),'truth_sha256':hashlib.sha256(bytes(x==1 for x in f)).hexdigest(),'I':str(ii),'true_H':ser(hp),'degree_reference_H':ser(hs),'pointed_witness_H':ser(hw),'per_set_witness_H':ser(hi),'per_set_witness_overhead':ser(overhead),'coordinate_label_H':ser(entlaw(idx)),'true_cross_entropy':ser(ce(p,s)),'root_reset_KL':ser(debt),'old_guard_query_CE_debit':ser(olddebit),'both_guard_children_nonconstant':True,'full_terminal_CE':ser(full),'full_terminal_KL':ser(scale(add(*debts),Q(1,2))),'expected_terminal_reference_H':ser(terminal_ref_H),'active_fresh_reset_positive':bool(debts[0]),'z_children':zrows}

def compressed(k):
 m=1<<k;d=Q(1,m);ii=2+(k-1)*d;ip=3+2*(k-2)*d
 count=mass=moment=Q(0);carrier_degree=Q(0);guard_degree=Q(0)
 for r in range(k+1):
  c=comb(k,r);count+=c;carrier_degree+=c*(m+r);mass+=c*d*d;moment+=c*d*d*(m+r)
  if r:guard_degree+=c*(1+r);mass+=c*d*d;moment+=c*d*d*(1+r)
 mass+=(1-d)**2;moment+=(1-d)**2
 ck(count==m);ck(mass==1);ck(moment==ii);ck(carrier_degree==m*(m+Q(k,2)))
 ck(2<=ii<=Q(9,4));ck(k*d<=Q(1,2));ck((k-1)*d<=Q(1,4))
 ck(d*d*(m+k)/ii<=d);cy=d*(m+Q(k,2))/ii;ck(cy>=1/ii)
 # Rational coefficient L certifies H(S)>=L; no logarithmic evaluation.
 lower=Q(k,1)/ii;ratio=lower/ii;ck(ratio>=Q(16*k,81))
 source_tail=2*k*(2*m-1)*d*d;ck(source_tail<=2);ck(3<=Q(3,2)*ii)
 pointed_y_mass=d*m/ii;ck(pointed_y_mass==1/ii)
 ck(ii==d+(1+ip)/2)
 after=None
 if k>=2:
  dp=2*d;ck(ip<=Q(7,2));ck((m+k-1)*dp*dp/ip<=dp)
  after=Q(k-1,1)/ip;ck(after>=Q(2*(k-1),7));ck(after/ii>=Q(8*(k-1),63))
 v=2*d-d*d;jg=d*(m+k);ck(ii==(1-d)+jg);ck(v*(k+1)<=2)
 return {'k':k,'m':str(m),'input_bits':str(1+k+m),'I':str(ii),'H_P_upper':'3','H_P_shrinking_upper':str(4*(k+1)*d),'H_S_lower':str(lower),'H_S_over_I_lower':str(ratio),'root_reset_KL_upper':str(ii),'cross_entropy_P_S_over_I_upper':'5/2','active_child_I':str(ip),'both_guard_children_balanced_nonconstant':True,'expected_terminal_H_S_lower':str(after) if after is not None else '0','z_child_absolute_mean':str(1-d),'z_child_V':str(v),'z_child_I':str(jg),'z_child_H_S_upper':'3','certificate':'EXACT RATIONAL BINOMIAL MOMENTS PLUS ANALYTIC ENTROPY BOUNDS'}

def main():
 t=time.perf_counter();pilot='--pilot' in sys.argv;rows=[];cert=[]
 h,o=per_set_joint((Q(1),));ck(not h and not o)
 for k in ([1] if pilot else [1,2,3]):
  ck(time.perf_counter()-t<55);rows.append(direct(k,1<<k))
 for k in ([1] if pilot else list(range(1,33))+[64,128,256]):
  ck(time.perf_counter()-t<55);cert.append(compressed(k))
 out={'status':'PASS','helper':'A056-degree-entropy-boundary-v1.1','pilot':pilot,'assertions':N,'runtime_seconds':time.perf_counter()-t,'direct_cases':rows,'compressed_cases':cert,'all_k_proof':'DERIVATION.md (1)-(15); finite certificates do not establish the all-k limit by extrapolation','full_FEI':'OPEN'}
 (R/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ['direct_cases','compressed_cases']}|{'direct_cases':len(rows),'compressed_cases':len(cert)},indent=2))

if __name__=='__main__':main()

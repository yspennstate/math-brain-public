import itertools,json,time,math
from fractions import Fraction as R
from pathlib import Path
base=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=traces=0
def test(x):
 global checks
 assert x
 checks+=1
rows=[]
for a,b in [(2,2),(2,3),(3,3)]:
 E=[(i,j) for i in range(a) for j in range(a,a+b) if (i,j)!=(0,a)]
 def edge(i,j): return (i,j) if i<a else (j,i)
 def neigh(i): return [j for j in range(a+b) if edge(i,j) in E]
 lam=R(1,b); p=lam/4/(1+lam/4); cond=1-(1-p)**len(E); D=(1+lam/4)**len(E)-1
 N=2**(a+b); values=[2*int(any(x>>i&1 and x>>j&1 for i,j in E))-1 for x in range(N)]
 I=sum(R(sum(values[x]!=values[x^(1<<j)] for x in range(N)),N) for j in range(a+b))
 degree=R(0); qsum=R(0); exceptions=0
 for mask in range(1,N):
  A={i for i in range(a+b) if mask>>i&1}; L=sorted(A&set(range(a))); T=sorted(A-set(range(a)))
  walsh=sum(values[x]*(-1 if (mask&x).bit_count()%2 else 1) for x in range(N)); degree+=R(walsh*walsh,N*N)*len(A)
  if not L or not T:
   selected=L or T; total=R(0)
   for partner in itertools.product(*(neigh(i) for i in selected)):
    labels=[edge(i,j) for i,j in zip(selected,partner)]
    test(len(set(labels))==len(A))
    total+=p**len(A)*(1-p)**(len(E)-len(A))/cond*R(1,8)**len(A); traces+=1
   lower=R(1,64)**len(L) if L else R(a,64*b)**len(T)
  else:
   candidates=[e for e in E if set(e)<=A]
   def covered(e): return set(e)|{i for i in A-set(e) if any(edge(i,j) in E for j in e if (i<a)!=(j<a))}
   if candidates:
    pivot=max(candidates,key=lambda e:len(covered(e)))
    remaining=sorted(A-covered(pivot)); children=[]
    for i in sorted(covered(pivot)-set(pivot)):
     partners=[j for j in pivot if edge(i,j) in E]
     test(bool(partners)); children.append(edge(i,partners[0]))
    c=len(children); roots=[pivot]
    probability=R(1,6)*R(1,(c+1)*(c+2))*R(1,c+1)*(lam/8)**c
   else:
    roots=[]; children=[]; remaining=sorted(A); probability=R(1)
   for i in remaining:
    outside=[j for j in neigh(i) if j not in A]
    test(bool(outside)); roots.append(edge(i,outside[0])); probability*=R(1,8)
   labels=roots+children
   test(len(set(labels))==len(labels))
   test(all(e in E for e in labels))
   test(len(roots)<=2)
   probability*=p**len(roots)*(1-p)**(len(E)-len(roots))/cond
   total=probability; traces+=1; exceptions+=int(len(roots)==2)
   lower=(lam/64)**len(A)
  test(total*D>=lower)
  qsum+=total
 test(qsum<=1); test(degree==I)
 rows.append({'a':a,'b':b,'I':str(I),'actual_subprobability':str(qsum),'two_root_output_sets':exceptions})
result={'helper_version':'A009-damaged-original-probability-replay-v1','functions':len(rows),'checks':checks,'distinct_explicit_traces':traces,'elapsed_seconds':time.perf_counter()-start,'all_passed':True,'cases':rows}
base.joinpath('out','DAMAGED_VERIFY.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))

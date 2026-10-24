import numpy as np, scipy.special as ss, scipy.linalg as la, json,math,pathlib

def part_of_mask(n,m):
 cuts=[i for i in range(n) if m>>i&1]; lens=[(cuts[(j+1)%len(cuts)]-x)%n or n for j,x in enumerate(cuts)];return tuple(sorted(lens))
def rates(p,n,b):
 out={}
 for x in range(len(p)):
  for y in range(x+1,len(p)):
   q=list(p);q.pop(y);q.pop(x);q.append(p[x]+p[y]);q=tuple(sorted(q));out[q]=out.get(q,0)+2/n
 for x,j in enumerate(p):
  for t in range(1,j):
   q=list(p);q.pop(x);q.extend([t,j-t]);q=tuple(sorted(q));out[q]=out.get(q,0)+b
 return out
rows=[]
for n in range(2,10):
 b=1/n; groups={}
 for m in range(1,2**n):groups.setdefault(part_of_mask(n,m),[]).append(m)
 worst=0;count_error=0
 for p,group in groups.items():
  avg={}
  for m in group:
   k=m.bit_count()
   for i in range(n):
    dest=m^(1<<i); v=(k-1)/n if m>>i&1 else b
    if v:
     q=part_of_mask(n,dest);avg[q]=avg.get(q,0)+v/len(group)
  exact=rates(p,n,b)
  worst=max(worst,max((abs(avg.get(q,0)-exact.get(q,0)) for q in set(avg)|set(exact)),default=0))
  count=n*math.factorial(len(p)-1)
  for j in set(p):count//=math.factorial(p.count(j))
  # Check using exact rational quotient rather than successive division.
  denom=math.prod(math.factorial(p.count(j)) for j in set(p)); count=n*math.factorial(len(p)-1)//denom
  count_error=max(count_error,abs(len(group)-count))
 rows.append({'n':n,'averaged_rate_error':worst,'subset_count_error':count_error})
cert_upper=0; count_upper_error=0;count_lower_error=0
for n in [2,3,8,16,100,1000,10000]:
 k=np.arange(1,n,dtype=float)
 for b in np.geomspace(1e-12,1e4,33):
  a=max(1,n*math.sqrt(b));R=2*b*(n-k-1)/(k+a+2)+b+2*k*a/(n*(k+a-1))
  bound=b+4*max(math.sqrt(b),1/n);cert_upper=max(cert_upper,float(max(R)/bound))
  # Symmetric representative of minus the gradient killed generator.
  up=b*(n-k-1);down=k*(k-1)/n;V=b+2*k/n
  off=-np.sqrt(up[:-1]*down[1:]); diagonal=up+down+V
  gap=float(la.eigvalsh_tridiagonal(diagonal,off,select='i',select_range=(0,0))[0]) if n>2 else float(diagonal[0])
  count_upper_error=max(count_upper_error,(gap-bound)/bound)
  count_lower_error=max(count_lower_error,(b+2/n-gap)/max(1,gap))
output={'stationary_projection':rows,'count_weight_max_bound_ratio':cert_upper,'count_gap_upper_relative_violation':count_upper_error,'count_gap_curvature_relative_violation':count_lower_error}
pathlib.Path('final_audit.json').write_text(json.dumps(output,indent=2),encoding='utf8');print(json.dumps(output,indent=2))

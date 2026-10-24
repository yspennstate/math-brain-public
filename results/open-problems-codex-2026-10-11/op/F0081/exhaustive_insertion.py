import itertools,json,time
from pathlib import Path
start=time.time();reports=[]
def greedy(weights,n,m):
 a=[float('inf')]*n;b=[float('inf')]*m
 for weight,i,j in sorted((weights[i*m+j],i,j) for i in range(n) for j in range(m)):
  if a[i]==float('inf') and b[j]==float('inf'):a[i]=b[j]=weight
 return a,b
for oldn,m in [(2,2),(3,2)]:
 count=0
 for weights in itertools.permutations(range(1,(oldn+1)*m+1)):
  a,b=greedy(weights,oldn,m);aa,bb=greedy(weights,oldn+1,m)
  assert all(aa[i]>=a[i] for i in range(oldn)) and all(bb[j]<=b[j] for j in range(m))
  for r in range((oldn+1)*m+1):
   inc=[int(aa[i]>r)-int(a[i]>r) for i in range(oldn)]
   dec=[int(b[j]>r)-int(bb[j]>r) for j in range(m)]
   assert all(x>=0 for x in inc+dec) and sum(inc)+sum(dec)+int(aa[-1]>r)==1
  count+=1
 reports.append(dict(old_reds=oldn,blues=m,all_strict_edge_orders=count,thresholds_per_order=(oldn+1)*m+1))
Path('exhaustive_insertion.json').write_text(json.dumps(dict(reports=reports,elapsed=time.time()-start),indent=2))
print(reports,'elapsed',time.time()-start)

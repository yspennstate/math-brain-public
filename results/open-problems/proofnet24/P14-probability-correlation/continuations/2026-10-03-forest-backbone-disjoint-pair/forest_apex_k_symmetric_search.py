from forest_apex_k_countersearch import coefficients,real_roots_with_multiplicity
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

def cases():
 for n in [6,8,10]:
  m=n//2
  yield 'complete_bipartite_'+str(m),n,[(i,m+j)for i in range(m)for j in range(m)]
 yield 'cube',8,[(x,y)for x in range(8)for y in range(x+1,8)if(x^y).bit_count()==1]
 yield 'petersen',10,[(i,(i+1)%5)for i in range(5)]+[(i,i+5)for i in range(5)]+[(i+5,(i+2)%5+5)for i in range(5)]
 for n in [6,8,10]:
  yield 'prism_'+str(n),n,[(i,(i+1)%(n//2))for i in range(n//2)]+[(i+n//2,(i+1)%(n//2)+n//2)for i in range(n//2)]+[(i,i+n//2)for i in range(n//2)]
 yield 'octahedron',6,[(i,j)for i in range(6)for j in range(i+1,6)if i//2!=j//2]

def main():
 report={'status':'finite exact exploration only','cases':[],'counterexample':None}
 for name,n,edges in cases():
  for weight in [F(1,1000),F(1,100),F(1,10),F(1),F(10),F(100),F(1000)]:
   c=coefficients(n,[(u,v,weight)for u,v in edges],[1]*n)
   count=real_roots_with_multiplicity(c)
   entry={'name':name,'n':n,'weight':str(weight),'degree':len(c)-1,'count_real_with_multiplicity':count,'coefficients_ascending':list(map(str,c))}
   report['cases'].append(entry)
   print(name,weight,count,'of',n,flush=True)
   if count!=len(c)-1:report['counterexample']=entry;report['status']='exact counterexample';break
  Path(__file__).with_name('forest_apex_k_symmetric_search_results.json').write_text(json.dumps(report,indent=2)+'\n')
  if report['counterexample']:break
if __name__=='__main__':main()

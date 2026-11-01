"""Exact bounded tests. Integer weights stand for abstract interface dimensions.
No estimated Poisson frontier dimensions are used.
"""
from itertools import product, combinations
from pathlib import Path
import random, json, time

def cut_value(w,side):
 return max([w[i][j] for i in side for j in range(len(w)) if j not in side]+[0])
def min_cut(w):
 n=len(w)
 return min(cut_value(w,{0}|{j+2 for j,b in enumerate(bits) if b})
            for bits in product([False,True],repeat=n-2))
def widest_path(w):
 n=len(w); values=[-1]*n; values[0]=100
 done=set()
 for _ in range(n):
  v=max((i for i in range(n) if i not in done),key=lambda i:values[i])
  done.add(v)
  for u in range(n):
   if u not in done: values[u]=max(values[u],min(values[v],w[v][u]))
 return values[1]
def collapse(w,parent):
 n=max(parent)+1; out=[[0]*n for _ in range(n)]
 for i,j in combinations(range(len(w)),2):
  a,b=parent[i],parent[j]
  if a!=b: out[a][b]=out[b][a]=max(out[a][b],w[i][j])
 return out
start=time.monotonic(); exhaustive=0
for n in [2,3,4,5]:
 edges=list(combinations(range(n),2))
 for vals in product(range(3),repeat=len(edges)):
  w=[[0]*n for _ in range(n)]
  for (i,j),v in zip(edges,vals): w[i][j]=w[j][i]=v
  assert min_cut(w)==widest_path(w)
  exhaustive+=1
random.seed(23102); refined=0
for n in range(3,8):
 for _ in range(100):
  w=[[0]*n for _ in range(n)]
  for i,j in combinations(range(n),2): w[i][j]=w[j][i]=random.randrange(21)
  # Split root 2; terminals 0 and 1 stay singleton groups.
  fine=[row+[0] for row in w]+[[0]*(n+1)]
  for j in range(n):
   if j!=2:
    v=w[2][j]; a=random.randrange(v+1)
    fine[2][j]=fine[j][2]=a
    fine[n][j]=fine[j][n]=v
  fine[2][n]=fine[n][2]=random.randrange(21)
  parent=list(range(n))+[2]
  assert collapse(fine,parent)==w
  assert min_cut(fine)<=min_cut(w)
  # Any inherited cut has exactly the same value before/after refinement.
  for bits in product([False,True],repeat=n-2):
   side={0}|{j+2 for j,b in enumerate(bits) if b}
   lift={i for i in range(n+1) if parent[i] in side}
   assert cut_value(fine,lift)==cut_value(w,side)
  refined+=1
# Small obstruction: fine path r--u--b, with weights 13 and 16.
# Vertex order r,b,u; the unweighted graph is connected.
w=[[0,0,13],[0,0,16],[13,16,0]]
coarse=collapse(w,[0,1,0])
assert min_cut(coarse)==16 and min_cut(w)==13
assert cut_value(w,{0,2})==16 and cut_value(w,{0})==13
result={'exhaustive_graphs':exhaustive,'weight_alphabet':[0,1,2],
 'exhaustive_vertex_counts':[2,3,4,5],'random_refinement_tests':refined,
 'obstruction':{'fine':w,'coarse':coarse,'coarse_min_cut':16,'fine_min_cut':13,
 'inherited_cut':16,'recolored_cut':13},'seed':23102,
 'seconds':time.monotonic()-start,'result':'all assertions passed',
 'scope':'Exact finite graph identities and an abstract obstruction; not a Poisson-coloring counterexample.'}
Path(__file__).with_name('bottleneck_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))

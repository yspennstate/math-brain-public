import json, pathlib
# A finite planar nearest-neighbour arrow system. No Brownian claim is made.
arrows={(0,-2):[-3,-1],(0,2):[1,3],(1,-3):[-2],(1,-1):[0],(1,1):[0],(1,3):[2],(2,-2):[-1],(2,0):[-1,1],(2,2):[1],(3,-1):[0],(3,1):[0]}
def extreme(x,right):
 p=[x]
 for t in range(4): p.append((max if right else min)(arrows[t,p[-1]]))
 return p
def meet(p,q):
 for t in range(1,len(p)):
  if p[t]==q[t] and all(p[u]<q[u] for u in range(1,t)): return t
 return None
r=extreme(-2,True); l=extreme(2,False); a=extreme(-2,False); b=extreme(2,True)
assert meet(r,l)==2 and meet(a,b)==4
out={'arrows':{str(k):v for k,v in arrows.items()},'inward_pair':[r,l],'outward_pair':[a,b],'inward_first_meeting':2,'outward_first_meeting':4,'conclusion':'Distinct source pair has two distinct first meeting points in this finite model; not a counterexample to Brownian-net local finiteness.'}
pathlib.Path('finite_counterexample.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))

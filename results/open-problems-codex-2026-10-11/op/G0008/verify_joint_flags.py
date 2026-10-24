from pathlib import Path
from collections import defaultdict
import json,inspect
from joint_boundary import exact_joint
R=2;marks=[(-1,0),(0,1),(1,0),(0,-1)];rim=[((-1,0),(-1,1)),((-1,1),(0,1)),((0,1),(1,1)),((1,1),(1,0)),((1,0),(1,-1)),((1,-1),(0,-1)),((0,-1),(-1,-1)),((-1,-1),(-1,0))];spokes=[(v,(2*v[0],2*v[1])) for v in marks];eds=rim+spokes;allowed={frozenset(e) for e in eds}
s=inspect.getsource(exact_joint);s=s.replace('if reverse:edges.reverse()','edges=[ed for ed in edges if frozenset(ed) in allowed]\n if reverse:edges.reverse()');scope=exact_joint.__globals__.copy();scope['allowed']=allowed;exec(s,scope);calc=scope['exact_joint'](2,poly=True)
vs=sorted(set(v for e in eds for v in e));idx={v:i for i,v in enumerate(vs)};brute={}
for mask in range(4096):
 roots=list(range(len(vs)))
 def find(i):
  while roots[i]!=i:i=roots[i]
  return i
 for j,(a,b) in enumerate(eds):
  if mask>>j&1:roots[find(idx[a])]=find(idx[b])
 labels={};tokens=[]
 for v in marks:
  root=find(idx[v]);lab=labels.setdefault(root,len(labels));hit=any(find(idx[w])==root and max(abs(w[0]),abs(w[1]))==2 for w in vs);tokens.append(2*lab+int(hit))
 row=brute.setdefault(tuple(tokens),[0]*13);row[mask.bit_count()]+=1
assert brute=={tuple(st['tokens']):st['weight'] for st in calc['states']}
r=json.loads(Path('joint_verification.json').read_text());r['R2_restricted_12_edge_bruteforce_boundary_flag_OR']='PASS: all 4096 configurations, including genuine hit/non-hit blocks';Path('joint_verification.json').write_text(json.dumps(r,indent=2),encoding='utf8');print('NONTRIVIAL_FLAG_BRUTE_FORCE_PASS',len(brute),'states')

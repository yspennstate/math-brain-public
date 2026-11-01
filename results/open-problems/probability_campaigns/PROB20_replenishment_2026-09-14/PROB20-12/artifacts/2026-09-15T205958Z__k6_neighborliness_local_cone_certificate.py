import itertools, collections
P=1000003
V=tuple(range(6)); C=tuple(range(3)); EDGES=list(itertools.combinations(V,2)); EID={e:i for i,e in enumerate(EDGES)}
def edge(e):return tuple(sorted(e))
def ix(c,e):return 15*c+EID[edge(e)]
ST=[]; COL=[]
for col in itertools.product(C,repeat=6):
    if all(col.count(c)==2 for c in C):
        r=[0]*45
        for c in C:
            pts=tuple(v for v in V if col[v]==c); r[ix(c,pts)]=1
        ST.append(r); COL.append(col)
SINDEX={c:i for i,c in enumerate(COL)}; i0=SINDEX[(0,0,1,1,2,2)]

def val(a,r):return sum(x*y for x,y in zip(a,r))
def active(a,b):return frozenset(i for i,r in enumerate(ST) if val(a,r)==b)
def slackvec(a,b):return tuple(b-val(a,r) for r in ST)
def inside(S):return [e for e in EDGES if set(e)<=set(S)]
FAC={}
def put(fam,a,b):
    assert all(val(a,r)<=b for r in ST)
    ac=active(a,b)
    if ac not in FAC: FAC[ac]=(fam,tuple(a),b,slackvec(a,b))
for c in C:
 for e in EDGES:
  a=[0]*45;a[ix(c,e)]=-1;put('nonneg',a,0)
bad={0,63,11,21,38,56}
for tc in C:
 others=[c for c in C if c!=tc];c0,c1=others
 for te in EDGES:
  comp=tuple(v for v in V if v not in te);bases=list(itertools.combinations(comp,2))
  for mask in range(64):
   if mask in bad:continue
   a=[0]*45;a[ix(tc,te)]=1
   for j,B in enumerate(bases):
    co=edge(set(comp)-set(B))
    if (mask>>j)&1:a[ix(c0,B)]-=1
    else:a[ix(c1,co)]-=1
   put('fibre',a,0)
for SS in itertools.combinations(V,3):
 a=[0]*45
 for c in C:
  for e in EDGES:
   if set(e)<=set(SS):a[ix(c,e)]+=1
 put('blossom',a,1)
for tc in C:
 others=[c for c in C if c!=tc]
 for AA in itertools.combinations(V,3):
  A=set(AA);B=set(V)-A;a=[0]*45
  for e in EDGES:
   if set(e)<=A:a[ix(tc,e)]+=1
   if set(e)<=B:
    for c in others:a[ix(c,e)]-=1
  put('s1',a,0)
for tc in C:
 for be in EDGES:
  A=set(V)-set(be);a=[0]*45
  for c in C:
   if c!=tc:
    for e in EDGES:
     if set(e)<=A:a[ix(c,e)]+=1
  a[ix(tc,be)]-=1;put('s2',a,1)
fullgrp=[]
for vp_t in itertools.permutations(V):
 for cp_t in itertools.permutations(C):fullgrp.append((vp_t,cp_t))
def transf(a,g):
 vp,cp=g;out=[0]*45
 for c in C:
  for e in EDGES:out[ix(cp[c],(vp[e[0]],vp[e[1]]))]=a[ix(c,e)]
 return out
L={0,3};D={1,2};R={4,5};SA=[e for e in inside(L|D) if set(e)!=D];SB=[e for e in inside(D|R) if set(e)!=D]
a=[0]*45
for e in SA:a[ix(0,e)]+=1
for c in (1,2):
 for e in SB:a[ix(c,e)]-=1
for g in fullgrp:put('bridge',transf(a,g),0)
T={0,1,3};d=2;RR={4,5};AA=set(inside(T))|{edge((d,r)) for r in RR};BB={edge((d,t)) for t in T}|set(inside(RR));CC={edge((t,r)) for t in T for r in RR}
a=[0]*45
for e in AA:a[ix(0,e)]+=1;a[ix(1,e)]-=1
for e in BB:a[ix(1,e)]+=1;a[ix(2,e)]-=1
for e in CC:a[ix(2,e)]+=1;a[ix(0,e)]-=1
for g in fullgrp:put('residue',transf(a,g),1)
a=[0]*45
for e in [(0,1),(0,2)]:a[ix(0,e)]+=1
for e in [(1,5),(2,5),(3,4),(3,5),(4,5)]:a[ix(1,e)]-=1
for e in [(3,5),(4,5)]:a[ix(2,e)]-=1
for g in fullgrp:put('sparse',transf(a,g),0)
assert len(FAC)==4450
famcnt=collections.Counter(t[0] for t in FAC.values());print('families',dict(famcnt))
ACT={ac:t for ac,t in FAC.items() if i0 in ac}; assert len(ACT)==2985;print('active rays',len(ACT))
pair_face_counts=collections.Counter()
for i in range(90):
 for j in range(i+1,90):
  w=[ST[i][q]+ST[j][q] for q in range(45)]; scores=[val(w,r) for r in ST];mx=max(scores);tops=[k for k,s in enumerate(scores) if s==mx]
  pair_face_counts[len(tops)]+=1
  assert set(tops)=={i,j}
print('pair exposes',dict(pair_face_counts),'edges',90*89//2)
pairs={0:(0,1),1:(2,3),2:(4,5)}; stab=[]
for cp_t in itertools.permutations(C):
 cp={c:cp_t[c] for c in C}
 for flips in itertools.product([0,1],repeat=3):
  vp={}
  for c in C:
   src=pairs[c];dst=pairs[cp[c]];dst=dst[::-1] if flips[c] else dst
   vp[src[0]]=dst[0];vp[src[1]]=dst[1]
  perm=[None]*90
  for ii,s in enumerate(COL):
   t=[None]*6
   for v in V:t[vp[v]]=cp[s[v]]
   perm[ii]=SINDEX[tuple(t)]
  stab.append(perm)
assert len(stab)==48
other=set(range(90))-{i0};seen=set(); worbs=[]
for j in sorted(other):
 if j in seen:continue
 o={p[j] for p in stab};seen|=o;worbs.append(o)
assert sorted(map(len,worbs))==[2,3,8,12,16,24,24]
print('wall orbits',sorted(map(len,worbs)))
facetkeys=set(ACT);seenf=set();forbs=[]
def actset(ac,p):return frozenset(p[i] for i in ac)
for ac in facetkeys:
 if ac in seenf:continue
 o={actset(ac,p) for p in stab};seenf|=o;forbs.append(o)
assert len(forbs)==109
print('ray orbits',len(forbs),collections.Counter(map(len,forbs)))
def rank_mod(rows,p=P):
 if not rows:return 0
 A=[ [x%p for x in row] for row in rows]
 m=len(A);n=len(A[0]);r=0
 for c in range(n):
  piv=next((i for i in range(r,m) if A[i][c]),None)
  if piv is None:continue
  A[r],A[piv]=A[piv],A[r]; inv=pow(A[r][c],p-2,p); A[r]=[(x*inv)%p for x in A[r]]
  for i in range(m):
   if i!=r and A[i][c]:
    t=A[i][c];A[i]=[(a-t*b)%p for a,b in zip(A[i],A[r])]
  r+=1
  if r==m:return r
 return r
for o in sorted(worbs,key=lambda z:(len(z),min(z))):
 j=min(o); rows=[]; fams=collections.Counter()
 for ac,(fam,a,b,s) in ACT.items():
  if j in ac:
   rows.append(s);fams[fam]+=1
 rk=rank_mod(rows)
 assert rk==36
 print('wall',len(o),'rep',j,COL[j],'incident_known',len(rows),'rank_mod',rk,'families',dict(fams))
print('ALL CHECKS PASSED')

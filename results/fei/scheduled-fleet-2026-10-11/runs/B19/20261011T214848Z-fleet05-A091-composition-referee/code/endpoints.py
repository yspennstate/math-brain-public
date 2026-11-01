from check import *
def maj(x):return 1 if sum(x)>0 else -1
def s(x,i):return 1 if x>>i&1 else -1
# Fix first majority coordinate to +1, retaining two physical inputs and fresh z.
t=tuple(1 if maj((1,s(x,0),s(x,1)))==1 and s(x,2)==1 else -1 for x in range(8))
r,P=spectrum(t,(Q(1,2),)*3)
check(r[0],Q(-1,4));check(inf(P),Q(5,4))
check(sorted(P),[Q(1,16)]*7+[Q(9,16)])
check(ent(P),{2:Q(4),3:Q(-9,8)})
# Shared data majority pair; selectors disjoint from all four data coordinates.
u=tuple(maj((s(y,0),s(y,1),s(y,2))) for y in range(16))
v=tuple(maj((s(y,0),-s(y,1),s(y,3))) for y in range(16))
check(sum(a*b for a,b in zip(u,v)),0)
tf=tuple((u,v)[x&1][x>>1] for x in range(32))
PF=tuple(c*c for c in uniform_coeff(tf))
check(sorted(p for p in PF if p),[Q(1,16)]*8+[Q(1,4)]*2)
check(ent(PF),{2:Q(3)});check(inf(PF),Q(2))
# B09 tensor-only scope counter: literal child channels are point masses.
t=tuple(1 if x==3 else -1 for x in range(4))
_,P=spectrum(t,(Q(1,2),)*2)
check(P,(Q(1,4),)*4)
q=(P[0]+P[1],P[2]+P[3])
M=add((1,ent(P)),(-1,ent(q)))
J=ent(q) # actual physical children: constant and unbiased literal, both spectral H=0
check(M,{2:Q(1)});check(J,{2:Q(1)})
out={'cases':3,'A056_restriction':'PASS','shared_majority_pair':'PASS','AND_child_ledger_additivity_counter':'M=1,J=1; child M=J=0','arithmetic':'Fraction/direct Walsh/prime-log vectors','status':'PASS'}
(ROOT/'out/endpoints.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))

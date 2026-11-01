from collections import deque, Counter, defaultdict
from fractions import Fraction

# Exact arithmetic in Z[a,b], a^2=2, b^2=b+1 (b=phi).
def add(x,y):
    return (x[0]+y[0],x[1]+y[1],x[2]+y[2],x[3]+y[3])
def mul(x,y):
    x0,x1,x2,x3=x; y0,y1,y2,y3=y
    return (
        x0*y0 + 2*x1*y1 + x2*y2 + 2*x3*y3,
        x0*y1 + x1*y0 + x2*y3 + x3*y2,
        x0*y2 + x2*y0 + x2*y2 + 2*x1*y3 + 2*x3*y1 + 2*x3*y3,
        x0*y3 + x3*y0 + x1*y2 + x2*y1 + x2*y3 + x3*y2,
    )
Z=(0,0,0,0); ONE=(1,0,0,0); A=(0,1,0,0); B=(0,0,1,0); MONE=(-1,0,0,0)
def sring(items):
    z=Z
    for x in items: z=add(z,x)
    return z
def mm(X,Y):
    return tuple(tuple(sring(mul(X[i][k],Y[k][j]) for k in range(3)) for j in range(3)) for i in range(3))
def mv(X,v):
    return tuple(sring(mul(X[i][k],v[k]) for k in range(3)) for i in range(3))
I=tuple(tuple(ONE if i==j else Z for j in range(3)) for i in range(3))
def mpow(X,n):
    Y=I
    for _ in range(n): Y=mm(X,Y)
    return Y

S1=((MONE,A,Z),(Z,ONE,Z),(Z,Z,ONE))
S2=((ONE,Z,Z),(A,MONE,B),(Z,Z,ONE))
S3=((ONE,Z,Z),(Z,ONE,Z),(Z,B,MONE))
assert mm(S1,S1)==I and mm(S2,S2)==I and mm(S3,S3)==I
assert mpow(mm(S1,S2),4)==I and mpow(mm(S2,S3),5)==I and mpow(mm(S1,S3),2)==I

R=mm(S2,S3); Ri=mpow(R,4)
Q=mm(mm(S1,R),S1); Qi=mpow(Q,4)
assert mpow(R,5)==I and mpow(Q,5)==I
# New exact triangle-group relation: (r q^{-1})^2=1.
assert mpow(mm(R,Qi),2)==I

MID=(A,(2,0,0,0),B)
assert mv(S1,MID)==MID and mv(S3,MID)==MID
NAMES=('r','R','q','Q'); GENS=(R,Ri,Q,Qi); GD=dict(zip(NAMES,GENS))
assert len({mv(g,MID) for g in GENS})==4

MAX_R=18
dist={MID:0}; q=deque([MID])
while q:
    v=q.popleft(); d=dist[v]
    if d==MAX_R: continue
    for g in GENS:
        w=mv(g,v)
        if w not in dist:
            dist[w]=d+1; q.append(w)

byd=defaultdict(list)
for v,d in dist.items(): byd[d].append(v)
shell=[len(byd[n]) for n in range(MAX_R+1)]
expected=[1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,17934,33178,61450,113708,210566]
assert shell==expected

# New rigorous ball upper bound at radius 16.
B16=sum(shell[:17]); bd17=shell[17]
ratio=Fraction(bd17,B16)
assert B16==133611 and bd17==113708 and ratio==Fraction(113708,133611)
assert ratio < Fraction(33178,38983)
margin=33178*133611-113708*38983
assert margin==266794

# Exact finite shell anatomy. For all fully exposed layers 1..17 every vertex is one of:
# A=(one arrival,no fraternal,three departures),
# B=(one arrival,one fraternal,two departures),
# C=(two arrivals,no fraternal,two departures).
ABC={}
for n in range(1,18):
    ctr=Counter()
    for v in byd[n]:
        ds=[dist[mv(g,v)]-n for g in GENS]
        t=(ds.count(-1),ds.count(0),ds.count(1))
        ctr[t]+=1
    assert set(ctr) <= {(1,0,3),(1,1,2),(2,0,2)}
    ABC[n]=(ctr[(1,0,3)],ctr[(1,1,2)],ctr[(2,0,2)])
expected_abc={
1:(4,0,0),2:(4,4,2),3:(4,12,4),4:(8,24,6),5:(16,40,14),6:(32,72,26),
7:(56,132,52),8:(104,252,90),9:(188,464,172),10:(356,864,308),11:(652,1584,588),
12:(1220,2948,1066),13:(2236,5436,2008),14:(4168,10104,3662),15:(7672,18648,6858),
16:(14272,34600,12578),17:(26320,63924,23464)}
assert ABC==expected_abc

# Exact face profiles of fraternal edges. The square partner under the directed Cayley model.
partner={'r':'Q','R':'q','q':'R','Q':'r'}
seen=set(); X=Counter(); Y=Counter()
profile_X=((0,0,-1,-2,-1,0),(0,0,1,1,0))   # pentagon inward, square outward
profile_Y=((0,0,1,2,1,0),(0,0,-1,-1,0))   # pentagon outward, square inward
for n in range(2,17):
    for v in byd[n]:
        for name,g in zip(NAMES,GENS):
            w=mv(g,v)
            if dist[w]!=n: continue
            key=(v,w) if v<w else (w,v)
            if key in seen: continue
            seen.add(key)
            # Pentagon containing this edge: repeat its order-five generator.
            pp=[v]; cur=v
            for _ in range(5):
                cur=mv(GD[name],cur); pp.append(cur)
            assert pp[-1]==v
            # Square containing this edge: alternate with the unique non-backtracking square partner.
            sp=[v,w]; cur=w; h=partner[name]
            for lab in (h,name,h):
                cur=mv(GD[lab],cur); sp.append(cur)
            assert sp[-1]==v
            pprof=tuple(dist[z]-n for z in pp)
            sprof=tuple(dist[z]-n for z in sp)
            if (pprof,sprof)==profile_X: X[n]+=1
            elif (pprof,sprof)==profile_Y: Y[n]+=1
            else: raise AssertionError((n,pprof,sprof))

# Every B vertex is an endpoint of exactly one fraternal edge.
for n in range(2,17):
    assert ABC[n][1] == 2*(X[n]+Y[n])
for n in range(3,17):
    assert Y[n]==X[n-1]

# Split C by the face closed between its two arrival edges.
square_pairs={frozenset(('r','q')),frozenset(('R','Q'))}
pent_pairs={frozenset(('r','R')),frozenset(('q','Q'))}
C4=Counter(); C5=Counter()
for n in range(2,18):
    for v in byd[n]:
        parents=[name for name,g in zip(NAMES,GENS) if dist[mv(g,v)]==n-1]
        if len(parents)==2:
            pair=frozenset(parents)
            if pair in square_pairs: C4[n]+=1
            elif pair in pent_pairs: C5[n]+=1
            else: raise AssertionError((n,parents))
    assert C4[n]+C5[n]==ABC[n][2]

# Finite instances of the face-start/face-close identities that motivate the all-generation reduction.
for n in range(3,15):
    assert C5[n+2]==Y[n]
    # Number Q_n of square faces starting at generation n can be read both locally and as C4_{n+2}.
    Qn=ABC[n][0] + 2*Y[n] + C4[n]
    assert C4[n+2]==Qn
    # Number P_n of pentagons starting at generation n closes as X at generation n+2.
    Pn=ABC[n][0] + 2*X[n] + C5[n]
    assert X[n+2]==Pn

# The candidate scalar recurrence now has exact finite support through n=18.
for n in range(7,19):
    rhs=(shell[n-1] + 2*shell[n-2] - 2*shell[n-3]
         + 2*shell[n-4] + shell[n-5] - shell[n-6])
    assert shell[n]==rhs

print('EXACT_TRIANGLE_RELATION_PASS', '(r*Q)^2=1')
print('T_SHELLS_0_TO_18', shell)
print('T_RADIUS16_BALL', B16)
print('T_RADIUS16_OUTER_VERTEX_BOUNDARY', bd17)
print('T_RADIUS16_RATIO', f'{ratio.numerator}/{ratio.denominator}')
print('STRICT_IMPROVEMENT_OVER_33178_38983_MARGIN', margin)
print('ABC_COUNTS_1_TO_17', [ABC[n] for n in range(1,18)])
print('X_COUNTS_2_TO_16', [X[n] for n in range(2,17)])
print('Y_COUNTS_2_TO_16', [Y[n] for n in range(2,17)])
print('FINITE_FACE_STATE_IDENTITIES_N_3_TO_14_PASS')
print('FINITE_RECURRENCE_CHECK_N_7_TO_18_PASS')
print('CANDIDATE_RECURRENCE', 'S_n=S_(n-1)+2S_(n-2)-2S_(n-3)+2S_(n-4)+S_(n-5)-S_(n-6)')
print('ALL_EXACT_CHECKS_PASS')

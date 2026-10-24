"""Exact finite-width algebra checks; not stable-network asymptotic evidence."""
from fractions import Fraction as F

def dot(a,b): return sum((x*y for x,y in zip(a,b)), F(0))
def mv(A,x): return [dot(row,x) for row in A]
def tr(A): return list(map(list,zip(*A)))
def mm(A,B): return [[dot(row,col) for col in tr(B)] for row in A]
def add(a,b): return [x+y for x,y in zip(a,b)]
def sub(a,b): return [x-y for x,y in zip(a,b)]
def scl(c,a): return [c*x for x in a]
def relu(v): return [max(F(0),x) for x in v]
def sumvec(vs,k): return [sum((v[j] for v in vs),F(0)) for j in range(k)]

X=[[F(1),F(0),F(0)],[F(3,5),F(4,5),F(0)]]
Z=[[F(-1),F(0),F(1)],[F(0),F(1),F(0)],[F(1),F(-2),F(3)]]
Gi=[[F(25,16),F(-15,16)],[F(-15,16),F(25,16)]]
K=mm(mm(Z,tr(X)),Gi)
assert mm(K,X)==[row[:2]+[F(0)] for row in Z]
a,L,gamma=F(2),F(3),F(1,4)
h=gamma/L
U=[[F(1),F(-1),F(2)],[F(-1,2),F(2),F(-3)],[F(-2),F(-1),F(4)]]
W=[F(2),F(-1),F(1,2)]
y=[F(1,3),F(-2,3)]
U0=[u[:] for u in U]; W0=W[:]
history=[]
for n in range(6):
    H=[relu(mv(X,u)) for u in U]
    B=[relu(mv(Z,u)) for u in U]
    f=scl(1/(a*L),sumvec([scl(w,v) for w,v in zip(W,H)],2))
    ft=scl(1/(a*L),sumvec([scl(w,v) for w,v in zip(W,B)],3))
    r=sub(y,f)
    history.append((H,B,r,ft))
    for i,u in enumerate(U):
        initial_offset=sub(mv(Z,U0[i]),mv(K,mv(X,U0[i])))
        assert mv(Z,u)==add(mv(K,mv(X,u)),initial_offset)
    if n:
        endpoint=scl(1/L,sumvec([scl(W0[i]/a,sub(B[i],history[0][1][i])) for i in range(3)],3))
        gram_term=[F(0)]*3
        for j in range(n):
            Hj,_,rj,_=history[j]
            gram_term=add(gram_term,scl(h/(a*a),sumvec([scl(dot(Hj[i],rj),B[i]) for i in range(3)],3)))
        assert sub(ft,history[0][3])==add(endpoint,gram_term)
    if n==5: break
    newU=[]; newW=[]
    for i,u in enumerate(U):
        v=mv(X,u)
        gated=[r[j] if v[j]>0 else F(0) for j in range(2)]
        newU.append(add(u,scl((gamma/a)*W[i],mv(tr(X),gated))))
        newW.append(W[i]+(gamma/a)*dot(r,H[i]))
    U,W=newU,newW

q=[F(1),F(1)]
assert relu(mv(K,q)) != mv(K,relu(q))
print('PASS: 18 exact row projection identities over 6 grid states.')
print('PASS: 15 scalar test-output integration-by-parts identities over 5 nonzero times.')
print('PASS: retained orthogonal initial offsets are preserved exactly at finite width.')
print('PASS: ReLU after K differs from moving K outside ReLU.')
print('K =', [[str(v) for v in row] for row in K])
print('Deterministic Fraction arithmetic only; not a stable-network simulation or rate estimate.')

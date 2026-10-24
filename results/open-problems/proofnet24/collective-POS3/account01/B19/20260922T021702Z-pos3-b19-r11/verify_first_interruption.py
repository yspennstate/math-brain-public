from itertools import product, combinations
from fractions import Fraction

def seqs(n,m,lo=0):
    if n==0:
        yield ()
        return
    def rec(pref,a):
        if len(pref)==n:
            yield tuple(pref); return
        for x in range(a,m+1):
            pref.append(x); yield from rec(pref,x); pref.pop()
    yield from rec([],lo)

def weight(lams,m):
    return sum(all(ti>=li for ti,li in zip(t,lams)) for t in seqs(len(lams),m))

def tail_weight(tail,m,j):
    return sum(t and t[0]>=j and all(ti>=li for ti,li in zip(t,tail))
               for t in seqs(len(tail),m)) if tail else 1

cases=0
for m in range(1,5):
  for n in range(1,6):
    for lams in product(range(m+1),repeat=n):
      W=weight(lams,m)
      if lams[0]==m:
        assert W==1
      else:
        assert W-1==sum(tail_weight(lams[1:],m,j) for j in range(lams[0],m))
      cases+=1

def closure(n,covers):
    R=[[False]*n for _ in range(n)]
    for i,j in covers:R[i][j]=True
    for k in range(n):
      for i in range(n):
        if R[i][k]:
          for j in range(n):
            if R[k][j]:R[i][j]=True
    return R

def linexts(R):
    n=len(R); pred=[{i for i in range(n) if R[i][j]} for j in range(n)]
    out=[]
    def rec(p,u):
      if len(p)==n: out.append(tuple(p)); return
      for v in range(n):
        if v not in u and pred[v]<=u: rec(p+[v],u|{v})
    rec([],set()); return out

def width(R):
    n=len(R); w=0
    for mask in range(1<<n):
      A=[i for i in range(n) if mask>>i&1]
      if all(not R[i][j] and not R[j][i] for i,j in combinations(A,2)): w=max(w,len(A))
    return w

covers=[(0,2),(0,3),(1,2),(2,4),(2,5)]
Q=closure(6,covers); lam=[4,3,4,4,4,4]; m=4
QE=linexts(Q); ws=[weight([lam[q] for q in e],m) for e in QE]
mins=[q for q in range(6) if not any(Q[r][q] for r in range(6))]
M=[q for q in mins if lam[q]<m]
assert len(QE)==18 and sum(ws)==26 and M==[1]
u=sum(e.index(2)<e.index(3) for e in QE)
z=sum(w for e,w in zip(QE,ws) if e.index(2)<e.index(3))
assert Fraction(u,len(QE))==Fraction(2,3)
assert Fraction(z,sum(ws))==Fraction(9,13)

N=m+6
P=[[False]*N for _ in range(N)]
for i in range(m):
  for j in range(i+1,m):P[i][j]=True
for i in range(6):
  for j in range(6):
    if Q[i][j]:P[m+i][m+j]=True
for q,l in enumerate(lam):
  for i in range(l):P[i][m+q]=True
for k in range(N):
  for i in range(N):
    if P[i][k]:
      for j in range(N):
        if P[k][j]:P[i][j]=True
PE=linexts(P)
assert len(PE)==26 and width(P)==3
c4q1=sum(e.index(3)<e.index(5) for e in PE)
q4q5=sum(e.index(8)<e.index(9) for e in PE)
assert Fraction(c4q1,len(PE))==Fraction(9,13)
assert Fraction(q4q5,len(PE))==Fraction(1,2)

print("POS3_FIRST_INTERRUPTION_RENEWAL_CHECK_PASS")
print("word_cases",cases)
print("Q_extensions",len(QE),"P_extensions",len(PE),"M",M)
print("Pr_Q(q2<q3)",Fraction(u,len(QE)))
print("Pr_P(q2<q3)",Fraction(z,sum(ws)))
print("Pr_P(c4<q1)",Fraction(c4q1,len(PE)))
print("Pr_P(q4<q5)",Fraction(q4q5,len(PE)))

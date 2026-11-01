from fractions import Fraction
from collections import defaultdict
from math import comb


def canon_edge(a,b):
    return tuple(sorted((a,b)))


def simple_paths_z2(target_n, maxlen):
    start=(0,0); target=(target_n,0); paths=[]
    def rec(v, path, used):
        steps=len(path)
        dist=abs(v[0]-target[0])+abs(v[1]-target[1])
        if steps+dist>maxlen:
            return
        if v==target:
            paths.append(tuple(path)); return
        if steps>=maxlen:
            return
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            w=(v[0]+dx,v[1]+dy)
            if w in used:
                continue
            rec(w,path+[canon_edge(v,w)],used|{w})
    rec(start,[],{start})
    return paths


def poly_add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c


def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def poly_pow_1_minus_p(k):
    return [((-1)**j)*comb(k,j) for j in range(k+1)]


def derivative(a):
    return [(i+1)*a[i+1] for i in range(len(a)-1)]


def eval_poly(a,x):
    out=Fraction(0,1)
    for coeff in reversed(a): out=out*x+coeff
    return out

# Part A: actual Z^2 two-valued FPP at n=2,3.
p2=simple_paths_z2(2,4)
p3=simple_paths_z2(3,6)
assert set(map(len,p2))=={2,4}
assert set(map(len,p3))=={3,5}
edges=sorted({e for path in p2+p3 for e in path})
assert len(edges)==17
idx={e:i for i,e in enumerate(edges)}
p2i=[[idx[e] for e in path] for path in p2]
p3i=[[idx[e] for e in path] for path in p3]
N=1<<len(edges)
count2=defaultdict(int); count3=defaultdict(int)
s2=s3=s22=s33=s23=0
for mask in range(N):
    def cost(path):
        return len(path)+sum((mask>>i)&1 for i in path)
    t2=min(cost(path) for path in p2i)
    t3=min(cost(path) for path in p3i)
    count2[t2]+=1; count3[t3]+=1
    s2+=t2; s3+=t3; s22+=t2*t2; s33+=t3*t3; s23+=t2*t3
m2=Fraction(s2,N); m3=Fraction(s3,N)
v2=Fraction(s22,N)-m2*m2
v3=Fraction(s33,N)-m3*m3
c23=Fraction(s23,N)-m2*m3
cyz=c23-v2
vz=v3+v2-2*c23
assert dict(count2)=={2:32768,3:65536,4:32768}
assert dict(count3)=={3:16384,4:49152,5:50160,6:15376}
assert m2==3 and v2==Fraction(1,2)
assert m3==Fraction(36801,8192)
assert v3==Fraction(49295487,67108864)
assert c23==Fraction(4033,8192)
assert cyz==Fraction(-63,8192)
assert v3-v2==2*cyz+vz

# Part B: exact finite shortest-path counterexample to global density convexity.
gedges=[(0,1),(0,3),(1,2),(1,3),(1,4),(2,4),(3,4)]
adj=defaultdict(list)
for i,(a,b) in enumerate(gedges):
    adj[a].append((b,i)); adj[b].append((a,i))
gpaths=[]
def grec(v,used,path):
    if v==2:
        gpaths.append(tuple(path)); return
    for w,i in adj[v]:
        if w in used: continue
        grec(w,used|{w},path+[i])
grec(0,{0},[])
layer_sum=[0]*8
for mask in range(1<<7):
    k=mask.bit_count()
    t=min(len(path)+sum((mask>>i)&1 for i in path) for path in gpaths)
    layer_sum[k]+=t
assert layer_sum==[2,16,53,98,109,72,26,4]
# h(p)=sum_k layer_sum[k] p^k(1-p)^(7-k)
poly=[0]
for k,L in enumerate(layer_sum):
    term=[0]*k+[L]
    term=poly_mul(term,poly_pow_1_minus_p(7-k))
    poly=poly_add(poly,term)
while len(poly)>1 and poly[-1]==0: poly.pop()
assert poly==[2,2,-1,3,-3,1]
d2=derivative(derivative(poly))
assert d2==[-2,18,-36,20]
assert eval_poly(d2,Fraction(7,10))==Fraction(-9,50)
assert eval_poly(d2,Fraction(1,2))==Fraction(1,2)

print('R12 I0060 B2 exact checker')
print(f'Z2 relevant_edges={len(edges)} configs={N} paths_n2={len(p2)} paths_n3={len(p3)}')
print('T2 counts:', dict(sorted(count2.items())))
print('T3 counts:', dict(sorted(count3.items())))
print('E[T2]=', m2, 'Var(T2)=', v2)
print('E[T3]=', m3, 'Var(T3)=', v3)
print('Cov(T2,T3)=', c23)
print('Cov(T2-E[T2], (T3-T2)-E[T3-T2])=', cyz)
print('Var(T3-T2)=', vz)
print('Variance increment identity:', v3-v2, '=', 2*cyz+vz)
print('finite graph layer sums:', layer_sum)
print('h coefficients low-to-high:', poly)
print("h'' coefficients low-to-high:", d2)
print("h''(7/10)=", eval_poly(d2,Fraction(7,10)))
print("h''(1/2)=", eval_poly(d2,Fraction(1,2)))
print('ALL_EXACT_CHECKS_PASS')

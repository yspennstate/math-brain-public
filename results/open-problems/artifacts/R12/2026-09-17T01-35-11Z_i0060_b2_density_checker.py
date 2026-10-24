from fractions import Fraction
from math import comb


def canon_edge(a,b):
    return tuple(sorted((a,b)))

def simple_paths_z2(target_n,maxlen):
    out=[]
    def rec(v,used,path):
        d=abs(v[0]-target_n)+abs(v[1])
        if len(path)+d>maxlen: return
        if v==(target_n,0): out.append(tuple(path)); return
        if len(path)>=maxlen: return
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            w=(v[0]+dx,v[1]+dy)
            if w in used: continue
            rec(w,used|{w},path+[canon_edge(v,w)])
    rec((0,0),{(0,0)},[])
    return out

def poly_add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def one_minus_p_pow(k):
    return [(-1)**j*comb(k,j) for j in range(k+1)]

def derivative(a):
    return [(i+1)*a[i+1] for i in range(len(a)-1)]

def eval_poly(a,x):
    out=Fraction(0,1)
    for c in reversed(a): out=out*x+c
    return out

p2=simple_paths_z2(2,4)
p3=simple_paths_z2(3,6)
edges=sorted({e for P in p2+p3 for e in P})
assert len(edges)==17
idx={e:i for i,e in enumerate(edges)}
p3i=[[idx[e] for e in P] for P in p3]
layer_sum=[0]*18
for mask in range(1<<17):
    k=mask.bit_count()
    def cost(P): return len(P)+sum((mask>>i)&1 for i in P)
    layer_sum[k]+=min(cost(P) for P in p3i)
assert layer_sum==[3,54,456,2399,8806,23958,50068,82117,106998,111372,92592,61134,31666,12600,3720,768,99,6]

# If an edge is expensive (weight 2) with probability p, then
# h_3(p)=sum_k layer_sum[k] p^k(1-p)^(17-k).
poly=[0]
for k,L in enumerate(layer_sum):
    poly=poly_add(poly,poly_mul([0]*k+[L],one_minus_p_pow(17-k)))
while len(poly)>1 and poly[-1]==0: poly.pop()
expected=[3,3,0,-1,0,25,-100,200,-250,210,-120,45,-10,1]
assert poly==expected
second=derivative(derivative(poly))
assert eval_poly(second,Fraction(1,5))==Fraction(-1938944,48828125)
assert eval_poly(second,Fraction(1,2))==Fraction(73,512)
assert eval_poly(second,Fraction(3,5))==Fraction(-3235968,48828125)

print('R12 I0060 source-valid B2 density checker')
print('relevant_edges=',len(edges),'configs=',1<<17,'paths_n3=',len(p3))
print('layer sums:',layer_sum)
print('h3 coefficients low-to-high:',poly)
print("h3'' coefficients low-to-high:",second)
print("h3''(1/5)=",eval_poly(second,Fraction(1,5)))
print("h3''(1/2)=",eval_poly(second,Fraction(1,2)))
print("h3''(3/5)=",eval_poly(second,Fraction(3,5)))
print('ALL_EXACT_CHECKS_PASS')

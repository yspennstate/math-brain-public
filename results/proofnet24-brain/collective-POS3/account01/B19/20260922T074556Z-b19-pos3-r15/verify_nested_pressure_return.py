from functools import lru_cache
from itertools import combinations

M = 3
PFX = [(0,1),(0,2),(0,2)]
J = (0,1)
A = (1,2)
B = (0,3)
SFX = [(0,3),(2,3),(0,3)]


def wc(seq):
    f = [int(seq[0][0] <= r <= seq[0][1]) for r in range(M+1)]
    for lo, hi in seq[1:]:
        c=[]; s=0
        for z in f:
            s += z; c.append(s)
        f = [c[r] if lo <= r <= hi else 0 for r in range(M+1)]
    return sum(f)


def prefix_state(seq):
    f = [int(seq[0][0] <= r <= seq[0][1]) for r in range(M+1)]
    for lo, hi in seq[1:]:
        c=[]; s=0
        for z in f:
            s += z; c.append(s)
        f = [c[r] if lo <= r <= hi else 0 for r in range(M+1)]
    return f


def suffix_state(seq):
    f = [int(seq[-1][0] <= r <= seq[-1][1]) for r in range(M+1)]
    for lo, hi in reversed(seq[:-1]):
        c=[0]*(M+1); s=0
        for r in range(M,-1,-1):
            s += f[r]; c[r]=s
        f = [c[r] if lo <= r <= hi else 0 for r in range(M+1)]
    return f


def cum_left(p):
    out=[]; s=0
    for z in p:
        s += z; out.append(s)
    return out


def cum_right(q):
    out=[0]*len(q); s=0
    for r in range(len(q)-1,-1,-1):
        s += q[r]; out[r]=s
    return out


def determinant_defect(prefix, suffix):
    p=prefix_state(prefix); q=suffix_state(suffix)
    U=cum_left(p); V=cum_right(q)
    UA=U[1]+U[2]; UL=U[0]; VA=V[1]+V[2]; VR=V[3]
    return UA*VR-UL*VA, (UA,UL,VA,VR)


def build_poset(k):
    js=[f'j{i+1}' for i in range(k)]
    names=['c1','c2','c3','p1','p2','p3']+js+['u','v','s1','s2','s3']
    rel={('c1','c2'),('c2','c3')}
    prof={'p1':(0,1),'p2':(0,2),'p3':(0,2),'u':(1,2),'v':(0,3),'s1':(0,3),'s2':(2,3),'s3':(0,3)}
    for z in js: prof[z]=(0,1)
    D=['p1','p2','p3','u','s2']
    E=js+['v','s1','s3']
    for ch in (D,E): rel.update(zip(ch,ch[1:]))
    C=['c1','c2','c3']
    for x,(la,rho) in prof.items():
        for i,c in enumerate(C,1):
            if i <= la: rel.add((c,x))
            if i >= rho+1: rel.add((x,c))
    changed=True
    while changed:
        changed=False; nxt=set(rel)
        for a,b in rel:
            for c,d in rel:
                if b == c and a != d and (a,d) not in nxt:
                    nxt.add((a,d)); changed=True
        rel=nxt
    return names,rel,js


def width(names,rel):
    best=0
    for r in range(1,len(names)+1):
        for S in combinations(names,r):
            if all((x,y) not in rel and (y,x) not in rel for x,y in combinations(S,2)):
                best=r
    return best


def valid_q_order(order,rel):
    pos={x:i for i,x in enumerate(order)}
    return all(a not in pos or b not in pos or pos[a] < pos[b] for a,b in rel)


def full_counts(names,rel,x,y):
    idx={z:i for i,z in enumerate(names)}
    pred=[0]*len(names)
    for a,b in rel: pred[idx[b]] |= 1<<idx[a]
    allmask=(1<<len(names))-1
    @lru_cache(None)
    def F(mask):
        if mask == allmask: return 1
        return sum(F(mask|(1<<i)) for i in range(len(names)) if not (mask>>i)&1 and pred[i]&~mask == 0)
    ix,iy=idx[x],idx[y]
    @lru_cache(None)
    def H(mask,state):
        if mask == allmask: return int(state == 1)
        ans=0
        for i in range(len(names)):
            if not (mask>>i)&1 and pred[i]&~mask == 0:
                ns=state
                if state == 0:
                    if i == ix: ns=1
                    elif i == iy: ns=2
                ans += H(mask|(1<<i),ns)
        return ans
    return F(0),H(0,0)

expected=[(93,91,2),(85,86,-1),(102,101,1)]
press=[]
for k in range(3):
    pre=PFX+[J]*k
    x=wc(pre+[A,B]+SFX); y=wc(pre+[B,A]+SFX)
    d,p=determinant_defect(pre,SFX)
    assert (x,y,x-y) == expected[k]
    assert d == x-y
    press.append((d,p))
assert press == [(2,(13,1,11,1)),(-1,(10,1,11,1)),(1,(12,1,11,1))]

full=[]
for k in range(3):
    names,rel,js=build_poset(k)
    sk=['p1','p2','p3']+js+['u','v','s1','s2','s3']
    sw=sk.copy(); iu=sw.index('u'); iv=sw.index('v'); sw[iu],sw[iv]=sw[iv],sw[iu]
    assert width(names,rel) == 3
    assert ('u','v') not in rel and ('v','u') not in rel
    assert valid_q_order(sk,rel) and valid_q_order(sw,rel)
    E,N=full_counts(names,rel,'c3','s2')
    assert 2*N == E
    full.append((k,E,N))
assert full == [(0,4290,2145),(1,11546,5773),(2,25770,12885)]
print('defects', [z[0] for z in press])
print('pressures_UA_UL_VA_VR', [z[1] for z in press])
print('full_extension_half_pairs', full)
print('POS3_NESTED_PRESSURE_RETURN_COUNTEREXAMPLE_PASS')

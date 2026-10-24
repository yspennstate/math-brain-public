from itertools import product
from collections import defaultdict, deque

def components(state):
    adj = defaultdict(list)
    for r in range(3):
        for c in range(3):
            s = state[3*r+c]
            if s:
                adj[("r",r)].append(("c",c))
                adj[("c",c)].append(("r",r))
    seen=set(); out=[]
    for v in [("r",r) for r in range(3)] + [("c",c) for c in range(3)]:
        if v in seen or not adj[v]:
            continue
        stack=[v]; seen.add(v); comp=[]
        while stack:
            x=stack.pop(); comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        out.append(comp)
    return out

def necessary_support_conditions(state):
    for r in range(3):
        if all(state[3*r+c] == 0 for c in range(3)):
            return False
    for c in range(3):
        if all(state[3*r+c] == 0 for r in range(3)):
            return False

    for comp in components(state):
        nr=sum(t=="r" for t,_ in comp)
        nc=sum(t=="c" for t,_ in comp)
        if nr != nc:
            return False

    for r1 in range(3):
        for r2 in range(r1+1,3):
            same=opp=0
            for c in range(3):
                x,y=state[3*r1+c], state[3*r2+c]
                if x and y:
                    if x*y == 1: same += 1
                    else: opp += 1
            if same == 1 or opp == 1:
                return False

    for c1 in range(3):
        for c2 in range(c1+1,3):
            same=opp=0
            for r in range(3):
                x,y=state[3*r+c1], state[3*r+c2]
                if x and y:
                    if x*y == 1: same += 1
                    else: opp += 1
            if same == 1 or opp == 1:
                return False
    return True

def solve_gauge(state):
    rs=[None]*3; cs=[None]*3
    for r0 in range(3):
        if rs[r0] is not None:
            continue
        if not any(state[3*r0+c] for c in range(3)):
            continue
        rs[r0]=1
        q=deque([("r",r0)])
        while q:
            typ,i=q.popleft()
            if typ=="r":
                for c in range(3):
                    s=state[3*i+c]
                    if not s: continue
                    want=s*rs[i]
                    if cs[c] is None:
                        cs[c]=want; q.append(("c",c))
                    elif cs[c] != want:
                        return None
            else:
                c=i
                for r in range(3):
                    s=state[3*r+c]
                    if not s: continue
                    want=s*cs[c]
                    if rs[r] is None:
                        rs[r]=want; q.append(("r",r))
                    elif rs[r] != want:
                        return None
    return rs,cs

def even_even_adjustable(state, gauge):
    rs,cs = map(list,gauge)
    comps=components(state)
    for flips in product((1,-1), repeat=len(comps)):
        rr=rs[:]; cc=cs[:]
        for comp,f in zip(comps,flips):
            if f == -1:
                for typ,i in comp:
                    if typ=="r": rr[i]*=-1
                    else: cc[i]*=-1
        if sum(x==-1 for x in rr)%2 == 0 and sum(x==-1 for x in cc)%2 == 0:
            return True
    return False

def gram_chi_identity(a,b,c,d):
    # m=a+ib, n=c+id; B is the real matrix of z -> mz+n zbar.
    B00=a+c
    B01=d-b
    B10=b+d
    B11=a-c
    s00=B00*B00+B01*B01
    s11=B10*B10+B11*B11
    s01=B00*B10+B01*B11
    # chi(BB^T) = ((s00-s11)/2) + i*s01 = 2mn.
    return (s00-s11 == 4*(a*c-b*d) and s01 == 2*(a*d+b*c))

admissible=0
balanced_failures=0
det_compatible=0
even_even_failures=0

for state in product((-1,0,1), repeat=9):
    if not necessary_support_conditions(state):
        continue
    admissible += 1
    gauge=solve_gauge(state)
    if gauge is None:
        balanced_failures += 1
        continue

    rs,cs=gauge
    # An actual O in SO(6) that becomes complex-linear after this gauge
    # necessarily has an even total number of coordinate conjugations.
    if (sum(x==-1 for x in rs)+sum(x==-1 for x in cs)) % 2:
        continue
    det_compatible += 1
    if not even_even_adjustable(state,gauge):
        even_even_failures += 1

sample_count=0
for a,b,c,d in product((-1,0,1), repeat=4):
    sample_count += 1
    assert gram_chi_identity(a,b,c,d)

# Exact non-vacuity check for a structured spectral coefficient X already
# present in the shared campaign (account03/B20 r11).
X = ((-284,-294,-148),(-624,-430,-376),(1110,1100,590))
r1 = tuple(X[0][j]-X[1][j] for j in range(3))
r2 = tuple(X[0][j]-X[2][j] for j in range(3))
omega = (
    r1[1]*r2[2]-r1[2]*r2[1]
    - (r1[0]*r2[2]-r1[2]*r2[0])
    + (r1[0]*r2[1]-r1[1]*r2[0])
)

print(f"spinor_gram_identity_samples={sample_count}")
print(f"admissible_support_sign_patterns={admissible}")
print(f"gauge_balance_failures={balanced_failures}")
print(f"det_compatible_patterns={det_compatible}")
print(f"even_even_gauge_failures={even_even_failures}")
print(f"structured_example_Omega_X={omega}")

assert sample_count == 81
assert admissible == 512
assert balanced_failures == 0
assert det_compatible == 256
assert even_even_failures == 0
assert omega == -133824

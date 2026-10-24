from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial, gcd
import sys, hashlib
MS = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else list(range(6, 18))
ORBITS = [
    ("CC_adj",   3, ('c',0,1), ('c',0,2)),
    ("CC_disj",  4, ('c',0,1), ('c',2,3)),
    ("CS_inc",   2, ('c',0,1), ('s',0,0)),
    ("CS_non",   3, ('c',0,1), ('s',2,0)),
    ("SS_sameR", 2, ('s',0,0), ('s',1,0)),
    ("SS_sameC", 1, ('s',0,0), ('s',0,1)),
    ("SS_diff",  2, ('s',0,0), ('s',1,1)),
]
@lru_cache(None)
def integer_partitions(n, min_part=1):
    """Nondecreasing integer partitions of n."""
    if n == 0:
        return ((),)
    out = []
    for a in range(min_part, n+1):
        for rest in integer_partitions(n-a, a):
            out.append((a,) + rest)
    return tuple(out)
@lru_cache(None)
def marked_set_partitions(d):
    """Set partitions of {0,...,d-1}; each block sorted, blocks sorted by minimum."""
    if d == 0:
        return ((),)
    parts = [((0,),)]
    for x in range(1, d):
        nxt = set()
        for p in parts:
            for j in range(len(p)):
                q = [list(b) for b in p]
                q[j].append(x)
                qq = tuple(sorted((tuple(sorted(b)) for b in q), key=lambda b: b[0]))
                nxt.add(qq)
            nxt.add(tuple(sorted(p + ((x,),), key=lambda b: b[0])))
        parts = sorted(nxt)
    return tuple(parts)
def weak_compositions_leq(total, slots):
    out = []
    def rec(prefix, k, rem):
        if k == 1:
            for a in range(rem+1):
                out.append(tuple(prefix + [a]))
            return
        for a in range(rem+1):
            rec(prefix + [a], k-1, rem-a)
    rec([], slots, total)
    return out
@lru_cache(None)
def quotient_states(m, d):
    """Orbits of clique-connectivity partitions under S_{m-d} fixing d marked clique labels.
    State = (distinguished_blocks, pure_sizes), where distinguished_blocks is
    (((marked-label block), number_of_unmarked_in_that_block), ...), and
    pure_sizes is the sorted list of sizes of blocks containing no marked labels.
    """
    u = m-d
    out = []
    for marked_partition in marked_set_partitions(d):
        g = len(marked_partition)
        for avec in weak_compositions_leq(u, g):
            rem = u - sum(avec)
            for pure in integer_partitions(rem):
                db = tuple((marked_partition[i], avec[i]) for i in range(g))
                out.append((db, pure))
    return tuple(out)
def canon_state(db, pure):
    db2 = tuple(sorted(((tuple(sorted(group)), a) for group,a in db), key=lambda z:min(z[0])))
    return (db2, tuple(sorted(pure)))
def orbit_multiplicity(m, d, state):
    db, pure = state
    u = m-d
    den = 1
    for _,a in db:
        den *= factorial(a)
    C = Counter(pure)
    for s,c in C.items():
        den *= (factorial(s)**c) * factorial(c)
    return factorial(u)//den
def transition_row(state, required_labels, state_index):
    """Strongly lumped fresh-right-vertex transition.
    required_labels are distinguished clique terminals whose spokes are forced.
    If two required labels are already in the same connectivity block, forced spokes make a cycle.
    Every optional selected block contributes multiplicity equal to its block size.
    """
    db, pure = state
    label_to_block = {}
    for i,(group,a) in enumerate(db):
        for z in group:
            label_to_block[z] = i
    req_blocks = [label_to_block[z] for z in required_labels]
    if len(set(req_blocks)) != len(req_blocks):
        return {}
    req_blocks = set(req_blocks)
    optional_db = [i for i in range(len(db)) if i not in req_blocks]
    pure_counts = Counter(pure)
    pure_items = sorted(pure_counts.items())
    out = defaultdict(int)
    for mask in range(1 << len(optional_db)):
        selected_db = set(req_blocks)
        w_db = 1
        for j,bi in enumerate(optional_db):
            if (mask >> j) & 1:
                selected_db.add(bi)
                group,a = db[bi]
                w_db *= len(group) + a
        chosen = [0]*len(pure_items)
        def rec(t, w_pure, selected_count, selected_sum):
            if t == len(pure_items):
                total_selected = len(selected_db) + selected_count
                if total_selected < 2:
                    target = state
                else:
                    new_db = [b for i,b in enumerate(db) if i not in selected_db]
                    new_pure = []
                    for (s,c),k in zip(pure_items, chosen):
                        new_pure.extend([s]*(c-k))
                    if selected_db:
                        union_group = []
                        unmarked_count = selected_sum
                        for i in sorted(selected_db):
                            group,a = db[i]
                            union_group.extend(group)
                            unmarked_count += a
                        new_db.append((tuple(sorted(union_group)), unmarked_count))
                    else:
                        new_pure.append(selected_sum)
                    target = canon_state(new_db, new_pure)
                out[state_index[target]] += w_db * w_pure
                return
            s,c = pure_items[t]
            for k in range(c+1):
                chosen[t] = k
                rec(t+1,
                    w_pure * comb(c,k) * (s**k),
                    selected_count + k,
                    selected_sum + s*k)
        rec(0, 1, 0, 0)
    return dict(out)
def build_rows(m, d, required_labels=frozenset()):
    states = quotient_states(m,d)
    idx = {s:i for i,s in enumerate(states)}
    return [transition_row(s, required_labels, idx) for s in states]
def tree_extensions(q, required_edges):
    """Number of spanning trees of K_q containing a fixed required forest.
    Required edges use distinguished labels but q may also include undistinguished vertices.
    Weighted Cayley contraction gives q^(c-2) prod(component_size), c=q-|R|.
    """
    if q <= 1:
        return 1
    parent = {}
    size = {}
    def find(x):
        if x not in parent:
            parent[x] = x
            size[x] = 1
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a,b in required_edges:
        ra,rb = find(a),find(b)
        if ra == rb:
            return 0
        if size[ra] < size[rb]:
            ra,rb = rb,ra
        parent[rb] = ra
        size[ra] += size[rb]
    roots = {}
    for x in list(parent):
        r = find(x)
        roots[r] = size[r]
    prod_sizes = 1
    for s in roots.values():
        prod_sizes *= s
    c = q - len(required_edges)
    if c == 1:
        return 1
    return (q**(c-2)) * prod_sizes
def core_vector(m, d, required_edges):
    states = quotient_states(m,d)
    out = []
    for state in states:
        db,pure = state
        loc = {}
        for i,(group,a) in enumerate(db):
            for z in group:
                loc[z] = i
        if any(loc[a] != loc[b] for a,b in required_edges):
            out.append(0)
            continue
        z = orbit_multiplicity(m,d,state)
        for s in pure:
            z *= 1 if s <= 2 else s**(s-2)
        for i,(group,a) in enumerate(db):
            q = len(group)+a
            req = [e for e in required_edges if loc[e[0]] == i]
            z *= tree_extensions(q, req)
        out.append(z)
    return out
def vec_mul(v, rows):
    out = [0]*len(v)
    for i,a in enumerate(v):
        if a:
            for j,c in rows[i].items():
                out[j] += a*c
    return out
def mat_vec(rows, u):
    return [sum(c*u[j] for j,c in row.items()) for row in rows]
def trim(p):
    p = list(p)
    while len(p)>1 and p[-1] == 0:
        p.pop()
    return p
def padd(a,b):
    out = [Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): out[i] += x
    for i,x in enumerate(b): out[i] += x
    return trim(out)
def psub(a,b):
    return padd(a,[-x for x in b])
def pmul(a,b):
    out = [Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    return trim(out)
def pscale(a,c):
    return trim([c*x for x in a])
def peval(a,x):
    s = Fraction(0)
    for c in reversed(a):
        s = s*x+c
    return s
def binom_poly(j):
    p = [Fraction(1)]
    for r in range(j):
        p = pmul(p,[Fraction(-r),Fraction(1)])
    return pscale(p,Fraction(1,factorial(j)))
def primitive(poly):
    den = 1
    for c in poly:
        den = den*c.denominator//gcd(den,c.denominator)
    ints = [int(c*den) for c in poly]
    g = 0
    for z in ints:
        g = gcd(g,abs(z))
    if g > 1:
        ints = [z//g for z in ints]
        den //= g
    return den,ints
def analyze_orbit(m, orbit):
    name,d,e,f = orbit
    states = quotient_states(m,d)
    idx = {s:i for i,s in enumerate(states)}
    M = [transition_row(s,frozenset(),idx) for s in states]
    base = m+1
    N = []
    for i,row in enumerate(M):
        r = dict(row)
        r[i] = r.get(i,0)-base
        if r.get(i) == 0:
            r.pop(i,None)
        N.append(r)
    U = [[1]*len(states)]
    for _ in range(m):
        U.append(mat_vec(N,U[-1]))
    assert any(U[m-1]) and not any(U[m])
    rights_all = sorted({ed[2] for ed in (e,f) if ed[0]=='s'})
    k = len(rights_all)
    masks = {frozenset()}
    for cond in [(),(e,),(f,),(e,f)]:
        rr = defaultdict(set)
        for ed in cond:
            if ed[0]=='s':
                rr[ed[2]].add(ed[1])
        for sset in rr.values():
            masks.add(frozenset(sset))
    T = {mask:(M if not mask else [transition_row(s,mask,idx) for s in states]) for mask in masks}
    binoms = [binom_poly(j) for j in range(m)]
    def count_poly(v):
        p = [Fraction(0)]
        for j in range(m):
            scalar = sum(a*b for a,b in zip(v,U[j]))
            if scalar:
                p = padd(p, pscale(binoms[j], Fraction(scalar,base**j)))
        return p
    P = {}
    for tag,cond in [('0',()),('e',(e,)),('f',(f,)),('ef',(e,f))]:
        req_core = [(ed[1],ed[2]) for ed in cond if ed[0]=='c']
        v = core_vector(m,d,req_core)
        forced_by_right = defaultdict(set)
        for ed in cond:
            if ed[0]=='s':
                forced_by_right[ed[2]].add(ed[1])
        for rid in rights_all:
            mask = frozenset(forced_by_right.get(rid,set()))
            v = vec_mul(v,T[mask])
        P[tag] = count_poly(v)
    R = psub(pmul(P['e'],P['f']), pmul(P['0'],P['ef']))
    den,ints = primitive(R)
    first_x = 1 if k == 0 else 0
    first_val = peval(R,first_x)
    assert min(ints) >= 0 and first_val > 0, (m,name,ints,first_val)
    return {
        'name':name,'d':d,'states':len(states),'k':k,
        'den':den,'ints':ints,'R':R,'P':P,'first':first_val,
        'nnzM':sum(len(row) for row in M)
    }
def abstract_to_edge(edge,m):
    if edge[0]=='c':
        return tuple(sorted((edge[1],edge[2])))
    return tuple(sorted((edge[1],m+edge[2])))
def brute_counts(m,n,marked_pair=None):
    V = m+n
    E = list(combinations(range(m),2)) + [(i,m+r) for r in range(n) for i in range(m)]
    E = [tuple(sorted(e)) for e in E]
    idx = {e:i for i,e in enumerate(E)}
    marks = None
    if marked_pair is not None:
        marks = [idx[tuple(sorted(e))] for e in marked_pair]
    Z=Ze=Zf=Zef=0
    for mask in range(1<<len(E)):
        parent = list(range(V))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        ok = True
        for j,(u,v) in enumerate(E):
            if (mask>>j)&1:
                ru,rv = find(u),find(v)
                if ru == rv:
                    ok = False
                    break
                parent[rv] = ru
        if not ok:
            continue
        Z += 1
        if marks is not None:
            a = bool((mask>>marks[0])&1)
            b = bool((mask>>marks[1])&1)
            Ze += a
            Zf += b
            Zef += (a and b)
    return (Z,Ze,Zf,Zef)
def predicted_counts(m,n,info):
    x = n-info['k']
    assert x >= 0 or info['k']==0
    base = m+1
    return tuple(int(base**x * peval(info['P'][tag],x)) for tag in ('0','e','f','ef'))
def regression_all_seven_K4_I2():
    m,n = 4,2
    rows=[]
    for orbit in ORBITS:
        info = analyze_orbit(m,orbit)
        e = abstract_to_edge(orbit[2],m)
        f = abstract_to_edge(orbit[3],m)
        direct = brute_counts(m,n,(e,f))
        predicted = predicted_counts(m,n,info)
        assert direct == predicted, (orbit[0],direct,predicted)
        delta = direct[1]*direct[2]-direct[0]*direct[3]
        assert delta > 0
        rows.append((orbit[0],direct,delta))
    return rows
def old_bug_witness():
    m,n=3,2
    orbit = next(o for o in ORBITS if o[0]=='SS_diff')
    info = analyze_orbit(m,orbit)
    e = abstract_to_edge(orbit[2],m)
    f = abstract_to_edge(orbit[3],m)
    direct = brute_counts(m,n,(e,f))
    corrected = predicted_counts(m,n,info)
    assert direct == corrected == (198,70,70,24)
    old = (7,14,14,24)
    assert old != direct
    return direct,old,direct[1]*direct[2]-direct[0]*direct[3]
print('PROB10-07 corrected complete-split quotient certificate')
print('scope=uniform measure on ALL forests of K_m join I_n; exact integer/Fraction arithmetic')
print('critical_rule=every distinguished right vertex is processed in every conditioning event; T_empty=M')
direct,old,delta = old_bug_witness()
print('OLD_BUG_WITNESS K3_JOIN_I2 SS_diff direct=',direct,'old_omission=',old,'corrected_delta=',delta)
reg = regression_all_seven_K4_I2()
print('DIRECT_REGRESSION K4_JOIN_I2 all_seven_orbits PASS')
for name,counts,d in reg:
    print(' REG',name,'counts=',counts,'delta=',d)
for m in MS:
    infos=[]
    for orbit in ORBITS:
        if m < orbit[1]:
            continue
        infos.append(analyze_orbit(m,orbit))
    assert len(infos)==7
    max_states=max(z['states'] for z in infos)
    max_nnz=max(z['nnzM'] for z in infos)
    min_coeff=min(min(z['ints']) for z in infos)
    min_first=min(z['first'] for z in infos)
    print(f'M={m} ALL_N_EXACT_PASS max_quotient_states={max_states} max_sparse_nnz={max_nnz} min_primitive_coeff={min_coeff} min_first_physical={min_first}')
    for z in infos:
        coeff_text=','.join(str(q) for q in z['ints'])
        coeff_hash=hashlib.sha256(coeff_text.encode()).hexdigest()
        print(f" ORBIT {z['name']} d={z['d']} states={z['states']} k={z['k']} degree={len(z['ints'])-1} den={z['den']} min_coeff={min(z['ints'])} max_coeff={max(z['ints'])} first={z['first']} coeff_sha256={coeff_hash}")
print('PROB10_07_SPLIT_QUOTIENT_CORRECTED_EXACT_PASS')

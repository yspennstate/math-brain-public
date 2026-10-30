"""A068 systematic parity controls: exact finite verification, version 1."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations, combinations
from math import comb
import argparse, json, time

ROOT = Path(__file__).resolve().parents[1]
checks = 0
def require(ok):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(checks)

def fwht(a):
    a = list(a)
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2*step):
            for j in range(start, start+step):
                u,v = a[j],a[j+step]
                a[j],a[j+step] = u+v,u-v
        step *= 2
    return a

def syndrome(s, rows):
    out = 0
    for i, row in enumerate(rows):
        if s >> i & 1:
            out ^= row
    return out

def table_lift(h, rows, m):
    q = len(rows)
    out = []
    for v in range(1 << (q+m)):
        x,z = v & ((1 << q)-1),v >> q
        logical = x
        for i,row in enumerate(rows):
            logical ^= ((row & z).bit_count() % 2) << i
        out.append(h[logical])
    return out

def edge_counts(h, n):
    return [sum(h[v] != h[v ^ (1 << i)] for v in range(1 << n)) for i in range(n)]

def regular_order(h,q):
    # Bit 0 is sign +1, so a monotone gate has h(bit=0)>=h(bit=1).
    if any(h[v] < h[v | (1 << i)] for i in range(q)
           for v in range(1 << q) if not v >> i & 1):
        return None
    for order in permutations(range(q)):
        good = True
        for r,i in enumerate(order):
            for j in order[:r]:
                for v in range(1 << q):
                    if v & ((1 << i) | (1 << j)):
                        continue
                    if h[v | (1 << i)] < h[v | (1 << j)]:
                        good = False
                        break
        if good:
            return order
    return None

def check_antichain(h,order):
    q = len(order)
    for r,i in enumerate(order):
        u = sum(1 << j for j in order[:r])
        rest = ((1 << q)-1) ^ u ^ (1 << i)
        for outside in range(1 << q):
            if outside & ~rest:
                continue
            support = [v for v in range(1 << q) if not v & ~u
                       and h[outside | v] != h[outside | v | (1 << i)]]
            for a,b in combinations(support,2):
                require(a & b != a and a & b != b)

def check_noise(h, order):
    q = len(order)
    for r,i in enumerate(order):
        # Derivative is embedded as a function independent of bit i.
        d = [(h[v & ~(1 << i)]-h[v | (1 << i)])//2 for v in range(1 << q)]
        a = fwht(d)
        mass = sum(v*v for v in a)
        if not mass:
            continue
        u = sum(1 << j for j in order[:r])
        for rate in (F(1,4),F(1,2),F(3,4),F(1)):
            lhs = sum(F(v*v)*(1-rate)**((s & u).bit_count()) for s,v in enumerate(a))
            density = sum(F(comb(r,b))*rate**b*(1-rate)**(r-b)
                          * F(comb(b,b//2),1 << b) for b in range(r+1))
            require(lhs <= mass*density)
        harmonic = lambda k: sum((F(1,j) for j in range(1,k+1)),F(0))
        lhs = sum(F(v*v)*(harmonic(r)-harmonic((s & u).bit_count())) for s,v in enumerate(a))
        rhs = mass*sum((F(comb(b,b//2), (1 << b)*b) for b in range(1,r+1)),F(0))
        require(lhs <= rhs)

def check_reference(q,rows,m):
    # Exact rational normalized finite Euler reference, pushed along the graph.
    for k in range(q+1):
        weights = {s: F(1,1) for s in range(1 << q) if s.bit_count()==k}
        for s in weights:
            for i in range(q):
                if s >> i & 1:
                    weights[s] /= (i+1)**2
        normalizer = sum(weights.values(), F(0))
        lifted = {(s | (syndrome(s,rows) << q)): w/normalizer for s,w in weights.items()}
        require(len(lifted)==len(weights))
        require(sum(lifted.values(),F(0))==1)

def check_lift(h,rows,m):
    q,n = len(rows),len(rows)+m
    base = fwht(h)
    truth = table_lift(h,rows,m)
    actual = fwht(truth)
    expected = [0]*(1 << n)
    for s,v in enumerate(base):
        expected[s | (syndrome(s,rows) << q)] = v*(1 << m)
    require(actual == expected)
    require(sum(v*v for v in actual)==1 << (2*n))
    # Equality of atom-probability multisets certifies entropy equality without logs.
    require(sorted(F(v*v,1 << (2*n)) for v in actual if v)
            == sorted(F(v*v,1 << (2*q)) for v in base if v))
    edges = edge_counts(truth,n)
    for i in range(n):
        spectral = sum(v*v for s,v in enumerate(actual) if s >> i & 1)
        require(spectral == edges[i]*(1 << n))
    base_edges = edge_counts(h,q)
    require(edges[:q] == [v*(1 << m) for v in base_edges])
    for j in range(m):
        derivative = sum(base[s]**2 for s in range(1 << q) if syndrome(s,rows) >> j & 1)
        require(F(edges[q+j],1 << n)==F(derivative,1 << (2*q)))
    return truth,actual,edges

def quad_phase(v, linear, quadratic):
    return -1 if ((linear & v).bit_count()+sum(bool(v >> i & 1) and bool(v >> j & 1) for i,j in quadratic))%2 else 1

def check_quadratic(h, linear, quadratic, m):
    q,n=len(linear),len(linear)+m
    base=fwht(h)
    truth=[]
    for v in range(1 << n):
        x,z=v & ((1 << q)-1),v >> q
        mask=sum((quad_phase(z,linear[i],quadratic[i])==-1) << i for i in range(q))
        truth.append(h[x ^ mask])
    actual=fwht(truth)
    expected=[0]*(1 << n)
    packet_rank=[]
    packet_influence=[]
    conditional_reference={}
    for s,b in enumerate(base):
        controls=[quad_phase(z,0,[]) for z in range(1 << m)]
        for i in range(q):
            if s >> i & 1:
                controls=[v*quad_phase(z,linear[i],quadratic[i]) for z,v in enumerate(controls)]
        raw=fwht(controls)
        support=[t for t,v in enumerate(raw) if v]
        require(len({raw[t]**2 for t in support})==1)
        size=len(support)
        require(size & (size-1)==0)
        rank=size.bit_length()-1
        packet_rank.append(rank)
        # Check affine closure directly; small m except cyclic m<=7.
        anchor=support[0]
        differences={t ^ anchor for t in support}
        require(all(a ^ b in differences for a in differences for b in differences))
        influence=F(sum(t.bit_count() for t in support),size)
        packet_influence.append(influence)
        require(rank <= 2*influence)
        require(sum(F(raw[t]**2,1 << (2*m)) for t in support)==1)
        for t,v in enumerate(raw):
            expected[s | (t << q)]=b*v
        conditional_reference[s]={t:F(1,size) for t in support}
    require(actual==expected)
    require(sum(v*v for v in actual)==1 << (2*n))
    edges=edge_counts(truth,n)
    for i in range(n):
        require(sum(v*v for s,v in enumerate(actual) if s >> i & 1)==edges[i]*(1 << n))
    require(edges[:q]==[v*(1 << m) for v in edge_counts(h,q)])
    expected_control=sum(F(b*b,1 << (2*q))*packet_influence[s] for s,b in enumerate(base))
    require(expected_control==F(sum(edges[q:]),1 << n))
    # Exact entropy chain: conditional flat packet size determines all probabilities.
    require(sorted(F(v*v,1 << (2*n)) for v in actual if v)==sorted(
        F(base[s]**2,(1 << (2*q))*len(conditional_reference[s]))
        for s in range(1 << q) if base[s] for t in conditional_reference[s]))
    for k in range(q+1):
        weights={s:F(1) for s in range(1 << q) if s.bit_count()==k}
        for s in weights:
            for i in range(q):
                if s >> i & 1:
                    weights[s]/=(i+1)**2
        total=sum(weights.values(),F(0))
        require(sum(weights[s]/total*sum(conditional_reference[s].values(),F(0)) for s in weights)==1)
    return edges,packet_rank

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pilot',action='store_true')
    args=ap.parse_args()
    start=time.perf_counter()
    cases=0
    regular_bases=0
    for q in (0,1,2,3):
        m=2
        for hmask in range(1 << (1 << q)):
            h=[1 if hmask >> v & 1 else -1 for v in range(1 << q)]
            order=regular_order(h,q)
            if order is not None:
                regular_bases+=1
                check_antichain(h,order)
                check_noise(h,order)
            for matrix in range(1 << (m*q)):
                rows=[(matrix >> (m*i)) & ((1 << m)-1) for i in range(q)]
                check_lift(h,rows,m)
                cases+=1
                if args.pilot and cases>=100:
                    break
            if args.pilot and cases>=100:
                break
        if args.pilot and cases>=100:
            break
    cycles=[]
    quadratic_cases=0
    if not args.pilot:
        for q in (0,1,2,3):
            for hmask in range(1 << (1 << q)):
                h=[1 if hmask >> v & 1 else -1 for v in range(1 << q)]
                if q<=2:
                    tuples=range(1 << (3*q))
                    for packed in tuples:
                        linear=[packed >> (3*i) & 3 for i in range(q)]
                        quadratic=[[(0,1)] if packed >> (3*i+2) & 1 else [] for i in range(q)]
                        check_quadratic(h,linear,quadratic,2)
                        quadratic_cases+=1
                else:
                    for flags in range(8):
                        check_quadratic(h,[1,2,3],[[(0,1)] if flags >> i & 1 else [] for i in range(3)],2)
                        quadratic_cases+=1
        for q in (3,5,7):
            h=[1 if q-2*v.bit_count()>0 else -1 for v in range(1 << q)]
            rows=[(1 << i) | (1 << ((i+1)%q)) for i in range(q)]
            truth,a,edges=check_lift(h,rows,q)
            central=F(comb(q-1,(q-1)//2),1 << (q-1))
            require(all(F(v,1 << (2*q))==central for v in edges))
            # Direct signed-edge witnesses of non-unateness for every data bit.
            for i in range(q):
                differences={truth[v]-truth[v | (1 << i)] for v in range(1 << (2*q)) if not v >> i & 1}
                require(-2 in differences and 2 in differences)
            require(len({syndrome(z,rows) for z in range(1 << q)})==1 << (q-1))
            check_antichain(h,tuple(range(q)))
            check_noise(h,tuple(range(q)))
            check_reference(q,rows,q)
            # Signed derivative support transported by the actual context.
            for z in range(1 << q):
                mask=sum(((row & z).bit_count()%2) << i for i,row in enumerate(rows))
                for i in range(q):
                    for x in range(1 << q):
                        left=(truth[x | (z << q)]-truth[(x ^ (1 << i)) | (z << q)])//2
                        right=(h[x ^ mask]-h[(x ^ mask) ^ (1 << i)])//2
                        require(left==right)
            cycles.append({'q':q,'each_coordinate_influence':str(central),
                           'total_influence':str(2*q*central),
                           'neighbor_correlation':str(1-2*central),
                           'distinct_context_orientations':1 << (q-1)})
            nonlinear_edges,ranks=check_quadratic(h,[0]*q,[[(i,(i+1)%q)] for i in range(q)],q)
            require(all(F(v,1 << (2*q))==F(3,4)*central for v in nonlinear_edges[q:]))
            require(all(F(v,1 << (2*q))==central for v in nonlinear_edges[:q]))
            cycles[-1].update({'quadratic_each_control_influence':str(F(3,4)*central),
                              'quadratic_total_influence':str(F(7,4)*q*central),
                              'quadratic_packet_ranks':ranks})
    output={'helper_version':2,'pilot':args.pilot,'status':'PASS','actual_boolean_lift_cases':cases,
            'quadratic_control_cases':quadratic_cases,
            'regular_base_gates_checked':regular_bases,'assertions':checks,'cyclic_family':cycles,
            'arithmetic':'integer FWHT, exact Fraction; no floating entropy used',
            'runtime_seconds':time.perf_counter()-start}
    (ROOT/'out'/('pilot.json' if args.pilot else 'validation.json')).write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,indent=2))

if __name__=='__main__':
    main()

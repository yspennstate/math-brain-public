"""Exact rank-one-bottom diamond coupling.  Python standard library only.

All capacities and probabilities are Fraction values.  Two independent,
deterministic constructions are provided: Edmonds--Karp and the finite
sum/min edge-deletion formula proved in agents/C033.md.
"""

from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb
import random


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def cast(z):
        return z if isinstance(z, C) else C(F(z))

    def __add__(self, other):
        z = C.cast(other)
        return C(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-C.cast(other))

    def __rsub__(self, other):
        return C.cast(other) - self

    def __mul__(self, other):
        z = C.cast(other)
        return C(self.re*z.re - self.im*z.im,
                 self.re*z.im + self.im*z.re)

    __rmul__ = __mul__

    def conj(self):
        return C(self.re, -self.im)

    def norm2(self):
        return self.re*self.re + self.im*self.im

    def __truediv__(self, other):
        z = C.cast(other)
        t = self*z.conj()
        d = z.norm2()
        return C(t.re/d, t.im/d)

    def json(self):
        return [str(self.re), str(self.im)]


def determinant(a):
    n = len(a)
    ans = C()
    for p in permutations(range(n)):
        term = C(1)
        for i in range(n):
            term *= a[i][p[i]]
        parity = sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
        ans += term if parity % 2 == 0 else -term
    return ans


def minors(frame, columns):
    return {s: determinant([[frame[i][j] for j in columns] for i in s])
            for s in combinations(range(len(frame)), len(columns))}


def matmul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), C())
             for j in range(len(b[0]))] for i in range(len(a))]


def householder(z):
    norm = sum(x.norm2() for x in z)
    return [[C(int(i == j)) - 2*z[i]*z[j].conj()/norm
             for j in range(len(z))] for i in range(len(z))]


def rational_frame(n, seed=0, real=False):
    """First three columns of three exact rational unitary reflections."""
    rng = random.Random(330000 + 31*n + seed)
    q = [[C(int(i == j)) for j in range(n)] for i in range(n)]
    for _ in range(3):
        z = [C(rng.randrange(-3,4), 0 if real else rng.randrange(-3,4))
             for _ in range(n)]
        if all(x == C() for x in z):
            z[0] = C(1)
        q = matmul(householder(z), q)
    return [row[:3] for row in q]


def assert_orthonormal(frame):
    for i in range(3):
        for j in range(3):
            assert sum((r[i].conj()*r[j] for r in frame), C()) == C(int(i == j))


def laws(frame):
    assert_orthonormal(frame)
    bottom = {(i,): row[0].norm2() for i, row in enumerate(frame)}
    left = {s: z.norm2() for s,z in minors(frame, (1,2)).items()}
    top = {s: z.norm2() for s,z in minors(frame, (0,1,2)).items()}
    gu = {s: z.norm2() for s,z in minors(frame, (0,1)).items()}
    gv = {s: z.norm2() for s,z in minors(frame, (0,2)).items()}
    middle = {s: gu[s] + gv[s] for s in gu}
    assert sum(bottom.values()) == sum(left.values()) == sum(top.values()) == 1
    assert sum(middle.values()) == 2
    return bottom, left, top, middle


def incidence(left, right):
    return [(b,t) for b in sorted(left) for t in sorted(right)
            if set(b) <= set(t)]


def maxflow_transport(left, right):
    """Deterministic exact Edmonds--Karp; input need only satisfy Hall."""
    left, right = dict(left), dict(right)
    total = sum(left.values())
    assert total == sum(right.values())
    assert all(v >= 0 for v in (*left.values(), *right.values()))
    edges = incidence(left, right)
    if total == 0:
        return {e: F(0) for e in edges}, 0
    ls, rs = sorted(left), sorted(right)
    li = {b: i+1 for i,b in enumerate(ls)}
    ri = {t: i+1+len(ls) for i,t in enumerate(rs)}
    source, sink = 0, len(ls)+len(rs)+1
    adj = [[] for _ in range(sink+1)]
    residual = {}

    def add(i, j, capacity):
        adj[i].append(j)
        adj[j].append(i)
        residual[i,j] = capacity
        residual[j,i] = F(0)

    for b in ls:
        add(source, li[b], left[b])
    for b,t in edges:
        add(li[b], ri[t], 2*total)
    for t in rs:
        add(ri[t], sink, right[t])
    for a in adj:
        a.sort()
    flow = F(0)
    augmentations = 0
    while True:
        predecessor = {source: None}
        queue = deque([source])
        while queue and sink not in predecessor:
            i = queue.popleft()
            for j in adj[i]:
                if j not in predecessor and residual[i,j] > 0:
                    predecessor[j] = i
                    queue.append(j)
        if sink not in predecessor:
            break
        path = []
        j = sink
        while j != source:
            i = predecessor[j]
            path.append((i,j))
            j = i
        amount = min(residual[e] for e in path)
        for i,j in path:
            residual[i,j] -= amount
            residual[j,i] += amount
        flow += amount
        augmentations += 1
    assert flow == total, "Hall failure in supplied transport instance"
    answer = {(b,t): 2*total-residual[li[b],ri[t]] for b,t in edges}
    assert_transport(left, right, answer)
    return answer, augmentations


def edge_deletion_transport(left, right):
    """Exact sum/min formula; exponential, intended for small certificates.

    At each step take the first remaining edge (b,t).  Allocate the minimum
    of its endpoint masses and every Hall slack whose pair family omits b
    but has t as a neighbor.  Delete that edge even if its weight is zero.
    """
    original_left, original_right = dict(left), dict(right)
    a, c = dict(left), dict(right)
    ls = sorted(a)
    edges = incidence(a, c)
    remaining = set(edges)
    answer = {}
    for b,t in edges:
        delta = min(a[b], c[t])
        other = [l for l in ls if l != b]
        neighbors = {l: {r for q,r in remaining if q == l} for l in ls}
        for mask in range(1 << len(other)):
            subset = {other[i] for i in range(len(other)) if mask >> i & 1}
            nb = set().union(*(neighbors[l] for l in subset)) if subset else set()
            if t in nb:
                slack = sum((c[r] for r in nb), F(0)) - sum((a[l] for l in subset), F(0))
                assert slack >= 0
                delta = min(delta, slack)
        assert delta >= 0
        answer[b,t] = delta
        a[b] -= delta
        c[t] -= delta
        remaining.remove((b,t))
    assert all(v == 0 for v in (*a.values(), *c.values()))
    assert_transport(original_left, original_right, answer)
    return answer


def assert_transport(left, right, answer):
    assert all(x >= 0 for x in answer.values())
    for b in left:
        assert sum((x for (q,t),x in answer.items() if q == b), F(0)) == left[b]
    for t in right:
        assert sum((x for (b,q),x in answer.items() if q == t), F(0)) == right[t]


def assert_diamonds(frame, answer):
    bottom, left, top, middle = laws(frame)
    assert_transport(left, top, answer)
    out_bottom = dict.fromkeys(bottom, F(0))
    out_top = dict.fromkeys(top, F(0))
    out_middle = dict.fromkeys(middle, F(0))
    for (b,t),x in answer.items():
        center = next(iter(set(t)-set(b)))
        out_bottom[center,] += x
        out_top[t] += x
        for j in b:
            out_middle[tuple(sorted((center,j)))] += x
    assert out_bottom == bottom
    assert out_top == top
    assert out_middle == middle


def contraction(w, z, degree):
    out = {}
    for s in combinations(range(len(w)), degree-1):
        value = C()
        for i in range(len(w)):
            if i not in s:
                t = tuple(sorted((*s,i)))
                value += (-1)**t.index(i)*w[i].conj()*z.get(t,C())
        out[s] = value
    return out


def wedge(w, z, degree):
    return {t: sum(((-1)**k*w[i]*z.get(t[:k]+t[k+1:], C())
                    for k,i in enumerate(t)), C())
            for t in combinations(range(len(w)), degree+1)}


def hall_records(left, right):
    ls = sorted(left)
    edges = [(b,t) for b,t in incidence(left,right) if right[t] > 0]
    neighbors = {b: {t for q,t in edges if q == b} for b in ls}
    for mask in range(1 << len(ls)):
        subset = {ls[i] for i in range(len(ls)) if mask >> i & 1}
        nb = set().union(*(neighbors[b] for b in subset)) if subset else set()
        slack = sum((right[t] for t in nb), F(0))-sum((left[b] for b in subset), F(0))
        crossing = sum(b not in subset and t in nb for b,t in edges)
        yield subset, nb, slack, crossing


def positive_transport(left, right):
    """Explicit positive floor, under the report's strict Hall hypotheses."""
    assert all(v > 0 for v in left.values())
    edges = [(b,t) for b,t in incidence(left,right) if right[t] > 0]
    dl = {b: sum(q == b for q,t in edges) for b in left}
    dr = {t: sum(q == t for b,q in edges) for t in right}
    candidates = [left[b]/dl[b] for b in left]
    candidates += [right[t]/dr[t] for t in right if right[t] > 0]
    minimum_slack = None
    for a,nb,slack,crossing in hall_records(left,right):
        assert slack >= 0
        if a and len(a) < len(left):
            assert slack > 0
            minimum_slack = slack if minimum_slack is None else min(minimum_slack,slack)
        if crossing:
            candidates.append(slack/crossing)
    epsilon = min(candidates)/2
    assert epsilon > 0
    reduced_left = {b: left[b]-epsilon*dl[b] for b in left}
    reduced_right = {t: right[t]-epsilon*dr[t] for t in right}
    answer, augmentations = maxflow_transport(reduced_left,reduced_right)
    for e in edges:
        answer[e] += epsilon
    assert_transport(left,right,answer)
    assert all(answer[e] >= epsilon for e in edges)
    return answer, epsilon, minimum_slack, augmentations


def closed_floor_transport(frame):
    """Positive coupling with a closed floor; no Hall-family enumeration."""
    bottom,left,right,middle = laws(frame)
    a_min, h_min = min(bottom.values()), min(left.values())
    assert a_min > 0 and h_min > 0
    c_min = min(x for x in right.values() if x > 0)
    n = len(frame)
    epsilon = min(h_min/(n-2), c_min/3,
                  a_min*h_min/(3*comb(n,3)))/2
    edges = [(b,t) for b,t in incidence(left,right) if right[t] > 0]
    dl = {b: sum(q == b for q,t in edges) for b in left}
    dr = {t: sum(q == t for b,q in edges) for t in right}
    reduced_left = {b: left[b]-epsilon*dl[b] for b in left}
    reduced_right = {t: right[t]-epsilon*dr[t] for t in right}
    answer,augmentations = maxflow_transport(reduced_left,reduced_right)
    for e in edges:
        answer[e] += epsilon
    assert_transport(left,right,answer)
    assert all(answer[e] >= epsilon for e in edges)
    return answer,epsilon,a_min*h_min,augmentations


def verify_hall_sos(frame):
    """Check both SOS formulas and the uniform Hall gap (small n)."""
    w = [r[0] for r in frame]
    b = minors(frame,(1,2))
    z = minors(frame,(0,1,2))
    assert contraction(w,z,3) == b
    left = {s:v.norm2() for s,v in b.items()}
    right = {s:v.norm2() for s,v in z.items()}
    gap = min(x.norm2() for x in w)*min(left.values())
    checked = 0
    for a,nb,slack,crossing in hall_records(left,right):
        zn = {t:(value if t in nb else C()) for t,value in z.items()}
        contracted = contraction(w,zn,3)
        lifted = wedge(w,zn,3)
        rhs = sum(v.norm2() for v in lifted.values())
        rhs += sum(v.norm2() for s,v in contracted.items() if s not in a)
        assert slack == rhs
        ba = {s:(value if s in a else C()) for s,value in b.items()}
        bac = {s:(C() if s in a else value) for s,value in b.items()}
        contracted_ba = contraction(w,ba,2)
        lifted_bac = wedge(w,bac,2)
        rhs2 = sum(v.norm2() for v in contracted_ba.values())
        rhs2 += sum(v.norm2() for t,v in lifted_bac.items() if t in nb)
        assert slack == rhs2
        if a and len(a) < len(left):
            assert slack >= gap
        checked += 1
    return checked


def serial_weights(answer):
    return [{"pair":list(b), "triple":list(t),
             "center":next(iter(set(t)-set(b))), "weight":str(x)}
            for (b,t),x in sorted(answer.items()) if x]

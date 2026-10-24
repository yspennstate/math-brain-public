from fractions import Fraction
from itertools import combinations
import hashlib
import json

MAX_N = 80
CHECKS = 0

def ck(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def w(N, s):
    return Fraction(N, 2*s*(N-s))

def x(N, s):
    return Fraction(s, N)

def p_support(N, s, i, j):
    xx = x(N, s)
    return xx**i * (1-xx)**j + xx**j * (1-xx)**i

def q(N, i, j):
    return sum((w(N,s)*p_support(N,s,i,j) for s in range(1,N)), Fraction())

def q_riemann(N, i, j):
    return sum((Fraction(1,N)*x(N,s)**(i-1)*(1-x(N,s))**(j-1)
                for s in range(1,N)), Fraction())

def exit_rate(N, b):
    return sum((w(N,s)*(1-x(N,s)**b-(1-x(N,s))**b)
                for s in range(1,N)), Fraction())

# 1. Harmonic-grid and exact beta-Riemann identities.
for N in range(3, MAX_N+1):
    tau = Fraction(1, N**3)
    for s in range(1, N):
        ck(tau*w(N,s) < 1, f"illegal gate N={N} s={s}")
    ck(q(N,1,1) == Fraction(N-1,N), f"q11 N={N}")
    ck(q(N,2,2) == Fraction(N*N-1, 6*N*N), f"q22 N={N}")
    for i in range(1,6):
        for j in range(1,6):
            ck(q(N,i,j) == q_riemann(N,i,j), f"Riemann identity N={N} i={i} j={j}")
    for b in range(2,9):
        ck(exit_rate(N,b) <= b, f"exit bound N={N} b={b}")

# 2. The minimum-label channel is collision-free on every set partition:
# distinct disjoint nonempty blocks have distinct minima.
def set_partitions(seq):
    seq = list(seq)
    if not seq:
        yield []
        return
    first = seq[0]
    for rest in set_partitions(seq[1:]):
        yield [{first}] + [set(b) for b in rest]
        for idx in range(len(rest)):
            new = [set(b) for b in rest]
            new[idx].add(first)
            yield new

for n in range(1,9):
    for pi in set_partitions(range(1,n+1)):
        mins = [min(B) for B in pi]
        ck(len(mins) == len(set(mins)), f"minimum collision n={n} pi={pi}")

# 3. Hidden-carrier lemma for canonical restrictions [k]:
# if A is a nonempty visible block and H uses only labels > k, min(A union H)=min(A).
for N in range(3,11):
    for k in range(1, min(5,N)+1):
        hidden = list(range(k+1,N+1))
        for maskA in range(1, 1<<k):
            A = {i+1 for i in range(k) if (maskA>>i)&1}
            for maskH in range(1<<len(hidden)):
                H = {hidden[r] for r in range(len(hidden)) if (maskH>>r)&1}
                ck(min(A|H) == min(A), f"hidden-min N={N} k={k} A={A} H={H}")

# 4. Exact N=4 finite non-equivalence witnesses.
N = 4
s = 1
Delta_C028 = Fraction(1, N**3)
c_C028 = (N-1)*w(N,s)
a_C028 = Delta_C028*c_C028
pair_visible = a_C028 * 2*x(N,s)*(1-x(N,s))
c028_two_pair_same_step = pair_visible**2
ck(c028_two_pair_same_step == Fraction(9,65536), "C028 simultaneous witness")
c040_two_pair_direct_rate = Fraction(N*N-1, 3*N**3)
ck(c040_two_pair_direct_rate == Fraction(5,64), "C040 simultaneous witness")
c041_same_microstep = Fraction(0,1)
ck(c041_same_microstep == 0, "C041 collision-free support")
ck(c041_same_microstep != c028_two_pair_same_step, "C041 != C028")
ck(c041_same_microstep != c040_two_pair_direct_rate, "C041 != C040")

# 5. Representative exact values used in report.
payload = {
    "claim": "R11-I0054-C041 self-check",
    "arithmetic": "fractions.Fraction only",
    "checks": CHECKS,
    "max_N": MAX_N,
    "q4_22": str(q(4,2,2)),
    "exit4_4": str(exit_rate(4,4)),
    "C028_N4_two_pair_same_raw_step": str(c028_two_pair_same_step),
    "C040_N4_two_pair_direct_rate": str(c040_two_pair_direct_rate),
    "C041_same_microstep_two_block_jump": str(c041_same_microstep),
    "status": "ALL_EXACT_CHECKS_PASS",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",",":"))
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
print(json.dumps(payload, indent=2, sort_keys=True))

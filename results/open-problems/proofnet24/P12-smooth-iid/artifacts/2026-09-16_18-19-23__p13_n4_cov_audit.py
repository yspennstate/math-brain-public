from fractions import Fraction
import json

# Independent exact audit of P13-I0051-INDEPENDENCE-NOGO-01.
# No code or moment tables are imported from P13.

H3 = sum((Fraction(1, j) for j in range(1, 4)), Fraction())


def q4(i: int) -> Fraction:
    return Fraction(4, 2 * i * (4 - i)) / H3


q = {i: q4(i) for i in (1, 2, 3)}
assert sum(q.values(), Fraction()) == 1
assert q == {1: Fraction(4, 11), 2: Fraction(3, 11), 3: Fraction(4, 11)}

# For DTCS(4):
# - root split 1+3 or 3+1 (total probability 8/11) gives (N_2,N_3)=(1,1);
# - root split 2+2 (probability 3/11) gives (N_2,N_3)=(2,0).
states = [
    (q[1] + q[3], Fraction(1), Fraction(1)),
    (q[2], Fraction(2), Fraction(0)),
]

E_N2 = sum(p * n2 for p, n2, n3 in states)
E_N3 = sum(p * n3 for p, n2, n3 in states)
E_N2N3 = sum(p * n2 * n3 for p, n2, n3 in states)
cov = E_N2N3 - E_N2 * E_N3

assert E_N2 == Fraction(14, 11)
assert E_N3 == Fraction(8, 11)
assert E_N2N3 == Fraction(8, 11)
assert cov == Fraction(-24, 121)

payload = {
    "result": "PASS",
    "claim_id": "P13-I0051-INDEPENDENCE-NOGO-01",
    "scope": "independent exact n=4 covariance audit",
    "arithmetic": "fractions.Fraction only",
    "H3": str(H3),
    "q4": {str(i): str(q[i]) for i in (1, 2, 3)},
    "state_probabilities": {
        "(N2,N3)=(1,1)": str(q[1] + q[3]),
        "(N2,N3)=(2,0)": str(q[2]),
    },
    "E_N2": str(E_N2),
    "E_N3": str(E_N3),
    "E_N2N3": str(E_N2N3),
    "Cov_N2_N3": str(cov),
    "note": "P12 independent component audit; not a closure audit for P13 or P12.",
}

print(json.dumps(payload, indent=2, sort_keys=True))

"""Independent check of the anticommuting-assembly identity used in U-Q, and of U for the author's d = 2 example
under the two candidate quantum orders.

(1) For pairwise anticommuting Hermitian unitaries P_1..P_L and commuting Hermitian B_1..B_L with sum B_l^2 = I,
    A = sum_l P_l (x) B_l is Hermitian with A^2 = I.  Tested with random diagonal B_l whose pointwise vectors are unit.
(2) Pauli spectrum of A = (X (x) (Z1+Z2) + Z (x) (Z1-Z2))/2 (the author's code/slote_check.py example), H, I and U
    with pi defined by (a) letter agreement on supp P, (b) support containment.
"""
import itertools, json
import numpy as np

rng = np.random.default_rng(5)
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], dtype=complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1.0 + 0j, -1.0])
PA = {'I': I2, 'X': X, 'Y': Y, 'Z': Z}


def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


res = {}
# (1) L = 3 on one qubit, L = 5 on two qubits
families = {
    'L3': [X, Y, Z],
    'L5': [kron(X, I2), kron(Y, I2), kron(Z, X), kron(Z, Y), kron(Z, Z)],
}
for name, P in families.items():
    L = len(P)
    ac = max(np.abs(P[a] @ P[b] + P[b] @ P[a]).max() for a in range(L) for b in range(L) if a != b)
    for trial in range(5):
        m = 3  # B_l act on m qubits, diagonal
        D = rng.normal(size=(L, 1 << m))
        D = D / np.linalg.norm(D, axis=0, keepdims=True)    # pointwise unit vectors -> sum_l B_l^2 = I
        B = [np.diag(D[l]).astype(complex) for l in range(L)]
        A = sum(np.kron(P[l], B[l]) for l in range(L))
        err = max(np.abs(A @ A - np.eye(A.shape[0])).max(), np.abs(A - A.conj().T).max())
        res[f'{name}_trial{trial}'] = dict(max_anticommutator=float(ac), err_A2_minus_I_or_nonhermitian=float(err))

# (2) the author's d = 2 example
A = (kron(X, Z, I2) + kron(X, I2, Z) + kron(Z, Z, I2) - kron(Z, I2, Z)) / 2.0
assert np.allclose(A @ A, np.eye(8))
coef = {}
for lab in itertools.product('IXYZ', repeat=3):
    c = np.trace(kron(*[PA[ch] for ch in lab]).conj().T @ A).real / 8
    if abs(c) > 1e-12:
        coef[''.join(lab)] = c
p = {k: v * v for k, v in coef.items()}
H = -sum(v * np.log2(v) for v in p.values())
Iq = sum(sum(ch != 'I' for ch in k) * v for k, v in p.items())
supp = lambda k: frozenset(i for i, ch in enumerate(k) if ch != 'I')


def agree_above(Q, P):
    return all(Q[i] == P[i] for i in supp(P))


U_agree = sum(v * np.log2(sum(w for Q, w in p.items() if agree_above(Q, P)) / v) for P, v in p.items())
U_supp = sum(v * np.log2(sum(w for Q, w in p.items() if supp(Q) >= supp(P)) / v) for P, v in p.items())
res['d2_example'] = dict(coefficients=coef, H=float(H), I=float(Iq), U_letter_agreement=float(U_agree), U_support_order=float(U_supp))
print(json.dumps(res, indent=1))
with open('slote_mech_results.json', 'w', encoding='utf-8') as fh:
    json.dump(res, fh, indent=1)

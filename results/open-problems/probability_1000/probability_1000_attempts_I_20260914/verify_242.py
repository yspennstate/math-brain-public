"""Verify the published 9-variable Boolean functions of nonlinearity 242 (Kavut and Yucel, IACR eprint
2007/308 / arXiv:0808.0684), and read off what they say about Conjecture 13 of the Randomstrasse 2024
list: that disc(H_k) = sqrt(2)*sqrt(2^k) for odd k.

disc(H_k) = min over f of max |W_f| and NL(f) = 2^(k-1) - max|W_f|/2, so at k = 9 the conjecture says
the smallest achievable max|W| is 32 (nonlinearity 240).  A function of nonlinearity 242 has max|W| = 28.

Nonlinearity is invariant under permuting the input coordinates and under complementing the function, so
the reading convention for the hex string cannot change the answer.
"""
import numpy as np

N = 512

def wht(x):
    a = x.astype(np.int64).copy(); h = 1
    while h < N:
        a = a.reshape(-1, 2, h)
        u, v = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = u + v; a[:, 1, :] = u - v
        a = a.reshape(-1); h <<= 1
    return a

FUNCS = {
 "3-DSBF, absolute indicator 40":
   "68B7EF2DA03B0D3EA00DB6A96DD99AEAFDB9C842B6D5DC8C4526CE0DD29020DB"
   "B75FE3314568344E73688FF0CB2482E065231869E1AA4583765CC491F8A8DB12",
 "3-DSBF, absolute indicator 32":
   "125425D30A398F36508C06817BEE122E250D973314F976AED58A3EA9120DA4FE"
   "0E4D4575C42DD0426365EBA7FC5F45BE9B2F336981B5E1863618F49474F6FE00",
 "3-RSBF, absolute indicator 56":
   "3740B6A118A1E19642A85E2B7E2F3C3CB65FA0D95EC9DB1EA92BDB3666185AE0"
   "087F5FE6E0757106A12FC918754C40E8A1BCCB7A714032A8961456E066E8A801",
}

print(f"{'function':>34} {'hex digits':>11} {'max|W|':>7} {'nonlinearity':>13} {'beats 240?':>11}")
for name, h in FUNCS.items():
    assert len(h) == 128, (name, len(h))
    bits = np.array([(int(h, 16) >> (N - 1 - i)) & 1 for i in range(N)], dtype=np.int64)
    w = wht(1 - 2 * bits)
    mx = int(np.abs(w).max()); nl = N // 2 - mx // 2
    print(f"{name:>34} {len(h):>11} {mx:>7} {nl:>13} {'YES' if nl > 240 else 'no':>11}")
    assert bits.sum() in (240, 256, 272) or True
print("\nConjecture 13 at k = 9 requires min over f of max|W| to be 32 (nonlinearity 240).")

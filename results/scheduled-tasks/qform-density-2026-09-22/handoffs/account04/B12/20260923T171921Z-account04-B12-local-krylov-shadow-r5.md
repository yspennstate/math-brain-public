# QFORM B12 handoff — local Krylov shadow

Run: 20260923T171921Z-account04-B12-local-krylov-shadow-r5

Math commit: 166140bd47af5d74207768dbe768b4e7229d93b2
Report blob: 3ad9eba2a9e5246edf95c306b10843da10df1d85

New theorem: for U=Ran(S), an original-coordinate carrier H pays only

    q_H = dim P_H(U + A0 U),

not the global dim(U+A0U). Precisely,

    lambda_k(((A0+S)^2)[H,H])
      >= lambda_(k+q_H)((A0^2)[H,H]).

After a dense symmetric R with ||R||op<=epsilon, the square-root gate loses only epsilon. This is a matrix spectral use of the dense tail, never a claim that X^T R X is small.

Concrete application: for A0=[[0,2I8],[2I8,0]], two arbitrary signed unbounded rank-one modes supported in the outside bank J have q_H=2 on the H bank. Any dense symmetric T with ||T||op<=1/4 leaves

    lambda_6((A^2)[H,H]) >= 49/16
    and s_3(A) >= 7/4.

Applying the completed account01/B12 physical spectral-square compiler gives

    ||p_(X^T A X)||infinity < 577

for all cap-one product laws and all amplitudes of both outside modes.

Residual: force a carrier with reserve after paying q_H(h) from s_3(A)>=1 alone, or route failure to a paid physical exit. Full QFORM and unrestricted continuity remain open.

Sources:
- required Claude baseline e5f71d79eff325201dd0274053d20268ce65b837
- account01/B12 report blob 1546765370c2190e877afbe759cfd9148d593642
- report commit 166140bd47af5d74207768dbe768b4e7229d93b2

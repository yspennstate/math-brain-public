SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T02:15:48Z.
attacking: derive a leverage-peeling reduction that converts arbitrary extra large spectrum into either a proved terminal volume certificate or an explicit no-pivot obligation, then compile dependent completion through account04/B12.

# Early substantive checkpoint: scalar-pivot chain stability

Let L>0. For a real symmetric matrix H on independent original coordinates, suppose a physical scalar pivot a=H_ii satisfies |a|>=tau L. Writing the physical Schur complement S=H/H_ii and completing the square in the ORIGINAL coordinate X_i gives

Q_H=a(X_i+m(Y))^2+Q_S(Y),

where Y consists of the untouched independent original coordinates. If Q_S has density cap M, then the conditional square kernel obeys

p_{a(X_i+m)^2}(u)<=|a|^{-1/2} u^{-1/2} 1_{u>0},

uniformly in the translation m. Hence

||p_{Q_H}||_infty <= |a|^{-1/2} sup_t E|Q_S-t|^{-1/2}.

If ||p_{Q_S}||_infty<=M, then for every r>0,

E|Q_S-t|^{-1/2} <=4M sqrt(r)+r^{-1/2};

at r=(4M)^{-1} this is <=4 sqrt(M). Therefore

||p_{Q_H}||_infty <=4 sqrt(M/|a|).

Normalize M=B/L. Since |a|>=tau L,

B_new <= T_tau(B):=4 sqrt(B/tau).

The fixed point is B_*=16/tau and T_tau(B)=sqrt(B_* B). Thus after k scalar pivots,

T_tau^k(B)=B_*^(1-2^{-k}) B^(2^{-k}) <= max(B,16/tau).

Using the already-proved threshold-preserving Schur theorem from account03/B12 r21, each p=1 physical Schur elimination removes at most one eigenvalue of modulus >=L and does not reduce the threshold L. Therefore any number of EXTRA large eigenvalues can be peeled along such a scalar-pivot chain without a growing density constant: any terminal cap B/L propagates backward as at most max(B,16/tau)/L.

Two concrete terminal insertions to finish in the full report:

1. New volume-stability theorem (interactive 20260923T002323Z): if the terminal cross block has its near-diffuse certificate at scale aL, terminal density <23/(aL), hence the original density is <=L^{-1} max(23/a,16/tau).
2. Assigned partner account04/B12: any terminal mixed-norm certificate M(h)<=B/L survives an arbitrary measurable outside quadratic remainder psi(Z), so the same chain gives <=L^{-1} max(B,16/tau) without an independence claim between core and remainder.

Remaining work: state the exhaustive normalized tau=1 reduction, including the already-paid determinant-pair exit, and isolate the only unpaid no-pivot/high-rank or exactly-three-large terminal classes. Full QFORM remains OPEN.

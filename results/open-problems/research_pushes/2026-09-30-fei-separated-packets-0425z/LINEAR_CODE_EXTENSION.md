# Linear-code packet collisions also admit a paid degree reduction

2026-09-30 UTC. Status: proved scoped extension of the companion separated-packet report. Full FEI remains open. Novelty unverified.

## What this adds

The companion Sidon theorem isolates every cross-product separately. Here the packet centers form a linear code, so many pairs have the same difference. Keeping each entire collision sum still yields an exact pointwise Boolean field. Its low-degree slices provide a paid degree reduction when code distance is sufficiently large compared with code rank and packet radius.

The prior Sept19 coded-budget report, blob 6bd3cef08192616a27053f01edb94863e7ad3720, Section 3, proves exact/approximate entropy additivity for a product of two pre-existing Boolean functions under a code-separation hypothesis. That result is credited; the theorem here assumes no such factorization. No later-disproved resolvent candidate from that historical report is used.

## Theorem

Let C be a binary linear code in F_2^n, of rank r>=1 and minimum nonzero weight D. Let d>=0 be an integer and suppose

    D>4d,
    supp(fhat) subseteq union_(c in C) B(c,d)

for a genuine Boolean f. There is a family of genuine Boolean functions h_z on the original n physical variables, indexed by z in the dual group of C, such that deg(h_z)<=d.

Put m=sum_(c!=0) ||u_c||_2^2, where u_c are the packet fields constructed below. If m>0, then every h_z has strictly smaller real degree than f, and

    H(f) <= E_z H(h_z)+K [I(f)−E_z I(h_z)],              (1)

where one may take

    K=2[d+2r−1+log2(e)]/(D−2d).                         (2)

Thus any common child FEI constant C_target>=K carries unchanged to f. In particular, r<=d and D>4d imply K<3, so C_target>=3 is sufficient in that regime.

If m=0, f already has degree at most d and no reduction is claimed. Rank r=0 is the same low-degree case. The general theorem also includes d=0: all children are constants.

## Exact Boolean field from the colliding packets

The radius-d code balls are disjoint. Define degree-d fields uniquely by

    f(x)=sum_(c in C) chi_c(x) u_c(x).

Squaring and using closure of C under addition gives

    f(x)^2=sum_(v in C) chi_v(x) G_v(x),
    G_v(x)=sum_(c in C) u_c(x)u_(c+v)(x),
    deg(G_v)<=2d.

The Fourier supports of chi_v G_v lie in B(v,2d). These balls are pairwise disjoint because D>4d. The identity f^2=1 consequently forces

    G_0(x)=1,              G_v(x)=0 for v!=0             (3)

pointwise. No individual product in a colliding sum is discarded.

For z in the dual group of C, put

    h_z(x)=sum_(c in C) chi_c(z)u_c(x).

Equations (3) give h_z(x)^2=1 for every x,z. Thus h_z is Boolean and has degree at most d in x. Conversely, for each fixed x, the function z -> h_z(x) is a Boolean function on an r-dimensional cube, with Fourier coefficients u_c(x). This is the pointwise Boolean field that preserves all code-center collisions.

## Lower bound on the active code mass

For fixed x, Parseval and (3) give

    Var_z(h_z(x))=1−u_0(x)^2=sum_(c!=0)u_c(x)^2.

Any nonconstant Boolean function on r bits has variance at least

    4*2^(−r)(1−2^(−r)) >=2^(1−r).                       (4)

If m>0, choose one nonzero field u_c, c!=0. As a nonzero degree-d polynomial it is nonzero on at least a 2^(−d) fraction of physical x. On all those x the r-bit Boolean slice is nonconstant. Averaging (4) proves

    m>=2^(1−r−d),             log2(1/m)<=d+r−1.          (5)

This does not assume the individual u_c are ternary; that stronger assertion need not hold with code collisions.

## Entropy and influence accounts

The original labels (c,S) -> c+S are injective for |S|<=d. Let their probability law be uchat_c(S)^2. The conditional Walsh-uncertainty calculation in the companion report applies verbatim, because all h_z have exact norm one. It gives

    H(f)−E_zH(h_z) <=2H((||u_c||_2^2)_c).                (6)

For precision, if Q(c,S)=uchat_c(S)^2 and R(S,z)=2^(−r)hzhat(S)^2, then z is uniform and

    H(f)−E_zH(h_z)=H_Q(c|S)+I_R(S;z),
    I_R(S;z)<=H_Q(c|S).

The second inequality is exactly the normalized Walsh entropy uncertainty inequality, proved by interpolation in the companion report.

There are at most 2^r−1 nonzero-code labels. Equations (5) and h_2(m)<=m log2(1/m)+m log2(e) yield

    H((||u_c||_2^2)_c)
      <=h_2(m)+rm
      <=m[d+2r−1+log2(e)].                              (7)

Orthogonality of the code characters gives

    E_z I(h_z)=sum_c sum_S |S| uchat_c(S)^2.

The original influence uses |c+S| instead of |S|. Therefore

    I(f)−E_zI(h_z)
      =sum_c sum_S [|c+S|−|S|] uchat_c(S)^2
      >=(D−2d)m.                                        (8)

Combine (6)–(8) to prove (1)–(2). If m>0, some coefficient of f lies at degree at least D−d>d, while every child has degree at most d. Finally, if r<=d then d>=1, and

    2[d+2r−1+log2(e)]
      <=6d+2(log2(e)−1)<3(2d+1)<=3(D−2d).

This proves the displayed constant-three regime.

## Scope and verification

This is a constructive degree-induction step for exact code-ball support, including interacting centers. It does not assert that an arbitrary spectrum has such a decomposition, and it gives no entropy-stable approximate version. It excludes these configurations from a minimal-real-degree counterexample to any proposed constant satisfying (2), rather than from physical-restriction criticality alone.

The parent independently checked the grouped product identity, the minimum-variance/support argument for m, the conditional Walsh normalization, and the constant-three calculation before publication. The proofs are analytic; no executable code or numerical certificate is included.

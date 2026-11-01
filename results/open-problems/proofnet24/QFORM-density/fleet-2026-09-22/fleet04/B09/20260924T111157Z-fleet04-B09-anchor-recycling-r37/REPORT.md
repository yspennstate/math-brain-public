SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B09, 2026-09-24T11:11:57Z.
attacking: affine-anchor recycling for a literal mixed-hub star with arbitrary dense outside self-coupling, while preserving all original-coordinate independence after conditioning.

# fleet04/B09 — affine-anchor recycling for mixed-hub stars

Status: **NEW TARGET-VALID DENSE-COUPLING CHAMBER / FULL QFORM OPEN / CONTINUITY SEPARATE**

## 1. The general compiler

Let the original coordinates be split into two disjoint banks (K=H\sqcup I) and (J).  Let (Y=(Y_k)_{k\in K}) and (Z=(Z_j)_{j\in J}) be the corresponding independent cap-one product sources.  Fix a symmetric active matrix (A_0) on (K) satisfying the hypotheses of the completed mixed-hub Theorem H:

[
(A_0)_{II}=\sum_{
u=1}^r\lambda_
u v_
u v_
u^T+D_I,
]
where (D_I) is diagonal, and the rows
[
\widetilde\rho_i=((v_
u)_i:1\le\nu\le r; (A_0)_{ih}:h\in H)
]
have Gram matrix (widetilde G) and normalized leverages at most (1/2).

Choose completely arbitrary real matrices (L,C) of size (|K|\times |J|), and arbitrary symmetric (D) on (J).  Put
[
S=Y+LZ,
qquad
Q=S^TA_0S+2S^TCZ+Z^TDZ.                                      	ag{1}
]

### Theorem — mixed-hub affine-anchor recycling

For every (t\ne0),
[
|\phi_Q(t)|
\le (2|t|)^{-|H|}
   \prod_{
u=1}^r(4\pi |t\lambda_
u|)^{-1/2}
   (4\pi)^{r+|H|}\det(\widetilde G)^{-1/2}.                  	ag{2}
]

Thus every density or interval consequence of Theorem H transfers to (1) with exactly the same constant.  In particular, if (|H|+r/2>1), then (Q) has an essentially bounded density.

### Proof

Expand (1) before conditioning:
[
Q=Y^TA_0Y+2Y^T(A_0L+C)Z+c(Z),                                 	ag{3}
]
where
[
c(Z)=Z^T(L^TA_0L+L^TC+C^TL+D)Z.
]
Condition on the literal outside bank (Z=z).  The variables (Y_k) remain independent cap-one original-coordinate anchors.  Equation (3) is the same active quadratic form (Y^TA_0Y), plus an arbitrary affine term in (Y) and a constant.  Theorem H is uniform in all such affine terms, so (2) holds conditionally for every (z), and averaging in (z) proves it.

No translated coordinate (S_k) is asserted independent of any other (S_{k'}); indeed they may share every coordinate of (Z).  The proof uses only the independence of the unshifted anchors (Y_k) after conditioning.

The final matrix of (1), in the physical split (K\sqcup J), is
[
A=
\begin{pmatrix}
A_0&A_0L+C\\
L^TA_0+C^T&L^TA_0L+L^TC+C^TL+D
\end{pmatrix}.                                                  	ag{4}
]
Hence (A_0) is an actual principal block of the final matrix.  Positive and negative interlacing therefore transfer every threshold eigenvalue already present in (A_0).  This is an actual final-matrix spectral gate, not a statement about a discarded component.

## 2. Concrete target-valid chamber

Let (m\ge8) and choose flat orthonormal vectors (c,d,v\in\mathbb R^m).  On two literal hubs (a,b) and the (m) literal leaves (I), define
[
F_m(Y)=Y_a^2+2Y_a\langle c,Y_I\rangle
       +2Y_b\langle d,Y_I\rangle
       +\langle v,Y_I\rangle^2.                               	ag{5}
]
This is the completed fleet01/B09 mixed-hub example.  Its mixed rows are
[
\rho_i=(v_i,c_i,d_i),
qquad \sum_i\rho_i\rho_i^T=I_3,
qquad \|\rho_i\|^2=3/m\le1/2.                              	ag{6}
]
Here (|H|=2,r=1,lambda_1=1).  The fleet01/B09 inequality gives
[
|\phi_{F_m}(t)|\le8\pi^{5/2}|t|^{-5/2}.                       	ag{7}
]
Integrating (min(1,8\pi^{5/2}|t|^{-5/2})) yields
[
\|p_{F_m}\|_\infty\le {5\over3}2^{6/5}<3.829.                	ag{8}
]

Now translate every hub and leaf by an arbitrary common outside bank:
[
S=(Y_a,Y_b,Y_I)+LZ,
]
and set, for arbitrary (L,C,D),
[
Q=F_m(S)+2S^TCZ+Z^TDZ.                                         	ag{9}
]
The compiler proves
[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}
       \le {5\over3}2^{6/5}<3.829}.                            	ag{10}
]

The active principal block has spectrum
[
\left\{{1+\sqrt5\over2},{1-\sqrt5\over2}\right\}
\cup\{1,-1\}\cup\{1\}
]
plus zeros.  Therefore the final matrix (4) has at least three eigenvalues of modulus at least one, by interlacing.  Equation (10) is consequently a genuine subclass of the owner target, in every ambient dimension.

This chamber permits simultaneously:

- arbitrary dense self-coupling on the outside bank through (D);
- arbitrary dense active/outside coupling through (C);
- arbitrary sharing of the outside bank among all translated hubs and leaves through (L);
- arbitrary fragmented and unbounded cap-one input supports;
- no moments, support bounds, Gaussianity, or post-rotation independence.

## 3. What this does and does not close

The result closes dense self-coupling that can be placed on a bank disjoint from a paid literal mixed-hub anchor frame.  It does not handle a completely arbitrary dense quadratic twist living on the same active leaf bank (I); that twist destroys the exact low-rank-plus-diagonal factorization used by Theorem H.  The remaining B09 endpoint is precisely to pay that entangled active-leaf curvature, or force it into the disjoint (D_3), localized one-hub, diagonal-energy, or physical-core exits proved elsewhere.

The unrestricted QFORM conjecture and full-target continuity remain open.

## 4. Sources

- Fresh owner controls and assignment: `yspennstate/math-research-brain`, current main read during this run; target and correction set unchanged.
- Required Claude theorem H: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.
- Completed fleet01/B09 disjoint-leaf collision theorem: `yspennstate/math-open-problems@9f4a5bd1b7140117ad39b5b65fb5fe4db809b918`.
- Completed square-hyperbola/mixed-hub application used at (7)-(8): `yspennstate/math-open-problems@57b57dc6fa114b1c782a91599bdfbe94a358b2cb`.

No arbitrary-joint coarea estimate, density monotonicity, nonseparable product twist, or independence after rotation is used.

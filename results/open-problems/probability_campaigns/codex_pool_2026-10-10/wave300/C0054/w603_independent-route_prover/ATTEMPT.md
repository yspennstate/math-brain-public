# Independent spectral-pole route for C0054

2026-10-10. Target and assumptions: STATEMENT.md. Route precommit: APPROACH_PRECOMMIT.md, written before reading current peer proofs. Outcome so far: finite-dimensional pole-cancellation lemmas; no solution of C0054. Independent mathematical review pending.

## Prior-attempt digest and route boundary

C0054-A001 (intake attempts.jsonl, line 43) tried a fractional-moment decoupling argument across bandwidth-sized blocks. It reported a bandwidth-dependent loss and no bulk theorem. Its unsourced edge-localization sentence is not reused. Exact-ID searches found no additional C0054 record in the named H/I attempts or lean folders beyond the annotated ranking. Team O's board has no C0054 row. Current core-lane proofs have not been read.

This lane instead computes the joint resonant numerator/Schur denominator in the deleted minor's spectral basis. It does not assume that a Gaussian row is independent of the full resolvent. The intended gain is cancellation of minor poles before taking moments, rather than a product of one-step decoupling estimates.

## Lemma L1: exact bordering and resonant cancellation

Let B be a finite-dimensional Hermitian matrix, v a real scalar, h a complex column vector, and H=[[v,h*],[h,B]]. Define z=E+i eta with eta>0, R=(B-z)^(-1), and d=v-z-h*Rh. The first row of G=(H-z)^(-1) satisfies

    G_xx=1/d;  G_xy=-(h*R)_y/d.

Here x is the newly adjoined coordinate and y is a coordinate of B. If E is an eigenvalue of B, let P be its spectral projection. If Q=h*Ph>0, then

    lim_{eta->0+} G_xy(E+i eta) = (h*P e_y)/Q,
    lim_{eta->0+} G_xx(E+i eta) = 0.

Proof. Block multiplication proves the Schur formula; Im d=-eta-h*(Im R)h<0, so its denominator is nonzero. In finite dimension, write R=i P/eta+R_reg(eta); R_reg stays bounded because all other eigenvalues have a positive distance from E. Then eta d tends to -iQ and eta h*R e_y tends to i h*P e_y. Dividing proves both limits. The result remains valid when rank(P)>1: eigenvectors at E orthogonal to h have zero x-coordinate, so the full matrix may have a pole at E without a pole in this first-row limit.

Status: proved special case; no independent review yet. No claim about exchanging expectation and the eta limit is made.

## Lemma L2: exact Gaussian moment of a simple-pole transfer

Condition on B, and suppose E is its simple eigenvalue with unit eigenvector u. Let h be independent of B and proper centered complex Gaussian with covariance Sigma. Put t^2=u*Sigma u>0. v may be any finite real scalar, including a random scalar. For 0<s<2,

    E_h |lim_{eta->0+} G_xy(E+i eta)|^s
      = |u_y|^s t^(-s) Gamma(1-s/2).

If u_y is nonzero, the moment diverges for s>=2.

Proof. Alpha=u*h is proper complex Gaussian with variance t^2. Almost surely alpha is nonzero. By L1, the limit is conjugate(u_y)/alpha. The variable |alpha|^2/t^2 has the exponential density e^(-r), r>0. Its negative s/2 moment is the gamma integral Gamma(1-s/2), finite exactly for s<2. The formula is an expectation of the limit, not a limit of expectations.

For the Gaussian block model of STATEMENT.md, Sigma is the diagonal matrix of the x-row off-diagonal variances. If A_x consists of coordinates in the x block and its four neighboring blocks, excluding x, then

    t^2=(5 W^2)^(-1) sum_{j in A_x}|u_j|^2.

Consequently the simple-pole transfer moment is

    Gamma(1-s/2) (sqrt(5) W)^s |u_y|^s /
      (sum_{j in A_x}|u_j|^2)^(s/2).

This is an exact dependence on a deleted eigenvector's local mass. It neither proves decay of that mass ratio nor a spatial localization estimate. A tiny coupling mass can make the ratio large.

Status: proved special case; no independent review yet.

## Lemma L3: isotropic cluster formula

In L1, suppose rank(P)=r>=1 and P h is a proper complex Gaussian of covariance tau^2 P, tau>0. For P_yy>0 and 0<s<2r,

    E |lim_{eta->0+} G_xy|^s
      = P_yy^(s/2) tau^(-s)
        Gamma(1+s/2) Gamma(r-s/2) / Gamma(r+s/2).

Proof. In an orthonormal basis of ran(P), write Ph=R U, where U is uniform on the complex unit sphere in C^r, independent of R. Rotate P e_y to sqrt(P_yy) times the first basis vector. The transfer magnitude is sqrt(P_yy)|U_1|/R. R^2/tau^2 is Gamma(r,1), giving E R^(-s)=tau^(-s)Gamma(r-s/2)/Gamma(r). For r>1, |U_1|^2 is Beta(1,r-1), hence E|U_1|^s=Gamma(1+s/2)Gamma(r)/Gamma(r+s/2). For r=1, |U_1|=1 and the same formula holds. Multiplying proves the claim. The divergence threshold is s>=2r when P_yy>0.

Isotropy on ran(P) is an explicit extra assumption. It is generally false for a band row whose covariance vanishes outside neighboring blocks. Thus L3 is a benchmark, not an unrestricted band-matrix lemma.

Status: proved special case; no independent review yet.

## Lemma L4: a uniform two-site control and a failed shortcut

Take H=[[v,conjugate(h)],[h,0]], with v real, h proper complex Gaussian of variance tau^2, and E=0. For all eta>0,

    |G_xy(i eta)| = |h| / sqrt((|h|^2+eta^2)^2+eta^2 v^2)
                  <= 1/|h|.

For 0<s<2, dominated convergence therefore gives

    sup_{eta>0} E|G_xy(i eta)|^s
      = lim_{eta->0+} E|G_xy(i eta)|^s
      = tau^(-s) Gamma(1-s/2).

The supremum equals the limit because the upper bound is uniform and the pointwise limit attains it in expectation. v can be arbitrary or random: the bound does not depend on v. Meanwhile the deleted numerator alone has moment

    E|h*(B-i eta)^(-1)|^s
      = tau^s eta^(-s) Gamma(1+s/2).

Thus dropping the correlated Schur denominator invents an eta divergence absent from the exact ratio. Taking tau=1/W makes the exact transfer moment Gamma(1-s/2) W^s, which is not a uniformly contracting constant for large W. This is a two-site conditional benchmark and an obstruction to an unrestricted worst-case-minor contraction; it is not a counterexample to unconditional localization for the 2D Gaussian ensemble.

Proof. The 2x2 determinant is -|h|^2-eta^2-i eta v. Inversion yields the displayed magnitude and its bound. The Gaussian negative moment from L2 is integrable for s<2; apply dominated convergence. The numerator's positive moment follows from the same exponential integral.

Status: proved special case; no independent review yet.

## Attempt to close the bulk problem

Step 1 is complete at the finite-dimensional level: exact simple poles of the minor cancel against their own quadratic self-energy, with the explicit conditional moment in L2. L3 quantifies how a truly isotropic multi-mode coupling would change the cancellation. L4 shows why a regulator-divergent decoupled bound need not be the actual behavior.

Step 2 would need a bound for near-resonant clusters at a fixed deterministic energy, rather than conditioning on an exact eigenvalue of the minor. Exact E being an eigenvalue of an independently sampled continuous Gaussian minor has probability zero. Selecting a random minor eigenvalue and proving a pole limit does not control the deterministic-energy resolvent.

Step 3 would need to average the local mass ratio over the actual deleted-minor eigenvectors, uniformly in volume and regulator, and obtain strict decay across annuli. Conditional bounds at successive deleted minors may not be multiplied: their sigma-fields and eigenvectors overlap. No suitable tower-property iteration or block independence has been proved here.

Single hardest gap G1: prove a volume- and eta-uniform near-resonant spectral-cluster estimate for the actual 2D Gaussian band minor that yields strict decay of the boundary transfer across some finite scale at every fixed W. It must control the joint local coupling mass and remote eigenvector mass without assuming the desired localization of the minor. L2 exposes those masses, but does not bound them. The finite-scale length may need to be superpolynomial in W, consistent with the current primary delocalization results.

Even closing G1 would still require a rigorously stated localization implication and a separate eigenvalue-count/Minami-type argument for Poisson statistics. No such implication or count bound is claimed in this packet.

NEXT: Audit L1-L4, then attack the actual-band covariance and near-resonant-cluster version of G1 at deterministic bulk energy.

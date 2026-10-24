SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T00:31:27Z.
attacking: determinant-weighted finite-bank packets — close the bounded-coordinate spectral receiver, then separate genuinely diffuse third-compound mass from a fixed two-anchor survivor without selecting one tiny minor.

# account02/B07 — bounded-core compound receiver and q=0 diffuse-or-bianchor reduction

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Status:** ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED(intermediate bounded-cardinality core extraction from aggregate third-compound mass); FULL QFORM OPEN.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## 1. Exact target and source boundary

The target is: for arbitrary dimension, independent real original-coordinate inputs with marginal probability densities at most one, and real symmetric A with at least three eigenvalues of modulus at least one, prove a universal essential density bound for X^T A X, or give a valid counterexample. No moments, support bounds, log-concavity, iid assumption, diagonal-basis assumption, or independence after spectral rotation is used. Continuity remains separate.

Fresh owner control remained revision 2026-09-22.15. The mathematical correction ledger was reread; in particular this report does not use the refuted arbitrary-joint 3D coarea bound, worst conditional projection-density moments, pointwise law-uniform stationary phase, fiber suprema, or a universally good single coordinate minor.

Completed sources actually used:

1. `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md` and `RESULTS.md`: Theorem D and extension D' (volume-weighted original-coordinate decoupling), including the arbitrary-minor-weight AM-GM form.
2. `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`: projected-gradient finite-dimensional theorem, uniform in affine terms and arbitrary outside coefficients after conditioning on original coordinates.
3. Designated partner account03/B07, `yspennstate/math-open-problems@391688138f7f481a2c8688c2d27f9508db7af6af`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T000734Z-account03-B07-qform-r20/REPORT.md`: `QFORM-THIRD-COMPOUND-OVERLAP-COLORING-v1`, giving the four finite-bank packet lower bounds P0>=1/5184, P1>=1/3125, P2>=1/512, P3>=1/18.

The live no-pivot reduction from `GEOMETRIC_SYNTHESIS.md` is also used only as a reduction of scope: fix tau in (0,1], and consider matrices with |A_ii|<tau and every physical 2x2 principal determinant of magnitude <tau. Proving this N3 class suffices for the full target; N3 itself is open.

## 2. First unpaid implication, attacked immediately

Partner r20 converts total third-compound energy into a constant-mass packet on a bounded NUMBER of disjoint original-coordinate banks. What it does not provide is a bounded NUMBER of coordinates. The first question is therefore:

> If a constant amount of packet mass is captured on a bounded set H of original coordinates, can it be paid without choosing one individual minor?

Yes. The following receiver closes exactly that analytic step.

## 3. Bounded-core third-compound receiver

For an m by m real symmetric matrix B write

V3(B) = sum_{|I|=|J|=3} det(B[I,J])^2
      = ||wedge^3 B||_F^2
      = e_3(s_1(B)^2,...,s_m(B)^2),

where s_1>=s_2>=... are the singular values.

### Theorem 3.1 — QFORM-BOUNDED-CORE-COMPOUND-RECEIVER-v1

Let H be m>=3 original coordinates and B=A[H,H]. Suppose

V3(B) >= eta > 0,             ||B||_op <= L.

Then

s_3(B) >= sqrt(eta)/(sqrt(C(m,3)) L^2),                         (3.1)

and for the FULL ambient quadratic form, with arbitrary coefficients outside H and arbitrary affine terms created by conditioning,

||p_(X^T A X + b^T X + c)||_infinity
 <= 2 sqrt(6 pi m C(m,3)) L^2 / sqrt(eta).                      (3.2)

### Proof

Every term in e_3(s_1^2,...,s_m^2) has the form s_i^2 s_j^2 s_k^2 with i<j<k. Since k>=3,

s_i^2 s_j^2 s_k^2 <= L^4 s_3(B)^2.

There are C(m,3) terms, so

eta <= V3(B) <= C(m,3) L^4 s_3(B)^2,

which is (3.1). Because B is symmetric, its singular values are the absolute values of its eigenvalues, so B has three actual eigenvalues of modulus at least the right side of (3.1).

Condition on all ORIGINAL coordinates outside H. Product independence and the cap-one marginals inside H are unchanged; the outside values create only deterministic affine and constant terms. The completed projected-gradient finite-dimensional theorem at the source above gives, uniformly in those affine terms,

||p_(Q | X_(H^c))||_infinity <= 2 sqrt(6 pi m)/s_3(B).

Insert (3.1) and average the conditional interval inequality. This proves (3.2). No spectral rotation of the random inputs occurs. QED.

### Corollary 3.2 — explicit N3 receiver

Inside the no-tau-pivot class, tau<=1,

|B_ij|^2 <= |B_ii B_jj| + |det B[{i,j},{i,j}]| < tau^2+tau <=2tau.

Hence ||B||_op <= m sqrt(2tau), and (3.2) becomes

||p_Q||_infinity
 <= 4 tau m^2 sqrt(6 pi m C(m,3)) / sqrt(eta).                  (3.3)

Thus any partner packet (of ANY overlap type q=0,1,2,3) which places mass eta on a bounded physical support H is paid as an aggregate. No reciprocal individual determinant is selected.

In particular, if the whole selected partner packet is supported on m coordinates, then one may take respectively

eta = 1/5184, 1/3125, 1/512, 1/18.

More generally it suffices that any bounded H captures that much packet mass, because its terms are a subset of V3(A[H,H]). This is the promised integration of the completed bounded-dimensional spectral theorem into coordinate-core extraction.

## 4. q=0 packet: either Fourier payment or a fixed bi-anchor

The partner's q=0 branch supplies six disjoint original-coordinate banks L1,L2,L3,R1,R2,R3 and

P = sum det A[{i1,i2,i3},{j1,j2,j3}]^2 >= 1/5184,             (4.1)

where i_a belongs to L_a and j_b belongs to R_b.

Normalize the packet by

w_(S,T)=det(A[S,T])^2/P.

Let alpha_i=P_w(i in S) and beta_j=P_w(j in T). These are honest inclusion marginals and sum alpha=sum beta=3.

### Theorem 4.1 — QFORM-Q0-DIFFUSE-OR-BIANCHOR-v1

For the q=0 packet, one of the following holds:

1. the full QFORM output already satisfies

   ||p_Q||_infinity <= 9 sqrt(3e) P^(-1/6)
                    <= 106.921;                                (4.2)

2. there are fixed original coordinates i_* in L1 union L2 union L3 and j_* in R1 union R2 union R3 such that the determinant-weighted subpacket containing BOTH anchors has mass

   sum_{S contains i_*, T contains j_*} det(A[S,T])^2
      > P/3 >= 1/15552.                                       (4.3)

### Proof

The determinant-AM-GM step in Theorem D does not require the full volume-sampling law: for any weight w on nonzero 3x3 minors it produces the resource

Z_w = exp(E_w log(det(A[S,T])^2) + H(w)).

For the normalized squared-minor weights above, Z_w=P exactly. Extension D' then gives, whenever max_i alpha_i<=h<3/4,

||p_Q||_infinity
 <= 6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1) P^(-1/6).                (4.4)

Take h=2/3. The prefactor is 9 sqrt(3e), proving (4.2) if the row side is light. If instead the column side is light, apply exactly the same original-coordinate decoupling to the transposed cross block; A is symmetric, and the q=0 banks are disjoint, so the same bound follows.

If neither orientation is light, choose alpha_(i_*)>2/3 and beta_(j_*)>2/3. Under the same joint minor law w,

P_w(i_* in S and j_* in T)
 >= alpha_(i_*)+beta_(j_*)-1 >1/3.

Multiplying by P yields (4.3). QED.

This is aggregate-before-inversion: a diffuse packet is paid directly, while failure produces TWO fixed physical anchors carrying constant total third-minor mass, not one tiny 3x3 minor.

## 5. Target-valid stress: bounded coordinate cores cannot be the universal extraction

The bounded-core receiver is useful only when structural work actually compresses packet mass. The following exact N3 family proves that such compression cannot be demanded universally.

For even m>=4 let

A_m = diag(J_m/m, J_m/m, -J_m/m),                                (5.1)

where J_m is the all-ones m by m matrix.

### 5.1 Target and no-pivot checks

The nonzero spectrum is exactly {1,1,-1}; hence A_m is a genuine target matrix.

For any fixed tau in (0,1], once m>1/tau,

|A_ii|=1/m<tau.

A physical 2x2 principal determinant is zero for two coordinates in the same block and has magnitude 1/m^2 for coordinates in different blocks. Hence A_m lies in the live N3(tau) no-pivot class for all sufficiently large m.

### 5.2 Every bounded physical core loses its third eigenvalue

If H contains h_k coordinates from block k, then

A_m[H,H] = diag(J_(h1)/m, J_(h2)/m, -J_(h3)/m).

Its nonzero singular values are h_1/m,h_2/m,h_3/m. Therefore, for every fixed M and every |H|<=M,

s_3(A_m[H,H]) <= M/(3m) ->0.                                    (5.2)

So no theorem of the form

"constant global/packet third-compound mass => a bounded-cardinality physical core with s_3>=c"

can be true, even inside the exact target and the no-pivot class.

### 5.3 The determinant weight survives in a diffuse cross bank

Split EACH of the three m-coordinate blocks into equal halves. Put the three first halves in I and the three second halves in J. The physical cross block M=A_m[I,J] has exactly three nonzero singular values, all equal to 1/2. Consequently

Z_3=e_3(M^T M)=(1/2)^6=1/64.                                    (5.3)

Every nonzero 3x3 cross minor chooses one row and one column from each of the three blocks. Each such determinant has magnitude m^(-3), but there are (m/2)^6 of them, so

(m/2)^6 m^(-6)=1/64.                                             (5.4)

Thus a constant aggregate packet coexists with individual minors tending to zero.

The row volume marginals are exactly 2/m<=1/2. Applying the completed e5 Theorem D at the REAL inequality gives

||p_(X^T A_m X)||_infinity
 <= 6 sqrt(e) (1/64)^(-1/6)
 = 12 sqrt(e)
 < 19.785.                                                        (5.5)

Hence this is not a QFORM counterexample. It is a source-valid refutation of bounded-cardinality core extraction as a universal structural step, and simultaneously a positive example of the required repair: carry determinant volume through the diffuse bank and pay it before choosing any minor.

For completeness, the full third-compound overlap energies of A_m are

E_q = C(3,q) (m-1)^(3-q)/m^3, q=0,1,2,3,                        (5.6)

so E_0->1 while E_1,E_2,E_3->0. The family naturally lands in the partner's q=0 packet, exactly where Theorem 4.1/Theorem D is designed to receive it.

## 6. What is now paid and the first remaining implication

The coordinate-core side is now closed in the exact sense needed for N3:

- any bounded physical support carrying constant third-compound packet mass is paid by Theorem 3.1/Corollary 3.2;
- the partner q=0 packet is paid whenever either orientation has all packet marginals <=2/3;
- if q=0 is not paid, a fixed row anchor and fixed column anchor jointly carry >1/15552 of squared third-minor mass;
- the block-constant target family proves that the diffuse alternative is essential and is correctly paid by e5 Theorem D.

The sharpened first unpaid implication is therefore

**QFORM-Q0-BIANCHOR-RECEIVER-v1:** starting from two fixed disjoint original-coordinate anchors i_*,j_* and aggregate q=0 third-minor mass >1/15552 through both, obtain a universal product-preserving density/half-Riesz estimate, or route a constant fraction into a bounded physical core covered by Corollary 3.2. Do not select one residual 2x2 cofactor. In the live no-pivot class, the physical pair {i_*,j_*} itself may be singular or have arbitrarily small determinant, so the determinant-only pair theorem cannot simply be invoked.

For q=1,q=2,q=3, the same bounded-support receiver is complete, while genuinely diffuse shared-coordinate/Schur packets remain separate obligations. Partner r20's exact-zero/genuine-Schur splits should be retained there.

Full QFORM is **OPEN / NOT PROVED / NOT DISPROVED**. Continuous density in the unrestricted target remains separately open.

## 7. Exact checks

`checker.py` and `CHECKS.txt` in this immutable run directory verify the stress-family overlap formula, balanced cross volume, marginal threshold, constants, and a numerical regression of the elementary compound inequality used in Theorem 3.1. The checker is corroboration only; the universal steps above are analytic proofs.

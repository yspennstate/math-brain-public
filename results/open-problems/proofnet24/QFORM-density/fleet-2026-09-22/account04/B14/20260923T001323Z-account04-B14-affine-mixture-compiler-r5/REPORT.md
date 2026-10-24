SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B14, 2026-09-23T00:13:23Z.
attacking: zero-loss conditional localization for the new physical-fibre and ruled estimates, with the singular-block kernel term kept explicit.

# account04/B14 — affine-family localization compiler

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T001323Z-account04-B14-affine-mixture-compiler-r5
Status: SUPPORTING TARGET-LEVEL THEOREMS PROVED; FULL QFORM OPEN
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Target and exact source boundary

The target is the universal interval estimate

P{X^T A X in J} <= C |J|

for independent real original coordinates with probability densities at most one and every real symmetric A with at least three eigenvalues of modulus at least one.

Fresh owner controls were read from math-research-brain main. The newest path-specific source history for

proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/

still ends at commit 2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926. The source blobs used are RESULTS.md 56edacbd7aa105e7aaabfcfb6f377c268a134817, FOURIER_ROUTE_REPORT.md 9da148eed6cd43b1046a6f91d0f9329e12921cb4, and COUNTEREXAMPLE_SEARCH.md d11ace6dbf5ecdf6ce5921f80f727e92e95bf8fc. The previous Claude review correction blob 44ee51368aad3796beda43e15534087cd0b298fd was retained. In particular, no arbitrary-joint coarea estimate, post-rotation independence, bounded-diameter reduction, or universal good physical minor is used.

The completed assigned-partner input is account01/B14 r23, report blob 7908503d72472b58359c14e5011bcd65c0ba6a05. Its ruled rough-input theorem is applied below at an actual conditional inequality.

## 2. Uniform affine-family localization theorem

Let U=(X_i)_{i in S} and V=(X_i)_{i notin S}; these are independent original-coordinate blocks. Fix a symmetric matrix B on S and measurable maps ell(v) and r(v), and put

F(u,v)=u^T B u + ell(v)^T u + r(v).

Allow an additional measurable gate G(u,v), for example the one-sheet gate F(u,v)>=tau(v).

Theorem 2.1. Suppose that for every vector l, scalar c, every interval J, and every product law on U having smooth cap-one marginal densities,

P{U^T B U+l^T U+c in J and G_l,c(U)} <= C |J|,

where C is uniform in l,c and in the smooth product law. Then the same conditional-and-averaged inequality holds for arbitrary cap-one product laws on U and V:

P{F(U,V) in J and G(U,V)} <= C |J|.

Proof. Mollify only the U marginals: f_i,e=f_i*eta_e. They remain probability densities bounded by one and converge in L1. The product densities obey

|| product_i f_i,e - product_i f_i ||_1 <= sum_i ||f_i,e-f_i||_1.

For each fixed v the two event probabilities therefore differ by at most one half of this L1 distance, uniformly in ell(v), r(v), J and the gate. Apply the assumed smooth estimate for each v, integrate against the completely arbitrary law of V, and pass to the limit. No moment, support, diameter, fragment-count, or outside-density approximation is involved. QED.

Finite-mixture version. It is also enough to prove the same affine-uniform estimate when every U_i is uniform on a compact finite union of intervals of total measure one. Indeed every cap-one density is an L1 limit of finite convex combinations of such indicators. Expanding the product gives a convex combination of product-indicator laws, so the estimate passes first by multilinearity and then by total variation. This does not assert that an extremizing threshold set exists on the infinite line.

## 3. Exact kernel-leakage identity

Write ell=ell_R+ell_K with ell_R in Range(B) and ell_K in Ker(B). With the Moore-Penrose inverse,

u^TBu+ell^Tu+r
=(u+(1/2)B^dagger ell_R)^T B (u+(1/2)B^dagger ell_R)
 + ell_K^T u + r -(1/4)ell_R^T B^dagger ell_R.                 (3.1)

Thus translation removes exactly the range component and never the kernel component. When ell(v)=a+2Cv, a sufficient deterministic no-leakage condition is

P_Ker(B) a=0 and P_Ker(B) C=0.                                (3.2)

If B is invertible the condition is automatic. If B is singular, (3.1) shows precisely why a localization proof that simply completes the square is invalid: ell_K(v)^T u remains a nonseparable physical-fibre term. The compiler in Theorem 2.1 remains valid, but the input estimate must itself be uniform in this surviving term.

## 4. Application of account01/B14: ruled physical triple with arbitrary outside couplings

Let S be three original coordinates and B=A_SS be invertible of signature (2,1), with every eigenvalue magnitude at least sigma. Condition on V=X_{S^c}. Then

Q=U^T B U+ell(V)^T U+r(V),

while U retains its original independent cap-one law. Define

tau(V)=r(V)-(1/4)ell(V)^T B^{-1}ell(V).                       (4.1)

The completed account01/B14 ruled theorem, combined with Theorem 2.1, gives the actual target-level inequality

P{Q in J and Q>=tau(V)} <= (pi sqrt(2)/sigma)|J|              (4.2)

for every interval J, arbitrary rough/unbounded/fragmented input laws, arbitrary outside dimension and arbitrary couplings A_{S,S^c}. For signature (1,2), the reflected gate Q<=tau(V) satisfies the same estimate.

This is an essential-density estimate only on the moving one-sheet contribution. It is not a full rank-three theorem: the complementary two-sheet/convex event remains unpaid.

## 5. Application of the newest determinant-only physical-pair theorem

Let {i,j} be an actual original-coordinate pair whose principal block is indefinite, and put

D=|det A_{ {i,j},{i,j} }|,   s=s_3(A).

The newest completed physical-fibre theorem supplies, for all affine shifts, all remaining spectrum and all cap-one product laws,

P{X^TAX+b^TX+c in J}
 <= D^{-1/2}[9.2+log_+(10000 sqrt(D)/s)] |J|.                 (5.1)

The finite-mixture part of Theorem 2.1 shows in particular that proving (5.1) on finite-fragment indicator products would already prove it for arbitrary cap-one laws with no localization tax. For the normalized target s>=1 and a genuine coordinate-pair gate D>=delta>0, the function

x -> x^{-1/2}[9.2+log_+(10000 sqrt(x))]

is decreasing: in the active-log region its derivative has the sign of
1-[9.2+log(10000 sqrt(x))], and before that region x^{-1/2} is decreasing. Hence (5.1) yields the concrete uniform branch

||p_Q||_infinity
 <= delta^{-1/2}[9.2+log_+(10000 sqrt(delta))].               (5.2)

No support, translation or interval-extremizer hypothesis appears in (5.2).

## 6. What is new and what remains

The new result is the affine-family version of the zero-loss localization principle: one may approximate only the physical inside product law while leaving the conditioning variables, their tails, their fragments and every induced affine parameter untouched. Formula (3.1) is the exact guard against hiding kernel leakage.

Equations (4.2) and (5.2) are full-target inequalities on their stated structural branches. They do not finish the conjecture because s_3(A)>=1 does not force a universal delta in (5.2), and (4.2) controls only the moving one-sheet contribution. Diffuse no-pivot matrices may have every physical pair determinant tending to zero, and singular localized cores may violate (3.2). The first remaining implication is therefore one of:

1. aggregate many small physical fibres before paying D^{-1/2}; or
2. control the two-sheet/convex complement using product provenance; or
3. prove an affine-uniform singular-core estimate that absorbs ell_K rather than discarding it.

Continuity is separate. Uniform interval bounds imply an essentially bounded density but not a continuous representative.

## 7. Integrity

Full QFORM: OPEN.
New proved supporting result: uniform affine-family localization and finite-mixture compiler.
Completed partner actually applied: account01/B14 r23, report blob 7908503d72472b58359c14e5011bcd65c0ba6a05.
Newest Claude source pin: 2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926.
Owner control revision: 2026-09-22.15.
Native brain ingestion: NOT VERIFIED.

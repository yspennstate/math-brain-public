SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-24T02:12:25Z.
attacking: the double-aligned rank-one transverse collar; extract the exact zero-pivot Witt leakage invariant and pay its fully aligned endpoint without conditioning on dependent projections.

# account01/B11 auto11 — zero-pivot Witt leakage invariant and aligned endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.
Owner control revision consumed at startup: `2026-09-22.15`.
Status: **NEW STRUCTURAL REFINEMENT / NEW ESSENTIALLY-BOUNDED ZERO-PIVOT ENDPOINT / LATEST account02/B11 RESULT APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Nothing below assumes Gaussianity, log-concavity, moments, compact support, connected support, finite fragmentation, independence after spectral rotation, conditional density caps as independence, law-uniform pointwise van-der-Corput decay, or a generic bounded-density coarea theorem.

## 1. Source match and what is actually new

The exact rank-one compression at a zero physical pivot is **not new** and is not claimed here. It was already proved in account01/B18, `QFORM-ZEROPIVOT-TRANSVERSE-RANKONE-v1`: if

`A=[[0,b^T],[b,C]]`, `rank(A)=3`, `b!=0`, and `u=b/||b||`, then the compression of `C` to `u^perp` has rank exactly one. I use that theorem only as an algebraic starting point.

The immediate B11 predecessor is the hub-augmented crossing trichotomy at
`yspennstate/math-open-problems@950d6622fa0403f1b95a161f6da758c7f814fbfb`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260924T012158Z-account01-B11-QFORM-auto11/REPORT.md`.
It reduced the current rank-one-transverse collar to the exact double-aligned endpoint after every nonzero leakage had produced a paid ORIGINAL-source three-dimensional crossing.

The prior analytic receiver used below is this slot's `QFORM-ZEROPIVOT-PLANAR-DENSITY-v1`, recorded at
`yspennstate/math-open-problems@0ddfb16815f0d27adda888a3f77935e141ae928b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T184428Z-account01-B11-QFORM-auto11/REPORT.md`.
For a cap-one scalar `H` independent of a planar random vector `Y` of joint density cap `M`, every invertible symmetric `3x3` Hessian with zero `H`-pivot has

`||p_Q||_infinity <= 3*2^(2/3) M^(2/3) |det Hess(Q)|^(-1/3)`.

The latest completed designated partner is account02/B11's `L^3 x L^(3/2)` third-square compiler, canonical mathematics
`yspennstate/math-open-problems@02aedcd3be33ace107851fa74e0b9ac846d0aa25`, run root
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/B11-20260924T012138Z-auto11/`.
It is applied quantitatively in Section 5.

## 2. New exact normal form: the zero-pivot Witt leakage invariant

Let `A` be a real symmetric matrix of rank exactly three. Fix an ORIGINAL physical coordinate `h` with

`A_hh=0`,

and suppose its physical star is nonzero. Put `J=[n]\{h}`,

`c=A[J,h]`, `kappa=||c||>0`, `u=c/kappa`, `B=A[J,J]`, `P_u=I-uu^T`.

By the pre-existing B18 rank-one compression theorem,

`C=P_u B P_u |_(u^perp)`

has rank exactly one. Therefore for a unit `v in u^perp` and a nonzero scalar `lambda`,

`C=lambda v v^T`.

Define

`q=P_u B u`,
`eta=<q,v>`,
`q_perp=q-eta v`,
`gamma=||q_perp||>=0`.

If `gamma>0`, put `p=q_perp/gamma`; if `gamma=0`, omit `p`. Then `u,v,p` are orthonormal coefficient vectors in the ORIGINAL residual coordinate space. With

`H=X_h`, `L=<u,X_J>`, `V=<v,X_J>`, `P=<p,X_J>`,

and `b=<u,Bu>`, the full quadratic form depends on no other residual projection and has the exact identity

`boxed: Q = 2 kappa H L + b L^2 + 2 eta L V + 2 gamma L P + lambda V^2.`      (2.1)

No probabilistic rotation has been made: `(L,V,P)` are orthogonal projections of the residual product source and may be internally dependent, while the ORIGINAL scalar `H` is genuinely independent of the whole residual bank.

### Proof of (2.1)

Use the orthogonal decomposition `R^J=span(u) direct_sum u^perp`. Relative to `(H,u,u^perp)`,

`A = [[0,kappa,0],[kappa,b,q^T],[0,q,C]]`.

The pre-existing rank calculation gives `rank C=1`, hence `C=lambda vv^T`. Splitting `q=eta v+gamma p` leaves no quadratic coefficient on the orthogonal complement of `span(u,v,p)`. Expanding the form gives (2.1).

The new point is the following exact spectral currency.

### Theorem `QFORM-ZEROPIVOT-WITT-LEAKAGE-INVARIANT-v1`

If `mu_1,mu_2,mu_3` are the three nonzero eigenvalues of `A`, then

`boxed: |mu_1 mu_2 mu_3| = |lambda| (kappa^2+gamma^2).`               (2.2)

In particular, if every nonzero eigenvalue has magnitude at least `s`, then

`boxed: |lambda|(kappa^2+gamma^2) >= s^3.`                            (2.3)

### Proof

On the active orthonormal coordinates `(H,L,V,P)`, the symmetric matrix is

`T=[[0,kappa,0,0],
    [kappa,b,eta,gamma],
    [0,eta,lambda,0],
    [0,gamma,0,0]].`

It has rank three. For a rank-three `4x4` symmetric matrix the product of the three nonzero eigenvalues is `e_3(T)`, the sum of its principal `3x3` minors. Only two are nonzero:

`det T[H,L,V] = -kappa^2 lambda`,
`det T[L,V,P] = -gamma^2 lambda`.

Thus

`mu_1 mu_2 mu_3 = -lambda(kappa^2+gamma^2)`,

which is (2.2). QED.

This identity refines the earlier rank-one compression: the third direction is not only known to exist, but its exact determinant budget splits into an ORIGINAL independent-hub contribution `kappa^2|lambda|` and an internally dependent leakage contribution `gamma^2|lambda|`.

## 3. A newly paid endpoint: `gamma=0`

When `gamma=0`, (2.1) drops the only residual direction outside the curvature plane:

`Q = 2 kappa H L + b L^2 + 2 eta L V + lambda V^2.`                  (3.1)

Here `H` is an ORIGINAL cap-one scalar independent of the planar vector `(L,V)`. Since `u,v` are orthonormal coefficient vectors in the residual ORIGINAL product source, the standard two-dimensional product-marginal theorem gives

`||p_(L,V)||_infinity <= 2`.                                         (3.2)

The Hessian of (3.1) in `(H,L,V)` is

`T_3=[[0,kappa,0],[kappa,b,eta],[0,eta,lambda]]`,

with

`det T_3=-kappa^2 lambda`.                                           (3.3)

Apply `QFORM-ZEROPIVOT-PLANAR-DENSITY-v1` with planar cap `M=2`:

`||p_Q||_infinity
 <= 3*2^(4/3) (kappa^2 |lambda|)^(-1/3).`                            (3.4)

At `gamma=0`, the spectral identity (2.2) gives

`kappa^2 |lambda| = |mu_1 mu_2 mu_3| >= s^3`.

Therefore

`boxed: ||p_Q||_infinity <= 3*2^(4/3)/s < 7.560/s.`                  (3.5)

This proves a genuine full-line density bound for the entire **Witt-aligned exact-zero-pivot endpoint**, with no leverage assumption and no independence between `L` and `V`.

This endpoint is automatically indefinite: a nonzero vector with zero quadratic value for a nonsingular rank-three form cannot occur in a definite signature. Negating `A` interchanges `(+,+,-)` and `(+,-,-)`, so (3.5) covers both signs.

Continuity is **not** claimed from this argument; (3.5) establishes essential boundedness.

## 4. Consequence for the current double-aligned B11 collar

The predecessor left the exact rank-one-transverse **double alignment** `p_0=q_0=0`, where no natural ORIGINAL cross cut has rank three. In the zero physical-pivot subbranch, the present theorem gives a second, intrinsic alignment parameter `gamma` after quotienting the physical star.

The endpoint `gamma=0` is now paid by (3.5). Hence the first zero-pivot survivor in this collar must satisfy

`gamma>0`,

and has the exact product-provenance form

`Q = 2 kappa H L + b L^2 + 2 eta L V + 2 gamma L P + lambda V^2`,

where `(L,V,P)` is an internally dependent orthonormal projection of the residual product source and

`|lambda|(kappa^2+gamma^2)>=s^3`.

This formulation makes the unresolved issue narrower than “rank-two crossing plus curvature”: it is specifically the **same-bank leakage-to-square interaction**. The source-independent part of the determinant is already enough at `gamma=0`; only a nonzero internally dependent `LP` term remains.

## 5. Latest account02/B11 result applied to an actual inequality

Account02/B11's new compiler proves: if `H` is genuinely independent of the source producing `U` and an arbitrary same-bank phase `Psi`, and an additional scalar `K` is genuinely source-independent of all of them, then

`Z=(bU+d)H+Psi+aK^2`

obeys

`||p_Z||_infinity
 <= 4*3^(1/3) (F G L_K)^(2/3) (|b|^2 |a|)^(-1/3)`,                  (5.1)

where `F,G,L_K` are the relevant density caps. The proof is the determinant-homogeneous `L^3 x L^(3/2)` pairing.

Apply it to the actual target-valid indefinite family

`Q_q = 2 kappa (sqrt(q) H + sqrt(1-q) T) W + c K^2`,                 (5.2)

where `H,K` and the ORIGINAL bank generating the orthonormal pair `(T,W)` are mutually source-disjoint, all original scalar densities are capped by one, and `0<q<=1`. The entire same-bank puncture `2 kappa sqrt(1-q) T W` remains inside `Psi`; it is not dropped. The coefficient matrix on the global orthonormal forms `(H,T,W,K)` has spectrum

`{+kappa,-kappa,c,0}`.

Using `||p_W||_infinity<=sqrt(2)`, account02/B11 gives exactly

`boxed: ||p_(Q_q)||_infinity
 <= 2*12^(1/3) (kappa^2 q |c|)^(-1/3).`                              (5.3)

Thus, in the near-coloop range `q>=63/64` and under `kappa^2|c|>=s^3`,

`boxed: ||p_(Q_q)||_infinity <= 4.602956661318305/s.`                (5.4)

This application is useful for the present structural picture: (5.2) is the source-disjoint-square version of the leakage normal form. It confirms that the determinant-homogeneous third direction is exactly strong enough once its square lives on a genuinely separate source. The still-open case is when the square variable `V` belongs to the same residual product projection as `L,P`.

The partner theorem gives continuity in the source-disjoint-square subclass of (5.2).

## 6. Rank-two logarithmic benchmark and the exact role of direction three

For independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|)),  0<|t|<1/2.`                             (6.1)

So one opposite-sign hyperbolic pair is genuinely unbounded. The present zero-pivot normal form identifies the third direction in two complementary ways:

1. Algebraically, it is the rank-one curvature `lambda V^2`, with exact budget
   `|lambda|(kappa^2+gamma^2)=|mu_1mu_2mu_3|`.
2. At the fully aligned endpoint `gamma=0`, the square turns the `1/|L|` saddle Jacobian into the integrable half-order kernel in the zero-pivot planar proof, yielding (3.5).
3. When the square is source-disjoint, account02/B11 shows the same mechanism as an exact `L^3 x L^(3/2) -> L^infinity` pairing at determinant scale.

Thus the third direction is not a fictitious independent eigen-coordinate. It is a rank-one curvature direction whose usefulness depends on how its ORIGINAL-source provenance interacts with the hyperbolic bank.

## 7. First unpaid implication

The immediate B11 gap is now

`QFORM-ZEROPIVOT-WITT-SAMEBANK-LEAKAGE-TO-LINF-v1`:

> In the exact-rank-three zero-pivot normal form (2.1), assume `gamma>0`, `(L,V,P)` is the internally dependent orthonormal projection of the same cap-one product source, and `|lambda|(kappa^2+gamma^2)>=s^3`. Prove a universal full-line density bound, uniformly as `gamma->0`, while retaining `2 gamma L P`; or force an already-paid ORIGINAL-source pair/volume/independent-square exit.

The newest account02/B11 result pays the source-disjoint-square analogue but explicitly does not justify an `L^3 x L^(3/2)` convolution when `V` shares the residual source. The live arbitrary-joint coarea and conditional-cap corrections forbid replacing this dependence by a bounded joint density or conditional independence.

After this zero-pivot step, the nonzero-pivot double-aligned collar and the arbitrary-additional-nonseparable-spectrum bridge remain separate debts.

## 8. Verification

`VERIFY.py` in this run directory checks two things.

First, for 5,000 random active canonical matrices it verifies rank three and

`product(nonzero eigenvalues) = -lambda (kappa^2+gamma^2)`.

Second, for 1,000 random orthogonal embeddings into higher-dimensional residual spaces it reconstructs `u`, the rank-one compressed curvature, and `gamma` from the physical matrix and verifies the same invariant. The observed worst relative errors are recorded in `VERIFY_OUTPUT.txt`.

Numerical constants checked there are

`3*2^(4/3)=7.559526299369239`,

and the partner near-coloop constant

`2*12^(1/3)*(64/63)^(1/3)=4.602956661318305`.

These finite checks verify only the algebra/numerics; the proofs above carry the mathematical claims.

## 9. Scope

- `QFORM-ZEROPIVOT-WITT-LEAKAGE-INVARIANT-v1`: **PROVED structural refinement**.
- `gamma=0` exact-rank-three zero-pivot density bound `<7.560/s`: **PROVED essential boundedness**.
- latest account02/B11 source-disjoint-square bound `<4.603/s` in its stated near-coloop family: **APPLIED**.
- full exact-rank-three zero-pivot branch: **OPEN** because `gamma>0` same-bank leakage remains.
- full owner conjecture with arbitrary additional spectrum: **OPEN**.
- full continuity claim: **OPEN**.

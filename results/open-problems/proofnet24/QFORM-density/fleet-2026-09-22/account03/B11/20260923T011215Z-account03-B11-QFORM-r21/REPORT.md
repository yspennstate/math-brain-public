# QFORM B11 r21 — null-Schur ruling lifts product-partition smoothing through arbitrary hub overlap

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T01:12:15Z.

attacking: near-coloop no-tangent-ray aggregation via exact null-cone geometry and a bank-vs-spread dichotomy in the residual spectral plane.

## Status

**ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL TARGET OPEN.**

Execution label: **WITHOUT_VERIFIED_BRAIN**.

This run changes mechanism from the previous tangent-ray theorem.  Instead of trying to separate the heavy null hub from the residual spectral variables, it conditions on that original coordinate and uses an exact null-Schur ruling to turn *all* hub overlap into coordinatewise translations of the remaining product law.  Any translation-uniform residual product theorem then lifts to the full form with no loss depending on the hub leverage.

The theorem is valid for arbitrary cap-one product laws, disconnected/unbounded supports, and both indefinite signatures.  It uses neither post-rotation independence nor a conditional-density substitute for independence.

## 1. General null-Schur ruling transfer

Split one **original coordinate** from the others and write

\[
A=\begin{pmatrix}0&a^T\\ a&B\end{pmatrix},\qquad X=(\xi,Y),
\]

where \(\xi\) is independent of the product vector \(Y\).  Assume there is a deterministic vector \(v\) such that

\[
Bv=a,\qquad v^TBv=0. \tag{1.1}
\]

Then

\[
\boxed{X^TAX=(Y+v\xi)^TB(Y+v\xi).} \tag{1.2}
\]

Indeed,

\[
(Y+v\xi)^TB(Y+v\xi)
=Y^TBY+2\xi v^TBY+\xi^2v^TBv
=Y^TBY+2\xi a^TY.
\]

### Theorem 1.1 (translation-uniform theorem compiler)

Suppose there is a constant \(C_B\) such that for **every** deterministic translation \(z\in\mathbb R^{n-1}\), and for every independent cap-one product law of \(Y\),

\[
\|p_{(Y+z)^TB(Y+z)}\|_\infty\le C_B. \tag{1.3}
\]

Then

\[
\boxed{\|p_{X^TAX}\|_\infty\le C_B.} \tag{1.4}
\]

Proof. Condition only on the original variable \(\xi=x\).  The coordinates of \(Y+vx\) remain independent and each density is merely translated, hence still bounded by one.  Apply (1.3) with \(z=vx\), uniformly in \(x\), and average the conditional interval estimates over \(\xi\).  QED.

The point is structural: the hub may be spectrally entangled with **every** residual direction.  Equation (1.2) removes that overlap exactly before any density estimate is made.

## 2. Exact-rank-three null coordinates automatically satisfy the ruling identity

Let

\[
A=RMR^T,\qquad R^TR=I_3,
\]

where \(M\) is invertible of inertia \((2,1)\) or \((1,2)\).  Let \(r_i^T\) be the \(i\)-th physical row of \(R\), put \(c_i=\|r_i\|^2\), and assume the single physical diagonal is null:

\[
A_{ii}=r_i^TMr_i=0. \tag{2.1}
\]

For \(0<c_i<1\), delete row \(i\) and set

\[
R_-=R_{[n]\setminus\{i\}},\quad G=R_-^TR_-=I-r_ir_i^T,
\]
\[
B=R_-MR_-^T,\qquad a=R_-Mr_i,\qquad v=R_-G^{-1}r_i. \tag{2.2}
\]

Since \(G\) is invertible,

\[
Bv=R_-MGG^{-1}r_i=R_-Mr_i=a, \tag{2.3}
\]

and

\[
v^TBv=(G^{-1}r_i)^TGMG(G^{-1}r_i)=r_i^TMr_i=0. \tag{2.4}
\]

Thus every non-coloop null physical coordinate in an exact-rank-three form satisfies Theorem 1.1.  Also, by Sherman--Morrison,

\[
\boxed{\|v\|^2=\frac{c_i}{1-c_i}.} \tag{2.5}
\]

The norm may diverge as \(c_i\uparrow1\), but crucially **the density constant in (1.4) does not depend on \(\|v\|\)**: arbitrary translations cost zero under cap-one hypotheses.  This is precisely the near-coloop feature that the previous tangent-ray route did not exploit.

At the endpoint \(c_i=1\), the complementary spectral frame has rank two and the hub itself is an independent full null scalar.  The completed account04/B11 null-scalar theorem applies directly; see Section 4 below.

## 3. Lifting the completed account04/B11 theorem

Completed designated partner source:

`yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`.

Its quantitative theorem is the following.  If \(Z\) is independent of \((V,W)\), with

\[
\|p_Z\|_\infty\le L,\qquad \|p_{V,W}\|_\infty\le M,
\]

then for arbitrary affine terms

\[
T=2\alpha ZW+\beta V^2+2\gamma VW+\delta W^2+\text{affine},
\quad \alpha\beta\ne0,
\]

one has

\[
\boxed{
\|p_T\|_\infty\le
3\,2^{2/3}(LM)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}.
} \tag{3.1}
\]

The partner proof is translation-stable: translating any of the underlying independent original-coordinate banks changes only their densities by translation and/or introduces affine terms, neither of which changes (3.1).

### Theorem 3.1 (null-ruling partner lift)

Assume (1.1).  Suppose the residual original coordinates admit a disjoint product partition to which the partner theorem applies with parameters \(L,M,\alpha,\beta\).  Then the **full** form, including arbitrary spectral overlap of the null hub with those residual banks, satisfies

\[
\boxed{
\|p_{X^TAX}\|_\infty\le
3\,2^{2/3}(LM)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}.
} \tag{3.2}
\]

Proof.  Condition on \(\xi=x\).  By (1.2) the conditional law is the residual quadratic form evaluated at the translated product vector \(Y+vx\).  The residual bank independence, the scalar cap \(L\), and the pair cap \(M\) are unchanged by this deterministic coordinatewise translation.  Apply the partner inequality (3.1) for every \(x\), then average.  QED.

When the scalar residual bank is one cap-one original coordinate and the pair is an orthonormal two-dimensional projection of a disjoint product bank, the partner uses \(L=1,M\le e\), giving

\[
\boxed{
\|p_Q\|_\infty\le
3(2e)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}
<9.276\,|\alpha|^{-2/3}|\beta|^{-1/3}.
} \tag{3.3}
\]

No factor depending on \(c_i\), \((1-c_i)^{-1}\), or \(\|v\|\) appears.

This is a genuine overlap compiler: the null hub need not be disjoint from the pair bank in spectral space.  Only the *residual original-coordinate partition* must carry genuine product provenance.

## 4. Actual target example and partner inequality

Take four independent cap-one variables \((X_0,Z,V,W)\) and

\[
A=
\begin{pmatrix}
0&-1/2&1&1\\
-1/2&0&0&1\\
1&0&1&0\\
1&1&0&0
\end{pmatrix}. \tag{4.1}
\]

Let

\[
B=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},\qquad
v=(1,1,-1/2)^T.
\]

Then

\[
Bv=(-1/2,1,1)^T=:a,\qquad v^TBv=0. \tag{4.2}
\]

Therefore

\[
Q= X^TAX
=( (Z,V,W)^T+X_0v)^TB((Z,V,W)^T+X_0v). \tag{4.3}
\]

Equivalently, before translation,

\[
Q=2ZW+V^2+2X_0(-Z/2+V+W). \tag{4.4}
\]

The hub \(X_0\) couples to **all three** residual coordinates, so this is not a separated hub example.  Yet after conditioning on \(X_0\), (4.3) is exactly a translated version of the residual canonical saddle-plus-square.

The characteristic polynomial is

\[
\chi_A(\lambda)=\frac14\lambda(\lambda-1)(4\lambda^2-13), \tag{4.5}
\]

so the spectrum is

\[
\{0,1,\sqrt{13}/2,-\sqrt{13}/2\}. \tag{4.6}
\]

Thus this is a genuine target instance with signature \((2,1)\) and all three nonzero eigenvalue magnitudes at least one.  Here the partner theorem has \(\alpha=\beta=1\), and because \(Z,V,W\) are themselves independent original coordinates, \(L=M=1\).  Hence

\[
\boxed{
\|p_Q\|_\infty\le3\,2^{2/3}=4.762203155904598\ldots .
} \tag{4.7}
\]

Negating \(A\) gives a genuine \((1,2)\) example with the same bound.

This is an actual application of the completed designated partner result, not merely a citation.

## 5. Where the third direction removes the rank-two logarithm

For independent \(X,Y\sim\mathrm{Unif}[-1/2,1/2]\), the opposite-sign rank-two control remains

\[
 p_{2XY}(t)=\log\frac1{2|t|},\qquad 0<|t|<1/2. \tag{5.1}
\]

The partner theorem shows exactly what the third direction does in

\[
2\alpha ZW+\beta V^2+2\gamma VW+\delta W^2.
\]

Conditioning at fixed \(W=w\), the hyperbolic variable gives a \(1/|w|\) density scale.  Convolution with the independent square-curvature variable \(\beta V^2\) changes the near-singular kernel to \(|w|^{-1/2}\), which is locally integrable.  Splitting at \(|w|=r\) gives a near cost proportional to \(r^{1/2}\) and a far cost proportional to \(r^{-1}\); optimization yields the determinant-homogeneous exponents in (3.1).

The new point of this run is that a null hub that overlaps every residual spectral direction can be removed **exactly as a product-law translation** before this smoothing is applied.  It neither recreates the logarithm nor costs a leverage factor.

## 6. Relation to the small-positive-D0 / near-coloop obstruction

The newest account01/B11 exact null-ruling work shows, in the zero-diagonal exact-rank-three chamber, that a heavy null hub has an exact translated residual form and a matched minority-sign residual curvature.  The present theorem pays the analytic estimate whenever that residual curvature can already be exposed through a genuine partner-compatible product partition.

Therefore the remaining small-positive-D0 obstruction is now sharper:

> it is **not** the spectral overlap of the heavy null hub itself.  The hub can be conditioned away at zero density cost.  The unpaid step is to compile the residual dense matched-curvature direction into a disjoint original-coordinate scalar/pair (or another already-paid ridge/pair/grouped-bank certificate) without rotating the independent inputs.

In particular, small \(1-c_i\) is not a perturbative parameter: without moments or bounded support, the residual translated coordinates can live on arbitrarily large scales.  The ruling identity avoids that invalid perturbation entirely.

A next implication is

`QFORM-RESIDUAL-MATCHED-CURVATURE-TO-PRODUCT-PARTITION-v1`:
from the account01/B11 certificate \(|u^TBu|\ge s/2\) and an original-coordinate residual cross cut \(\|B_{S,T}\|_{op}\ge s/4\), force either a partner-compatible disjoint scalar/pair bank with determinant payment at universal scale, or an existing ridge/diffuse/grouped-bank exit.  Failure of a single good physical minor must not be used as a contradiction.

## 7. Scope and continuity

This report proves an essential-L-infinity density bound in the exact null-Schur/product-partition branch, and gives an explicit four-coordinate target instance.  It does **not** prove that every three-large-eigenvalue matrix admits the needed residual partition, and it does not absorb arbitrary additional spectrum unless it is already covered by the residual theorem being lifted.

The full universal conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**.

Continuity is **not proved by this argument**.  The result established here is the interval/essential-density bound only.

## Sources and corrections consumed

- Fresh owner control main commit `6252e3caaeaae3d24aa15d8ee9558a3ff3c9fe54`, OWNER CONTROL revision `2026-09-22.15`.
- `CURRENT_RESEARCH.md`: full target open; arbitrary-joint rank-three coarea and conditional positive-moment gates are false.
- Live correction inbox, including `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and the standing pointwise-decay/fiber-sup/rotation corrections.
- Completed designated partner: `yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`.
- Structural null-ruling source used and independently rederived above: `yspennstate/math-open-problems@e4a8345b649c8340ec34182c25ee7c76c970ed6c`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T001151Z-account01-B11-QFORM-r12/REPORT.md`.

No pointwise van-der-Corput bound, arbitrary-joint coarea bound, diagonal-basis independence, conditional-cap-as-independence step, fiber supremum, or Monte Carlo extremality claim is used.

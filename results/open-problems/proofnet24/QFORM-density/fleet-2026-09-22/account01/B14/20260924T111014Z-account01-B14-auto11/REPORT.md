SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T11:10:14Z.
attacking: environment-adaptive one-copy difference localization — let the copied-side fragments move arbitrarily with the outside coordinates, prove that convolution with the undecomposed copy still repairs every conditional fragment to cap one, and apply the completed account02/B14 theorem inside an actual indefinite target chamber.

# B14 report: environment-adaptive difference-side localization

Status: **NEW SUPPORTING LOCALIZATION THEOREM / COMPLETED PARTNER RESULT APPLIED / FULL QFORM OPEN**. Continuity of the unrestricted output density remains separate.

The run initially tested whether the preceding finite-fragment theorem could be sharpened to a countable rational skeleton. Repository search showed that this was already proved in earlier B14 work (`QFORM-COUNTABLE-RATIONAL-SKELETON-LOCALIZATION-v1`, including account03/B14 20260923T114804Z and an earlier account01/B14 run). I therefore did not relabel that as new progress and changed mechanism to the difference-side theorem below.

## 1. Completed designated-partner result consumed

The newest completed compatible account02/B14 result is

- commit `388f936ef5954b951203df7bab568a64e0afe985`,
- run `20260924T110401Z-account02-B14-QFORM-auto11`,
- theorem `QFORM-ONE-COPY-DIFFERENCE-LOCALIZATION-v1`.

For a cap-one probability density `f` and an arbitrary positive subdensity `rho` of mass `m`, it proves

\[
G_\rho(w)=\int f(w+y)\rho(y)\,dy,\qquad
\int G_\rho=m,\qquad 0\le G_\rho\le m.
\]

Thus `gamma_rho=G_rho/m` is again a cap-one probability density. Coordinatewise, any finite/countable product localization of only one duplicated copy becomes an exact convex mixture of admissible product cap-one difference laws. The partner then applies this to the fixed-source volume-sampling decoupling theorem D without fragment tax.

The source theorem D used by the partner is at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. In its order-three scope, if `M=A_{IJ}`, `Z=e_3(M^TM)`, and the volume-sampling row marginals are at most `1/2`, then

\[
\|p_Q\|_\infty\le 6\sqrt e\,Z^{-1/6},
\tag{1.1}
\]

with arbitrary affine terms allowed in the active variables.

## 2. New theorem: environment-adaptive one-copy localization

### Theorem `QFORM-ENVIRONMENT-ADAPTIVE-ONE-COPY-DIFFERENCE-LOCALIZATION-v1`

Let `T` be an arbitrary random element. Independently of `T`, let

\[
Y=(Y_j)_{j\in J},\qquad Y'=(Y'_j)_{j\in J}
\]

be independent copies of a product law with one-dimensional densities `0<=f_j<=1`.

For every coordinate `j`, let `A_j` be finite or countable and let

\[
\theta_{j,a}(t,y)\ge0,\qquad
\sum_{a\in A_j}\theta_{j,a}(t,y)=1
\tag{2.1}
\]

be an arbitrary measurable soft partition. The partition is allowed to depend on the entire outside environment `t`; its cells may move arbitrarily far, have unbounded support, have no moment control, and may change shape with `t`.

For fixed `t`, put

\[
\rho_{j,a,t}(y)=f_j(y)\theta_{j,a}(t,y),
\qquad
m_{j,a}(t)=\int \rho_{j,a,t}(y)\,dy.
\tag{2.2}
\]

Whenever `m_{j,a}(t)>0`, define

\[
\gamma_{j,a,t}(w)
=\frac1{m_{j,a}(t)}
\int f_j(w+y)\rho_{j,a,t}(y)\,dy.
\tag{2.3}
\]

Then, for every `t,j,a`,

\[
\boxed{\int\gamma_{j,a,t}=1,\qquad 0\le\gamma_{j,a,t}\le1.}
\tag{2.4}
\]

For a multi-label `alpha=(a_j)`, set

\[
m_\alpha(t)=\prod_jm_{j,a_j}(t),
\qquad
\Gamma_{\alpha,t}(w)=\prod_j\gamma_{j,a_j,t}(w_j).
\tag{2.5}
\]

Then

\[
\boxed{\sum_\alpha m_\alpha(t)=1}
\tag{2.6}
\]

for every `t`, and every `Gamma_{alpha,t}` is an admissible product probability density with each coordinate cap at most one.

Consequently, suppose a post-decoupling receiver is uniform over all product cap-one difference laws and over all values of an outside environment and its induced affine parameters. Then **any finite/countable/soft copied-side localization whose cells depend measurably on that environment preserves the receiver constant exactly**. No infimum of the fragment masses is needed.

### Proof

Fix `t,j,a`. The completed account02/B14 theorem applies to the subdensity `rho_{j,a,t}`. Directly,

\[
0\le \int f_j(w+y)\rho_{j,a,t}(y)\,dy
\le \int\rho_{j,a,t}=m_{j,a}(t),
\]

because `f_j<=1`; Tonelli gives total mass `m_{j,a}(t)`. This proves (2.4). From (2.1),

\[
\sum_a m_{j,a}(t)=\int f_j(y)\sum_a\theta_{j,a}(t,y)dy=1,
\]

and therefore (2.6) follows by multiplying the coordinate sums. The conditional copied variables still factor coordinatewise because the soft partition itself has the product form (2.1) coordinate by coordinate. Hence the difference law on a cell is exactly (2.5).

If `R(t,alpha;nu)` is any nonnegative receiver functional satisfying

\[
R(t,\alpha;\nu)\le C
\tag{2.7}
\]

for every `t,alpha` and every product cap-one probability law `nu`, then

\[
\sum_\alpha m_\alpha(t)
R(t,\alpha;\Gamma_{\alpha,t})
\le C\sum_\alpha m_\alpha(t)=C.
\tag{2.8}
\]

Integrating (2.8) over the arbitrary law of `T` preserves `C`. This is the exact zero-tax statement. Notice that no normalization parameter survives because the mass extraction happens after convolution with the undecomposed copy.

The product-form label restriction is essential to this proof: a genuinely joint label depending simultaneously on several copied coordinates need not leave a product conditional difference law. No claim is made for such joint labels.

## 3. Moving-fragment corollary

For arbitrary measurable functions `s_j(t)`, take the deterministic moving partition

\[
E_{j,k}(t)=[s_j(t)+k,s_j(t)+k+1),\qquad k\in\mathbb Z,
\tag{3.1}
\]

and `theta_{j,k}(t,y)=1_{E_{j,k}(t)}(y)`. The shifts `s_j(T)` may be unbounded and may have no finite moment. Fragment masses may be arbitrarily small or zero and can vary wildly with `t`. Nevertheless every nonzero conditional difference density (2.3) remains cap one, and every receiver covered by the theorem keeps exactly its unsplit constant.

The same statement holds for arbitrary measurable countable partitions instead of the unit cells in (3.1), including remote disconnected teeth and soft randomized partitions.

Thus an outside coordinate may decide **where** the copied variable is spatially localized without introducing a support-radius, tail, translation, or fragment-mass tax, provided localization is postponed until after the legal independent-copy decoupling.

## 4. Actual target-valid quadratic inequality

Let `I` consist of six original coordinates and `J` of three. Define

\[
M=\frac1{\sqrt2}
\begin{pmatrix}
1&0&0\\
1&0&0\\
0&1&0\\
0&1&0\\
0&0&1\\
0&0&1
\end{pmatrix}.
\tag{4.1}
\]

Let `T` be an arbitrary additional bank of original independent cap-one coordinates. For arbitrary real matrices `C,E` and arbitrary symmetric `D`, consider the full symmetric quadratic matrix

\[
A=
\begin{pmatrix}
0&M&C\\
M^T&0&E\\
C^T&E^T&D
\end{pmatrix}.
\tag{4.2}
\]

The `9x9` active principal block

\[
B=\begin{pmatrix}0&M\\M^T&0\end{pmatrix}
\]

has spectrum

\[
\{-1,-1,-1,0,0,0,1,1,1\},
\tag{4.3}
\]

because `M^TM=I_3`. Hence by Cauchy interlacing every ambient matrix (4.2) has at least three eigenvalues `>=1` and at least three `<=-1`. This is a genuine indefinite/off-diagonal instance of the exact owner target, for completely arbitrary ambient couplings `C,E,D`.

Condition on `T=t`. The active quadratic form is

\[
Q_t=2X_I^TMX_J+2X_I^TCt+2X_J^TEt+t^TDt.
\tag{4.4}
\]

There are exactly eight nonzero `3x3` row minors of `M`, each with squared determinant `1/8`; every row belongs to four, so every volume-sampling row marginal is exactly `1/2`. Also

\[
Z=e_3(M^TM)=1.
\]

Therefore the completed fixed-source theorem D gives, uniformly in the arbitrary affine terms generated by `t`,

\[
\boxed{\|p_{Q\mid T=t}\|_\infty\le6\sqrt e.}
\tag{4.5}
\]

Averaging over the arbitrary outside product law yields

\[
\boxed{\|p_Q\|_\infty\le6\sqrt e
=9.89232762420077\ldots .}
\tag{4.6}
\]

No moment or support assumption on the outside coordinates is used.

Now apply the completed account02/B14 one-copy difference theorem inside the decoupling proof of (4.5). For each realized outside value `t`, localize only the copied `J` variables according to any environment-dependent system (2.1), including the moving remote cells (3.1). On every nonzero label cell, the partner theorem gives the product cap-one difference law (2.5), while the matrix `M`, `Z=1`, and all volume marginals stay unchanged. Theorem D therefore supplies the same decoupled majorant on every cell. Equation (2.8) then returns exactly (4.5), and integrating `t` returns exactly (4.6).

This is an actual application of the completed designated-partner result to a full quadratic-form inequality: **outside-dependent moving localization of the duplicated bank costs zero, even with arbitrary ambient curvature/couplings and no tail or moment control.**

## 5. Why fragment-first conditioning is still the wrong order

For a static `N`-tooth marginal on a `J` coordinate, conditioning the original coordinate on a tooth first raises its normalized cap to `N`; rescaling to cap one reduces the corresponding cross coefficient by `1/N`, so the source volume certificate loses a factor `N`. The completed account02/B14 report makes this quantitative and gives an infinite fragment-first certificate for a suitable countable remote comb.

The theorem above shows that even if the teeth themselves move as arbitrary functions of the outside environment, that loss is completely absent after decoupling: the undecomposed copy supplies the missing mass factor pointwise in the environment. Thus the safe proof order is

\[
\text{condition outside environment}
\to\text{decouple the designated bank}
\to\text{localize only the copied difference side}
\to\text{extract true mass}
\to\text{pay BL/HY receiver}.
\]

It is not

\[
\text{localize original active variable}
\to\text{normalize tiny fragment}
\to\text{pay reciprocal curvature}.
\]

## 6. Scope and remaining implication

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The new theorem pays a localization issue only **after** a suitable decoupled receiver has been exposed.

It does not prove that bare `s_3(A)>=1` always yields a Theorem-D/D'/D5/projected-crossing receiver with universal matrix parameters. It also does not permit a label that jointly couples several copied coordinates, nor a label depending on the undecomposed active copy in a way that destroys product provenance.

The remaining B14 structural implication is therefore:

`QFORM-ROUTE-ROUGH-LOCALIZATION-TO-DIFFERENCE-SIDE-OR-WHOLELAW-EXIT-v1` — from the bare spectral hypothesis, arrange every necessary rough spatial localization either on one duplicated difference-side copy of an already-exposed product receiver, where the present theorem makes it zero-tax, or keep the corresponding active law whole and enter another completed whole-law ridge/hub/grouped-bank/physical receiver.

This is a structural decomposition problem, not a remaining tail/moment/translation estimate.

## 7. Integrity / source scope

Fresh owner control was re-resolved before publication; the latest protected controls still require exclusive full-QFORM work and contain no later B14 stop. The live correction set forbidding law-uniform pointwise oscillatory decay, bounded-diameter localization, fixed fragment-count localization, post-rotation independence, and false arbitrary-joint coarea arguments was retained.

Completed designated partner actually applied: `yspennstate/math-open-problems@388f936ef5954b951203df7bab568a64e0afe985`, account02/B14 `QFORM-ONE-COPY-DIFFERENCE-LOCALIZATION-v1`.

Fixed-source receiver actually applied: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, theorem D in the decoupling/Brascamp-Lieb report.

Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository reads and writes occurred, but no genuine native learned-memory receiver use was established. No schedule, task identity, enabled/quiet state, notification, email/push, cross-account authentication, paid/remote call, public release, or permission state was changed.

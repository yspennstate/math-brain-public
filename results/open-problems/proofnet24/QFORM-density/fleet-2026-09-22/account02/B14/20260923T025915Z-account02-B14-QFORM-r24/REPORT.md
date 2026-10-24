# account02/B14 r24 — overlap-mass-preserving localization and a D_k conditioning-order barrier

Programme: QFORM-DENSITY-3EIG-20260922. Role: translations and localization / complementary constructions and source-valid counterexamples. Status: NEW SUPPORTING LOCALIZATION THEOREM + TARGET-VALID PROOF-MECHANISM BARRIER; FULL QFORM REMAINS OPEN. Continuity is separate.

## Source pins actually used

1. Latest control observed before publication: `yspennstate/math-research-brain@81fcbfd6e199ab32f5feee75e6f9646f34bd7b52`, OWNER CONTROL revision `2026-09-22.15`; QFORM is the sole research target and no account02/B14 stop was present.
2. Required newest-Claude source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. I use its proved D_k theorem, in particular the no-marginal-condition k>=5 branch.
3. Assigned partner account03/B14 r24: `yspennstate/math-open-problems@2fe2734d7fc9a7e9a29edd26cbeda837fee10900`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T023535Z-account03-B14-QFORM-r24/REPORT.md`, together with its overlap calculation at `9f7efc2c599ca92ad63e2f55a526498132d8604b`. I use the exact conjugate-fiber cap and overlap-power formula.
4. Previous account02/B14 simultaneous affine-envelope localization: `yspennstate/math-open-problems@ae5a1d83e5434d0c318a53da7095cebe8ec6f17e`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T015809Z-account02-B14-QFORM-r23/REPORT.md`.

No arbitrary-joint coarea, post-rotation independence, bounded-diameter localization, fixed fragment count, moment bound, or small-output-law perturbation premise is used.

## 1. First unpaid implication: preserve a full overlap power before reciprocal curvature payment

A recurring surviving proof pattern introduces conjugate variables

\[
U=X-X',\qquad V=X+X'
\]

and then conditions on U. For cap-one fragmented product laws the conditional density cap of V can be arbitrarily large. The partner calculation shows that for iid uniform X,X' on a unit-measure set E,

\[
m_E(u)=|E\cap(E-u)|
\]

is the density of U and, for m_E(u)>0,

\[
\|f_{V\mid U=u}\|_\infty=\frac1{2m_E(u)}. \tag{1}
\]

Thus any local certificate homogeneous in a positive power of the normalized conditional cap consumes a negative power of the overlap m_E. The question is exactly how much overlap mass must remain before averaging.

### Proposition 1 (overlap-power localization compiler)

Let `(S,du)` be a parameter space and let `nu_u` be finite positive measures of total mass `w(u)` with

\[
0\le w(u)\le1,\qquad \int w(u)\,du=1,
\]

such that `nu=\int nu_u du`. If for every interval J and almost every u,

\[
\nu_u\{P_u\in J\}\le C\,w(u)^\gamma |J| \tag{2}
\]

with \(\gamma\ge1\), then

\[
\nu\{P\in J\}\le C|J|. \tag{3}
\]

**Proof.** Integrate (2). Since `0<=w<=1` and `gamma>=1`, `w^gamma<=w`, hence

\[
\nu\{P\in J\}\le C|J|\int w^\gamma\le C|J|\int w=C|J|.
\]

This is exact, uses no support information, and is unchanged by arbitrary translations of the fibers. ∎

The exponent one is sharp for unrestricted fragmented conjugate fibers. For

\[
E_N=\bigcup_{j=1}^N[4^j,4^j+N^{-1}],
\]

the partner proves for every \(\gamma>-1\)

\[
\int m_N(u)^\gamma du
=\frac{2}{\gamma+1}
\left[(1-N^{-1})N^{1-\gamma}+N^{-1}\right]. \tag{4}
\]

Hence `sup_N int m_N^gamma=infinity` whenever `0<=gamma<1`, whereas `int m_E^gamma<=1` for every unit set E once `gamma>=1`. So one full overlap power is not a technical convenience: it is the exact fragment-uniform threshold for this conditioning variable.

## 2. Simultaneous variable-cap localization

The assigned partner's variable-cap theorem and the previous B14 simultaneous-supremum argument combine without loss.

### Theorem 2 (simultaneous variable-cap affine localization)

Fix positive caps \(M_1,\ldots,M_n\). Let `D(M)` be the product laws whose i-th marginal density is at most \(M_i\). Let `F(M)` be the product laws with i-th density

\[
M_i\mathbf 1_{E_i},\qquad |E_i|=M_i^{-1},
\]

where each \(E_i\) is a compact finite union of intervals. Let \(\Theta\) be an arbitrary index set, \(P_\theta\) arbitrary measurable real-valued maps, and \(\Phi_\theta\) convex TV-lower-semicontinuous extended functionals of output laws. Then

\[
\boxed{
\sup_{\mu\in D(M)}\sup_{\theta\in\Theta}
\Phi_\theta((P_\theta)_\#\mu)
=
\sup_{\nu\in F(M)}\sup_{\theta\in\Theta}
\Phi_\theta((P_\theta)_\#\nu).
} \tag{5}
\]

**Proof.** The partner r24 theorem gives finite-convex-mixture TV approximation of every law in `D(M)` by laws in `F(M)`, after the coordinate scaling `Y_i=M_i X_i`. The functional

\[
\mu\mapsto\sup_\theta\Phi_\theta((P_\theta)_\#\mu)
\]

is again convex and TV-lower-semicontinuous, because arbitrary suprema preserve both properties. Applying the partner approximation to this single envelope gives (5). ∎

For quadratic families and all affine coefficients at once, coordinate scaling with `D=diag(M_i)` sends

\[
A\mapsto D^{-1}AD^{-1},\qquad b\mapsto D^{-1}b,
\]

and does not introduce a support radius, moment, fragment-number, fragment-separation, or translation penalty. This theorem legitimizes variable-cap localization itself. What it does **not** legitimize is applying a cap-homogeneous certificate separately on normalized thin fibers and then averaging; the next theorem shows the distinction sharply.

## 3. A target-valid D_k conditioning-order barrier for every k>=5

Claude's proved D_k theorem says the following. For an original-coordinate cross block `M=A_IJ`, put

\[
Z_k=e_k(M^TM).
\]

For \(k\ge5\), choosing q=2 in the general D_k estimate requires no row-marginal hypothesis and gives

\[
\boxed{
\|p_Q\|_\infty
\le C_k Z_k^{-1/(2k)},\qquad
C_k=\sqrt{2e}\,\frac{k}{k-4}.
} \tag{6}
\]

All self blocks, outside couplings and affine terms are allowed. For k=5 this is `5 sqrt(2e) Z_5^{-1/10}`.

I now apply (6) to a fully target-valid family and compare two proof orders.

Take `2k` independent pairs `(X_i,X_i')`, with every variable uniform on the same `E_N` above, and set

\[
U_i=X_i-X_i',\qquad V_i=X_i+X_i'.
\]

The variables \(V_1,\ldots,V_{2k}\) are independent. Their densities satisfy

\[
p_{V_i}(v)=\int 1_{E_N}(x)1_{E_N}(v-x)\,dx\le |E_N|=1. \tag{7}
\]

Consider

\[
Q_k(V)=2\sum_{i=1}^k V_iV_{k+i}. \tag{8}
\]

Its symmetric matrix is

\[
A_k=\begin{pmatrix}0&I_k\\ I_k&0\end{pmatrix},
\]

whose spectrum is \(+1\) with multiplicity k and \(-1\) with multiplicity k. Thus (8) is inside the exact QFORM target for every k>=5. The physical cross block is `I_k`, so `Z_k=1`; direct application of Claude's theorem gives

\[
\boxed{\|p_{Q_k}\|_\infty\le C_k.} \tag{9}
\]

This bound is independent of N.

Now reverse the order: condition first on all differences \(U_i=u_i\), normalize each sum fiber, rescale to cap one, and only then invoke D_k.

Write \(m_i=m_N(u_i)\). By (1), conditional on `U_i=u_i`, the variable `V_i` has cap

\[
M_i=(2m_i)^{-1}. \tag{10}
\]

Set \(Y_i=M_iV_i\). Then every conditional `Y_i` has density cap at most one, but (8) becomes a cross form whose k-by-k cross block is diagonal with entries

\[
(M_iM_{k+i})^{-1}=4m_im_{k+i}. \tag{11}
\]

Since this block has exactly k singular values,

\[
Z_k(u)=\det(M(u))^2
=4^{2k}\prod_{i=1}^{2k}m_i^2. \tag{12}
\]

Therefore the conditional D_k certificate is

\[
\|p_{Q_k\mid U=u}\|_\infty
\le \frac{C_k}{4}\prod_{i=1}^{2k}m_i^{-1/k}. \tag{13}
\]

The joint density of the differences is exactly \(\prod_i m_i\). Averaging (13) therefore gives the proof bound

\[
\frac{C_k}{4}
\left(\int m_N(u)^{1-1/k}\,du\right)^{2k}. \tag{14}
\]

By (4), with \(\gamma=1-1/k\),

\[
\int m_N^{1-1/k}
=
\frac{2k}{2k-1}
\left[(1-N^{-1})N^{1/k}+N^{-1}\right]. \tag{15}
\]

Consequently the normalized-fiber-then-D_k certificate equals

\[
\boxed{
\frac{C_k}{4}
\left\{
\frac{2k}{2k-1}
\left[(1-N^{-1})N^{1/k}+N^{-1}\right]
\right\}^{2k},
} \tag{16}
\]

which grows as

\[
\frac{C_k}{4}
\left(\frac{2k}{2k-1}\right)^{2k}N^2. \tag{17}
\]

For k=5, this specializes to

\[
\frac{5\sqrt{2e}}4
\left\{\frac{10}{9}\left[(1-N^{-1})N^{1/5}+N^{-1}\right]\right\}^{10}. \tag{18}
\]

### Conclusion of the barrier

The same target-valid family has the dimension-free direct bound (9), yet the proof order

`condition on differences -> normalize thin sum fibers -> rescale -> pay reciprocal D_k volume -> average`

loses exactly order \(N^2\) for every fixed k>=5. Increasing the exterior-volume order does not cure the fragmentation loss. This does **not** refute D_k and does **not** refute QFORM. It refutes a localization/compiler ordering that first normalizes conjugate fibers and then applies any such reciprocal cross-volume certificate.

The algebra also explains the loss through Proposition 1. In each of the `2k` difference variables, the normalized D_k payment converts the conditioning weight \(m_i\) into

\[
m_i^{1-1/k},
\]

which is below the sharp safe overlap exponent one. The product of `2k` such deficits accumulates to the universal \(N^2\) failure in (17). By contrast, Claude's decoupling theorem integrates the original difference law **before** reciprocal volume inversion and retains the correct aggregate mass.

## 4. Translation and unbounded-support implications

Nothing above uses bounded support diameter. In fact the witness deliberately places legal fragments at locations \(4^j\), so separation grows rapidly. Translating any individual original marginal leaves every density cap unchanged and merely translates the relevant sum/difference fibers. Equations (1)-(17) depend only on overlap masses, not on absolute locations. Thus remote fragments and conditioning-generated affine terms cannot be repaired by recentering individual normalized fibers; the correct invariant is unnormalized mass retained through the smoothing/aggregation step.

Together with the previous B14 range-affine quotient, the full localization interface is now:

1. Localize the **whole** product law, or a whole variable-cap product law, by the convex-mixture theorem before choosing affine/small-ball parameters.
2. Range-compatible affine terms of an active quadratic block are removable by translation at the worst-law level; only kernel leakage is genuine.
3. If a sum/difference or other disintegration is introduced inside the proof, keep its unnormalized piece mass through reciprocal curvature/volume payment. A full power of each independent overlap mass is the fragment-uniform threshold in the conjugate model.
4. Do not infer that a correct cap-one certificate remains uniform after normalize-thin-fibers-then-average; (16) gives a target-valid exact obstruction even for the strongest no-marginal D_k branch.

## 5. First remaining implication

`QFORM-UNNORMALIZED-DECOUPLING-OR-KERNEL-LEAKAGE-v1`:

For every surviving no-pivot/heavy-star configuration under `s_3(A)>=1`, obtain one of the existing volume/ridge/bank exits **before** normalized fiber conditioning, or expose an original-coordinate active core whose genuine kernel-leakage envelope can be averaged against the unnormalized outside law while retaining at least one full overlap/mass power for every independently introduced conditioning variable. Equivalently, a successful positive-copy or decoupling compiler must keep overlap weights inside the Brascamp-Lieb/curved kernel until after reciprocal inversion.

This is an actual narrowing of the localization step: `D_k` itself is not the missing inequality on the witness family; the missing operation is an unnormalized aggregate theorem for the heavy-star/no-pivot branches where direct D/D'/D_k is not yet structurally available.

Full QFORM remains OPEN. No continuity claim is made for the unrestricted target.

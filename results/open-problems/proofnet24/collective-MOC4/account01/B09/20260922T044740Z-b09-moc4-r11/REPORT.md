# MOC4 account01/B09 — exact complex-Hadamard fiber lift and P-only obstruction

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira scope  
**Worker/run:** account01/B09, `20260922T044740Z-b09-moc4-r11`  
**Assignment:** construct genuine unitary/spectrum adversaries to proposed coefficient representations; coefficient failure alone is not a target counterexample  
**Candidate:** `MOC4-HADAMARD-FIBER-LIFT-v1`  
**Outcome:** `AUXILIARY_ONLY`; `MOC4-P-ONLY-FULL-LIFT-v1` is exactly refuted, while the parent MOC4 target remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact team state consumed

The source-exact target is: for every complex normal `4 x 4` pair, after diagonalizing one matrix and writing the relative eigenbasis as a true unitary `U`, prove for every real-linear support direction

\[
\Re\!\left(\eta\det(D_a+UD_bU^*)\right)
\le \max_{\sigma\in S_4}\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right).
\]

This run read the current lead account03/B07 candidate `MOC4-V4-PAIR-GAP-CEILING-v1`. With endpoint supports `H_sigma`, mean `m`, `M=max H_sigma`, `d=M-m`, best Klein-four fiber average `Q`, `Delta=M-Q`, and six pair gaps summing to `G`, it proves every genuine support violation `h(U)=M+gamma` satisfies

\[
0<\gamma\le {3d-\Delta-G/2\over4},
\]

and leaves a positive-reserve common-unitary `P/R/D` compatibility problem.

The assigned OTHER-account partner result used directly is account02/B07 `MOC4-ONE-CYCLE-NORMAL-CONE-v1`. For its genuine closing `SU(2)` orbit, the determinant is an affine filled ellipse and directional safety is exactly the payment inequality `C^2<=delta_0 delta_1`; it reduces the continuum of support directions to finitely many exact `2 x 2` copositivity checks and gives two rank-two chord identities. This run supplies a different exact phase fiber on which the full common-permutation lift can actually be written down, furnishing a calibration family for those phase-sensitive searches.

I also consume account04/B09 `MOC4-STANDARD-CHANNEL-CEILING-v1`. If `k(U)` is the lead's standard/oriented channel, `K_std` is the maximum endpoint standard-channel value, and `P=|U|^2`, then

\[
k(U)\le K_{\rm std},\qquad \gamma\le K_{\rm std}-\Delta,
\]

with `D=(1/4)E^TPE`. The corollary in Section 5 below applies this theorem to the minimum entry of the same unistochastic matrix.

## 2. A genuine one-parameter unitary phase fiber

For `|z|=1`, put

\[
U(z)={1\over2}
\begin{pmatrix}
1&1&1&1\\
1&z&-1&-z\\
1&-1&1&-1\\
1&-z&-1&z
\end{pmatrix},
\qquad c=\Re z\in[-1,1].
\tag{1}
\]

This is a true unitary for every phase `z`, and

\[
P(z)=\bigl(|u_{ij}(z)|^2\bigr)={1\over4}J
\tag{2}
\]

is independent of `z`. Thus this is an exact test of how much determinant information survives after discarding compound-minor phase data and retaining only the level-one unistochastic matrix.

Let `C_1={12,34}`, `C_2={13,24}`, `C_3={14,23}` be the three complementary-pair classes. Let

\[
\pi:S_4\to S_3
\]

be the quotient action on these classes. Define a probability law `mu_c` on `S_4` by

\[
\mu_c(\sigma)=
\begin{cases}
(1-c)/16,&\pi(\sigma)\in\{(12),(23)\},\\
(1+c)/16,&\pi(\sigma)\in\{(123),(132)\},\\
0,&\pi(\sigma)\in\{e,(13)\}.
\end{cases}
\tag{3}
\]

Every quotient fiber has four permutations, so the weights in (3) are nonnegative for `c in [-1,1]` and sum to one.

The corresponding complementary-pair transport is

\[
R(c)=
\begin{pmatrix}
(1-c)/4&1/2&(1+c)/4\\
1/2&0&1/2\\
(1+c)/4&1/2&(1-c)/4
\end{pmatrix}.
\tag{4}
\]

Equivalently, in the `S_3` quotient,

\[
R(c)={1-c\over4}\bigl(P_{(12)}+P_{(23)}\bigr)
+{1+c\over4}\bigl(P_{(123)}+P_{(132)}\bigr).
\tag{5}
\]

So the flat level-one matrix `P=J/4` does **not** freeze the middle compound channel: `R(c)` moves linearly with the unitary phase.

## 3. Theorem — `MOC4-HADAMARD-FIBER-LIFT-v1`

For every `|z|=1`, every complex spectra `a=(a_1,...,a_4)` and `b=(b_1,...,b_4)`, and `c=Re z`,

\[
\boxed{
\det(D_a+U(z)D_bU(z)^*)
=\sum_{\sigma\in S_4}\mu_c(\sigma)
\prod_{i=1}^4(a_i+b_{\sigma(i)}).
}
\tag{6}
\]

In particular the MOC4 inclusion holds for this entire genuine complex-Hadamard phase family, for arbitrary complex spectra, including repeated spectra and singular sums.

### Proof

For a true unitary `U`, Cauchy--Binet gives

\[
\det(D_a+UD_bU^*)
=\sum_{S,T\subseteq[4],\ |S|=|T|}
 a_{S^c}b_T\,|\det U[S,T]|^2.
\tag{7}
\]

On the other hand, for any probability law `mu` on `S_4`,

\[
\sum_\sigma\mu(\sigma)\prod_i(a_i+b_{\sigma(i)})
=\sum_{S,T}a_{S^c}b_T\,
\Pr_{\sigma\sim\mu}[\sigma(S)=T].
\tag{8}
\]

Thus it suffices to match every compound-minor coefficient.

For `mu_c` in (3), exact symbolic calculation gives for every singleton `i,j`

\[
\Pr[\sigma(i)=j]=1/4=|u_{ij}(z)|^2,
\tag{9}
\]

and for every pair of two-subsets `S,T`

\[
\Pr[\sigma(S)=T]=|\det U(z)[S,T]|^2.
\tag{10}
\]

The `k=3` coefficients follow from (9) by taking complements, while `k=0,4` are trivial. Substituting (9)--(10) into (7)--(8) proves (6). The committed verifier checks the 16 singleton identities, all 36 two-subset identities, and the full symbolic determinant identity with arbitrary spectral indeterminates. No floating-point sign or sampling argument is used. `QED`

A useful fiber-average form of (6) is obtained by setting

\[
B_\rho={1\over4}\sum_{\pi(\sigma)=\rho}z_\sigma,
\qquad z_\sigma=\prod_i(a_i+b_{\sigma(i)}).
\]

Then

\[
\boxed{
\det(D_a+U(z)D_bU(z)^*)
={1-c\over4}(B_{(12)}+B_{(23)})
+{1+c\over4}(B_{(123)}+B_{(132)}).
}
\tag{11}
\]

This is a source-valid positive coefficient representation, not an arbitrary bistochastic surrogate.

## 4. Exact adversary: a P-only full coefficient rule cannot work

Equation (2) means every unitary in the family has exactly the same `P=|U|^2=J/4`. Nevertheless the determinant generally changes with `z`.

Take the fixed simple complex spectra

\[
a=(-4+4i,-i,-3+2i,-4-4i),
\]
\[
b=(-4-4i,2-i,2-4i,4-i).
\tag{12}
\]

All 24 endpoint products are distinct. Exact arithmetic gives

\[
D(c):=\det(D_a+U(z)D_bU(z)^*)
=-209+{521\over4}i
+c\left(15-{15\over2}i\right).
\tag{13}
\]

In particular,

\[
D(1)=-194+{491\over4}i,
\qquad
D(i)=-209+{521\over4}i,
\tag{14}
\]

although both unitaries have the identical `P=J/4`.

Therefore the following stronger proposed mechanism is false:

> **`MOC4-P-ONLY-FULL-LIFT-v1` — REFUTED.** There is no rule assigning convex endpoint weights from only `(P,a,b)` that represents the determinant for every true unitary with that `P`.

Indeed such a rule would assign the same endpoint combination to `U(1)` and `U(i)`, contradicting (14). This is a genuine true-unitary/spectrum obstruction, rather than a negative formal coefficient in a relaxed model.

It is emphatically **not** a counterexample to MOC4. In fact Section 3 gives a positive lift `mu_c`. For the spectra (12), the entire segment (13), `-1<=c<=1`, lies strictly inside the triangle of target vertices

\[
V_0=80-240i,\qquad V_1=64+256i,\qquad V_2=-280+120i.
\]

The exact barycentric weights are

\[
w_0(c)={613+462c\over17280},\qquad
w_1(c)={65+6c\over384},\qquad
w_2(c)={6871-366c\over8640},
\tag{15}
\]

which sum to one, reproduce `D(c)`, and are strictly positive at both endpoints `c=+-1`, hence throughout the interval.

This is the main adversarial lesson of the run: **level-one unistochastic data can be completely phase-blind even while the correct positive endpoint coefficients move nontrivially through the level-two compound channel.** Any surviving coefficient proof must retain more than `P`, exactly as the campaign's `P/R/D` compatibility architecture requires.

## 5. Unconditional flat-escape corollary from the OTHER-account standard-channel theorem

The account04/B09 standard-channel theorem can be sharpened into a simple necessary geometric condition on any residual violator.

Let

\[
p_*:=\min_{i,j}P_{ij},\qquad P=|U|^2.
\]

Since `P` is doubly stochastic, `0<=p_*<=1/4`, and when `p_*<1/4`

\[
P=p_*J+(1-4p_*)P',
\tag{16}
\]

where `P'` is again doubly stochastic. Because `E^TJE=0`, the standard channel has no uniform component. Applying `MOC4-STANDARD-CHANNEL-CEILING-v1` to `P'` gives

\[
\boxed{k(U)\le(1-4p_*)K_{\rm std}.}
\tag{17}
\]

If a genuine support violation of size `gamma>0` exists, the lead's V4 roof gives `k(U)>=gamma+Delta`. Thus, if `K_std>0`,

\[
\boxed{
p_*\le{K_{\rm std}-\Delta-\gamma\over4K_{\rm std}}
<{K_{\rm std}-\Delta\over4K_{\rm std}}.}
\tag{18}
\]

If `K_std=0`, then `Delta=0` and a positive violation is already impossible. In particular every flat complex-Hadamard point `P=J/4` is automatically outside the residual violating branch, consistent with the explicit lift above.

This does not close the positive-reserve core, but it adds an exact, source-valid **escape-from-flatness** requirement on every possible counterexample/maximizer. It uses the same true `P` as the common-unitary exterior-square data and does not assume a full positive lift.

## 6. Compact conditional end-to-end chain after this run

A surviving proof route is now:

1. Separate a hypothetical MOC4 failure by a real support direction and choose a global true-unitary maximizer.
2. Apply the campaign's source-valid repeated-spectrum/common-block/boundary reductions rather than discard singular or degenerate cases.
3. Apply the lead's `V4` fiber roof and pair-gap ceiling, together with the bidirectional refinement already in the team state; a residual violator must lie on a strictly positive reserve branch.
4. Apply `MOC4-STANDARD-CHANNEL-CEILING-v1`. If `K_std=Delta`, the direction closes. Otherwise (18) forces the maximizing unistochastic matrix away from the flat center by an explicit amount.
5. On that nonflat residual, impose the existing exact same-unitary identities `D=(1/4)E^TPE`, `R>=|D|`, the odd-Weyl/twist constraints, row/column bi-Rayleigh and bi-orientation maximizer gates, Cartan/Hessian conditions, and the structured spectral support normal.
6. Exclude this remaining feasible set, or produce a true unitary/spectral witness with positive support gap. Then every support direction is safe and MOC4 follows; a genuine witness would disprove MOC4.

The first essential unpaid implication remains the team's positive-reserve common-unitary residual, now with the additional exact necessary condition (18). The present phase family does not solve that implication: it identifies a large, genuinely complex phase direction that is **provably safe** and proves that `P` alone cannot encode the required endpoint weights.

## 7. Verification, status, and non-claims

The committed verifier performs exact symbolic algebra for arbitrary spectral variables and exact finite checks for the concrete simple-complex datum. Captured output begins

```text
PASS MOC4-HADAMARD-FIBER-LIFT-v1
universal_symbolic_identity = PASS
level1_and_level2_common_permutation_marginals = PASS
```

and records the exact values in (14)--(15).

Status:
- `MOC4-HADAMARD-FIBER-LIFT-v1`: **PROVED** for every `|z|=1` and arbitrary complex spectra.
- `MOC4-P-ONLY-FULL-LIFT-v1`: **REFUTED** by the true-unitary/simple-spectrum pair (12)--(14).
- Flat-escape inequality (18): **PROVED** as a corollary of the consumed OTHER-account standard-channel theorem.
- Parent MOC4: **OPEN**.
- Honest run label: **`AUXILIARY_ONLY`**.

No benchmark material or held-out answers, credentials, scheduler identifiers, machine-local paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex call, remote workflow, permission change, or notification enabling was used.

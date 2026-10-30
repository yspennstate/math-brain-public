# fleet02/B15 — suspension pullback of the influence I-projection and an exact no-loss KL obstruction

**Run:** `20260922T085941Z-fleet02-B15-r16a`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_KL_NO_LOSS_OBSTRUCTION`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Current candidate, before/after, and the first missing Shannon implication

Fresh owner control keeps B12--B18 on full FEI and requires Campaign B to preserve and spend the negative information credits in the common all-gate residual. The newest complete B-lead source used here is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T075546Z-gibbs-price-bellman/REPORT.md`.

Its arbitrary-potential Gibbs identity remains valid even though its then-fixed `Gamma^dagger` seed was subsequently refuted. The compatible replacement construction consumed below is fleet03/B12's completed

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B12/20260922T074537Z-tilted-quartic-universal-repair/REPORT.md`,

which proves a universally gate-safe tilted-quartic direction and repairs the known biased 18-input prime witness, yielding the current proposed center

\[
C_*=\Gamma^*(1/2)=6.538805311222222\ldots.
\]

This report does **not** assume that `Gamma*` is universal; fleet03/B12 explicitly leaves that implication open.

The latest completed fleet02/B15 result before this run is

`20260922T0829Z-influence-iprojection-kl`.

For a nonempty biased spectral law \(P=w^+\), with exact original-coordinate occurrence marginals
\[
r_i=P(i\in S)=\operatorname{It}_i(G;p)/V_{p_{\rm out}},
\]
it constructs the unique maximum-entropy conditional-product law \(Q_r\) with those marginals and proves
\[
K_{\rm occ}:=D_{\rm KL,2}(P\|Q_r)=H_{\max}(r)-H(P),
\]
together with the exact Pythagorean decomposition of **every** conditional-product Gibbs KL. For an arbitrary symmetric potential \(\Gamma\), the normalized all-gate residual is
\[
R_\Gamma
=
B_{\rm inf}^{\Gamma}+K_{\rm occ},
\qquad
B_{\rm inf}^{\Gamma}
=
\sum_i r_i a_i-a_q-H_{\max}(r).
\tag{0.1}
\]
Thus the first missing Shannon implication is
\[
\boxed{
K_{\rm occ}(G;p)
\ge
\left[
H_{\max}(r)+a_q-\sum_i r_i a_i
\right]_+
}
\tag{0.2}
\]
on every source for a proposed universal potential.

The last three completed substantive fleet02/B15 mechanisms before this run were:

1. `20260922T060159Z-bent-nearisoclinic-sector-obstruction`: local high-posterior information payment was destroyed by a genuine Boolean near-isoclinic bent carrier; child/global slack was shown necessary.
2. `20260922T0704Z-gibbs-kl-prime-tube`: the exact all-gate Gibbs KL factorization and packet/original-coordinate price statistic were derived. Its fixed `Gamma^dagger` seed is now globally refuted, but the identity is potential-independent.
3. `20260922T0829Z-influence-iprojection-kl`: every original-coordinate first moment was paid exactly, leaving the canonical higher-order dependence credit \(K_{\rm occ}\).

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`; no finite universal FEI upper constant is proved.

**MECHANISM CHANGE:** `near-conditional-product corridor / first-moment I-projection -> exact codimension-one Boolean suspension pullback and asymptotic no-loss theorem for the surviving KL credit`.

This is not another renamed remainder. It determines exactly how much of (0.2) can be compressed on a genuine Boolean family and proves that any fixed fractional loss of the surviving negative KL is fatal, even after adding an arbitrary \(O(J)\) valuation bank.

The standing open-problems moves used substantively were #2 (attack the negation first), #7 (take the sparse-defect limit), and #11 (dualize through the exact I-projection).

## 1. Exact suspension theorem: the missing KL implication contains FEI isometrically

Let \(g:\{-1,1\}^m\to\{-1,1\}\) be any uniform Boolean function. Introduce one fresh unbiased bit \(y\), independent of \(x\), and define the balanced suspension
\[
F(y,x)=y\,g(x).
\tag{1.1}
\]

### Theorem 1.1 — suspension pullback of the complete I-projection residual

For every Boolean \(g\):

\[
\widehat F(\{y\}\cup T)=\widehat g(T),
\qquad
\widehat F(S)=0\quad(y\notin S).
\tag{1.2}
\]

Consequently
\[
H(F)=H(g),\qquad
\operatorname{Inf}_y(F)=1,\qquad
\operatorname{Inf}_i(F)=\operatorname{Inf}_i(g),
\qquad
I(F)=1+I(g).
\tag{1.3}
\]

Let \(P_F\) be the nonempty spectral law of \(F\) (it is the whole spectral law because \(F\) is balanced), and put
\[
j_i=\operatorname{Inf}_i(g).
\]
The I-projection \(Q_r\) from `20260922T0829Z-influence-iprojection-kl` is exactly
\[
Q_r(\{y\}\cup T)
=
\prod_{i\in T}j_i
\prod_{i\notin T}(1-j_i).
\tag{1.4}
\]
Therefore
\[
\boxed{
H_{\max}(r)=\sum_{i=1}^m h_2(j_i)
}
\tag{1.5}
\]
and
\[
\boxed{
K_{\rm occ}(F)
=
D_{\rm KL,2}\!\left(
\widehat g(\cdot)^2
\bigg\|
\bigotimes_{i=1}^m{\rm Bernoulli}(j_i)
\right)
=
\sum_i h_2(j_i)-H(g).
}
\tag{1.6}
\]

For any symmetric all-gate potential with center
\[
C=\Gamma(1/2)<\infty,
\]
the balanced-uniform residual is
\[
\boxed{
R_\Gamma(F;1/2^{m+1})
=
C\,I(g)-H(g).
}
\tag{1.7}
\]
Under the exact I-projection split,
\[
\boxed{
B_{\rm inf}^{\Gamma}(F)
=
C\,I(g)-\sum_i h_2(j_i),
}
\tag{1.8}
\]
and (1.7) is exactly (1.8) plus (1.6).

In particular, the first missing Shannon implication (0.2), restricted only to Boolean suspensions, is **exactly**
\[
\sum_i h_2(j_i)-H(g)
\ge
\sum_i h_2(j_i)-C I(g),
\]
i.e.
\[
\boxed{H(g)\le C I(g).}
\tag{1.9}
\]

So after every original-coordinate first moment has been optimally paid, the surviving dependence-KL problem still contains the original FEI target without loss on the codimension-one suspension face.

### Proof

Equation (1.2) follows by separating expectations:
\[
\mathbb E_{y,x}[y g(x)\chi_A(y)\chi_T(x)].
\]
The \(y\)-expectation vanishes unless \(A=\{y\}\), in which case it equals one. Squaring gives a measure-preserving bijection \(T\mapsto\{y\}\cup T\) between the spectral laws of \(g\) and \(F\), proving the entropy statement in (1.3). Flipping \(y\) always flips \(F\); flipping \(x_i\) flips \(F\) exactly when it flips \(g\), proving the influence statements.

For the I-projection, the occurrence marginals are
\[
r_y=1,\qquad r_i=j_i.
\]
If \(g\) is nonconstant then some \(j_i>0\). In the exact I-projection equation
\[
1-c=\prod_z(1-c r_z)
\]
the factor for \(y\) is \(1-c\). The unique positive solution is therefore \(c=1\): if \(c<1\), cancellation would force \(\prod_i(1-cj_i)=1\), impossible. Thus \(y\) is deterministic and the remaining coordinates are independent Bernoulli \(j_i\), proving (1.4)--(1.5). Because \(P_F\) and \(Q_r\) have the same coordinate marginals, the cross-entropy against the product law is \(\sum_i h_2(j_i)\), which gives (1.6).

At uniform input bias and balanced output, \(V=1\), \(h_2(V)=0\), and every input/output price is \(C\). The exact gate residual is therefore
\[
R_\Gamma=C(I(F)-1)-H(F).
\]
Apply (1.3) to obtain (1.7), then subtract (1.6) to obtain (1.8).

If \(g\) is constant, \(F=\pm y\) is a character, \(I(g)=H(g)=K_{\rm occ}=0\), and all displayed identities hold by the \(\mu=1\) endpoint of the I-projection theorem. QED.

### Consequence

A proof strategy that says only “small \(K_{\rm occ}\) forces the Boolean spectrum near its conditional-product I-projection, so stabilize the Poincare endpoint” has not reduced FEI by itself: on the suspension face the exact quantitative statement required to pay the residual is already FEI for the unsuspended source. Additional signed/source structure must be converted into an actual KL payment, not merely into another near-product description.

## 2. Sparse one-point defects force asymptotically exact use of the negative KL

The preceding theorem shows equivalence. The following genuine Boolean family gives a quantitative obstruction to **losing any fixed fraction** of \(K_{\rm occ}\).

Let
\[
\alpha=2^{-m},
\qquad
g_m(x)=1-2\,{\bf 1}_{\{x=0\}},
\qquad
F_m(y,x)=y\,g_m(x),
\tag{2.1}
\]
with \(m\ge2\).

For \(g_m\),
\[
\widehat g_m(\varnothing)=1-2\alpha,
\qquad
|\widehat g_m(T)|=2\alpha\quad(T\ne\varnothing),
\tag{2.2}
\]
and every coordinate has
\[
j_i=\operatorname{Inf}_i(g_m)=2\alpha.
\tag{2.3}
\]
Hence
\[
I(g_m)=2m\alpha.
\tag{2.4}
\]
The exact spectral entropy is
\[
\boxed{
H(g_m)
=
-(1-2\alpha)^2\log_2(1-2\alpha)^2
+
4\alpha(1-\alpha)(2m-2).
}
\tag{2.5}
\]
The suspension I-projection has
\[
\boxed{
H_{\max}(r)=m\,h_2(2\alpha),
\qquad
K_{\rm occ}(F_m)=m h_2(2\alpha)-H(g_m).
}
\tag{2.6}
\]

Using
\[
{h_2(x)\over x}
=
\log_2{1\over x}+{1\over\ln2}+o(1)
\quad(x\downarrow0),
\]
and (2.5),
\[
{H(g_m)\over I(g_m)}\longrightarrow4,
\tag{2.7}
\]
\[
\boxed{
{H_{\max}(r)\over I(g_m)}
=
m-1+{1\over\ln2}+o(1),
}
\tag{2.8}
\]
and
\[
\boxed{
{K_{\rm occ}(F_m)\over I(g_m)}
=
m-5+{1\over\ln2}+o(1).
}
\tag{2.9}
\]

For a finite center \(C\),
\[
{B_{\rm inf}^{C}(F_m)\over I(g_m)}
=
C-m+1-{1\over\ln2}+o(1),
\tag{2.10}
\]
while the **exact** sum satisfies
\[
{B_{\rm inf}^{C}+K_{\rm occ}\over I(g_m)}
=
C-{H(g_m)\over I(g_m)}
\longrightarrow C-4.
\tag{2.11}
\]

The negative dependence KL is therefore not a small correction: each of the two terms in (2.11) has magnitude \(\Theta(mI)\), and the finite FEI-scale remainder appears only after their nearly exact cancellation.

### Theorem 2.1 — no fixed fractional KL recovery plus an \(O(J)\) bank

Fix any finite \(C\), any finite \(L\), and any \(\theta<1\). Then for all sufficiently large \(m\),
\[
\boxed{
B_{\rm inf}^{C}(F_m)
+
\theta K_{\rm occ}(F_m)
+
L\,J(F_m)
<0.
}
\tag{2.12}
\]

Thus no proof can replace the surviving negative KL by a uniform fixed fraction \(\theta<1\) and repair the loss with any dimension-independent \(O(J)\) reserve.

### Proof

For \(m\ge2\), the new suspension coordinate has influence one and hence folded influence zero, while every old coordinate has folded influence \(2\alpha\). Thus
\[
J(F_m)=2m\alpha=I(g_m).
\tag{2.13}
\]
Using (2.7)--(2.8),
\[
\frac{
B_{\rm inf}^{C}+\theta K_{\rm occ}+LJ
}{I(g_m)}
=
C+L
-\theta\,{H(g_m)\over I(g_m)}
-(1-\theta)\,{H_{\max}(r)\over I(g_m)}.
\]
The right side equals
\[
C+L-4\theta
-(1-\theta)\left(m-1+{1\over\ln2}\right)+o(1),
\]
which tends to \(-\infty\). QED.

There is a stronger inherited arithmetic obstruction on this exact family. The signed magnitude packets of the one-point defect have valuation depth \(r_a=0\), as proved in the earlier B15 packet analysis. Therefore every valuation-depth tail is literally zero here. The valuation-tail majorization theorem is not merely too weak by a constant: there is no valuation-tail mass available to compensate a lossy dependence-KL step.

Equivalently, if a proposed source statistic \(Z_m\) recovers only
\[
\widetilde K_m
=
D_{\rm KL,2}\bigl((Z_m)_\#P\|\,(Z_m)_\#Q_r\bigr)
\le K_{\rm occ},
\]
then any fixed-center proof on this family with only an \(O(J)\) auxiliary bank must satisfy
\[
\boxed{
K_{\rm occ}(F_m)-\widetilde K_m=O(I(g_m)).
}
\tag{2.14}
\]
Since \(K_{\rm occ}/I\sim m\), this means the **relative** KL loss must be \(O(1/m)\), not a fixed percentage.

## 3. The hard zero-valuation family still has an exact one-dimensional information payment

The obstruction above does not say that the KL is intrinsically high-dimensional. On the one-point defect, it has an exact, source-natural sufficient statistic.

Under \(P=\widehat g_m^2\), all nonempty Fourier coefficients have the same magnitude. Therefore \(P\), conditional on the Fourier level
\[
K=|T|,
\]
is uniform over the \(\binom mk\) subsets of that level. The I-projection tail reference is the iid product law with success probability \(2\alpha\), which is also uniform conditional on \(K\). Hence the likelihood ratio \(P(T)/Q_r(T)\) depends only on \(K\), and
\[
\boxed{
K_{\rm occ}(F_m)
=
D_{\rm KL,2}\!\left(
\mathcal L_P(K)
\big\|
{\rm Binomial}(m,2\alpha)
\right).
}
\tag{3.1}
\]

So the entire \(\Theta(mI)\) cancellation on this mandatory stress test is already retained by the **full level/price-profile KL**. It is lost only when that distribution is compressed further to a scalar mean or to a fixed-fraction/data-processing surrogate.

This applies the completed OTHER-account result fleet04/B15 `20260922T081139Z-bellman-packet-split`: that report warned that scalar Bellman price information is insufficient and that the full price-profile KL must remain live. Equation (3.1) gives an exact reason on the one-point-defect suspension: the full price profile alone captures every bit of the surviving I-projection KL, while valuation depth contributes zero.

More generally, whenever \(g\) is permutation-invariant, its squared spectral law and its product I-projection are both exchangeable, so the same chain-rule argument yields
\[
K_{\rm occ}(y g)
=
D_{\rm KL,2}\!\left(
\mathcal L_{\widehat g^2}(|S|)
\big\|
{\rm Binomial}(m,I(g)/m)
\right).
\tag{3.2}
\]
This is an exact class identity, not a full FEI theorem.

## 4. Direct application to the current repaired center

The named completed OTHER-account construction fleet03/B12 proves the universally gate-safe tilted-quartic direction and proposes
\[
C_*=6.538805311222222\ldots
\]
after repairing the known biased Numaro prime obstruction.

The no-loss theorem is potential-independent, so it applies to this center without assuming that `Gamma*` is universal. As a decisive diagnostic, retaining \(99\%\) of \(K_{\rm occ}\) and dropping only \(1\%\), with no other subsidy, already fails on the genuine Boolean one-point-defect suspension at
\[
\boxed{m=258}
\]
in the stable direct computation:
\[
{B_{\rm inf}^{C_*}+0.99K_{\rm occ}\over I(g_{258})}
=
-0.001344647640000\ldots<0.
\tag{4.1}
\]
For every fixed percentage loss, Theorem 2.1 gives failure at some finite \(m\); (4.1) is only a finite sanity witness for the current repaired center.

This is the concrete way the fleet03/B12 result is used: the newest safe repair changes the finite center, but it does **not** relax the requirement that the dependence KL be preserved to additive \(O(I)\) accuracy on sparse suspensions.

## 5. Checker and finite scope

`verify_suspension_no_loss.py` uses only the Python standard library. It performs exact integer Walsh transforms for the one-point defect through \(m=8\), verifies the exact coefficient pattern and the two oriented pivotal points per coordinate, verifies normalization with rational arithmetic, compares the level-law KL with \(K_{\rm occ}\) at \(m=4,8,12,20\), and evaluates the stable closed forms through the \(99\%\) diagnostic above.

Recorded hashes before repository write:

- checker SHA-256: `008159b64fee32064ae571a7fb28506da90d9fad46f534205d6736d275e9f48e`;
- output SHA-256: `22e09afa894dc6b72d1e12c86e5d296f15175f5095ed84d583525e159cdf0376`.

The output ends in `PASS`. These computations check formulas and one finite witness only. Theorems 1.1 and 2.1 are analytic.

## 6. Exact old/new implication and remaining obligation

**Old first missing Shannon implication:** after exact payment of all original-coordinate first moments, prove
\[
K_{\rm occ}
\ge
\left[
H_{\max}(r)+a_q-\sum_i r_i a_i
\right]_+
\]
for every Boolean gate/source under a universal finite-cap potential.

**New proved inference:** on the exact Boolean suspension \(F=yg\), that implication is identically the original FEI inequality for \(g\). On the one-point-defect suspensions, \(K_{\rm occ}/I\sim m\), the signed valuation-tail bank is zero, and any fixed fractional loss of \(K_{\rm occ}\), even supplemented by an arbitrary finite multiple of \(J\), fails.

**Remaining quantified obligation:** the full universal inequality is still open. A viable continuation must preserve the dependence credit to **additive influence scale**, not merely multiplicative accuracy. Concretely, any data-processing statistic used in the low-Bellman corridor must establish a source-valid bound of the form
\[
\boxed{
K_{\rm occ}
-
D_{\rm KL,2}(Z_\#P\|Z_\#Q_r)
\le L\,J
}
\tag{6.1}
\]
for one finite \(L\), **and** the all-gate argument must explicitly pay that \(LJ\) loss from the candidate's actual safe-direction/child slack. On the one-point-defect suspension the exact level/price profile achieves loss zero, so (6.1) is at least compatible with the mandatory hard family. It remains completely unproved for arbitrary Boolean sources.

An alternative valid closure is to avoid data processing and prove the original exact \(K_{\rm occ}\) payment directly from signed Boolean convolution plus the gate-safe potential. What is ruled out by this run is the intermediate shortcut “recover any fixed positive fraction of \(K_{\rm occ}\), then use the valuation bank.”

## 7. Current literature applicability

A fresh primary-source check on 22 September 2026 still finds unrestricted FEI open in the inspected sources. Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued functions with sharp class constant \(4\) and for partially bent functions with sharp class constant \(2\), not all Boolean functions. González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), give restriction/stopping-tree progress and structured classes. Li--Han, arXiv:2512.03117 (2 December 2025), retain an influence-profile entropy term in a strengthened information-theoretic inequality. None supplies the universal exact dependence-KL payment above.

No novelty or priority claim is made for the abstract I-projection identity, suspension trick, or data-processing observation; the contribution here is their exact application to the current source-normalized FEI residual and the resulting no-loss obstruction.

## 8. Ledger

- **PROVED:** exact suspension pullback (1.2)--(1.8), including all degenerate cases.
- **PROVED:** on the suspension face, the missing I-projection Shannon implication is exactly FEI for the unsuspended source.
- **PROVED:** one-point-defect asymptotics (2.7)--(2.11).
- **PROVED:** any fixed fractional dependence-KL recovery plus any finite \(O(J)\) reserve fails on those genuine Boolean suspensions.
- **PROVED:** the full level/price-profile law is KL-sufficient on the one-point-defect suspension, so its dependence credit can be retained losslessly there.
- **OPEN:** additive-\(O(J)\)-loss source statistic or direct signed payment for arbitrary Boolean sources.
- **OPEN:** construction of one universal finite-cap symmetric potential satisfying every all-gate inequality.
- **OPEN:** full uniform-cube FEI.

# B16 FEI — pair-correlation Shapley bridge and one-sided signed transport interface

**Date:** 21 September 2026  
**Fleet scope:** `fleet04 / B16`  
**Directive:** `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z` under `BRAIN-BENCHMARK-FEI-2026-09-21-01`  
**Execution label:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Novelty/publication priority:** unverified; no novelty claim.

## 0. Fresh state and the route change

This run starts from four compatible signed facts.

1. The fleet04 coupled q-flip selector is exactly dummy-refinement invariant, preserves signed parity allocation relation by relation, and differs from ordinary fine-player Shapley only by third-and-higher mixed curvature. Its Harsanyi coefficient vector has squared norm at most `1/(8s)` at touched-pair support `s`.
2. The fleet04 Shapley--plaquette bridge is
   \[
   \frac8N L_v=E(g_v)-\mathcal C_v^M-\Theta_v^M,
   \]
   with the signed plaquette bank and terminal share retained literally.
3. The fleet03 fractional noisy-square bank gives
   \[
   \int_0^1
   \frac{\sum_{U\ne\varnothing}\sqrt{|U|}\,C_U(\rho)^2}
        {\sqrt{1-\rho^2}}\,d\rho
   \le I(f),
   \]
   and the original-coordinate q-flip profile is the cut-Radon transform of the disagreement indicator.
4. The fresh fleet01 one-sided multiplier theorem corrects the earlier absolute-value diagnostic. For the centered ordered-min raw entropy kernel, the dangerous negative multiplier tail is only `O(1/n)` even though positive low multipliers are `Theta(n)`. In particular the centered raw generator-entropy debit is
   \[
   \sum_i\langle k_n^{\rm raw},p_i\rangle
   <\frac{24}{n}J(f).
   \]
   Positive low multipliers are credits because every nonconstant Fourier coefficient of `p_i` is nonpositive. The unresolved large raw term is therefore the **constant displacement mode**, together with any genuinely negative modes introduced by the fully refunded signed residual.

The previous fleet04 handoff asked for a map from the `1/sqrt{s}` selector-refinement scale to the physical `sqrt{|U|}` noisy-square bank. Directly identifying Harsanyi support `s` with a physical Fourier frequency is artificial and risks losing signs. This run changes coordinates instead.

> **New move.** Interpolate continuously between independent fine-clone inclusion and perfectly block-coupled inclusion while preserving every one-clone marginal. The interpolation is a genuine pair-correlation semigroup. It gives an exact signed-curvature formula for the ordinary-Shapley/coupled-selector defect, and it diagonalizes on complete-pair biased Fourier modes with eigenvalue `lambda^{|A|}`. At `t=1/2`, `lambda` is literally the correlation/noise parameter of each clone pair.

This does not close FEI. It does put the selector mismatch into a noise-semigroup form without taking absolute values, and it shows exactly why a generic endpoint `L2` estimate is still insufficient.

---

## 1. Fine Shapley versus block-coupled Shapley

Let a cooperative game `V` have `m` labeled clone pairs
\[
P_j=\{j0,j1\},\qquad j=1,\dots,m.
\]
Write `Psi_j` for the aggregate of the two ordinary fine-player Shapley values and `Phi_j` for the coarse Shapley value of block `P_j`. For the q-flip entropy game, `Phi_j` is exactly the block-coupled selector share from the preceding fleet04 run.

For a target block `j`, let
\[
\Delta_j^{\rm blk}V(R)=V(R\cup P_j)-V(R)
\]
and
\[
\delta_jV(R)
=V(R\cup P_j)-V(R\cup\{j0\})-V(R\cup\{j1\})+V(R).
\]

Let `R_t` contain every individual fine player outside `P_j` independently with probability `t`.

### Theorem 1 — `B16-PAIR-SHAPLEY-BRIDGE`

For every finite cooperative game,
\[
\boxed{
\Psi_j
=
\int_0^1
\mathbb E\!\left[
\Delta_j^{\rm blk}V(R_t)
-(1-2t)\delta_jV(R_t)
\right]dt.
}
\tag{1.1}
\]

The block-coupled/coarse share is
\[
\boxed{
\Phi_j
=
\int_0^1
\mathbb E_{\rm blk,t}
\Delta_j^{\rm blk}V(R)\,dt,
}
\tag{1.2}
\]
where every other pair is included completely with probability `t`.

#### Proof

The standard beta-integral representation of a Shapley value is
\[
\phi_a(V)=\int_0^1
\mathbb E_{S_t\subseteq N\setminus\{a\}}
\bigl[V(S_t\cup\{a\})-V(S_t)\bigr]\,dt.
\]

Fix the other-player set `R` and abbreviate
\[
V_{00}=V(R),\quad
V_{10}=V(R\cup\{j0\}),\quad
V_{01}=V(R\cup\{j1\}),\quad
V_{11}=V(R\cup P_j).
\]
Summing the two fine-player marginals gives
\[
(1-t)(V_{10}+V_{01}-2V_{00})
+t(2V_{11}-V_{10}-V_{01}),
\]
which is exactly
\[
(V_{11}-V_{00})
-(1-2t)(V_{11}-V_{10}-V_{01}+V_{00}).
\]
Average over `R_t` and integrate to obtain (1.1). Equation (1.2) is the same Shapley integral applied to the coarse game on blocks. `square`

---

## 2. Correlating clone pairs continuously

For each other pair, define a distribution on its two inclusion bits `(X_0,X_1)` by
\[
\begin{aligned}
\nu_{t,\lambda}(00)&=(1-t)^2+\lambda t(1-t),\\
\nu_{t,\lambda}(11)&=t^2+\lambda t(1-t),\\
\nu_{t,\lambda}(10)&=\nu_{t,\lambda}(01)
=(1-\lambda)t(1-t),
\end{aligned}
\tag{2.1}
\]
for `0<=t,lambda<=1`.

Every single clone still has marginal `t`. At `lambda=0` the two clones are independent. At `lambda=1` they are perfectly coupled: only `00` and `11` remain, with probabilities `1-t` and `t`. Thus this interpolates exactly between the two selector laws in Section 1.

For a function `F` of the other clone players, write
\[
\mathbb E_{t,\lambda}F
\]
for expectation under the independent product of (2.1) over all other pairs.

### Theorem 2 — `B16-PAIR-CORRELATION-FLOW`

For every `F`,
\[
\boxed{
\frac{\partial}{\partial\lambda}\mathbb E_{t,\lambda}F
=
t(1-t)\sum_{k\ne j}
\mathbb E_{t,\lambda}^{(k)}
\delta_kF,
}
\tag{2.2}
\]
where the expectation on the right samples every pair except `k` from (2.1), and
\[
\delta_kF(R)=
F(R\cup P_k)+F(R)
-F(R\cup\{k0\})-F(R\cup\{k1\}).
\]

Consequently,
\[
\boxed{
\begin{aligned}
\Psi_j-\Phi_j
={}&-\int_0^1(1-2t)\,
\mathbb E_{t,0}\delta_jV\,dt\\
&-\int_0^1 t(1-t)
\int_0^1\sum_{k\ne j}
\mathbb E_{t,\lambda}^{(k)}
\delta_k\Delta_j^{\rm blk}V
\,d\lambda\,dt.
\end{aligned}
}
\tag{2.3}
\]

#### Proof

The derivative of one pair law is
\[
t(1-t)(\delta_{00}+\delta_{11}-\delta_{10}-\delta_{01}).
\]
Differentiate the product measure one factor at a time; this gives (2.2). Since `lambda=0` is the independent fine law and `lambda=1` is the coupled-block law,
\[
\mathbb E_{t,0}F-\mathbb E_{t,1}F
=
-t(1-t)\int_0^1
\sum_{k\ne j}\mathbb E_{t,\lambda}^{(k)}\delta_kF\,d\lambda.
\]
Insert `F=Delta_j^{blk}V` into (1.1)--(1.2). `square`

This is an exact interpolation identity, not a norm estimate.

---

## 3. Entropy games: the whole selector defect is signed plaquette curvature

Now let
\[
V(S)=E\!\left(\prod_{a\in S}g_a\right)
\]
be the spectral-entropy game of Boolean phase generators.

For a prefix phase `sigma`,
\[
\delta_kV=-\kappa_\sigma(g_{k0},g_{k1}),
\]
where
\[
\kappa_\sigma(a,b)
=E(a\sigma)+E(b\sigma)-E(\sigma)-E(ab\sigma)
\]
is the signed plaquette curvature from the earlier fleet04 transport report.

Also
\[
\delta_k\Delta_j^{\rm blk}V
=
-\Delta_j^{\rm blk}\kappa_\sigma(g_{k0},g_{k1}).
\]

### Corollary 3 — `B16-SELECTOR-CURVATURE-FLOW`

For an entropy game,
\[
\boxed{
\begin{aligned}
\Psi_j-\Phi_j
={}&
\int_0^1(1-2t)
\mathbb E_{t,0}
\kappa_{\sigma_R}(g_{j0},g_{j1})\,dt\\
&+
\int_0^1t(1-t)\int_0^1
\sum_{k\ne j}
\mathbb E_{t,\lambda}^{(k)}
\Delta_j^{\rm blk}
\kappa_{\sigma_R}(g_{k0},g_{k1})
\,d\lambda\,dt.
\end{aligned}
}
\tag{3.1}
\]

Thus the move from ordinary Shapley to the exact dummy-invariant coupled selector introduces **no positive generator-entropy baseline at all**. The correction is a signed average of plaquette curvature and its block response. Via the earlier four-phase theorem, every curvature in (3.1) is itself an exact signed Fourier log-cross-ratio. Negative Fourier tetrahedra remain credits.

The first kernel `(1-2t)` integrates to zero. Hence any curvature term independent of the other players vanishes automatically.

### Corollary 4 — low cooperative degrees vanish

If the Harsanyi degree of `V` is at most two, then
\[
\boxed{\Psi_j=\Phi_j\quad\text{for every }j.}
\tag{3.2}
\]

Indeed `delta_j V` is then independent of all other players, so the first integral in (2.3) vanishes by
\[
\int_0^1(1-2t)\,dt=0,
\]
while `Delta_j^{blk}V` is at most linear in each other fine player and therefore every pair second difference in the second line is zero.

This recovers, in semigroup form, the preceding Harsanyi conclusion that only third-and-higher mixed curvature can redistribute mass between clone blocks.

---

## 4. Exact pair-noise spectral diagonalization

The correlation parameter has an exact spectral meaning.

Fix `0<t<1`. Under independent Bernoulli-`t` inclusion define the normalized centered bit
\[
\xi_a=\frac{X_a-t}{\sqrt{t(1-t)}}.
\]
Let `hat F_t(S)` be the corresponding `t`-biased Fourier coefficient of `F`.

For a set `A` of clone pairs, let
\[
P_A=\bigcup_{k\in A}\{k0,k1\}
\]
be the complete-pair frequency.

### Theorem 5 — `B16-PAIR-NOISE-DIAGONALIZATION`

For every `F`,
\[
\boxed{
\mathbb E_{t,\lambda}F
=
\sum_{A}
\lambda^{|A|}\,
\widehat F_t(P_A).
}
\tag{4.1}
\]

In particular,
\[
\boxed{
\mathbb E_{t,1}F-\mathbb E_{t,0}F
=
\sum_{\varnothing\ne A}
\widehat F_t(P_A).
}
\tag{4.2}
\]

#### Proof

Within one pair under (2.1),
\[
\mathbb E\xi_{k0}
=\mathbb E\xi_{k1}=0,\qquad
\mathbb E[\xi_{k0}\xi_{k1}]=\lambda.
\]
Different pairs are independent. Therefore the expectation of a biased Fourier character is zero if any pair contributes exactly one clone, and is `lambda^{|A|}` if the frequency is exactly `P_A`. Expanding `F` proves (4.1). `square`

At `t=1/2`, `xi=2X-1` and `lambda` is literally the correlation of the two clone-selection signs. The selector correction is therefore a genuine noise/correlation flow, not merely an analogy based on matching exponents.

This supplies a concrete analytic interface to the already-proved midpoint `sqrt{|U|}` noisy-square bank: the missing map is now from **complete-pair selector frequencies** `P_A` to the physical cut/Radon frequencies, rather than from raw Harsanyi support counts to physical frequencies.

---

## 5. A killed shortcut: generic endpoint `L2` control still fails

Equation (4.2) also shows exactly what cannot work.

At `t=1/2`, take `q` other pairs and put
\[
F(X)=
\prod_{k=1}^q
\left(1+\xi_{k0}\xi_{k1}\right)-1.
\tag{5.1}
\]
Every nonempty complete-pair biased Fourier coefficient equals `1`. Hence
\[
\|F\|_{L^2(\nu_{1/2,0})}
=\sqrt{2^q-1},
\]
but
\[
\mathbb E_{1/2,1}F-\mathbb E_{1/2,0}F
=2^q-1.
\tag{5.2}
\]

So evaluation at the fully coupled endpoint has operator norm at least
\[
\sqrt{2^q-1}
\]
from generic selector-space `L2` to scalars. There is no dimension-free game-level Cauchy--Schwarz closure of (4.2).

This is **not** an FEI counterexample and is not asserted to be an entropy-game obstruction. It kills only the shortcut “pair-noise diagonalization plus a generic endpoint `L2` bound is enough.” The next step must use the physical Boolean/q-flip structure, the one-sided sign of the cut-Radon spectrum, or the signed cross-ratio cancellations.

---

## 6. What the fresh one-sided multiplier theorem changes

The fleet01 result means that the earlier `Theta(n)` positive low modes of the centered raw generator kernel no longer need cancellation: they are credits in the upper-bound direction. For any nonnegative codimension-level charge sequence `q_c`,
\[
\widehat{\mathcal K_n^q}(U)
=
\frac1n\sum_{c=2}^n q_c
\left[
2^{c-1}
\frac{\binom{n-1-|U|}{c-1}}{\binom{n-1}{c-1}}
-1
\right]
\ge-\frac{Q_n}{n},
\]
where `Q_n=sum_c q_c`. Since
\[
\widehat p_i(U)=-2\widehat\eta_i(U)^2\le0
\]
for `U ne 0`, only the negative multiplier tail is a debit.

For the actual raw generator entropies,
\[
Q_n^{raw}<12,
\]
so the entire centered raw baseline is one-sidedly paid by `<24J/n`.

Therefore the selector problem after this run is more precise:

* do **not** try to cancel all positive low modes;
* do **not** take an absolute selector-space norm;
* retain the coupled selector to enforce exact dummy Ward invariance;
* use (3.1)/(4.1) to express its higher-curvature correction as a pair-correlation flow;
* identify the constant displacement mode of the **fully refunded** Shapley/terminal/R16 residual and any genuinely negative nonconstant multipliers;
* map only those debit modes to the original-coordinate cut/noisy-square bank.

The constant-mode issue is not solved here. Also, because both fine and coarse Shapley rules are efficient,
\[
\sum_j(\Psi_j-\Phi_j)=0.
\]
Thus switching selectors only redistributes charge between blocks; it cannot by itself supply a missing global constant-mode refund. That refund must come from the actual signed plaquette/terminal/R16 ledger, not from relabeling the Shapley rule.

---

## 7. Executed exact checks

Companion code: `check_pair_correlation_curvature.py`.

It passed `python -m py_compile` and **1,975 exact rational checks** using only `fractions.Fraction`:

* 224 general cooperative-game bridge identities;
* 280 signed parity-game bridge identities, with either coefficient sign;
* 165 degree-at-most-two zero-defect checks;
* 650 pair-correlation derivative identities;
* 650 exact biased pair-parity spectral diagonalizations;
* 6 explicit generic endpoint-`L2` obstruction instances, for `q=1,...,6`.

No floating tolerance is used in these checks.

Checker SHA-256:

`e1a3f6bb75999f8790800f5fe70ff019536ce827e2586a955604f9391ad6b71d`

Output SHA-256:

`6685074d3fd26d8a0071c2ff5a0676e7d7db6c9d50cda2c0b6a13f710756654b`

The finite checks test implementation and formulas; Theorems 1, 2 and 5 and their entropy corollaries have algebraic proofs above.

---

## 8. Next exact target

The next B16 calculation should keep the pair-correlation parameter `lambda` and substitute the signed four-phase log-cross-ratio for `kappa` in (3.1). Then average over the physically meaningful translation/invariance q-flip blocks and use the exact cut-Radon sign
\[
\widehat p_i(U)=-2\widehat\eta_i(U)^2
\]
before applying any norm.

A successful closure need only control:

1. the constant displacement mode of the fully refunded residual; and
2. genuinely **negative** nonconstant multipliers.

Large positive multipliers are credits by the fresh one-sided theorem. The generic endpoint-`L2` counterexample in Section 5 shows why the physical cut sign and the signed cross-ratio cannot be discarded at the last step.

**Full FEI remains OPEN / NOT PROVED.**

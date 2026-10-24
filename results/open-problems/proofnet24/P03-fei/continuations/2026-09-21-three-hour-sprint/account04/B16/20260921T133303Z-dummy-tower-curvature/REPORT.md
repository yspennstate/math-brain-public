# B16 FEI — arbitrary-depth dummy Ward renormalization and exact plaquette cancellation

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, FEI signed transport / exact coupled selector  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Novelty/publication priority:** unverified; no novelty claim.

## 0. What moved

The entering route has three exact pieces that must be kept together.

1. The signed q-flip/Shapley ledger
   \[
   \frac8N L_v=H(g_v)-\mathcal C_v^M-\Theta_v^M
   \]
   preserves the alternating R32 signs, dual-code multiplicity, the terminal share, and the inherited moment/R16 refunds.
2. The coupled q-flip selector is exactly invariant under one dummy-coordinate split, while ordinary fine-player Shapley is not.  Its refinement defect is third-and-higher mixed curvature.
3. The pair-correlation interpolation rewrites the ordinary/coupled selector defect as a signed plaquette-curvature flow and diagonalizes the clone-pair correlation parameter.  A generic endpoint `L2` estimate is false, so the next useful result has to exploit structure rather than absolute values.

The fresh one-sided multiplier theorem also says that the large positive nonconstant Walsh multipliers of the raw ordered-min kernel are credits.  The unresolved large raw contribution is the constant displacement mode, together with genuinely negative modes created by the fully refunded residual.

This run isolates one entire source of that constant-mode growth and removes it exactly.

> **Main result.** Append *any number* of dummy physical coordinates.  Split every old q-flip dual phase into all of its dummy slices and keep those slices as one coupled block.  For every Boolean phase game, the block-coupled Shapley share is projectively invariant: the whole fine block has exactly the old Shapley share and every dummy slice has exactly `2^{-d}` of it.  In the entropy game this forces an exact signed plaquette-curvature refund.  For a codimension-`c` ordered-min dual defect, the apparently growing raw baseline `2^d H_{c+d}` is reduced exactly to the old share; in the isolated-block case the refund is
> \[
> 2^dH_{c+d}-H_c>0,
> \]
> and it grows as `8 d 2^{-c}+O_c(1)` bits.  Thus the linear dummy-dimension part of the raw constant mode is not a payment at all: it is an exact signed curvature refund.

This does **not** pay the genuinely relevant-coordinate constant mode and does not prove FEI.  It removes ambient dummy inflation from the target and shows that a universal payment should be formulated on a dummy-stable quotient.

---

## 1. Arbitrary Boolean phases and an arbitrary dummy tower

Let
\[
G=\mathbb F_2^n,
\qquad Y=\mathbb F_2^d,
\qquad k=2^d.
\]
Take arbitrary Boolean phases
\[
g_1,\ldots,g_m:G\to\{\pm1\}.
\]
For every `v` and every dummy label `y in Y`, define its slice clone
\[
 h_{v,y}(x,z)=
 \begin{cases}
 -1,&g_v(x)=-1\text{ and }z=y,\\
 +1,&\text{otherwise.}
 \end{cases}
 \tag{1.1}
\]
and let
\[
P_v=\{(v,y):y\in Y\}
\tag{1.2}
\]
be the size-`k` clone block.

At a fixed point `(x,z)`, if `g_v(x)=+1` every clone is `+1`; if `g_v(x)=-1`, exactly the clone with label `z` is `-1`.  Therefore
\[
\boxed{
 \prod_{y\in Y}h_{v,y}(x,z)=g_v(x).
}
\tag{1.3}
\]
The right side is understood as the dummy lift of `g_v`.

This construction is exactly what happens to an ordered-min q-flip dual generator when `d` dummy coordinates are appended *after* the old coordinates.  The pivot remains old, the old q-flip syndrome is duplicated over all dummy labels, and the descendant cell is partitioned into its `2^d` dummy slices.

Define the old entropy game
\[
V(S)=H\!\left(\prod_{v\in S}g_v\right)
\tag{1.4}
\]
and the fine game
\[
V^{\uparrow d}(T)=H\!\left(\prod_{a\in T}h_a\right).
\tag{1.5}
\]
Because adding ignored inputs leaves spectral entropy unchanged, (1.3) gives, for every old coalition `S`,
\[
\boxed{
 V^{\uparrow d}\!\left(\bigcup_{v\in S}P_v\right)=V(S).
}
\tag{1.6}
\]
No special form of the phases is used here.

---

## 2. `B16-DUMMY-TOWER-WARD` — exact projective invariance

Use the following selector on the fine players.

1. Choose a uniformly random permutation of the old blocks `P_1,...,P_m`.
2. Keep every block contiguous.
3. Inside every block choose a uniformly random order of its `k=2^d` slices.

Let `phi^{blk}_{v,y}` be the expected marginal of the fine clone `(v,y)` under this law, and let `phi_v(V)` be the ordinary Shapley value in the old `m`-player game.

### Theorem 2.1 — arbitrary-depth dummy Ward identity

For every finite family of Boolean phases, every `d>=0`, and every old block `v`,
\[
\boxed{
 \sum_{y\in Y}\phi^{blk}_{v,y}=\phi_v(V).
}
\tag{2.1}
\]
Moreover all `k` fine shares in one block are equal, hence
\[
\boxed{
 \phi^{blk}_{v,y}=2^{-d}\phi_v(V)
 \qquad(y\in Y).
}
\tag{2.2}
\]

#### Proof

Condition on the outer block order.  Immediately before block `P_v`, the prefix is a union of complete earlier blocks.  By (1.6) it is the dummy lift of an old coalition `S`.  Whatever the internal order of `P_v`, the `k` consecutive fine marginals telescope:
\[
\sum_{y\in Y}
\bigl[V^{\uparrow d}(S\cup\text{earlier slices}\cup\{(v,y)\})
      -V^{\uparrow d}(S\cup\text{earlier slices})\bigr]
=V(S\cup\{v\})-V(S).
\]
Averaging the uniform outer block order proves (2.1).

For (2.2), translation of the dummy input `z` by any `a in Y` permutes the slice labels `y -> y+a` simultaneously in every block.  Spectral entropy and the selector law are invariant under this translation.  The translation group acts transitively on the `k` labels in `P_v`, so their expected marginals are equal.  Equation (2.1) gives the common value.  `square`

### Corollary 2.2 — projective consistency through any refinement depth

Refine first by `d_1` dummy bits and then by `d_2`, or refine directly by `d_1+d_2`.  After identifying the labels in `F_2^{d_1}\times F_2^{d_2}`, every final clone has share
\[
2^{-(d_1+d_2)}\phi_v(V).
\tag{2.3}
\]
Thus the coupled selector is projectively consistent along the entire dummy tower.  No choice of how many harmless coordinates are appended can change the block charge.

This is stronger than the previous one-dummy statement: it is an all-depth Ward identity and it holds for arbitrary Boolean phases, not only for subcube defects.

---

## 3. Exact signed plaquette refund forced by the Ward identity

For Boolean phases `sigma,f,g`, retain the signed plaquette curvature
\[
\kappa_\sigma(f,g)
=H(f\sigma)+H(g\sigma)-H(\sigma)-H(fg\sigma).
\tag{3.1}
\]
For a fixed fine permutation and a target fine player `a`, if the preceding fine players are `b_1,...,b_r`, repeated use of
\[
\Delta_a H(b\sigma)=\Delta_aH(\sigma)-\kappa_\sigma(a,b)
\tag{3.2}
\]
gives
\[
\Delta_aH(b_1\cdots b_r)
=H(h_a)-
\sum_{j=1}^r
\kappa_{h_{b_1}\cdots h_{b_{j-1}}}(h_a,h_{b_j}).
\tag{3.3}
\]
No curvature is positive-parted.

Let `C^{(d)}_{v,y}` denote the expectation of the signed curvature sum in (3.3) under the coupled selector.

### Theorem 3.1 — `B16-DUMMY-TOWER-PLAQUETTE-RENORMALIZATION`

For every old Boolean phase game,
\[
\boxed{
 \mathcal C^{(d)}_{v,y}
 =H(h_{v,y})-2^{-d}\phi_v(V).
}
\tag{3.4}
\]
Consequently
\[
\boxed{
 \sum_{y\in Y}\mathcal C^{(d)}_{v,y}
 =\sum_{y\in Y}H(h_{v,y})-\phi_v(V).
}
\tag{3.5}
\]

#### Proof

Average (3.3) under the coupled selector.  The left side is `phi^{blk}_{v,y}`.  Apply (2.2) and rearrange.  Summing over `y` gives (3.5).  `square`

Equations (3.4)--(3.5) are exact signed transport identities.  They say that if dummy splitting makes the sum of raw generator entropies large, the signed plaquette bank *must* remove exactly the excess needed to recover the old Shapley share.  There is no extra dummy payment left over.

The theorem is deliberately only the entropy component.  The terminal-band/R16 ledgers stay separate exactly as in the entering compiler; no unproved dummy-invariance property of the terminal response is inserted here.

---

## 4. Ordered-min subcube duals: the raw linear dummy growth is exactly refunded

Now specialize to the ordered-min q-flip dual from the preceding B16 report.  Suppose the old generator `g_v` is the one-subcube defect of codimension `c>=2`.  Its squared Fourier spectrum has
\[
p_0=(1-2^{1-c})^2,
\qquad
p_1=2^{2-2c}
\tag{4.1}
\]
with `p_1` repeated `2^c-1` times.  Write its entropy in bits as
\[
H_c=-p_0\log_2p_0-(2^c-1)p_1\log_2p_1.
\tag{4.2}
\]
Each dummy slice clone is a codimension-`c+d` defect, so
\[
H(h_{v,y})=H_{c+d}.
\tag{4.3}
\]
Theorem 3.1 therefore gives the exact block refund
\[
\boxed{
 \sum_y\mathcal C^{(d)}_{v,y}
 =2^dH_{c+d}-\phi_v(V).
}
\tag{4.4}
\]
For an isolated old block, `phi_v(V)=H_c`, hence
\[
\boxed{
 R_{c,d}:=2^dH_{c+d}-H_c
}
\tag{4.5}
\]
is precisely the signed curvature refund generated by the dummy tower.

### Theorem 4.1 — the isolated-block refund is strictly positive

For every `c>=2` and every `d>=1`,
\[
\boxed{R_{c,d}>0.}
\tag{4.6}
\]

#### Proof

Put `q=2^{-c}` and `x=2q`.  For a subcube defect of negative-set density `q`, its entropy in natural units is
\[
H^{\rm nat}(q)
=-2(1-x)^2\ln(1-x)-2x(2-x)\ln x.
\tag{4.7}
\]
Since `q=x/2`, direct differentiation gives
\[
\frac{d}{dx}\left(\frac{H^{\rm nat}(q)}q\right)
=-\frac4{x^2}
\left[-x^2\ln x+(x^2-1)\ln(1-x)+x\right].
\tag{4.8}
\]
For `0<x<1`, every term inside the square bracket is strictly positive: `-x^2 ln x>0`, `(x^2-1)ln(1-x)>0`, and `x>0`.  Hence `H(q)/q` is strictly decreasing as a function of `q`.

Let `q'=q/2^d`.  Then
\[
\frac{H(q')}{q'}>\frac{H(q)}q,
\]
so
\[
2^dH(q')>H(q),
\]
which is (4.6).  `square`

Thus on this exact q-flip diagnostic the curvature term is not merely capable of canceling the dummy baseline; it is forced to carry a positive refund that grows with the refinement depth.

---

## 5. Exact layer telescope and asymptotic constant-mode cancellation

The refund has the exact one-dummy-layer decomposition
\[
\boxed{
R_{c,d}
=\sum_{r=0}^{d-1}2^r
\bigl(2H_{c+r+1}-H_{c+r}\bigr).
}
\tag{5.1}
\]
This is a literal telescope.  It matches the pair-correlation picture: every new dummy bit splits each current slice into a clone pair, and its fully integrated pair-correlation/plaquette refund is `2H_{m+1}-H_m` at codimension `m`.

For large `m`, (4.7) gives
\[
H_m
=2^{-m}
\left[
8m+4(\log_2 e-2)+O(m2^{-m})
\right].
\tag{5.2}
\]
Consequently, for fixed `c` and `d->infinity`,
\[
\boxed{
R_{c,d}=8d\,2^{-c}+O_c(1).
}
\tag{5.3}
\]
Equivalently each additional dummy layer contributes asymptotically
\[
2^r(2H_{c+r+1}-H_{c+r})
=8\,2^{-c}+o_c(1).
\tag{5.4}
\]

This is exactly the scale that looked dangerous in the raw generator baseline.  The coupled signed curvature ledger removes it layer by layer.

Examples in bits:
\[
R_{2,1}=2.4338343733773984\ldots,
\qquad
R_{2,4}=9.219292053694154\ldots,
\]
\[
R_{3,4}=4.440707685411548\ldots,
\qquad
R_{4,4}=2.14154481629863\ldots.
\tag{5.5}
\]
These numbers are diagnostic values of the proved formula, not evidence for a universal FEI constant.

---

## 6. What this says about the live constant-mode obstruction

The account01 one-sided multiplier theorem reduced the centered ordered-min debit to `O(J/n)` and left the constant displacement mode as the main raw obstruction.  The present theorem identifies a whole family of large constant-mode contributions that are *artifacts of harmless ambient dimension*:

* appending `d` dummy coordinates turns one codimension-`c` dual generator into `2^d` codimension-`c+d` fine generators;
* their raw entropy sum changes from `H_c` to `2^dH_{c+d}` and grows linearly in `d` after rescaling;
* the block-coupled signed plaquette bank refunds **exactly** `2^dH_{c+d}-H_c` in the isolated block, and more generally reduces the fine raw sum exactly to the old Shapley share `phi_v(V)`.

Therefore a correct universal transport norm should be invariant under this dummy refinement before any one-sided multiplier bound is applied.  The ambient-dimension piece of the constant mode is now removed exactly.

What remains is genuinely harder: for a Boolean function in which the coordinates are actually relevant, the old block share `phi_v(V)` itself can carry a nontrivial constant-mode debit, and the separately retained terminal/R16/moment ledgers may be needed.  Nothing above bounds that essential-coordinate contribution by `CI(f)`.

---

## 7. A stronger shortcut I did not promote

A tempting way to make every plaquette curvature monotone would be to prove the spectral-entropy triangle inequality
\[
H(ab)\le H(a)+H(b)
\tag{7.1}
\]
for arbitrary Boolean phases on shared variables.  The account02 coherent-product ledger shows why this is not a classical convolution inequality: the actual coherent product spectrum can have *larger* entropy and *smaller* influence than the independent XOR reference.  I did not obtain a proof of (7.1), and this run does not use it.

The dummy-tower theorem avoids that unproved shortcut completely.  Its cancellation follows from exact selector telescoping and signed plaquette identities, not from any sign assertion for a generic triangle defect.

---

## 8. Executed self-check

`check_dummy_tower_curvature.py` checks the algebra on two general Boolean phase games, not just subcube defects.

* three old phases with one dummy bit: all `48` coupled selector orders;
* two old phases with two dummy bits: all `1,152` coupled selector orders;
* complete-block product identity;
* block-share conservation and equal clone shares;
* the actual plaquette telescope (3.3), not only its endpoint;
* `56` subcube tower cases `2<=c<=8`, `1<=d<=8`, including strict positivity of (4.5) and the exact layer telescope;
* asymptotic diagnostics at `d=40`.

The run passed.  Maximum observed error in the general-game plaquette telescope was `1.18e-14`; the subcube layer telescope was exact to the displayed binary64 arithmetic.  The checker is a sanity check for the proved algebra, not a substitute for the proof and not an FEI audit.

---

## 9. Precise residual obligation

**Proved here:** arbitrary-depth dummy refinement is an exact Ward symmetry of the coupled selector, and the signed plaquette bank exactly removes the resulting raw entropy inflation.  For ordered-min subcube duals the isolated-block refund is strictly positive and has the explicit asymptotic `8d2^{-c}+O_c(1)`.

**Still open:** after quotienting out this dummy-stable component, prove a dimension-free upper bound on the **essential-coordinate** constant mode and on any genuinely negative nonconstant modes of the fully refunded q-flip residual, while retaining the terminal-band and R16/moment credits.

A concrete next calculation is to define the full basis-averaged residual on the dummy-stable quotient, insert the exact cut-Radon sign
\[
\widehat p_i(U)=-2\widehat\eta_i(U)^2\le0\quad(U\ne0),
\]
and ask only for a lower multiplier bound on the nonconstant quotient kernel plus a direct signed payment of its remaining constant mode.  The theorem above shows that no such payment is allowed to depend on the number of appended dummy coordinates.

Full unrestricted FEI remains **OPEN / NOT PROVED**.

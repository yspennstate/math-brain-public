# B16 — restriction-margin martingale: exact all-depth signed gate ledger

**Run:** `B16-20260922T003212Z-fei-gate-r13`  
**Status:** **AUXILIARY THEOREM / MECHANISM ADVANCE. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Authenticated repository context was consumed directly, but no authenticated cognitive-brain retrieval entered the proof.  
**Publication/novelty:** not assessed; no external priority claim is made.

## 0. Control change and why this run does not continue the old half-band campaign

Fresh owner control at `yspennstate/math-research-brain` revision `2026-09-22.2` supersedes the older fleet02/B16 half-band Campaign-C prompt mathematically. The live FEI target is the all-gate reformulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{G}
\]

The owner's two requested jobs were to prove that the read-once gate-margin extremum is decomposable/AND, or falsify it by an explicit gate. The second job has now been completed by compatible peer work, so this report does not repeat a numerical sweep.

### Named completed peer results actually used

1. **fleet01/B14, balanced 18-input gate refutation**, commit `a0b599c1fa6d27a5511f915a7ecb9e2fd8272040`. At uniform biases the source-valid balanced 18-input seed has
   \[
   I=261/128,
   \qquad
   6.521845710923046575658143972948578468366662292
   \le \frac{H}{I-1}
   \le
   6.521845710923046575658143972948578468366662293.
   \]
   Therefore for the read-once base cap `C0=6.4548`,
   \[
   c_G=4\left(\frac{H}{I-1}-C_0\right)
   \ge 0.268182843692186302632575891794313873466649168,
   \]
   over sixty times the reported AND margin `0.0043974201`. This rigorously falsifies the old AND/decomposable extremality claim for that potential.

2. **fleet04/B14, prime-gate falsifier**, commit `6cb77c5fe7e8705260eee8b7d1dd3cb925a05cff`. It proves the same 18-input seed is composition-prime, so the obstruction is not hidden disjoint composition.

3. **fleet04/B12, prime safe-split envelope**, scientific commit `d96b3f494236cacf75f4ae0d4395f0f2dbb3008c`. It derives the exact one-coordinate restriction residual `R_i`, Poincare currency `Q_i`, and proves that the old read-once base has a composition-prime obstruction for which every essential first split has residual margin above the Numaro-scale threshold. Thus a one-step "choose a good coordinate" rule is not the correct signed mechanism for that base.

4. **fleet04/B18, curvature-lift/Q-currency selector reduction**, commit `fddbb433154cccf36943c574b34a646cdb51add8`. It proves
   \[
   4Q_i=\sum_{S\ni i,\ |S|\ge2}w_S,
   \qquad
   4P_G=\sum_{|S|\ge2}(|S|-1)w_S,
   \qquad
   P_G\le\sum_iQ_i\le2P_G,
   \]
   and proposes a one-step aggregate selector as a sufficient replacement for blind arity induction.

5. **fleet01/B18, balanced-excess equivalence**, commit `64935432d83bb0c759225a6149535980157f1a62`. It proves full FEI(C) is equivalent to
   \[
   H(g)\le C[I(g)-1]
   \]
   for every balanced Boolean `g`.

The theorem below combines the restriction recursion and Q-currency with the global gate margin. It explains exactly where the one-step selector can lose valid signed compensation.

## 1. Normalizations

Fix a symmetric base potential `Gamma_0` with
\[
\Gamma_0(0)=\Gamma_0(1)=0.
\]
For a Boolean gate `G` under an interior product bias vector `p`, write
\[
A_0(t)=\frac{\Gamma_0(t)+h(V_t)}{V_t},
\]
\[
D_0(G;p)
=
\sum_i \operatorname{It}_i(G;p)A_0(p_i)
-H_t(G;p)-\Gamma_0(p_{\rm out}),
\tag{1.1}
\]
and
\[
P(G;p)=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})\ge0.
\tag{1.2}
\]

For a split on coordinate `i`, let `G_0,G_1` be the cofactors and let
\[
\mathcal E_i X=(1-p_i)X(G_0)+p_iX(G_1).
\]
Define the exact child-slack residual and Poincare currency
\[
R_i^0(G)=D_0(G)-\mathcal E_iD_0,
\qquad
Q_i(G)=P(G)-\mathcal E_iP.
\tag{1.3}
\]
The completed restriction work gives
\[
Q_i=p_i(1-p_i)\left[d_i-(q_1-q_0)^2\right]\ge0.
\tag{1.4}
\]

For the scalar curvature lift
\[
\Gamma_c=\Gamma_0+c\,\phi,
\qquad \phi(t)=t(1-t),
\tag{1.5}
\]
one has exactly
\[
D_c=D_0+cP,
\qquad
R_i^c=R_i^0+cQ_i.
\tag{1.6}
\]

Whenever `P(G)>0`, define the **global gate margin**
\[
c_G=-\frac{D_0(G)}{P(G)}.
\tag{1.7}
\]
Whenever `Q_i(G)>0`, define the **local restriction margin**
\[
c_{R,i}(G)=-\frac{R_i^0(G)}{Q_i(G)}.
\tag{1.8}
\]
These are in exactly the owner's `c_G` units: the scalar lift `c` makes the gate valid iff `c\ge c_G`.

Zero-currency cases cause no hidden term. By the biased-Fourier identity above, `P=0` means all Fourier mass is on levels 0 and 1; Booleanity then forces a constant or a literal. For a symmetric endpoint-zero potential its defect is exactly zero. Likewise an essential coordinate with `Q_i=0` would have no higher-order Fourier coefficient containing `i`; Booleanity forces the whole gate to be a literal, so at a non-affine node `Q_i=0` means the coordinate is inessential and `R_i^0=0`.

## 2. New theorem: exact Bellman decomposition of the gate margin

### Theorem 2.1 — one-step margin barycenter

For every non-affine gate (`P(G)>0`) and every coordinate `i`,

\[
\boxed{
P(G)c_G
=
Q_i(G)c_{R,i}(G)
+(1-p_i)P(G_0)c_{G_0}
+p_iP(G_1)c_{G_1},
}
\tag{2.1}
\]

with every zero-`P` child contribution interpreted as zero.

Moreover
\[
\boxed{
P(G)=Q_i(G)+(1-p_i)P(G_0)+p_iP(G_1).
}
\tag{2.2}
\]
Hence `c_G` is a literal convex combination of the local restriction margin and the two child global margins, with the displayed Poincare currencies as weights.

#### Proof

From the exact child-slack identity,
\[
D_0(G)=R_i^0+(1-p_i)D_0(G_0)+p_iD_0(G_1).
\]
Multiply by `-1` and use `-D_0=Pc_G` and `-R_i^0=Q_ic_{R,i}`. This is (2.1). Equation (2.2) is the defining Poincare-currency recursion. No inequality is used. `\square`

This is the exact missing continuation term in a blind one-step selector. A large `c_{R,i}` need not imply a large global `c_G`; it can be compensated by smaller child margins, and the compensation is paid in the same Poincare currency.

## 3. New theorem: adaptive restriction-margin martingale

An **adaptive restriction policy** may choose the next unrevealed coordinate using all previously exposed input values and its own independent randomness, but not future input values. Let
\[
G=G_0,G_1,\ldots,G_\tau
\]
be the resulting restriction path, stopped when the residual gate is affine. At step `r`, let `i_r` be the chosen coordinate and abbreviate
\[
Q_r=Q_{i_r}(G_r),
\qquad
c_r=c_{R,i_r}(G_r).
\]

### Theorem 3.1 — full-path signed NET identity

For every such adaptive policy,
\[
\boxed{
P(G)=\mathbb E\sum_{r<\tau}Q_r,
}
\tag{3.1}
\]
\[
\boxed{
P(G)c_G
=\mathbb E\sum_{r<\tau}Q_r c_r,
}
\tag{3.2}
\]
and therefore
\[
\boxed{
c_G
=
\frac{\mathbb E\sum_{r<\tau}Q_r c_r}
     {\mathbb E\sum_{r<\tau}Q_r}.}
\tag{3.3}
\]
The right side is independent of the adaptive policy.

For the scalar lift `Gamma_c`,
\[
\boxed{
D_c(G)
=
\mathbb E\sum_{r<\tau}Q_r\,(c-c_r).
}
\tag{3.4}
\]
Thus the exact all-depth signed sufficient-and-necessary NET bound is
\[
\boxed{
\mathbb E\sum_{r<\tau}Q_r(c_r-c)\le0.
}
\tag{3.5}
\]
Positive and negative local credits are retained; no positive part or absolute value appears.

#### Proof

Iterate (2.2) until the affine terminal node, whose Poincare currency is zero. This gives (3.1). Iterating (2.1) gives (3.2), because every terminal affine gate has zero defect and hence zero `Pc_G`. Division yields (3.3). Finally
\[
D_c=D_0+cP=-Pc_G+cP=P(c-c_G),
\]
and substitute (3.1)--(3.3). `\square`

### Stopping-time form

For any earlier bounded stopping time `sigma`, not necessarily terminal,
\[
\boxed{
P(G)c_G
=
\mathbb E\left[
\sum_{r<\sigma}Q_rc_r+P(G_\sigma)c_{G_\sigma}
\right].
}
\tag{3.6}
\]
This is the exact continuation-credit identity. The one-step safe-split method keeps the first summand but attempts to make it nonpositive relative to `c` before allowing the child continuation. The peer prime obstruction shows that requirement can be too strong.

## 4. Signed block-selector theorem: a noncircular repair of one-step induction

For a stopping rule `sigma` with at least one coordinate revealed almost surely, define the consumed block currency
\[
Q_{\sigma}=\mathbb E\sum_{r<\sigma}Q_r
=P(G)-\mathbb E P(G_\sigma),
\tag{4.1}
\]
and, when `Q_sigma>0`, the signed block margin
\[
c_{\sigma}
=
\frac{\mathbb E\sum_{r<\sigma}Q_rc_r}{Q_\sigma}.
\tag{4.2}
\]

### Theorem 4.1 — adaptive block induction

Fix `c<infinity`. Suppose that for every non-affine finite gate there exists an explicitly source-defined adaptive stopping rule that reveals at least one coordinate on every path and satisfies
\[
\boxed{c_\sigma\le c.}
\tag{4.3}
\]
Then every gate obeys `c_G\le c`; equivalently the scalar-lifted potential `Gamma_0+c phi` satisfies (G) for every arity.

#### Proof

Induct on essential arity. Every descendant at the stopping time has smaller essential arity and therefore has global margin at most `c`. The stopping identity (3.6) becomes a convex combination of the block margin and descendant global margins, all at most `c`. Hence the parent margin is at most `c`. `\square`

A fixed depth-two version is already strictly weaker than the failed one-step condition:
\[
\boxed{
\frac{\mathbb E[Q_0c_0+Q_1c_1]}
     {\mathbb E[Q_0+Q_1]}
\le c
}
\tag{4.4}
\]
for some adaptive two-coordinate rule at every non-affine gate (with a one-step base case at arity one). No claim that (4.4) is true is made here. It is the first concrete signed successor to test after the prime one-step obstruction.

## 5. Application to the completed prime safe-split obstruction

The fleet04/B12 theorem says that, for the old read-once base and the Numaro-scale threshold around
\[
c_*=0.2681828436921863\ldots,
\]
there is a composition-prime obstruction at arity at most 18 for which every essential **first-step** residual margin exceeds `c_*`.

Theorem 3.1 shows exactly what that result does and does not imply:

* it decisively kills a proof that requires `c_{R,i}\le c_*` at the first split;
* it does **not** by itself force the full gate margin above `c_*`, because the descendant terms in (2.1) are authentic signed continuation credits;
* if a root margin is at or below `c_*` while every first-step margin is above it, then (2.1) forces the Poincare-weighted child margin strictly below `c_*`. In other words, descendant refund is not optional; it is algebraically forced.

This reconciles the one-step prime obstruction with the gate formulation without dropping child slack.

The newer fleet04/B18 aggregate selector
\[
\sum_i(R_i^0+cQ_i)\ge0
\]
is another legitimate **sufficient** depth-one criterion for its certified reference potential. The present theorem shows it is not the weakest signed condition: the exact global object is the all-depth Q-weighted barycenter (3.5). Because fleet04/B18 uses a different certified base/cap normalization from the old `C0=6.4548` candidate, the fleet04/B12 counterexample is not silently transferred to that newer aggregate inequality. That compatibility test remains to be done source-exactly.

## 6. Balanced-excess specialization: an exact full-FEI restriction currency

Now consume the fleet01/B18 theorem that FEI(C) is equivalent to
\[
H(g)\le C[I(g)-1]
\]
for every balanced Boolean `g`.

Take the base potential `Gamma_0=0` and uniform input biases. At every restriction node let
\[
L_r
=H_t(G_r)-\mathbb E[H_t(G_{r+1})\mid G_r]
=JS_r+B_r\ge0.
\tag{6.1}
\]
Then `R_r^0=-L_r`, hence on `Q_r>0`,
\[
c_r=\frac{L_r}{Q_r}.
\tag{6.2}
\]
Entropy and Poincare currency telescope separately:
\[
H(g)=\mathbb E\sum_r L_r,
\qquad
\frac{I(g)-1}{4}=P(g)=\mathbb E\sum_r Q_r.
\tag{6.3}
\]
Therefore
\[
\boxed{
\frac{H(g)}{I(g)-1}
=
\frac{
\mathbb E\sum_r Q_r\,\frac{L_r}{4Q_r}
}{
\mathbb E\sum_r Q_r
}.
}
\tag{6.4}
\]
When `Q_r=0`, Booleanity forces either an inactive split or a literal node, and then `L_r=0`, so there is no hidden zero-denominator entropy charge.

Combining (6.4) with balanced-excess equivalence gives the exact target-level identity
\[
\boxed{
C_{\rm FEI}
=
\sup_{g\ \mathrm{balanced}}
\frac{
\mathbb E\sum_r Q_r\,\rho_r
}{
\mathbb E\sum_r Q_r
},
\qquad
\rho_r:=\frac{L_r}{4Q_r},
}
\tag{6.5}
\]
for **every** adaptive restriction policy. This is not a proof that the supremum is finite. It is a source-exact signed/all-depth replacement for the already-refuted pointwise-erasure and blind-one-step routes.

The owner's recorded bent-plus-one-point-flip family already warns why one must not replace (6.5) by `rho_r<=C` pointwise: a single-coordinate erasure ratio can grow linearly with dimension. The all-depth Q-weighted average, rather than the worst local ratio, is the exact quantity.

## 7. Weakest sufficient full-net statement and next exact target

For a fixed base `Gamma_0` and candidate scalar lift `c`, the mathematically weakest source-exact restriction statement furnished by this mechanism is simply
\[
\boxed{
\mathbb E\sum_r Q_r(c_r-c)\le0
\quad\text{for every Boolean gate.}
}
\tag{7.1}
\]
It is equivalent to the gate inequality for `Gamma_0+c phi`, so (7.1) is a target representation, not closure.

A genuinely noncircular strengthening that would close FEI is the finite-block statement in Theorem 4.1. The first unresolved concrete version is depth two, (4.4), for the certified replacement reference and the current source-certified scalar lift. It preserves the precise continuation cancellation that the prime safe-split theorem proves is necessary.

The immediate computational/theoretical test should therefore be:

> On the composition-prime 18-input source gate and then the stronger 162-input balanced obstruction, compute the source-exact **two-step block margin** for the certified replacement base, minimizing over the second split adaptively after the first revealed value. If it still exceeds the candidate scalar lift on every first coordinate, depth two is refuted; if it drops below, the calculation identifies an explicit descendant refund to prove analytically.

This is materially different from another all-coordinate root average and does not reuse the killed AND-extremality claim.

## 8. Independent self-check

A standard-library checker beside this report exhaustively enumerates all 276 Boolean functions through three variables, all fixed coordinate orders, and an intentionally value-dependent adaptive order. It also checks 1,000 random four-variable truth tables under three policies. In total it verifies 4,848 restriction paths. For the uniform `Gamma_0=0` specialization it confirms

\[
H=\mathbb E\sum L,
\qquad
P=\mathbb E\sum Q,
\qquad
Q\ge0,
\qquad
Q=0\Rightarrow L=0,
\]
with maximum reported telescope error `0.0` in the exact dyadic/Walsh floating computations used by the script. This is a self-check of the algebra, not independent end-to-end FEI verification.

## 9. Problem-status statement

**FULL-PROBLEM CHANGE:** none. Full uniform-cube FEI remains open and is not proved here.

**MECHANISM CHANGE:** yes. The current owner gate target is already falsified for the old read-once potential by a completed explicit prime balanced gate. This run replaces the now-dead one-step safe-coordinate logic by an exact Poincare-currency restriction martingale and a finite-block signed induction theorem. The universal unpaid implication is now a finite-block bound (depth two is the first concrete test), not an unsigned root selector and not the retired half-band positive-current route.

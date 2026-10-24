# B16 FEI — coupled q-flip selectors and dummy-split Ward transport

**Date:** 21 September 2026  
**Fleet scope:** `account04 / B16`  
**Execution label:** **WITHOUT_VERIFIED_BRAIN**  
**Current sprint role:** exact coupled selector constructions inside the signed/shared-variable FEI route  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Novelty/publication priority:** unverified; no novelty claim.

## 0. Entering state and the move made in this run

The entering signed compiler state has three exact compatible pieces.

1. The weight-four q-flip basis gives an exact signed Aumann--Shapley disintegration of the R32 residual. Relation coefficients keep their alternating sign, so the `2 mod 4` terms remain negative credits and dual-code multiplicity is not collapsed.
2. The Shapley--plaquette bridge identifies each q-flip load with a dual-generator entropy marginal minus the signed plaquette-curvature bank and the matching terminal Shapley share.
3. The cut-Radon and fractional noisy-square identities keep the original physical disagreement geometry and provide a dimension-free signed `L2` sink, including the midpoint bank with `sqrt(|U|)` weight.

The newest compatible handoffs add two warnings/positive results that this run respects. Account03 proves that on dummy-extended monomial defects the Shapley curvature refund cancels the bad `Theta(n)` low mode exactly. Account02 then **refutes** the proposed basiswise pointwise `L_v=O(n)` q-flip bound by an exponential singleton-syndrome family, while proving exact random-basis orbit-averaged signed cancellation on transitive disagreement-edge orbits. Thus a basiswise local-charge proof is dead; averaging/coupling is mathematically necessary. The open question used here is whether one can construct a selector that has exact dummy-coordinate cancellation for an arbitrary Boolean phase without reviving that killed pointwise lemma.

This run answers that question at the selector level.

> **Main result.** Ordinary fine-player Shapley values are *not* invariant under a dummy-coordinate refinement, even for a genuine three-variable Boolean function. However, a block-coupled selector that keeps the two dummy clones of each q-flip adjacent has exact refinement invariance for every Boolean function. On every signed parity monomial in the R32 polynomial it also has an exact sign-preserving allocation: blocks with even relation occupancy get zero, while the blocks with odd occupancy split the signed coefficient equally. The difference between ordinary Shapley and the coupled selector consists only of third-and-higher mixed plaquette curvatures, with an exact `1/sqrt(8s)` coefficient bound at support size `s`.

This is a new implication, not an audit or a rerun. It is designed to preserve signed cancellation, original-coordinate q-flip geometry, dual-code multiplicity, R16/moment refunds and the separately retained terminal payment.

---

## 1. Ordered-min q-flips under one dummy-coordinate extension

Let `f : F_2^n -> {+1,-1}` and append a dummy physical coordinate `y` *after* all old coordinates in the ordered-min pivot rule:

\[
 f^\uparrow(x,y)=f(x).
\]

For an old ordered-min q-flip index `v` with pivot `p=min supp(v)`, write its two fine descendants as

\[
 v^0=v,\qquad v^1=v+e_y.
\]

The q-flip syndrome exponent is

\[
 b_v=q(v)+q(v+e_p)
\]

in the usual affine gauge. Since the extended phase is independent of `y`,

\[
 b_{v^0}(f^\uparrow)=b_{v^1}(f^\uparrow)=b_v(f).
\tag{1.1}
\]

Hence every active old q-flip is replaced by exactly two active fine q-flips, and no inactive old q-flip becomes active.

For the ordered-min dual phase generator, the negative set is the descendant cell fixing every coordinate from the pivot onward. Therefore the two fine generators are the two `y`-halves of the old descendant cell. If they are denoted `g_{v,0}` and `g_{v,1}`, then

\[
 \boxed{g_{v,0}g_{v,1}=g_v^\uparrow.}
\tag{1.2}
\]

This is an exact factorization in the physical truth-table phase group. It introduces no synthetic geometry.

Let the old active q-flip set be `M`. The fine active set is therefore the disjoint union of pairs

\[
 P_v=\{(v,0),(v,1)\},\qquad v\in M.
\tag{1.3}
\]

For the entropy game

\[
 G(S)=E\!\left(\prod_{v\in S}g_v\right),
\qquad
 G^\uparrow(T)=E\!\left(\prod_{a\in T}g_a\right),
\]

dummy extension and (1.2) imply

\[
 \boxed{
 G^\uparrow\!\left(\bigcup_{v\in S}P_v\right)=G(S)
 }
\tag{1.4}
\]

for every old coalition `S`. Spectral entropy is unchanged by appending an ignored input.

---

## 2. A coupled selector that is exactly dummy-invariant

Define a random **block-coupled permutation** of the fine active players as follows.

1. Choose a uniformly random permutation of the old q-flip blocks `P_v`.
2. Keep each block contiguous.
3. Inside each two-player block choose either order with probability `1/2`.

For any cooperative game `V` on the fine players, let

\[
 \phi_a^{\rm blk}(V)
 =\mathbb E[ V(S_{\pi,a}\cup\{a\})-V(S_{\pi,a})]
\]

be the marginal under this coupled permutation law.

### Theorem 2.1 — `B16-COUPLED-DUMMY-WARD` — PROVED

For the dummy-refined entropy game in Section 1 and every old active q-flip `v`,

\[
 \boxed{
 \phi_{(v,0)}^{\rm blk}(G^\uparrow)
 +\phi_{(v,1)}^{\rm blk}(G^\uparrow)
 =\phi_v(G),
 }
\tag{2.1}
\]

where the right side is the ordinary Shapley value in the old game.

Moreover translation in the dummy coordinate swaps the two clones in *every* block and preserves spectral entropy. The coupled permutation law is invariant under the same swap. Therefore

\[
 \boxed{
 \phi_{(v,0)}^{\rm blk}(G^\uparrow)
 =\phi_{(v,1)}^{\rm blk}(G^\uparrow)
 =\frac12\phi_v(G).
 }
\tag{2.2}
\]

#### Proof

Condition on the outer block order. Immediately before block `P_v`, the prefix is a union of complete earlier blocks. By (1.4) it is exactly an old coalition `S`. The two consecutive fine marginals telescope, independently of their internal order:

\[
\begin{aligned}
&[G^\uparrow(S\cup\{(v,b_1)\})-G^\uparrow(S)]\\
&\quad+[G^\uparrow(S\cup P_v)-G^\uparrow(S\cup\{(v,b_1)\})]\\
&=G^\uparrow(S\cup P_v)-G^\uparrow(S)
=G(S\cup\{v\})-G(S).
\end{aligned}
\]

Averaging the uniform outer block order gives (2.1). The global dummy translation sends clone `0` to clone `1` in every block, leaves the game value unchanged, and preserves the coupled permutation distribution, so the two expected fine marginals are equal. Together with (2.1) this gives (2.2). `square`

### Consequence

The exact dummy-coordinate Ward cancellation is **not** confined to monomial defects. It holds for the coupled selector for every Boolean function and every old q-flip simultaneously. In particular appending a dummy coordinate cannot create a growing baseline entropy charge in this selector: the old charge is simply divided by two across the two physical clone cells.

The construction changes the selector law, not the compiler identity. Efficiency and linearity hold for any distribution on permutations, so the signed Shapley--plaquette telescope may be run with this same coupled law. This is compatible with the newer account02 result showing that averaging/coupling is necessary and that a basiswise `L_v=O(n)` bound is false. What remains open is the dimension-free payment for genuinely interacting non-dummy blocks after the permitted averaging.

---

## 3. Exact signed parity allocation under the coupled selector

The R32 relation polynomial is a signed sum of parity monomials. The coupled selector has a particularly simple exact action on each one.

Partition any active player set into blocks `P_1,...,P_m`, keep every block contiguous, and choose a uniform random outer block order. Consider one signed parity game

\[
 Q_R(S)=c\,\frac{1-(-1)^{|S\cap R|}}2,
\tag{3.1}
\]

where `R` is the set of active relation coordinates appearing in that monomial. In the frustrated case `|R|` is odd. Define

\[
 o_j=|R\cap P_j|\pmod2,
\qquad
 q_{\rm odd}=|\{j:o_j=1\}|.
\]

Then `q_odd` is itself odd and nonzero.

### Theorem 3.1 — `B16-BLOCK-PARITY-SELECTOR` — PROVED

The total coupled-selector marginal assigned to block `P_j` is

\[
 \boxed{
 \Phi_j^{\rm blk}(Q_R)
 =
 \begin{cases}
 c/q_{\rm odd},&o_j=1,\\
 0,&o_j=0.
 \end{cases}
 }
\tag{3.2}
\]

This remains true for either sign of `c`.

#### Proof

Inside a contiguous block, every selected relation coordinate toggles the parity. If the block contains an even number, its total telescoped marginal is zero. If it contains an odd number, its total marginal is `+c` or `-c` according to whether an even or odd number of previous odd blocks have appeared. Even blocks do not affect that parity. Thus the game reduces exactly to a parity game on the `q_odd` odd blocks. Their relative outer order is uniform. Since `q_odd` is odd, the alternating sequence `+c,-c,+c,...,+c` sums to `c`, and symmetry gives expected share `c/q_odd` to each odd block. `square`

### Corollary 3.2 — signed R32 load with orbit cancellation

Apply Theorem 3.1 relation by relation to the exact signed R32 polynomial. For a chosen block partition of active q-flips, let `q_A^{odd}` be the number of blocks in which relation `A` has odd basis-coordinate occupancy. The coupled block load is

\[
 \boxed{
 L_B^{\rm blk}
 =\sum_{\substack{A\ \mathrm{frustrated}\\
                   A\ \mathrm{has\ odd\ occupancy\ in}\ B}}
 \frac{c_A}{q_A^{\rm odd}}.
 }
\tag{3.3}
\]

Summing over all blocks recovers the original signed relation charge exactly. Thus

* `2 mod 4` negative R32 coefficients stay negative;
* every relation retains its own coefficient and multiplicity;
* even within-block relation occupancy cancels *before* payment rather than being absolutized;
* no T-join length, synthetic edge distance, or positive-part operation is introduced.

For dummy clone blocks this is the exact algebraic reason that redundant even dummy occupancy need not consume transport budget.

---

## 4. Why ordinary fine-player Shapley is not enough

A tempting stronger statement would say that ordinary uniform Shapley on all fine clone players already has the orbit conservation (2.1). That statement is false.

For a general fine game `V`, write its Harsanyi dividend

\[
 d(T)=\sum_{R\subseteq T}(-1)^{|T|-|R|}V(R).
\tag{4.1}
\]

Let the fine players be paired into clone blocks `P_v`. Write

\[
 \Psi_v=\sum_{a\in P_v}\phi_a(V)
\]

for the aggregate *ordinary* fine Shapley share, and let `Phi_v` be the Shapley value of the coarse game obtained by restricting `V` to unions of complete pairs.

For a fine coalition `T`, let

\[
 s(T)=|\{v:T\cap P_v\ne\varnothing\}|,
\qquad
 t_v(T)=|T\cap P_v|\in\{1,2\}.
\]

### Theorem 4.1 — `B16-SHAPLEY-REFINEMENT-DEFECT` — PROVED

For every paired game,

\[
 \boxed{
 \Psi_v-\Phi_v
 =\sum_{T:T\cap P_v\ne\varnothing}
 d(T)\left(\frac{t_v(T)}{|T|}-\frac1{s(T)}\right).
 }
\tag{4.2}
\]

If `r(T)` is the number of touched pairs from which `T` contains both clones, then `|T|=s+r` and the coefficient is

\[
 w_v(T)=
 \begin{cases}
 \displaystyle \frac{s-r}{s(s+r)},&t_v=2,\\[6pt]
 \displaystyle -\frac{r}{s(s+r)},&t_v=1.
 \end{cases}
\tag{4.3}
\]

Consequently, for each dividend `T`,

\[
 \sum_v w_v(T)=0,
\tag{4.4}
\]

and

\[
 \boxed{
 \sum_v w_v(T)^2
 =\frac{r(s-r)}{s(s+r)^2}
 \le \frac1{8s}.
 }
\tag{4.5}
\]

Also

\[
 \boxed{
 \sum_v|w_v(T)|
 =\frac{2r(s-r)}{s(s+r)}
 \le 6-4\sqrt2<0.344.
 }
\tag{4.6}
\]

If `r=0` or `r=s`, every coefficient vanishes.

#### Proof

The standard dividend representation of the Shapley value is

\[
 \phi_a(V)=\sum_{T\ni a}\frac{d(T)}{|T|}.
\]

Therefore the fine pair aggregate weights dividend `d(T)` by `t_v/|T|`. The Harsanyi dividend of the coarse game on a set `S` of pairs is the sum of all fine dividends whose set of touched pairs is exactly `S`; hence the coarse Shapley value weights the same fine dividend by `1/s(T)`. Subtraction gives (4.2).

If `r` of the `s` touched pairs are doubled, then `|T|=s+r`, yielding (4.3). Equation (4.4) is immediate. Squaring the `r` positive and `s-r` negative coefficients gives

\[
 r\frac{(s-r)^2}{s^2(s+r)^2}
 +(s-r)\frac{r^2}{s^2(s+r)^2}
 =\frac{r(s-r)}{s(s+r)^2}.
\]

Writing `x=r/s`, the factor after `1/s` is `x(1-x)/(1+x)^2`, maximized at `x=1/3` with value `1/8`, proving (4.5). The `l1` expression is `2x(1-x)/(1+x)`, maximized at `x=sqrt(2)-1`, giving `6-4sqrt(2)`. `square`

### Corollary 4.2 — only third-and-higher curvature can move mass between clone orbits

A nonzero refinement coefficient requires `1<=r<=s-1`. Hence `s>=2` and

\[
 |T|=s+r\ge3.
\]

Thus **no first-order generator entropy and no second-order dividend can contribute to the orbit redistribution** between ordinary fine Shapley and the exact coupled selector.

For an entropy product game,

\[
 d(T)=\Delta_T E(1).
\]

If `a,b in T`, the account04 plaquette curvature satisfies

\[
 \Delta_a\Delta_bE(\sigma)=-\kappa_\sigma(g_a,g_b),
\]

so for `|T|>=3`

\[
 \boxed{
 d(T)
 =-\Delta_{T\setminus\{a,b\}}
 \kappa_1(g_a,g_b).
 }
\tag{4.7}
\]

The ordinary-Shapley refinement defect is therefore *purely a signed higher-curvature transport*. The dangerous raw `H_c` baseline is absent from (4.2).

The `l2` coefficient scale in (4.5) is `O(s^{-1/2})`. This is the same half-order exponent appearing in the already-proved midpoint fractional noisy-square bank

\[
 \int_0^1
 \frac{\sum_{U\ne\varnothing}\sqrt{|U|}\,C_U(\rho)^2}
 {\sqrt{1-\rho^2}}\,d\rho
 \le I(f).
\]

This does **not** yet identify `s(T)` with `|U|` or prove the needed operator bound. It does isolate an exact combinatorial mechanism with the right half-order scaling for that next comparison.

---

## 5. Genuine Boolean counterexample to ordinary orbit invariance

The stronger claim

> “after appending a dummy coordinate, the sum of the two ordinary fine-player Shapley entropy shares in each q-flip clone pair equals the old Shapley share”

is **REFUTED**.

Take the three-variable Boolean truth vector, indexed by `x0+2x1+4x2`,

\[
 (1,-1,1,-1,1,-1,-1,-1).
\tag{5.1}
\]

Its ordered-min active q-flip indices are `6` and `7`. The old entropy Shapley shares are

\[
 \phi_6=1,
 \qquad
 \phi_7=1.2169171866886992\ldots
\]

Append one dummy coordinate. The active fine q-flips are `6,7,14,15`, paired as `(6,14)` and `(7,15)`. Ordinary fine-player Shapley gives orbit aggregates

\[
 \Psi_6=1.4547869923250596\ldots,
 \qquad
 \Psi_7=0.7621301943636398\ldots.
\]

Hence

\[
 \Psi_6-\phi_6
 =+0.4547869923250596\ldots,
\qquad
 \Psi_7-\phi_7
 =-0.4547869923250594\ldots.
\tag{5.2}
\]

Total entropy is unchanged, exactly as (4.4) predicts, but the ordinary fine Shapley rule transfers a substantial signed amount between the two coarse q-flip orbits.

For this two-orbit example the transfer is already visible in third-order dividends. If the first orbit is `A={a,a'}` and the second `B={b,b'}`, global dummy-swap symmetry gives

\[
 \Psi_A-\Phi_A
 =\frac13\bigl(d(aa'b)-d(abb')\bigr),
\tag{5.3}
\]

with the opposite transfer to `B`. Numerically the two representative third dividends are

\[
 d(aa'b)=2.4338343733773984\ldots,
\qquad
 d(abb')=1.0694733964022198\ldots,
\]

which gives (5.2).

This counterexample kills the naive “ordinary Shapley automatically has universal dummy Ward invariance” shortcut. The coupled selector in Theorem 2.1 is the replacement.

---

## 6. What this buys for the signed FEI transport route

The exact compiler wants a selector that spends signed relation charge on genuine q-flip channels while preserving cancellation. The block-coupled rule has three features not simultaneously available in the previous ordinary fine-Shapley picture.

1. **Universal dummy invariance of the entropy side.** Any physically irrelevant appended coordinate only refines an old q-flip into clone cells; block coupling returns exactly the old entropy marginal, split equally across the cells.
2. **Exact signed parity reduction of the relation side.** Relation coordinates with even occupancy inside a coupled orbit contribute zero to that orbit; only odd orbit occupancy survives, with the original signed coefficient divided by the number of odd blocks.
3. **A quantified comparison back to ordinary Shapley.** If one needs the ordinary Shapley/plaquette representation, the difference is zero-sum higher curvature only, with coefficient `l2` norm at most `1/sqrt(8s)` at orbit support `s`. This removes first-order generator entropy from the discrepancy before any analytic estimate is attempted.

The R16 odd-moment/high-resolvent refunds and the terminal response have not been spent or modified here. The terminal Shapley share must be evaluated under the same coupled permutation law if this selector is inserted into the full bridge. Nothing in this report turns the terminal endpoint into cumulative variation.

### Remaining universal obligation

A complete FEI proof still needs a dimension-free estimate on the *genuinely interacting* mixed-orbit curvature after this exact selector cancellation. One must **not** return to the now-refuted basiswise pointwise q-flip bound. A precise next target is:

> For a translation/invariance orbit partition of the active ordered-min q-flips, use the block-coupled signed relation allocation (3.3) and prove that the residual higher-curvature transfer in (4.2)--(4.7), after grouping by the physical cut-Radon frequencies, is paid by a constant multiple of the midpoint fractional noisy-square bank plus the already-retained R16 and terminal ledgers.

The coefficient theorem (4.5) shows why the midpoint `sqrt(|U|)` bank is the natural first sink to test: the selector mismatch itself supplies an exact `1/sqrt{s}` factor. The missing mathematical map is from mixed q-flip-orbit support `s(T)` to the Fourier/noise-square frequency support without losing dimension.

**Full FEI remains OPEN / NOT PROVED.**

---

## 7. Executed decisive checks

`check_dummy_split_selector.py` was compiled with `python -m py_compile` and executed using only the Python standard library.

It passed:

* **80** generic paired cooperative games with exact `fractions.Fraction` arithmetic, verifying (4.2)--(4.5) and exact coupled block group conservation;
* **80** globally pair-swap-symmetric exact games, verifying that the coupled selector splits each coarse group share exactly in half between its two clones;
* **168** exact signed parity games, verifying Theorem 3.1 for both positive and negative coefficients;
* **all 256** Boolean functions on three variables, each extended by one dummy coordinate, verifying the q-flip clone structure, product identity (1.2), the Harsanyi refinement formula and total conservation;
* the explicit Boolean counterexample (5.1), with maximum observed orbit redistribution `0.4547869923250596` bits in that exhaustive `3 -> 4` test.

The maximum floating discrepancy in the entropy/Harsanyi identity sweep was `1.2212453270876722e-15`. The generic game and signed parity checks were exact rational arithmetic, not floating evidence.

Checker SHA-256:

`7ade7ce5a8323e74d0a152712844d4621d27026f7b270eb97e08e146e570d669`

Output SHA-256:

`80fc8e91ecfed2dddf7cc0d6d71b658cfae7750d418deed08a3f7f59879db1a1`

Finite computation is used here to falsify the stronger ordinary-Shapley claim and sanity-check formulas. Theorems 2.1, 3.1 and 4.1 are proved algebraically above and do not rely on finite enumeration.

## 8. Before / after

**Before:** exact signed q-flip transport and the Shapley--plaquette bridge existed, but the general dummy-coordinate cancellation was proved only on a transitive monomial-defect family. It was unknown whether ordinary Shapley had a universal orbitwise Ward identity.

**After:** ordinary Shapley orbit invariance is rigorously refuted by a genuine Boolean example. A replacement selector is proved: coupled block permutations have exact universal dummy invariance, exact signed parity/orbit allocation, and a closed-form higher-curvature comparison to ordinary Shapley with `1/sqrt(8s)` coefficient scale. The remaining difficulty is no longer the raw dummy baseline; it is the mixed third-and-higher curvature operator on genuinely interacting q-flip orbits.

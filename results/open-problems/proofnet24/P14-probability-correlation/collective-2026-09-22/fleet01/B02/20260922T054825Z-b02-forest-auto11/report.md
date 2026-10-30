# FOREST B02 — rank-homogenization refutation and a source-exact disconnecting switching interface

Run: `20260922T054825Z-b02-forest-auto11`  
Outcome: **CANDIDATE_REFUTED** for the rank-homogeneous strengthening in the latest lead version; the parent FOREST conjecture is **not** refuted and remains open.  
Context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh control and exact dependencies


The latest complete campaign-lead version consumed was fleet01/B01 `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, shared handoff blob `4cee205cb7d254caf785692838111988a0b8a155`, canonical report commit `79044b575c4b689248892f37b9930e983dddabca`. Its source-safe core is the triangle-free conditioning lemma; its new spectral strengthening replaces the ground-set homogenizing degree by graphic rank.

The required named OTHER-account partner consumed and applied was fleet02/B03 run `20260922T051049Z-b03-forest-auto11`, report blob `57bd1c4cceaa39ba9db44f4f024a3b9a4f41c65c`. That report proves exact rational two-terminal unitization and exact simple replacements for contraction-created parallel classes, with the Rayleigh gap multiplied only by a positive square factor. I use that result in Section 4 below to determine exactly what a global STAR-2 theorem would mean.

## 2. Decisive source correction: the lead's rank-degree CLC polynomial is false

The latest lead invokes

`h_M(y,z)=sum_{I independent} y^(R-|I|) z^I`,

where `R=rank(M)`, and asserts that this is the canonical completely-log-concave homogenization. That assertion is false.

The independent-set CLC theorem of Anari--Liu--Oveis Gharan--Vinzant is in *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv:1811.01600. In the introduction they take an **n-element ground set** and explicitly define

`g_M(y,z)=sum_{I independent} y^(n-|I|) z^I`.

The exponent is the ground-set size `n`, not the matroid rank. The rank-degree object used by the lead is obtained by dividing the source-valid ground-degree polynomial by a positive power of `y`; complete log-concavity is not preserved by that division.

There is a source-exact counterexample already on `K_3`. Its cycle matroid has ground-set size `n=3` and rank `R=2`. The rank-degree polynomial is

`h=y^2+y(z1+z2+z3)+z1 z2+z1 z3+z2 z3`.

At the all-ones point `h=7`. For variables `(y,z1,z2)`, the matrix

`grad(h) grad(h)^T - h Hess(h)`

is exactly

```
[11  8  8]
[ 8  9  2]
[ 8  2  9]
```

and has determinant **`-49`**. Equivalently the corresponding principal determinant of `-Hess log h` is `-1/2401`. Hence the rank-degree polynomial is not even log-concave at the all-ones point.

For comparison, the source-valid ground-degree homogenization on `K_3` is `g=y h`; its same raw principal matrix is

```
[60  8  8]
[ 8  9  2]
[ 8  2  9]
```

with determinant **`3724>0`**.

The lead's stated rank-slack consequences also fail numerically on this exact source graph. Under the uniform law on all seven forests of `K_3`,

`mu=9/7`, `v=Var(K)=24/49`, `p_e=3/7`, `c_e=Cov(X_e,K)=8/49`, `R=2`.

Its claimed rank version of (A2) gives

`v^2/(R-mu)+sum_h c_h^2/p_h = 128/245`,

whereas `v=24/49=120/245`; the claimed inequality fails by **`8/245`**. Likewise its derived variance bound

`v <= mu(R-mu)/R`

fails by exactly **`3/98`**. The claimed `(slack,e,f)` rank block is

`(1/49)*[[11,8,8],[8,9,2],[8,2,9]]`

and has determinant `-1/2401`.

Therefore the lead's rank-homogeneous Theorem A, including the derivation of its stronger `R-mu` spectral budget, cannot be used. This does **not** invalidate the triangle-free Simpson identity itself. A source-safe repair is to revert to the ground-set-degree `m-|F|` CLC polynomial and the weaker `m-mu` budget already derived in fleet02/B02. Any future use of the stronger `R-mu` edge-row inequality needs an independent proof; it cannot be justified by the rank-degree CLC assertion.

## 3. Source-exact reformulation of the STAR-2 debt without weights

Let `G` be a simple graph, let `g=uv` be an edge distinct from queried edges `e,f`, and put `H=G-g`. There is a literal bijection

`Phi : {forests F of G : g in F} -> {forests A of H : u and v are disconnected in A}`

by `Phi(F)=F-g`.

**Acyclicity and inverse.** If `F` is a forest containing `g`, then `u,v` cannot be joined in `F-g`, because such a path together with `g` would be a cycle. Conversely, if `A` is a forest of `H` with `u,v` disconnected, then `A+g` joins two different components and is a forest. Thus `A -> A+g` is the inverse. Presence of `e,f` is preserved exactly.

Consequently, the contraction/STAR-2 conditional law has an equivalent formulation entirely inside the smaller **simple** graph `H`:

> the conditional law given `g in F` is exactly the uniform forest law of `H` conditioned on `u` and `v` being disconnected.

If `u,v` have common neighbors, contraction identifies their two incident choices and produces the familiar weight-two star. The weight `2` is only the quotient multiplicity of the two colors; the disconnected-forest formulation retains those colors in the original simple graph.

Define `D_ij` to be the number of forests `A` of `H` such that `u` and `v` are disconnected and `(1_{e in A},1_{f in A})=(i,j)`. The exact unpaid STAR-2 comparison is therefore

`D_10 D_01 >= D_00 D_11`.                                      (3.1)

This is the clean forest-pair injection target for B02. It has no surrogate rooted law, no fixed-size restriction, and no arbitrary external field.

## 4. Applying fleet02/B03: global STAR-2 is parent-equivalent

The partner's exact rational unitizer gives one direction immediately. Any `{1,2}`-weighted star instance can be regarded as a star of size-two parallel classes; fleet02/B03 replaces every unmarked or singly-marked class by finite unit simple terminal networks and proves

`Delta_simple = kappa^2 Delta_STAR2`

for an explicit `kappa>0` (with the same-class queried case trivial). Therefore, if the source unit FOREST theorem held for every finite simple graph, every global STAR-2 instance would follow.

Conversely, a theorem asserting STAR-2 for **all** simple graphs would already imply the source conjecture. Given any unit graph `G` and queried pair `e,f`, attach one new pendant edge `h` and give only `h` weight `2`. Since `h` is a bridge, every forest of `G` independently either omits it with weight `1` or includes it with weight `2`. Hence

`Z'=3Z`, `Z'_e=3Z_e`, `Z'_f=3Z_f`, `Z'_{ef}=3Z_{ef}`,

so

`Delta'_{ef}=9 Delta_{ef}`.

The doubled set consists of a single star edge. Thus global STAR-2 and the parent source conjecture are equivalent (the partner proves the nontrivial weighted-to-unit direction exactly).

This sharpens the lead's localization: the useful missing statement must retain the **edge-minimal-counterexample antecedent** and the fact that the weighted graph is the contraction stratum of that specific counterexample. A stand-alone universal STAR-2 lemma is not a smaller bridge.

The correct minimality-conditioned target is:

> **MIN-STAR2 / DISCONNECT gate.** If `G` is an edge-minimal unit simple counterexample with violating pair `e,f`, and `g=uv` is a triangle edge distinct from `e,f`, then in `H=G-g` the pair `e,f` is nonpositively correlated under the uniform forest law conditioned on `u` and `v` being disconnected; equivalently (3.1) holds.

This is exactly the implication needed to make the lead's total-covariance Simpson step source-safe for a triangle conditioner.

## 5. A genuine multiplicity-one disconnecting exchange

The disconnect formulation exposes a useful switching that was hidden by the weight-two quotient.

Let `F` be a forest of `H` with `u,v` disconnected. Let `x` be an edge not in `F` such that `F+x` connects `u` to `v`. Then the endpoints of `x` lie in the two relevant components of `F`, so `F+x` is acyclic and has a unique `u-v` path `P`. For any marked edge `h in P-{x}`, set

`F' = F + x - h`.

Then:

1. `F'` is a forest, because it is obtained from the tree `F+x` by deleting one edge;
2. `u,v` are disconnected in `F'`, because `h` lies on the unique `u-v` path;
3. the marked transformation

`(F; x,h) <-> (F'; h,x)`

is an involution with multiplicity exactly one.

Indeed adding `h` back to `F'` restores `F+x`, and deleting `x` then restores `F`; the same unique path certifies the reverse move. Thus acyclicity, preservation of the disconnect event, and the inverse are all explicit rather than assumed.

This is not yet an unmarked injection `D_00 x D_11 -> D_10 x D_01`: the remaining combinatorial debt is to choose/charge the repair edge `h` during the e/f transfer so that the marked-path multiplicities cancel. But it supplies a concrete, reversible repair operation for exactly the failure mode that ordinary forest exchanges have under the disconnect conditioning.

## 6. Algebra-only STAR-2 inference is insufficient

There is also an exact finite count witness showing why scalar endpoint signs alone cannot pay MIN-STAR2. Consider formal three-bit strata for `(e,f,g)` with counts

```
          ef=00  10  01  11
g=0          4   7   9   9
g=1          6   4   0   0
```

The `e,f` Rayleigh polynomial as the activity of `g` is changed is

`Delta_ef(t)=27-18 t`.

Thus deletion gives `Delta_ef(0)=27`, the unit point gives `Delta_ef(1)=9`, and the `g=1` endpoint gap is `0`, while doubling gives `Delta_ef(2)=-9`. At the unit point the other pair gaps are also nonnegative:

`Delta_eg=44`, `Delta_fg=180`.

So the signs of the deletion gap, contraction endpoint, and all three unit pair gaps do not algebraically imply safety at activity two. This table is **not** claimed to be graph-realizable and hence is not a source counterexample; its role is to refute a proof mechanism that uses only those scalar inequalities. Graphic realizability and an actual switching such as Section 5 are indispensable.

## 7. Compact corrected end-to-end chain

The source-safe chain after this audit is:

1. choose an edge-minimal simple counterexample `G` and violating pair `e,f`;
2. use the source-valid **ground-set-degree** CLC budget (`m-mu`, not `R-mu`);
3. for every triangle-free third edge, deletion and contraction are smaller simple source instances, so the lead's exact total-covariance Simpson inequality remains valid;
4. for a triangle conditioner `g=uv`, replace the weight-two quotient by the exact simple-graph disconnect formulation (3.1);
5. prove MIN-STAR2 by a bounded-multiplicity forest-pair switching that preserves `u not connected v`; the marked disconnecting exchange in Section 5 is a reversible repair primitive;
6. only after this gate is paid can the all-conditioner Simpson constraints be combined with the spectral budget to seek a global contradiction.

The first essential missing implication is therefore **(3.1) under the edge-minimal-counterexample antecedent**, not universal STAR-2. A proof using only rank-homogeneous CLC or scalar endpoint signs is invalidated above.

## 8. Exact computation

`audit_switching_checker.py` checks the K3 source counterexample to rank homogenization and the formal STAR-2 scalar witness with exact `Fraction` arithmetic. It returns:

- rank-degree K3 raw principal determinant `-49`;
- ground-degree K3 raw principal determinant `3724`;
- rank-A2 excess `8/245`;
- rank variance-bound excess `3/98`;
- abstract `Delta(t)=27-18t`, with values `27,9,-9` at `t=0,1,2`;
- unit pair gaps `(ef,eg,fg)=(9,44,180)`;
- `STATUS=PASS`.

No finite computation is extrapolated into the all-graphs theorem.

## 9. Status

**Outcome: `CANDIDATE_REFUTED`** for the lead's rank-homogeneous strengthening as stated. The source conjecture remains open. The triangle-free Simpson conditioning part survives; the safe spectral replacement uses ground-set degree. The new exact target is the minimality-conditioned disconnect injection (3.1), with a proved multiplicity-one path-repair involution available for the next switching construction.

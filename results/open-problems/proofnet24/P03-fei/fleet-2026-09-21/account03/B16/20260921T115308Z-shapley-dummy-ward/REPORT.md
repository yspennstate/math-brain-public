# B16 FEI signed transport: a dummy-coordinate Ward identity for the Shapley curvature bank

**Date:** 21 September 2026  
**Scope:** `account03 / B16`, FEI signed transport proof  
**Brain label:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact proved identities for a diagnostic Boolean family; no publication-priority claim.

## 0. Route and entering obstruction

This run follows the owner-required creative FEI order and does not audit the read-once certificate. It consumes the exact signed R32/T-join transport state, the Shapley--plaquette identity from the newer B16 handoff, and the newest coordinate-noise/Radon calculation.

The live obstruction from the latter is concrete. For the random ordered-min q-flip basis, the raw generator-entropy displacement kernel has fixed-weight Walsh multiplier

\[
 A_{n,r}=\frac1n\sum_{c=2}^n H_c
 \left[2^{c-1}\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}-1\right]
 =\frac{4n}{(r+1)(r+2)}+O_r(1),
\]

so centering alone still loses a factor `n`. The embedded two-variable parity-switch function realizes the bad singleton mode. The previous report therefore asked whether the **signed Shapley curvature refund**, not just centering, cancels that low-mode growth.

This run answers that diagnostic exactly: **yes, for the entire dummy-extended parity-switch family, and in fact for every Walsh weight at once.** The cancellation is forced by a translation symmetry of the Shapley game. It is a genuine signed-refund calculation, not an absolute-value estimate. It does not yet prove the corresponding universal operator bound for arbitrary Boolean functions, so full FEI stays OPEN.

The terminal Shapley bank `Theta` and the inherited R16 moment refunds are deliberately not spent here. They remain separate exactly as in the existing compiler ledger.

---

## 1. Ordered-min q-flips for a codimension-k defect

Fix a coordinate order. In `F_2` notation let

\[
 q_A(x)=\prod_{j\in A}x_j,
 \qquad f_A(x)=(-1)^{q_A(x)},
 \qquad |A|=k\ge2.
\]

Thus `f_A=-1` precisely on one codimension-`k` face. Let `p` be the earliest coordinate of `A` in the order, let its rank be `r_0`, and put

\[
 c=n-r_0+1.
\]

For the ordered-min relation basis, the q-flip syndrome exponent is

\[
 b_v=q_A(v)+q_A(v+e_{i(v)}),
\]

where `i(v)` is the earliest coordinate in `supp(v)`.

### Theorem 1.1 — `B16-MONOMIAL-QFLIP-PARTITION` — PROVED

One has `b_v=1` exactly when

1. `i(v)=p`, and
2. `A\setminus\{p\}\subseteq supp(v)`.

Consequently the active generator set `M` has

\[
 |M|=2^{c-k}.
\]

The corresponding dual generators `g_v` are pairwise disjoint codimension-`c` subcube defects, and their negative cells partition the negative codimension-`k` face of `f_A`. Hence

\[
 \boxed{f_A=\prod_{v\in M}g_v.}\tag{1.1}
\]

### Proof

If `i(v)<p`, toggling `i(v)` does not change the monomial. If `i(v)>p`, then `p` is absent from `v` (otherwise `i(v)` would not be the earliest support coordinate), so both monomial values are zero. Thus only `i(v)=p` can contribute. In that case toggling `p` changes the monomial iff every other active coordinate is present, proving the syndrome characterization. The `c-k` later coordinates outside `A` are free, giving `2^{c-k}` active q-flips.

The ordered-min dual-generator theorem from the inherited Shapley handoff says that `g_v` is negative precisely on the descendant cell fixing all coordinates from `p` onward according to `v`, with earlier coordinates free. Distinct assignments of the `c-k` later dummy coordinates give disjoint cells, and their union is exactly the face `x_j=1` for every `j in A`. Multiplying their signs gives (1.1). `square`

---

## 2. Shapley symmetry forces the exact curvature refund

Let spectral entropy in bits be `E`. On the active player set `M` define

\[
 G(S)=E\left(\prod_{v\in S}g_v\right).
\]

Let `D` be the set of the `c-k` coordinates later than `p` but outside `A`. Translation by any vector supported on `D` permutes the active cells regularly and transitively. It also leaves `f_A` invariant. Input translation changes Walsh coefficients only by signs, so it preserves spectral entropy. Therefore the cooperative game `G` is transitive on its players.

### Theorem 2.1 — `B16-SHAPLEY-DUMMY-WARD` — PROVED

For every `v in M`,

\[
 \boxed{\phi_v(E)=\frac{E(f_A)}{|M|}=E(f_A)2^{k-c}.}\tag{2.1}
\]

If `H_j` denotes the spectral entropy of one codimension-`j` subcube defect, then `E(g_v)=H_c` and the inherited exact Shapley--plaquette identity

\[
 \phi_v(E)=E(g_v)-\mathcal C_v^M
\]

gives the exact curvature refund

\[
 \boxed{\mathcal C_v^M=H_c-H_k2^{k-c}.}\tag{2.2}
\]

Equivalently, after the full entropy-curvature refund but **before** the separate terminal Shapley share,

\[
 \boxed{E(g_v)-\mathcal C_v^M=H_k2^{k-c}.}\tag{2.3}
\]

### Proof

The translation group supported on `D` acts transitively on `M` and is an automorphism of `G`. By the symmetry axiom of the Shapley value, all `phi_v(G)` are equal. By Shapley efficiency,

\[
 \sum_{v\in M}\phi_v(G)=G(M)-G(\varnothing)=E(f_A),
\]

using (1.1) and `E(1)=0`. Division by `|M|=2^{c-k}` gives (2.1). The exact inherited identity `phi_v(E)=E(g_v)-C_v^M` then gives (2.2)--(2.3). `square`

### Meaning

The raw generator entropy has asymptotic size `H_c ~ 8c2^{-c}` bits, so its factor `c` was exactly what produced the ambient-dimension low-mode growth. On this family the signed curvature bank removes that factor **exactly**: for fixed `k`, the paid entropy share is `H_k 2^{k-c}=O_k(2^{-c})`.

This is a Ward identity for dummy-coordinate invariance: adding coordinates on which the Boolean function does not depend cannot leave a growing entropy charge after the exact Shapley curvature telescope.

---

## 3. Exact cancellation of the parity-switch low-mode obstruction

Now specialize to `k=2`, the same two-variable parity-switch/one-corner defect used to refute the centered raw kernel. Here

\[
 H_2=2\quad\text{bits},
\]

so (2.3) gives the exact refunded player charge

\[
 \widetilde H_c=\frac{2}{2^{c-2}}=2^{3-c}.\tag{3.1}
\]

Replace `H_c` by this **proved Shapley entropy marginal** in the random-order displacement-multiplier calculation. For a Walsh frequency of weight `r`, define

\[
 \widetilde A_{n,r}
 =\frac1n\sum_{c=2}^n2^{3-c}
 \left[2^{c-1}
 \frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}-1\right].\tag{3.2}
\]

### Theorem 3.1 — `B16-REFUNDED-PARITYSWITCH-MULTIPLIER` — PROVED

For every `n>=2` and `1<=r<=n-1`,

\[
 \boxed{
 \widetilde A_{n,r}
 =\frac4{r+1}-\frac{8-2^{3-n}}{n}.}
 \tag{3.3}
\]

In particular,

\[
 \boxed{\sup_{n\ge2}\sup_{1\le r\le n-1}|\widetilde A_{n,r}|\le2.}\tag{3.4}
\]

For the formerly bad singleton mode,

\[
 \widetilde A_{n,1}=2-\frac{8-2^{3-n}}n\longrightarrow2,
\]

whereas the raw multiplier satisfies `A_{n,1}=(2/3)n+O(1)`.

### Proof

Write

\[
 R_{n,r,c}=\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}
 =\frac{\binom{n-c}{r}}{\binom{n-1}{r}}.
\]

The hockey-stick identity gives

\[
 \sum_{c=2}^nR_{n,r,c}
 =\frac{\binom{n-1}{r+1}}{\binom{n-1}{r}}
 =\frac{n-r-1}{r+1}=\frac n{r+1}-1.\tag{3.5}
\]

Also

\[
 \sum_{c=2}^n2^{3-c}=4-2^{3-n}.\tag{3.6}
\]

Since `2^{3-c}2^{c-1}=4`, substitution of (3.5)--(3.6) into (3.2) gives (3.3). The first term in (3.3) lies in `(0,2]`; direct endpoint comparison gives (3.4). `square`

Thus the exact Shapley curvature refund eliminates not only the previously observed singleton divergence but **all** Walsh-weight divergences of this diagnostic entropy kernel at once.

---

## 4. Numbers and attempted refutation

A standard-library checker independently evaluated the finite Shapley game for the parity-switch defect through `c=5` and checked the exact multiplier formula for every `(n,r)` with `2<=n<=100`.

Small Shapley games:

| c | active players | full entropy | each Shapley entropy share | raw generator entropy | curvature refund |
|---:|---:|---:|---:|---:|---:|
|2|1|2|2|2|0|
|3|2|2|1|2.216917186689|1.216917186689|
|4|4|2|0.5|1.701237775599|1.201237775599|
|5|8|2|0.25|1.132418874907|0.882418874907|

For the first three Walsh weights, the raw versus refunded multipliers were:

| n | raw r=1 | refunded r=1 | raw r=2 | refunded r=2 | raw r=3 | refunded r=3 |
|---:|---:|---:|---:|---:|---:|---:|
|10|5.052044993087|1.20078125|1.718072839117|0.534114583333|0.452462479720|0.20078125|
|20|12.517741944303|1.600000381470|5.748281523121|0.933333714803|3.079489597458|0.600000381470|
|40|26.299930950032|1.800000000000|12.831006936345|1.133333333334|7.468337111252|0.800000000000|
|80|53.052992914408|1.900000000000|26.359780511365|1.233333333333|15.679250249284|0.9|

The exact all-mode sweep covered **4,950** `(n,r)` pairs through `n=100`; all matched (3.3) exactly as rational numbers and all satisfied the bound `<=2` in absolute value. The maximum absolute value in that finite range was `1.92` at `(n,r)=(100,1)`, moving monotonically toward the proved limiting value `2` rather than growing with dimension.

**Attempted refutation:** the first obvious way to kill the Ward identity is to find two active dummy cells with unequal Shapley entropy shares. Exhaustive Shapley evaluation through eight active cells found none, as predicted by the exact translation action. The second way is a hidden higher Walsh mode whose refunded multiplier regains dimension growth. The exact formula (3.3), not merely the finite sweep, rules this out for every mode of this parity-switch diagnostic.

The checker SHA-256 for the locally executed bytes was `2815084c3ae6e98fc4d55f22ce6f4a9180183cd2a19606b1a1245e0fef7b91e3`; the committed source must still be identified by Git readback independently.

---

## 5. What this does and does not pay

**PROVED:** on the dummy-extended codimension-`k` monomial defect, the exact Shapley curvature bank changes every active q-flip entropy charge from the raw `H_c` to the dimensionally correct `H_k2^{k-c}`. For the exact parity-switch family that exposed the `Theta(n)` raw-kernel failure, every refunded entropy Walsh multiplier is bounded by `2` uniformly in `n` and `r`.

**PRESERVED / NOT SPENT:**

- negative R32 `2 mod 4` entropy credits;
- exact dual-code multiplicities;
- original-coordinate q-flip geometry;
- R16 odd-moment/high-resolvent refunds;
- the terminal response `R_d` and its separate one-sided terminal-band payment.

**OPEN:** the universal analogue for an arbitrary Boolean active q-flip set. The proof above uses a transitive dummy-translation orbit. General functions have several interacting active orbits, and the signed curvature Shapley share can depend on the prefix state. No universal dimension-free multiplier theorem is claimed.

**FULL FEI:** OPEN / NOT PROVED.

---

## 6. Next attack

The next B16 step should exploit the mechanism rather than re-run this diagnostic:

> Decompose the active ordered-min q-flip game into orbits under translations by coordinates on which the relevant local quotient is invariant. Prove an orbitwise Shapley/Ward identity that subtracts the entire dummy-coordinate low-frequency component of the entropy kernel. Then show that the remaining non-invariant high-frequency component is controlled by the already-proved fractional noisy-square bank, while keeping the terminal Shapley share and R16 moment refunds in their existing separate ledgers.

A decisive target is a universal decomposition

\[
 \widehat R_i(U)=\widehat R_i^{\rm Ward}(U)+\widehat R_i^{\rm high}(U),
\]

where the Ward term has a dimension-free multiplier bound by exact Shapley symmetry and the high term carries a positive power of `|U|` or a coordinate derivative that the inherited fractional-resolvent estimate already pays. A Boolean family with no such orbitwise cancellation would refute this continuation and force a genuinely different signed transport route.

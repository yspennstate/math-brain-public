# FOREST / fleet03 B03 — split-graph obstruction to any uniform sign-cluster slack

Run: `20260922T002444Z-b03-forest-r11`  
Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` / FOREST  
Outcome: **AUXILIARY_ONLY / STRUCTURAL_CONSTRAINT_PROVED**. The Grimmett–Winkler uniform-forest conjecture remains OPEN.

## 1. Source-exact target and consumed cross-account result

For a finite simple graph `G`, let

\[
Z=\#\{F\subseteq E(G):F\text{ is acyclic}\},
\qquad
Z_S=\#\{F:F\text{ is acyclic and }S\subseteq F\}.
\]

For distinct edges `a,b`, write

\[
\Delta(a,b)=Z_aZ_b-ZZ_{ab}.
\]

The source target is `Delta(a,b)>=0` for every pair in every finite simple graph.

This run directly consumes the completed other-account result

`proofnet24/P14-probability-correlation/collective-2026-09-22/fleet04/B01/b01-20260922T001208Z-forest-r11/report.md`

(blob `d5faa9e572e9fa67b736693a7f1a9d5205764b3c`). That report proves exact multi-bridge two-separator transfer and therefore localizes any lexicographically minimal counterexample to a **3-connected** simple graph. It also combines the current reconnection identity with the fleet03/B02 deletion/contraction constraints, so the first unpaid universal step is no longer separator bookkeeping: one must rule out a 3-connected pair whose reconnection excess is positive while the sign-coherence constraints hold for every third edge.

The exact fleet03/B02 identity used below is, for distinct `e,f,g`,

\[
AB\,\Delta(e,f)
=Z(BD_0+AD_1)-\Delta(g,e)\Delta(g,f),
\tag{1.1}
\]

where

\[
A=Z-Z_g,\quad B=Z_g,
\]

\[
D_0=(Z_e-Z_{eg})(Z_f-Z_{fg})-(Z-Z_g)(Z_{ef}-Z_{efg}),
\tag{1.2}
\]

and

\[
D_1=Z_{eg}Z_{fg}-Z_gZ_{efg}.
\tag{1.3}
\]

In a lexicographically minimal counterexample the deletion and contraction strata give `D_0,D_1>=0`. Thus, whenever `Z(BD_0+AD_1)>0`, define the exact Simpson/sign-cluster ratio

\[
R_G(e,f;g)
:=\frac{\Delta(g,e)\Delta(g,f)}{Z(BD_0+AD_1)}.
\tag{1.4}
\]

Then (1.1) gives

\[
1-R_G(e,f;g)
=\frac{AB\,\Delta(e,f)}{Z(BD_0+AD_1)}.
\tag{1.5}
\]

So the desired sign is equivalent to `R<=1` when the denominator is positive. A tempting quantitative strengthening is to seek a fixed `epsilon>0` with `R<=1-epsilon` on the surviving 3-connected obstruction. The family below proves that **no such graph-independent epsilon can exist**.

## 2. Structured 3-connected family

For integers `r>=3`, `m>=1`, let

\[
S_{r,m}=K_r\vee \overline{K_m}.
\]

Call the `K_r` vertices the terminals `0,1,...,r-1` and the independent vertices the star centers `s_1,...,s_m`. Every star center is adjacent to every terminal. Mark

\[
e=\{0,1\},\qquad
f=\{s_1,2\},\qquad
g=\{s_1,0\}.
\tag{2.1}
\]

These are distinct for `r>=3`.

`S_{r,m}` is 3-connected. Indeed, after deleting fewer than three vertices, at least one of the `r>=3` clique terminals remains; that vertex is adjacent to every surviving star center and to every surviving terminal. Hence the remaining graph is connected. (For `m>=2` its vertex connectivity is in fact `r`; that stronger fact is not needed.)

This is therefore a source-valid structured adversary to any proposed **uniform quantitative** strengthening of the current 3-connected sign-cluster step.

## 3. Exact transfer-polynomial lemma

Put

\[
n=m-1,\qquad q=r+1.
\]

Process the clique and the marked center `s_1` first, then the `n` unmarked star centers. A forest induces a partition of the terminal set. An unmarked star center has exactly `q` partition-preserving choices: select no spoke, or select exactly one of its `r` spokes. Any choice of at least two spokes is admissible exactly when the selected terminals currently lie in distinct components; it then merges those components.

Fix a forest in the clique plus `s_1`, and suppose its terminal components have sizes

\[
s_1,\ldots,s_c,\qquad \sum_i s_i=r.
\]

Let `T(s)` be the number of ways to complete those components to one terminal component using pair-merging ordinary stars, ignoring the choice of which ordinary centers perform the merges. Contracting the fixed components turns this into the weighted Cayley tree count with edge weight `s_i s_j`, hence

\[
T(s)=r^{c-2}\prod_{i=1}^c s_i.
\tag{3.1}
\]

Let `U(s)` denote the corresponding finite count with exactly `c-2` active ordinary centers. It consists of the two possibilities relevant at that degree: all active centers use two spokes and leave two terminal components, or one active center uses three spokes and the remaining active centers use two spokes and finish connected. Its closed form will not be needed.

After dividing the count by `q^n`, the contribution of this fixed front forest is a polynomial in `n`, and its two highest coefficients are

\[
\frac{T(s)}{q^{c-1}}n^{c-1}
+
\left[
\frac{U(s)}{q^{c-2}}
-\binom{c-1}{2}\frac{T(s)}{q^{c-1}}
\right]n^{c-2}
+O(n^{c-3}).
\tag{3.2}
\]

Proof: choose the active ordinary centers. The `c-1` active-center term can only consist of pair merges and is a spanning-tree completion, giving `T(s)`. The falling factorial `(n)_{c-1}` has second coefficient `-binom(c-1,2)`. With only `c-2` active centers, an acyclic terminal hyperforest can lose the required `c-1` terminal components only by the two cases included in `U(s)`. All lower active-center counts contribute only `O(n^{c-3})`. This proves (3.2).

For the component types needed here,

\[
T(1^r)=r^{r-2},\quad
T(2,1^{r-2})=2r^{r-3},\quad
T(3,1^{r-3})=3r^{r-4},\quad
T(2,2,1^{r-4})=4r^{r-4}.
\tag{3.3}
\]

## 4. Front-rank classification

The top two degrees of all joint counts needed in (1.1) require only the minimum-rank front forests and those of one additional terminal rank. The complete classification is:

| count | minimum component type | number of minimum fronts | next-rank `(3,1,...)` fronts | next-rank `(2,2,1,...)` fronts |
|---|---|---:|---:|---:|
| `Z` | `1^r` | `q` | `C(r,2)(q+1)` pair-type fronts total | — |
| `Z_f=Z_g` | `1^r` | `1` | `C(r,2)+(r-1)` pair-type fronts total | — |
| `Z_e` | `(2,1,...)` | `q` | `2(r-2)(q+1)` | `C(r-2,2)(q+1)` |
| `Z_ef` | `(2,1,...)` | `1` | `2(r-1)` | `r(r-3)/2` |
| `Z_eg` | `(2,1,...)` | `1` | `3(r-2)` | `C(r-2,2)` |
| `Z_fg` | `(2,1,...)` | `1` | `3(r-2)` | `C(r-2,2)` |
| `Z_efg` | `(3,1,...)` | `1` | not needed | not needed |

Here “pair-type fronts total” in the first two rows means that the one additional rank produces component type `(2,1,...)`; the split into clique-edge and marked-star origins is irrelevant because (3.1) depends only on component sizes.

For example, with `e` present, a minimum front is just the core edge `01` together with one of the `q` partition-preserving marked-star choices. At one additional rank, the new connection either enlarges that component to size three or creates a disjoint size-two component, giving the two counts displayed above. With `e,f,g` all present, the core edge `01` and the two-spoke path `0-s_1-2` already form one size-three terminal component.

Substituting this classification into (3.2) is enough. The unknown quantities `U(1^r)` and `U(2,1^{r-2})` cancel from every leading Rayleigh coefficient below; no unproved closed form for them is being assumed.

## 5. Leading exact gaps

Define

\[
c_r=\left(\frac{r}{r+1}\right)^{r-2}.
\tag{5.1}
\]

Direct substitution of §4 into §3 and cancellation of the common `U` terms gives, as `n=m-1\to\infty` with fixed `r`,

\[
Z=c_r n^{r-1}+O(n^{r-2}),
\tag{5.2}
\]

\[
A=\frac{r}{r+1}c_r n^{r-1}+O(n^{r-2}),
\qquad
B=\frac{1}{r+1}c_r n^{r-1}+O(n^{r-2}),
\tag{5.3}
\]

and

\[
D_0=\frac{2c_r^2}{r^2}n^{2r-4}+O(n^{2r-5}),
\qquad
D_1=\frac{c_r^2}{r^2}n^{2r-4}+O(n^{2r-5}),
\tag{5.4}
\]

\[
\Delta(g,e)
=\frac{r^2+r+2}{r^2}c_r^2 n^{2r-4}+O(n^{2r-5}),
\tag{5.5}
\]

\[
\Delta(g,f)
=\frac{c_r^2}{(r+1)^2}n^{2r-2}+O(n^{2r-3}),
\tag{5.6}
\]

\[
\Delta(e,f)
=\frac{2c_r^2}{r^2}n^{2r-4}+O(n^{2r-5}).
\tag{5.7}
\]

For transparency, two of these coefficients need no second-order cancellation at all. From the leading front counts,

\[
\operatorname{LC}(D_1)
=\left(\frac{2c_r}{r}\right)^2
-\frac{c_r}{r+1}\frac{3(r+1)c_r}{r^2}
=\frac{c_r^2}{r^2},
\]

and `Z_f Z_g` has degree `2r-2` whereas `Z Z_fg` has degree only `2r-3`, giving (5.6). For `D_0`, `Delta(g,e)` and `Delta(e,f)`, the nominal highest terms cancel; the one-rank-higher front table of §4 supplies the displayed next coefficient, with both `U` terms cancelling algebraically.

In particular, for each fixed `r>=3`, all quantities in the denominator of (1.4) are positive for all sufficiently large `m`.

## 6. No graph-independent multiplicative slack

Combining (5.2)–(5.6),

\[
\operatorname{LC}\bigl(\Delta(g,e)\Delta(g,f)\bigr)
=
\frac{r^2+r+2}{r^2(r+1)^2}c_r^4,
\]

while

\[
\operatorname{LC}\bigl(Z(BD_0+AD_1)\bigr)
=
\frac{r+2}{r^2(r+1)}c_r^4.
\]

Therefore

\[
\boxed{
\lim_{m\to\infty}R_{S_{r,m}}(e,f;g)
=
L_r
:=\frac{r^2+r+2}{(r+1)(r+2)}.
}
\tag{6.1}
\]

Equivalently,

\[
\boxed{
1-L_r=\frac{2r}{(r+1)(r+2)}\longrightarrow0.
}
\tag{6.2}
\]

### Corollary `FOREST-NO-UNIFORM-SIGNCLUSTER-SLACK-20260922`

There is **no** constant `epsilon>0` such that every 3-connected finite simple graph and every distinct triple with positive denominator in (1.4) satisfies

\[
\Delta(g,e)\Delta(g,f)
\le (1-\epsilon) Z(BD_0+AD_1).
\tag{6.3}
\]

Proof: choose `r` so large that `1-L_r<epsilon/2`, then choose `m` so large that the ratio in (6.1) differs from `L_r` by less than `epsilon/2`.

This does **not** refute the exact sign target `R<=1`. It proves that the current minimal-counterexample strategy cannot be completed by a graph-independent multiplicative reserve below one. Any successful use of (1.1) must exploit additional graph-local structure, or prove the sign at a scale whose slack is allowed to collapse with structural complexity.

## 7. Exact computation

A standard-library exact checker is stored beside this report. It uses terminal-partition dynamic programming, exact `Fraction` arithmetic, and finite-difference polynomial interpolation. For each `r=3,4,5,6,7` it reconstructs the normalized joint-count polynomials exactly and verifies the five leading coefficients (5.4)–(5.7), the exact deletion/contraction identity, and the limit (6.1).

The exact limits checked are

- `r=3`: `7/10`;
- `r=4`: `11/15`;
- `r=5`: `16/21`;
- `r=6`: `11/14`;
- `r=7`: `29/36`.

At `m=100` the corresponding exact-polynomial ratios are approximately

`0.68976649, 0.72146664, 0.74886773, 0.77181037, 0.79098794`,

converging upward to the displayed limits in these checks. The computation is corroboration of the analytic coefficient derivation, not a substitute for it.

## 8. Consequence for the collective proof search

The partner’s multi-bridge theorem has paid the separator cases; fleet03/B02 has paid the exact deletion/contraction sign-coherence identity. This run now removes a further tempting shortcut:

> The 3-connected obstruction cannot be ruled out merely by proving a **uniform quantitative gap** in the sign-coherence/Simpson ratio.

The next useful target should retain the exact sign `R<=1` but make the bound depend on structural data that sees the `K_r` core / many-star regime, or should derive a contradiction from the **simultaneous** inequalities over all third edges `g` rather than bounding each triple independently by a fixed margin.

A particularly concrete next question is whether summing the exact identities (1.1) over all `g` in a bad-pair equivalence class and its complement yields a graph-dependent conservation law that survives the `S_{r,m}` regression. The present family should be mandatory regression data for any such proposal.

## 9. Scope and claim discipline

- Parent FOREST conjecture: **OPEN**.
- This report proves only the no-uniform-slack structural corollary above and the exact asymptotic coefficient formulas for the displayed split family.
- It does not claim that every pair in `S_{r,m}` has been proved negatively correlated here.
- It does not claim novelty or publication priority for the split-graph asymptotic; external novelty is **UNVERIFIED**.
- No brain/native-memory assistance was used; status is `WITHOUT_VERIFIED_BRAIN`.

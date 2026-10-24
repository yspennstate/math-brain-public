Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-08 / T07 — independent-terminal response-strip closure and linear-forest order-11 theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and substantive move

The preceding NM13-08 run proved unit pairwise negative edge correlation for the independent-terminal repeated-`P7` family

\[
K_{3,7p+r}+\bigl(pP_7\sqcup rK_1\bigr),\qquad p,r\ge0,
\]

and sharpened the path-layer transfer recurrence. The newest companion NM13-04 run then changed method and proved a **triangle-seeded response-strip theorem** for

\[
K_3\vee H,
\]

where `H` is any linear forest whose components have order at most seven. That companion theorem is not copied here.

This run imports only the reusable algebraic idea and applies it to the **different seed with three independent terminals**. It also pushes the local path order from seven through eleven. The result is one 11-parameter theorem for arbitrary mixtures of `P_1,...,P_11`, not another fixed-path-length calculation.

The core new closure lemma is seed-independent: normalized terminal-symmetric layers with responses `I+aN+cN^2`, `N^3=0`, collapse under arbitrary products to a two-dimensional strip parameterized by a weighted average of one scalar `rho=(a^2/2-c)/a`. The independent-terminal seed then has a distinct local sign cone. Exact orbit reduction and strip positivity prove the application below.

Essential dependencies read: `operations/PROGRESS20_2026-09-20.md`, `POSTED.md`, the preceding NM13-08 `P7` report, the newest NM13-04 response-strip report, and the preserved P14/HARD10 finite-order/3-connected handoff. No historical or peer file was edited.

## 1. Parent theorem before/after, separately from demonstrated mechanism gain

For a finite graph `G=(V,E)`, define the spanning-forest generating polynomial

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\]

and for distinct present edges `e,f`

\[
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of `e,f` under the uniform measure on **all** spanning forests, with all component counts mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No complete-order metric moves in this run.

**Mechanism before:** independent-terminal fixed-length repeated path families through `P7` plus singleton layers; companion NM13-04 had a triangle-seeded arbitrary mixture theorem through component order seven.

**Mechanism after:** one response-strip closure for arbitrary mixtures plus a complete independent-terminal sign theorem for every right linear forest whose components have order at most **eleven**. The component multiplicities are all independent and unbounded.

## 2. Recovered P14 and exact source scope

The preserved source/repository boundaries are unchanged.

1. **Grimmett–Winkler, arXiv:math/0302185 / RSA 24 (2004).** Their conjecture concerns the uniform law on **all forests**. Their published computation verifies pairwise edge negative correlation for every graph with at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree theorem.
2. **P14/HARD10 dense-nine completion.** Repository exact computation covers the complementary 19--36-edge nine-vertex sector, so all 274,668 unlabeled simple graphs on nine vertices are covered in the source unit-weight scope. The dense sector has 120,314 unlabeled graphs and 25,304,635 present-edge pairs in the recorded exact audit.
3. **P14 structural reduction.** Forest factorization over blocks reduces a vertex-minimal source counterexample to a 2-connected graph. P14's two-separator transfer, together with its recovered fixed-graph weighted implication, reduces a vertex-minimal source counterexample further to a **3-connected** graph. This is a reduction, not a proof of the conjecture.
4. **P14 failed generic routes remain failed.** The degree-three apex/star-mesh attack leaves a mixed three-terminal polarization without a universal sign; the reverse-Cauchy rescue was exactly refuted on a physical example even though the true Rayleigh gap there remained positive. Naive real-stability/Lorentzian shortcuts still lack the needed hypothesis for arbitrary graphic independence polynomials.
5. **Erickson, arXiv:1008.3660.** Erickson proves a stronger all-positive-weight SOS/Rayleigh theorem for **series-parallel** graphs. The class proved below contains `K_{3,3}` whenever the right side has at least three vertices, hence lies outside that class.
6. **Huang, arXiv:2311.00965.** The general arboreal-gas negative-correlation problem is still described as open while restricted graphs/parameters are treated.
7. **Bado, DOI 10.1016/j.spl.2026.110960.** Bado proves strict unit pairwise negative correlation for every wheel under the uniform-all-forests law, an infinite 3-connected non-series-parallel class.
8. **Tang--Zhang, arXiv:2603.10738 (11 March 2026).** They prove p-NC for specified spanning-subgraph ensembles of the complete graph, including forests with exactly `k` components for fixed `k` and sufficiently large `n`. This is not the arbitrary-graph uniform law mixing all component counts.

A bounded 20 September 2026 web search for source-matching `K_{3,n}` / linear-forest uniform-forest correlation theorems did not locate the class below. This is negative evidence only, not a priority certificate.

## 3. New decomposition lemma: the two-dimensional response strip

Use the five connectivity states of three terminals

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one fresh right vertex adjacent to all three terminals, its transfer is

\[
S=4I+N,
\]

where exact enumeration gives

\[
N^3=0,\qquad N^2\ne0.
\]

Any terminal-symmetric right layer considered here has transfer

\[
T=A I+B N+C N^2.
\]

Normalize by `A>0`:

\[
\widehat T=I+aN+cN^2,
\qquad a=B/A,
\qquad c=C/A.
\]

Define its scalar response

\[
\rho(\widehat T)=\frac{a^2/2-c}{a}
\]

when `a>0`.

### Lemma `T07-RESPONSE-STRIP-PRODUCT-18`

Let

\[
\widehat T_j=I+a_jN+c_jN^2,
\qquad a_j>0,
\qquad N^3=0.
\]

Then

\[
\prod_j\widehat T_j=I+uN+vN^2
\]

with

\[
u=\sum_j a_j,
\qquad
v=\sum_j c_j+\sum_{i<j}a_i a_j,
\]

and therefore

\[
\frac{u^2}{2}-v
=
\sum_j\left(\frac{a_j^2}{2}-c_j\right)
=
\sum_j \rho_j a_j.
\]

Consequently, if `u>0`,

\[
\boxed{
 v=\frac{u^2}{2}-hu,
 \qquad
 h=\frac{\sum_j\rho_j a_j}{\sum_j a_j}
}
\]

and `h` lies in the convex hull of the layer responses `rho_j`. If there are no unmarked layers, `u=v=0`.

**Proof.** Multiply the factors and use `N^3=0`. Only the linear `N` terms and either one quadratic term or two linear terms survive in the `N^2` coefficient. The displayed identity follows by expanding `u^2/2`. The formula for `h` is a positive weighted average. `QED`.

This is the closure/decomposition gain of the run. It replaces an arbitrarily high-dimensional vector of layer multiplicities by the two continuous variables `(u,h)`.

## 4. Exact path responses through order eleven

For a right path `P_l`, every path vertex adjacent to all three terminals, exact frontier enumeration gives

\[
T_l=A_lI+B_lN+C_lN^2.
\]

The independently executed checker gives:

| `l` | `A_l` | `B_l` | `C_l` |
|---:|---:|---:|---:|
|1|4|1|0|
|2|23|12|5/3|
|3|130|103|85/3|
|4|734|780|961/3|
|5|4144|5524|9050/3|
|6|23396|37512|25562|
|7|132088|247492|202132|
|8|745736|1598880|4566296/3|
|9|4210240|10165072|33154864/3|
|10|23769968|63815424|234031360/3|
|11|134199328|396565360|1615193936/3|

For the normalized path response set

\[
\rho_l=\frac{(B_l/A_l)^2/2-C_l/A_l}{B_l/A_l}.
\]

Exact arithmetic gives the strict chain

\[
\rho_1>\rho_2>\cdots>\rho_{11}>0,
\]

with endpoints

\[
\rho_1=\frac18,
\qquad
\rho_{11}=\frac{149517080679839}{1247315737970580}.
\]

Hence **every arbitrary product of unmarked path layers of orders `1,...,11` lies in the same strip**

\[
\boxed{
 u\ge0,
 \qquad
 v=\frac{u^2}{2}-hu,
 \qquad
 \rho_{11}\le h\le\frac18.
}
\]

## 5. New all-parameter graph theorem

For integers `n_1,...,n_11>=0`, let

\[
H=\bigsqcup_{\ell=1}^{11} n_\ell P_\ell,
\qquad
N_H=\sum_{\ell=1}^{11}\ell n_\ell.
\]

Create three new **independent** terminals and join each terminal to every vertex of `H`. Equivalently,

\[
G=K_{3,N_H}+H,
\]

where the displayed `K_{3,N_H}` uses the three independent terminals and the right vertices of `H`.

### Theorem `T07-INDEPENDENT-LINEAR-FOREST11-STRIP-18`

For every `n_1,...,n_11>=0` and every pair of distinct present edges `e,f` of `G`,

\[
\boxed{\Delta_G(e,f)\ge0.}
\]

If `G` has edges and is not the tree `K_{3,1}` (`n_1=1`, all other `n_l=0`), then every pair is strict:

\[
\boxed{\Delta_G(e,f)>0.}
\]

Thus the uniform measure on all spanning forests of every graph in this eleven-parameter family has pairwise negative edge correlation.

The parameters are genuinely unbounded. In particular the repeated-`P11` subfamily has

\[
|V|=3+11p,
\qquad
|E|=43p,
\qquad p\ge1.
\]

The first member has 14 vertices and 43 edges, already well beyond the complete nine-vertex census.

More generally,

\[
|V|=3+\sum_{\ell=1}^{11}\ell n_\ell,
\qquad
|E|=\sum_{\ell=1}^{11}(4\ell-1)n_\ell.
\]

Whenever `N_H>=3`, the graph is 3-connected: deleting any two vertices leaves at least one terminal and at least one right vertex, and the surviving terminal/right incidence connects all remaining vertices. It contains `K_{3,3}`, so it is nonplanar and not series-parallel.

## 6. Proof of the theorem: expose marked components, then certify the strip

The seed row for three independent terminals is

\[
q_D=(1,0,0,0,0).
\]

Fix distinct edges `e,f`. They meet at most two right path components. Expose those one or two components completely, including their exact required-edge transfer matrices. Every remaining right component is unmarked and therefore collapses, after removal of its positive scalar `A_l`, to

\[
U(u,v)=I+uN+vN^2
\]

in the strip above.

For each of the four forest counts `I,I_e,I_f,I_ef`, the exposed marked transfers produce a row vector `r_X`, and

\[
I_X=r_XU(u,v)\mathbf1.
\]

Therefore every `I_X` is affine in `(u,v)`. Hence

\[
\Delta(e,f)=Q_{e,f}(u,v)
\]

for an exact polynomial of degree at most two in `(u,v)`.

Parameterize the strip by

\[
h=\rho_{11}+y\left(\frac18-\rho_{11}\right),
\qquad 0\le y\le1,
\]

and substitute

\[
v=\frac{u^2}{2}-hu.
\]

Then

\[
R_{e,f}(u,y)=Q_{e,f}\!\left(u,\frac{u^2}{2}-hu\right)
\]

has degree at most four in `u` and at most two in `y`.

### Exhaustive local orbit classification

The checker does not enumerate global graphs or bound the multiplicities `n_l`. It enumerates only local marked responses. For path orders `1,...,11`, it reduces edge pairs under:

- the global `S_3` permutation of the three terminals;
- path reversal in each exposed path component;
- exchange of the two exposed components when they have the same order.

The code constructs each orbit directly by applying these symmetries to **all raw local edge pairs**, so the classification is exhaustive. There are exactly

\[
\boxed{3478}
\]

local pair orbits.

### Regular strip cone: 3402 orbits

Write

\[
R(u,y)=\sum_{i=0}^4 r_i(y)u^i.
\]

For **3402** orbits, every nonzero quadratic `r_i(y)` has nonnegative degree-two Bernstein coefficients on `[0,1]`, and `r_0>0`. Hence

\[
R(u,y)>0
\]

for every `u>=0`, `0<=y<=1`.

### One zero-constant orbit

Exactly one additional orbit is the pair of two distinct spokes at the only vertex of a distinguished `P1`. Here `r_0=0`, but all positive-degree `u` coefficients have nonnegative Bernstein coefficients and the coefficient of `u` is strictly positive. Thus

\[
R(u,y)\ge0,
\]

with equality exactly when `u=0`. That means there are no other right components, so the whole graph is `K_{3,1}`, a tree. Under the uniform measure on all subsets of a tree the edge indicators are independent, hence equality is expected.

### Discriminant cone: 75 orbits

The remaining **75** exceptional orbits are all two spokes in the same path component, with different terminal labels. Every one has exact form

\[
R(u,y)
=
 u^2\bigl(a_4u^2-b_3(y)u+a_2(y)\bigr)
 +a_1(y)u+a_0,
\]

where `a_4>0`, and the degree-two Bernstein coefficients of `a_0,a_1,a_2,b_3` are all strictly positive on `[0,1]`. Moreover the exact checker finds

\[
\boxed{4a_4a_2(y)-b_3(y)^2=D>0}
\]

with `D` independent of `y` in every exceptional orbit. Therefore the quadratic

\[
a_4u^2-b_3(y)u+a_2(y)
\]

has negative discriminant and positive leading coefficient, so it is positive for every real `u`. The remaining terms are also positive for `u>=0`. Hence every one of these 75 orbits is strictly positive throughout the strip.

This completes the proof of `T07-INDEPENDENT-LINEAR-FOREST11-STRIP-18`, conditional only on the exact local enumeration executed and archived below. The theorem is therefore **CANDIDATE_FULL pending independent review**, not certified publication-ready.

## 7. Why this is genuinely complementary to NM13-04

The newest NM13-04 theorem has a **triangle seed**:

\[
K_3\vee H,
\]

and currently treats arbitrary mixtures of path components through order seven. The theorem here has three **independent** terminals:

\[
K_{3,|H|}+H,
\]

and treats arbitrary mixtures through order eleven.

Deleting the three triangle edges from an NM13-04 graph produces the seed used here, but unit p-NC is not automatically inherited under deletion without a stronger weighted hypothesis. Thus the independent-terminal theorem is not a formal corollary of NM13-04's unit theorem.

For right side size at least three, the present graphs are themselves 3-connected and contain `K_{3,3}`, directly inhabiting the structural regime that survives P14's minimal-counterexample reduction and lying outside Erickson's series-parallel theorem.

## 8. Exact checker and executed output

Essential code archived with this report:

`2026-09-20T09-35-17Z__independent-linear-forest11-response-strip-checker.py`

Executed command used for the substantive certificate:

```text
python /tmp/ind_orbit_strip.py 11
```

The archived stdout records, in exact rational/integer arithmetic:

```text
ABC last 11 (134199328, 396565360, 1615193936/3) rho 149517080679839/1247315737970580
rho monotone True
reps 3478
unique 3478
reg positive const 3402 exc 76
...
cert 76 fail 0
```

The same run displays the positive exact discriminant constant for each exceptional orbit. No floating-point sign decision is used in the proof.

Separate scratch brute-force sanity checks, not needed for the theorem, enumerated all edge subsets for the one-path physical graphs and gave

```text
P4: n=7, m=15, Z=5776, min Rayleigh numerator=27300
P5: n=8, m=19, Z=44340, min Rayleigh numerator=340560
```

These agree with the transfer calculation.

## 9. Failure accounting and residual obstruction

No source-level counterexample was found. The parent conjecture remains open.

The earlier repeated-path route has now been materially replaced by a mixture/response-strip attack, so this is not another unchanged fixed-length run. The new obstruction is more focused:

1. The response-strip product lemma itself is not limited to eleven, but the **local marked-pair sign classification is**. Long path components introduce new same-path spoke geometries.
2. Through path order eleven, every exceptional local polynomial still has the same exact negative-discriminant quadratic core. This strongly suggests an all-path theorem, but the checker does not prove that the discriminant identity stays positive for arbitrary path length/positions.
3. A finite local classification, even with an all-multiplicity transfer, is not the general uniform-forest conjecture. Arbitrary 3-connected graphs need not admit this three-terminal path-layer decomposition.

## 10. Next materially distinct attack

Do **not** continue by merely incrementing `P11 -> P12` indefinitely. The next attack should derive the same-path different-terminal spoke polynomial symbolically from the 15-state path-tail operator. The target is an exact recurrence/closed form in the path length `L` and spoke positions `i<j`, proving

\[
4a_4a_2-b_3^2>0
\]

for all admissible `L,i,j`, or producing the first exact negative case. If that succeeds, combine it with a uniform lower response bound for the sequence `rho_L` to replace the bounded component order by **arbitrary finite path components**.

That would convert the current finite-local-order theorem into a genuine arbitrary-linear-forest class; failure would identify a concrete source-valid obstruction rather than another growing corner threshold.

## 11. Compact ledger delta

- Parent theorem: `OPEN -> OPEN`.
- Complete all-simple-graph order: `9 -> 9`.
- Counterexample-order lower bound: `>=10 -> >=10`.
- Independent-terminal structured scope: repeated `P7` + singleton -> arbitrary mixtures `P1,...,P11`.
- Free multiplicity parameters: `2 -> 11` for the displayed mixed-path theorem.
- Local pair certificate: `3478` exact symmetry orbits; `3402` Bernstein-positive, `1` zero-constant tree orbit, `75` positive-discriminant exceptions; `fail=0`.
- New closure lemma: arbitrary products of normalized terminal-symmetric layers collapse to a response strip with `h` a positive weighted average of layer `rho` values.
- Status: restricted theorem `CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW`; external novelty/priority `UNVERIFIED`.

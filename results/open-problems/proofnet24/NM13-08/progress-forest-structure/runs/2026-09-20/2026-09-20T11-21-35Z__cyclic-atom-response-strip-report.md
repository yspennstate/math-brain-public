Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-08 / T07 — cyclic-atom response-strip closure and independent-terminal C3/C4 theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and substantive move

The preceding NM13-08 run proved a response-strip theorem for three **independent** terminals joined to an arbitrary right linear forest whose path components have order at most eleven. Its next-attack instruction explicitly said not to continue by merely increasing `P11 -> P12`; the unresolved marked-path recurrence needs a separate symbolic attack. The current companion NM13-04 has meanwhile proved the distinct triangle-seeded response-strip theorem through path order fifteen.

This run therefore executes a materially different attack: keep the independent-terminal seed but enlarge the right-side component algebra from forests to **cyclic atoms**. Exact enumeration shows that right triangles `C3` and right four-cycles `C4`, with every atom vertex adjacent to all three terminals, lie in the same nilpotent three-terminal algebra. A new algebraic sign lemma explains why the exceptional quadratic discriminant used in the earlier strip proofs is automatically independent of the strip coordinate. Combining the two facts yields a 13-parameter theorem allowing arbitrary multiplicities of `P1,...,P11,C3,C4`.

No previous report is overwritten. This is not a finite global graph census: the finite exact computation classifies local marked-atom responses; arbitrary atom multiplicities are transferred analytically by the response strip.

## 1. Parent theorem before/after, separated from mechanism gain

For a finite graph `G=(V,E)`, write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of the two edge indicators under the uniform probability measure on **all** spanning forests, with every component count mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No complete-order metric moves in this run.

**Mechanism before:** response-strip closure for independent-terminal right **linear forests** with components in `P1,...,P11`.

**Mechanism after:** the same arbitrary-multiplicity closure now accepts two genuinely cyclic terminal-symmetric atoms `C3` and `C4`, and the exceptional strip sign test is reduced by a new exact discriminant-cancellation identity. The demonstrated application is the 13-parameter class in Section 6.

## 2. Recovered P14 and exact literature scope

The inherited source/repository boundary remains unchanged.

1. **Grimmett–Winkler, arXiv:math/0302185 / Random Structures & Algorithms 24 (2004).** Their conjecture concerns the uniform law on **all forests**. Their published computation verifies pairwise edge negative correlation for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree theorem.
2. **P14/HARD10 dense-nine completion.** Repository exact computation covers the complementary 19–36-edge sector. Thus all 274,668 unlabeled simple graphs on nine vertices are covered in the source unit-weight scope; the dense sector has 120,314 graphs and 25,304,635 present-edge-pair checks in the preserved exact audit.
3. **P14 structural reduction.** Forest factorization over blocks reduces a vertex-minimal source counterexample to a 2-connected graph. P14's two-separator transfer, together with its recovered fixed-graph weighted implication, reduces a vertex-minimal source counterexample further to a **3-connected** graph. This remains a reduction, not a proof of the conjecture.
4. **Erickson, arXiv:1008.3660.** Erickson proves a stronger all-positive-weight SOS/Rayleigh theorem for **series-parallel** spanning-forest polynomials. The class below contains `K_{3,3}` as soon as the right side has at least three vertices, so it is outside that theorem.
5. **Tang–Zhang, arXiv:2603.10738 (11 March 2026).** Their p-NC theorem concerns specified spanning-subgraph ensembles of `K_n`, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; it is not the arbitrary-graph uniform law mixing all forest component counts.
6. **Bado, DOI 10.1016/j.spl.2026.110960.** Bado proves strict unit p-NC for wheel graphs under the uniform-all-forests law, another restricted infinite 3-connected non-series-parallel class.

A bounded source check did not locate the cyclic-atom class below. That is negative evidence only; novelty remains **UNVERIFIED**.

## 3. Three-terminal response algebra retained

Use the five connectivity states of three terminals

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one fresh right vertex adjacent to all three terminals, exact enumeration gives

\[
S=4I+N,\qquad N^3=0,\quad N^2\ne0.
\]

Every terminal-symmetric layer used here has transfer

\[
T=A I+B N+C N^2,
\]

with `A>0`. Normalizing gives

\[
\widehat T=I+aN+cN^2,
\qquad a=B/A,\quad c=C/A,
\]

and define

\[
\rho(T)=\frac{a^2/2-c}{a}.
\]

For a product of normalized unmarked layers,

\[
\prod_j(I+a_jN+c_jN^2)=I+uN+vN^2,
\]

nilpotence gives

\[
u=\sum_j a_j,
\qquad
\frac{u^2}{2}-v=\sum_j\left(\frac{a_j^2}{2}-c_j\right).
\]

Hence, if `u>0`,

\[
\boxed{v=\frac{u^2}{2}-hu,\qquad
h=\frac{\sum_j\rho_j a_j}{\sum_j a_j}},
\]

so `h` is a positive weighted average of the component responses. This is the response-strip product closure retained from the preceding run.

## 4. New sign lemma: exact strip-discriminant cancellation

The previous strip computations repeatedly found that exceptional Rayleigh quartics had an `h`-independent quadratic discriminant. Here that phenomenon is proved algebraically for **every** quadratic response polynomial.

### Lemma `T07-QUADRATIC-STRIP-DISCRIMINANT-CANCELLATION-21`

Let

\[
Q(u,v)=q_{00}+q_{10}u+q_{01}v+q_{20}u^2+q_{11}uv+q_{02}v^2.
\]

Substitute

\[
v=\frac{u^2}{2}-hu
\]

and write

\[
R(u,h)=Q\!\left(u,\frac{u^2}{2}-hu\right)
       =c_4u^4+c_3(h)u^3+c_2(h)u^2+c_1(h)u+c_0.
\]

Then

\[
\begin{aligned}
c_4&=\frac{q_{02}}4,\\
c_3(h)&=\frac{q_{11}}2-q_{02}h,\\
c_2(h)&=q_{20}+\frac{q_{01}}2-q_{11}h+q_{02}h^2,\\
c_1(h)&=q_{10}-q_{01}h,\\
c_0&=q_{00},
\end{aligned}
\]

and consequently

\[
\boxed{4c_4c_2(h)-c_3(h)^2
=q_{02}\left(q_{20}+\frac{q_{01}}2\right)-\frac{q_{11}^2}{4}},
\]

which is independent of `h`.

**Proof.** Direct substitution gives the five displayed coefficients. Then

\[
4c_4c_2=q_{02}\left(q_{20}+\frac{q_{01}}2-q_{11}h+q_{02}h^2\right),
\]

whereas

\[
c_3^2=\frac{q_{11}^2}{4}-q_{11}q_{02}h+q_{02}^2h^2.
\]

The `h` and `h^2` terms cancel exactly. `QED`.

### Corollary: a reusable strip sign test

If

\[
q_{02}>0,
\qquad
K:=q_{02}\left(q_{20}+\frac{q_{01}}2\right)-\frac{q_{11}^2}{4}>0,
\]

and `c0>=0`, `c1(h)>=0` throughout the relevant strip, then

\[
c_4u^2+c_3(h)u+c_2(h)>0
\]

for every real `u`, because its discriminant is `c3^2-4c4c2=-K<0` and `c4>0`. Therefore

\[
R(u,h)=u^2(c_4u^2+c_3u+c_2)+c_1u+c_0\ge0
\]

for every `u>=0`. It is strict whenever `c0>0`, or whenever `u>0` and `c1(h)>0`.

This removes the need to prove separate strip signs for `c2` and `-c3` in the exceptional sectors.

## 5. New cyclic atoms and widened response strip

A **right atom** means a fresh finite internal graph whose every vertex is adjacent to each of the three independent terminals. Exact enumeration gives the following unmarked transfers.

For a right triangle:

\[
\boxed{T_{C_3}=178I+144N+41N^2},
\qquad
\boxed{\rho_{C_3}=\frac{1535}{12816}}.
\]

For a right four-cycle:

\[
\boxed{T_{C_4}=1014I+1096N+\frac{1384}{3}N^2},
\qquad
\boxed{\rho_{C_4}=\frac{2767}{23153}}.
\]

The checker also reconstructs the previous path endpoint

\[
T_{P_{11}}=134199328I+396565360N+\frac{1615193936}{3}N^2,
\]

with

\[
\rho_{P_{11}}=\frac{149517080679839}{1247315737970580}.
\]

Exact rational comparison gives

\[
\boxed{
\rho_{C_4}<\rho_{C_3}<\rho_{P_{11}}<\cdots<\rho_{P_1}=\frac18.
}
\]

Hence an arbitrary product of unmarked components selected from

\[
P_1,\ldots,P_{11},C_3,C_4
\]

lies in the single strip

\[
\boxed{u\ge0,\qquad
v=\frac{u^2}{2}-hu,\qquad
\frac{2767}{23153}\le h\le\frac18.}
\]

The component multiplicities do not appear in the subsequent local sign classification.

## 6. New all-parameter theorem with cyclic right components

Let

\[
H=aC_3\sqcup bC_4\sqcup\bigsqcup_{\ell=1}^{11} n_\ell P_\ell,
\qquad a,b,n_1,\ldots,n_{11}\in\mathbb Z_{\ge0}.
\]

Create three new **independent** terminals and join every terminal to every vertex of `H`. Equivalently,

\[
G=\overline{K_3}\vee H.
\]

### Theorem `T07-INDEPENDENT-CYCLIC-ATOM-STRIP-21`

For every choice of the thirteen nonnegative multiplicities above and every pair of distinct present edges `e,f` of `G`,

\[
\boxed{\Delta_G(e,f)\ge0.}
\]

If `G` has edges and is not the tree `K_{3,1}`, every physical edge pair is strict:

\[
\boxed{\Delta_G(e,f)>0.}
\]

Thus the uniform measure on **all** spanning forests of every graph in this 13-parameter family has pairwise negative edge correlation.

The graph parameters are

\[
|V(G)|=3+3a+4b+\sum_{\ell=1}^{11}\ell n_\ell,
\]

\[
|E(G)|=12a+16b+\sum_{\ell=1}^{11}(4\ell-1)n_\ell.
\]

Whenever `|V(H)|>=3`, `G` is 3-connected and contains `K_{3,3}`, hence is nonplanar and non-series-parallel.

### Proof

Fix `e,f`. They lie in at most two right components. Expose those one or two marked components completely, including exact required-edge transfer matrices. Every other component is unmarked, so after removing its positive scalar `A` its product is

\[
U(u,v)=I+uN+vN^2
\]

in the strip of Section 5.

For each of `I,I_e,I_f,I_ef`, the exposed local part produces a row vector `r_X`, and

\[
I_X=r_XU(u,v)\mathbf1.
\]

Thus every one of the four counts is affine in `(u,v)`, and every Rayleigh numerator is a quadratic

\[
\Delta(e,f)=Q_{e,f}(u,v).
\]

It remains only to check finitely many **local marked response types**, because all unbounded component multiplicities have already been compressed into the strip.

The exact executable retains the exhaustive 3,478 symmetry-reduced path/path local representatives from the preceding independent-terminal theorem, and adds every raw marked representative involving `C3` or `C4`: same-atom pairs, pairs on two cyclic atoms, and cyclic-atom/path pairs. There are 7,862 such additional raw representatives, for 11,340 total local representatives. Exact deduplication leaves 3,842 distinct quadratic response polynomials.

On the widened strip `[rho_C4,1/8]`, the certificate divides them as follows:

- 3,402 old path polynomials: coefficientwise nonnegative in the degree-two Bernstein basis after strip substitution;
- one old zero-constant path polynomial: the expected two-spoke equality case of `K_{3,1}`;
- 75 old path polynomials: certified by the new discriminant lemma;
- **363 new cyclic/mixed polynomials:** coefficientwise Bernstein-positive;
- **one new cyclic/mixed polynomial:** certified by the new discriminant lemma.

There are **zero failures**. The minimum positive exact `K` among every discriminant-certified polynomial is

\[
\boxed{207792}.
\]

Therefore every local response polynomial is nonnegative throughout the entire continuous strip, which proves the theorem for arbitrary component multiplicities. `QED`.

## 7. Why the application is genuinely complementary to NM13-04

The companion NM13-04 response-strip theorems have the **triangle seed** `K_3\vee L` with right linear-forest components. The present seed is an **independent** terminal triple and the right induced graph is allowed to contain cycles.

A particularly clean new subfamily is

\[
G_{b,r}=\overline{K_3}\vee(bC_4\sqcup rK_1),
\qquad b\ge1,\ r\ge0.
\]

It has

\[
|V|=3+4b+r,\qquad |E|=16b+3r.
\]

Because the terminal set is independent and the right graph `bC4 sqcup rK1` has clique number two, every graph in this subfamily has clique number exactly three. In contrast, every nonempty triangle-seeded graph `K_3\vee L` contains a `K_4`. Thus this is not merely an isomorphic reparameterization of the NM13-04 class. Nor can the theorem be obtained by deleting the three triangle edges from a unit-only p-NC theorem: unit p-NC is not known to be preserved by arbitrary edge deletion. Finally, `b>=1` introduces genuine cycles in the right induced graph, beyond the previous independent-terminal linear-forest theorem.

For example, `b=2,r=0` has 11 vertices and 32 edges. The theorem covers all `b,r`, not just this example.

## 8. Independent exact checks

The executable performs three direct brute-force whole-graph checks in addition to the local transfer certificate:

- `I3 join C4`: 7 vertices, 16 edges, 8,166 forests, minimum Rayleigh numerator 146,464;
- `I3 join (C4 sqcup K1)`: 8 vertices, 19 edges, 43,296 forests, minimum numerator 1,512,768;
- `I3 join C3`: 6 vertices, 12 edges, 1,000 forests, minimum numerator 2,496.

The archived exact run terminates

`ALL_EXACT_CHECKS_PASS`.

All sign decisions use exact integers/rationals; no floating-point sign comparison is used.

## 9. Honest failure / residual obstruction

This does **not** prove the Grimmett–Winkler conjecture. The source-level all-graph order cutoff remains nine. The present closure still requires the graph to decompose into terminal-symmetric right atoms around one distinguished independent 3-set. An arbitrary 3-connected graph need not admit such a decomposition.

The earlier arbitrary-path obstruction also remains: path components are certified only through order eleven in this independent-terminal seed. This run deliberately did not hide that gap by another blind cutoff increase. The new discriminant-cancellation lemma removes one algebraic burden, but a symbolic recurrence for the remaining marked coefficients as path length and spoke positions vary is still needed for an all-path theorem.

A next materially distinct attack is to combine the exact 15-state path-tail operator with the new formula for `K`: derive a recurrence directly for the four response coefficients `q02,q20,q01,q11` of same-path different-terminal spoke pairs. Positivity of the single scalar

\[
K=q_{02}(q_{20}+q_{01}/2)-q_{11}^2/4
\]

would then replace the larger strip-polynomial certificate and may make an arbitrary-path proof tractable.

## 10. Durable artifacts

This run saves, under the assigned immutable run directory:

- `2026-09-20T11-21-35Z__cyclic-atom-response-strip-report.md` — this substantive report;
- `2026-09-20T11-21-35Z__ledger_delta.yaml` — structured before/after and residual obstruction;
- `2026-09-20T11-21-35Z__cyclic-atom-response-strip-checker.py` — exact executable;
- `2026-09-20T11-21-35Z__cyclic-atom-response-strip-checker.out` — actual executed output.

No historical or peer file is modified.

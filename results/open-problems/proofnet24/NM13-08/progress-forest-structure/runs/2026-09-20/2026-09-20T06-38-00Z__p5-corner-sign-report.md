Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — P5 right-layer transfer and two-corner lattice sign theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and this run's materially new move

The previous NM13-08 run proved pairwise negative edge correlation for

\[
F^{(4)}_{p,r}=K_{3,4p+r}+\bigl(pP_4\sqcup rK_1\bigr)
\]

with three independent terminals. Its positive-Newton proof failed for exactly one marked `P4` spoke-pair orbit and was repaired by a shifted-quadrant staircase. The explicit next attack was `P5`, refutation first.

The newest NM13-04 run independently proved the complementary **triangle-seeded** theorem

\[
K_3\vee(aP_4\sqcup bP_3\sqcup cK_2\sqcup dK_1),
\]

again with one exceptional `P4` orbit repaired by a staircase. That mathematics is preserved and not duplicated here.

This run executes the promised `P5` attack with independent terminals. The refutation scan found no negative integer parameter point. Exact orbit reduction shows that the `P5` layer has **two**, not one, exceptional marked-spoke orbit outside the positive Newton cone. A new reusable two-corner lattice sign lemma proves both exceptional quartics positive on the whole nonnegative integer quadrant. This yields a complete all-parameter `P5` class.

`operations/PROGRESS20_2026-09-20.md`, current LIVE20 ownership, the latest own and NM13-04 reports, the P14 mandatory handoff, and `POSTED.md` were checked. A repository search found `P5` only as the unresolved next attack in the preceding NM13-08/NM13-04 reports; no prior repository theorem covering the class below was found. External novelty/priority remains **UNVERIFIED**.

## 1. Parent theorem before/after, separately from mechanism gain

For a finite graph `G=(V,E)`, write

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation for the uniform measure on **all** acyclic spanning edge subsets, with all component counts mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent lower bound on the order of a source-valid counterexample:** `>=10 -> >=10`.

No source-level complete-order metric moves.

**Mechanism before:** independent three-terminal right components up through `P4`, with 39/40 positive-Newton orbit polynomials and one shifted-quadrant repair.

**Mechanism after:** the first right component of order five is controlled. For repeated `P5` layers plus isolated right vertices, 59/61 orbit polynomials lie in the nonnegative Newton cone. The two failures are proved positive by the new two-corner lattice lemma, with exact corner shifts `(3,0),(0,15)` and `(10,0),(0,50)` plus finite boxes. This proves a new two-parameter 3-connected non-series-parallel family.

## 2. Recovered P14 and current literature scope

The source distinctions remain essential.

1. **Grimmett–Winkler, arXiv:math/0302185.** They study the uniform measure on **all forests**. Their published computation verifies pairwise edge negative correlation for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree theorem.
2. **P14/HARD10 repository completion.** The complementary dense nine-vertex sector was checked exactly, giving all `274,668` unlabeled simple graphs on nine vertices in the source unit-weight scope. P14's block/direct-sum factorization and two-separator transfer, together with the recovered fixed-graph unit-to-positive-weight implication, reduce a vertex-minimal source counterexample to a **3-connected** graph. This is a reduction, not closure.
3. **P14 failed routes.** The generic degree-three star/mesh route leaves a mixed three-terminal polarization. That mixed term is not universally nonnegative, and a proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex graph while the true Rayleigh gap remained positive. Lorentzian/complete-log-concavity, naive stability perturbation, and Gårding shortcuts still lack source-matching hypotheses for arbitrary graphic independence polynomials.
4. **Erickson, arXiv:1008.3660.** Erickson proves a positive sum-of-squares expression for the spanning-forest Rayleigh difference of every **series-parallel** graph, hence a stronger all-positive-edge-weight independent-set-Rayleigh theorem for that class. The graphs below contain `K_{3,3}` and therefore are not series-parallel.
5. **Huang, arXiv:2311.00965.** The paper treats restricted arboreal-gas negative-correlation questions and still presents the general negative-correlation problem as open.
6. **Bado, DOI 10.1016/j.spl.2026.110960.** Bado proves strict pairwise negative correlation for every wheel under the uniform-all-forests law, a genuine infinite 3-connected non-series-parallel class.
7. **Tang–Zhang, arXiv:2603.10738, 11 March 2026.** They prove p-NC for specified complete-graph spanning-subgraph ensembles, including forests with exactly `k` components for fixed `k` and sufficiently large `n`. This is not the arbitrary-graph uniform measure over forests of all component counts.

Thus a spanning-tree theorem, a series-parallel weighted theorem, a wheel theorem, or a complete-graph fixed-component theorem is not the parent T07 conjecture.

## 3. New P5 layer decomposition

Use the five terminal-connectivity states

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one isolated right vertex the transfer is

\[
S=\begin{pmatrix}
4&1&1&1&1\\
0&4&0&0&2\\
0&0&4&0&2\\
0&0&0&4&2\\
0&0&0&0&4
\end{pmatrix},
\qquad N=S-4I,
\qquad N^3=0.
\]

For one right `P5` with vertices `0-1-2-3-4`, each joined to all three terminals, exact local forest enumeration gives

\[
P_5=
\begin{pmatrix}
4144&5524&5524&5524&23624\\
0&4144&0&0&11048\\
0&0&4144&0&11048\\
0&0&0&4144&11048\\
0&0&0&0&4144
\end{pmatrix}
=
\boxed{4144I+5524N+\frac{9050}{3}N^2}.
\]

Hence, after normalizing by the positive leading factor, `x` unmarked `P5` layers and `z` singleton layers contribute

\[
U(x,z)=I+uN+vN^2,
\]

where

\[
u=\frac{1381}{1036}x+\frac14z
\]

and

\[
v=\frac{4525}{6216}x
 +\binom{x}{2}\left(\frac{1381}{1036}\right)^2
 +\binom{z}{2}\frac1{16}
 +xz\frac{1381}{4144}.
\]

Because `N^3=0`, every marked forest count obtained after exposing the one or two layers containing a chosen edge pair is a polynomial of total degree at most two in `(x,z)`. Every normalized Rayleigh difference is therefore a rational polynomial of total degree at most four.

As a check on the transfer, for

\[
F^{(5)}_{p,r}:=K_{3,5p+r}+\bigl(pP_5\sqcup rK_1\bigr)
\]

(the three vertices in the size-three side are independent), the total forest count satisfies

\[
\frac{I_{F^{(5)}_{p,r}}(\mathbf1)}{4144^p4^r}
=
\frac{5721483p^2+2146074pr+4689281p+201243r^2+872053r+1073296}{1073296}.
\]

The exact checker reconstructs this identity from the local subset enumeration; it is not inferred numerically.

## 4. New reusable sign lemma

### Lemma `T07-TWO-CORNER-LATTICE-SIGN-12`

Let `Q in R[x,z]` and let `A,B` be positive integers. Suppose:

1. every coefficient of `Q(A+X,Z)` in the ordinary monomial basis `X^i Z^j` is strictly positive;
2. every coefficient of `Q(X,B+Z)` is strictly positive; and
3. `Q(i,j)>0` for every integer lattice point `0<=i<A`, `0<=j<B`.

Then

\[
\boxed{Q(x,z)>0\quad\text{for every }(x,z)\in\mathbb Z_{\ge0}^2.}
\]

**Proof.** If `x>=A`, write `x=A+X` with `X>=0`; hypothesis 1 gives positivity because every monomial and every coefficient is nonnegative/positive and the constant coefficient is positive. If `x<A` but `z>=B`, write `z=B+Z` and use hypothesis 2. The only remaining points lie in the finite rectangle from hypothesis 3. QED.

This is elementary, but it is a useful exact certificate because the positive Newton cone can fail while eventual shifted monomial cones remain positive. It gives a proof-size bound of two symbolic shifted expansions plus one finite rectangle rather than an unstructured infinite parameter scan.

## 5. Exhaustive marked-orbit reduction for P5

Take a universal witness containing two `P5` layers and two singleton layers. It has `44` present edges and `946` unordered edge pairs. The automorphism group generated by terminal `S_3`, the swap of the two `P5` blocks, independent `P5` reversals, and the singleton swap reduces these to exactly

\[
\boxed{61}
\]

edge-pair orbits.

For an orbit `O`, expose the one or two distinguished layers containing its representative pair and let `(x,z)` be the remaining numbers of `P5` and singleton layers. Marked-layer commutation and the transfer formula above give

\[
\Delta(e,f)=(4144^x4^z)^2R_O(x,z),
\]

where `R_O` has total degree at most four.

For **59 of the 61** orbits, the exact bivariate Newton expansion

\[
R_O(x,z)=\sum_{i+j\le4} c^O_{ij}\binom{x}{i}\binom{z}{j}
\]

has no negative coefficient. Every nonzero coefficient is positive; among these 59 orbit certificates the minimum positive Newton coefficient is `27/32`, and the minimum positive constant among positive-constant orbits is `36`.

Exactly one regular orbit has zero constant term: two distinct terminal spokes of one singleton layer. Its remaining Newton coefficients are positive, so equality occurs only when no other layer exists, namely the tree `F^{(5)}_{0,1}=K_{3,1}`.

The positive Newton cone fails for exactly two `P5` spoke-pair orbits:

- same `P5` block, vertices `0` and `3`, different terminal labels;
- same `P5` block, vertices `0` and `4`, different terminal labels.

Both have four negative Newton coefficients. The refutation-first scan therefore disproves the hoped-for universal positive-Newton mechanism at `P5`, but does **not** find a negative Rayleigh value.

## 6. Exact two-corner certificates for the two exceptional quartics

### 6.1 Distance-three spoke pair

For the orbit represented by `v0-T0` and `v3-T1`, clearing the positive denominator `143995537952` gives

\[
\begin{aligned}
Q_3(x,z)={}&818384192982225x^4+613936295387100x^3z-9136364031753690x^3\\
&+172711260505350x^2z^2-5142562002879630x^2z+490005160552704505x^2\\
&+21594118499100xz^3-964860104843670xz^2+183808103360018970xz\\
&+1457511652994302080x+1012468626225z^4-60343130123010z^3\\
&+17237278361480625z^2+274875962307331840z+1029199467779642880.
\end{aligned}
\]

The checker verifies exactly:

- `Q_3(3+X,Z)` has all 15 monomial coefficients positive, minimum `1012468626225`;
- `Q_3(X,15+Z)` has all 15 monomial coefficients positive, minimum `404987450490`;
- all `3*15=45` lattice values in `0<=x<3`, `0<=z<15` are positive; the minimum is `1029199467779642880` at `(0,0)`.

By `T07-TWO-CORNER-LATTICE-SIGN-12`, `Q_3(x,z)>0` on the whole nonnegative integer quadrant.

### 6.2 Opposite-endpoint spoke pair

For the orbit represented by `v0-T0` and `v4-T1`, clearing the positive denominator `71997768976` gives

\[
\begin{aligned}
Q_4(x,z)={}&32735367719289x^4+24557451815484x^3z-1206956576814066x^3\\
&+6908450420214x^2z^2-679161615580518x^2z+268856412154291161x^2\\
&+863764739964xz^3-127389419462046xz^2+100847050777720170xz\\
&+771304113230371616x+40498745049z^4-7964753192970z^3\\
&+9456839457089185z^2+145401366389025376z+538203482470913280.
\end{aligned}
\]

The checker verifies exactly:

- `Q_4(10+X,Z)` has all 15 monomial coefficients positive, minimum `40498745049`;
- `Q_4(X,50+Z)` has all 15 monomial coefficients positive, minimum `40498745049`;
- all `10*50=500` lattice values in `0<=x<10`, `0<=z<50` are positive; the minimum is `538203482470913280` at `(0,0)`.

Again the two-corner lemma gives `Q_4(x,z)>0` for all nonnegative integer parameters.

These certificates are exact integer/rational calculations. No floating-point sign decision is used.

## 7. New all-parameter theorem

### Theorem `T07-RIGHT-P5-FOREST-PNC-12`

For every `p,r>=0` and every two distinct present edges `e,f` of

\[
F^{(5)}_{p,r}=K_{3,5p+r}+\bigl(pP_5\sqcup rK_1\bigr),
\]

\[
\boxed{\Delta_{F^{(5)}_{p,r}}(e,f)\ge0.}
\]

The inequality is strict for every physical edge pair except the degenerate tree `F^{(5)}_{0,1}=K_{3,1}`.

**Proof.** Every physical edge pair lies in one of the 61 witness orbits. Remove the one or two distinguished layers containing it. The remaining counts `(x,z)` are nonnegative integers, and the Rayleigh difference factors as `(4144^x4^z)^2R_O(x,z)` with positive scalar prefactor. For 59 orbits the nonnegative Newton expansion proves `R_O>=0`; positive constant gives strictness, except for the unique singleton-spoke orbit whose zero constant occurs only at `x=z=0`, i.e. `F_{0,1}`. The two remaining orbit polynomials are strictly positive by Sections 6.1–6.2 and the two-corner lemma. QED.

The proof is symbolic in `p,r`; it is not finite extrapolation in graph order.

## 8. Why this class is genuinely uncovered and complementary to NM13-04

For `p>=1`,

\[
|V|=3+5p+r,
\qquad
|E|=19p+3r.
\]

Several structural separations are immediate.

- `5p+r>=5`, so the graph contains `K_{3,3}` and is nonplanar. Hence it is not series-parallel and is outside Erickson's theorem.
- `K_{3,5p+r}` is 3-connected for `p>=1`, and adding the right-path edges preserves 3-connectivity. Thus this family lies directly in the 3-connected regime surviving P14's minimal-counterexample reduction.
- The three distinguished high-degree terminals are independent, and the whole graph has clique number `3`: at most one terminal can be used in a clique, and the right induced graph is a linear forest. By contrast every nontrivial NM13-04 triangle-seeded join contains a `K4` (its left triangle plus any right vertex). Therefore the classes are not isomorphic presentations of one another.
- The right induced graph contains genuine `P5` components. The preceding NM13-08 theorem stopped at `P4`, and the newest NM13-04 theorem allows right linear-forest components only through order `4`. A repository search before this write found `P5` precisely as their stated next unresolved attack.
- For `p>=1` the graph is not complete multipartite: on the induced right `P5`, nonadjacency is not an equivalence relation. Thus current complete-bipartite/complete-tripartite fixed-width results do not subsume this class.
- It is not a wheel family: it is nonplanar while wheel graphs are planar.

Hence this is a genuinely new unbounded 3-connected non-series-parallel class in the source probability space, complementary to NM13-04.

## 9. Essential exact execution

The checker

`2026-09-20T06-38-00Z__p5-corner-checker.py`

was executed locally with exact integer/SymPy rational arithmetic before persistence. It reconstructs `S`, the complete `P5` transfer and all one-/two-edge marked `P5` transfer matrices directly from acyclic local subsets; verifies `N^3=0`; verifies the closed forest-count formula; constructs the exact automorphism action and 61 pair orbits; derives every orbit polynomial; verifies the 59 Newton certificates; identifies the two and only two exceptional orbits; verifies both shifted-corner coefficient cones and all `45+500` finite residual lattice values; and independently brute-forces physical examples.

Archived output includes:

- `F^{(5)}_{1,0}`: `n=8`, `m=19`, `Z=44340`, minimum Rayleigh numerator `340560`, maximum `49717320`;
- `F^{(5)}_{1,1}`: `n=9`, `m=22`, `Z=227080`, minimum Rayleigh numerator `7363344`, maximum `1829342544`;
- `F^{(5)}_{0,2}`: `n=5`, `m=6`, `Z=54`, minimum Rayleigh numerator `36`.

The execution terminates with

`ALL_EXACT_CHECKS_PASS`.

Artifact creation commits before this report:

- checker: `b37c0e95cd907074c2bb5c27bddd2dcea54f84b2`;
- executed output: `e95aa2fb8e5ef4c95d155d208f3dd463283fdaf1`;
- structured ledger delta: `425a8d2d2071a83d21ba1757f6605d6e5c406c68`.

## 10. What failed, what moved, and the residual obstruction

The refutation-first move was informative. The hoped-for statement

> every marked `P5` orbit polynomial has nonnegative Newton coefficients

is false: exactly two orbit polynomials have negative Newton coefficients. Thus the previous cone mechanism did **not** survive unchanged.

The substantive gain is that both failures are still globally positive on the nonnegative integer quadrant, by a compact exact certificate. This moves the demonstrated structured scope from right component order `4` to right component order `5` for an independent terminal triple.

The parent theorem does not move. An arbitrary 3-connected graph need not decompose into these right layers. More specifically, nothing here proves a uniform-in-path-length sign theorem. The corner threshold for the hardest opposite-endpoint orbit has already grown from the `P4` staircase scale to a `(10,50)` two-corner certificate at `P5`; this may be a proof artifact or the first sign of a genuine obstruction.

The next materially distinct attack is therefore not merely `run P6 and hope`. It is:

1. derive a transfer recurrence in path length `m` for the hardest marked spoke-pair Rayleigh polynomials, tracking endpoint separation and terminal-label coincidence;
2. use that recurrence to search `P6` **refutation first** for a negative integer parameter point;
3. only if no counterexample appears, ask whether the recurrence implies a uniform eventual-corner bound or forces thresholds to grow in a controlled way.

This is the missing mechanism needed to turn the sequence `P3/P4/P5` into an actual closure theorem for arbitrarily long right paths.

## 11. ledger_delta summary

Parent theorem: `OPEN -> OPEN`; complete-order metric `9 -> 9`; counterexample-order lower bound `>=10 -> >=10`.

Restricted theorem: `T07-RIGHT-P5-FOREST-PNC-12`, **CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW**.

Mechanism: `P4 one-exception staircase -> P5 two-exception exact two-corner lattice certificates`, with an exact `P5` transfer in the common nilpotent three-terminal algebra.

Novelty/priority: **UNVERIFIED**. No public posting or closure claim is made.

END OF REPORT

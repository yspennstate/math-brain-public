Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — P6 right-layer sign theorem and an exact path-tail recurrence

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and this run's new move

The previous NM13-08 run proved p-NC for

\[
F^{(5)}_{p,r}=K_{3,5p+r}+\bigl(pP_5\sqcup rK_1\bigr)
\]

with three independent terminals. Of 61 marked edge-pair orbits, 59 lay in the nonnegative bivariate Newton cone; the two remaining same-layer spoke orbits at path distances three and four were proved positive by exact two-corner certificates. Its explicit next attack was to derive a path-length recurrence and then test `P6` refutation-first.

The newest companion NM13-04 report proves the complementary triangle-seeded theorem

\[
K_3\vee(pP_5\sqcup rK_1),
\]

with 70/72 Newton-positive orbit polynomials and two geometric `P5` exceptions repaired by different corner certificates. That result is preserved and not duplicated here.

This run executes both promised pieces. First, it derives a fixed 15-state path-extension operator and its exact minimal polynomial, giving an order-eight recurrence for every unmarked path-layer response and for every marked response once the marked prefix has been passed. Second, it carries out the full independent-terminal `P6` sign calculation. The refutation-first search found no negative lattice point. Exactly four orbit polynomials leave the Newton cone, and all four admit exact two-corner certificates. This proves an all-parameter `P6` class.

`operations/PROGRESS20_2026-09-20.md`, the current LIVE20 mapping, `POSTED` status, the latest own report, the latest NM13-04 report, and the preserved P14 scope were the essential repository dependencies. No historical or peer file was edited. A repository search found no prior T07 `P6` theorem. External novelty/priority remains **UNVERIFIED**.

## 1. Parent theorem before/after, separately from mechanism gain

For a finite graph `G=(V,E)` let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is equivalent to pairwise negative correlation of `e,f` in the uniform measure on **all** acyclic spanning edge subsets, with all component counts mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent lower bound on the order of a source-valid counterexample:** `>=10 -> >=10`.

No source-level complete-order metric moves.

**Mechanism before:** independent three-terminal `P5` right layers, with 59/61 Newton-positive orbit polynomials and two exact corner repairs.

**Mechanism after:** an exact finite-state recurrence in the path length plus a complete `P6` all-parameter theorem. The `P6` witness has 81 edge-pair orbits; 77 lie in the nonnegative Newton cone and the four failures have exact corner certificates. The exceptional geometry becomes systematic: precisely the different-terminal spoke pairs in one `P6` layer whose path vertices are at distance at least three.

## 2. Recovered P14 and literature scope

The source boundaries remain unchanged and important.

1. **Grimmett–Winkler, arXiv:math/0302185 / RSA 24 (2004).** They study the uniform measure on **all forests**. Their computation verifies pairwise edge negative correlation for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree theorem.
2. **P14/HARD10 repository completion.** Exact complementary work covers the dense nine-vertex sector, giving all 274,668 unlabeled simple graphs on nine vertices in the source unit-weight scope. P14's block/direct-sum factorization and two-separator transfer, with the recovered fixed-graph weighted implication used there, reduce a vertex-minimal source counterexample to a **3-connected** graph. This is a structural reduction, not a solution.
3. **P14 failed generic routes.** The degree-three star/mesh attack leaves a mixed three-terminal polarization that is not universally nonnegative. A proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex graph while the actual Rayleigh gap remained positive. Lorentzian/complete-log-concavity and naive stability shortcuts still lack source-matching hypotheses.
4. **Erickson, arXiv:1008.3660.** Erickson proves a stronger positive-weight SOS / independent-set-Rayleigh theorem for **series-parallel** graphs. The class below contains `K_{3,3}` for every `p>=1` and therefore is not series-parallel.
5. **Huang, arXiv:2311.00965 / SPL 213 (2024).** The general arboreal-gas negative-correlation problem is still presented as open while restricted parameters/graphs are treated.
6. **Bado, DOI 10.1016/j.spl.2026.110960.** Bado proves strict p-NC for every wheel under the uniform-all-forests law, a genuine infinite 3-connected non-series-parallel class.
7. **Tang–Zhang, arXiv:2603.10738, 11 March 2026.** Their p-NC theorem concerns specified complete-graph spanning-subgraph ensembles, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; it is not the arbitrary-graph law mixing all forest component counts.

Thus neither a spanning-tree theorem, an all-positive-weight series-parallel theorem, a wheel theorem, nor a complete-graph fixed-component theorem settles T07.

## 3. New decomposition lemma: exact path-tail recurrence

Use a frontier consisting of the three terminals together with the current endpoint of a partially built right path. Its connectivity state is a partition of four labelled points, so there are exactly `Bell(4)=15` states.

To extend the path by one vertex, introduce a new right vertex, independently choose the old-new path edge and the three spokes from the new vertex to the terminals, reject any choice that creates a cycle, and then forget the old frontier vertex. This defines a fixed integer `15 x 15` matrix `E` on frontier partitions.

### Lemma `T07-PATH-TAIL-RECURRENCE-13`

The exact path-extension matrix satisfies

\[
\chi_E(\lambda)=(\lambda-1)^5(\lambda^2-6\lambda+2)^5
\]

and has minimal polynomial

\[
\boxed{m_E(\lambda)=(\lambda-1)^2(\lambda^2-6\lambda+2)^3.}
\]

Consequently every scalar forest count obtained from a fixed initial frontier vector, followed by `n` unmarked path extensions and a fixed final linear functional, satisfies the order-eight recurrence

\[
\boxed{
 a_{n+8}=20a_{n+7}-151a_{n+6}+534a_{n+5}-918a_{n+4}
 +816a_{n+3}-380a_{n+2}+88a_{n+1}-8a_n.}
\]

The same recurrence applies to a marked path response after all required marked edges lie in the already-built prefix, because every further step is multiplication by the same unmarked `E`.

**Proof.** The 15 states and every transition are finite combinatorial objects. The exact checker enumerates all 16 subsets of the four possible extension edges in each frontier state, rejects cycle-forming subsets, and constructs `E` with integer entries. Exact symbolic arithmetic then gives the characteristic polynomial above and verifies

\[
(E-I)^2(E^2-6E+2I)^3=0,
\]

while both `(E-I)(E^2-6E+2I)^3` and `(E-I)^2(E^2-6E+2I)^2` are nonzero, proving the stated minimal polynomial. Expanding `m_E(E)=0` gives the displayed recurrence after left/right multiplication by arbitrary fixed vectors. QED.

This is the first path-length recurrence in the NM13-08 line; previous `P3/P4/P5` theorems treated each layer order separately.

## 4. Exact `P6` transfer

Use the five terminal partitions

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one isolated right vertex,

\[
S=4I+N,\qquad N^3=0.
\]

Exact frontier enumeration for one right `P6` gives

\[
P_6=
\begin{pmatrix}
23396&37512&37512&37512&190884\\
0&23396&0&0&75024\\
0&0&23396&0&75024\\
0&0&0&23396&75024\\
0&0&0&0&23396
\end{pmatrix}
=
\boxed{23396I+37512N+25562N^2}.
\]

Hence, after exposing the one or two layers containing a chosen marked edge pair, `x` remaining `P6` layers and `z` singleton layers contribute, after division by `23396^x4^z`,

\[
U(x,z)=I+uN+vN^2,
\]

where

\[
u=\frac{37512}{23396}x+\frac14z
\]

and

\[
v=\frac{25562}{23396}x
+\binom{x}{2}\left(\frac{37512}{23396}\right)^2
+\binom{z}{2}\frac1{16}
+xz\frac{37512}{93584}.
\]

Because `N^3=0`, every marked forest count is degree at most two in `(x,z)`, and every normalized Rayleigh difference is degree at most four.

For

\[
F^{(6)}_{p,r}:=K_{3,6p+r}+\bigl(pP_6\sqcup rK_1\bigr)
\]

with the three size-three-side vertices independent, the total forest count has the exact closed form

\[
\frac{I_{F^{(6)}_{p,r}}(\mathbf1)}{23396^p4^r}
=
\frac{
4221450432p^2+1316446128pr+2877363888p
+102632403r^2+444740413r+547372816
}{547372816}.
\]

## 5. Exhaustive marked-orbit reduction for `P6`

Take a universal witness with two `P6` blocks and two singleton blocks. It has 52 present edges and 1326 unordered edge pairs. The exact automorphism group generated by terminal `S_3`, swapping the two `P6` blocks, independently reversing each path, and swapping the two singletons reduces these to exactly

\[
\boxed{81}
\]

edge-pair orbits.

Every physical pair in every `F^{(6)}_{p,r}` touches at most two right layers, hence is represented in this witness. Once the distinguished layers are exposed, the remaining counts `(x,z)` are nonnegative integers and

\[
\Delta(e,f)=(23396^x4^z)^2R_{\mathcal O}(x,z)
\]

for an exact rational quartic `R_O`.

Expand in the bivariate Newton basis

\[
R_{\mathcal O}(x,z)=\sum_{i+j\le4}c^{\mathcal O}_{ij}\binom xi\binom zj.
\]

The exact checker proves:

- **77 of 81** orbit polynomials have no negative Newton coefficient;
- among those 77, the minimum positive Newton coefficient is `27/32`;
- the minimum positive regular-orbit constant is `36`;
- the unique zero-constant regular orbit is the pair of two different-terminal spokes on one singleton layer, and all its nonzero Newton coefficients are positive, so equality occurs only for `F^{(6)}_{0,1}=K_{3,1}`.

The positive-Newton cone fails for exactly four orbit representatives:

1. spokes `v0-T0` and `v3-T1` in one `P6` block;
2. spokes `v0-T0` and `v4-T1`;
3. spokes `v0-T0` and `v5-T1`;
4. spokes `v1-T0` and `v4-T1`.

Up to path reversal and terminal permutations, these are precisely the same-block, different-terminal spoke pairs whose path vertices have distance at least three. Thus `P6` exposes a clean geometric location for every Newton-cone failure.

## 6. Exact corner certificates for all four exceptional quartics

Reuse the elementary two-corner lemma from the `P5` run: if an integer polynomial `Q(x,z)` has coefficientwise-positive monomial expansions after shifts `x=A+X` and `z=B+Z`, and is positive on the finite rectangle `0<=x<A, 0<=z<B`, then it is positive on all nonnegative integer pairs.

After clearing positive denominators, the checker establishes the following exact certificates:

| exceptional spoke geometry | x-shift | z-shift | residual exact points |
|---|---:|---:|---:|
| `(0,3)` different terminals | `3` | `15` | `45` |
| `(0,4)` different terminals | `9` | `56` | `504` |
| `(0,5)` different terminals | `24` | `153` | `3672` |
| `(1,4)` different terminals | `3` | `17` | `51` |

For each row, **all 15 coefficients** of each shifted quartic are strictly positive and every residual lattice value is positive. The archived output records the exact cleared quartic, every negative Newton coefficient, both shifted minimum coefficients, and the residual-box minimum. No floating-point sign decision is used.

The growth of the worst corner from `(10,50)` at `P5` to `(24,153)` at `P6` is a genuine obstruction to a naive uniform-in-path-length corner bound; the recurrence lemma above is intended to attack that obstruction structurally.

## 7. New all-parameter theorem

### Theorem `T07-RIGHT-P6-FOREST-PNC-13`

For every `p,r>=0` and every two distinct present edges `e,f` of

\[
F^{(6)}_{p,r}=K_{3,6p+r}+\bigl(pP_6\sqcup rK_1\bigr),
\]

\[
\boxed{\Delta_{F^{(6)}_{p,r}}(e,f)\ge0.}
\]

The inequality is strict for every physical edge pair except the degenerate tree `F^{(6)}_{0,1}=K_{3,1}`.

**Proof.** Any pair lies in one of the 81 witness orbits. Expose its one or two distinguished right layers. Marked-layer commutation and the exact nilpotent response reduce the gap to the positive factor `(23396^x4^z)^2` times the corresponding quartic `R_O(x,z)`. For 77 orbits the nonnegative Newton expansion proves nonnegativity on `Z_{>=0}^2`, with strictness except at the unique zero-constant singleton orbit. The remaining four quartics are strictly positive by the exact two-corner certificates in Section 6. Therefore every physical pair has nonnegative Rayleigh difference, and the only equality case is the stated tree. QED.

A direct independent layer check gives for `F^{(6)}_{1,0}`:

\[
|V|=9,\qquad |E|=23,\qquad I(\mathbf1)=326816,
\]

with minimum Rayleigh numerator

\[
\boxed{10756032},
\]

attained by the two endpoint path edges.

## 8. Why this is a genuinely new all-parameter class

For `p>=1`,

\[
|V(F^{(6)}_{p,r})|=3+6p+r,
\qquad
|E(F^{(6)}_{p,r})|=23p+3r.
\]

The graph contains `K_{3,3}`, hence is nonplanar and not series-parallel; it is 3-connected because the underlying `K_{3,6p+r}` already has vertex connectivity three and adding right-side edges cannot reduce connectivity. It is not a wheel: for `p>=1` there are three independent high-degree terminals rather than one hub. It is structurally complementary to NM13-04's triangle-seeded `P5` class: here the terminal triple is independent and the right side contains genuine order-six path components. In particular the first unbounded tail `p>=2` lies far beyond P14's finite order-nine census.

The single `p=1,r=0` graph has nine vertices and 23 edges, so it already lies outside Grimmett–Winkler's published nine-vertex / eighteen-edge computation, although it is covered by the repository's later complete nine-vertex census. The theorem here is not finite enumeration: it proves every `p,r` at once by transfer and sign certificates.

A bounded repository and public-source search found no theorem matching this independent-terminal repeated-`P6` class. That is negative evidence only; **novelty/priority remains UNVERIFIED**.

## 9. Executed exact certificate

Files in this run:

- `2026-09-20T07-40-30Z__p6-path-recurrence-checker.py` — SHA-256 `7b1a5d609bf9515170bb264d3dc420cfbdf5261eb968d170320b63a2e289ef8f`;
- `2026-09-20T07-40-30Z__p6-path-recurrence-checker.out` — SHA-256 `a381dbd9e14a3fc2d79d65545444de04d48967e8090d6d22d09e491d8a902df4`;
- `2026-09-20T07-40-30Z__ledger_delta.yaml`.

The checker reconstructs the 15-state path operator, proves its characteristic/minimal polynomials by exact matrix arithmetic, reconstructs the five-state `P6` transfer, derives the all-parameter forest-count formula, reduces all 1326 witness pairs to 81 exact orbits, computes every quartic and Newton expansion, proves all four corner certificates, checks the unique equality orbit, and directly evaluates every pair in the physical `p=1,r=0` layer. It terminates

`ALL_EXACT_CHECKS_PASS`.

No workflow, external script, paid compute, email, Drive, public posting, permission, schedule, shared root, or peer namespace was modified.

## 10. Residual obstruction and next distinct attack

The parent conjecture remains open because an arbitrary 3-connected graph need not have this three-terminal repeated-layer form. Even within the structured path family, the new recurrence currently controls unmarked tails (and marked responses after their marked prefix) but has not yet been converted into a uniform sign theorem for all `P_l` spoke-pair quartics.

The next materially distinct attack is therefore to use `T07-PATH-TAIL-RECURRENCE-13` to derive a recurrence **in the path length** for the fixed-position different-terminal marked-spoke Rayleigh quartics. The first target is the distance-at-least-three exceptional family identified above. The goal is either an eventual uniform corner bound plus finitely many base path lengths, or a source-valid negative lattice point. Merely running `P7` as an isolated new finite layer is secondary to that recurrence attack.

## ledger_delta summary

Parent theorem: `OPEN -> OPEN`; complete-order metric `9 -> 9`; counterexample-order lower bound `>=10 -> >=10`.

Restricted theorem: `T07-RIGHT-P6-FOREST-PNC-13`, **CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW**.

Mechanism: `P5 two-exception corner proof -> exact path-tail recurrence + P6 four-exception geometric classification and exact corner proof`.

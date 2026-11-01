Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — explicit path-layer coefficient recurrences and a P7 right-layer sign theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending later independent review.** The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and what changed in this run

The preceding NM13-08 report proved pairwise negative edge correlation for

\[
F^{(6)}_{p,r}=K_{3,6p+r}+\bigl(pP_6\sqcup rK_1\bigr),\qquad p,r\ge0,
\]

with three independent terminals. It also constructed a 15-state path-tail operator `E` with minimal polynomial

\[
(\lambda-1)^2(\lambda^2-6\lambda+2)^3,
\]

so every fixed marked response satisfies an order-eight recurrence after the marked prefix is passed. Four `P6` pair orbits left the nonnegative Newton cone and were repaired by exact two-corner certificates.

The newest companion NM13-04 report proves the complementary triangle-seeded `P6` theorem

\[
K_3\vee(pP_6\sqcup rK_1),
\]

and likewise finds four geometric same-layer spoke exceptions. That mathematics is preserved and not duplicated here.

This run does **not** treat `P7` as an unrelated fresh enumeration. It first sharpens the 15-state recurrence to three explicit scalar recurrences for the universal path-layer coefficients `A_n,B_n,C_n`, then uses those recurrences to obtain the exact `P7` transfer. It next performs a refutation-first all-parameter sign calculation for the independent-terminal `P7` family. No negative point appears. Of 110 exact pair orbits, 104 lie in the nonnegative bivariate Newton cone; the six failures are exactly the same-layer, different-terminal spoke pairs at path distance at least three, and all six have rigorous two-corner lattice certificates.

A repository search for `T07-RIGHT-P7`, `7p+r`, and nearby terminology found no prior theorem of this form. `POSTED.md` and the current LIVE20 assignment were checked. External novelty/priority remains **UNVERIFIED**.

## 1. Parent theorem before/after, separately from demonstrated mechanism gain

For a finite graph `G=(V,E)` define its spanning-forest generating polynomial

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\]

and for distinct present edges `e,f`

\[
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit edge weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of `e,f` when a forest is chosen uniformly from **all** acyclic spanning edge subsets, with all component counts mixed.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

The parent metric does not move. This run proves only a new structured infinite class.

**Mechanism before:** order-eight path-tail recurrence plus a complete `P6` sign theorem.

**Mechanism after:** explicit nested annihilators for the unmarked path-layer coefficients,

\[
q(\lambda)=\lambda^2-6\lambda+2,
\]

with `A_n` annihilated by `q`, `B_n` by `q^2`, and `C_n` by `q^3`, together with a complete `P7` all-parameter sign theorem. The first nondegenerate member `F^{(7)}_{1,0}` has ten vertices, so this theorem reaches beyond the repository's complete finite-order census rather than merely reproving a nine-vertex instance.

## 2. Recovered P14 and exact literature scope

The source boundaries remain essential.

1. **Grimmett–Winkler, arXiv:math/0302185 / Random Structures & Algorithms 24 (2004).** They study the uniform measure on **all forests**. Their computation verifies pairwise edge negative correlation for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish the already-known uniform-spanning-tree theorem.
2. **P14/HARD10 repository completion.** The exact dense-nine certificate covers the complementary 19--36 edge sector: all 120,314 unlabeled nine-vertex graphs there and all 25,304,635 present-edge pairs. Together with Grimmett--Winkler this covers all 274,668 unlabeled simple graphs on nine vertices in the source unit-weight scope. P14's block/direct-sum and two-separator arguments, using its recovered fixed-graph unit-to-positive-weight implication, reduce a vertex-minimal source counterexample to a **3-connected** graph. This is a structural reduction, not a general solution.
3. **P14 failed generic routes remain failed.** A generic degree-three star/mesh reduction leaves a mixed three-terminal polarization with no universal sign. Universal mixed-term nonnegativity is false; the proposed reverse-Cauchy rescue was exactly refuted on a physical six-vertex graph while the actual Rayleigh gap remained positive. Lorentzian/complete-log-concavity, naive real stability, and Garding shortcuts still lack the source-matching hypothesis for arbitrary graphic independence polynomials.
4. **Erickson, arXiv:1008.3660.** Erickson proves a stronger all-positive-weight SOS/Rayleigh theorem for **series-parallel** graphs. The class below contains `K_{3,3}` for every `p>=1`, hence is not series-parallel.
5. **Huang, arXiv:2311.00965.** The general arboreal-gas negative-correlation problem is still presented as open while special graphs/parameters are treated.
6. **Bado, DOI 10.1016/j.spl.2026.110960.** Bado proves strict pairwise negative correlation for every wheel under the uniform-all-forests law, an infinite 3-connected non-series-parallel class.
7. **Tang--Zhang, arXiv:2603.10738 (11 March 2026).** Their p-NC results concern specified spanning-subgraph ensembles of complete graphs, including forests with exactly `k` components for fixed `k` and sufficiently large `n`; this is not the arbitrary-graph uniform law mixing all component counts.
8. **Tang--Zhang, arXiv:2609.11578 (10 September 2026).** Their high-degree regular random-cluster theorem includes `Q=0`, but at that endpoint the model is bond percolation conditioned to be connected, not the uniform-all-forests measure here.

A bounded 20 September 2026 search did not locate a source-matching general resolution or a published theorem covering the `P7` family below. This miss is not a priority certificate.

## 3. New decomposition lemma: explicit path-layer coefficient recurrences

Use the five terminal partitions

\[
D=0|1|2,\quad P_{12}=0|12,\quad P_{01}=01|2,\quad P_{02}=02|1,\quad T=012.
\]

For one isolated right vertex,

\[
S=4I+N,\qquad N^3=0,\quad N^2\ne0.
\]

The previously proved terminal-symmetric layer algebra says that the unmarked transfer of a right path `P_n`, every one of whose vertices is adjacent to all three terminals, has the form

\[
T_n=A_nI+B_nN+C_nN^2.
\]

Let

\[
q(\lambda)=\lambda^2-6\lambda+2.
\]

### Lemma `T07-PATH-ABC-RECURRENCE-15`

For every `n>=1`, the path-layer coefficients satisfy

\[
\boxed{A_{n+2}=6A_{n+1}-2A_n,}
\]

\[
\boxed{B_{n+4}=12B_{n+3}-40B_{n+2}+24B_{n+1}-4B_n,}
\]

and

\[
\boxed{C_{n+6}=18C_{n+5}-114C_{n+4}+288C_{n+3}-228C_{n+2}+72C_{n+1}-8C_n.}
\]

Equivalently, `A`, `B`, `C` are annihilated by `q`, `q^2`, `q^3` respectively.

**Proof.** The 15-state path-tail operator `E` from the preceding run is reconstructed independently by the checker. Exact symbolic arithmetic gives

\[
\chi_E(\lambda)=(\lambda-1)^5q(\lambda)^5
\]

and exact minimal polynomial

\[
m_E(\lambda)=(\lambda-1)^2q(\lambda)^3.
\]

Every scalar entry of `T_n` is a fixed initial vector, followed by `E^{n-1}`, followed by a fixed final functional, hence satisfies the order-eight recurrence induced by `m_E`.

Since `T_n=A_nI+B_nN+C_nN^2`, the three coefficient sequences are fixed linear combinations of entries of `T_n`; they also satisfy the same order-eight recurrence. Apply the shift polynomials `q`, `q^2`, `q^3` respectively. Each residual sequence again satisfies the same order-eight recurrence because shift polynomials commute. The exact checker evaluates `T_n` through `n=21` and verifies more than eight consecutive zero residuals for each proposed shorter recurrence. Eight consecutive zeros determine the zero solution of the order-eight recurrence, so each residual vanishes for every later `n`. The displayed recurrences follow. QED.

The initial values begin

\[
(A_1,A_2)=(4,23),
\]

\[
(B_1,B_2,B_3,B_4)=(1,12,103,780),
\]

and

\[
(C_1,C_2,C_3,C_4,C_5,C_6)
=\left(0,\frac53,\frac{85}3,\frac{961}3,\frac{9050}3,25562\right).
\]

The lemma gives immediately

\[
(A_7,B_7,C_7)=(132088,247492,202132).
\]

Thus

\[
\boxed{T_7=132088I+247492N+202132N^2.}
\]

This is a genuine path-length transfer statement, not merely a `P7` table entry.

## 4. The new all-parameter graph class

Define

\[
F^{(7)}_{p,r}:=K_{3,\,7p+r}+\bigl(pP_7\sqcup rK_1\bigr),\qquad p,r\ge0,
\]

where the size-three side consists of three **independent** terminals and the displayed paths/singletons are placed inside the right side.

For `p>=1`,

\[
|V|=3+7p+r,\qquad |E|=27p+3r.
\]

Every such graph is 3-connected: deletion of any two vertices leaves at least one terminal or, if both deleted vertices are terminals, leaves the third terminal adjacent to every surviving right vertex; surviving terminals are connected through any surviving right vertex. Every `p>=1` member contains `K_{3,3}`, so it is nonplanar and not series-parallel.

The family is complementary to NM13-04: its three high-degree terminals are independent, whereas NM13-04 currently treats triangle-seeded right-path families through `P6`. The unit p-NC theorem for the triangle-seeded graph does not imply the theorem after deleting the three triangle edges; such deletion inheritance would require a stronger weighted statement that is not available for those unit-only classes.

The first new nondegenerate point is

\[
F^{(7)}_{1,0},\qquad |V|=10,\quad |E|=27,
\]

so it lies beyond the complete `n<=9` census.

## 5. Nilpotent reduction for repeated P7 layers

Set

\[
a=\frac{247492}{132088},\qquad c=\frac{202132}{132088},\qquad s=\frac14.
\]

After exposing the one or two right layers containing a marked edge pair, if `x` unmarked `P7` layers and `z` unmarked singleton layers remain, division by the positive scalar `132088^x4^z` leaves

\[
U(x,z)=I+uN+vN^2,
\]

where

\[
u=ax+sz,
\]

\[
v=cx+\binom{x}{2}a^2+\binom{z}{2}s^2+xzas.
\]

Thus every marked forest count is a polynomial of total degree at most two in `(x,z)`, and every normalized Rayleigh numerator is a rational quartic.

As a consistency identity, the exact total forest count is

\[
\frac{I_{F^{(7)}_{p,r}}(\mathbf1)}{132088^p4^r}
=
\frac{
45939217548p^2+12259021236pr+26800323172p
+817839363r^2+3543970573r+4361809936
}{4361809936}.
\]

## 6. Exact orbit reduction and the new P7 sign lemma

Take a universal witness with two labelled `P7` blocks and two labelled singleton blocks. It has exactly 60 edges and 1770 unordered edge pairs. The automorphism group generated by terminal `S_3`, swapping the two `P7` blocks, independently reversing each path, and swapping the singletons reduces these to exactly

\[
\boxed{110}
\]

pair orbits.

This witness is exhaustive for local pair types in every `F^{(7)}_{p,r}` because any edge pair meets at most two right components. Once those components are exposed, the remaining counts are nonnegative integers `x,z`, and

\[
\Delta(e,f)=(132088^x4^z)^2R_{\mathcal O}(x,z)
\]

for an exact rational quartic `R_O`.

Expand each quartic in the integer Newton basis

\[
R_{\mathcal O}(x,z)=\sum_{i+j\le4}c^{\mathcal O}_{ij}\binom xi\binom zj.
\]

### Lemma `T07-P7-GEOMETRIC-SIGN-15`

Of the 110 orbit quartics, **104** have no negative Newton coefficient. The six failures are exactly the same-`P7`-block, different-terminal spoke pairs whose path vertices are at distance at least three. Up to path reversal and terminal permutations they are

\[
(0,3),\ (0,4),\ (0,5),\ (0,6),\ (1,4),\ (1,5).
\]

All six exceptional quartics are nevertheless strictly positive on `Z_{>=0}^2`.

**Proof.** The first statement is an exhaustive exact orbit computation. For the six exceptional quartics, clear the positive rational denominator and call the resulting integer quartic `Q(x,z)`. The elementary two-corner lemma says that if `Q(A+X,Z)` and `Q(X,B+Z)` are coefficientwise positive and `Q>0` on the finite residual rectangle `0<=x<A, 0<=z<B`, then `Q>0` on the entire nonnegative lattice.

The exact certificates are:

| spoke positions | x-shift `A` | z-shift `B` | exact residual points |
|---|---:|---:|---:|
| `(0,3)` | 2 | 13 | 26 |
| `(0,4)` | 8 | 55 | 440 |
| `(0,5)` | 24 | 173 | 4,152 |
| `(0,6)` | 60 | 448 | 26,880 |
| `(1,4)` | 3 | 16 | 48 |
| `(1,5)` | 9 | 63 | 567 |

For every row, every nonzero monomial coefficient in both shifted quartics is strictly positive, and every residual lattice value is evaluated exactly and is strictly positive. No floating-point sign decision is used. QED.

The six-exception geometry continues the `P5/P6` pattern but is sharper here: *every* Newton-cone failure is characterized solely by being a different-terminal spoke pair at path distance at least three.

## 7. Restricted theorem

### Theorem `T07-RIGHT-P7-FOREST-PNC-15`

For every `p,r>=0` and every two distinct present edges `e,f` of

\[
F^{(7)}_{p,r}=K_{3,7p+r}+\bigl(pP_7\sqcup rK_1\bigr),
\]

one has

\[
\boxed{\Delta_{F^{(7)}_{p,r}}(e,f)\ge0.}
\]

The inequality is strict for every physical edge pair except in the degenerate tree `F^{(7)}_{0,1}=K_{3,1}`.

**Proof.** Every physical pair belongs to one of the 110 witness orbits. Expose the one or two distinguished right components. Marked-layer commutation and `N^3=0` reduce its Rayleigh numerator to the positive factor `(132088^x4^z)^2` times the exact orbit quartic `R_O(x,z)`. For 104 orbits, nonnegative Newton coefficients prove nonnegativity for all nonnegative integer `(x,z)`; every such orbit has positive constant term except the different-terminal spoke pair on the unique singleton layer, whose remaining Newton coefficients are positive and therefore vanishes only when there are no other layers, namely `K_{3,1}`. The other six quartics are strictly positive by `T07-P7-GEOMETRIC-SIGN-15`. Hence every physical pair is nonnegative, with exactly the stated equality case. QED.

An independent direct computation on the first ten-vertex member gives

\[
I_{F^{(7)}_{1,0}}(\mathbf1)=2,334,848
\]

and minimum Rayleigh numerator

\[
\boxed{413,667,072},
\]

attained by the path-edge pair `(0,1)` and `(4,5)` in the right `P7` block.

## 8. What moved, and what did not

**Parent theorem:** `OPEN -> OPEN`; all-graph order metric `9 -> 9`; counterexample-order lower bound `>=10 -> >=10`.

**Demonstrated mechanism gain:**

- before: one order-eight path-tail recurrence plus a complete `P6` family;
- after: explicit `q,q^2,q^3` recurrences for the universal path coefficients `A_n,B_n,C_n`, plus the complete `P7` all-parameter family;
- finite sign complexity at `P7`: `104/110` orbit quartics lie in the Newton cone and the remaining six have exact global lattice certificates.

This is more than finite enumeration because the nilpotent transfer proves every `p,r` simultaneously. It is still only a restricted theorem: arbitrary 3-connected graphs need not admit the three-terminal right-path decomposition.

The main residual obstruction is now quantitative. The furthest-endpoint exceptional orbit requires corner thresholds `(60,448)` at `P7`, compared with `(24,153)` at `P6`. A uniform-in-path-length theorem will therefore need the spectral recurrence itself, not a hope that the finite corner thresholds stay bounded.

## 9. Essential exact certificate

The executed checker

`2026-09-20T09-17-30Z__p7-path-recurrence-checker.py`

uses integer/rational arithmetic throughout. It:

1. reconstructs the five-state terminal transfer and verifies `N^3=0`;
2. reconstructs the 15-state path-tail matrix and its characteristic/minimal polynomials;
3. reconstructs `T_n` through `n=21` and proves the `A/B/C` coefficient recurrences by exact recurrence propagation;
4. verifies `T_7=132088 I+247492 N+202132 N^2` and the all-parameter forest-count formula;
5. reduces all 1770 witness pairs to 110 automorphism orbits;
6. computes every exact normalized Rayleigh quartic and every Newton coefficient;
7. certifies the 104 Newton-positive orbits and all six exceptional two-corner certificates, including all 32,113 residual lattice evaluations;
8. independently computes the ten-vertex `F^{(7)}_{1,0}` forest count and all 351 physical edge-pair Rayleigh numerators.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

## 10. Next attack

Do **not** merely increment to `P8` and repeat the orbit census. The next materially useful step is to combine the path-tail spectrum with marked-spoke responses. For each fixed relative spoke geometry, derive the recurrence in the path length for the coefficients of the normalized Rayleigh quartic and exploit the dominant root `3+sqrt(7)` of `q`. The goal is either:

- an eventual positive shifted-cone theorem plus finitely many base path lengths, which would convert the `P3`--`P7` ladder into an arbitrary-path result; or
- an exact negative lattice point, which would provide a source-valid counterexample within this structured 3-connected family.

Refutation remains first: any recurrence-derived sign reversal should be checked exactly before attempting another positive certificate.

## 11. ledger_delta

See sibling file `2026-09-20T09-17-30Z__ledger_delta.yaml`.

`END OF REPORT`

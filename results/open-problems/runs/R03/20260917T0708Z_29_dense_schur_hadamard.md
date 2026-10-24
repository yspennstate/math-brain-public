Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed task interface still has no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the fixed replay-certified metric: `r(10)=222.610473674316849...` remains exact and `r(11)<=523.907004072269228...` remains the best certified bound; consecutive unchanged count `0 -> 1`. Section-B methods actually used: **#2 ATTACK THE NEGATION FIRST; #3 PROVE SOMETHING STRONGER; #12 FIND WHAT IS CONSERVED.**

# R03 run29 — dense Schur reduction and Hadamard obstruction

Run ID: `20260917T0708Z_29_dense_schur_hadamard`  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source gate, ownership and fixed metric

I continued from

`runs/R03/20260917T0602Z_28_primary_n9_schur_reduction.md`

and did not restart the problem, reset the killed-route ledger, or substitute a different metric.

Before new mathematics I recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical `F0001` history, newest own run28, and newest neighboring R04 retirement/handoff state. The large intake JSONL corpus is connector-truncated, so this is a targeted source/ownership recovery rather than a claim that every approximately 780-row intake file was rendered byte-for-byte. No posted exclusion or competing ownership claim was found for the assigned R03 target.

The dated source/current-status record is

`artifacts/R03/20260917T0708Z_29_source_status.md`.

The primary modern source remains Jain--Sah--Sawhney, arXiv:2010.06554v2, Conjecture 1.1. For iid uniform signs,

\[
P(E_{e_1})=0,
\qquad
P(E_{e_1-e_2})=P(E_{e_1+e_2})=2^{-n},
\]

so the source specialization is exactly

\[
\boxed{
P(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}.
}
\tag{1.1}
\]

Let `T_n` be the exact union of all equal/opposite signed row-pair and column-pair events. Retained C225 controls their overlaps. The fixed metric remains

\[
\boxed{r(n)=2^nP(\det B_n=0,T_n^c),}
\tag{1.2}
\]

and source closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

Run28 made `r(10)` exact using the newly recovered primary order-nine computation:

\[
\boxed{r(10)=222.6104736743168493957921796888577\ldots}
\tag{1.4}
\]

and the strongest retained `n=11` bound is

\[
\boxed{r(11)\le523.907004072269227999\ldots .}
\tag{1.5}
\]

Those do not move this run.

Fresh bounded 2026-09-17 arXiv searches again found JSS's uniform-support gap, Song--Wang's growing-corank theorem, Hunter--Kwan--Sauermann--Sawhney's large-corank theorem, and the Sahasrabudhe survey, but no later primary proof of the sharp iid nonsymmetric Rademacher prefactor. This is a bounded-search statement, not a worldwide novelty certificate.

A crucial continuity correction came from rereading the older R03 history: run13 already proved **C238/C239**, importing JSS Theorem 1.5 plus explicit Bonferroni subtraction to show that, after signed row/column collisions are removed, the almost-constant/structured null-vector sector contributes only `o(2^{-n})`. I therefore do **not** re-prove that lemma here. Run28 explicitly left one next-run obligation: combine that retained linear-support localization with the exact cofactor weight `s_L(B)s_R(B)` in C277 instead of the wasteful universal lower bound `9`. Sections 3--4 do exactly that.

## 2. Method #2 — ATTACK THE NEGATION FIRST: pointwise Schur anticoncentration is false

Run28 rewrote the real-corank-one residual as the inverse-bilinear event

\[
c^TA^{-1}b\in\{-1,+1\}
\tag{2.1}
\]

for an invertible sign minor `A`, after deleting the border choices that recreate signed row/column collisions. A tempting next statement would be a pointwise exponentially small bound in `(A,b)`. I first tried to refute that before proving an averaged theorem.

### R03-C279 — Hadamard cores give an infinite pointwise obstruction

**STATUS: PROVED.** Let `H` be a normalized Hadamard matrix of order `d+1`, and write

\[
H=\begin{pmatrix}1&\mathbf1^T\\ \mathbf1&A\end{pmatrix},
\qquad A\in\{\pm1\}^{d\times d}.
\tag{2.2}
\]

Hadamard orthogonality gives

\[
A\mathbf1=-\mathbf1,
\qquad
A^T\mathbf1=-\mathbf1,
\qquad
AA^T=(d+1)I-J,
\tag{2.3}
\]

so `A` is invertible. In particular

\[
A^{-1}\mathbf1=-\mathbf1.
\tag{2.4}
\]

Neither `+1` nor `-1` is equal up to sign to a column of `A`: every column sum is `-1`, while the constant sign columns have sum `\pm d`. Thus `b=\pm\mathbf1` survives the collision deletion.

For `b=\mathbf1`, equation (2.1) becomes

\[
-\sum_{i=1}^dc_i\in\{-1,+1\},
\tag{2.5}
\]

and for `b=-\mathbf1` it is the same condition. Since `d` is odd, the number of sign vectors `c` with sum `\pm1` is

\[
2\binom d{(d-1)/2}.
\tag{2.6}
\]

Every row of `A` has sum `-1`; hence the `2d` forbidden vectors `\pm`row`_i(A)` are among the solutions in (2.6), and they are distinct because `A` is invertible. Therefore each of the two constant `b` choices leaves exactly

\[
2\binom d{(d-1)/2}-2d
\tag{2.7}
\]

admissible `c`'s. Consequently

\[
\boxed{
\Xi_\pm^\circ(A)
\ge4\binom d{(d-1)/2}-4d
=\Theta(2^d/\sqrt d).
}
\tag{C279}
\]

Sylvester Hadamard matrices give this for the infinite sequence `d=2^k-1`. Thus a proof of the sharp singularity asymptotic **cannot** proceed by demanding exponentially small Schur small-ball probability for every invertible `A` and every admissible `b`; exceptional minors with polynomial-scale pointwise concentration genuinely exist.

This does not create a source-scale counterexample, because a fixed Hadamard core is extraordinarily rare among all sign minors. It says the missing ingredient must exploit the **distribution/rarity of `A`**, not only a worst-case Littlewood--Offord bound conditional on `A`.

### A stronger finite obstruction already inside a bilaterally unstructured sector

The exact checker also tests the Walsh-Hadamard core of order `16`. Let `A` be the `15 x 15` core of the normalized Walsh matrix and let, on the nonzero vectors `x in F_2^4`,

\[
b_x=(-1)^{x_1x_2+x_3x_4}.
\tag{2.8}
\]

The quadratic sign function is bent. The checker verifies exactly

\[
\det A=268435456,
\qquad
A^{-1}b\in\{0,-1/2\}^{15},
\tag{2.9}
\]

with nine zero coordinates and six `-1/2` coordinates. Hence the bordered right-null direction `(-A^{-1}b,1)` is **not** in `Cons(1/4,1/4)`.

For this single admissible pair `(A,b)`, the exact count is

\[
\#\{c:c^TA^{-1}b=\pm1\}=15360.
\tag{2.10}
\]

After deleting all `\pm`row collisions, `15330` remain. An exact rational test of the left-null vector `(-A^{-T}c,1)` shows that

\[
\boxed{14622}
\tag{2.11}
\]

of those completions have **both** normalized null directions outside `Cons(1/4,1/4)`.

This is only a finite obstruction, not an asymptotic counterexample. But it is concrete evidence that even after structured-vector deletion one cannot expect a useful pointwise-in-`(A,b)` exponential estimate. The asymptotic proof has to average over the minor `A` (and probably over `b`) or quantify how rare such highly arithmetic inverse images are.

The checker for C279 and (2.8)--(2.11) is

`artifacts/R03/20260917T0708Z_29_dense_schur_hadamard_exact.py`

with archived output

`artifacts/R03/20260917T0708Z_29_dense_schur_hadamard_exact.out`.

It uses only exact integer/rational arithmetic and ends with both `SELF-CHECK PASS` markers.

## 3. Method #12 — FIND WHAT IS CONSERVED: the cofactor-support mass

The useful quantity in run28 C277 is not merely the number of residual corank-one matrices. For a corank-one sign matrix `B`, if `u` and `v` span its right and left nullspaces, then

\[
\operatorname{adj}(B)=\kappa vu^T
\tag{3.1}
\]

for `\kappa\ne0`. Hence the number of invertible codimension-one minors is exactly

\[
\boxed{s_R(B)s_L(B),}
\tag{3.2}
\]

where `s_R,s_L` are the support sizes of `u,v`. Row/column sign switches do not change this zero pattern. This cofactor-support mass is the conserved weight that lets the JSS linear-support theorem cancel the `n^2` loss in run28.

It is cleaner to formulate the next reduction directly in the sign model rather than pass back through the binary normalization.

For an invertible

\[
A\in\{\pm1\}^{(n-1)\times(n-1)},
\]

let `Col(A)` and `Row(A)` be its signed column and row sets. Define

\[
\Xi_\pm^\circ(A)
:=\#\Bigl\{(b,c)\in\{\pm1\}^{n-1}\times\{\pm1\}^{n-1}:
 b\notin\pm\mathrm{Col}(A),\ c\notin\pm\mathrm{Row}(A),\ c^TA^{-1}b\in\{\pm1\}\Bigr\}.
\tag{3.3}
\]

For a block matrix

\[
B=\begin{pmatrix}A&b\\c^T&d\end{pmatrix},
\tag{3.4}
\]

the Schur identity gives

\[
\det B=\det A\,(d-c^TA^{-1}b).
\tag{3.5}
\]

Thus (3.3) counts exactly the collision-free singular sign completions for this chosen invertible minor. Since `A` is invertible, every such completion has real corank exactly one. Summing over the `n^2` possible deleted row/column positions gives the direct-sign analogue of C277:

\[
\boxed{
n^2\sum_{\det A\ne0}\Xi_\pm^\circ(A)
=\sum_{B\in\mathcal R_{n,\pm}^{(1),\circ}}s_L(B)s_R(B).
}
\tag{3.6}
\]

Here `R_{n,pm}^{(1),circ}` is the set of collision-free sign matrices of real rank `n-1`.

The exact checker verifies (3.6) independently at sign order `n=5`:

- invertible sign `4 x 4` minors: `22272`;
- `sum_A Xi_pm^circ(A)=589824`;
- collision-free dephased rank-four classes: `1800`;
- weighted cofactor sum over those classes: `28800`;
- row/column-switch orbit size: `512`;
- full weighted sign sum: `14745600`;
- `5^2 * 589824 = 14745600` exactly;
- every residual class has exactly `16` nonzero cofactors.

This is a self-check of the finite core of the direct-sign reformulation, not an independent audit.

## 4. Method #3 — PROVE SOMETHING STRONGER: C280, an equivalent dense-unstructured Schur target

Run28's C278 used only the universal bound `s_Ls_R>=9`, leading to a sufficient condition with an unnecessary `n^2` loss. The retained JSS C238/C239 result lets us remove that loss and also discard the pointwise structured pathology exhibited in Section 2.

Let `delta,rho>0` be constants for which JSS Theorem 1.5 applies to the Rademacher law. Replacing them by smaller positive constants if necessary, we may take

\[
0<\delta\le1/4,
\qquad
0<\rho\le1/4,
\tag{4.1}
\]

because `Cons(delta',rho')` is a subset of `Cons(delta,rho)` when both parameters are decreased, so the same JSS upper bound remains valid on the smaller set. For sufficiently large `n`, the elementary signed pair directions still lie in this smaller `Cons` set, and the retained C238 Bonferroni subtraction applies unchanged.

Call a collision-free real-corank-one sign matrix `B` **UU** if both its normalized left and right null directions lie in

\[
\operatorname{Noncons}(\delta,\rho)
:=S^{n-1}\setminus\operatorname{Cons}(\delta,\rho).
\tag{4.2}
\]

A nonzero vector with support at most `delta n` has at least `(1-delta)n` zero coordinates and therefore lies in `Cons(delta,rho)`. Hence every UU matrix satisfies

\[
s_L(B)>\delta n,
\qquad
s_R(B)>\delta n.
\tag{4.3}
\]

For a fixed invertible `A`, define `Xi_pm^UU(A)` to be the number of pairs counted in (3.3) for which the two bordered null directions

\[
u=(-A^{-1}b,1),
\qquad
v=(-A^{-T}c,1)
\tag{4.4}
\]

normalize into `Noncons(delta,rho)`. Let

\[
\boxed{
q_n^{UU}
:=2^{-(n^2-1)}\sum_{\det A\ne0}\Xi_\pm^{UU}(A).
}
\tag{4.5}
\]

Exactly the same cofactor double count as (3.6), now restricted to UU matrices, gives

\[
 n^2\sum_A\Xi_\pm^{UU}(A)
=\sum_{B\in\mathcal R_{n,\pm}^{UU}}s_L(B)s_R(B).
\tag{4.6}
\]

Using (4.3) and the trivial upper bound `s_Ls_R<=n^2`,

\[
\delta^2 n^2|\mathcal R_{n,\pm}^{UU}|
< n^2\sum_A\Xi_\pm^{UU}(A)
\le n^2|\mathcal R_{n,\pm}^{UU}|.
\tag{4.7}
\]

Cancel `n^2`, divide by the total number `2^{n^2}` of sign matrices, and use (4.5):

\[
\boxed{
2^{n-1}q_n^{UU}
\le
2^nP(B_n\in\mathcal R_{n,\pm}^{UU})
\le
\delta^{-2}2^{n-1}q_n^{UU}.
}
\tag{4.8}
\]

Retained C238/C239 says that the collision-free corank-one matrices with at least one structured null direction contribute `o(1)` after multiplication by `2^n`. Retained higher-corank control from C244/C278 gives another `o(1)` normalized contribution. Therefore

\[
\boxed{
r(n)
=2^nP(B_n\in\mathcal R_{n,\pm}^{UU})+o(1).
}
\tag{4.9}
\]

Combining (4.8)--(4.9) proves the new reduction:

### R03-C280 — dense-unstructured Schur equivalence

**STATUS: PROVED REDUCTION.** For the fixed JSS constants chosen above,

\[
\boxed{
2^{n-1}q_n^{UU}
\le r(n)
\le \delta^{-2}2^{n-1}q_n^{UU}+o(1).
}
\tag{C280.1}
\]

Consequently the original sharp Rademacher singularity conjecture is equivalent to

\[
\boxed{
q_n^{UU}=o(n^2 2^{-n}).
}
\tag{C280.2}
\]

This is strictly stronger than run28's sufficient reduction. It fulfills the exact next-run obligation recorded there:

1. the structured/null-support sector is not re-proved; it is imported at the correct `o(2^{-n})` scale from retained C238/C239;
2. the exact cofactor weight converts linear left/right support into an `n^2` gain;
3. the remaining scalar is an **average over invertible minors and border signs**, not a worst-case conditional small-ball probability;
4. C279 and the bent-Walsh certificate show concretely why this averaging is necessary.

No source theorem is claimed. C280 is a source-equivalent reformulation of the unresolved dense/unstructured corank-one sector.

## 5. What the next proof must actually contain

C280 isolates the remaining problem more sharply than the earlier modular or bounded-support routes. One now needs target-scale control of

\[
c^TA^{-1}b\in\{\pm1\}
\tag{5.1}
\]

**on average over random invertible sign `A` and admissible `b,c`, after both bordered null directions are required to be JSS-unstructured.** A pointwise Littlewood--Offord theorem is insufficient and, by C279 plus the bent-Walsh certificate, false at the scale one would need.

The algebraic form

\[
c^T\operatorname{adj}(A)b=\pm\det A
\tag{5.2}
\]

suggests that the useful information has to be distributional in the cofactor vector / inverse image, or a metric-entropy statement for the ensemble of arithmetic profiles `A^{-1}b`. The JSS proof itself says the unstructured uniform-support case is precisely where the entropy-gap mechanism degenerates. A bounded current search for the exact collision-deleted Schur statistic (5.1) did not locate a published theorem at the needed `n^2 2^{-n}` scale; this is not a novelty certificate.

A reasonable next attack, distinct from the killed routes, is to stratify admissible `(A,b)` by the additive energy / concentration profile of `A^{-1}b` and prove that the high-concentration strata occupy at most `o(n^2 2^{-n})` of the **joint** `(A,b,c)` space. Hadamard/bent cores should be test objects for that stratification: they have very high pointwise concentration but should pay an enormous entropy cost in the `A` coordinate.

## 6. Fixed metric and stuck accounting

The fixed complete-domain upper envelope does **not** move in this run. Retain all exact values through `n=10`, in particular C276 (1.4), retain (1.5) at `n=11`, and retain every earlier certified all-`n` branch thereafter. C279/C280 change the asymptotic route, not the numerical full-domain upper envelope.

Therefore the consecutive unchanged count is

\[
\boxed{0\to1.}
\]

This is not a stuck episode. The source remains **OPEN** and R03 remains **PARTIAL**.

The older killed routes remain killed with no stagnation reset: fixed-epsilon JSS diagonalization X27, naive conditional row/column independence X28, fixed-best-prime X29, naive multiplication of left/right-null probabilities, worst-case universal modular-rank floors, bounded-support sparse-plane enumeration as an asymptotic strategy, and any exponential-rate estimate presented as though it settled the polynomial prefactor.

## 7. Neighbor/audit obligation

The newest recovered R04 state is

`runs/R04/20260917T0310Z_i0027_retirement_handoff.md`.

It is a retirement/handoff report and introduces no new theorem claim or finite checker requiring a fresh R03 audit. Earlier R03 audits of the R04 source-closing chain remain historical; I did not manufacture a duplicate audit.

R03 itself still lacks a P26 end-to-end audit of the current package and lacks a second distinct current-package closure audit. The retained `R02-AUDIT-R03-C253-04=PASS` is claim-scoped only.

## 8. Model/runtime and permission state

The controlling repository policy still says that the exposed scheduler mutation interface has prompt/title/schedule/timing/enabled controls but **no model-family field, no reasoning-effort field, and no authenticated runtime telemetry**. Hence GPT-6 maximum remains a prompt request only; this report does not pretend it was enforced.

The historical `You cannot modify this task` response for P26/P01/P03 is consistent with an ownership/workspace boundary; P26 later updated from a different authorized context. The legitimate fix is an owning/admin-authorized product surface that exposes model controls, or platform support. No duplicate task, permission bypass, scheduler edit, email, Drive write, public post, workflow execution or purchase was attempted.

## 9. Artifacts and ledger delta

Exact checker:

`artifacts/R03/20260917T0708Z_29_dense_schur_hadamard_exact.py`

Checker creation commit: `9c224a3544638a8b650c603e552d95f56b9ae673`.

Archived checker output:

`artifacts/R03/20260917T0708Z_29_dense_schur_hadamard_exact.out`

Output creation commit: `e6476b68495d88efbfd1cbe841f2c9500884101b`.

Dated source/status artifact:

`artifacts/R03/20260917T0708Z_29_source_status.md`

Status creation commit: `668ebf72876f06a8c5130afbd5df99cd09ee11e6`.

```yaml
ledger_delta:
  worker: R03
  target: sharp iid Rademacher singularity prefactor
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: smallest replay-certified full-domain upper envelope for r(n)=2^n P(det B_n=0,T_n^c)
  metric_before:
    r10: 222.6104736743168493957921796888577_exact
    r11_upper: 523.907004072269227999...
  metric_after:
    r10: 222.6104736743168493957921796888577_exact
    r11_upper: 523.907004072269227999...
  movement: none
  unchanged_count_before: 0
  unchanged_count_after: 1
  methods: [2,3,12]
  new_claims:
    - R03-C279: normalized Hadamard cores obstruct worst-case pointwise Schur anticoncentration; exact d=7 and bent-Walsh n=16 certificates archived
    - R03-C280: dense-unstructured Schur equivalence; source closes iff q_n^UU=o(n^2 2^-n)
  retained_key_claims:
    - C238/C239 JSS structured-sector payment
    - C276 exact r(10)
    - C277 Schur/cofactor incidence identity
    - C278 higher-corank/dense corank-one reduction
  closure_audits:
    p26_current_package: absent
    second_distinct_current_package: absent
  next_obligation: average inverse-bilinear anticoncentration over (A,b,c), exploiting entropy cost of high-concentration inverse images; pointwise bounds are ruled out by C279
```

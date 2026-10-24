Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **METRIC MOVED:** `K_5^* <= sqrt(100/31)` -> **`K_5^* = T_* = (2 sqrt(2)+3 sqrt(3)+2 sqrt(51+3 sqrt(6)))/13 = 1.792447191483282763...`**; the complete certified envelope improves in **73 dimensions**. Methods actually used: **#3 PROVE SOMETHING STRONGER, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE.**

# R13 — Boolean Komlós: exact determination of the five-column constant

Run ID: `20260918T1314Z_k5-exact-equality-7c2f`  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Deployment: `NEW-METHODS-2026-09-16`.

## 1. Continuity, ownership, and source status

The target remains the **real Boolean** Komlós signing problem. For a real `m x n` matrix `A` whose columns have Euclidean norm at most one,

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{-1,+1\}^n}\|A\varepsilon\|_\infty,
\qquad
K_n^*=\sup_A \operatorname{disc}(A).
\]

R13's fixed tracked quantity remains the complete rigorously certified pointwise upper envelope `B_R13(n)`; complex phases, rank-two/vector colorings, and average-case bounds do not count as Boolean solutions.

Before new mathematics I reread or recovered the required controlling state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042/R13 history, the newest R13 complete report, and current neighboring R12/R16 state. `QUEUE.md` continues to reserve Boolean Komlós to R13 rather than the unassigned pool. R12 and R16 have moved to unrelated outside targets, so there is no current ownership collision.

The immediately preceding complete R13 report was

`runs/R13/20260918T1205Z_k5-c31-symmetry-b7e4.md`

at commit `6a9c56b252dfd06ac9000dab58f9f3e26f659923`. It proved

\[
K_5^*\le \sqrt{100/31}=1.796053020267749\ldots
\]

and retained the exact lower obstruction

\[
T_*=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
=1.792447191483282763\ldots .
\]

After that report, the repository acquired an unreported exact finite-check tail at `c_1=311249/10^6`, an exceptional-orbit verifier, and an exact symbolic postcheck. This run continues from that state rather than restarting the finite search.

### Current source check — 18 September 2026

The current literature separation remains:

- Bansal--Jiang, arXiv:2508.03961v2, gives the earlier real-Boolean `\widetilde O((\log n)^{1/4})` Komlós bound.
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 September 2026, states the unrestricted real-sign bound `3\sqrt{2\pi}`. Thus the qualitative dimension-free Boolean Komlós problem is **KNOWN in the current preprint literature**; R13 is a quantitative finite-dimensional track.
- Guillen--Kobzar, arXiv:2609.15071v1, submitted 14 September 2026, allows arbitrary unit-modulus complex phases; for real inputs this is rank-two vector discrepancy and is not a Boolean-sign substitute.
- Belhaouari--AlQudah, *Contemporary Mathematics* 5(3) (2024), DOI `10.37256/cm.5320244110`, advertises a lower-dimensional value for `K(5)` under the same Komlós convention. R13 previously produced an exact admissible `5 x 5` obstruction strictly above their advertised value, so that equality cannot be correct as stated.
- Kunisky's unsatisfiable-matrix framework gives a much stronger asymptotic lower bound for the unrestricted universal constant, approaching `1+sqrt(2)`; it does not determine the exact finite-five constant proved below.

Fresh bounded searches for the exact radical, decimal `1.792447191483...`, and its degree-eight minimal polynomial did not locate a matching finite-five theorem. This is only bounded negative evidence: **novelty remains UNVERIFIED**.

## 2. Main theorem: the five-column constant is exact

### Theorem R13-C40

For every real matrix with exactly five columns and column Euclidean norms at most one,

\[
\boxed{
\operatorname{disc}(A)\le
T_*:=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
}.
\]

Moreover there is an explicit real `5 x 5` unit-column matrix whose Boolean discrepancy is exactly `T_*`. Hence

\[
\boxed{
K_5^*=T_*
=1.79244719148328276329032036724\ldots
}.
\]

The exact value satisfies

\[
28561T_*^8-161564T_*^6+271782T_*^4-161564T_*^2+28561=0.
\]

The proof below separates the exact lower obstruction from the universal five-column upper bound.

---

# 3. Method #3 — PROVE SOMETHING STRONGER: target equality, not another nearby upper bound

The preceding run left only a gap of about `0.003606` between an exact lower obstruction and the upper theorem. Instead of improving the rational upper parameter again, I used the exact obstruction itself as the target scale.

Write

\[
T=T_*,\qquad
c_*=T^{-2}=0.311248495646606345158346862955\ldots .
\]

The already executed finite check used the slightly larger rational number

\[
c_1=\frac{311249}{10^6}
=0.311249,
\qquad
c_1-c_*=5.0435339365\ldots\times10^{-7}>0.
\]

Thus every finite certificate proved at `c_1` remains valid at the exact smaller parameter `c_*`. The only finite configurations not certified at `c_1` can be isolated and treated symbolically at `c_*`.

This converts the previous “push the upper constant” problem into a stronger exact-equality problem.

## 4. Exact lower obstruction

Let

\[
b=\frac1{\sqrt3},\qquad d=\frac1{\sqrt2},\qquad
 a=\frac{T-b}{2},\qquad c=\frac{T-d}{3}.
\]

The defining radical satisfies

\[
2a+b=T,\qquad 3c+d=T,\qquad a^2+c^2=\frac12,
\]

with `a,b,c,d>0`. Define

\[
A_*=
\begin{pmatrix}
0&a&0&a&b\\
-a&0&0&a&-b\\
a&a&0&0&-b\\
-c&c&-d&-c&0\\
-c&c&d&-c&0
\end{pmatrix}.
\tag{4.1}
\]

Every column of `A_*` has squared Euclidean norm exactly one. Every row has `\ell_1` norm exactly `T`; hence for every Boolean signing `\varepsilon`,

\[
\|A_*\varepsilon\|_\infty\le T.
\tag{4.2}
\]

The exact obstruction checker enumerates all 32 Boolean signings. For every signing, at least one row of `A_*` has dot product exactly `+T` or `-T`. Therefore

\[
\|A_*\varepsilon\|_\infty=T
\quad\hbox{for every }\varepsilon\in\{\pm1\}^5,
\]

and consequently

\[
\boxed{\operatorname{disc}(A_*)=T},\qquad K_5^*\ge T.
\tag{4.3}
\]

This lower half was already certified in R13's exact obstruction history; the new work is to match it from above.

---

# 5. Upper-bound setup at the exact scale

Assume for contradiction that a real matrix `A` with five unit-bounded columns satisfies

\[
\operatorname{disc}(A)>T.
\]

Scale the rows by `1/T`. Every scaled column then has squared Euclidean energy at most

\[
c_*=T^{-2}.
\tag{5.1}
\]

Fix one representative of each antipodal Boolean sign class by requiring the first coordinate to be `+1`; there are 16 projective classes. For each class choose a row witnessing discrepancy strictly larger than one, orient the class so the corresponding row dot product is `>1`, and delete unused rows. The active rows partition the 16 projective classes into nonempty oriented blocks

\[
B_1,\ldots,B_q.
\]

If `r_i` is the active scaled row assigned block `B_i`, then

\[
r_i\cdot t>1\qquad(t\in B_i).
\tag{5.2}
\]

For a block `B` let

\[
v_B=\sum_{t\in B}t,\qquad k=|B|.
\]

Summing (5.2) gives

\[
r\cdot v_B>k.
\tag{5.3}
\]

For any positive diagonal matrix

\[
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_5),
\qquad \sum_j\lambda_j=1,
\]

weighted Cauchy implies

\[
r^T\Lambda r>
\frac{k^2}{v_B^T\Lambda^{-1}v_B}.
\tag{5.4}
\]

At the same time, if `E_j` is the squared scaled energy in column `j`, then

\[
\sum_i r_i^T\Lambda r_i
=\sum_j\lambda_jE_j
\le c_*.
\tag{5.5}
\]

The subset version retained from the preceding run is stronger: for every nonempty `U\subseteq B`,

\[
r\cdot u_U>|U|,
\qquad u_U=\sum_{t\in U}t,
\]

so

\[
r^T\Lambda r>
\psi_\Lambda(B):=
\max_{\varnothing\ne U\subseteq B}
\frac{|U|^2}{u_U^T\Lambda^{-1}u_U}.
\tag{5.6}
\]

A zero subset sum is an immediate contradiction to the strict witness inequalities.

## 6. Analytic active-row regimes

### `q<=3`

The retained partial-rounding lemma applied to the active `q`-row submatrix gives a Boolean signing with Euclidean norm at most `\sqrt q`. Therefore

\[
\|A_{\rm active}\varepsilon\|_\infty
\le\sqrt3<T,
\]

because `T^2>3`. This contradicts the assumption that every signing has active infinity norm `>T` before scaling.

### `q>=6`

For a block of size `k`, exact projective-cube optimization gives the largest squared norm `M_k` of an oriented block sum. The retained table is

\[
(M_1,\ldots,M_{16})=
(5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256).
\]

Hence (5.3) and ordinary Cauchy force total scaled row energy strictly larger than

\[
\sum_i\frac{k_i^2}{M_{k_i}}.
\]

Exact partition optimization for `q>=6`, `\sum k_i=16`, gives

\[
\min\sum_i\frac{k_i^2}{M_{k_i}}
=\frac{49}{30},
\tag{6.1}
\]

attained at profile `(1,1,1,1,4,8)`. But the total available scaled Frobenius energy is at most `5c_*`, and the exact postcheck verifies

\[
\frac{49}{30}>5c_*.
\tag{6.2}
\]

Thus `q>=6` is impossible.

Only `q=4,5` remain.

---

# 7. The finite core at `c_1=311249/10^6`

The exact C++ finite checkers use integer/rational comparisons for every accepted certificate. Their search target is the slightly *harder* energy allowance `c_1>c_*`.

For four active rows, all 34 sorted block profiles are included. After safe norm pruning, three disjoint exhaustive segments contain

\[
69{,}245{,}080,
\qquad
113{,}371{,}000,
\qquad
105{,}346{,}400
\]

oriented configurations, for a total of

\[
\boxed{287{,}962{,}480}.
\tag{7.1}
\]

Every q=4 configuration is exactly certified at `c_1`. Therefore every q=4 configuration is also excluded at `c_*<c_1`.

For five active rows, exact profile screening leaves 22 profiles and the checker exhausts

\[
\boxed{6{,}047{,}460}
\tag{7.2}
\]

oriented configurations. Of these, all but **160** receive a rational full-block or subset diagonal certificate already at `c_1`. The surviving 160 configurations are all in the profile

\[
(2,2,4,4,4).
\tag{7.3}
\]

No claim is made that the rational `c_1` checker alone proves the theorem; the point of the next two methods is that the 160 residuals collapse exactly to one analytic object.

---

# 8. Method #18 — SAY IT IN ANOTHER LANGUAGE: the 160 residual configurations are one group orbit

Instead of regarding the 160 residuals as 160 unrelated failed certificates, rewrite them under the natural signed-coordinate action on the projective five-cube.

The exact postcheck parses every residual and verifies that the 160 distinct configurations are **exactly one orbit** under coordinate permutations together with coordinate sign changes. A representative has encoded blocks

`((2,3,3),(2,12,12),(4,1440,160),(4,20560,20560),(4,43520,43520))`.

Decoded into oriented cube vectors, its five block sums are

\[
\begin{aligned}
v_1&=(2,0,-2,-2,-2),\\
v_2&=(2,0, 2,-2,-2),\\
v_3&=(0,4,0,4,-4),\\
v_4&=(4,-4,0,4,0),\\
v_5&=(4,4,0,0,4),
\end{aligned}
\tag{8.1}
\]

with block sizes `(2,2,4,4,4)`.

Thus it is enough to prove one exact diagonal-dual identity for (8.1); signed coordinate permutations carry it to every residual.

## 9. Exact dual certificate for the exceptional orbit

Retain the obstruction parameters `a,b,c,d,T` from Section 4 and define

\[
D=3+\frac ab+\frac cd,
\qquad
p=\frac1D,
\qquad
q=\frac{pa}{b},
\qquad
r=\frac{pc}{d}.
\tag{9.1}
\]

Then

\[
p,q,r>0,\qquad 3p+q+r=1.
\tag{9.2}
\]

Use

\[
\Lambda=\operatorname{diag}(p,q,r,p,p).
\tag{9.3}
\]

For each of the two size-two blocks in (8.1), the full-block contribution in (5.4) is

\[
\frac{pr}{p+3r}.
\tag{9.4}
\]

For each of the three size-four blocks, the contribution is

\[
\frac{pq}{p+2q}.
\tag{9.5}
\]

The exact symbolic postcheck proves

\[
\frac{pr}{p+3r}=\frac{pc}{T},
\qquad
\frac{pq}{p+2q}=\frac{pa}{T},
\tag{9.6}
\]

and

\[
T(3a+2c)=D.
\tag{9.7}
\]

Therefore the total lower bound is exactly

\[
2\frac{pr}{p+3r}
+3\frac{pq}{p+2q}
=
\frac{p(2c+3a)}{T}
=
\frac1{T^2}
=c_*.
\tag{9.8}
\]

But every witness inequality in (5.2) is strict, so (5.4) is strict row by row. Hence for the representative exceptional configuration,

\[
\sum_i r_i^T\Lambda r_i>c_*.
\tag{9.9}
\]

This contradicts the column-energy budget (5.5), which says the same quantity is at most `c_*`.

Every one of the 160 residuals is a signed-coordinate image of the representative. Permuting the corresponding diagonal weights gives the same contradiction. Thus **all q=5 configurations are impossible at `c_*`**.

---

# 10. Method #25 — COUNT THE SAME THING TWICE: exact residual set equals the analytic orbit

There are two independent finite descriptions of the hard remainder:

1. the q=5 exact classifier outputs **160** distinct residual configurations;
2. the signed-coordinate orbit generated from the single representative in Section 8 has **160** distinct configurations.

The postcheck does not merely compare the cardinalities: it constructs both finite sets in canonical encoding and checks exact set equality.

\[
\boxed{F_{\rm residual}=\operatorname{Orb}(B_*)},
\qquad
|F_{\rm residual}|=|\operatorname{Orb}(B_*)|=160.
\tag{10.1}
\]

This closes the finite-to-analytic interface. There is no unclassified q=5 residual hidden behind the orbit argument.

**Outcome of method #25:** success. The finite search discovers one extremal orbit; the analytic dual proves the orbit impossible above the exact obstruction scale.

---

# 11. Completion of the exact upper bound

The four regimes

\[
q\le3,\qquad q=4,\qquad q=5,\qquad q\ge6
\]

exhaust every possible active-row count. Sections 6--10 rule out each regime under the assumption `disc(A)>T`. Therefore

\[
K_5^*\le T.
\tag{11.1}
\]

Together with the explicit obstruction (4.3),

\[
K_5^*\ge T,
\]

so

\[
\boxed{
K_5^*
=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
}.
\qquad\Box
\tag{11.2}
\]

This is stronger than every preceding R13 finite-five upper theorem: the bracket has collapsed to a point.

## 12. Propagation to the complete fixed metric

Using the retained five-column block-composition theorem,

\[
B(n)\le K_5^*\sqrt{\lceil n/5\rceil},
\]

R13's complete chosen certified envelope becomes

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\displaystyle
\min\left\{\sqrt{\frac{3n}{4}},
T_*\sqrt{\left\lceil\frac n5\right\rceil}\right\},
&5\le n\le85,\\[3mm]
3\sqrt{2\pi},&n\ge86.
\end{cases}
}
\tag{12.1}
\]

This equality defines the **chosen rigorously certified upper envelope**; it is not a claim that every finite `B(n)` appearing in (12.1) is exact. Only the displayed `n=1,2,3,4` retained exact values and the newly proved `K_5^*` equality have exact-value status here.

Relative to the immediately preceding `sqrt(100/31)` envelope, the exact postcheck verifies strict improvement in exactly **73 dimensions**:

\[
\boxed{
5;\quad9\!:\!10;\quad13\!:\!15;\quad18\!:\!20;\quad22\!:\!85.
}
\tag{12.2}
\]

The finite/universal crossover remains at `n=86`. The exact comparison uses the rational bounds `333/106<pi<22/7`: the postcheck verifies

\[
17T_*^2<18\frac{333}{106}<18\pi,
\]

while

\[
T_*^2>\frac{22}{7}>\pi,
\qquad
\frac{3\cdot86}{4}>18\frac{22}{7}>18\pi.
\]

Thus the five-block certificate remains below the current universal certificate through `n=85`, while the retained universal certificate is the chosen envelope from `n=86` onward.

## 13. What moved, what did not, and what remains open

The fixed metric **moved**. The old finite-five bracket

\[
T_*\le K_5^*\le\sqrt{100/31}
\]

is replaced by the exact identity

\[
\boxed{K_5^*=T_*}.
\]

The qualitative Boolean Komlós conjecture is not being claimed here as a new closure: Guo--Fang--Lu's 10 September 2026 preprint already states the dimension-free real-sign theorem. R13's new mathematical claim is the exact five-column constant and the consequent finite-dimensional envelope improvement.

The next source-relevant quantitative frontier is therefore **not another five-column lemma**. Any continued R13 run should either:

1. seek an exact `K_6^*` upper bound matching or approaching the retained six-column obstruction;
2. use the exact `K_5^*` extremal orbit to derive a sharper composition theorem than independent five-block grouping; or
3. if neither route moves the fixed `B(n)` envelope or an explicit finite obstruction under the two-recovery rule, hand off rather than accumulating more five-column certificates.

The fixed-metric stagnation count resets to **0**.

## 14. Exact artifacts and self-check status

The relevant immutable finite/checker history is:

- exact lower obstruction and full 32-sign enumeration: commit `ea33d21fa2ae398a2e92b04e456fbc5230892b57`;
- q4/q5 exact finite-checker patch at `c_1=311249/10^6`: commit `4c15b67aed425932191ced903d7f88970760eba1`, including
  - `artifacts/R13/20260918T1252Z_k5-exact-cstar-e41c_q4_checker.cpp`,
  - `artifacts/R13/20260918T1252Z_k5-exact-cstar-e41c_q5_classifier.cpp`;
- exceptional-orbit / exact-radical postcheck: commit `6c10d91997f31f1e0472fb73ba7ae73b1d56e50a`;
- compact corrected postcheck source: commit `a4680170881580f8ebc87b21144d1e634029861a`, file
  `artifacts/R13/20260918T1252Z_k5-exact-cstar-e41c_postcheck_v2.py`;
- archived executed postcheck output: commit `27596cd8286d600001227562510f1592faab96cf`, file
  `artifacts/R13/20260918T1252Z_k5-exact-cstar-e41c_postcheck_output.txt`, ending
  `R13_K5_EXACT_POSTCHECK_PASS`.

That archived output records

\[
T=1.79244719148328276329032036724\ldots,
\qquad
c_*=0.311248495646606345158346862955\ldots,
\]

`q4_configs=287962480`, `q5_configs=6047460`, `q5_exceptional_configs=160`, `exceptional_signed_coordinate_orbit=160`, exact dual sum `=c_*`, and `improved_dimensions=73`.

These are **self-checks**, not independent outside audits.

## 15. Status and closure discipline

Status after this run:

**PARTIAL QUANTITATIVE / EXACT `K_5^*` PROVED / FIXED METRIC MOVED / written proof on page / exact self-check PASS / outside audits 0/2 / novelty UNVERIFIED / unrestricted dimension-free Boolean source already KNOWN in current preprint literature.**

This does not satisfy the owner's protocol for calling a new result externally closed because two independent OTHER-track audits have not been obtained. No paper folder is created in this run. No shared root or peer file is edited.

## 16. Model-control / scheduler-control status

The exposed task-control surface still offers prompt/title/schedule/enabled/timing fields but no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry. Therefore GPT-6/maximum remains prompt-only and this report correctly labels the actual run as GPT-5.6 Sol / reasoning UNVERIFIED.

The historical `You cannot modify this task` failure is an authorization/context restriction, not a mathematical blocker. The legitimate remedy is an authorized owner/workspace task surface or platform support exposing binding model/reasoning controls. This research run performs no scheduler changes, permission changes, duplication, or bypass.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  run_id: "20260918T1314Z_k5-exact-equality-7c2f"
  source_id: "E0042"
  source: "real Boolean Komlos; current navigation Bansal-Jiang arXiv:2508.03961v2 and Guo-Fang-Lu arXiv:2609.11189v1"
  fixed_metric: "complete rigorously certified pointwise upper envelope B_R13(n)"
  before:
    K5_lower: "T_* = (2sqrt2+3sqrt3+2sqrt(51+3sqrt6))/13"
    K5_upper: "sqrt(100/31)"
    K5_interval_width: "~0.00360582878447"
    envelope_five_block: "sqrt((100/31)*ceil(n/5))"
    stagnation: 0
  after:
    K5_exact: "T_* = (2sqrt2+3sqrt3+2sqrt(51+3sqrt6))/13 = 1.792447191483282763..."
    K5_interval_width: 0
    envelope_five_block: "T_* sqrt(ceil(n/5))"
    strict_dimensions_improved_vs_previous_envelope: 73
    improved_dimension_set: "{5} U [9,10] U [13,15] U [18,20] U [22,85]"
    crossover_to_3sqrt2pi: 86
    stagnation: 0
  methods: [3, 18, 25]
  finite_core:
    q4_configs_certified_at_c1: 287962480
    q5_configs_examined_at_c1: 6047460
    q5_residuals: 160
    residual_orbit_size: 160
    residual_set_equals_orbit: true
    exact_dual_sum: "1/T_*^2"
  status: "PARTIAL_QUANTITATIVE; exact K5 proved; source dimension-free Boolean theorem KNOWN in current preprint literature"
  self_check: "PASS"
  outside_audits: "0/2"
  novelty: "UNVERIFIED"
  shared_root_edits: false
```

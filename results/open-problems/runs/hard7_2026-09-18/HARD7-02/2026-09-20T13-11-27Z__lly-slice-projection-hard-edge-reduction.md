Model: **GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did not run on GPT-6 at verified maximum reasoning. NO MOVEMENT: external/source-verified `p_comb<=2 -> <=2`; in-track written candidate `p_comb<=1 -> <=1` remains pending independent validation. Methods tried this run: B8 / B15 / B19.**

# HARD7-02 — Li--Litvak--Yu Conjecture 3.9: exact slice-projection moments and an `o(n)` hard-edge reduction

Date: 2026-09-20 UTC  
Track: `HARD7-02`  
Status: **PARTIAL / SOURCE OPEN**  
Frozen metric: `p_comb`  
External verified value before/after: **`<=2 -> <=2` (no movement)**  
Internal written milestone before/after: **`<=1 -> <=1` pending independent validation**  
Post-STUCK1 ordinary no-movement count: **2**

## 1. Continuation and controls read

This is a continuation of the exclusively owned Li--Litvak--Yu fixed-row-sum circular-law target. It does not restart the released Han band problem and does not claim a new target.

Before the mathematics I re-read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
- root `POSTED.md` and `RESULTS.md`,
- the active claim `operations/claims/LI-LITVAK-YU-2026-SPARSE-COMBINATORIAL-CIRCULAR-LAW.md`,
- the latest own checkpoint `2026-09-20T12-09-17Z__lly-row-only-rectangular-absorption.md`,
- repository search surfaces for the exact arXiv identifier `2604.10446` and neighboring non-Hermitian/heavy-tail tracks, including the distinct C0031/C0032 material.

The source remains Dongbin Li, Alexander E. Litvak and Tingzhou Yu, *Least singular values of shifted sparse random combinatorial matrices*, arXiv:2604.10446v2 (11 August 2026), Conjecture 3.9. The source asks whether the ESD converges in probability to the circular law under the sole sparsity assumption `d(n)->infinity`; Corollary 1.4 proves the circular law for `d >= (log n)^(2+eps)`, `d=o(n)`. The active HARD7-02 written candidate `p_comb<=1` remains an unaudited internal theorem and is not promoted here.

A bounded fresh 20 September 2026 literature search for the exact source/title/authors, fixed-cardinality quadratic-form concentration, multislice Hanson--Wright estimates, and permutation/slice Littlewood--Offord results found the source paper, Sah--Sahasrabudhe--Sawhney's iid sparse circular-law work, Sambale--Sinulis (2022) on concentration on the multislice/sampling without replacement, and Do--Nguyen--Phan--Tran--Vu (2025) on permutation-space Littlewood--Offord. I did not locate a theorem that supplies the exact uniform shifted projection lower-tail estimate proved below for this row-combinatorial hard-edge application. This is bounded negative evidence only. The exact moment identity itself is elementary sampling-without-replacement algebra and **no novelty claim is made for that identity in isolation**.

Current references checked:

- https://arxiv.org/abs/2604.10446
- https://arxiv.org/abs/2310.17600
- https://arxiv.org/abs/2010.16289
- https://arxiv.org/abs/2512.21779

No root ledger, other track, scheduler, email, Drive, workflow, permission, or public-posting state was edited.

## 2. Why this run changed route

The previous run found the exact row-only determinant absorption identity

`det(B_+ B_+^*) = det(BB^*) ||P_{ker B} x^*||_2^2`

for appending an independent fixed-sum row. The remaining obstruction was therefore a lower-tail theorem for

`||P_V(Y + u)||_2`,

where `Y` is a uniform `d`-subset indicator, `u` is deterministic after conditioning on the past, and `V` is the evolving right kernel.

The important point this run is that **no delocalization theorem for `V` is needed as long as its dimension `h` satisfies `dh/n >> 1`**. An exact fourth-order computation on the slice gives a universal lower-tail estimate for every deterministic subspace and every deterministic shift. This controls all but `o(n)` row-absorption factors for every `d->infinity`.

That does not yet close the source conjecture: an `o(n)` set of factors can still carry macroscopic negative logarithmic mass if they are super-small. The exact remaining blocker is now much narrower and is stated in Section 10.

## 3. B8 — exact second moment of a quadratic form on the fixed-cardinality slice

Let

`Y=(Y_1,...,Y_n)`

be uniform over `{0,1}^n` with exactly `d` ones. Put

`p=d/n`, `R=Y-p 1`, `H=I-11^*/n`.

For `r=1,2,3,4`, write

`q_r=(d)_r/(n)_r`,

with `q_r=0` when `r>d`. Thus `E product_{j=1}^r Y_{i_j}=q_r` for distinct indices.

### Lemma 3.1 (exact slice quadratic moment)

Let `S` be a real symmetric `n x n` matrix satisfying `S1=0`. Put

`tau=tr S`, `s_2=tr(S^2)`, `delta_2=sum_i S_ii^2`,

and `F=Y^T S Y`. Then

`E F = (q_1-q_2) tau`,                                            (3.1)

and

`E F^2`
` = (q_2-2q_3+q_4) tau^2`
` + (2q_2-4q_3+2q_4) s_2`
` + (q_1-7q_2+12q_3-6q_4) delta_2`.                              (3.2)

#### Proof

Write

`D=sum_i S_ii Y_i`,
`O=sum_{i!=j} S_ij Y_iY_j`,

so `F=D+O`. Since every row sum of `S` is zero,

`sum_{i!=j} S_ij=-tau`.

The diagonal square is

`E D^2 = q_2 tau^2 + (q_1-q_2) delta_2`.                         (3.3)

For the mixed term, for fixed `i`, the ordered off-diagonal entries involving `i` sum to `-2S_ii`, while those avoiding `i` sum to `-tau+2S_ii`. Hence

`E DO = (-2q_2+2q_3) delta_2 - q_3 tau^2`.                       (3.4)

For `E O^2`, classify two ordered pairs `(i,j)` and `(k,l)` according to whether their underlying index sets have size two, three, or four. The size-two contribution has coefficient `q_2` and total weight

`2 sum_{i!=j} S_ij^2`.

The size-three total weight is

`4 delta_2 - 4 sum_{i!=j} S_ij^2`,

again by the zero-row-sum identity. The disjoint weight is the remaining part of

`(sum_{i!=j}S_ij)^2=tau^2`.

Therefore

`E O^2`
` = q_4 tau^2`
` + (2q_2-4q_3+2q_4) (s_2-delta_2)`
` + 4(q_3-q_4) delta_2`.                                        (3.5)

Adding (3.3), twice (3.4), and (3.5) gives (3.2). Equation (3.1) is the corresponding first-moment expansion. `square`

The exact finite algebra of (3.1)--(3.2) was self-checked by exhaustive rational enumeration on six small `(n,d)` cases. The checker/output are

- `artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T13-11-27Z__slice_projection_moment_check.py` @ `0f1e93f97e37979308defa6e373213d36d57739e`,
- `artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T13-11-27Z__slice_projection_moment_check.out` @ `d758f2063573da75b3cb68c5198703dcbaf40139`,

with archived final line `ALL_EXACT_CHECKS_PASS = True`. This is a self-check only.

## 4. Coefficient bounds in the sparse half

Set

`alpha=q_1-q_2=d(n-d)/(n(n-1))`.

For `n>=6`, `1<=d<=n/2`, define

`a_0=q_2-2q_3+q_4-alpha^2`,
`b_0=2q_2-4q_3+2q_4`,
`c_0=q_1-7q_2+12q_3-6q_4`.

The exact factorizations are

`b_0 = 2 d(d-1)(n-d)(n-d-1) / [n(n-1)(n-2)(n-3)] >=0`,          (4.1)

`c_0 = d(n-d)(6d^2-6dn+n^2+n) / [n(n-1)(n-2)(n-3)]`,           (4.2)

and

`a_0`
`= d(d-n) B / [n^2(n-1)^2(n-2)(n-3)]`,                         (4.3)

where, with `m=n-2d>=0`,

`B=((2n-3)m^2-n^2+2n)/2`.                                      (4.4)

Consequently the positive parts satisfy the safe universal estimates

`(a_0)_+ <= 2/n^2`,
`0<=b_0<=16p^2`,
`(c_0)_+<=16p`.                                                  (4.5)

For (4.3), if `a_0>0` then `B<0`; hence `|B|<n^2/2`, while `d(n-d)<=n^2/4`, and the denominator is a fixed positive fraction of `n^6` for `n>=6`. The other two bounds follow directly from (4.1)--(4.2) and `d<=n/2`.

This exact cancellation in the `tau^2` coefficient is the useful feature. A generic second-moment estimate that simply bounds `E F^2` would leave a term of order `p^2 tau^2` and would not yield concentration. Subtracting `(E F)^2` reduces the positive `tau^2` contribution to order `tau^2/n^2`.

## 5. B15 — uniform shifted projection lower tail, with no subspace regularity assumption

Let `P` be any deterministic orthogonal projection on `C^n` of rank `h>=2`, and let `u in C^n` be arbitrary. We apply the slice formula to the real random vector `R`.

Define

`S=Re(HPH)`

as a real operator on `R^n`. Then

`0<=S<=I`, `S1=0`,

and

`tau=tr S=tr(HPH)=h-||P1||_2^2/n`,

so

`h-1 <= tau <= h`.                                               (5.1)

Moreover `tr(S^2)<=tau` and `sum_i S_ii^2<=tau`.

Since `R=HR` is real,

`R^* P R = R^T S R = Y^T S Y`.

From Lemma 3.1 and (4.5),

`Var(R^*PR) <= 2 h^2/n^2 + 32 p tau`.                            (5.2)

Now put

`W=||P(R+u)||_2^2`,
`s=||Pu||_2^2`.

Because `ER=0` and `Cov(R)=alpha H`,

`E W = alpha tau+s`.                                             (5.3)

The linear cross term is

`L=2 Re <R,Pu>`.

Writing `g=2 Re(Pu)`, its exact sampling-without-replacement variance is

`Var(L)=alpha ||Hg||_2^2 <= 4 alpha s <= 5ps`                    (5.4)

for `n>=6`. Hence, by `Var(X+Y)<=2Var X+2Var Y`, (5.2)--(5.4) imply

`Var(W) <= C [ h^2/n^2 + p tau + ps ]`                          (5.5)

for a universal `C`.

Since `d<=n/2`,

`alpha >= p/2`,

and therefore

`E W >= (p/2)tau+s`.                                             (5.6)

Using `tau>=h-1`, Chebyshev's inequality now gives the source-useful uniform estimate.

### Theorem 5.1 (universal slice-row projection lower tail)

There is a universal constant `C` such that, for all `n>=6`, `1<=d<=n/2`, every rank-`h` orthogonal projection `P` with `h>=2`, and every deterministic `u in C^n`,

`P( ||P(R+u)||_2 <= (1/2) sqrt(d(h-1)/n) )`
` <= C [ n/(d(h-1)) + 1/d^2 ].`                                 (5.7)

#### Proof

If the event in (5.7) occurs then, by (5.3), (5.6), and `tau>=h-1`,

`W <= p(h-1)/4 <= (E W)/2`.

Thus

`P(event) <= 4 Var(W)/(E W)^2`.

For the `p tau` term in (5.5), use `E W>=p tau/2` to get `O(1/(p tau))`. For the shift term, writing `a=p tau/2`,

`p s/(a+s)^2 <= p/(4a)=1/(2tau)`.

For the remaining term and `h>=2`, `tau>=h/2`, so

`(h^2/n^2)/(E W)^2 <= 4h^2/(p^2 tau^2 n^2) <= 16/d^2`.

Since `p=d/n` and `tau>=h-1`, these bounds give (5.7). `square`

### Why (5.7) matters

The estimate is completely uniform in the subspace and in the deterministic shift. It therefore does **not** require an incompressible normal vector, small leverage scores, a net over subspaces, or a conditional column reservoir. It has the correct transition parameter

`p h = d h/n`.

So once the evolving kernel has dimension much larger than `n/d`, a fresh fixed-sum row hits it at its natural `sqrt(dh/n)` scale with high conditional probability.

This is exactly the regime where the direct SSS column port was needlessly difficult.

## 6. B19 — the row-only absorption algorithm and the natural cutoff `h ~ n/d`

Fix a Girko shift `z` and use the unnormalized shifted matrix

`A_n(z)=M_n-z sigma I_n`,

where

`sigma=sqrt(d(1-d/n))`.

Let `A_t(z)` be the first `t` rows. The fresh row is

`x_{t+1}=Y_{t+1}-z sigma e_{t+1}`.

Because rows are independent, conditioned on `A_t(z)`, the row `Y_{t+1}` is still a fresh uniform `d`-subset indicator.

### Proposition 6.1 (a.e. shift gives deterministic full prefix rank)

For the fixed sequence `d=d(n)`, there is a countable set `E subset C` such that for every `z notin E`, for every `n`, every `t<=n`, and **every possible realization** of `M_n`, the rectangular prefix `A_t(z)` has full row rank `t`.

#### Proof

For fixed `(n,t,M_n)`, the first `t` columns of `A_t(z)` form

`M_[t],[t] - z sigma I_t`.

Its determinant is a nonzero polynomial in `z` of degree `t` with leading coefficient `(-sigma)^t`. Hence it has finitely many roots. There are only finitely many allowed `M_n` for each `n`, finitely many `t`, and countably many `n`. The union of all these finite root sets is countable. Outside that union the displayed principal minor is nonzero for every realization. `square`

Thus the exact row-absorption identity from the preceding run applies pathwise for every prefix for every `z notin E`.

Let `P_t` be orthogonal projection onto `ker A_t(z)`. Then

`rank P_t = h=n-t`.

Write

`R_{t+1}=Y_{t+1}-p1`,
`u_{t+1}=p1-z sigma e_{t+1}`,

so `x_{t+1}=R_{t+1}+u_{t+1}`. Conditional on `A_t(z)`, Theorem 5.1 gives, for `h>=2`,

`P( ||P_t x_{t+1}^*||_2 <= (1/2)sqrt(d(h-1)/n) | A_t(z))`
` <= C [ n/(d(h-1)) + 1/d^2 ].`                                 (6.1)

This bound holds for the **actual evolving random kernel**, without any further structural event.

## 7. All but `o(n)` hard-edge absorption factors are automatically at natural scale

Fix any `eps in (0,1)` and consider the final `eps n` row additions, i.e. kernel dimensions

`1 <= h <= eps n`.

Set

`H_n=ceil(n/d)+2`.                                                (7.1)

Call the step at kernel dimension `h` bad when

`||P_t x_{t+1}^*||_2 < (1/2)sqrt(d(h-1)/n)`.

Let `N_bad` count bad steps with

`H_n <= h <= eps n`.

Taking expectations in the conditional estimate (6.1) and summing the harmonic series gives

`E N_bad`
` <= C (n/d) sum_{h=H_n}^{floor(eps n)} 1/(h-1) + C eps n/d^2`
` <= C n log(e d)/d + C n/d^2`.                                  (7.2)

Therefore, whenever only

`d(n)->infinity`,                                                  (7.3)

we have

`N_bad/n -> 0` in probability.                                    (7.4)

The terminal range `1<=h<H_n` itself has only

`H_n/n <= 1/d+o(1)`                                               (7.5)

of all row additions. Combining (7.4)--(7.5):

> **For every `d->infinity` and every a.e. fixed shift `z`, all but `o_p(n)` of the terminal row-absorption factors are bounded below at the natural `sqrt(dh/n)` scale.**

This is a genuine strengthening of the previous qualitative row-only route. It is still a partial theorem, not Conjecture 3.9.

## 8. The good factors already have negligible logarithmic cost

Normalize by `sigma=sqrt(d(1-d/n))`. On every good step,

`||P_t x_{t+1}^*||_2 / sigma`
` >= c sqrt((h-1)/n)`                                             (8.1)

with an absolute `c>0`, because `sigma^2<=d`.

Hence

`[-log( ||P_t x_{t+1}^*||_2/sigma )]_+`
` <= C + (1/2) log(n/(h-1)).`                                    (8.2)

Summing (8.2) over `H_n<=h<=eps n` and dividing by `n` yields

`limsup_{n->infinity} (1/n) sum_good [-log(...)]_+`
` <= C eps + (1/2) eps log(1/eps) + o(1)`                         (8.3)

in probability. The right side tends to zero as `eps->0`.

So the ordinary logarithmic hard-edge problem is no longer spread across all `eps n` terminal singular directions. The good directions have the correct integrable cost automatically.

## 9. What was tried and what failed/succeeded

### B8 — discretize / compute the exact finite law

Successful. Expanding the degree-two statistic under exact fixed-cardinality inclusion probabilities produced (3.2), and the cancellation after subtracting the square of the mean produced the sparse-sensitive variance estimate (5.2). A generic multislice concentration theorem does not expose this exact cancellation at the scale needed here.

### B15 — break symmetry on purpose

Successful. The previous SSS-inspired route treated rows and columns symmetrically, but the source model does not: rows are independent while columns are not. Keeping only row additions converts the endpoint problem into a shifted projection norm of a single fresh slice row. Theorem 5.1 is uniform in the conditioned kernel and bypasses the terminal-column determinism obstruction completely.

### B19 — make it an algorithm

Successful as a reduction, not as a full proof. The deterministic algorithm is: expose independent rows, apply exact Gram-determinant absorption, certify every step with `h>=H_n` using (6.1), and quarantine all bad plus terminal `h<H_n` factors. The quarantine has size `o_p(n)` for every `d->infinity`. What remains is no longer a bulk lower-tail problem; it is an aggregate-log problem on an `o(n)` exceptional set.

This triple is new for the active Li--Litvak--Yu target and differs from the previous run's B7/B12/B27.

## 10. Exact remaining blocker

Let `G_n(z)` be the good absorption steps certified by (6.1), and let `E_n(z)` be the union of

1. the bad steps in `H_n<=h<=eps n`, and
2. all terminal steps `1<=h<H_n`.

The run proves

`|E_n(z)|/n -> 0` in probability                                  (10.1)

for every `d->infinity`, and proves that the negative logarithmic contribution of `G_n(z)` vanishes after `n->infinity`, then `eps->0`.

The source-closing obligation is now exactly to show

`(1/n) sum_{h in E_n(z)}`
`   [-log( ||P_t x_{t+1}^*||_2 / sigma )]_+  -> 0`                (10.2)

in probability for a.e. fixed `z`.

A mere cardinality bound (10.1) is **not** enough: an `o(n)` family of factors can still contribute order `n` if individual factors are exponentially small. Proposition 6.1 removes exact zero for a.e. `z` but gives no quantitative floor, so I do not claim (10.2).

This is substantially narrower than the previous blocker. Any one of the following would close the new gap:

- an averaged logarithmic small-ball bound for the slice-row projection in the range `h<=C n/d`;
- a bound `E[-log(D_h/sqrt(dh/n))]_+ <= o(d/log d)` uniform in the conditioned kernel, strong enough after summing `O(n log d/d)` exceptional steps;
- a direct comparison showing the ridge-to-ordinary log-volume difference is negligible when only `o(n)` absorption factors are uncertified, with a regularization level whose logarithm is `o(d/log d)`.

The next run should attack (10.2), not re-prove (5.7).

## 11. Relation to the frozen metric

The frozen metric does **not** move this run.

- verified external literature: `p_comb<=2`;
- current in-track written theorem: `p_comb<=1`, still pending independent validation;
- full source conjecture `d->infinity`: still open.

The new theorem works under the full source sparsity condition `d->infinity`, but only for the **number and natural scale of good row-absorption factors**. It does not establish logarithmic uniform integrability of the exceptional factors, so it is not a new circular-law threshold.

## 12. Current literature comparison

Sambale--Sinulis provide general concentration/Hanson--Wright machinery on the multislice. At the natural mean scale for the quadratic projection statistic, a generic non-sparse-sensitive Hanson--Wright substitution does not by itself expose the `dh/n` transition used in (5.7); the exact inclusion-probability computation does. The 2025 permutation Littlewood--Offord work is potentially relevant to the remaining exceptional factors, because (10.2) needs logarithmic rather than merely constant-probability control. I did not locate an existing theorem that can simply be quoted to finish (10.2) in the conditioned evolving-kernel setting.

This literature comparison is a route assessment, not a priority claim.

## 13. Scheduler/model capability statement

The currently exposed native automation interface still offers schedule/prompt/title/timing/enabled-state fields but **no model selector, no reasoning-effort selector, and no guaranteed run-duration field**. Thus `GPT-6 / maximum` remains a prompt request only; this invocation identifies itself as GPT-5.6 Sol and the reasoning level is UNVERIFIED. Changing that would require an authorized product/interface capability that actually exposes model and reasoning controls; a repository edit cannot supply one.

The historical `You cannot modify this task` response for P26/P01/P03 is an ownership/permission boundary, not a mathematical issue. This worker did not probe or modify those schedules. The lawful workaround remains modification by the authorized task owner/workspace through an interface with permission, or platform support; do not bypass it by duplicating the task.

## 14. Ledger delta and next checkpoint

No shared root ledger was edited. Suggested coordinator delta:

`HARD7-02 | Li--Litvak--Yu Conj. 3.9 | p_comb | external <=2 -> <=2; internal <=1 remains unaudited | PARTIAL / SOURCE OPEN | B8/B15/B19: exact slice quadratic moments imply universal shifted projection lower tail; all but o_p(n) row-absorption hard-edge factors are at natural scale for every d->infinity; remaining blocker is aggregate negative-log mass on the o(n) exceptional factors`

Post-STUCK1 ordinary no-movement count is now **2**. If the frozen quantity is unchanged on the next ordinary run, the track reaches the three-run stagnation trigger and the following invocation must obey the Section-I STUCK2 thinking protocol rather than produce another incremental lemma.

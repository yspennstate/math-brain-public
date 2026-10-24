Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `N_exact = 101 -> 102`; Section-B methods actually tried: #21 ASK WHO ELSE HAS THIS SHAPE, #14 FIND THE GROUP ACTING, and #4 PROVE SOMETHING WEAKER, COMPLETELY — all explicitly RECYCLED because all 30 numbered methods had already genuinely been used on P0282.**

# NM13-07 — P0282 Jucys/Weingarten norm representation, curvature block through order 32, and exact row 102

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Namespace: `proofnet24/NM13-07/`  
Category: `CLOSABLE OUTSIDE`  
Canonical claim: `P0282`, `operations/claims/P0282.md`  
Source id: `aim_kpz_followup_2025`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
SHA256: `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`  
Selection shard: `6 mod 13`  
Parent source status: **OPEN**  
NM13-07 status: **PARTIAL**  
Frozen metric before / after: **`N_exact = 101 -> 102`**  
Consecutive unchanged runs: **`0 -> 0`**  
Stuck recoveries: **`0 -> 0`**  
Audits: **P26 NOT PASSED; NM13-08 NOT PASSED**

## 1. Authoritative continuity and ownership

This invocation continues the already-admitted exclusive P0282 assignment. I did **not** reopen intake, create an alias claim, or screen a replacement source. The current canonical claim still assigns P0282 to NM13-07 and freezes the literal source statement:

for a uniform permutation `sigma in S_n`, with

`ell_{n,k} = #{sigma in S_n : LIS(sigma)=k}`,

Chen asks whether

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`

for every positive integer `n` and every `1<k<n`.

The controlling predecessor is

`proofnet24/NM13-07/runs/2026-09-19/2026-09-19T14-45-30Z__p0282-numerator-polynomial-twenty-nine-thirtieths-row101.md`

at creation commit `d50be0a08824802fd2d1c84c1822650b85535576`. Its authoritative entry state is:

- `N_exact=101`;
- source **OPEN**, worker **PARTIAL**;
- retained all-`n` Chen theorem for defects `j=n-k<=66`;
- retained growing-defect sufficient window `j+1<=n^(29/30)/8`;
- all-`n` stronger ULC/shadow-density frontier through defect 32;
- `unchanged_runs=0`, `stuck_recoveries=0`;
- P26 and NM13-08 audits both NOT PASSED.

I preserve that state and only add claims proved in this invocation.

A complete Git comparison from the predecessor report commit to current master was available with `too_large=null`. It contained no mutation of `operations/claims/P0282.md`, root `QUEUE.md`, root `POSTED.md`, root `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, or the P0282 source/attempt ledgers. The newest NM13-08 report explicitly records P0282 as NM13-07's active residue-6 source and records no P0282 audit PASS. Current targeted search for `P26-AUDIT-P0282` likewise recovered no PASS. Therefore there is no ownership release and neither designated outside audit is counted as passed.

## 2. Required repository reads and access disclosure

Before new mathematics I reread or exact-target-recovered current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical `operations/claims/P0282.md`;
- the newest complete NM13-07 predecessor;
- newest visible NM13-06 and NM13-08 reports;
- newest P26 audit report;
- P0282 canonical-key / source / prior-attempt / audit searches; and
- the complete predecessor-to-current Git delta.

The append-only `probability_1000_intake_*/problems.jsonl` and attempt corpora are too large for an honest claim that every unchanged historical byte was freshly rendered model-visible in one connector turn. I make no such claim. The exact Git delta showed no relevant intake/attempt mutation, and candidate-specific canonical identity, claim, ownership, source scope, attempt continuity, and audit state were reopened directly. No private-repository history needed for this decision was known to be inaccessible.

## 3. Fresh source and literature check — 2026-09-19

The public literature check was refreshed before promoting the new theorem.

- William Y. C. Chen, *Log-concavity and q-Log-convexity Conjectures on the Longest Increasing Subsequences of Permutations*, arXiv:0806.3392 (2008), is the original fixed-size source.
- Bóna--Lackner--Sagan and Gao--Xie--Yang give restricted / Schur-positive progress rather than a proof of the full fixed-size statement.
- Novak--Rhoades formulate a stronger Kronecker-coefficient conjecture implying Chen.
- Baslingker--Krishnapur--Madiman, arXiv:2412.15116, prove **Poissonized** Plancherel top-row log-concavity and explicitly describe it as the first known positive result toward Chen, not a fixed-size resolution.
- Manuel Kauers and Chen Wang, arXiv:2609.02220, submitted 2026-09-02, prove bivariate recurrences and D-finiteness for long-LIS counts; their abstract does not claim fixed-size Chen log-concavity.
- A current MathDB entry still labels Chen's conjecture open.

For the new representation-theoretic route I also searched `Jucys-Murphy Weingarten`, `unitary Weingarten Jucys-Murphy`, `monotone Hurwitz Jucys-Murphy`, and `content product Plancherel regular trace`. The relevant classical prior art includes Jonathan Novak's 2008/2010 work identifying complete homogeneous symmetric functions of Jucys--Murphy elements with the asymptotic expansion of the unitary Weingarten function, and Matsumoto--Novak, *Jucys--Murphy Elements and Unitary Matrix Integrals*, IMRN 2013. Goulden--Guay-Paquet--Novak connect the same complete-symmetric-function expansion with monotone Hurwitz factorizations. I therefore make **no novelty claim for the Jucys/Weingarten mechanism itself**. The exact P0282 adjacent-quotient norm representation below was not found stated in the bounded search, but that absence is only negative evidence: novelty / priority remain **UNVERIFIED**.

A recent 2026 paper by Umesh Shankar on log-concavity of triangular arrays with two-term positive recurrences also surfaced. I did not claim it applies to P0282: this run did not establish a reduction of the Kauers--Wang bivariate LIS recurrences to Shankar's specific hypotheses.

## 4. Methods actually tried

All thirty Section-B methods had already been genuinely used on P0282, so a literal unused triple is no longer available. I used a different recycled triple from the predecessor and record the actual work.

### #21 ASK WHO ELSE HAS THIS SHAPE — RECYCLED; productive

The retained Plancherel content product was compared with the classical Jucys--Murphy / unitary Weingarten calculus. This reveals that the correction factor is not merely an expectation over partitions: it is the regular-trace / identity coefficient of the square of one central group-algebra element, and hence an exact `l2` norm square of its coefficients. The inverse factor is precisely of Weingarten type, while its expansion is governed by the monotone-factorization machinery of the classical literature.

This does not solve Chen, but it changes the structural target from `prove signs of infinitely many Taylor coefficients` to `prove a norm comparison / conditional-expectation inequality in the tower Q[S_j] subset Q[S_{j+1}]`.

### #14 FIND THE GROUP ACTING — RECYCLED; exact theorem proved

I used the symmetric group acting through its regular representation and the content spectrum of the Jucys--Murphy elements to prove the norm identity in Section 5. It also upgrades the predecessor's numerator polynomial into a norm square of a central polynomial element.

### #4 PROVE SOMETHING WEAKER, COMPLETELY — RECYCLED; exact finite theorem and metric movement

Rather than assert the all-order curvature sign suggested by data, I proved only the next finite block, through Taylor order 32, by exact arithmetic. This yields a rigorous `33/34` growing-defect window. Separately, an exact Gessel/Toeplitz seam certificate closes row 102 and moves the frozen metric `101 -> 102`.

## 5. New structural theorem: the Plancherel correction is a Jucys/Weingarten `l2` norm square

Retain the stable hook factorization, with `j=n-k`,

\[
F_j(n):=\ell_{n,n-j}
   =\frac{(n)_j^2}{j!}A_j(1/n),
\]

where for `mu |- j`

\[
A_j(t)=\mathbb E_{\mu\sim\mathrm{Plancherel}(j)}R_\mu(t)^2,
\qquad
R_\mu(t)=
\prod_{x\in\mu}
\frac{1-(j+c(x))t}{1-(j+c(x)-1)t}.
\]

Let

\[
J_r=\sum_{a<r}(a\ r)\in\mathbb Q[S_j]
\]

be the Jucys--Murphy elements and define, formally near `t=0`,

\[
Z_j(t)=
\prod_{r=1}^j
\frac{1-(j+J_r)t}{1-(j+J_r-1)t}.
\]

### Proposition `NM13-07-P0282-JUCYS-WEINGARTEN-NORM-11`

`Z_j(t)` is central and self-adjoint. On the irreducible `S_j` module indexed by `mu`, it acts by the scalar `R_mu(t)`. Consequently

\[
\boxed{
A_j(t)=[e]Z_j(t)^2
      =\sum_{\sigma\in S_j}z_{j,\sigma}(t)^2,
}
\]

where `Z_j(t)=sum_sigma z_{j,sigma}(t) sigma` and `[e]` denotes identity coefficient.

At the source point `t=1/n`, with `k=n-j`,

\[
\boxed{
Z_j(1/n)=
\prod_{r=1}^j\frac{k-J_r}{k+1-J_r}.
}
\]

In the stable regime `n>=2j` these denominators are invertible on every irreducible because every Young-diagram content is at most `j-1` while `k>=j`.

### Proof

The Jucys--Murphy elements commute. A symmetric polynomial in them is central, and by the standard content-eigenvalue theorem it acts on `V^mu` by evaluation on the multiset of contents of `mu`. The same statement holds for a rational symmetric function wherever its denominators are invertible, or coefficientwise as a formal series at `t=0`.

The product defining `Z_j` is symmetric in `J_1,...,J_j`. In any Young seminormal basis, the eigenvalues of the `J_r` are the contents of the boxes occupied by labels `r=1,...,j`. Their product therefore gives exactly `R_mu(t)`, independent of the tableau, so `Z_j` acts by that scalar on all of `V^mu`.

The regular representation decomposes as

\[
\mathbb Q[S_j]\cong\bigoplus_{\mu\vdash j} f^\mu V^\mu.
\]

Hence its normalized trace on `Z_j^2` is

\[
\frac1{j!}\operatorname{Tr}_{\mathrm{reg}}Z_j^2
 =\sum_{\mu\vdash j}\frac{(f^\mu)^2}{j!}R_\mu(t)^2
 =A_j(t).
\]

For left multiplication by any group-algebra element `X`, normalized regular trace is `[e]X`, so this equals `[e]Z_j^2`. Each transposition is self-adjoint under the involution `sigma^*=sigma^{-1}`; therefore every `J_r`, and hence `Z_j`, is self-adjoint for real/formal coefficients. Writing `Z_j=sum z_sigma sigma`, self-adjointness gives `z_{sigma^{-1}}=z_sigma`, and

\[
[e]Z_j^2=\sum_\sigma z_\sigma z_{\sigma^{-1}}
        =\sum_\sigma z_\sigma^2.
\]

Finally substituting `t=1/n` changes each factor to `(n-j-J_r)/(n-j+1-J_r)=(k-J_r)/(k+1-J_r)`. QED.

### Numerator-polynomial strengthening

The predecessor proved

\[
A_j(t)=\frac{P_j(t)}{\Delta_j(t)^2},
\quad
\Delta_j(t)=\prod_{s=1}^{j-1}(1-st),
\]

and rowwise telescoping gives the scalar

\[
H_\mu(t)=\Delta_j(t)R_\mu(t)
        =\prod_{r=1}^j(1-(j+\mu_r-r)t).
\]

Set `Y_j(t)=Delta_j(t) Z_j(t)`. The same regular-trace proof gives

\[
\boxed{
P_j(t)=[e]Y_j(t)^2
      =\sum_{\sigma\in S_j}y_{j,\sigma}(t)^2.
}
\]

Thus the exact numerator polynomial driving the source ratio is itself a central group-algebra norm square. This is the useful output of the #21/#14 route. It suggests trying conditional expectation in the tower `S_j subset S_{j+1}`, Weingarten convolution inequalities, or connected monotone-factorization expansions before computing more Taylor orders.

## 6. Exact diagonal-curvature block through order 32

Write

\[
G_j(t)=\log A_j(t)=\sum_{m\ge1}D_m(j)t^m,
\qquad
C_m(j)=2D_m(j)-D_m(j-1)-D_m(j+1).
\]

The predecessor proved the theorem-sized finite-degree statement

\[
\deg_jD_m\le m
\]

for every fixed `m`. The current checker uses the exact numerator polynomial to compute each `D_m(j)` much faster:

if

\[
P_j(t)=1+\sum_{m\ge1}p_m t^m,
\qquad
\log P_j(t)=\sum_{m\ge1}L_m t^m,
\]

then coefficient comparison in `P_j'=P_j (log P_j)'` gives

\[
L_m=p_m-\frac1m\sum_{r=1}^{m-1}rL_rp_{m-r},
\]

and therefore

\[
\boxed{
D_m(j)=L_m+\frac2m\sum_{s=1}^{j-1}s^m.
}
\]

The production self-check enumerates partitions exactly, computes hook dimensions and `P_j`, checks Plancherel mass `sum_mu(f^mu)^2=j!`, reconstructs each degree-`<=m` polynomial `D_m(j)` from `j=0,...,m`, and checks **two unused values**, `j=m+1,m+2`, before using the interpolation.

It proves the finite theorem

\[
\boxed{
C_m(j)>0
\quad\text{for every }2\le m\le32\text{ and every }j\ge m.
}
\]

More strongly, every coefficient of `C_m(m+x)` is strictly positive. The leading coefficient is exactly

\[
2m(m-1).
\]

For the four new orders beyond the predecessor's block, the minimum coefficient after shifting to the active sector `j=67+x` is:

- `m=29`: `1624`;
- `m=30`: `1740`;
- `m=31`: `1860`;
- `m=32`: `1984`.

This is deliberately reported as a **finite block**, not an all-order conjecture promoted to theorem.

## 7. New growing-defect theorem: exponent `33/34`

The exact source ratio is

\[
Q_j(n):=
\frac{F_j(n)^2}{F_{j-1}(n)F_{j+1}(n)}
=
\frac{j+1}{j}
\left(\frac{n-j+1}{n-j}\right)^2
\exp\!\left(2G_j(1/n)-G_{j-1}(1/n)-G_{j+1}(1/n)\right).
\]

For `j>=67`, every exact curvature coefficient through order 32 is nonnegative (`C_1=0`, and the block above handles `2<=m<=32`). It remains to control the tail.

The retained analytic-disk estimate gives

\[
|D_m(r)|\le2(6r)^m.
\]

If `n>8(j+1)`, put `q=6(j+1)/n<3/4`. For `r in {j-1,j,j+1}`, the post-order-32 remainder satisfies

\[
|R_r|
\le2\sum_{m\ge33}q^m
\le8q^{33}.
\]

Hence

\[
|2R_j-R_{j-1}-R_{j+1}|
\le32\,6^{33}\frac{(j+1)^{33}}{n^{33}}.
\]

The exact checker verifies

\[
2^{90}<32\,6^{33}<2^{91}.
\]

Assume now `j>=67` and

\[
\boxed{
n^{33}\ge2^{93}(j+1)^{34}.
}
\]

First, because `j+1>=68` and `2^93*68>8^33`, this hypothesis implies `n>8(j+1)`, so the analytic tail estimate is valid. Second,

\[
|\text{tail curvature}|
<\frac{1}{4(j+1)}.
\]

All retained curvature terms through order 32 are nonnegative, while

\[
\log\frac{j+1}{j}\ge\frac1{j+1}.
\]

The second deterministic factor `2 log((n-j+1)/(n-j))` is also positive. Therefore

\[
\log Q_j(n)>
\frac1{j+1}-\frac1{4(j+1)}>0.
\]

This proves:

### Theorem `NM13-07-P0282-THIRTY-THREE-THIRTY-FOURTHS-WINDOW-11`

For `j>=67`,

\[
\boxed{
n^{33}\ge2^{93}(j+1)^{34}
\Longrightarrow
F_j(n)^2>F_{j-1}(n)F_{j+1}(n).
}
\]

Since `8^34=2^102>2^93`, the simpler sufficient condition

\[
\boxed{
j+1\le\frac{n^{33/34}}8
}
\]

implies the theorem hypothesis. Chaining with the retained all-`n` theorem for `j<=66` advances the rigorous growing-defect exponent

\[
\boxed{29/30\longrightarrow33/34}.
\]

This remains **PARTIAL**. It does not control defects `j=Theta(n)` and is not source closure.

## 8. Exact self-check for the finite core

Idea-before-code artifact:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_weingarten_curvature36_row102_idea.md`

creation commit `273662caa42389de8e669301bf64c8fca18c45d5`.

Production checker:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_curvature32_selfcheck.py`

creation commit `eb288825b705acc7c311211affe14ec6fb57d97c`, SHA256

`db911e04b8419f4b79515801960633abfa9e73cc33720d9426240d7f2eec102a`.

Executed output:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_curvature32_selfcheck.out`

creation commit `e72e934612ecfcc6bb7a68e8a37166c8a25196e6`, SHA256

`fb4b93f42619e74e7769e343b61c42642ba5d48e139547ad9b8d9b57141e3fe6`.

The executed exact output records:

- exact numerator table through `j=34`, Taylor order 32;
- `p(34)=12310` partitions enumerated at the largest partition level;
- exact Plancherel mass at every level used;
- two unused-value checks for every interpolated `D_m`;
- coefficientwise positivity of `C_m(m+x)` for every `2<=m<=32`;
- leading coefficient `2m(m-1)` for every order in the block;
- active-sector minimum coefficients `1624,1740,1860,1984` for orders 29--32;
- exact tail constant `32*6^33=1528062933109708969803251712`, lying strictly between `2^90` and `2^91`;
- the disk-implication and simple-window power checks; and
- terminal line `ALL_EXACT_CHECKS_PASS`.

This is explicitly a **self-check**, not either required independent audit.

## 9. Frozen metric: exact row 102

The frozen metric is kept independent of the Taylor theorem. For row `n=102`, the retained exact theorem `j<=66` covers

`k=n-j>=36`.

Therefore only `k=2,...,35` require a new finite calculation; the checker reconstructs through `k=36` to supply the final neighbor.

Exact checker:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_row102_gessel_low.cpp`

creation commit `14d9c0eb60abc67e04caccbfdd35c7e3024e6db3`, SHA256

`da2c0cd0aef534fe902519efdf9e24e5bea125d771985021c10662ef261b3c2c`.

Executed output:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_row102_gessel_low.out`

creation commit `bc8489ee0e41c4003ae27dabb7b038d9ff4fbeb1`, SHA256

`1a876e57abb321be21f720323815d5bb11885364d39a1dc9ae0c7d57f2f6c254`.

The Gessel Bessel/Toeplitz determinant computation used **19** distinct independently trial-division-checked prime moduli. The CRT reconstruction modulus has **569 bits**, versus **539 bits** for `102!`, and is therefore safely larger than `2*102!`. The independent exact Catalan check

`u_2(102)=C_102`

passes. All **34** new source inequalities `k=2,...,35` are strictly positive.

The weakest newly computed ratio occurs at `k=35`:

\[
\frac{\ell_{102,35}^2}
     {\ell_{102,34}\ell_{102,36}}
\approx1.08549209919482518>1.
\]

The exact numerator, denominator, and positive margin are archived in the output. The checker ends `ALL_EXACT_CHECKS_PASS`.

Chaining the low seam with the retained `j<=66` theorem certifies every interior inequality in row 102. Together with the archived complete certificates through row 101, the frozen metric therefore moves

\[
\boxed{N_{\rm exact}:101\to102}.
\]

`unchanged_runs` remains `0 -> 0`; `stuck_recoveries` remains `0 -> 0`.

## 10. What the Weingarten route did and did not accomplish

The new norm identity is not a disguised solution. It does, however, produce a substantially better structural target than another raw moment expansion.

By Jucys' product identity,

\[
\prod_r(x-J_r)
\]

is the sign-twisted cycle-count central element. By Novak's Weingarten identity,

\[
\prod_r(N-J_r)^{-1}
\]

is the sign-twist of the unitary Weingarten central element, whose large-`N` expansion is governed by complete homogeneous symmetric functions in the `J_r` and monotone transposition factorizations. Hence

\[
Z_j(1/n)=\prod_r\frac{k-J_r}{k+1-J_r}
\]

is an adjacent-dimension convolution of two classical central elements, and `A_j` is exactly its squared regular `l2` norm.

What is still missing is a **cross-rank norm inequality** in the tower `Q[S_j] subset Q[S_{j+1}]` strong enough to compare the three adjacent norms appearing in Chen. Ordinary Cauchy--Schwarz inside one fixed rank does not by itself give that comparison. The next route should therefore target conditional expectation / branching or a monotone-factorization coupling across adjacent ranks, not another automatic Taylor order.

## 11. Status and closure discipline

Source verdict: **OPEN**.  
Worker verdict: **PARTIAL**.  
Frozen metric: **`N_exact=102`**.  
Retained complete fixed-defect Chen frontier: **`j<=66`**.  
Retained stronger ULC/shadow-density all-`n` frontier: **defect 32**.  
New rigorous growing-defect sufficient exponent: **`33/34`**.  
Novelty / priority: **UNVERIFIED**.  
P26 audit: **NOT PASSED**.  
NM13-08 audit: **NOT PASSED**.

Nothing is called closed. No paper folder is created because the literal all-`n` source remains open and the required two outside audits have not passed.

## 12. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-07
  namespace: proofnet24/NM13-07/
  source_id: aim_kpz_followup_2025
  canonical_claim_id: P0282
  canonical_dedup_key: chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis
  source_status_before: OPEN
  source_status_after: OPEN
  worker_status_before: PARTIAL
  worker_status_after: PARTIAL
  metric_name: N_exact
  metric_before: 101
  metric_after: 102
  metric_movement: true
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  methods:
    - number: 21
      name: ASK WHO ELSE HAS THIS SHAPE
      accounting: RECYCLED
      outcome: "Jucys/Weingarten and monotone-Hurwitz literature gives the correct central-element language; exact P0282 correction becomes a regular-representation l2 norm square."
    - number: 14
      name: FIND THE GROUP ACTING
      accounting: RECYCLED
      outcome: "proved Z_j content-spectrum / regular-trace norm identity and numerator-polynomial norm-square refinement."
    - number: 4
      name: PROVE SOMETHING WEAKER, COMPLETELY
      accounting: RECYCLED
      outcome: "exactly certified curvature block through order 32, derived 33/34 window, and certified row 102."
  new_local_claims:
    - NM13-07-P0282-JUCYS-WEINGARTEN-NORM-11
    - NM13-07-P0282-THIRTY-THREE-THIRTY-FOURTHS-WINDOW-11
  retained_fixed_defect_frontier: 66
  retained_ulc_shadow_density_frontier: 32
  growing_defect_exponent_before: "29/30"
  growing_defect_exponent_after: "33/34"
  p26_audit: NOT_PASSED
  nm13_08_audit: NOT_PASSED
  novelty: UNVERIFIED
  next_step: "exploit the exact Jucys/Weingarten l2 representation to seek an adjacent-rank conditional-expectation or monotone-factorization norm inequality; compute another Taylor order only as fallback."
```

## 13. Next mathematical route

Primary next route: use the tower of symmetric-group algebras and the exact central element

\[
Z_j(k)=\prod_{r=1}^j\frac{k-J_r}{k+1-J_r}
\]

to seek a conditional-expectation inequality under `Q[S_j] subset Q[S_{j+1}]`. In spectral language this is a Plancherel branching / content-growth problem; in coefficient language it is an `l2` comparison for an adjacent-dimension Weingarten convolution. A successful inequality would attack **all Taylor orders at once** and is therefore preferable to extending the finite curvature block.

Secondary route: translate the coefficients of `Z_j` into monotone transposition-factorization counts using the classical Weingarten expansion, then identify whether the discrete `j`-curvature is a connected / two-marked count with a fixed sign after the low-defect exceptional sector.

Fallback only: extend the exact curvature block beyond 32. Another routine row census is also secondary, although row 103 remains available if the structural route does not move.

## 14. Model / scheduler-control truth

The requested line `Model: GPT-6. Reasoning: maximum` remains prompt text only. The model actually visible to this report is **GPT-5.6 Sol** and the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface in this run offers title/prompt, schedule or relative-start fields, timing mode, enabled state, listing, and update operations. It still exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort receipt**. Therefore there is nothing in this interface I can lawfully toggle to make GPT-6/maximum binding. Doing so would require an owner-authorized product/workspace/API/admin scheduling surface that persists model-family and reasoning-effort fields into inference routing and returns authenticated runtime attestation.

The historical P26 response `You cannot modify this task` is an authorization-context boundary, not proof of global immutability. Current repository continuity records a later successful P26 update from another authorized context. If such a denial recurs, the compliant workaround is the owning or otherwise authorized account/workspace/API/admin context, an authorized ownership transfer where supported, or platform support for the **same existing task**. It is not task duplication, identity substitution, or permission bypass.

No scheduler, task configuration, permission, shared root ledger, peer namespace, workflow, public surface, email/Drive resource, or paid compute was modified by NM13-07 in this invocation.

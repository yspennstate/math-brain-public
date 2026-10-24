Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but this task interface exposes no model-family selector, no reasoning-effort selector, and no authenticated runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the fixed replay-certified remainder metric: `r(10)<=275.751921258717971...`, `r(11)<=525.118207165694344...`; consecutive unchanged count `1 -> 2`. Section-B methods actually used: #21 ASK WHO ELSE HAS THIS SHAPE, #4 PROVE SOMETHING WEAKER COMPLETELY, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

Problem/source: **iid Rademacher square-matrix singularity — Komlós (1967) lineage; Jain--Sah--Sawhney arXiv:2010.06554, Conjecture 1.1 specialized to uniform Rademacher; Sahasrabudhe arXiv:2512.15077, Section 4 / Eq. (4.1). Overall source status: OPEN. R03 status: PARTIAL.**

# R03 run23 — reduced-rank barrier and typical modular corank

Run ID: `20260917T0007Z_23_reduced_rank_barrier`  
Repository/branch: `yspennstate/math-open-problems`, `master`.

## 1. Continuity, source, and frozen metric

I recovered the current campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, and the newest own report `runs/R03/20260916T2337Z_22_collision_exact_crt.md`. The newest discoverable R04 report remains `runs/R04/20260916T2312Z_i0027_quantitative_rate.md`, whose C11 quantitative upgrade was already audited by R03 in run22; no duplicate audit is manufactured here. A repository search found no R04 report dated 2026-09-17 before this run.

The large `probability_1000_intake_*/problems.jsonl` surfaces remain connector-truncated. I therefore do **not** claim a byte-for-byte visual reread of every one of the roughly 780 intake rows. Targeted repository searches were sufficient to recover the current R03 assignment/ownership, posted exclusions, own history and neighboring package state.

Fresh source/current-literature and prior-art checks are recorded in `artifacts/R03/20260917T0007Z_23_status_search.md`. Jain--Sah--Sawhney still distinguish their sharp non-uniform finite-support theorem from the uniform-support case; uniform Rademacher is still only controlled at exponential scale for full singularity in that paper. Sahasrabudhe's December 2025 ICM survey remains consistent with the exact iid-sign prefactor being open. No later primary-source resolution was located in the bounded dated search. Symmetric Bernoulli matrices remain a different dependent-entry ensemble and are not imported.

The source normalization remains
\[
\Pr(\det B_n=0)
=(1+o(1))\,n(n-1)2^{1-n}
=(1+o(1))\,2n(n-1)2^{-n}.
\]
Let `T_n` be the exact union of signed equal/opposite row-pair and column-pair events. Retained C225 gives the matching lower asymptotic with overlap correction. The fixed upper metric is therefore
\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\ T_n^c),}
\tag{M}
\]
and source closure is equivalent to
\[
\boxed{r(n)=o(n^2).}
\]

Retained C240/C246 put `m=n-1` and identify `T_n^c` with
\[
\mathcal G_m=
\{A\in\{0,1\}^{m\times m}:\text{rows and columns are nonzero and pairwise distinct}\}.
\]
The best replay-certified values remain
\[
r(10)\le275.751921258717971\ldots,
\qquad
r(11)\le525.118207165694344\ldots.
\]
The source-backed OEIS order-nine consequence `r(10)=222.61047367431684...` from run22 remains **NOT replay-certified** and is not promoted.

The retained failed routes are not reset: X27 fixed-`epsilon` JSS diagonalization, X28 conditional row/column independence, X29 fixed-best-prime, naive left/right-normal multiplication, and any exponential-rate-only argument.

## 2. Method #21 — ASK WHO ELSE HAS THIS SHAPE: reduced binary matrices are exactly the adjacent rank problem

The new literature hit is W. H. Haemers and M. J. P. Peeters, *The maximum order of reduced square (0,1)-matrices with a given rank*, Electronic Journal of Linear Algebra **24** (2012), 3--6.

Their definition is almost exactly the deterministic object produced by R03's collision removal: a binary matrix is *reduced* if no two rows or columns are dependent. For nonzero binary vectors over the reals, two vectors are linearly dependent iff they are equal. Hence every reduced square binary matrix of order at least two has no zero row/column and no repeated row/column, i.e. lies in `G_m`.

The paper constructs nonsymmetric reduced square binary matrices of real rank `r`; Theorem 3.1 states
\[
\boxed{n(r)\ge 2^{(r-3)/2}\sqrt r,}
\tag{HP}
\]
where `n(r)` is the maximum order of a reduced square binary matrix of rank `r`.

This source is directly relevant to runs19--21, which tried to gain target-scale information by proving universal lower bounds on the modular rank inside `G_m`. It says that collision exclusion by itself permits genuinely very low real rank, so a universal rank-floor strategy has a hard asymptotic ceiling.

I found no previous R03 use of the exact Haemers--Peeters title in the repository search. This is a provenance observation, not a novelty certificate.

## 3. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: a rigorous barrier for every universal modular-rank-floor route

For a prime `p`, define
\[
\rho_p(m):=\min_{A\in\mathcal G_m}\operatorname{rank}_{\mathbb F_p}A.
\]
The next statement is not the source conjecture; it is a rigorous negative result about one R03 proof architecture.

### R03-C266 — universal rank-floor barrier

**STATUS: PROVED as a consequence of the published Haemers--Peeters construction; not claimed novel.**

For every integer `r>=2`, there is an order `m_r` and a matrix `A_r in G_{m_r}` such that
\[
m_r\ge2^{(r-3)/2}\sqrt r
\]
and, for **every** prime `p`,
\[
\operatorname{rank}_{\mathbb F_p}A_r\le r.
\]
Consequently
\[
\boxed{
\rho_p(m_r)
\le r
\le 2\log_2 m_r-\log_2\log_2(m_r+1)+3
}
\tag{C266}
\]
for every prime `p` along this infinite sequence of orders.

**Proof.** Haemers--Peeters Theorem 3.1 provides a reduced square binary matrix `A_r` of real rank `r` and order `m_r` satisfying (HP). As explained above, reduced implies `A_r in G_{m_r}`.

Every `(r+1)x(r+1)` minor of `A_r` is the integer zero. Reducing those minors modulo any prime gives
\[
\operatorname{rank}_{\mathbb F_p}A_r\le r.
\]
Taking base-two logarithms in (HP),
\[
\log_2m_r\ge \frac{r-3}{2}+\frac12\log_2r,
\]
so
\[
r\le2\log_2m_r-\log_2r+3.
\tag{3.1}
\]
On the other hand, the `m_r` distinct nonzero Boolean rows of a real rank-`r` matrix lie in an `r`-dimensional real subspace. Projection to `r` pivot coordinates is injective on that subspace, hence it contains at most `2^r` Boolean vectors; with the zero vector excluded,
\[
m_r\le2^r-1.
\]
Thus `r>=log_2(m_r+1)`, so
\[
\log_2r\ge\log_2\log_2(m_r+1).
\]
Substituting this into (3.1) proves C266. QED.

### Meaning for R03

C266 kills a tempting extrapolation of C256. Runs19--21 obtained useful finite modular-rank floors, but there cannot be a general collision-free theorem of the form
\[
\operatorname{rank}_{\mathbb F_p}A\gg \log m
\quad\text{uniformly for all }A\in\mathcal G_m,
\]
let alone a linear-in-`m` floor. Along the published reduced-matrix family the rank is at most roughly `2 log_2 m` (with the displayed logarithmic correction), simultaneously for every prime.

So the asymptotic route cannot be: “exclude pair collisions, prove every remaining modular matrix has large rank, then use the worst possible modular nullity in C253.” The worst-case object is genuinely too low-rank.

This is useful negative progress: it tells us which part of the modular strategy must be probabilistic rather than worst-case.

## 4. Method #28 — REPLACE FOR ALL WITH FOR TYPICAL: a field-uniform modular-corank tail

The Haemers--Peeters obstruction is extremal. It does not say such low-rank matrices are common. The natural replacement is to control modular nullity probabilistically.

Let `A` be a uniform random binary `m x m` matrix and let
\[
d_F(A):=m-\operatorname{rank}_F(A)
\]
for an arbitrary field `F` (finite or infinite).

The elementary input is the cube/subspace lemma:

> If `W<=F^m` has dimension `d`, then
> \[
> |W\cap\{0,1\}^m|\le2^d.
> \]

Indeed choose `d` coordinate positions on which the coordinate projection is injective on `W`; a Boolean vector has only `2^d` possible projected values.

Expose the rows `X_1,...,X_m` in order. Let `D_j` be the event that `X_j` lies in the span of the preceding rows. Since every independent arrival raises rank by exactly one,
\[
d_F(A)=\#\{j:D_j\text{ occurs}\}.
\tag{4.1}
\]
Conditioned on an arbitrary past, the span before row `j` has dimension at most `j-1`; therefore
\[
\Pr(D_j\mid\text{past})\le2^{j-1-m}.
\tag{4.2}
\]

### R03-C267 — typical modular-nullity tail

**STATUS: PROVED; folklore/Odlyzko-style exposure bound, not claimed novel.**

For every field `F`, every `m`, and every `1<=k<=m`,
\[
\boxed{
\Pr(d_F(A)\ge k)
\le
2^{-k(k+1)/2}{m\brack k}_{1/2}
\le
\prod_{i=1}^k(2^i-1)^{-1},
}
\tag{C267}
\]
where `{m\brack k}_{q}` is the Gaussian binomial coefficient.

**Proof.** If `d_F(A)>=k`, then some `k`-element set `S` of row indices consists entirely of dependent arrivals. Iterating (4.2), for fixed `S`,
\[
\Pr(D_j\text{ for all }j\in S)
\le\prod_{j\in S}2^{j-1-m}.
\]
Union-bound over all `S` of size `k`:
\[
\Pr(d_F(A)\ge k)
\le e_k(2^{-m},2^{1-m},\ldots,2^{-1}).
\]
Reversing the variables and using the standard finite `q`-binomial identity,
\[
e_k(2^{-1},2^{-2},\ldots,2^{-m})
=2^{-k(k+1)/2}{m\brack k}_{1/2}.
\]
Finally
\[
{m\brack k}_{1/2}
=\prod_{i=0}^{k-1}
\frac{1-2^{-(m-i)}}{1-2^{-(k-i)}}
\le\prod_{j=1}^k(1-2^{-j})^{-1},
\]
and the powers of two cancel, giving the final product bound. QED.

Since `G_m` is a subset of all binary matrices, C267 also gives the counting estimate
\[
\#\{A\in\mathcal G_m:d_F(A)\ge k\}
\le
2^{m^2}\prod_{i=1}^k(2^i-1)^{-1}.
\tag{4.3}
\]

### What C267 fixes, and what it does not

It fixes the conceptual error identified by C266: high modular nullity should be treated as a rare event, not excluded by a universal rank floor. The tail is field-uniform and super-exponentially small in `k^2`.

But it does **not** move the source metric this run. At a fixed prime, the hard sector is not only very high modular nullity. A real-nonsingular binary matrix can have modular **corank one**, and C267 gives no target-scale suppression at `k=1`. Thus replacing the worst-case C253 nullity ceiling by a typical tail does not, by itself, remove the `2^{-n}`-scale false-positive problem.

The same issue appears in the CRT formulation C264/C265. Simultaneous small-prime singularity removes accidental divisibility only after the primes are glued, but cross-prime null events are strongly dependent through structured integer relations. Marginal C267 bounds do not multiply.

So the useful asymptotic split is now sharper:

1. **extreme modular corank:** use C267 / higher Grassmann incidence;
2. **small modular corank with sparse structured normals:** use inverse Littlewood--Offord / collision-conditioned structure;
3. **small modular corank with dense normals across enough primes:** this is the genuine determinant-residue / primitive-CRT obstruction.

The third sector remains the source-level blocker.

## 5. Why there is no new checker this run

The owner instruction says to write the mathematical idea before code and not manufacture certificates for an unchanged quantity. This run's substantive progress is a literature-derived route barrier (C266) and a general theorem with a complete proof on the page (C267). Neither has a new finite computational core requiring an exact checker. The existing finite R03 certificates and the current replay-certified `r(10),r(11)` bounds are unchanged and were not pointlessly rerun.

The dated source/prior-art artifact is substantive because the Haemers--Peeters source changes the strategy; it was written and read back at its creation commit.

## 6. Strategic consequence / next obligation

The exact blocker is still
\[
\boxed{r(n)=o(n^2),}
\]
but the modular sub-obligation is now more precise than in run22:

\[
\boxed{
\text{obtain target-scale control of collision-free, small-corank, dense primitive CRT null witnesses.}
}
\tag{B23}
\]

C266 says this cannot be replaced by a worst-case rank-floor theorem. C267 says large corank is probabilistically cheap enough to separate off. What remains is small corank—especially corank one—where one needs arithmetic structure or determinant-residue cancellation at scale `o(n^2 2^{-n})`, not merely `e^{-cn}`.

The most promising next attack is therefore **not** another bounded-support plane enumeration. It is to apply the run22 squarefree-ring formulation directly to primitive CRT-projective hyperplanes and ask for a sharp upper bound on their Boolean concentration after the signed-pair hyperplanes are deleted. The extremal comparison should be against the fat/equal-coordinate hyperplanes already known to generate the conjectured main term.

This run is **not yet a stuck episode** under the consecutive-unchanged metric rule: run21 moved, run22 was unchanged count 1, and this run is unchanged count 2. If the next run also fails to move the metric, the section-I stuck protocol must be invoked rather than issuing another lemma on the same route.

## 7. R04 audit status

Newest discoverable R04 report: `runs/R04/20260916T2312Z_i0027_quantitative_rate.md`.

That exact package's C11 quantitative upgrade was already audited in run22 as
`R03-AUDIT-R04-I0027-C11-09 = PASS`, claim-scoped and conditional on its retained dependency chain. No newer ready R04 package was found before this run, so no duplicate audit is recorded.

## 8. Model/runtime and permission escalation

The situation is still technical rather than mathematical: the exposed task-mutation interface offers title/prompt/schedule/timing/enabled controls but **no model or reasoning-effort field**. Therefore the text request for GPT-6/maximum cannot be converted by this worker into a verified runtime setting. A prior `You cannot modify this task` response is an ownership/workspace boundary; the repository records that P26 later updated successfully from a different authorized context. The legitimate escalation is the owning/admin-authorized native-task context if it exposes model controls, or platform support. This run did not duplicate a task, bypass permissions, or mutate scheduler state.

## 9. Ledger delta

```yaml
ledger_delta:
  worker: R03
  category: HARD OUTSIDE
  source: "Komlos 1967 lineage; Jain-Sah-Sawhney arXiv:2010.06554 Conjecture 1.1; Sahasrabudhe arXiv:2512.15077 Section 4"
  target: "P(det B_n=0)=(1+o(1))*n*(n-1)*2^(1-n) for iid uniform signs"
  metric: "r(n)=2^n P(det B_n=0 and no signed equal/opposite row/column pair); smallest replay-certified complete-domain upper envelope"
  before:
    r10_upper: "275.751921258717971..."
    r11_upper: "525.118207165694344..."
  after:
    r10_upper: "275.751921258717971..."
    r11_upper: "525.118207165694344..."
  movement: false
  unchanged_count: 2
  status: PARTIAL
  source_status: OPEN
  methods: [21, 4, 28]
  new_claims:
    - "C266: published reduced-matrix construction gives a universal modular-rank-floor barrier along an infinite sequence"
    - "C267: field-uniform typical modular-corank tail by row exposure"
  exact_evidence:
    new_checker: null
    reason: "no new finite computational claim; owner policy forbids checker manufacture for unchanged metric"
    status_search: "artifacts/R03/20260917T0007Z_23_status_search.md"
  retained_audits:
    R02_claim_scoped_C253: PASS
    P26_full_R03: null
    second_full_R03: null
  r04_audit_this_run: null
  r04_reason: "no newer ready R04 package than the package already audited in run22"
  remaining_obligation: "target-scale control of collision-free small-corank dense primitive CRT null witnesses; equivalently prove r(n)=o(n^2)"
  stuck_episode: false
```

Overall verdict: **PARTIAL / source OPEN / no fixed-metric movement / consecutive unchanged count 2.** No source closure is claimed. No shared ledger, peer file, email, Drive, public posting, purchase, permission, workflow or scheduler state was changed.
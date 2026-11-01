Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this scheduler exposes no model/reasoning selector, so GPT-6 / maximum was requested but cannot be claimed.
Problem/source: Beck–Fiala vector balancing — Beck–Fiala (1981), as restated in Bansal–Jiang arXiv:2508.03961v2 §1. Metric movement: B(t,n) was UNMEASURED in the fleet ledger; this run proves the explicit all-dimensions bound B_R16(t) below. Run status: PARTIAL for fleet closure (two required external audits are still missing); the source conjecture now has a fresh full-resolution preprint claim.

# R16 — support-sensitive directional-variation bound for Beck–Fiala

## 1. State recovery and current-source check

Repository: `yspennstate/math-open-problems`, branch `master`.

Read before doing mathematics:
- `probability_campaign_2026_09/INDEX.md`
- `probability_campaign_2026_09/RANKING.md`
- root `POSTED.md`
- root `RESULTS.md`
- root `QUEUE.md`
- `operations/FLEET_2026-09-16.md`
- `operations/RFLEET_2026-09-16.md`
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`
- recursive repository tree plus exact-target/ownership searches over the indexed repository.

The protocol path `proofnet24/R16-beck-fiala/` and `runs/R16/` were not present at the time of recovery. I therefore did **not** invent an old baseline. The current root ledger gives R16 `UNMEASURED -> UNMEASURED`, status `OPEN`, with the explicit warning that Bansal–Jiang already cover `t >= log^2 n`. That ledger value is the before-value for this run.

The recursive tree response was too large for the connector to return in full. I therefore do not claim to have semantically re-read all ~780 intake rows. I did read the available fleet/index ledgers and ran repository-wide exact-target/owner searches; those searches found no second R16 owner and no Beck–Fiala intake claim superseding the hard-outside assignment.

### Fresh literature/status queries, 2026-09-16

1. **Bansal–Jiang**, arXiv:2508.03961v2 (2025), was opened directly. Its abstract and Theorem 1.3 say:
   - `O(sqrt(t))` for `t = Omega(log^2 n)`;
   - `\widetilde O(sqrt(t)+sqrt(log n))` in the smaller-sparsity regime;
   - the tilde hides poly(log log n) factors.
   So it is not a full all-`t` solution.

2. **Altschuler–Tikhomirov**, arXiv:2607.14238 (2026), was checked as a later development. It pushes the `O(sqrt(t))` regime down to essentially logarithmic sparsity, still not every `t`.

3. A newer primary source changes the status materially: **Shengtao Guo, Ethan X. Fang, Junwei Lu, “Vector Balancing via Directional Total Variation,” arXiv:2609.11189v1, submitted 2026-09-10.** Theorem 1.1 gives Komlós discrepancy `< 3 sqrt(2 pi)`; Corollary 1.2 explicitly states, for the exact Beck–Fiala matrix class,
   \[
      \operatorname{disc}(A)<3\sqrt{2\pi t}
   \]
   for every positive integer `t`, with no restriction involving `n`. The paper is existential and does not claim a polynomial-time algorithm.

4. Searches on 2026-09-16 for corrections, withdrawals, later author papers, and proof-specific critiques found v1 only and no concrete correction/withdrawal. This is a six-day-old arXiv preprint, so that absence is **not** treated as mature external validation.

Primary URLs checked:
- https://arxiv.org/html/2508.03961v2
- https://arxiv.org/html/2609.11189v1
- https://arxiv.org/abs/2607.14238
- https://arxiv.org/abs/1306.6081

The outside conjecture is therefore **literature-resolution claimed** as of 2026-09-10. This run does not merely rename that corollary: it derives a direct incidence-sensitive improvement of its numerical bound.

## 2. Counterexample-first exact finite search

Before the proof attack I exhaustively searched, modulo column permutations, all `4 x n` binary matrices with `n <= 6` and column support at most `t`, for `t=1,2,3,4`. Every candidate discrepancy was computed by exhaustive enumeration of all sign vectors.

Exact worst values:
\[
 t=1:1,\qquad t=2:2,\qquad t=3:2,\qquad t=4:2.
\]

For `t=2,3,4`, one extremal finite witness in this search has the three nontrivial columns
\[
(0,0,1,1)^T,\quad (0,1,0,1)^T,\quad (0,1,1,0)^T
\]
and discrepancy `2`.

This finite search neither proves nor refutes the asymptotic theorem. It is archived as an exact-arithmetic self-check in `artifacts/R16/`.

## 3. Imported analytic ingredient, with scope checked

For a probability density `rho` on `R^m`, write
\[
V_u(\rho)=|D_u\rho|(\mathbb R^m)
\]
for directional total variation.

The Guo–Fang–Lu proof establishes the following pieces, which I checked against the current v1 source:

- the open Banaszczyk transform
  \[
  \mathcal T_vK=((K-v)\cap(K+v))+\{sv:-2<s<2\}
  \]
  is contained in `(K-v) union (K+v)`;
- their Section 3 proves Minkowski convexity of anisotropic Cheeger values for finite integrands
  \[
  H(\xi)=\sum_\ell \alpha_\ell |u_\ell\cdot\xi|
  \]
  by the Wang–Xia inverse-power eigenvalue inequality, a `p downarrow 1` limit, and a strongly-convex regularization;
- their finite common-density separation argument is explicit before the countable-dense-direction passage;
- the lift/rearrangement identity gives
  \[
  \int |s|R^\star
  =\frac32-\frac1{24}\int_0^6(6-h)
      \|\rho-\rho(\cdot+hv)\|_1\,dh
  \ge \frac32-\frac32 V_v(\rho);
  \]
- the height-one section of the symmetrized lift is exactly `T_v K`.

I use only these proved finite-direction ingredients and reproduce the heterogeneous-budget extension needed below.

## 4. R16-BF-01 — finite heterogeneous directional preservation

**Claim R16-BF-01 — PROVED.**

Let `K` be a nonempty bounded open convex subset of `R^m`. Let `u_1,...,u_N` be finitely many directions, including the coordinate basis, and let `b_i>0`.

Assume that for every `beta_i >= 0`, with
\[
H_\beta(\xi)=\sum_i\beta_i|u_i\cdot\xi|,
\]
one has
\[
h_{H_\beta}(K)\le \sum_i\beta_i b_i. \tag{4.1}
\]
Then there is a single probability density `rho in BV`, supported in `K`, such that
\[
V_{u_i}(\rho)\le b_i,\qquad i=1,\dots,N. \tag{4.2}
\]

### Proof

Let
\[
S=\{z\in\mathbb R^N:\exists \rho\in\mathcal P(K),\ z_i\ge V_{u_i}(\rho)\ \forall i\}.
\]
`S` is convex and coordinatewise upward closed. If no density satisfies (4.2), `S` is disjoint from the open box
\[
Q=\{z:z_i<b_i\ \forall i\}.
\]
Finite-dimensional separation yields nonzero `beta` with
\[
\inf_{z\in S}\beta\cdot z\ge\sup_{q\in Q}\beta\cdot q.
\]
Upward closure forces every `beta_i >= 0`; otherwise moving arbitrarily far in a coordinate with negative coefficient contradicts separation. Hence
\[
\inf_{\rho\in\mathcal P(K)}\sum_i\beta_i V_{u_i}(\rho)
\ge \sum_i\beta_i b_i,
\]
and strict separation after replacing each `b_i` by `(1-epsilon)b_i` contradicts (4.1). Thus the infimum of `max_i V_{u_i}(rho)/b_i` is at most one.

The listed coordinate directions have finite budgets, so a minimizing sequence has uniformly bounded full BV norm on the fixed bounded support. The compactness statement proved in Guo–Fang–Lu Lemma 3.1 supplies an `L^1`-convergent subsequence. Lower semicontinuity of each finite directional variation gives a limiting density satisfying (4.2). ∎

### Prescribed-section form

Let `B` be a bounded open convex subset of `R^m x R`, symmetric under `(y,s)->(y,-s)`, and write `D_a={y:(y,a) in B}`. Suppose a probability density `R` supported in `B` satisfies
\[
V_{(u_i,0)}(R)\le b_i
\]
for the same finite list, and
\[
\int |s|R(y,s)\,dy\,ds\ge a.
\]
Then `D_a` supports a density with every bound `V_{u_i}\le b_i`.

Indeed, fix arbitrary `beta_i>=0` and set `g(r)=h_{H_beta}(D_r)`. Guo–Fang–Lu Lemma 3.2 plus section inclusion makes `g` convex and nondecreasing. Slicing and Fatou give
\[
\int V_{u_i}(R_s)\,ds\le V_{(u_i,0)}(R).
\]
If `q(s)=int R(y,s)dy` and `M=int|s|q(s)ds`, then
\[
\int q(s)g(|s|)\,ds\le\sum_i\beta_i b_i.
\]
Jensen and monotonicity give
\[
h_{H_\beta}(D_a)\le h_{H_\beta}(D_M)
\le\int q(s)g(|s|)\,ds
\le\sum_i\beta_i b_i.
\]
Apply R16-BF-01. ∎

## 5. R16-BF-02 — finite-list transform stability

**Claim R16-BF-02 — PROVED.**

Let `K` support a probability density `rho` with `V_{u_i}(rho)<=b_i` for a finite list containing the coordinate basis and a vector `v` in the list. If
\[
V_v(\rho)\le\frac13,
\]
then `T_v K` is nonempty and supports a new density with the same finite list of bounds.

### Proof

Use the Guo–Fang–Lu lift
\[
R(y,s)=\frac16\rho(y+sv){\bf1}_{|s|<3}.
\]
Its symmetric decreasing vertical rearrangement `R^*` is supported in the symmetric convex lift whose height-one section is `T_v K`, and horizontal fiber rearrangement does not increase any of the finitely many horizontal variations:
\[
V_{(u_i,0)}(R^\star)\le V_{u_i}(\rho)\le b_i.
\]
The exact height identity gives
\[
\int |s|R^\star\ge\frac32-\frac32V_v(\rho)\ge1.
\]
Apply the prescribed-section result from §4 at height one. ∎

This finite-list version is the key point: the incidence proof below never needs a global Euclidean directional bound and never assumes the Komlós conjecture.

## 6. R16-BF-03 — support-sensitive all-`t` Beck–Fiala bound

**Claim R16-BF-03 — PROVED.**

Let `A in {0,1}^{m x n}` have at most `t` ones in each column. Define
\[
R_t:=6\,\frac{t!}{t^t}\sum_{r=0}^{t-1}\frac{t^r}{r!}. \tag{6.1}
\]
Then there is `epsilon in {+-1}^n` such that
\[
\boxed{\ \|A\epsilon\|_\infty<R_t\ }. \tag{6.2}
\]
Moreover, for every finite `t`,
\[
\boxed{\ R_t<3\sqrt{2\pi t}\ }. \tag{6.3}
\]

### Proof

For `C>0` take the product cosine-squared density on the open cube:
\[
\rho_C(x)=C^{-m}\prod_{i=1}^m\cos^2\!\left(\frac{\pi x_i}{2C}\right){\bf1}_{(-C,C)^m}(x).
\]
Guo–Fang–Lu Lemma 2.4 computes, exactly,
\[
V_u(\rho_C)=\frac{\pi}{C}\mathbb E\left|\sum_i u_iT_i\right|, \tag{6.4}
\]
where the `T_i` are iid with density
\[
f_T(x)=\frac{2}{\pi(1+x^2)^2}.
\]

If `v` is a binary column of support `k<=t`, then
\[
V_v(\rho_C)=\frac{\pi}{C}\mathbb E|T_1+\cdots+T_k|.
\]
Because `T_{k+1}` is centered,
\[
\mathbb E|S_{k+1}|=\mathbb E[\mathbb E(|S_k+T_{k+1}|\mid S_k)]\ge\mathbb E|S_k|
\]
by Jensen. Thus every input column obeys
\[
V_v(\rho_C)\le\frac{\pi}{C}\mathbb E|S_t|.
\]

Set
\[
C=3\pi\,\mathbb E|S_t|. \tag{6.5}
\]
Then every input column has directional variation at most `1/3`. For each coordinate direction,
\[
V_{e_i}(\rho_C)=\frac{\pi}{C}\mathbb E|T|=\frac{2}{C}<\infty.
\]
Hence the finite list consisting of all input columns together with the coordinate basis satisfies the hypotheses of R16-BF-02.

Starting with `K_0=(-C,C)^m`, iterate
\[
K_j=\mathcal T_{v_j}K_{j-1}.
\]
R16-BF-02 preserves the entire finite list of directional budgets at every step, so each transform remains nonempty. Symmetry is preserved. The translate-containment lemma
\[
\mathcal T_vK\subset(K-v)\cup(K+v)
\]
then gives the standard backward sign recovery from `0 in K_n`: there are signs with
\[
\sum_j\epsilon_jv_j\in K_0.
\]
Thus the discrepancy is strictly below `C`.

It remains to evaluate `C`. The Fourier transform of `f_T` is
\[
\varphi_T(s)=(1+|s|)e^{-|s|};
\]
this follows by differentiating the standard transform of `(x^2+a^2)^{-1}` with respect to `a` and setting `a=1`.

For any symmetric integrable random variable `X`,
\[
\mathbb E|X|=\frac2\pi\int_0^\infty\frac{1-\varphi_X(s)}{s^2}\,ds.
\]
Consequently,
\[
\mathbb E|S_t|=\frac2\pi\int_0^\infty\frac{1-(1+s)^te^{-ts}}{s^2}\,ds.
\]
Integration by parts gives
\[
\mathbb E|S_t|=\frac{2t}{\pi}\int_0^\infty(1+s)^{t-1}e^{-ts}\,ds
=\frac2\pi\frac{t!}{t^t}\sum_{r=0}^{t-1}\frac{t^r}{r!}.
\]
Substitution into (6.5) proves (6.1)-(6.2).

Finally the same paper gives the exact mixture
\[
T_i\stackrel d=\frac{G_i}{\sqrt{Q_i}},\qquad Q_i\sim\chi^2_3,
\]
all independent. Conditional on the `Q_i`,
\[
\mathbb E(|S_t|\mid Q)=\sqrt{\frac2\pi}\sqrt{\sum_iQ_i^{-1}}.
\]
Since `E Q_i^{-1}=1` and the square root is strictly concave,
\[
\mathbb E|S_t|=\sqrt{\frac2\pi}\mathbb E\sqrt{\sum_iQ_i^{-1}}<\sqrt{\frac{2t}{\pi}}
\]
for every finite `t`. Multiplying by `3 pi` proves (6.3). ∎

### Prior-art label

I found no occurrence in the fresh searches of formula (6.1) as a Beck–Fiala bound. Guo–Fang–Lu use the uniform Euclidean estimate and obtain `3 sqrt(2 pi t)` after rescaling. Therefore R16-BF-03 is labelled **PROVED WITHIN THIS RUN / LITERATURE NOVELTY UNVERIFIED**, not “new theorem” without qualification.

## 7. The tracked bound after this run

Because discrepancy is integer-valued for a binary matrix, (6.2) gives
\[
\operatorname{disc}(A)\le \lceil R_t\rceil-1.
\]
For comparison:
- Beck–Fiala’s finite-degree floating-colors argument is recorded in Bukh’s primary paper as `2t-2` (for the nontrivial range);
- Bednarchak–Helm prove `2t-3` for `t>=3`;
- Bukh proves `2t-\log^*t` for sufficiently large `t`, but the theorem is stated with an unspecified “sufficiently large” threshold and is asymptotically much larger than `R_t`;
- Bansal–Jiang and Altschuler–Tikhomirov have stronger algorithmic structure in restricted `t,n` regimes, but their displayed `O` constants are not a complete numerical all-parameter `B(t,n)`;
- Guo–Fang–Lu give the explicit all-parameter real bound `<3 sqrt(2 pi t)`.

A fully explicit uniform integer bound obtained from complete numerical constants is therefore
\[
B_{\rm R16}(t,n)=B_{\rm R16}(t):=\begin{cases}
1,&t=1,\\
2,&t=2,\\
\min\{2t-3,\ \lceil R_t\rceil-1\},&t\ge3.
\end{cases} \tag{7.1}
\]

The exact checker shows the support-sensitive term first strictly beats `2t-3` at `t=16`:
\[
R_{16}=\frac{7944785883214161}{281474976710656}=28.22554948\ldots,
\]
so
\[
B_{\rm R16}(16)=28\quad\text{versus}\quad 2t-3=29.
\]
For `t>=17`, the simpler bound `R_t<3 sqrt(2 pi t)<2t-3` already shows the variation term stays better. Thus (7.1) closes the former sparse-regime gap with an exact finite-`t` formula and no dependence on `m` or `n`.

**Tracked metric:**
- before: `UNMEASURED` (root fleet ledger; no recoverable R16 run report);
- after:
  \[
  B(t,n)\le B_{\rm R16}(t)
  \]
  with `R_t` given exactly by (6.1).

This is a strict measurable movement.

## 8. Exact certificate

Artifact: `artifacts/R16/2026-09-16T13-56-00Z__beck_fiala_exact_checker.py`

It uses exact Python `Fraction` arithmetic for every certified finite claim. It:
- verifies the two exact finite-sum formulas for `R_t` for `1<=t<=200`;
- verifies exact monotonicity over that finite range (the theorem uses the all-`t` Jensen proof above, not the finite check);
- verifies that the first integerized improvement over the `2t-3` baseline is `t=16`;
- exhaustively enumerates all column-multisets for `4 x n`, `n<=6`, `t=1,2,3,4`, and all signings;
- prints `ALL_EXACT_CHECKS_PASS`.

Checker-output SHA-256: `52efb6e54f7d0e840d7adb303c2d76112ab1fe68637e954e04735acc4c0608db`.

## 9. Audit status and R12 cross-read

The current repository states that the second-audit cycle is `R12 -> R13 -> R16 -> R12`.

I explicitly checked the **revised** R12 assignment from the current repository: it is no longer the old AT problem. It is Paley degree-four SOS, Randomstrasse / arXiv:2603.29571 Conjecture 28, intake I0102.

No complete post-reassignment R12 proof package was found in the repository search/tree during this run, so no R12 mathematical audit was fabricated.

Required audits for an R16 portfolio closure:
- P26 audit: **PENDING / not found for this package**.
- second independent audit: **PENDING**.

Therefore the fleet status of this package is **PARTIAL**, even though R16-BF-03 is written as a complete proof and the outside conjecture now has a direct v1 resolution claim.

## 10. Failed / superseded routes

- Treating Bansal–Jiang’s `t>=log^2 n` theorem as full Beck–Fiala: superseded and scope-wrong.
- Typical/random incidence systems: wrong target.
- Vector coloring without scalar sign recovery: wrong target.
- Spencer’s six-deviations theorem: wrong parameter regime.
- Assuming R13/Komlós: not used.
- Continuing to attack affine spectral-independence’s logarithmic loss as though no all-`t` theorem existed: status-obsolete after arXiv:2609.11189v1.
- Pure finite enumeration: retained only as a refutation search/certificate, never as asymptotic evidence.

## 11. Rotation / next outside target

Because the original Beck–Fiala source target now has a direct full-resolution preprint and the R16 metric has moved to an explicit all-`t` formula, the protocol requires this worker not to invent a new personal conjecture here.

The highest-ranked unowned HARD queue item was checked: **I0101 — Afonso Bandeira, Randomstrasse101 Conjecture 27:** for sufficiently large primes `p == 1 mod 4`,
\[
\vartheta(\overline{G_{p,2}})\le\frac23\sqrt p.
\]
The original Randomstrasse post was opened directly. Fresh searches on 2026-09-16 for `"2-localization" Paley Lovasz theta`, `"Conjecture 27"`, and later Kunisky/Bandeira work found the conjecture still stated as open and no resolution. `operations/claims/I0101.md` was absent and repository search found no existing owner.

A create-only claim is attempted only **after** this R16 report and exact certificate are preserved. If the claim conflicts, ownership wins and the worker will not overwrite it.

## 12. Structured ledger delta for P26

```json
{
  "track": "R16 HARD OUTSIDE",
  "source": "Beck–Fiala, Integer-making theorems (1981); Bansal–Jiang arXiv:2508.03961v2 §1",
  "target": "uniform discrepancy bound for every binary t-column-sparse matrix",
  "metric": "best complete explicit uniform B(t,n)",
  "before": "UNMEASURED",
  "after": "B_R16(t)=1 (t=1), 2 (t=2), min(2t-3, ceil(R_t)-1) (t>=3), R_t=6 t!/t^t sum_{r=0}^{t-1} t^r/r!",
  "status": "PARTIAL",
  "source_status": "full-resolution claimed by Guo-Fang-Lu arXiv:2609.11189v1; v1 only",
  "unchanged_count": 0,
  "exact_evidence": [
    "artifacts/R16/2026-09-16T13-56-00Z__beck_fiala_exact_checker.py",
    "artifacts/R16/2026-09-16T13-56-00Z__beck_fiala_exact_checker.out",
    "checker_sha256:52efb6e54f7d0e840d7adb303c2d76112ab1fe68637e954e04735acc4c0608db"
  ],
  "audit_ids": {
    "P26": "PENDING",
    "second": "PENDING",
    "R12_cross_audit": "PENDING_NO_COMPLETE_REVISED_PACKAGE_FOUND"
  }
}
```

## 13. Remaining obligations

1. Independent P26 full-proof audit of R16-BF-01 through R16-BF-03.
2. A second independent track audit.
3. If both pass, produce the required self-contained `paper_<name>/` package before any portfolio closure claim.
4. External maturity: arXiv:2609.11189 is only v1, six days old; continue checking for corrections/withdrawals even though its present argument was source-audited here.

No email, Drive, public posting, permission change, or schedule change was attempted.

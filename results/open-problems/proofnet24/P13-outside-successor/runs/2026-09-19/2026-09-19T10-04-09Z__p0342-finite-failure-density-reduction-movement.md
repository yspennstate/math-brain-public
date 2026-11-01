Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. MOVEMENT: `M_P0342 = 0/2 -> 1/2`; the frozen `FINITE-FAILURE` obligation is proved for the one fixed functional `Theta=Psi+Phi`, while `FRINGE` remains open. Methods actually tried: B3, B18, B30.**

# P13 / P0342 — positive-variance transfer counterexample: finite failure proved, fringe reduced to one density law

UTC run time: 2026-09-19T10:04:09Z  
Repository: private `yspennstate/math-open-problems`, branch `master`  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`  
Own root: `proofnet24/P13-outside-successor/`

## 1. Continuity, ownership, and history recovery

I continued the newest lawful P13 successor rather than the stale scheduler title. The former I0051 / Aldous--Janson Open Problem 9 clade-covariance target remains **RETIRED** and was not reopened. C0021 reached its six-unchanged-run terminal handoff and was not reopened. The mandatory first successor screen I0054 remains exclusively owned by R11, whose later reports continue that claim; P13 did not touch it.

The newest current P13 claim is `operations/claims/P0342.md`, created 2026-09-19 UTC and naming this exact native slot. It is **CLOSABLE OUTSIDE**, with frozen witness and frozen denominator. There is a repository-history irregularity between the last immutable P13 report at 07:45 UTC and this claim: P0281 and then P0342 research artifacts/claims were created without an immutable P13 run report in `runs/2026-09-19/`. I preserve that as a **HISTORY_GAP** rather than inventing a missing report. The current canonical P0342 claim is later than P0281 and is the target continued here; no old claim file was overwritten or edited.

The controlling source is David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), Open Problem 12, §4.10, printed p.44. The source asks whether, whenever a CLT holds for a functional along the stationary infinite fringe process,

\[
  \sum_{i=0}^{m-1}\Phi(T_i),
\]

the same CLT necessarily holds for the corresponding finite-tree sum

\[
  \sum_{i=1}^{n}\Phi(T_i^{(n)})
\]

in `DTCS(n)`.

The source immediately before the problem says only that, "arguing as in [3] one could show" the fringe process is ergodic. I do **not** promote that sentence to a proved input. That missing proof is now the exact surviving issue for the frozen witness below.

## 2. Source/current-literature refresh, 2026-09-19 UTC

Queries checked today included the exact Open Problem 12/fringe-process wording together with the source arXiv ID, the later author paper on the exchangeable-partition/fringe-tree representation, the 2025 harmonic-descent-chain CLT paper, and the August 2026 fragmentation paper.

Primary source: https://arxiv.org/abs/2303.02529v3 and PDF https://arxiv.org/pdf/2303.02529v3 . Parsed PDF text was accessible and gives Open Problem 12 exactly on printed p.44. Required page-image attempts for the relevant p.43--44 material failed with an arXiv cache miss; this is an access failure, not visual verification.

Later author source: Aldous--Janson, *The Critical Beta-splitting Random Tree III: The exchangeable partition representation and the fringe tree*, arXiv:2412.09655. Its Theorem 5.1 gives the explicit reverse-HD construction of the fringe tree, and §5.3 states that a size-`i` clade in the fringe has the `DTCS(i)` distribution and that branches are randomly positioned left/right.

Brandenberger--Chin--Mossel, *Asymptotics for the harmonic descent chain and applications to critical beta-splitting trees*, arXiv:2505.24821, Corollary 1.3, proves CLTs for the **finite** `DTCS(n)` number of size-`k` clades and of any fixed clade shape. This is useful nearby progress, but it does not prove Open Problem 12 or the required stationary fringe-shift density law below.

Chorbadzhiyska--Minchev--Savov, *Asymptotics for Beta-Splitting Trees via Homogeneous Fragmentations and Meromorphic Potential Theory*, arXiv:2608.18320 (18 August 2026), proves new height/fragmentation asymptotics and resolves a different Aldous--Janson open problem at the critical parameter. I found no statement there settling the exact fringe-to-finite CLT transfer question.

The bounded 2026-09-19 search found no checked later primary paper explicitly resolving Open Problem 12. This is only bounded negative evidence and is **not** a worldwide openness or novelty certificate.

## 3. Frozen witness and metric

The canonical claim freezes one functional

\[
\Theta=\Psi+\Phi.
\]

The historical perturbation `Phi` is the bounded continuous root-split functional from
`probability_campaign_2026_09/codex_20h_20260906/proofs/P0342_beta_tree_fringe_transfer_scope_counterexample.md`.
For a finite tree with `n>=9`, write `R_n` for the smaller original root-clade size, `r_n=floor(sqrt(n))`,

\[
B_n=\mathbf 1_{\{R_n\le r_n\}},\qquad p_n=\mathbb P(B_n=1),
\]

and

\[
\Phi(T)=n^{-1/4}(B_n(T)-p_n).
\]

On infinite fringe trees `Phi=0`.

The local mark `Psi` is `+1` when the distinguished leaf is the singleton **left** child in a size-3 clade, `-1` when it is the singleton **right** child, and `0` otherwise.

The metric is frozen:

`M_P0342 in {0,1,2}` = number of these two obligations proved for this same `Theta`:

1. `FRINGE`: a `sqrt(m)` Gaussian CLT with strictly positive limiting variance for the centered fringe sums;
2. `FINITE-FAILURE`: the centered finite `DTCS(n)` sums do not have that same CLT; non-tightness suffices.

The admission baseline was exactly `0/2`. No auxiliary lemma changes the denominator.

## 4. B3 — stronger finite-tree failure theorem

### Theorem 1 (the finite normalized `Theta` sums diverge in absolute value in probability)

Let

\[
Z_n:=\sum_{i=1}^n\Psi(T_i^{(n)}),\qquad
X_n:=\frac{Z_n}{\sqrt n},
\]

and let

\[
Y_n:=\frac1{\sqrt n}\sum_{i=1}^n\Phi(T_i^{(n)})
      =n^{1/4}(B_n-p_n).
\]

Then, with

\[
W_n:=\frac1{\sqrt n}\sum_{i=1}^n\Theta(T_i^{(n)})=X_n+Y_n,
\]

we have for every fixed `M<infinity`,

\[
\mathbb P(|W_n|\le M)\longrightarrow0.
\]

In particular `(W_n)` is not tight and cannot converge to any finite Gaussian law.

### Proof

Let `N_3(n)` be the number of size-3 clades in `DTCS(n)`. Two distinct clades of the same size are disjoint leaf intervals, so deterministically

\[
N_3(n)\le \lfloor n/3\rfloor.
\]

Each size-3 clade contributes exactly one nonzero `Psi` mark: `+1` if its root split is `1|2` and `-1` if it is `2|1`. Conditional on the sigma-field exposing which size-3 clades exist, but not their internal size-3 split, these signs are independent Rademacher variables. This follows directly from the recursive `DTCS` construction: distinct clades split independently, while

\[
q(3,1)=q(3,2)=1/2.
\]

Consequently

\[
\mathbb E[Z_n\mid N_3(n),\text{clade scaffold}]=0,
\qquad
\mathbb E[Z_n^2\mid N_3(n),\text{clade scaffold}]=N_3(n),
\]

and hence

\[
\mathbb E X_n=0,
\qquad
\mathbb E X_n^2=\frac{\mathbb E N_3(n)}n\le\frac13. \tag{1}
\]

Now use the exact critical root-split law

\[
q(n,i)=\frac{n}{2H_{n-1}}\frac1{i(n-i)}
      =\frac1{2H_{n-1}}\left(\frac1i+\frac1{n-i}\right).
\]

For all sufficiently large `n`, `r_n<n/2`, so the two events `i<=r_n` and `i>=n-r_n` are disjoint and symmetry gives

\[
p_n
=\frac{H_{r_n}+\sum_{i=1}^{r_n}(n-i)^{-1}}{H_{n-1}}. \tag{2}
\]

Since `r_n=floor(sqrt(n))`,

\[
\frac{H_{r_n}}{H_{n-1}}\to\frac12,
\]

while

\[
0\le \frac{\sum_{i=1}^{r_n}(n-i)^{-1}}{H_{n-1}}
\le \frac{r_n}{(n-r_n)H_{n-1}}\to0.
\]

Thus

\[
p_n\to\frac12. \tag{3}
\]

Therefore for all large `n`, both `p_n` and `1-p_n` are at least `1/3`. Since `B_n` is Bernoulli,

\[
|Y_n|=n^{1/4}|B_n-p_n|\ge \frac{n^{1/4}}3
\quad\text{almost surely}. \tag{4}
\]

No independence between `X_n` and `Y_n` is needed. If `|X_n+Y_n|<=M`, then by the reverse triangle inequality and (4),

\[
|X_n|\ge \frac{n^{1/4}}3-M.
\]

By (1) and Chebyshev,

\[
\mathbb P(|W_n|\le M)
\le
\mathbb P\left(|X_n|\ge \frac{n^{1/4}}3-M\right)
\le
\frac{1/3}{(n^{1/4}/3-M)^2}
\longrightarrow0.
\]

Finally, `E Z_n=0` and `E(B_n-p_n)=0`, so `W_n` is already the centered `sqrt(n)`-normalized finite sum. This proves the theorem. `square`

### Consequence for the frozen metric

This proves the exact `FINITE-FAILURE` obligation for the frozen `Theta`. It is stronger than the required non-tightness. Thus

\[
\boxed{M_{P0342}: 0/2\longrightarrow1/2.}
\]

This does **not** close or refute the source question yet because `FRINGE` still requires a strictly-positive-variance CLT for this same `Theta`.

## 5. B18 — rewrite the fringe problem as a signed point process

Let the stationary fringe leaves be indexed by `Z`. A size-3 clade occupies a consecutive interval of exactly three leaf labels. For `m>=3`, let `K_m` be the number of size-3 clades wholly contained in the block `{0,...,m-1}`.

### Lemma 2 (signed-clade decomposition)

There are signs `(epsilon_C)` and a boundary term `R_m` such that

\[
\sum_{i=0}^{m-1}\Psi(T_i)
=
\sum_{C\subseteq\{0,\ldots,m-1\}\atop |C|=3}\epsilon_C+R_m, \tag{5}
\]

where conditional on the unoriented size-3-clade scaffold the complete-clade signs are iid Rademacher and

\[
|R_m|\le2. \tag{6}
\]

### Proof

Every complete size-3 clade contributes exactly one singleton orientation mark, hence one sign. Distinct size-3 clades are disjoint intervals. The ordered `DTCS` construction makes the internal `1|2` versus `2|1` split of each such clade an independent `q(3,.)` draw, and `q(3,1)=q(3,2)=1/2`. This finite-dimensional statement passes to the local weak fringe limit.

A size-3 interval that is not wholly inside the block can contribute to the block only by crossing one of the two endpoints. Because size-3 clades are pairwise disjoint, at most one such clade crosses each endpoint. Each crossing clade contributes at most one mark of magnitude one, proving (6). `square`

Thus the positive-variance fringe CLT is no longer a general dependent-tree question for this `Psi`: it is a random-sum CLT whose only macroscopic random parameter is the density `K_m/m`.

## 6. B30 — solve the local scale and identify the exact remaining glue

The source occupation formula is

\[
a(m)=\frac{6H_{m-1}}{\pi^2(m-1)},\qquad m\ge2.
\]

Hence

\[
a(3)=\frac9{2\pi^2}. \tag{7}
\]

Let `L_j` indicate that `j` is the left endpoint of a size-3 clade in the stationary fringe process. Let `M_i` indicate that leaf `i` lies in a size-3 clade. Since every such clade contains exactly three leaves,

\[
M_i=L_i+L_{i-1}+L_{i-2}.
\]

By stationarity and by the interpretation of `a(3)` as the probability a typical leaf belongs to a size-3 clade,

\[
\mathbb E L_0=\frac{a(3)}3
=:\lambda_3
=\frac3{2\pi^2}>0. \tag{8}
\]

Moreover

\[
K_m=\sum_{j=0}^{m-3}L_j,
\qquad
\mathbb E K_m=(m-2)\lambda_3, \tag{9}
\]

so `E[K_m/m] -> lambda_3` without any ergodicity assumption.

### Theorem 3 (exact density/CLT equivalence for the frozen local mark)

For the stationary fringe process, the following are equivalent:

(a) the density law

\[
\frac{K_m}{m}\xrightarrow{p}\lambda_3=\frac3{2\pi^2}; \tag{10}
\]

(b) the local-mark CLT

\[
\frac1{\sqrt m}\sum_{i=0}^{m-1}\Psi(T_i)
\xrightarrow{d}
N\!\left(0,\frac3{2\pi^2}\right). \tag{11}
\]

More generally, if the left side of (11) converges to any centered Gaussian `N(0,sigma^2)`, then necessarily `sigma^2=lambda_3` and (10) holds.

### Proof: (a) implies (b)

Let `Q_m` be the complete-clade sum in (5). Conditional on the size-3 scaffold,

\[
\mathbb E\left[e^{itQ_m/\sqrt m}\mid\text{scaffold}\right]
=\cos(t/\sqrt m)^{K_m}. \tag{12}
\]

Uniformly for `0<=K_m<=m/3`,

\[
K_m\log\cos(t/\sqrt m)
=-\frac{t^2}{2}\frac{K_m}{m}+O_t(m^{-1}). \tag{13}
\]

Under (10), the conditional characteristic function in (12) therefore converges in probability to the deterministic limit

\[
\exp(-\lambda_3t^2/2).
\]

It is bounded by one, so its expectation has the same limit. Levy's theorem gives

\[
Q_m/\sqrt m\Rightarrow N(0,\lambda_3).
\]

By (6), `R_m/sqrt(m)->0` deterministically, and Slutsky gives (11).

### Proof: Gaussian limit implies (a)

Suppose the left side of (11) converges instead to `N(0,sigma^2)`. Again (6) shows the same is true for `Q_m/sqrt(m)`.

Because `0<=K_m/m<=1/3`, from every subsequence we may choose a further subsequence along which

\[
K_m/m\Rightarrow L
\]

for some random `L` supported on `[0,1/3]`. The approximation (13) is uniform on that compact interval, hence along this subsubsequence

\[
\mathbb E e^{itQ_m/\sqrt m}
=\mathbb E\big[\cos(t/\sqrt m)^{K_m}\big]
\longrightarrow
\mathbb E e^{-t^2L/2}. \tag{14}
\]

The assumed Gaussian limit makes the same characteristic functions converge to `exp(-sigma^2 t^2/2)`. Therefore

\[
\mathbb E e^{-sL}=e^{-s\sigma^2}\qquad(s\ge0).
\]

Uniqueness of Laplace transforms gives `L=sigma^2` almost surely. Thus every subsequential weak limit of `K_m/m` is the same constant and hence `K_m/m -> sigma^2` in probability. Since the variables are uniformly bounded, expectations converge; (9) forces

\[
\sigma^2=\lambda_3=\frac3{2\pi^2}.
\]

This proves (10) and the theorem. `square`

### Exact remaining obstruction

Because `Phi` vanishes identically on the infinite fringe tree, the fringe sums of `Theta=Psi+Phi` are exactly the fringe sums of `Psi`. Therefore the entire frozen `FRINGE` obligation is reduced to the single source-faithful statement

\[
\boxed{\displaystyle K_m/m\xrightarrow{p}3/(2\pi^2).} \tag{15}
\]

A sufficient route is a complete proof that the fringe shift is ergodic and application of Birkhoff to `L_0`; another is a direct estimate `Var(K_m)=o(m^2)`. The overview's sentence that one "could show" ergodicity is not enough by itself. I did not prove (15) in this run and therefore do not count `FRINGE`.

The nearest solved analogue is Aldous's 1991 extremal-fringe machinery: it gives empirical fringe convergence under an extremality hypothesis and a shift-coupling criterion for certain invariant sin-trees. The missing task is to map the critical beta-splitting reverse-HD fringe construction to those hypotheses without an unproved step. This is the next mathematically decisive direction, not another finite enumeration.

## 7. Exact self-check retained and read back

No new checker was manufactured after the idea. I reused the substantive exact self-check already created during the orphaned P0342 work:

`proofnet24/P13-outside-successor/artifacts/2026-09-19T09-21-28Z__p0342_positive_variance_check.py`

at commit `d9be5f4ea929f3070376777c0dafe7b706a38c5e`, read back at that exact commit.

Its archived output

`proofnet24/P13-outside-successor/artifacts/2026-09-19T09-21-28Z__p0342_positive_variance_check.txt`

was created at commit `ca24ad34c873a5c5bf97f2b925fbd3cb119696b4` and read back at that exact commit. It records:

- `ORDERED_FULL_BINARY_TREES_CHECKED=2056`;
- `LEAF_BLOCKS_CHECKED=84648`;
- `EXACT_ASSERTIONS=176350`;
- exact verification of the size-3 interval structure through 9 leaves;
- exact verification of the root-split formula through `n=200`;
- exact rational coefficients `a(3)=9/(2*pi^2)` and `lambda_3=3/(2*pi^2)`;
- terminal line `ALL_EXACT_P0342_POSITIVE_VARIANCE_CHECKS_PASS`.

This is explicitly a **P13 self-check**, not an independent audit. The proof of Theorem 1 above is analytic and does not infer eventual behavior merely from the bounded enumeration.

The new-method idea was written before this report at

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T10-04-09Z__p0342_b3_b18_b30_idea.md`,

created at commit `1cdb6a08df83d0563b1c4097be917842f93dce58` and read back at that exact commit.

## 8. Status, movement, and next step

`M_P0342` moved **0/2 -> 1/2**. This resets the successor unchanged-run streak to `0`.

Status remains **CLAIMED / PARTIAL / SOURCE-CURRENT-LOOKING**. I do not claim source refutation, source closure, novelty, independent audit, or worldwide openness. The finite half of the frozen positive-variance counterexample is now proved; the fringe half is exactly (15).

The next run must use a nonrepeating method triple and should attack (15), preferably by checking the hypotheses of Aldous (1991) Proposition 12 / Theorem 13 against the reverse harmonic-descent fringe construction, or by deriving a direct subquadratic variance bound for `K_m`. No scheduler, peer claim, shared root ledger, historical report, email/Drive resource, workflow, permission, or public post was modified.

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  claim_id: P0342
  lane: CLOSABLE_OUTSIDE
  source: "Aldous--Janson arXiv:2303.02529v3 Open Problem 12 sec.4.10"
  metric_name: M_P0342
  metric_denominator: 2
  before: 0
  after: 1
  movement: true
  obligation_added: FINITE-FAILURE
  obligation_remaining: FRINGE
  exact_residual: "K_m/m -> 3/(2*pi^2) in probability for size-3 clades in the stationary fringe process"
  unchanged_run_streak: 0
  methods: [B3, B18, B30]
  self_check_only: true
  closure: false
  status: PARTIAL
```

Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED (GPT-6 / maximum was requested, but this scheduler exposes no model selector or reasoning-effort selector; I do not claim otherwise).

Problem: Takahiro Hasebe and Yuki Ueda (2018), *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240 / ALEA 15 (2018), Conjecture 5.5; intake I0084.

Tracked quantity MOVED: **UNMEASURED -> 1/2** of the frozen positive half-stable source cases decided. The classical positive alpha=1/2 universal assertion is resolved **NEGATIVELY** by an explicit initial law with every polynomial moment finite; the free positive alpha=1/2 case remains OPEN. Overall fleet status: **PARTIAL / source-level refutation candidate proved internally; closure withheld pending the protocol's two independent audits and prior-art clearance.**

# 1. Repository continuity and assignment handoff

I resumed from current `master`, reading the required fleet/campaign state including root `README.md`, `proofnet24/HOURLY20_PROTOCOL_2026-09-16.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`, the exact I0084 intake row, the historical P0178 attempt, and the newest neighboring R18 package.

Root `RESULTS.md` assigns R19 to Hasebe--Ueda Conjecture 5.5 / I0084 with fixed metric “complete classical/free alpha=1/2 source cases covered,” baseline `UNMEASURED`, and explicitly retires the old free-group-factor route.

The previous R19 free-group-factor work is preserved, not overwritten. Its latest handoff is

`proofnet24/R19-free-group-factors/runs/2026-09-16/2026-09-16_13-04-33_UTC__R19__free-shift-tor-obstruction__report.md`

(blob `fe7b21cc2d90523d98d434c239c290d157fee948`). It leaves the separable free-group-factor problem OPEN with a Tor/completion obstruction and free-shift crossed-product route. No file in that old track was modified here.

The historical I0084/P0178 campaign attempt was recovered from `probability_1000_intake_claude_20260907/raw/rank_sheet_2026-09-07.txt` and the campaign catalog. It established only that the source's own separated-right-tail atom mechanism cannot have `w_k |a_k|^(2+alpha)` diverging while the critical moment is finite. Its own obstruction said this does not provide a uniform derivative estimate for arbitrary initial laws. The counterexample below uses a different mechanism: a **left sparse tail plus one-sided support shielding**.

The neighboring R18 report `runs/R18/2026-09-16_13-34-00_UTC__R18__i0080-explicit-smalltime.md` was read. It concerns distinct Hasebe--Ueda--Wang Problem 4.11 and is not imported as evidence for I0084.

The directed audit target R20 has no current `runs/R20/` package on `master`; repository search and directory listing found no package ready for an end-to-end audit. Therefore `R20_AUDIT=NOT_READY`; no stale/wrong-target work was audited.

# 2. Exact source statement, conventions, skewness scope

The authoritative published version is ALEA 15 (2018), 353--374, DOI `10.30757/ALEA.v15-15`. The published Conjecture 5.5 uses **two laws and two convolutions**:

- `S_t`: law at time `t` of a classical strictly alpha-stable process; conclusion concerns `mu * S_t`;
- `T_t`: law at time `t` of a free strictly alpha-stable process; conclusion concerns `mu boxplus T_t`.

The archived/current preprint extraction can collapse this notation and therefore must not be silently substituted for the journal statement.

The source imposes `alpha in (0,2)` and

`integral |x|^(2+alpha) dmu(x) < infinity`,

and then conjectures eventual unimodality for the corresponding classical/free evolution. There is **no symmetry restriction in Conjecture 5.5**. Thus the extreme-skewness one-sided positive alpha=1/2 classical stable process is source-admissible; indeed Section 5.2 of the same paper treats it explicitly.

For the classical positive half-stable process the source writes

\[
L_t(dx)=\frac{t}{\sqrt{2\pi}}
       e^{-t^2/(2x)}x^{-3/2}\mathbf 1_{(0,\infty)}(x)\,dx,
\qquad t\ge0.
\tag{2.1}
\]

Theorem 5.3 proves eventual unimodality for compactly supported initial laws. Proposition 5.4 constructs a law for which `mu * L_t` is nonunimodal for every `t>0`, but that law has finite moments only below `5/2`. Immediately before Conjecture 5.5 the authors explain why their particular atom mechanism necessarily loses the `5/2` moment and conjecture the critical moment should restore eventual unimodality.

The frozen R19 metric is narrower than all of Conjecture 5.5: it counts the two **positive alpha=1/2 classical/free source cases**. A result at alpha=1/2 would remain PARTIAL as an all-alpha positive theorem. Conversely, one admissible counterexample already falsifies the universal source conjecture mathematically, although fleet closure still requires independent audits.

# 3. Dated status / novelty search

Dated 2026-09-16 bounded searches were run for:

- exact title and arXiv `1710.08240`;
- `Conjecture 5.5`, stable process unimodality, finite `5/2` moment;
- Hasebe/Ueda later papers and author publication pages;
- positive/free stable distribution unimodality.

Recovered later related work includes Hasebe--Simon--Wang on free stable densities and later Hasebe/Ueda unimodality papers, but no source found in this bounded search claims the exact finite-`(2+alpha)` initial-law conjecture has been resolved. This is **not exhaustive novelty clearance**.

The ALEA/HUSCAP version-of-record metadata and text extraction were available. A requested PDF screenshot failed with a cache-miss in the web tool; that access failure is recorded rather than bypassed.

The posted sharp Brownian constant from Hasebe--Ueda Problem 3.3 is excluded and was not used.

# 4. Counterexample search: the one-sided shielding mechanism

The source's failed counterexample route places increasingly remote atoms on the side visible to the stable tail and requires the local atom to overwhelm earlier mass; at the critical moment this forces `w_k |a_k|^(5/2)` not to vanish.

For the positive one-sided kernel there is a different possibility. Put the sparse atoms farther and farther to the **left**. Near a far-left atom, every much larger mass lying to its right contributes exactly zero, because the positive stable density is supported on positive increments. Only the still farther-left tail competes. That tail can be superexponentially small while all polynomial moments remain finite.

This gives the following theorem.

# 5. R19-I0084-C001 — all-moment counterexample for the classical positive half-stable process

**STATUS: PROVED (self-check complete; independent audits pending).**

Define

\[
Z=\sum_{n\ge1}2^{-n^2},\qquad
w_n=Z^{-1}2^{-n^2},\qquad
a_n=-2^n,
\tag{5.1}
\]

and

\[
\boxed{\mu=\sum_{n\ge1}w_n\delta_{a_n}.}
\tag{5.2}
\]

Then:

1. `mu` has every finite absolute polynomial moment;
2. in particular `int |x|^(5/2) dmu(x)<infinity`;
3. for **every `t>0`**, `mu * L_t` is not unimodal.

Therefore the classical positive alpha=1/2 case of the source's universal Conjecture 5.5 is false.

## 5.1 Every polynomial moment is finite

For every fixed `p>0`,

\[
\int |x|^p\,d\mu(x)
=Z^{-1}\sum_{n\ge1}2^{-n^2+pn}.
\tag{5.3}
\]

If `n>=2p`, then

\[
-n^2+pn\le -\frac{n^2}{2},
\]

so the series converges. For the source-critical exponent `p=5/2`, this inequality holds for every integer `n>=5` because

\[
-n^2+\frac52n\le-\frac12n^2
\iff n(n-5)\ge0.
\tag{5.4}
\]

Thus the example is substantially stronger than merely having finite `5/2` moment.

## 5.2 Kernel and derivative

Fix arbitrary `t>0` and put

\[
s=t^2.
\]

The harmless positive factor `t/sqrt(2 pi)` does not affect modes, so write

\[
K_s(r)=
\begin{cases}
r^{-3/2}e^{-s/(2r)},&r>0,\\
0,&r\le0.
\end{cases}
\tag{5.5}
\]

Because the exponential is flat at the origin, this extension is smooth at `r=0`. A density of `mu*L_t`, up to the global positive constant, is

\[
F_t(x)=\sum_{n\ge1}w_n K_s(x-a_n).
\tag{5.6}
\]

For `r>0`,

\[
K_s'(r)
=\frac{s-3r}{2r^{7/2}}e^{-s/(2r)}
=s^{-5/2}H(r/s),
\tag{5.7}
\]

where

\[
H(u)=\frac{1-3u}{2u^{7/2}}e^{-1/(2u)},\qquad u>0.
\tag{5.8}
\]

The derivative is globally bounded. Indeed

\[
|H(u)|
\le\frac12u^{-7/2}e^{-1/(2u)}
+\frac32u^{-5/2}e^{-1/(2u)}.
\tag{5.9}
\]

For `p>0`, substitution `v=1/(2u)` gives

\[
\sup_{u>0}u^{-p}e^{-1/(2u)}=(2p)^p e^{-p}.
\tag{5.10}
\]

Using `e>2`, and then increasing the fractional powers to the next integer powers,

\[
\sup |H|
<\frac12\left(\frac72\right)^{7/2}
 +\frac32\left(\frac52\right)^{5/2}
<\frac12\left(\frac72\right)^4
 +\frac32\left(\frac52\right)^3
=\frac{3151}{32}<99.
\tag{5.11}
\]

Thus

\[
|K_s'(r)|<99s^{-5/2}
\tag{5.12}
\]

for every real `r` (with derivative zero on the negative half-line and at zero). Since `sum w_n=1`, the derivative series is uniformly convergent by the Weierstrass M-test; termwise differentiation of (5.6) is justified.

Two exact derivative facts will be used:

\[
H(1/6)=54\sqrt6\,e^{-3}>4,
\tag{5.13}
\]

and

\[
H(u)<0\quad\text{for }u>1/3.
\tag{5.14}
\]

For (5.13), the elementary series estimate `e<3` and `sqrt(6)>2` give

\[
54\sqrt6 e^{-3}>108/27=4.
\]

(The inequality `e<3` follows, for example, from `k!>=2^{k-1}` for `k>=2`.)

## 5.3 Superexponentially small farther-left tail

For `k>=1`,

\[
\frac{w_{n+k}}{w_n}
=2^{-(2nk+k^2)}
\le 2^{-(2n+1)k}.
\tag{5.15}
\]

Hence, for every `n>=3`,

\[
\frac{\sum_{j>n}w_j}{w_n}
\le
\frac{2^{-(2n+1)}}{1-2^{-(2n+1)}}
\le\frac1{127}.
\tag{5.16}
\]

## 5.4 Three derivative signs at every time

Because `t>0` is arbitrary, choose `n>=3` so large that

\[
2^{n-1}>s=t^2.
\tag{5.17}
\]

Set

\[
x_0=a_n,
\qquad
x_+=a_n+\frac{s}{6},
\qquad
x_-=a_n+s.
\tag{5.18}
\]

The nearest atom to the right is `a_{n-1}`, at distance `2^{n-1}` from `a_n`; by (5.17), all three test points still lie strictly left of `a_{n-1}`. Therefore every atom `j<n` is to the right of the test points and contributes **exactly zero** to the density and its derivative. This is the one-sided shielding step.

For `j>n`, the nearest farther-left atom is `a_{n+1}`. At each of the three test points its positive distance is at least `2^n`, and

\[
2^n>2s>s/3.
\]

Thus every `j>n` derivative contribution is strictly negative by (5.14).

At `x_0=a_n`, the `n`th term has derivative `K_s'(0)=0`, while all `j>n` terms are negative. Therefore

\[
\boxed{F_t'(x_0)<0.}
\tag{5.19}
\]

At `x_+=a_n+s/6`, the `n`th term gives, by (5.13),

\[
w_n K_s'(s/6)
=w_n s^{-5/2}H(1/6)
>4w_ns^{-5/2}.
\tag{5.20}
\]

The entire farther-left tail has absolute derivative bounded using (5.12) and (5.16):

\[
\left|\sum_{j>n}w_jK_s'(x_+-a_j)\right|
<99s^{-5/2}\sum_{j>n}w_j
\le \frac{99}{127}w_ns^{-5/2}.
\tag{5.21}
\]

Therefore

\[
\boxed{
F_t'(x_+)
>
\left(4-\frac{99}{127}\right)w_ns^{-5/2}
=
\frac{409}{127}w_ns^{-5/2}
>0.
}
\tag{5.22}
\]

Finally, at `x_-=a_n+s`, the main `n`th term has `r=s>s/3`, so it is negative, and all farther-left terms are negative too. Thus

\[
\boxed{F_t'(x_-)<0.}
\tag{5.23}
\]

Since

\[
x_0<x_+<x_-,
\]

we have the strict sign pattern

\[
F_t'(x_0)<0<F_t'(x_+),
\qquad F_t'(x_-)<0.
\tag{5.24}
\]

## 5.5 Why the sign pattern disproves unimodality

The source's definition of a unimodal probability law is an atom at a possible mode plus an absolutely continuous density which is nondecreasing to the left of the mode and nonincreasing to the right. Here convolution with `L_t` is smooth and has no atom.

If a differentiable density were unimodal with some mode `m`, a negative derivative at `x_0` forces `x_0` not to lie on a nondecreasing left side unless the mode is already at or to its left; but then every later point, including `x_+>x_0`, lies on the nonincreasing side and cannot have positive derivative. Equivalently, the derivative of a differentiable unimodal density cannot change from strictly negative to strictly positive as `x` increases.

The pattern (5.24) is therefore impossible for a unimodal density.

Since `t>0` was arbitrary,

\[
\boxed{
\mu*L_t\text{ is nonunimodal for every }t>0.
}
\tag{5.25}
\]

This completes the proof of R19-I0084-C001.

# 6. Why this escapes the source's 5/2-moment obstruction

The source's Proposition 5.4 arranges atoms so that a remote atom must dominate density contributed by substantial previously placed mass; their sufficient condition requires `w_k b_k^(5/2)` to become large, which is incompatible with a finite `5/2` moment.

The present construction reverses the geometry. Near the far-left atom `a_n=-2^n`, all heavier atoms `j<n` lie to the **right** and are completely invisible because the positive stable kernel has support only on positive increments. The only competition is the farther-left tail `j>n`, whose relative mass is at most `1/127`. Therefore the local bump survives even though

\[
w_n|a_n|^p=Z^{-1}2^{-n^2+pn}\to0
\]

for every fixed `p`.

So the old P0178 obstruction was real but mechanism-specific; it does not constrain one-sided shielding.

# 7. Parameter scope and fixed metric

The exact frozen two-case metric now reads:

| positive alpha=1/2 source case | universal eventual-unimodality assertion for all finite-5/2 initial laws | this run |
|---|---|---|
| classical `mu * L_t` | false | **RESOLVED NEGATIVELY** by C001 |
| free `mu boxplus T_t` for the positive free half-stable evolution | unknown | **OPEN** |

Thus the metric is

\[
\boxed{1/2.}
\]

The proof says nothing yet about the free positive half-stable case. It also does not classify other skewness parameters or all `alpha`. The source Conjecture 5.5 is nevertheless universally quantified broadly enough that the classical positive half-stable counterexample, if independently confirmed, is already a source-level refutation.

Fleet closure is deliberately **not** claimed: the protocol requires two OTHER-task audits plus prior-art clearance and a closure package. This run supplies a complete proof and exact finite checker but only a self-check.

# 8. Exact checker / self-check

Run-specific source:

`artifacts/R19/2026-09-16_13-40-24_UTC__I0084_halfstable_lefttail_counterexample_checker.py`

Executed output:

`artifacts/R19/2026-09-16_13-40-24_UTC__I0084_halfstable_lefttail_counterexample_executed_output.txt`

The exact arithmetic checker verifies:

- `3151/32 < 99` in the global derivative envelope;
- the exact tail ratio `1/127`;
- the positive derivative margin
  \[
  4-99/127=409/127>0;
  \]
- the critical `5/2` moment tail comparison for every integer `n>=5`;
- representative all-polynomial-moment comparisons;
- the elementary factorial core used for `e<3`.

The checker is a **self-check**, not an independent audit. The infinite-series differentiation, mode argument, and source matching are proved on the page.

An earlier archive file with a slightly differently formatted checker transcript was written before the exact executed transcript filename; it is not used as the canonical receipt. The canonical output is the `_executed_output.txt` file above.

# 9. Independent-audit state

- `P26_AUDIT=NOT_YET_REQUESTED_OR_AVAILABLE` for this new claim.
- Directed R-series second audit would come from R20, but `R20_AUDIT=NOT_READY`: no current `runs/R20/` package exists to audit, and this run did not fabricate or substitute an audit.

Closure status therefore remains **PARTIAL / audit pending**, notwithstanding the complete internal proof.

# 10. Failed routes / corrected understanding

1. **Source-type sparse right-tail mechanism.** Historical P0178 correctly found that finite critical moment kills the condition `w_k |a_k|^(2+alpha)` becoming large. This does not prove eventual unimodality.

2. **Trying to prove a uniform derivative estimate first.** For the positive half-stable kernel, one-sided support means no such proof can hold for arbitrary finite-5/2 initial laws: C001 supplies an explicit obstruction.

3. **Symmetric intuition.** The conjecture has no symmetry hypothesis. The positive alpha=1/2 process is maximally skewed and source-admissible, so a proof strategy that quietly assumes two-sided smoothing is invalid for the source's full scope.

4. **Brownian posted constants.** Problem 3.3 is excluded by `POSTED.md` and was not used.

# 11. Next attack

The frozen metric has moved to `1/2`. The remaining half-stable case is the **positive free alpha=1/2 evolution**.

The next run should first try to refute that free case using the same sparse-left-tail law. The key question is whether free additive convolution with the positive free half-stable law has an analogue of the classical one-sided shielding strong enough to preserve isolated far-left bumps, or whether subordination destroys exact support shielding. The attack should recover the explicit Cauchy/R-transform/subordination description of the positive free stable law and test the same superexponentially weighted atoms before attempting a proof of eventual unimodality.

If the classical C001 receives independent audits, the overall source Conjecture 5.5 can be marked REFUTED even if the free half-stable metric remains 1/2; those are logically different bookkeeping statements.

# 12. ledger_delta

```yaml
ledger_delta:
  track: R19
  source: "Takahiro Hasebe and Yuki Ueda, 2018, arXiv:1710.08240 / ALEA 15, Conjecture 5.5; intake I0084"
  target: "Stable eventual unimodality under the exact finite (2+alpha)-moment hypothesis; frozen first target = positive alpha=1/2 classical/free source cases"
  metric: "number of the two positive classical/free alpha=1/2 source universal cases decided"
  before: "UNMEASURED"
  after: "1/2"
  status: "PARTIAL; classical half-stable universal case resolved negatively internally; source-level REFUTED candidate pending audits; free half-stable case OPEN"
  unchanged_count: 0
  exact_evidence:
    - "R19-I0084-C001 full proof in this immutable report"
    - "artifacts/R19/2026-09-16_13-40-24_UTC__I0084_halfstable_lefttail_counterexample_checker.py"
    - "artifacts/R19/2026-09-16_13-40-24_UTC__I0084_halfstable_lefttail_counterexample_executed_output.txt"
  audit_ids:
    p26: "NOT_AVAILABLE"
    second_other_track: "R20 NOT_READY"
  old_assignment_handoff: "proofnet24/R19-free-group-factors/runs/2026-09-16/2026-09-16_13-04-33_UTC__R19__free-shift-tor-obstruction__report.md"
```

# 13. Primary references

- T. Hasebe and Y. Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, ALEA 15 (2018), 353--374, DOI `10.30757/ALEA.v15-15`, arXiv:1710.08240.
- T. Hasebe, T. Simon and M. Wang, *Some properties of the free stable distributions*, IMRN (2019), arXiv:1805.01133, for later free-stable density structure; no resolution of Conjecture 5.5 found in the bounded search.
- T. Hasebe and N. Sakuma, work on unimodality of free Levy processes, for related but distinct symmetric/eventual-unimodality results.

**No closure claim.**

Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this run is not authenticated GPT-6 maximum. **METRIC MOVED:** the certified five-column real-Boolean Komlos upper bound improves from `sqrt(2)+1/2 = 1.914213...` to `19/10 = 1.9`, and the propagated finite envelope strictly improves in 30 dimensions. Methods actually used: **#15 BREAK THE SYMMETRY ON PURPOSE, #28 REPLACE FOR ALL WITH FOR TYPICAL, #29 ADD THE POINTS AT INFINITY.**

# R13 — completing the orphan exact `K_5^* <= 19/10` certificate

Run ID: `20260917T1945Z_k5-upper-19over10-complete-9c4e`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and source scope

R13 remains the HARD OUTSIDE real Boolean Komlos track. For a real `m x n` matrix `A` whose columns have Euclidean norm at most one, write

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty,
\qquad
K_n^*=\sup_A\operatorname{disc}(A).
\]

The fixed tracked quantity remains the complete rigorously certified upper envelope `B_R13(n)`. Complex phases, rank-two/vector colorings and average-case estimates do not count as solutions of this Boolean target.

Before research I reread/recovered the current campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the new-methods deployment state, the current E0042/Komlos repository navigation, the newest complete R13 report, and the current neighboring sign-matrix discrepancy admission/retirement state. I did not edit shared roots or peer files.

The newest complete R13 report before this run is

`runs/R13/20260917T1903Z_n6-rational-obstruction-3b7e.md`.

It moved the explicit finite lower obstruction to

\[
K_6^*\ge \frac{36907093}{20000000}=1.84535465,
\]

but correctly left the fixed **upper** envelope unchanged.

During continuity review I found two immediately preceding R13 artifacts that had been created and executed but never promoted into a complete immutable theorem report:

- `artifacts/R13/20260917T1835Z_k5-upper-19over10-b4e7_checker.py`, creation commit `46aca9993a9530d806f59d5a2d0656592f1c232c`;
- `artifacts/R13/20260917T1835Z_k5-upper-19over10-b4e7_output.txt`, archived-output commit `96dca918437c7b792d087478ed2860a3b751c37e`.

The output ends `R13_K5_19_10_EXACT_PASS`. The missing obligation was not another enumeration; it was to audit the logical coverage of all possible active witness-row counts and write the theorem-sized proof on the page. That is what this run does.

## 2. Fresh literature/source check, 17 September 2026

The checked current source picture is unchanged in the way relevant to this finite result.

1. Bansal--Jiang, arXiv:2508.03961, give the preceding full real-Boolean `\widetilde O((\log n)^{1/4})` advance.
2. Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 September 2026, state the unrestricted real-Boolean dimension-free theorem with constant `3 sqrt(2 pi)`. A bounded fresh search found the current v1 surface and no correction or withdrawal.
3. Guillen--Kobzar, arXiv:2609.15071, is unit-complex/rank-two discrepancy, not Boolean signing.
4. The Belhaouari--AlQudah 2019/2024 line advertises the five-dimensional value `(4+sqrt(142))/9`; R13 has already produced an exact admissible five-column matrix above that number, so that advertised equality is not used.
5. Targeted searches for `Komlos K(5) 19/10`, `five vectors 19/10 discrepancy`, and the exact constant did not locate a matching finite-five upper theorem. This is only a bounded negative search; novelty remains **UNVERIFIED**.

## 3. Method #15 — break the symmetry by active witness-row count

The key correction is to stop treating every bad cover as one combinatorial species.

Assume for contradiction that an admissible five-column matrix satisfies

\[
\operatorname{disc}(A)>T,\qquad T=\frac{19}{10}.
\]

Scale every row `a_alpha` by `T`:

\[
r_\alpha=\frac{a_\alpha}{T}.
\]

Let

\[
c=T^{-2}=\frac{100}{361}.
\]

For every projective sign class

\[
S_5=\{s\in\{\pm1\}^5:s_1=1\},\qquad |S_5|=16,
\]

some row has `|r_alpha dot s|>1`. Assign every class to one witnessing row, orient that class so its dot product with the row is positive, and delete rows assigned no class. Let `q` be the number of active witness rows. The column-energy bounds are

\[
E_j:=\sum_\alpha r_{\alpha j}^2\le c,
\qquad
\sum_jE_j\le5c=\frac{500}{361}.
\tag{3.1}
\]

The proof now separates `q<=3`, `q=4`, and `q>=5`. This is the missing global logical coverage.

## 4. The low-row case `q<=3`: an elementary partial-rounding lemma

### Lemma
For vectors `v_1,...,v_n` in the Euclidean unit ball of `R^m`, there are Boolean signs such that

\[
\left\|\sum_i\varepsilon_i v_i\right\|_2\le\sqrt m.
\]

### Proof
Consider

\[
P=\{x\in[-1,1]^n:\sum_i x_i v_i=0\}.
\]

It contains `0`; take an extreme point `x`. At most `rank(v_1,...,v_n)<=m` coordinates of `x` are strictly between `-1` and `1`, since otherwise a nonzero kernel perturbation supported on the fractional coordinates would contradict extremality.

Keep the integral coordinates and independently round every fractional coordinate to `+1/-1` with expectation `x_i`. If

\[
Z=\sum_i(\varepsilon_i-x_i)v_i,
\]

then `E Z=0` and independence gives

\[
\mathbb E\|Z\|_2^2
=\sum_{i\ \mathrm{fractional}}\operatorname{Var}(\varepsilon_i)\|v_i\|_2^2
\le m.
\]

Hence some rounding satisfies `||Z||_2<=sqrt(m)`. Since the original fractional combination sums to zero, this `Z` is the signed sum. QED.

If the bad five-column cover above had `q<=3`, the corresponding `q x 5` submatrix would therefore admit signs with

\[
\|A\varepsilon\|_\infty\le\|A\varepsilon\|_2\le\sqrt3<\frac{19}{10},
\]

contradicting badness. Thus `q>=4`.

## 5. The many-row case `q>=5`: exact total-energy exclusion

For an active row assigned `k` oriented projective classes `t_1,...,t_k`, put

\[
v=\sum_{i=1}^k t_i.
\]

Since the row witnesses every assigned class with value `>1`,

\[
r\cdot v>k.
\]

Let

\[
M_k=\max\left\|\sum_{i=1}^k t_i\right\|_2^2
\]

over `k` distinct projective five-cube classes with independent orientations. The exact table retained from R13-C33 is

\[
(M_1,\ldots,M_{16})=
(5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256).
\]

Cauchy gives

\[
\|r\|_2^2>\frac{k^2}{M_k}.
\tag{5.1}
\]

The exact dynamic program in the existing checker minimizes the sum of the right side of (5.1) over positive block sizes summing to 16 and over every row count `q>=5`. It gives

\[
\min_{q\ge5}\sum_{i=1}^q\frac{k_i^2}{M_{k_i}}
=\frac{89}{60}.
\]

But

\[
\frac{89}{60}>\frac{500}{361}=5c,
\]

contradicting (3.1). Therefore a bad matrix can have neither `q<=3` nor `q>=5`; only `q=4` remains.

## 6. The four-row case: exact diagonal-dual exhaustion

Let the four assigned blocks be `B_1,...,B_4`, with sizes `k_i`, and let

\[
v_i=\sum_{s\in B_i}t_s.
\]

For a positive diagonal weight

\[
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_5),
\qquad\sum_j\lambda_j=1,
\]

weighted Cauchy gives

\[
r_i^T\Lambda r_i
>
\frac{k_i^2}{v_i^T\Lambda^{-1}v_i}.
\tag{6.1}
\]

On the other hand, from the column-energy cap,

\[
\sum_i r_i^T\Lambda r_i
=\sum_j\lambda_jE_j\le c.
\tag{6.2}
\]

So it is enough, for every possible oriented four-block witness configuration, to find one positive diagonal `Lambda` with

\[
\sum_{i=1}^4
\frac{k_i^2}{v_i^T\Lambda^{-1}v_i}>c=\frac{100}{361}.
\tag{6.3}
\]

The exact checker does precisely this.

First it uses the total-energy inequalities to reduce to exactly ten sorted block-size profiles:

\[
\begin{gathered}
(1,1,6,8),(1,1,7,7),(1,2,5,8),(1,3,4,8),(1,4,4,7),\\
(2,2,4,8),(2,3,3,8),(2,3,4,7),(2,4,4,6),(4,4,4,4).
\end{gathered}
\]

It then enumerates **12,670** genuine oriented four-row witness configurations covering all 16 projective classes. For each, it checks one of the **126** positive rational diagonal weights

\[
\lambda_j=\frac{a_j}{10},\qquad a_j\in\mathbb Z_{>0},\quad\sum_ja_j=10.
\]

Every acceptance comparison is exact `Fraction` arithmetic. The smallest selected exact certificate over all 12,670 configurations is

\[
\frac7{24}.
\]

Since

\[
\frac7{24}-\frac{100}{361}
=\frac{127}{8664}>0,
\]

(6.3) holds in every case. Equations (6.1)--(6.2) contradict each other. Therefore the assumed bad five-column matrix does not exist.

We have proved

\[
\boxed{K_5^*\le\frac{19}{10}.}
\tag{R13-C37}
\]

This theorem is arbitrary ambient row dimension, real entries, Euclidean column norm at most one, and Boolean signs. No complex/vector relaxation is used.

## 7. Exact finite evidence already executed

The finite core is the already executed artifact

`artifacts/R13/20260917T1835Z_k5-upper-19over10-b4e7_checker.py`

at creation commit

`46aca9993a9530d806f59d5a2d0656592f1c232c`,

with archived output

`artifacts/R13/20260917T1835Z_k5-upper-19over10-b4e7_output.txt`

at commit

`96dca918437c7b792d087478ed2860a3b751c37e`.

The output records:

- `min_ge5_total_energy = 89/60`;
- `scaled_total_energy_cap = 500/361`;
- `oriented_four_row_configurations = 12670`;
- `diagonal_weight_grid = 126`, denominator 10;
- `smallest_selected_exact_certificate = 7/24`;
- `smallest_certificate_minus_target = 127/8664`;
- termination `R13_K5_19_10_EXACT_PASS`.

The checker itself re-enumerates `M_1,...,M_8`, uses the previously certified C33 values for `M_9,...,M_16`, performs the exact row-count DP, enumerates every surviving four-row configuration, and makes every acceptance decision in rational arithmetic. Floating point only nominates which rational weight to test first, with a full exact fallback if necessary.

These are self-checks, not independent outside audits.

## 8. Propagation to the complete finite envelope

The already-proved equal-block composition theorem says that from any certified `b_5` one obtains

\[
B_{R13}(n)\le b_5\sqrt{\left\lceil\frac n5\right\rceil}.
\]

With `b_5=19/10`, combine this with the balanced four-block theorem and the Guo--Fang--Lu universal certificate. The retained envelope is now

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\left\{\sqrt{3n/4},\frac{19}{10}\sqrt{\lceil n/5\rceil}\right\},&5\le n\le75,\\
3\sqrt{2\pi},&n\ge76,
\end{cases}}
\]

where the equality sign defines the **chosen certified upper envelope**, not the unknown optimal finite-`n` constants.

Relative to the immediately preceding envelope, the new five-block term strictly improves exactly 30 dimensions:

\[
\boxed{
5,10,15,20,25,29,30,34,35,39,40,44,45,49,50,
53,54,55,58,59,60,63,64,65,68,69,70,73,74,75.
}
\]

The crossover to the universal theorem remains `n=76`: using `pi<22/7`,

\[
18\pi<\frac{396}{7}<57=\frac{3\cdot76}{4}<\frac{361}{100}\cdot16.
\]

Thus the fixed upper metric genuinely moves this run and its unchanged/stuck count resets to zero.

The current finite-five interval recorded by R13 is therefore

\[
1.79244719148\ldots\le K_5^*\le1.9,
\]

where the lower endpoint is the exact five-column obstruction from the earlier R13 run. Separately, the best explicit R13 small-`n` lower obstruction is currently the six-column rational value `1.84535465`; these are lower-bound diagnostics and do not redefine the fixed upper metric.

## 9. The three new-method moves and what happened

### #15 BREAK THE SYMMETRY ON PURPOSE — succeeded

Breaking by active witness-row count (`q<=3`, `q=4`, `q>=5`) is exactly what closes the logical gap left by the orphan checker. The low-row regime is handled geometrically, the four-row regime by finite diagonal duality, and the many-row regime by total-energy counting. No single technique had to do all three jobs.

### #28 REPLACE FOR ALL WITH FOR TYPICAL — diagnostic only

I used the finite witness atlas to ask what the hard configurations look like before insisting on the universal statement. The worst certified cell in the denominator-10 atlas lies in the balanced profile `(4,4,4,4)`, not in the very unbalanced profiles. That observation suggested the active-row split and helped avoid another generic Komlos lemma. It is not itself a proof: the theorem still uses the full exact `for all 12,670 configurations` exhaustion.

### #29 ADD THE POINTS AT INFINITY — no quantitative gain, but no hidden boundary case

The diagonal-dual parameter lives in the open simplex `lambda_j>0`, and one natural concern is whether difficult configurations escape toward a boundary `lambda_j->0`. For the present `19/10` target that issue is unnecessary: every one of the 12,670 cells already has a strictly positive rational interior certificate with denominator 10 and a uniform exact margin at least `127/8664` over the target. Compactifying the simplex therefore adds no missing case and gives no further gain at this threshold.

I also tested, diagnostically, whether the same coarse denominator-10 dictionary should simply be pushed to a noticeably stronger threshold. New witness profiles enter before the total-energy cutoff, so a stronger theorem will require a genuinely richer dual dictionary or a new structural reduction rather than merely changing `19/10` to a prettier decimal. No stronger constant is claimed in this report.

## 10. Status, audit scope, continuation

Status: **PARTIAL QUANTITATIVE / FIXED METRIC MOVED / FULL WRITTEN PROOF / EXACT SELF-CHECK PASS / OUTSIDE AUDITS PENDING**.

The previous R12 and P26 Komlos audits concern the Guo--Fang--Lu universal theorem, not R13-C37. They do not count as audits of this new finite-five theorem. Closure under the fleet protocol therefore still needs two independent OTHER-track audits of R13-C37 before any paper-ready status.

The next mathematically useful routes are now sharply constrained:

1. improve `K_5^*<=19/10` by enriching the four-row diagonal-dual atlas while preserving the `q<=3/q=4/q>=5` split;
2. derive a structural theorem that replaces the finite four-row atlas;
3. improve the explicit lower obstruction above `1.84535465` at `n>=6`.

A checker-only repeat of the same 19/10 statement is not progress.

## 11. Runtime/model-control note

The exposed scheduler surface still does not provide a native model-family selector, reasoning-effort selector, authenticated runtime telemetry, or a guarantee of hour-long execution. `GPT-6 / maximum` therefore remains prompt text on this surface. Reports identifying GPT-5.6 Sol / UNVERIFIED are report evidence, not scheduler telemetry.

The historical P26 `You cannot modify this task` response was authorization-context dependent; later repository evidence records successful P26 editing from an authorized context. The legitimate workaround is the owning/admin-authorized task context or platform support exposing binding model/reasoning fields, not duplication or permission bypass. No scheduler change was attempted in this run.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  run_id: "20260917T1945Z_k5-upper-19over10-complete-9c4e"
  source: "Boolean Komlos; E0042/Bandeira; Bansal-Jiang arXiv:2508.03961; Guo-Fang-Lu arXiv:2609.11189v1"
  fixed_metric: "complete rigorously certified real-Boolean upper envelope B_R13(n)"
  metric_before:
    B5: "sqrt(2)+1/2"
    finite_5block_coefficient: "sqrt(2)+1/2"
  metric_after:
    B5: "19/10"
    finite_5block_coefficient: "19/10"
    strict_envelope_improvement_count: 30
    universal_large_n: "3*sqrt(2*pi), retained for n>=76"
  status: "PARTIAL_QUANTITATIVE_METRIC_MOVED"
  exact_self_check: "PASS"
  outside_audits_for_R13_C37: "0/2"
  prior_lower_obstruction_n6: "36907093/20000000"
  stuck_count_after: 0
  methods_used: [15, 28, 29]
  shared_roots_modified: false
  peer_files_modified: false
  scheduler_modified: false
```

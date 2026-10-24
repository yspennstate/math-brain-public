Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but no authenticated runtime telemetry establishes GPT-6/maximum, so I do not claim it. **NO SOURCE-METRIC MOVEMENT:** Salez Problem 2.3 remains OPEN and historical `W_exp=1/2 provisional` is unchanged. **MECHANISM MOVEMENT:** corrected the prior Green/localization theorem to the early mixing threshold required by Salez, proved a stronger transitivity-based same-time Green + spectral-band obstruction, and proved that the source-admissible affine Haiman stress-test family is genuinely outside Altschuler long-range expansion (indeed outside the earlier sublinear-defect pre-entropic weakening).

# PROB10-08 — early-threshold regular-relation obstruction and an affine family genuinely outside LRE

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL / auxiliary obstruction theorems proved / no new TV-cutoff graph class this run / independent validation pending / worldwide novelty UNVERIFIED**.

## 0. Required continuity and consumed state

Before research I read/recovered the required current state:

- `operations/PROB10_2026-09-20.md`; the PROB10-08 assignment freezes Salez Problem 2.3, rate-one continuous-time SRW, and requires a nonduplicating transitivity/entropy/Green route;
- current `POSTED.md`; the posted Abelian Cayley/product-condition target remains excluded and is not reopened;
- canonical `operations/claims/I0112.md`, blob `707af6a4ca81d0d6bcf52225c6f69c266ae981e9`;
- preserved R16 successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, blob recorded by the predecessor as `fa18fa8669a638c362ad0f90300b733425e808e5`;
- newest own predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T05-04-00Z_polynomial-localization-green_3b7e.md`, blob `08f2f1ecfb1757513a8b354994d9e3fcc51eddf8`;
- matching predecessor proof artifact;
- historical I0112 stuck diagnosis `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`, preserving the exhausted product-varentropy, synchronous-tensor, moving-weight/local-Poincare, Hecke/information-curvature, curvature, local-limit/AEP and time-zero subcommutation routes;
- newest neighboring P26 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_07-58-10__ramanujan-spherical-set-transfer.md`, blob `5f38814781f04ad7c39c1462e4492f6eb268c1fe`; P26 owns shell/spherical-distance transfer and is not duplicated;
- neighboring NM13 report `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T05-00-20Z__exact-distance-k-orbit-compression.md`; NM13 owns exact-distance/transitivity-orbit-compression and direct output-spectrum routes, which are not duplicated here.

The master head observed immediately before this run's writes was `9b68c16352e35be418d895289ca0f7bb7b578826`. Writes were create-only and conflict-safe; no force push or shared-root edit was used.

## 1. Primary-source refresh

### Salez

I reread the exact source and, critically, the exact time appearing in the varentropy window theorem.

- Justin Salez, `arXiv:2508.21055v1`, Problem 2.3: every bounded-degree vertex-transitive expander sequence should exhibit cutoff.
- The source convention is rate-one continuous-time SRW.
- Salez Theorem 5.1 bounds

`w_mix(epsilon)=t_mix(epsilon)-t_mix(1-epsilon)`

using the varentropy at

`boxed: t=t_mix(1-epsilon)`,

the **early** edge of the window.

This exact quantifier matters below.

### Altschuler

I reread the full LRE proof, including the place where LRE transfers to oriented-edge growth and then to NBRW endpoint entropy. A fresh bounded check found the arXiv record still exposing `arXiv:2609.14945v1`, submitted 14 September 2026, and no v2/correction/erratum surfaced. Its result remains: fixed-degree fixed-constant LRE implies Gaussian-profile cutoff. It is a baseline, not a new result of this track.

### Haiman--Schildkraut--Zhang--Zhao

I reread `arXiv:2109.13131v3`, Theorem 1.4 and its proof. Their 18-regular affine Cayley construction is on

`Gamma_q=SL(2,q) semidirect F_q^2`,

using the 16-element lift of an 8-regular LPS set plus a translation pair. The preceding R16 affine report already proved the exact chosen pure-translation family is a uniform spectral expander and recorded its two-scale spectrum. This run uses that family only as a source-admissible stress test.

## 2. Important correction to the immediate predecessor

The predecessor's likelihood identities are correct, but its cutoff inference was timed incorrectly. It set

`t_+=t_mix(epsilon)`

and invoked Salez Theorem 5.1 there. Salez's theorem uses varentropy at

`t_-=t_mix(1-epsilon)`.

Therefore the predecessor's statement

`nH_{2t_mix(epsilon)}(o,o)=n^{o(1)} => cutoff`

is **not justified as written**. The new proof artifact supersedes precisely that late-threshold inference; it does not alter the exact moment identities, which hold at every time.

This is a substantive correction, not bookkeeping. The corrected theorem is below.

## 3. Corrected early-threshold Green criterion

Fix `epsilon in (0,1/2)`, put

`t_-=t_mix(1-epsilon)`, `t_+=t_mix(epsilon)`,

and define

`R_-=nH_{2t_-}(o,o)`, `rho_-=log R_-/log n`.

For source-admissible bounded-degree expanders,

`t_-,t_+=Theta(log n)`.

At `t_-`, with `mu(y)=H_{t_-}(o,y)`, `Z(y)=n mu(y)`, `Y~mu`, one has exactly

`E_mu Z = R_-`,

`E_mu Z^{-1}=1`.

Together with the uniform `O(log n)` range of `log Z` at mixing scale, these identities give, for every `a in (0,1)`,

`Varent(mu)`

` <= (log n)^2 [a^2+K^2(n^(rho_- - a)+n^(-a))]`.                (3.1)

Salez Theorem 5.1 now applies at the correct time and yields

`boxed:`

`w_epsilon/t_+`

` <= C[1/log n+a+sqrt(n^(rho_- - a)+n^(-a))]`.                  (3.2)

Consequently,

`boxed: nH_{2t_mix(1-epsilon)}(o,o)=n^{o(1)}`                    (3.3)

for every fixed threshold implies cutoff, quantitatively

`w_epsilon/t_+ = O(rho_-+log log n/log n)`.                      (3.4)

This is an auxiliary sufficient criterion, not a proof that transitivity + spectral expansion implies (3.3).

## 4. New theorem: non-cutoff forces a sparse invariant relation and a same-time Green spike

The corrected likelihood-tail argument gives the following contrapositive. If a source-admissible sequence fails cutoff, then along a subsequence there are fixed

`epsilon in (0,1/2)`, `a>0`, `b>0`

such that at

`t=t_mix(1-epsilon)`

the set

`B_x={y:nH_t(x,y)>=n^a}`                                        (4.1)

has

`H_t(x,B_x)>=b`,                                                 (4.2)

and

`|B_x|<=n^(1-a)`.                                                (4.3)

The new point is that transitivity gives much more than a small set. The relation

`x R y <=> y in B_x`

is symmetric, automorphism-invariant and regular. If its degree is `m`, let `Q=A_R/m`. Then `Q` is symmetric stochastic, so `I-Q` is positive semidefinite. The heat matrix `H_t` is positive definite. Therefore

`tr[H_t(I-Q)]>=0`.

On the other hand, transitivity gives the exact identity

`tr(H_tQ)=nH_t(x,B_x)/m`.

Since also `tr H_t=nH_t(o,o)`, one obtains

`nH_t(o,o) >= nH_t(x,B_x)/m`.

Using (4.2)--(4.3):

`boxed: nH_t(o,o) >= b n^a`.                                    (4.4)

This is a **same-time** return-density obstruction. It is strictly stronger than the predecessor's generic Cauchy--Schwarz consequence at doubled time.

The full proof, including the PSD trace step, is in the matching artifact.

## 5. New spectral-band rigidity of any counterexample

Let

`r_i=1-lambda_i(P)`

be the nontrivial relaxation rates. They lie in `[gamma,2]`. At the early mixing threshold `t`, (4.4) implies

`sum_{i>=2} exp(-r_i t) >= (b/2)n^a`                              (5.1)

for large `n`.

Partition `[gamma,2]` into `O(t)=O(log n)` intervals of width `1/t`. One interval `I_n` must carry at least a `1/O(log n)` share of (5.1). If `M_n` is its eigenvalue count and its left endpoint is `r>=gamma`, then

`M_n >= c n^a exp(rt)/log n`

`    >= c n^a exp(gamma t)/log n`.                               (5.2)

With

`kappa_n=gamma t/log n`,

this becomes

`boxed: M_n >= n^(a+kappa_n-o(1))`                               (5.3)

inside a spectral interval of width

`boxed: O(1/log n)`.                                             (5.4)

Thus a genuine counterexample must simultaneously possess:

1. positive own-law mass on a polynomially small heat-kernel superlevel relation;
2. a polynomial same-time on-diagonal return excess; and
3. a polynomial pile-up of adjacency spectrum in an `O(1/log n)` band.

The attempt to close the conjecture from known multiplicity bounds fails: existing general bounds still permit polynomial clusters of exponent below one. Haiman et al.'s constructions show that this is a real obstruction rather than a formal loophole.

## 6. Exact stress test: the Haiman affine family is not LRE

Take the exact pure-translation Haiman family already frozen by the earlier R16 reports:

`G_q=Cay(Gamma_q,S union {t,t^{-1}})`,

`Gamma_q=Pi_q semidirect V_q`,

`Pi_q=SL(2,q)`, `V_q=F_q^2`, `|S|=16`, `t=(I,e)`.

The preceding affine report proves these graphs are 18-regular vertex-transitive spectral expanders. This run proves they are **not** a fixed-constant LRE sequence.

Use the normal translation subgroup

`A_q=V_q`

as Altschuler's test set. Under the quotient `Gamma_q -> Pi_q`, the translation generators disappear and only the 16 subgroup generators remain. Hence

`|B_G(A_q,r)| <= |V_q| |B_Cay(Pi_q,S)(e,r)|`

`             <= C |V_q| 15^r`.                                 (6.1)

But the output degree is 18, so LRE requires growth at branching rate 17. Choose

`r_q=floor((1/2)log_17 |Pi_q|)`.

For every fixed `c>0`, the nonsaturated side of Altschuler's LRE minimum applies for all large `q`, while

`|B_G(A_q,r_q)|/(|A_q|17^r_q)`

` <= C(15/17)^r_q ->0`.                                         (6.2)

Therefore no fixed positive LRE constant exists.

The same witness is stronger than that: if one only requires fixed-constant 17-growth for pairs satisfying

`|A|17^r <= |Gamma_q| exp(-rho_q)`

with `rho_q=o(log |Gamma_q|)`, then `(A_q,r_q)` still lies in the required regime and still violates the estimate. Thus this affine family also lies outside the earlier R16 **sublinear-defect pre-entropic LRE** theorem.

This does not prove cutoff for the affine family. It does prove that it is a genuine source-admissible test that cannot be dismissed as a hidden application of Altschuler's 2026 theorem.

## 7. Three nonexhausted approaches compared

### A. Correct-side likelihood tails + invariant threshold relation — retained

This was successful. The late/early timing issue was corrected, and the automorphism-invariant superlevel set gave the new regular-relation trace inequality (4.4) and spectral-band obstruction (5.3).

### B. Use the forced spectral pile-up plus known multiplicity bounds to close the source — rejected

The exponent forced by (5.3) is source-dependent and can be strictly below one. Current bounded-degree exact/approximate multiplicity bounds do not exclude such a cluster. The Haiman family itself has polynomial second-eigenvalue multiplicity, so no generic multiplicity contradiction is available.

### C. Test whether the affine hard case is already LRE after all — refuted exactly

The subgroup witness `V_q` exposes the precise scale loss: quotient cosets can grow at most like `15^r`, whereas the 18-regular LRE benchmark is `17^r`. The failure already occurs at radius about `(1/2)log_17 |SL(2,q)|`, far before macroscopic saturation.

This is a different recovery from the predecessor's generic likelihood truncation and from the old L2/NBRW, moving-Poincare, tensor, shell-transfer and orbit-compression routes.

## 8. Tests/checks actually run

No simulation, finite mixing plot, numerical optimization or checker was used. There is no finite computational core.

Analytic self-checks performed:

- reread Salez Theorem 5.1 and corrected the early/late threshold quantifier;
- checked the trace identity `tr(H_t A_R)=nL` directly;
- checked `I-Q` is PSD because a symmetric stochastic matrix has all eigenvalues at most one;
- checked `H_t` is positive definite because all semigroup eigenvalues are positive;
- checked the 16-vs-17 LRE witness against Altschuler Definition 1.3 at a radius where the nonsaturated branch is active;
- bounded current search for Altschuler corrections: no v2/erratum surfaced.

These are self-checks, not independent audits.

## 9. Source before/after and mechanism delta

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  predecessor_correction:
    old_statement: "late-threshold doubled-time Green criterion at t_mix(epsilon)"
    verdict: "NOT JUSTIFIED by Salez Theorem 5.1 as written"
    repaired_statement: "early-threshold criterion at t_mix(1-epsilon)"
  mechanism_before: "non-cutoff claimed to force macroscopic polynomial localization, but at the wrong window endpoint"
  mechanism_after: "correct early-threshold localization; regular symmetric threshold relation; polynomial same-time Green spike; O(1/log n) spectral-band pile-up; affine Haiman family proved non-LRE"
  new_graph_class_with_TV_cutoff: false
  finite_checker: "not applicable"
  independent_audits: 0
  status_label: "OPEN/PARTIAL"
```

## 10. Matching artifact and remaining full-scope gap

Full proofs are in

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T06-07-00Z_early-threshold-relation-affine-lre_71c9.md`,

created at commit

`3a93df2d3954c4d004e5b036e1bbce7068a6c2d4`

and read back at that exact commit.

The remaining source-level gap is now sharper and correctly timed:

> Rule out, using vertex transitivity plus a fixed ordinary spectral gap alone, positive own-law heat-kernel mass on a polynomially sparse automorphism-invariant superlevel relation at `t_mix(1-epsilon)`; or analyze a genuine stress-test such as the affine Haiman family by a Shannon/conditional-information mechanism.

Stationary spectral trace, raw L2/NBRW collision, generic eigenvalue multiplicity, the historical moving-weight Poincare route, and Altschuler LRE do not settle this obligation.

No scheduler state, cadence, enabled state, email, Drive object, public post, permission, workflow, shared ledger, peer file, or force push was changed.
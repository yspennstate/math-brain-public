Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED — the scheduler exposes no model/reasoning selector, so GPT-6 / maximum cannot be claimed.
Problem/source: R16 / I0013 — Muneya Matsui (2026), arXiv:2609.04638v1, Remark 2.4(ii), stationary rho-mixing CLT counterexample region. Metric: **NO MOVEMENT — `r_bad` = UNMEASURED -> UNMEASURED.** Status: PARTIAL. Unchanged count on the active I0013 metric: 2.

# R16 — I0013 base-2 iterated-log transfer audit

Run ID: `2026-09-16T15-45-00Z_i0013-iterlog-normalization`.
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity and recovered state

The newest complete own report was read first:

`runs/R16/2026-09-16T14-57-42Z_i0013-logbase-audit.md`.

That report preserved the earlier Beck--Fiala package, then continued the canonical R16 claim `operations/claims/I0013.md`. It proved the first base-conversion correction for Matsui Remark 2.4(ii): if Bradley's literal coefficient `d_B` is carried unchanged into Matsui's displayed condition, the threshold derived from the globally declared convention `log=log_2` is

\[
\frac{\gamma}{\alpha}<d_B\ln2,
\]

not `gamma/alpha<d_B`. No `r_bad` value was credited because Bradley's construction constant remains unspecified.

Before new mathematics this run refreshed:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- `operations/RFLEET_2026-09-16.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- `operations/claims/I0013.md` and neighboring `operations/claims/I0014.md`;
- the I0013 intake row by repository-wide search in `probability_1000_intake_I_20260914/problems.jsonl` and its mirror;
- the newest neighboring I0014 report;
- the current revised R12 report `runs/R12/2026-09-16T14-30-05Z_6d92bf.md`.

The GitHub connector truncates corpus-scale responses, so I do not claim a bytewise reread of every row in all approximately 780 intake records. The required root/fleet controls, active source row/ownership, neighboring claim and latest relevant reports were recovered. No missing state was replaced by invented history.

### Directed R12 audit

R12 now owns Afonso Bandeira's 2025 Paley degree-four SOS Conjecture 28 / I0102, not the historical AT problem. Its newest report is explicitly `PARTIAL / OPEN`, with unchanged frozen metric `(a,C,p0)=(1/2,1,5)`, and it does not present a complete source-level package for external full-proof audit. Therefore

`R16_AUDIT_R12 = PENDING_NOT_READY`.

No spot check is counted as the required independent audit.

## 2. Dated source and current-literature refresh — 16 September 2026

### Beck--Fiala source status

The R16 origin target was refreshed rather than silently reopened. Bansal--Jiang, arXiv:2508.03961, still advertises square-root Beck--Fiala only for `t >= log^2 n`, with a polylogarithmic loss below that regime. Guo--Fang--Lu, arXiv:2609.11189, submitted 10 September 2026, still states the stronger all-dimensional Komlos theorem and explicitly the consequence

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every finite set system of maximum degree `t>=1`. A bounded fresh search found no v2, withdrawal or proof-specific correction. This is a very recent literature-resolution claim, not mature referee certification. R16 therefore preserves its Beck--Fiala package/audit dependencies and continues the already-created outside claim I0013 rather than duplicating R13's generic Komlos target.

### I0013 source status

Primary source opened directly:

- Muneya Matsui, `arXiv:2609.04638v1`, 4 September 2026, *Can we further improve the central limit theorem for stationary rho-mixing sequences?*

The source is still v1 and still states in Remark 2.4(ii) that further analysis of Bradley's construction constant `d`, depending on `A_j` and `B_tau`, is required to locate the counterexample subregion inside `gamma<2alpha`.

Dated searches for the Matsui title/arXiv number, the exact `gamma<2alpha` question, later author papers and citing papers found no later source claiming to settle this exact parameter region. This is bounded current-status screening, not a proof of unpublished-priority nonexistence.

Primary Bradley target:

- Richard C. Bradley, *The central limit question under rho-mixing*, Rocky Mountain J. Math. 17 (1987), 95--114, DOI `10.1216/RMJ-1987-17-1-95`;
- correction, same volume, p. 891.

Project Euclid exposes the bibliographic/full-page record, but the article body is behind an additional-security iframe in this runtime. The correction is indexed and its snippet confirms typographical corrections, but the full corrected Theorem 1 / Proposition 0 text and the definitions of `A_j`, `B_tau`, and the literal construction constant `d` were still not recovered. This remains an access blocker and is not bypassed by guessing.

## 3. R16-I0013-C02 — general base-2 Bradley-transfer lemma

**STATUS: PROVED for Matsui's displayed asymptotic Bradley tests.**

**Scope.** This is a normalization theorem for the expressions Matsui evaluates from Bradley's condition (1.5). It does not determine Bradley's construction constant and therefore does not itself certify a counterexample.

Matsui declares globally that

\[
\log x=\log_2x.
\]

Let

\[
c=\ln2,
\qquad
L_1(x)=\log_2x,
\qquad
L_{r+1}(x)=\log_2 L_r(x)
\]

for sufficiently large `x`. Direct differentiation gives

\[
\boxed{
\frac{d}{dx}L_r(x)
=
\frac{1}{c^r x\prod_{j=1}^{r-1}L_j(x)}.
}
\tag{C02.1}
\]

Fix `r>=1`, `alpha>0`, `0<beta<1`, and put `gamma=1-beta`. Define the source-normalized iterated-log rate

\[
\tau_r(n)
=
\frac{\alpha}{\left(\prod_{j=1}^{r-1}L_j(n)\right)L_r(n)^\beta}.
\tag{C02.2}
\]

For all sufficiently large `x`, the integrand in the corresponding harmonic sum is positive decreasing. The sum-integral discrepancy is therefore bounded, and C02.1 gives

\[
\boxed{
\sum_{k\le n}\frac{\tau_r(k)}{k}
=
\frac{\alpha c^r}{\gamma}L_r(n)^\gamma+O(1).
}
\tag{C02.3}
\]

For the critical logarithmic case `beta=1`, the same calculation yields

\[
\boxed{
\sum_{k\le n}
\frac{\alpha}{k\prod_{j=1}^{r}L_j(k)}
=
\alpha c^r\ln L_r(n)+O(1).
}
\tag{C02.4}
\]

Now insert the literal Bradley coefficient `d_B>0` in the argument used by Matsui,

\[
x_n
=
n^{1/2}
\exp\left[-\frac{d_B}{2}
\sum_{k\le n}\frac{\tau_r(k)}k\right].
\tag{C02.5}
\]

### Exponential moment gauge

Take

\[
q_r(x)=x^2\exp\big(L_r(x)^\gamma\big),
\qquad 0<\gamma<1.
\tag{C02.6}
\]

For depth `r=1`, C02.3 gives

\[
L_1(x_n)
=
\frac12L_1(n)+O(L_1(n)^\gamma),
\]

hence

\[
L_1(x_n)^\gamma
=
2^{-\gamma}L_1(n)^\gamma+o(L_1(n)^\gamma).
\]
Therefore

\[
\boxed{
\log\frac{q_1(x_n)}n
=
\left[
-\frac{d_B\alpha c}{\gamma}
+2^{-\gamma}
\right]L_1(n)^\gamma
+o(L_1(n)^\gamma).
}
\tag{C02.7}
\]

Thus the strict sufficient condition from this displayed test is

\[
\boxed{d_B\alpha\ln2>\gamma2^{-\gamma}.}
\tag{C02.8}
\]

For every fixed depth `r>=2`, C02.3 first gives `L_1(x_n)=(1/2)L_1(n)+o(L_1(n))`; hence

\[
L_2(x_n)=L_2(n)-1+o(1),
\]

and inductively

\[
L_r(x_n)^\gamma=L_r(n)^\gamma+o(L_r(n)^\gamma).
\]
Consequently

\[
\boxed{
\log\frac{q_r(x_n)}n
=
\left[
-\frac{d_B\alpha c^r}{\gamma}
+1
\right]L_r(n)^\gamma
+o(L_r(n)^\gamma),
\qquad r\ge2,
}
\tag{C02.9}
\]

and the strict sufficient condition is

\[
\boxed{d_B\alpha(\ln2)^r>\gamma.}
\tag{C02.10}
\]

### Polynomial iterated-log gauge

Using C02.4 with

\[
q_{r,\eta}(x)=x^2L_r(x)^\eta,
\qquad\eta>0,
\]

gives

\[
\boxed{
q_{r,\eta}(x_n)=o(n)
\quad\Longleftrightarrow\quad
 d_B\alpha(\ln2)^r>\eta
}
\tag{C02.11}
\]

at the strict exponent level. For `r=1`, the factor `L_1(x_n)~L_1(n)/2` changes only the multiplicative constant, not the logarithmic power.

## 4. Source-level consequences of C02

These are normalization consequences for Matsui's displayed asymptotic calculations **if Bradley's literal numerical `d_B` is carried unchanged**.

1. **Remark 2.4(ii)** (`r=1`, critical log-power gauge):
   
   \[
   \gamma/\alpha<d_B\ln2,
   \]
   
   recovering and subsuming C01 from the previous run.

2. **Remark 2.5(ii)** (`r=1`, `beta+gamma=1`, exponential gauge): Matsui prints the sufficient strict condition
   
   \[
   \alpha d_B>\gamma2^{-\gamma}.
   \]
   
   C02.8 instead gives
   
   \[
   \boxed{\alpha d_B\ln2>\gamma2^{-\gamma}.}
   \tag{C02.12}
   \]

3. **Remark 2.7(ii)** (`r=2`, critical iterated-log power): the analogous literal transfer uses
   
   \[
   d_B\alpha(\ln2)^2
   \]
   
   as the effective exponent coefficient.

4. **Remark 2.8(i)** (`r=2`, `beta+gamma=1`, exponential iterated-log gauge): Matsui prints the counterexample condition `alpha>gamma/d_B`. C02.10 gives instead
   
   \[
   \boxed{d_B\alpha(\ln2)^2>\gamma}
   \tag{C02.13}
   \]
   
   for the displayed test with an unchanged literal Bradley coefficient.

This does **not** establish that Matsui's qualitative counterexample statements are false. The constant `d` is unspecified and may be harmlessly renormalized. The precise issue is quantitative: before any recovered Bradley value is credited to I0013's frozen metric, one must determine whether Matsui silently absorbed these base-conversion factors into the symbol `d`. The inaccessible Bradley primary text is therefore now even more important.

### Coordination note for neighboring I0014

The neighboring I0014 report deliberately followed Matsui's displayed normalization and reduced its exact exponential-moment test to a condition involving `d=2`. C02 shows that any future attempt to identify that displayed `d` with Bradley's literal construction constant must first settle the same base-conversion convention. This report does not edit, invalidate, or count as an audit of the I0014 package.

## 5. Exact self-check

Executed exact/symbolic checker:

`artifacts/R16/2026-09-16T15-45-00Z_i0013-iterlog-normalization__base2_iterlog_checker.py`

Creation/readback commit:
`4bb21dc7f17a5cced55c8560056f725096552d5d`.

Executed output:

`artifacts/R16/2026-09-16T15-45-00Z_i0013-iterlog-normalization__base2_iterlog_checker.out`

Creation/readback commit:
`e7829ccc0fa4bc866451454266f04f4cb15407fb`.

The checker:

- certifies by exact rational arithmetic
  
  \[
  0.693147180559<\ln2<0.693147180560<1;
  \]
- verifies C02.1 symbolically through iterated-log depth four;
- verifies the exact primitive coefficient `(ln 2)^r/gamma` through depth four;
- verifies the threshold-coefficient algebra.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent research-track audit.

## 6. Metric, failed routes, and remaining obstruction

The active metric remains

\[
r_{\rm bad}
=
\sup\left\{
\frac\gamma\alpha<2:
\text{an explicit source-valid counterexample is rigorously certified}
\right\}.
\]

No literal Bradley value `d_B` has yet been recovered. Therefore

\[
\boxed{r_{\rm bad}:\ \text{UNMEASURED}\to\text{UNMEASURED}.}
\]

This is the second consecutive unchanged run on the active I0013 metric, so the stuck protocol has **not** yet triggered.

Failed/blocked routes retained:

1. **Credit Matsui's printed `d` directly to `r_bad`.** Invalid: `d` is unspecified, and C01/C02 show a nontrivial base-conversion ambiguity if it is identified literally with Bradley's coefficient.
2. **Infer `A_j`, `B_tau`, or `d_B` from secondary snippets.** Rejected: Project Euclid's primary article body remains security-gated; secondary metadata are insufficient for a source-normalized certificate.
3. **Use Bradley 1980 logarithmic-moment counterexamples.** Insufficient for evaluating the exact 1987 construction constant required by the I0013 frozen metric.
4. **Return to improving Beck--Fiala after the fresh all-`t` resolution claim.** Not the current canonical R16 allocation; its proof package and audits remain preserved.
5. **Borrow I0014 progress as I0013 movement.** Invalid scope and ownership; it is a distinct source question and its metric is `beta_bad`.

The blocker remains the same concrete statement:

\[
\boxed{\text{Recover and certify one literal }d_B=d_B(A_j,B_\tau)>0
\text{ from corrected Bradley (1987).}}
\]

The next run should obtain Bradley's corrected Theorem 1 and Proposition 0 from a primary/library representation that exposes the formulas, transcribe every admissibility constraint on `A_j,B_tau,d_B`, and reduce one explicit parameter choice to exact rational or interval inequalities. Only then can C02 turn the literal Bradley constant into a source-normalized candidate `r_bad`.

If the next run is again unable to move `r_bad`, the unchanged count becomes three and the owner's full stuck-report protocol must be used instead of producing another auxiliary lemma.

## 7. Audit status

- Beck--Fiala P26 full-proof audit: **PENDING**.
- Beck--Fiala second independent-track audit: **PENDING**.
- I0013 P26 audit: **PENDING**.
- I0013 second-track audit: **PENDING**.
- Directed R16 audit of R12: **PENDING_NOT_READY**.

No unavailable audit is counted.

## 8. Structured ledger delta for P26

```yaml
ledger_delta:
  track: R16 HARD OUTSIDE
  queue_id: I0013
  source: "Muneya Matsui (2026), arXiv:2609.04638v1, Remark 2.4(ii); Bradley (1987), Rocky Mountain J. Math. 17, 95-114 plus correction p.891"
  target: "source-valid stationary rho-mixing CLT counterexample region inside gamma<2alpha"
  metric: "largest certified r_bad=gamma/alpha<2 for an explicit source-normalized counterexample"
  before: UNMEASURED
  after: UNMEASURED
  status: PARTIAL
  unchanged_count: 2
  exact_evidence:
    - "R16-I0013-C02: general base-2 iterated-log transfer coefficients (ln 2)^r"
    - "artifacts/R16/2026-09-16T15-45-00Z_i0013-iterlog-normalization__base2_iterlog_checker.py @ 4bb21dc7f17a5cced55c8560056f725096552d5d"
    - "artifacts/R16/2026-09-16T15-45-00Z_i0013-iterlog-normalization__base2_iterlog_checker.out @ e7829ccc0fa4bc866451454266f04f4cb15407fb; ALL_EXACT_CHECKS_PASS"
  audit_ids:
    p26: PENDING
    second_track: PENDING
    directed_r12: PENDING_NOT_READY
  blocker: "literal corrected Bradley Theorem 1 / Proposition 0 formulas for A_j, B_tau and d_B remain inaccessible"
```

No root ledger, peer file, email, Drive content, public posting, permission, or schedule was changed in this run.

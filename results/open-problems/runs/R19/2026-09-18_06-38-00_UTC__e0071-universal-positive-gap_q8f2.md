Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **not GPT-6 at maximum. NO MOVEMENT: `C_E0071: 1 -> 1`; unchanged count `2 -> 3`; methods #5, #11, #27.**

# R19 CLOSABLE OUTSIDE — E0071 / Björklund Problem 3, universal positive-gap obstruction

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and preserved state

I continued from the newest R19 report

`runs/R19/2026-09-18_05-38-00_UTC__e0071-doubly-stochastic-obstruction_d7c4.md`

and did not restart from the native task title.

The original Hasebe--Ueda I0084 target remains frozen exactly as handed off in

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

Preserved facts:

- source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084;
- exact initial-law hypothesis: finite `(2+alpha)` moment;
- `S_t` may be the law of a classical or a free alpha-stable process;
- **the frozen arXiv-v2 conclusion uses ordinary classical convolution `mu * S_t` even when `S_t` is a free-stable law**;
- retained alpha=`1/2` source metric: **`2/2`**;
- stronger-moment and compact-support-only results do not replace source cases;
- the ordinary-`*` frozen package still needs one P26 and one distinct OTHER-track end-to-end audit; ALEA free-`boxplus` audits do not discharge that version-specific gate.

I0084 is not reopened. F0057 is also not reopened.

The active exclusive R19 claim remains `operations/claims/E0071.md`: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 3.

## 2. Repository/source refresh before mathematics

Before the new argument I reread/recovered on `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the newest R19 report and the I0084 rotation handoff;
- canonical E0071 ownership;
- the newest neighboring Björklund Problem-2 report, `research7_2026-09-17/R7-03/runs/2026-09-18/2026-09-18T053000Z__report.md`;
- exact E0071 audit searches.

No P26 E0071 end-to-end PASS and no distinct OTHER-track E0071 end-to-end PASS were recovered.

The primary source was reread on **2026-09-18** at arXiv:1406.0763v2. The current HTML remains v2 dated 2014-07-07. Section 1 defines a measured group by semigroup generation of `G` by `supp(mu)`. Appendix II §7.1 still prints Problem 3 as

\[
\lim_{n\to\infty}\frac1n\sum_{k=1}^n
\int_Gd(gH,H)\,d\mu^{*k}(g)=0?
\tag{P3}
\]

for `H` acting ergodically on the Poisson boundary. The surrounding paper defines ordinary drift with the usual single-time `1/n` normalization.

Fresh dated searches used combinations of the exact formula, the paper title, `Problem 3`, `drifts of random walks on homogeneous spaces`, later Björklund work, homogeneous-space drift, and citations to arXiv:1406.0763. They recovered the original v2 and later unrelated Björklund work but no later primary erratum or explicit source-matching resolution of the printed Problem 3. This remains bounded negative evidence only; publication novelty is **UNVERIFIED** and typo/folklore risk is high.

## 3. New idea before validation

Previous runs progressed from one explicit witness to the source-suggested product/diagonal witness and then to finite/proper-infinite quotient obstructions. The remaining question was whether nonproper metrics could evade the structural argument.

This run deliberately used three methods not previously used on E0071:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** split the quotient into a near ball of radius `a r` and a far set beyond `(1-a)r`, then optimize over `a`;
- **#11 DUALIZE:** replace the unbounded first moment by two bounded indicator tests and use total-variation control of the Cesàro stationarity defect;
- **#27 SWAP THE QUANTIFIERS:** prove the negation simultaneously for every nontrivial quotient and every invariant metric instead of constructing another example.

The route works and removes the properness assumption completely.

## 4. Universal positive-gap theorem

Let `(G,mu)` be a countable measured group in the source convention, let `H<G`, set `X=G/H` and `o=H`, and let `d` be any left `G`-invariant metric on `X`. Assume `X` is nontrivial. Define

\[
A_n:=\frac1n\sum_{k=1}^n
\int_Gd(gH,H)\,d\mu^{*k}(g).
\]

Because `supp(mu)` semigroup-generates `G` and `H` is proper, there is some `s in supp(mu)` with `sH != H`. Put

\[
p:=\mu(s)>0,
\qquad
r:=d(sH,H)>0.
\]

**Theorem.** For every `n>1/p`,

\[
\boxed{
A_n\ge\frac{r\,(p-1/n)}{(1+\sqrt p)^2}.
}
\tag{1}
\]

Consequently

\[
\boxed{
\liminf_{n\to\infty}A_n
\ge\frac{pr}{(1+\sqrt p)^2}>0.
}
\tag{2}
\]

Thus the printed Problem 3 is false for **every nontrivial quotient `G/H` and every left `G`-invariant metric**, irrespective of Poisson-boundary ergodicity.

### Proof

Let `P` be the quotient Markov kernel and

\[
\nu_n:=\frac1n\sum_{k=1}^n\delta_oP^k.
\]

Then `A_n=int d(o,x)dnu_n(x)`. Fix `a in (0,1)` and define

\[
U_a=\{x:d(o,x)<ar\},
\qquad
V_a=\{x:d(o,x)>(1-a)r\}.
\]

For `x in U_a`, left invariance gives

\[
d(o,sx)\ge d(o,so)-d(so,sx)
=r-d(o,x)>(1-a)r,
\]

so `sx in V_a`. Hence

\[
(\nu_nP)(V_a)\ge p\nu_n(U_a).
\tag{3}
\]

Markov's inequality gives

\[
\nu_n(U_a)\ge1-\frac{A_n}{ar},
\qquad
\nu_n(V_a)\le\frac{A_n}{(1-a)r}.
\tag{4}
\]

The exact telescoping identity

\[
\nu_nP-\nu_n
=\frac{\delta_oP^{n+1}-\delta_oP}{n}
\tag{5}
\]

implies, for every event `E`,

\[
|\nu_nP(E)-\nu_n(E)|\le\frac1n.
\tag{6}
\]

Applying (6) to `V_a` and combining (3)--(4),

\[
p\left(1-\frac{A_n}{ar}\right)
\le\frac{A_n}{(1-a)r}+\frac1n.
\]

Therefore

\[
A_n\ge
\frac{r(p-1/n)}{p/a+1/(1-a)}.
\tag{7}
\]

The denominator is minimized at

\[
a=\frac{\sqrt p}{1+\sqrt p},
\]

where it equals `(1+sqrt(p))^2`. This proves (1), and (2) follows by taking `n -> infinity`. If some `A_n=+infinity`, the inequality is automatic. ∎

## 5. Consequences and relation to earlier R19 work

This theorem strictly subsumes the preceding E0071 arguments:

- the simple symmetric walk on `Z` no longer needs parity;
- the source-suggested product/diagonal example no longer needs the central-binomial calculation;
- finite quotients no longer need convergence to the uniform law;
- infinite quotients no longer need a proper metric or escape from finite sets;
- recurrence, Liouville theory, CLTs and the Poisson boundary play no role.

The obstruction is purely local: if the Cesàro first moment were tending to zero, most Cesàro mass would lie very near the base coset. One support atom of positive mass moves that near mass a definite distance away, while the Cesàro occupation measure changes by only `O(1/n)` under one Markov step. Those two facts are incompatible.

This is a strong diagnosis of the printed normalization but **not** a claim about Björklund's intended correction. The surrounding source theory uses single-time normalized drift. Only the literal printed Problem 3 is being decided here.

## 6. Artifact / validation budget

The complete proof is archived at

`artifacts/R19/2026-09-18_06-36-00_UTC__e0071_universal_positive_gap_q8f2.md`

creation commit

`894e6873521d8017e108c94aee60454a0ec33688`,

blob

`a7b72592b5253df16ec68d400e4e8c58fd76c924`.

It was read back at that exact commit.

No finite checker was created: this is an analytic theorem, and the complete proof is on the page. A decorative finite certificate would not improve the tracked quantity.

## 7. Metric, stagnation and mandatory next mode

The source metric was already saturated:

\[
C_{E0071}:1\to1.
\]

Therefore this run is honestly **NO MOVEMENT**, and the ordinary unchanged count advances

`2 -> 3`.

Status remains

**REFUTED_CANDIDATE / SOURCE_MATCHING / AS_PRINTED / AUDIT_PENDING / NOVELTY_UNVERIFIED**.

Because this is now the **third consecutive no-movement E0071 run**, the next R19 invocation is required by Section I to be a **thinking-only STUCK1 report with no new theorem claim**. It must state the exact blocker, catalog prior routes and failures, identify the simplest unresolved issue and nearest literature analogue, choose exactly one permitted recovery action, and name a fresh method triple.

Current external closure obligations remain:

- P26 end-to-end source/package audit: `0/1` recovered;
- distinct OTHER-track end-to-end source/package audit: `0/1` recovered;
- preserve the dated prior-art/erratum search and explicit typo/folklore warning.

R19's own strengthening is a self-check, not an independent audit.

## 8. Scheduler/model-control status

The implementation evidence and this runtime interface remain aligned on the same limitation: the exposed task controls include prompt/title/schedule-or-start/timing/enabled state, but **no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated applied-run model receipt**. GPT-6/maximum therefore remains prompt-only here.

The older P26 response `You cannot modify this task` was authorization-context-specific. The current root ledger separately records that an authorized P/C context later succeeded in updating P26. The demonstrated lawful workaround is the owning/authorized scheduler context (or platform/backend support), not duplicating the task or bypassing permissions. No scheduler or permission change was attempted by R19 in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  preserved_predecessors:
    I0084:
      source: "Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5"
      convention: "ordinary classical convolution mu * S_t, including when S_t is a free-stable law"
      metric_name: "complete alpha=1/2 source cases under frozen arXiv scope"
      metric_value: "2/2"
      status: "ROTATED_HANDOFF; source mathematically refuted at retained endpoint scope; ordinary-* version-specific audits pending"
    F0057:
      status: "ROTATED / PROVED_CANDIDATE / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  active_source:
    id: E0071
    source: "Michael Bjorklund, arXiv:1406.0763v2, Appendix II section 7.1, Problem 3"
    exact_scope: "printed Cesaro average of unnormalized quotient distances"
    claim: "operations/claims/E0071.md"
  metric:
    name: C_E0071
    before: 1
    after: 1
    movement: false
  unchanged_count:
    before: 2
    after: 3
  tried_moves: [5, 11, 27]
  result: "For every nontrivial quotient and every invariant metric, choosing any support atom s moving H with p=mu(s), r=d(sH,H) gives A_n >= r(p-1/n)/(1+sqrt(p))^2 and liminf A_n >= pr/(1+sqrt(p))^2 > 0."
  status: "REFUTED_CANDIDATE / SOURCE_MATCHING / AS_PRINTED / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  remaining_obligation: "next invocation mandatory STUCK1 thinking-only; two independent audits (P26 plus one distinct OTHER); preserve erratum/normalization-risk qualification"
  evidence:
    I0084_handoff: "artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md"
    E0071_claim: "operations/claims/E0071.md"
    universal_gap_artifact: "artifacts/R19/2026-09-18_06-36-00_UTC__e0071_universal_positive_gap_q8f2.md @ 894e6873521d8017e108c94aee60454a0ec33688"
  audits:
    P26: null
    other: null
```

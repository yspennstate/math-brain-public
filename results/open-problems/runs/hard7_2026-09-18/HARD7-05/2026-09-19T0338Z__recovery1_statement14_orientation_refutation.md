Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 correction: the frozen metric previously recorded as `W_{1/4}=0` was based on an invalid comparator-exponent input; after source-level correction the verified value is restored to `W_{1/4}=1/8`. Recovery methods: B8 / B19 / B26.**

# HARD7-05 bounded research iteration — RECOVERY1: the Molchan `Statement 1.4` comparator exponent is inconsistent with Gaussian persistence continuity

Status: **PARTIAL / source target OPEN / comparator route REFUTED AS WRITTEN / prior HARD7-05 exact-`theta` consequences RETRACTED.**

This run executes the single Section-I recovery chosen in `2026-09-19T0252Z__stuck1_endpoint_consistency.md`: **refute instead of prove**, meaning refute the proposed global finite-`m` comparison route rather than the externally posed `theta_{2,H}` problem. The recovery succeeds, but in a more important way than the proposed finite counterexample search: the exact persistence rate assigned to the comparison family in Molchan v11, Statement 1.4, is itself incompatible with a published Gaussian-persistence continuity theorem and contains an orientation error in its displayed proof.

## 1. Continuity, ownership, repository state, and source refresh

I resumed the exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by HARD7-05. Before doing new mathematics I reread the required controls and fleet state: `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical claim, the full visible HARD7-05 history through the STUCK1 report, and the newest neighboring HARD7-04/HARD7-06 checkpoints. Repository-wide searches for the exact arXiv id/title and the HARD7-05 alias found no competing owner or posted equivalent.

Primary source rechecked directly:

- G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265v11, revised **4 July 2026**, https://arxiv.org/abs/2509.10265 .

The current PDF still says on printed p. 3 that the one-sided exponents `theta_{2,H}` for `H != 1/2` remain unsolved. Therefore the external target itself remains OPEN. The same PDF states on printed p. 6 / Statement 1.4 that the stationary process with covariance

\[
K_h(t):=\frac{\cosh((2h-1)t/2)}{\cosh(t/2)}
\tag{1.1}
\]

has persistence exponent

\[
\vartheta(h)=\frac38\min\{h,1-h\}.
\tag{1.2}
\]

The proof is on printed pp. 22--23, equations (70)--(75).

The published comparison/continuity source used below is:

- F. Aurzada and M. Kilian, *Asymptotics of the persistence exponent of integrated fractional Brownian motion and fractionally integrated Brownian motion*, Theory Probab. Appl. 67(1) (2022), 77--88, arXiv:2007.01254v2, https://arxiv.org/abs/2007.01254 .

Their Theorem 1 proves `theta_I(H) ~ H` as `H downarrow 0`, and their Lemma 1 gives a persistence-exponent continuity criterion for Gaussian stationary processes. I checked the current paper/PDF rather than relying on the previous report's paraphrase.

A bounded current-literature search on 2026-09-19 used the exact Molchan title/arXiv id, the covariance phrase `cosh((2H-1)t/2)/cosh(t/2)`, `3/8 persistence exponent`, and Laplace-transform-of-fBM persistence aliases. It recovered Molchan v11, Aurzada--Kilian, and standard related persistence papers, but no published correction of Statement 1.4. This is bounded negative evidence, not a worldwide novelty certification.

## 2. Frozen source metric — correction, not progress

The admission metric was

\[
W_{1/4}:=U_{1/4}-L_{1/4}.
\]

Run 3 had changed the track ledger from `1/8` to `0` by combining an exact covariance inequality with the exact reference rate asserted in Molchan Statement 1.4. Runs 4--6 then used the same reference-rate input at other rational points.

The present run proves that this exact reference-rate input cannot be correct as written. Therefore those persistence-exponent conclusions cannot be retained. The immutable old reports stay in the repository, but their `theta` conclusions are explicitly superseded by this correction.

Returning to the verified source bounds on printed p. 3, equation (3), at `H=1/4` gives

\[
L_{1/4}=\frac12\min\{1/4,3/4\}=\frac18,
\]

and

\[
U_{1/4}=\min\left\{\frac14,\sqrt{\frac{1-(1/4)^2}{12}}\right\}
=\min\left\{\frac14,\frac{\sqrt5}{8}\right\}=\frac14.
\]

Hence the honest corrected metric is

\[
\boxed{W_{1/4}:0\ \text{(invalid track value)}\longrightarrow\frac18\ \text{(verified source value)}.}
\tag{2.1}
\]

This is **negative movement / correction**, not research progress. It is preferable to preserving a false zero gap.

## 3. B8 — discretize first, then stop when the premise fails

The STUCK1 recovery proposed searching rational/algebraic triples `(H,m,t)` for a finite covariance reversal

\[
K_m\!\left(\frac{4H}{3m}t\right)>R_H(t).
\tag{3.1}
\]

I first attacked exactly that negation, including the small-`H` boundary layers suggested by Aurzada--Kilian. The direct covariance formulas repeatedly remained on the previously observed side over the tested regimes. That made a finite checker premature: a floating-point non-hit is not evidence for an all-lag theorem, and Section A explicitly forbids manufacturing a certificate merely to show that a run happened.

The right discretization was instead to isolate the comparison family itself and test its claimed rate against a scaling limit whose persistence exponent is rigorously known. This removes the integrated-fBM covariance completely and exposes a source-internal inconsistency.

## 4. B19 — make the comparison-family scaling an exact algorithmic proof

Let `vartheta(h)` denote the continuous-time zero-level persistence exponent of the centered stationary Gaussian process with covariance (1.1), for `0<h<=1/2`. For `t>=0`, the same covariance has the exact exponential form

\[
K_h(t)
=\frac{e^{-ht}+e^{-(1-h)t}}{1+e^{-t}}.
\tag{4.1}
\]

Rescale time by `1/h` and write

\[
A_h(\tau):=K_h(\tau/h)
=\frac{e^{-\tau}+e^{-(1-h)\tau/h}}{1+e^{-\tau/h}}.
\tag{4.2}
\]

For every fixed `tau>0`,

\[
A_h(\tau)\longrightarrow e^{-\tau}\qquad(h\downarrow0),
\tag{4.3}
\]

while `A_h(0)=1`. The limit is the Ornstein--Uhlenbeck correlation, whose stationary persistence exponent is `1`.

More importantly, the technical hypotheses of Aurzada--Kilian Lemma 1 are immediate and **uniform** here. For `0<h<=1/2` and `tau>=0`, (4.2) gives

\[
e^{-\tau}\le A_h(\tau)\le 2e^{-\tau}.
\tag{4.4}
\]

Indeed, the upper bound uses `(1-h)/h>=1` and the denominator `>=1`; for the lower bound,

\[
A_h(\tau)-e^{-\tau}
=\frac{e^{-(1-h)\tau/h}-e^{-(1+h)\tau/h}}
       {1+e^{-\tau/h}}\ge0.
\tag{4.5}
\]

Therefore for every integer `ell>=1`,

\[
\sup_{0<h\le1/2}\sum_{j=L}^{\infty}A_h(j/\ell)
\le 2\sum_{j=L}^{\infty}e^{-j/\ell}\longrightarrow0,
\tag{4.6}
\]

which is condition (4) of their Lemma 1. Also

\[
0\le1-A_h(\tau)\le1-e^{-\tau}\le\tau,
\tag{4.7}
\]

so for any `eta>1`,

\[
|\log\varepsilon|^\eta
\sup_{0<h\le1/2,\,0\le\tau\le\varepsilon}
(1-A_h(\tau))
\le |\log\varepsilon|^\eta\varepsilon\longrightarrow0,
\tag{4.8}
\]

which is their local condition (5). Finally the limit correlation satisfies

\[
\limsup_{\tau\to\infty}
\frac{\log(e^{-\tau})}{\log\tau}=-\infty<-1,
\tag{4.9}
\]

which is condition (6). The prelimit processes have analytic covariance and hence continuous versions; the OU limit is continuous.

Applying Aurzada--Kilian Lemma 1 to any sequence `h_k downarrow 0` therefore yields convergence of persistence exponents of the rescaled stationary processes. Time rescaling by `1/h` divides the original correlation scale and multiplies the stationary persistence rate by `1/h`. Hence

\[
\boxed{
\frac{\vartheta(h)}{h}\longrightarrow1
\qquad(h\downarrow0).
}
\tag{4.10}
\]

This is a full analytic argument, not simulation and not an appeal to the integrated-fBM target.

Molchan Statement 1.4 instead gives, for every `0<h<=1/2`,

\[
\frac{\vartheta(h)}h=\frac38.
\tag{4.11}
\]

Equations (4.10) and (4.11) are incompatible. Consequently **Statement 1.4 cannot be correct as written under the standard stationary persistence-exponent interpretation used in the same paper.**

No finite checker is appropriate for (4.10): it is a theorem-sized continuity argument whose proof is on the page. Creating a grid certificate would weaken, not strengthen, the claim.

## 5. B26 — the sporadic failure is an orientation error in the displayed proof

The contradiction above also points to a concrete error on printed pp. 22--23 of Molchan v11.

Equation (70) in the source gives, with the notation of Lemma 1.5,

\[
s\,[\log(\vartheta(H)/\psi(H))]'\le0.
\tag{5.1}
\]

For the application to `0<H<1/2`, the source sets `s=+1` and `psi(H)=cH`. Thus (5.1) says

\[
H\longmapsto \frac{\vartheta(H)}H
\quad\text{is nonincreasing.}
\tag{5.2}
\]

Taking `H<H_0=1/2` therefore yields

\[
\frac{\vartheta(H)}H
\ge
\frac{\vartheta(1/2)}{1/2}
=\frac38,
\qquad	ext{i.e.}\qquad
\vartheta(H)\ge\frac38H.
\tag{5.3}
\]

That is the **lower bound** already obtained in the preceding paragraph of the source by ordinary Slepian comparison (its equation (75)).

However, at the bottom of printed p. 23 the source applies the integrated relation in the opposite orientation and writes an **upper** bound `vartheta(H) < 3H/8` for `H<1/2`. Integrating a derivative inequality from `H_0=1/2` *downward* to `H< H_0` reverses the endpoint comparison. This is exactly the sign/orientation mistake: the displayed differential inequality cannot supply the claimed upper bound.

The independent scaling limit (4.10) is a useful sanity check: the corrected direction (5.3) is compatible with `vartheta(h)/h -> 1`, whereas the source's equality `3/8` is not.

## 6. Consequences for HARD7-05's previous reports

This correction affects the track, not merely a speculative global extension.

- `2026-09-18T2237Z_theta_quarter_exact.md`: the exact algebraic covariance inequality/checker may remain valid **as a covariance statement**, but the conclusion `theta_{2,1/4}=1/8` used the false exact comparator rate and is retracted.
- `2026-09-18T2341Z_theta_third_exact.md`: same; the covariance comparison may remain valid, but `theta_{2,1/3}=1/6` is retracted.
- `2026-09-19T0040Z_exact_open_neighborhoods.md`: the persistence-exponent identity on neighborhoods is retracted because its anchor rates are no longer certified.
- `2026-09-19T0138Z_theta_fifth_exact.md`: the covariance comparison may remain valid, but `theta_{2,1/5}=1/10` is retracted.
- `2026-09-19T0252Z__stuck1_endpoint_consistency.md`: its conclusion that the *finite-m covariance comparison* must fail because of Aurzada--Kilian was based on the same erroneous `3m/8` rate. The correct diagnosis is now sharper: the contradiction is already inside the claimed comparator-rate theorem.

The old exact-arithmetic artifacts are **not deleted or rewritten**. They are historical certificates for the finite algebra they actually checked. They must no longer be cited as certificates of the retracted persistence-rate consequences.

This distinction matters: an exact covariance inequality plus an incorrectly assigned reference persistence rate does not determine the target persistence exponent.

## 7. Source target remains open; what genuinely survives

The externally posed problem is still to determine `theta_{2,H}` for integrated fBM when `H != 1/2`. Nothing in this run solves or refutes that problem.

What survives rigorously from the track is:

1. the exact integrated-fBM Lamperti covariance formulas and the algebraic covariance inequalities already certified by the finite checkers;
2. the source's older published lower/upper bounds, subject to their original hypotheses;
3. Aurzada--Kilian's rigorous asymptotics `theta_I(H)/H -> 1` as `H downarrow0` and the symmetric `H upward1` asymptotic;
4. the new correction theorem (4.10) for the Molchan comparison covariance, obtained directly from Aurzada--Kilian's published persistence-continuity lemma;
5. the proof-level diagnosis that Molchan v11 Statement 1.4's upper-bound step reverses the integration orientation.

Status labels must therefore remain **OPEN / PARTIAL** for the source problem. The thing refuted is **Statement 1.4 as written and the HARD7-05 route depending on its exact `3h/8` value**, not the source's open `theta_{2,H}` question.

## 8. Section-I recovery outcome and next route

The single chosen recovery action `REFUTE INSTEAD OF PROVE` has now succeeded: the comparison architecture that powered runs 3--6 is invalidated at its rate input. Continuing to factor more covariance polynomials against this family would be wasted work until the reference exponent is correctly bounded.

The next run should not repeat B8/B19/B26. A useful fresh triple is **B1 / B12 / B30**:

- **B1 (change category):** move from pointwise covariance comparison to spectral-measure / persistence-variational bounds that do not require an exact unknown comparator exponent;
- **B12 (find what is conserved):** independently re-derive which of Molchan's spectral duality identities survive without Lemma 1.5, before using them as constraints on `theta_{2,H}`;
- **B30 (localize):** return to one source-valid point such as `H=1/4` and seek a direct quantitative improvement of the verified interval `[1/8,1/4]`, with every external theorem independently checked.

Because this recovery changed the obstruction itself, I do not manufacture a second STUCK report in the same invocation. If the corrected source metric remains unchanged through the required number of subsequent genuine attempts, Section I should be invoked again.

## 9. Capability honesty / scheduler controls

The interface exposed to this run still provides task prompt/title/schedule/timing/enabled controls but no model-family selector, no reasoning-effort selector, no authenticated model telemetry beyond the runtime identification stated on line 1, and no guaranteed execution duration. GPT-6 maximum is therefore prompt-requested only and cannot be honestly claimed here.

The repository ledger's historical permission nuance also remains: a P26 modification was denied in one context with `You cannot modify this task` and later succeeded from an authorized context. The legitimate workaround is the task-owning/authorized workspace or account context (or platform support), not cloning or bypassing ownership. This run was explicitly prohibited from modifying/creating schedules, so no scheduler edit was attempted.

## 10. Bookkeeping / ledger delta

No new finite-enumeration claim was made, so no artificial checker/output pair was created. The proof is analytic and written in full above.

```yaml
ledger_delta:
  track: HARD7-05
  source_id: MOLCHAN-2025-THETA2H
  status: PARTIAL
  recovery_stage: RECOVERY1
  source_problem: OPEN
  metric: W_{1/4}
  before: 0  # prior track value, now invalidated
  after: 1/8  # restored verified source gap
  movement: negative correction
  methods: [B8, B19, B26]
  route_status: REFUTED_AS_WRITTEN
  refuted_object: Molchan-v11-Statement-1.4 exact comparator rate and HARD7-05 consequences depending on it
  source_target_refuted: false
  prior_track_theta_claims_retracted:
    - theta_2_1_over_4_equals_1_over_8
    - theta_2_1_over_3_equals_1_over_6
    - exact_H_neighborhoods_from_those_anchors
    - theta_2_1_over_5_equals_1_over_10
  theorem_this_run: vartheta(h)/h -> 1 for K_h(t)=cosh((2h-1)t/2)/cosh(t/2)
  finite_checker_added: false
  next_methods: [B1, B12, B30]
```

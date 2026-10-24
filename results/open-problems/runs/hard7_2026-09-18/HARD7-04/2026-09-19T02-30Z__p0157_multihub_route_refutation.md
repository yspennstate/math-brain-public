Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-04 metric movement on the STUCK1 stress family: `Q_m` UNEVALUATED -> `m^{-1}+O(m^{-2}) -> 0`; methods B3 / B14 / B25.**

# HARD7-04 bounded research iteration — P0157 multi-hub route refutation

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source residual OPEN. The over-strong universal one-hub route statement is REFUTED.** This is the substantive continuation of the preceding Section-I STUCK1 recovery. The recovery choice was `REFUTE INSTEAD OF PROVE`; in this run that choice succeeds. I do **not** label the source problem REFUTED, because the source's 2026 prose prediction does not state the universal quantifiers of the route statement attacked here.

## 1. Continuity, ownership, and repository state

I resumed canonical claim `operations/claims/P0157.md`, owned by HARD7-04. I did not restart admission and did not return to candidate I0049.

Before the new mathematics I reread/recovered the controlling and fleet state required by the owner:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0157.md`;
- all indexed HARD7-04 P0157 checkpoints, especially the newest `runs/hard7_2026-09-18/HARD7-04/2026-09-19T01-27Z__p0157_stuck1_multihub_quantifier.md`;
- the existing route theorem `artifacts/hard7_2026-09-18/HARD7-04/p0157_finite_population_hub_lln.md`;
- newest neighboring HARD7-03 checkpoint `runs/hard7_2026-09-18/HARD7-03/20260919T0136Z__d0025-recovery2-sly-cusp-plateau.md`;
- newest neighboring HARD7-05 checkpoint `runs/hard7_2026-09-18/HARD7-05/2026-09-19T0138Z_theta_fifth_exact.md`;
- the P0157 intake/catalog entries and repository-wide P0157 ownership/alias searches.

The large intake collections are too large to render literally in one connector response, so I used their indexed P0157 entries plus canonical-claim and alias searches rather than falsely claiming a byte-for-byte full-file read. No release, duplicate canonical owner, posted equivalent, or claim collision surfaced. P0157 remains exclusively assigned to HARD7-04.

## 2. Source and current-literature refresh

Primary source retained: Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The page was rechecked visually. It recalls the strictly subcritical high-degree behavior, predicts that behavior sufficiently far below criticality / for sufficiently large maximum degree, contrasts it with the Erdos--Renyi barely-subcritical scale near the critical window, and says this suggests a phase transition within the subcritical regime in the finite-third-moment setting. It is predictive prose rather than a displayed theorem with universal quantifiers over every finite-third-moment degree sequence.

A bounded literature refresh dated 2026-09-19 again recovered:

- S. Janson, *The largest component in a subcritical random graph with a power law degree distribution*, Ann. Appl. Probab. 18 (2008), DOI `10.1214/07-AAP490`;
- M. Coulson and G. Perarnau, *Largest component of subcritical random graphs with given degree sequence*, Electron. J. Probab. 28 (2023), arXiv `2111.11780`, DOI `10.1214/23-EJP921`.

No surfaced paper was identified as proving or refuting the exact universal route statement below, nor as giving this explicit many-hub construction. This is bounded negative evidence only, not a novelty certification or proof of worldwide openness.

## 3. Frozen quantity — verified before/after

The canonical frozen quantity remains

\[
Q_n:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
    =\frac{\sigma_n^2}{d_{\max}\delta_n},
\qquad \delta_n:=1-\nu_n>0.
\]

The preceding STUCK1 report had introduced an explicit three-level stress family but had **not evaluated `Q_n` on that family**. Thus the source-relevant before value for that stress test was:

\[
Q_m=\text{UNEVALUATED}.
\]

This run proves, with the exact family below,

\[
\boxed{Q_m=m^{-1}+O(m^{-2})\longrightarrow0.}
\tag{3.1}
\]

So the frozen quantity genuinely moves on the chosen explicit family:

\[
\boxed{\text{UNEVALUATED}\ \longrightarrow\ m^{-1}+O(m^{-2})\to0.}
\]

This matters because it shows that the counterexample mechanism is **not** failure of the local hub branching process to self-average. The local metric is as favorable as possible; the failure is a global quantifier/multiplicity effect.

The exact symbolic checker and archived output are

- `artifacts/hard7_2026-09-18/HARD7-04/p0157_multihub_family_exact.py`;
- `artifacts/hard7_2026-09-18/HARD7-04/p0157_multihub_family_exact.out`,

with output ending `ALL_EXACT_CHECKS_PASS`.

## 4. Exact route statement attacked

The preceding route needed the stronger statement

\[
\boxed{
\forall\varepsilon>0:\quad
\mathbb P\!\left(
L_1>(1+\varepsilon)\frac{d_{\max}}{\delta_n}
\right)\longrightarrow0
\quad\text{whenever}\quad
\frac{d_{\max}\delta_n}{\log(n\delta_n^3)}\longrightarrow\infty,
}
\tag{R}
\]

under the finite-third-moment barely-subcritical hypotheses. Statement (R) is **our universal route formalization, not a verbatim source conjecture**.

This run proves (R) false.

## 5. The explicit finite-third-moment family

Let `m` run through even integers tending to infinity. Define

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\]

\[
x=3m^{11}+\frac{m^5}{4}(m^2-1)^2,
\]

and the degree counts

\[
N_d=M,\qquad N_3=2m^{12}-x,\qquad N_1=6m^{12}+x-M.
\tag{5.1}
\]

For large even `m` these are nonnegative integers summing to `n`; the total degree is even. Exact simplification gives

\[
\ell_m
=\frac{m^5}{2}(24m^7-12m^6-m^4+4m^2-3),
\tag{5.2}
\]

and

\[
\ell_m-\sum_i d_i(d_i-1)=12m^{11}.
\tag{5.3}
\]

Therefore

\[
\delta_m
=\frac{24m^6}{24m^7-12m^6-m^4+4m^2-3}
\sim\frac1m.
\tag{5.4}
\]

The empirical degree law converges to

\[
P(D=1)=3/4,\qquad P(D=3)=1/4,
\]

so `p_2=0<1`. Moreover the empirical third moment converges exactly to

\[
\frac1n\sum_i d_i^3\to\frac{15}{2}<\infty,
\tag{5.5}
\]

while the hub contribution itself is `Md^3/n=1/(8m)->0`. Hence the high-degree population is invisible to the limiting third moment.

Also

\[
n\delta_m^3\sim8m^9\to\infty,
\qquad
d\delta_m\sim m\to\infty.
\tag{5.6}
\]

For

\[
H_m=d/\delta_m,
\qquad
E_m=\delta_m^{-2}\log(n\delta_m^3),
\]

we have

\[
\frac{H_m}{E_m}
=\frac{d\delta_m}{\log(n\delta_m^3)}
\sim\frac{m}{9\log m}\to\infty.
\tag{5.7}
\]

So this family lies decisively on the nominal one-hub side of the two-scale comparison.

The forward-offspring variance satisfies `sigma_m^2->1`, which yields (3.1).

## 6. B25 — count the same matching pairs twice

The `M` hubs carry

\[
S=Md=m^7
\]

half-edges. Let `X_raw` count matched pairs with both half-edges in the hub half-edge set, allowing same-hub self-pairs. Uniform perfect matching gives the exact identities

\[
E X_{raw}=\frac{\binom S2}{\ell_m-1}=:\mu_{raw},
\tag{6.1}
\]

and

\[
E[X_{raw}(X_{raw}-1)]
=\frac{6\binom S4}{(\ell_m-1)(\ell_m-3)}.
\tag{6.2}
\]

The exact checker verifies

\[
\mu_{raw}\sim \frac{m^2}{24},
\qquad
\frac{E[X_{raw}(X_{raw}-1)]}{(E X_{raw})^2}\to1.
\tag{6.3}
\]

Since `mu_raw->infinity`,

\[
X_{raw}/\mu_{raw}\xrightarrow{L^2}1.
\tag{6.4}
\]

The expected number `Y` of hub self-loops is

\[
E Y=\frac{M\binom d2}{\ell_m-1}\sim\frac1{24m^3}\to0.
\tag{6.5}
\]

Thus for `X=X_raw-Y`, the number of direct edges between distinct hubs,

\[
\boxed{X/\mu\xrightarrow{P}1,\qquad
\mu=\frac{\binom M2d^2}{\ell_m-1}\sim\frac{m^2}{24}.}
\tag{6.6}
\]

In particular many direct hub-hub edges occur whp.

At the same time, a **preselected** hub has expected direct hub degree only

\[
\frac{(M-1)d^2}{\ell_m-1}\sim\frac1{12m^3}\to0.
\tag{6.7}
\]

This cleanly exhibits the quantifier swap diagnosed in STUCK1: each fixed hub is asymptotically isolated, while somewhere among `m^5` hubs many mergers occur.

## 7. B14 — use exchangeability and contract one conditioned hub edge

Fix two distinct hubs `u,v` and one specified half-edge at each. Condition on those two half-edges being matched. Delete the matched pair and contract `u,v` into a super-root `w`. By uniform-matching exchangeability, the remaining pairing is exactly uniform on the remaining half-edges; hence the contracted graph is exactly a configuration model on the transformed deterministic degree sequence with

\[
d_w=2d-2.
\tag{7.1}
\]

Let `ell_m^*=ell_m-2` and let `delta_m^*` be the transformed subcriticality parameter. Exact algebra gives

\[
\ell_m^*\delta_m^*
=12m^{11}-2m^4+8m^2-8,
\tag{7.2}
\]

so

\[
\delta_m^*/\delta_m\to1.
\tag{7.3}
\]

The transformed sequence still satisfies a uniform `sum d_i^3=O(n)` bound; replacing two degree-`d` vertices by one degree-`2d-2` vertex changes the third-moment sum by only `O(d^3)=O(m^6)=o(n)`. Also

\[
(n-1)(\delta_m^*)^3\to\infty,
\qquad
(2d-2)\delta_m^*\to\infty.
\tag{7.4}
\]

Therefore the already established finite-population maximal-root theorem in

`artifacts/hard7_2026-09-18/HARD7-04/p0157_finite_population_hub_lln.md`

applies to the super-root and gives

\[
\frac{|C^*(w)|}{(2d-2)/\delta_m^*}\xrightarrow{P}1.
\tag{7.5}
\]

Undoing the contraction adds one vertex. Conditional on the specified cross-hub edge,

\[
\boxed{\frac{|C(u)|}{H_m}\xrightarrow{P}2.}
\tag{7.6}
\]

The conditional law is identical for every specified cross-hub half-edge pair by symmetry.

## 8. B3 — prove the stronger obstruction: a `>3H/2` component exists whp

Let

\[
p_m=P\!\left(|C(u)|\le\frac32H_m\mid e\right),
\]

where `e` is any specified matched cross-hub half-edge pair. Equation (7.6) gives `p_m->0`.

Let `B` count direct distinct-hub edges whose endpoint component has size at most `3H_m/2`. Enumerating candidate cross-hub half-edge pairs, each candidate is matched with probability `1/(ell_m-1)` and, conditional on matching, is bad with probability `p_m`. Hence exactly by linearity,

\[
E B=\mu p_m=o(\mu),
\tag{8.1}
\]

with `mu` from (6.6).

Let `G=X-B` be the number of good direct hub edges. If `G=0` and `X>=mu/2`, then `B>=mu/2`. Consequently

\[
P(G=0)
\le P(X<\mu/2)+P(B\ge\mu/2).
\tag{8.2}
\]

The first term tends to zero by (6.6), while Markov and (8.1) give

\[
P(B\ge\mu/2)\le2p_m\to0.
\tag{8.3}
\]

Therefore

\[
\boxed{P(L_1>3H_m/2)\to1.}
\tag{8.4}
\]

But (5.7) has `H_m/E_m->infinity`. Statement (R), with `epsilon=1/2`, predicts the probability in (8.4) tends to zero. Thus:

\[
\boxed{\text{The universal one-hub route statement (R) is REFUTED.}}
\]

The complete on-page proof is preserved separately in

`artifacts/hard7_2026-09-18/HARD7-04/p0157_multihub_route_refutation.md`.

## 9. What the source problem now has to contain

The failed route shows that `d_max` and `delta_n` alone cannot parameterize a universal finite-third-moment largest-component law. A source-matching theorem needs information about **multiplicity and interaction of the upper degree tail**.

A direct-edge statistic already visible here is

\[
\Lambda_{dir}=\frac{M_nd_n^2}{\ell_n},
\]

the expected direct hub degree for a chosen hub among `M_n` comparable hubs. In this construction `Lambda_dir->0` but `M_n Lambda_dir->infinity`, so local isolation coexists with global merging.

The next genuinely new direction is to replace the one-hub scalar comparison by a high-degree **connection kernel** in which indirect subcritical explorations can connect hubs. The first-order heuristic scale is

\[
p_{hub}\asymp\frac{d_i d_j}{\ell_n\delta_n},
\tag{9.1}
\]

but (9.1) is **not proved in this run**. A rigorous derivation could produce a multi-hub random graph/coalescent whose component masses, multiplied by the one-hub scale `1/delta_n`, govern the largest components. That would turn the source's vague “phase transition” into a higher-dimensional crossover object rather than a scalar equality `H_n~E_n`.

Next unused section-B triple: **B7 TAKE THE LIMIT, B19 MAKE IT AN ALGORITHM, B29 ADD THE POINTS AT INFINITY**. Concretely: derive the limiting hub-connection kernel, encode joint explorations constructively, and include the boundary where the number of near-maximal hubs diverges while each individual connection probability vanishes.

## 10. Verification and capability honesty

The finite algebra was checked with exact symbolic arithmetic. The archived output verifies

- `m delta_m ->1`;
- empirical third moment `->15/2`;
- `sigma_m^2->1`;
- `m Q_m->1`;
- `n delta_m^3/m^9->8`;
- `d delta_m/m->1`;
- `delta_m^*/delta_m->1`;
- conditioned two-hub scale divided by `H_m ->2`;
- direct hub-pair mean divided by `m^2 ->1/24`;
- self-loop mean times `m^3 ->1/24`;
- raw matching second-factorial-moment ratio `->1`;
- final line `ALL_EXACT_CHECKS_PASS`.

The theorem-sized probabilistic argument is written on the page; the checker certifies only its finite algebraic core. The contraction/one-hub step reuses HARD7-04's earlier self-checked route theorem and therefore is **not an independent audit**. Closure protocol is not invoked.

Scheduler capability remains unchanged in the exposed interface: title, prompt, schedule/timing mode and enabled state are available, but there is **no model selector, reasoning-effort selector, or guaranteed run duration**. GPT-6/maximum is therefore only requested in prompt text. This invocation identifies as GPT-5.6 Sol; authenticated reasoning-effort telemetry is unavailable, so the reasoning level is UNVERIFIED. A true scheduler-side GPT-6/maximum guarantee would require the platform/product interface to expose and honor model and reasoning selectors; a repository edit cannot provide that.

The earlier recorded `You cannot modify this task` result for a P26 scheduler ID was a permission/context failure, not a mathematical issue. The current root ledger also preserves evidence that P26 was later successfully updated in another authorized context. The correct workaround for a denied native task is to use an authorized account/workspace/context or platform support, not to bypass permissions or create a duplicate schedule. I did not create, modify, disable, or reactivate any schedule in this run.

## 11. Checkpoint / ledger delta

```yaml
ledger_delta:
  track: HARD7-04
  target: P0157
  source_status: OPEN
  worker_status: PARTIAL
  route_statement_status: REFUTED
  frozen_quantity: Q_n = sigma_n^2/(d_max*delta_n)
  before_on_stress_family: UNEVALUATED
  after_on_stress_family: Q_m = m^-1 + O(m^-2) -> 0
  substantive_result: "explicit finite-third-moment barely-subcritical family with H/E->infinity but P(L1>3H/2)->1"
  exact_family: "degrees 1, 3, m^2; n=8m^12; M=m^5 hubs; delta_m~1/m"
  methods: [B3, B14, B25]
  checker: artifacts/hard7_2026-09-18/HARD7-04/p0157_multihub_family_exact.py
  checker_output: artifacts/hard7_2026-09-18/HARD7-04/p0157_multihub_family_exact.out
  theorem_artifact: artifacts/hard7_2026-09-18/HARD7-04/p0157_multihub_route_refutation.md
  stuck_recovery: "STUCK1 recovery choice REFUTE_INSTEAD_OF_PROVE succeeded; route obligation changes"
  next_obligation: "derive a rigorous high-degree connection kernel / multi-hub scaling object; do not return to universal L1~dmax/delta route"
  next_methods: [B7, B19, B29]
```

No root shared ledger is edited by this worker; the structured delta above is the handoff for the designated shared-ledger maintainer. No email or Drive action was taken.

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but authenticated runtime metadata does not establish GPT-6/maximum, so I do not claim it. **NO SOURCE-METRIC MOVEMENT:** Salez Problem 2.3 remains OPEN and historical `W_exp=1/2 provisional`; this run proves an exact two-scale/L2 theorem and a stronger obstruction showing why L2 cannot be the missing TV mechanism. Three nonexhausted approaches compared: **exact spectral plateau (success auxiliary), quiet-gap regeneration (refuted), multi-translation Feynman--Kac/epoch resolvent (structural progress but quantitatively insufficient).**

# PROB10-08 — exact heat-kernel L2 obstruction on a source-admissible affine expander

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / OPEN / auxiliary theorem proved / no TV cutoff theorem / independent validation pending / worldwide novelty UNVERIFIED**.

## 0. Contract recovery and consumed state

Required state was read before research:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- current `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`; the posted Abelian Cayley/product-condition paper remains excluded and is not this target;
- `operations/claims/I0112.md`, blob `707af6a4ca81d0d6bcf52225c6f69c266ae981e9`;
- preserved R16 successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, blob `fa18fa8669a638c362ad0f90300b733425e808e5`;
- newest own predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T03-00-00Z_affine-sx-green-obstruction_9c21.md`, blob `47fdaaf2a41b0982094c10ad9af2e73b8b1bd96e`;
- newest related P26 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_05-56-17__distance-set-shell-profile-transfer.md`.

The historical I0112 chain was recovered through the R16 handoff: product-varentropy, synchronous tensor, moving-window/local-Poincare, Hecke/information-curvature and tree-subcommutation are exhausted and were not restarted. P26/NM13 currently own finite-fiber, line-graph, graph-square/distance-shell and twisted/local-state transfer directions, so none was repackaged here.

Pre-write master observed at `3e675fe1aed142c6e1c41f86af62918338ed6e02`; concurrent fleet writes were treated as normal and only unique create-only paths were used.

## 1. Fresh source/current-status check

The source is still Salez, arXiv:2508.21055v1, Problem 2.3, under his rate-one continuous-time SRW convention: all bounded-degree vertex-transitive expander sequences should exhibit total-variation cutoff.

Altschuler, arXiv:2609.14945, is still v1 dated 14 September 2026 in the current arXiv record; a bounded correction/erratum search found no v2 or correction. His theorem remains fixed-degree long-range-expander cutoff, with LRE strictly stronger than spectral expansion. Its proof uses LRE to force near-maximal NBRW endpoint Shannon entropy before spectral entropy cleanup.

The Haiman--Schildkraut--Zhang--Zhao source was reread at arXiv:2109.13131v3 / BLMS 54 (2022). The crucial exact fact not used in the predecessor is in their proof of Theorem 1.4: the 16-regular `SL(2,q)` lift has spectrum exactly twice that of the 8-regular LPS Ramanujan base, plus zeros. Thus its entire nontrivial adjacency spectrum lies in `[-4 sqrt(7),4 sqrt(7)]`.

A bounded search for the exact Haiman affine family together with cutoff/L2 mixing returned the multiplicity paper itself but no theorem matching the auxiliary result below. This is not a novelty certificate.

## 2. Idea before calculation

The preceding run showed that the affine Haiman family is an admissible transitive spectral expander but has polynomially excessive NBRW collision at the ambient tree radius. The question this run was whether that was merely an NBRW artifact.

It is not. The exact lifted LPS spectrum gives a **single slow irreducible plateau plus a uniformly faster bulk** for the actual SRW heat kernel. This makes the true continuous-time chi-square distance exactly analyzable. The outcome is stronger than the predecessor's obstruction: the actual heat kernel is polynomially far from uniform in L2 at the fastest tree/Ramanujan TV scale, while its own L2 transition occurs more than a factor 4.5 later. Hence any proof of Salez 2.3 must be genuinely Shannon/typical-mass rather than L2.

## 3. Main auxiliary theorem proved this run

Freeze the same pure-translation Haiman family from the predecessor:

`Gamma_q=SL(2,q) semidirect F_q^2`,

`G_q=Cay(Gamma_q,S union {t,t^{-1}})`, `t=(I,e)`,

`N_q=q^3(q^2-1)`, `m_q=q^2-1`, degree `18`.

Let `mu_q` be the second adjacency eigenvalue. Put

`beta=2+4 sqrt(7)`,

`gamma_bulk=(16-4 sqrt(7))/18`.

The complete proof in the matching artifact establishes:

1. all nontrivial eigenvalues other than `mu_q` are at most `beta`;
2. `mu_q` has **exact multiplicity** `m_q=q^2-1`;
3. with
   `mu_bar=lambda_max([[16,sqrt(2)],[sqrt(2),beta]])`,
   one has
   `16-2/m_q <= mu_q <= mu_bar<18`;
4. hence, for `delta_q=1-mu_q/18`,
   `delta_- <= delta_q <= (1+1/m_q)/9` for a fixed `delta_->0`.

For Salez's rate-one semigroup `H_t=exp(t(P-I))`, vertex transitivity gives the exact heat-kernel trace identity

`chi_q^2(t)=sum_{i=2}^{N_q} exp(-2(1-lambda_i(P))t)`.

Therefore

`m_q e^{-2 delta_q t}`

` <= chi_q^2(t)`

` <= m_q e^{-2 delta_q t}+(N_q-m_q-1)e^{-2 gamma_bulk t}`.       (3.1)

Set

`t_q^(2)=(log m_q)/(2 delta_q)`.

The bulk term at this time is

`N_q m_q^{-gamma_bulk/delta_q}`,

and

`gamma_bulk/delta_q >= (8-2sqrt(7))/(1+1/m_q)`.

Since

`5-2(8-2sqrt(7))=4sqrt(7)-11<0`,

the bulk term is `o(1)`. Thus for each fixed `s`,

`chi_q^2(t_q^(2)+s)=e^{-2 delta_q s}+o(1)`.                      (3.2)

Consequently the continuous-time walk has **L2 cutoff with an O(1) window**:

`t_{2,q}(epsilon)=t_q^(2)+O_epsilon(1)`,

so the L2-window/center ratio is `O(1/log N_q)`.

This is a complete auxiliary theorem, not a total-variation cutoff theorem.

## 4. Stronger source-relevant obstruction

For degree 18 the fastest tree/Ramanujan benchmark is

`T_q=(9/8) log_17 N_q`.

The slow plateau in (3.1) gives

`chi_q^2(T_q) >= N_q^{2/5-1/(4 log 17)+o(1)} -> infinity`.        (4.1)

Moreover,

`liminf t_q^(2)/T_q >= (8/5)log 17 = 4.533...`.                  (4.2)

So the failure of near-uniform collision in the predecessor is not confined to NBRW. The **actual continuous-time SRW heat kernel** remains polynomially nonuniform in chi-square at the fastest possible TV scale.

This does not lower-bound TV: a tiny exceptional set can dominate chi-square while carrying vanishing total mass. That distinction is exactly why the source remains open. But it rules out a broad family of attempted proofs: transitivity plus spectral expansion cannot be converted to TV cutoff through a uniform L2/chi-square estimate at the relevant scale.

## 5. Approach 2 — single quiet-gap regeneration: refuted

The predecessor's semidirect Feynman--Kac identity suggested waiting for a translation-free interval, mixing the subgroup direction `M e`, and using the next translation as a refresh of the additive coordinate.

Translation events have independent rate `1/9`. On any fixed `C log q` time horizon there are `O(log q)` translation gaps, and for every `K>9`,

`P(max gap > K log log q) -> 0`.

During each such gap there are only `O(log log q)` subgroup `S`-moves uniformly over all gaps with probability tending to one. Starting from a fixed subgroup state, `O(log log q)` moves can put `M e` in at most `16^{O(log log q)}=(log q)^{O(1)}` positions, whereas the stationary orbit has `q^2-1` positions. Thus every available quiet gap leaves the direction at TV distance `1-o(1)` from uniform.

Hence a **single-quiet-gap regeneration cannot work on any logarithmic physical-time scale**. This is an exact support-growth obstruction, not a numerical observation.

## 6. Approach 3 — multi-translation epoch resolvent: structural progress, still quantitatively too weak

Between two translation events, the subgroup walk takes a geometric number of `S`-steps. If `P_S=A_S/16`, the exact epoch operator is

`R=(9I-8P_S)^{-1}`.

Because the nontrivial subgroup spectrum is in `[-sqrt(7)/4,sqrt(7)/4]`,

`||R||_{1^perp} <= r_0:=1/(9-2sqrt(7))=0.26965...`.

For a nontrivial additive character, sign averaging contributes the multiplier

`C_xi(M)=Re chi_xi(M e)`,

with uniform moments

`E C_xi=-1/(q^2-1)`,

`E C_xi^2=(q^2-2)/(2(q^2-1))<1/2`.

On the constant/mean-zero decomposition, `R M_{C_xi}` is dominated by

`[[1/m_q,1/sqrt(2)],[r_0/sqrt(2),r_0]]`,

whose operator norm is `<0.8` for all sufficiently large `q` (indeed its limiting Frobenius bound is about `0.780`). Thus the correlated translation epochs have a genuine uniform contraction.

But using this through ordinary Fourier/Parseval still pays for the `q^2` characters and point-mass L2 cost, so it produces only a late L2-type estimate. It does not approach the needed TV scale. The missing ingredient is now very specific: a **Shannon/typical-mass estimate for the multi-translation operator that harvests subgroup bridge randomness without paying the L2 norm**.

An entropy-budget check reinforces this. At `T_q`, if the whole ordered `S`-generator sequence is exposed, the remaining event-type/sign randomness contributes only

`[h(1/9)+(1/9)log2] T_q = 0.84547... log q+o(log q)`,

far short of the `2 log q+o(log q)` entropy of a uniform `F_q^2` coordinate. Any successful affine entropy proof must use the subgroup **bridge** randomness itself; conditioning it away is quantitatively fatal.

## 7. Source before/after and metric accounting

**Before:** Salez Problem 2.3 OPEN; `W_exp=1/2 provisional`. The predecessor made no TV graph-class/window improvement but proved a source-admissible Sarnak-Xue/NBRW-collision obstruction.

**After:** Salez Problem 2.3 remains **OPEN**; `W_exp` remains `1/2 provisional`. No new total-variation cutoff graph class is claimed, so there is **no source-metric movement**.

**Auxiliary changes, proved separately:** exact slow-eigenvalue multiplicity; uniform bulk spectral bound; O(1)-window continuous-time L2 cutoff for the affine family; polynomial actual-heat-kernel chi-square obstruction at the tree benchmark; refutation of single-gap regeneration; exact epoch-resolvent reduction.

This is the second consecutive own PROB10-08 run whose source-level TV metric does not move. It already changes method and writes the obstruction as required; another unchanged iteration should not continue sharpening L2 constants and instead must attack the bridge-entropy problem or another genuinely different TV mechanism.

## 8. Proof artifact and tests

Full analytic proof and assumptions:

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T03-58-30Z_affine-l2-spectral-barrier_d4c7.md`

created at commit

`a718aab34239cdea2b19f2fad979293c2c03fc6a`

and read back at that exact commit (blob `bdca7ade9c542f830ec1b734f0270065e70d5ceb`).

No finite mixing plot was run or used. A local symbolic/numerical sanity check evaluated only constants appearing in exact inequalities (`beta`, `gamma_bulk`, `mu_bar`, `delta_-`, `4sqrt(7)-11`, and the factor `(8/5)log17`). Every sign in the proof has an exact elementary justification; there is no finite computational core requiring a certificate.

## 9. Remaining full-scope obligation

For the affine stress test, prove a Shannon/varentropy estimate for the joint `(M_t,X_t)` law that transfers roughly `2 log q` bits/nats of subgroup bridge randomness into the additive coordinate on the TV mixing scale, despite the polynomial L2 excess. More generally, solve Salez 2.3 by a mechanism that is insensitive to precisely this kind of high-multiplicity, low-mass spectral pollution.

The old R16/H0002 successor remains preserved in the existing handoff and was not modified. No scheduler setting, cadence, enabled state, shared root ledger, peer-track file, email, Drive object, public posting, permission, workflow, or force push was changed.

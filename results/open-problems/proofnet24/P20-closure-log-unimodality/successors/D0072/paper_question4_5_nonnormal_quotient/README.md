# Grimmett–Li Question 4.5: a non-normal quotient not arising from any normal transitive quotient

Status: **internal source-matching closure package; mathematical answer YES; publication novelty UNVERIFIED; no public posting claimed.**

Owner track: P20.

Outside source: Geoffrey R. Grimmett and Zhongyang Li, *Self-avoiding walks and connective constants*, arXiv:1704.05884v2 (11 July 2019), later Springer Proceedings in Mathematics & Statistics 300 (2020), Section 4.2, Question 4.5.

## Exact source question addressed

Let `G` be an infinite, simple, locally finite, transitive rooted graph and let `Gamma <= Aut(G)` act transitively. Question 4.5 asks whether there can exist a non-normal subgroup `A <= Gamma` such that

1. the quotient graph `G_A` is transitive; and
2. there is no normal subgroup `N` of any transitively acting `Gamma' <= Aut(G)` for which `G_N` is isomorphic to `G_A`.

The source separately asks whether it may be relevant to assume that `A` acts freely. The witness below in fact has `A` acting freely.

## Witness

Let

- `Lambda = S_3 * A_5`;
- `pi: Lambda -> S_3` be identity on the `S_3` factor and trivial on the `A_5` factor;
- `H = <(12)> < S_3`;
- `A = pi^{-1}(H)`;
- `S_* = (S_3 \ {1}) union (A_5 \ {1})`.

Leemann–de la Salle, *Cayley graphs with few automorphisms: the case of infinite groups*, Annales Henri Lebesgue 5 (2022), Theorem 1.1 together with Theorem 3.1, Proposition 3.2 and the proof of Theorem 1.1, gives a finite symmetric generating set `S` containing the prescribed finite symmetric set `S_*` such that

`G = Cay(Lambda,S)`

has full automorphism group equal to the left-regular translation group `Lambda_L`.

Take `Gamma = Lambda_L` and identify `A` with its subgroup of left translations.

Then:

- `A` is non-normal because `H` is non-normal in `S_3` and `pi` is onto;
- `A` acts freely because every subgroup of a regular action acts freely;
- `G_A` has the three left cosets of `H` as vertices, and because every nonidentity element of the `S_3` factor remains a generator, every two distinct quotient vertices are adjacent, so `G_A ~= K_3`;
- every transitive subgroup of `Aut(G)=Lambda_L` equals the whole regular group `Lambda_L`;
- if a normal subgroup produced `K_3`, it would have index three and give a quotient `Lambda -> C_3`;
- but `(S_3*A_5)^ab ~= S_3^ab x A_5^ab ~= C_2`, so no such `C_3` quotient exists.

Thus both source conditions hold, including the universal quantifier over all transitively acting `Gamma' <= Aut(G)`. The answer to the literal source Question 4.5 is YES.

## Canonical proof and exact finite core

Canonical P20 proof report:

`proofnet24/P20-closure-log-unimodality/successors/D0072/runs/2026-09-17/2026-09-17T16-18-23Z__run-report.md`

creation commit `92b25a56025b3e0905274c554a4104d4acbc0685`.

Original exact finite checker:

`proofnet24/P20-closure-log-unimodality/successors/D0072/artifacts/2026-09-17/2026-09-17T16-17-30Z__finite_core.py`

creation commit `144f18a4da6d45581d79bb91d91af14b556cedde`.

Original checker output:

`proofnet24/P20-closure-log-unimodality/successors/D0072/artifacts/2026-09-17/2026-09-17T16-17-30Z__finite_core.out`

creation commit `14db9090c2e88788c9381cef3246d0d1415d53c8`, ending `ALL_EXACT_CHECKS_PASS`.

This package copies the exact checker and exact output as `check.py` and `check.out`. The checker verifies only the finite `S_3/A_5` core. The free-product and graphical-regular-representation steps are theorem-sized and are proved/cited in `main.tex` rather than misrepresented as machine-checked.

## Independent audits: 2/2 complete

Distinct full-proof audits of the canonical `K_3` source witness:

1. P19: `P19-AUDIT-P20-D0072-ENDTOEND-23 = PASS`, report
   `proofnet24/P19-closure-smr-optimal/runs/2026-09-17/2026-09-17T17-56-34Z__rotation-hold-d0072-audit.md`, creation commit `8debd604cb2090d04a64564ba6d29a8d70198bde`.
2. P26: `P26-AUDIT-P20-D0072-ENDTOEND-30 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_QUESTION_PASS / CLAIM_SCOPED_K3 / FINITE_CORE_INDEPENDENT_PASS / PRIOR_ART_UNVERIFIED`, report
   `proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_23-58-56__run-report.md`, creation commit `20863efed6afdd5f78a8832ca82e7a00f57f01de`.

P26's two-audit reconciliation is `P26-RECONCILE-P20-D0072-2OF2-30 = PASS`. P20 self-checks, the separate main-agent strengthening to other complete quotients, and repeated receipts are not counted as additional independent audits.

## Prior-art limitation

Bounded searches dated 2026-09-17 checked the Grimmett–Li source, exact wording around Question 4.5, later-author/citing literature, and the Leemann–de la Salle GRR paper. They recovered the original question and the 2022 GRR theorem but no later paper explicitly claiming resolution of the exact Question 4.5 quantifiers by this witness or another one. This is only bounded negative evidence. **Publication novelty is UNVERIFIED.**

## Scope discipline

This package certifies only the literal Grimmett–Li Question 4.5 witness above. It does not claim Question 4.6, a connective-constant inequality, the stronger all-`K_m` construction appearing elsewhere in the repository, or any public posting/publication result.

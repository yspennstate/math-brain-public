# Aldous–Fill Open Problem 2.34 — rooted-grove portmanteau package

Status: **PROVED / repository closure package complete; publication-level novelty remains UNVERIFIED.**

Outside source: David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs* (unfinished 2002 manuscript; 2014 recompilation), Chapter 2, Open Problem 2.34, “Portmanteau theorem for occupation times.” Intake: `I0023`.

## What the source asks

Section 2.2.2 lists eleven occupation/hitting identities (Lemmas 2.5–2.7, Corollary 2.8, Lemma 2.9, Corollary 2.10, Lemmas 2.11–2.12, Corollaries 2.13–2.14, Lemma 2.15). Open Problem 2.34 asks whether they can be formulated as a single theorem and, by analogy with Feynman diagrams, asks for a combinatorial structure attached to marked-state occupation expressions and a formal function of the marked stationary/fundamental-matrix data.

The exact source scope used here is a **finite-state irreducible discrete-time Markov chain**, not assumed reversible. “Visits before time `S`” includes time zero and excludes time `S`. For periodic chains, the source defines `Z` by the Cesàro (equivalently continuized) interpretation.

## What is proved

For every nonempty boundary `A`, let

```text
M_A = [[Z_A^T, -pi_A],
       [1^T,        0]],
Delta_A = det(M_A).
```

This is the denominator frozen by the P02 program. Let `F_A` be the total transition-weight of directed spanning forests converging to the root set `A`, and let `F_{A∪{j}}(i→j)` be the total weight of forests rooted at `A∪{j}` in which `i` lies in the component rooted at `j`. Let `T` be the total weight of all one-root converging spanning trees.

The package proves

```text
E_i[# visits to j before T_A]
    = F_{A∪{j}}(i→j) / F_A,
Delta_A = F_A / T,
N_{A;i,j} = F_{A∪{j}}(i→j) / T,
```

where `N_{A;i,j}` is the frozen bordered `(pi,Z)` numerator. Hence the same occupation quantity is counted twice: intrinsically by rooted groves and by the marked Aldous–Fill data.

More generally, for an integrable stopping time `T` whose terminal law is supported on `A`, initial law `sigma`, and boundary occupation vector `c=x_A`, put

```text
mu_q = sigma_q + sum_{a in A} c_a p_{a q},   q notin A.
```

Then

```text
x_j = E_sigma[# visits to j before T]
    = (1/F_A) sum_{q notin A} mu_q F_{A∪{j}}(q→j),
```

and this equals a single bordered determinant divided by the **same** `Delta_A`. The paper derives all eleven Section 2.2.2 identities from this one boundary-data theorem and treats the source prototype

```text
E_i[# visits to j before min(T_k,T_l)]
```

as the minimal two-boundary example.

## Files

- `main.tex` — self-contained theorem, proof, exact source-hypothesis statement, all eleven specializations, source prototype, and prior-art classification.
- `check.py` — exact-rational finite checker copied into the paper package from the already-verified P02 C5 artifact; it independently enumerates rooted forests and independently computes `pi`, `Z`, and the bordered determinants.
- `check.out` — archived output of that checker.

The checker is packaging of an existing verified certificate, not a new checker-only research run.

## Proof lineage and independent audits

Canonical theorem report:

- `proofnet24/P02-closure-occupation/runs/2026-09-16/2026-09-16_17-04-02__run-report.md`
- creation commit `8d40b5b3f5370e8209f63015a19b8a957be10e57`
- claim `P02-OCC-C5-ROOTED-GROVE-PORTMANTEAU = PROVED`.

Two genuinely distinct OTHER-track end-to-end mathematical/source audits now exist:

1. P26: `P26-AUDIT-P02-I0023-C5-ROOTED-GROVE-04 = PASS_MATHEMATICS / SOURCE_LITERAL_PASS / PRIOR_ART_UNVERIFIED`, creation commit `12bb57d37208bfc01baf494e46f6a87a4f1c90e4`.
2. P01: `P01-AUDIT-P02-I0023-C5-ROOTED-GROVE-74 = PASS_MATHEMATICS / SOURCE_LITERAL_PASS / PRIOR_ART_UNVERIFIED`, creation commit `77d2229b99e1eee42e0349facfbab14205514fac`.

P26 subsequently reconciled these as

`P26-RECONCILE-P02-I0023-C5-TWO-AUDITS-07 = PASS_2_OF_2_MATHEMATICAL_AUDITS / PRIOR_ART_UNVERIFIED / NOT_POSTED`.

## Prior-art posture

No novelty claim is made for the ingredients. In particular, Pitman (1977) gives a unified occupation-measure identity; directed matrix-tree/all-minors formulas are classical; Chebotarev–Agaev develop forest representations of Laplacian generalized inverses; Pitman–Tang give tree/forest formulas for finite-chain Green and hitting quantities; and Chung–Zeng give forest formulas for discrete Green functions on directed/weighted graphs.

The bounded literature searches recorded in the reports did **not** locate the exact package consisting simultaneously of (i) the frozen Aldous–Fill bordered `(pi,Z)` denominator, (ii) its rooted-grove interpretation, (iii) arbitrary stopping/boundary data, and (iv) one-rule accounting of the exact eleven Section 2.2.2 identities. That search failure is **not** a novelty certificate. Publication-level novelty therefore remains `UNVERIFIED` even though the source-level mathematics and repository closure requirements are complete.

No public posting is asserted by this folder.
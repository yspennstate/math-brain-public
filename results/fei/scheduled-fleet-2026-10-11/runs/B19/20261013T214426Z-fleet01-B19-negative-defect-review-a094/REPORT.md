# B19 / A094 — independent review of the negative point-defect tower

## Verdict

**ACCEPT THE THREE B05 CLAIMS AT THEIR FORMAL SCOPE, WITHOUT REPAIR.**

Review target:

- B05/A023 run `20261013T213434Z-fleet01-B05-negative-defect-retained-credit-a023`;
- canonical commit `9a6f9a8eeb3795ebdbeebf4efa767ed607af2897`;
- claims `B05_A023_NEGATIVE_DEFECT_BLOCK_v1`,
  `B05_A023_NEGATIVE_DEFECT_ENDPOINT_v1`, and
  `B05_A023_NEGATIVE_DEFECT_RETAINED_v1`.

For `N_r=-Q_r`, where `Q_r` is positive except at one point, and

\[
F_1=A(wP),\qquad F_k=A(N_{r_k}F_{k-1}),\qquad r_k\ge2,
\]

the source proof correctly establishes

\[
U(P)\le\frac{16}{9}I(P)
\Longrightarrow U(F_d)\le\frac{16}{9}I(F_d)
\]

for all finite depths and rank sequences.  Its adaptive/pruned physical-tree
bound with one common disjoint terminal factor is also correct.  The proof
accounts for the point-defect physical inputs and the selector influence; no
bias or normalization factor is missing.

## Stronger theorem found during review

The same argument closes at the smaller coefficient

\[
\boxed{c=\frac53}.
\]

Specifically,

\[
U(P)\le\frac53I(P)
\Longrightarrow U(F_d)\le\frac53I(F_d),
\]

and every permitted common-core tree has retained loss at most
`5I(F_d)/3`.  Hence

\[
\boxed{H(F_d)\le\frac{16}{3}I(F_d).}
\]

The improvement is proved in `STRENGTHENING.md`.  In outline:

1. Every negative point-defect block satisfies `U(N_r)<5I(N_r)/3`.
2. The exact mean recurrence gives `s_k=beta_k m_{k-1} in [1/8,1/2]`.
3. The accepted shape analysis of `R`, plus an independent derivative check,
   gives `R(-s)<=R(-1/8)<15/16`.
4. At `c=5/3`, the physical selector pays at least
   `c(1+s)/2 >= 15/16`.

Because B19 contributed this strengthening, it is
**AUTHOR PROVED PENDING FRESH A085/A090 REVIEW**.  It is not part of the
independent acceptance verdict for the original `16/9` claims.

## Independent computation

`CHECK.py` is independent in test selection and includes exact integer log
certificates, ranks 2 through 500, 200,001 scalar points, all 256 Boolean
three-bit bases with five tower patterns (1,280 direct towers), 613,181
nonstationary recurrence states, and 128 adaptive/pruned trees with terminal
tensor cancellation.  All tests passed; `CHECK.out` records the executed
counts.  The theorem itself is analytic.

## Tree scope

The tree theorem is exactly a signed endpoint telescope:

\[
U(F_dh)-\sum_lw_lU((F_d)_lh)
=U(F_d)-\sum_lw_lU((F_d)_l)\le U(F_d).
\]

It does not establish nonnegative node charges, a first-revelation stopping
rule, or single-use ownership of `mu[log(1/mu)-D]` credits.  It also does not
cover biased outer selectors, reused variables, or changing, overlapping, or
leaf-dependent cores.  The B05 scope ledger already states these limitations
correctly.

## Literature scope

O'Donnell--Tan proves FEI composition for disjoint inner blocks under a
product-biased outer hypothesis.  That theorem is compatible with the fresh
disjoint construction but does not state the upper-set potential `U`, the
one-sided scalar payment, or the adaptive retained-tree endpoint.

Potapov proves FEI for plateaued and partially bent functions.  It does not
supply this nonstationary activation recurrence or common-core retained-`U`
telescope.  No novelty or priority claim is made here.

## Remaining universal gap

The result remains a proper-class closure theorem whose base is already
assumed to satisfy an endpoint.  A023 still lacks a dimension-independent
first-revelation mismatch/KL payment for arbitrary changing or overlapping
coherent cores.  Full FEI remains **OPEN**.

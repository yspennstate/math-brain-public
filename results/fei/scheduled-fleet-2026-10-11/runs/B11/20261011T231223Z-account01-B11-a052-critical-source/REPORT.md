# B11 / A052 — critical descendants and tensor purity

**Status:** PROVED structural theorem, pending independent review. **Full FEI remains OPEN.**

## Frozen objective and prior status

Packet A052 asks for a structural restriction forced by true entropy/influence
ratio extremality under every allowed physical descendant, with the known raw
component-entropy and maximum-component-ratio failures replayed explicitly.
Before this run, A052 was `OPEN`, with no adopted artifact or attempt history.

The exact notion used here is: a nonconstant Boolean `f` is `eta`-critical if
every nonconstant coordinate restriction `g` satisfies
`R(g) <= R(f)+eta`, where `R=H/I`.  This is finite and attained for every fixed
truth table: select a maximum-ratio descendant.  No optimizer over all
dimensions is assumed.

## New theorem

For a disjoint physical tensor product `F=product_j f_j`, put
`w_j=I(f_j)/I(F)`.  If `F` is `eta`-critical, then

```
R(F) - ((1-w_j)/w_j) eta <= R(f_j) <= R(F)+eta,
```

and every physical descendant `u` of `f_j` satisfies

```
R(u) <= R(f_j) + eta/w_j.
```

Thus an exact critical tensor product has only critical factors, all with the
same ratio.  Conversely, a tensor product of equal-ratio critical factors is
critical.  The proof is the exact identity

```
R(F) = sum_j w_j R(f_j),
```

plus actual coordinate restrictions fixing all blocks but one.  Criticality is
used precisely at that physical-descendant comparison; it is not inferred from
support connectedness.

This is a real narrowing of decomposable extremizers.  It also gives a clean
deficit law: a factor with nonnegligible influence weight inherits quantitative
criticality.  It does not control factors of vanishing influence weight.

## Mandatory controls

- The pinned nine-bit raw-entropy witness compares connected support
  components, not physical descendants, so the criticality line is unavailable.
- The pinned seven-bit maximum-component-ratio witness is concretely
  noncritical: a two-coordinate restriction gives NAND2 with ratio more than
  `0.59` larger than the union.  Hence it does not refute this theorem.
- Criticality alone remains full-FEI hard.  Every Boolean source has a
  maximum-ratio critical descendant, and tensor powers of a critical core remain
  critical.
- Qualitative nonfactorization is insufficient.  Lifting an arbitrary core by
  unused variables and flipping one joint truth-table value produces a function
  that is not a product across the old/new split, while its entropy, influence,
  and ratio converge to those of the core.  Exact total-variation and boundary
  bounds are proved in `CRITICAL_SOURCE_STRUCTURE.tex`.

## Verification

Command:

```
python3 verify_criticality.py
```

The checker uses integer Walsh transforms and `Fraction` arithmetic for
Parseval, influence, tensor, and point-defect identities; it also checks finite
one-point-surgery witnesses.  Floating entropy values are diagnostics only.
The all-dimension result is the analytic proof in the TeX file.

## Source pins

- B11 contract blob `faaa0875ddb129d134bb62abb513f3795e88b590`, catalog
  hash `fd09039c4d5efe48fba1bc1652f6cd04183181db82912305d4354c1b2fa14f5b`.
- Component raw-entropy obstruction: Brain commit
  `5d7a75c0b7ae3aab71df5abdafc31832be81321b`, blob
  `fc36cb9447b4fc17c5ed49d8c6e98cf59d11f7eb`.
- Component ratio obstruction: same commit, blob
  `c76c486f8568aa53ee411c2fb1de0275b4037d72`.
- Reduction source `reports/fei-2026-10-11/source_material/reductions/paper/main.tex`,
  SHA256 `f8d454549fedbb688261d0181fe33b0c4f01be8d26d9c8a38cc1cc6d6a0b3153`.

## Exact remaining obstacle

The theorem handles exact tensor decompositions.  It does not prove that a
critical source decomposes or that a prime critical source has bounded ratio.
The next mathematical target is a quantitative near-tensor interface theorem:
an `eta`-critical function close to a tensor must either pay its interference
by physical influence or expose a higher-ratio descendant.  One-point surgery
shows that qualitative primitivity cannot supply this conclusion.

Route the proof to A054/A055 and independent reviewers A090/A094.  Acceptance
and downstream use are not claimed before independent review.

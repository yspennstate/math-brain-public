# Regime comparison

## Exact scope

The new statement applies only to genuine Boolean functions of exact
Fourier degree at most `d`.  It is not an approximate-degree theorem and
does not apply to bounded or nearly Boolean real functions.

| Route | Hypothesis | Entropy allowance |
|---|---|---|
| Support count | arbitrary degree `d` spectrum on `N` coordinates | at most `log2(sum_{k<=d} C(N,k))`, retaining a logarithmic dimension term |
| Real Bohnenblust--Hille | arbitrary real degree `d`, bounded sup norm | Renyi conversion retains the `C^{sqrt(d log d)}` factor |
| Boolean granularity | genuine Boolean, degree at most `d` | `H <= 2(d-1)v + (1-v)log2(1/(1-v))` |
| Influence corollary | same | `H <= (2(d-1)+log2(e)) I` |

Here `v=1-fhat(empty)^2`.  The final step uses `v<=I` and is therefore
not a generic real-valued consequence.

## Separating family: AND / one-point defects

For the degree-`d` point defect with `mu=2^-d`,

`I=2d mu` and `H/I -> 4`.

The bare support estimate `H<=d` would give coefficient `d/I=2^(d-1)`
in front of influence.  The Boolean refinement gives
`2(d-1)+log2(e)`, an exponential improvement in this conversion.  It is
still not sharp: the exact ratio tends to four.

## Required controls

1. **Fixed Renyi order below one.**  No claim is made for `H_alpha`.
   The same point-defect family has `H_alpha/I -> infinity` for each
   fixed `alpha<1`; the checker prints the increasing ratio for
   `alpha=3/4`.
2. **Near-Boolean real functions.**  The normalized real degree-one
   function with squared spectral law `(1-epsilon^2,epsilon^2)` has
   `H/I ~ log2(1/epsilon^2)`.  Hence no degree-only FEI constant holds
   after weakening Booleanity to real bounded-degree normalization.
3. **Addressing.**  The degree-`d` address function saturates the first
   entropy bound, so the `2(d-1)` spectral-support allowance cannot be
   improved using degree and Booleanity alone.  This does not make it an
   FEI extremizer because its influence also grows.
4. **Rare restrictions and selectors.**  Their degree grows with the
   construction.  The theorem therefore supplies no universal constant
   and does not repay the known rare logarithmic debts.
5. **Parity lift.**  The A066 parity lift can increase degree and remains
   full-FEI-hard; even spectral support alone gives no bounded `d` and
   no dimension-independent consequence.

## Literature boundary

The granularity lemma and the sharp support count are known.  They appear
as Fact 2.5 and Corollary 2.7 in the 2014 ECCC report used here, and as
Lemma 4.1 / Proposition 4.2 in the 2025 Mathematische Annalen paper on
the Boolean Bohnenblust--Hille inequality.  The present package makes no
novelty claim for those inputs.  Its contribution to the campaign is the
explicit influence-weighted entropy corollary, its exact limits, and the
control comparison required by A067.

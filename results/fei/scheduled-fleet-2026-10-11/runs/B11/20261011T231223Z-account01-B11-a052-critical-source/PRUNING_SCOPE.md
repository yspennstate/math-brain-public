# Pruning scope and mandatory counterexamples

## What is proved

For a nonconstant Boolean function, ratio-criticality means comparison with
**every actual physical descendant**, not with abstract pieces of its support.
For disjoint tensor products this hypothesis is strong enough to force exact
factor purity: every factor is itself critical and every factor has the same
entropy/influence ratio.  The approximate form retains the exact influence
weight `w_j`; a low-weight factor may have a correspondingly large deficit.

Criticality is used at one identifiable line: fixing every block except `j`
turns the product into `±f_j`, so `R(f_j) <= R(F)+eta`.  Without that physical
descendant inequality, the weighted-average identity alone gives no upper
bound on an individual factor.

## Replay of the two component failures

1. **Raw component entropy.** The pinned nine-bit indicator has two connected
   support components `A,B` and
   `Hraw(1_{A union B}) > Hraw(1_A)+Hraw(1_B)` by more than `1/5000`.
   Moreover `R(A)<R(A union B)<R(B)=4 ln 2`.  This does not contradict tensor
   purity: support components are not physical descendants, and no inequality
   of the form `R(B)<=R(A union B)` follows from criticality unless `B` is
   realized by a coordinate restriction.

2. **Maximum-component ratio.** The pinned seven-bit two-component indicator
   has (natural-log units)
   `R(A)=2.752783270380521...`, `R(B)=4 ln 2`, and
   `R(A union B)=2.775426599558637...`, so the union exceeds both components.
   But fixing two data coordinates gives a NAND2 descendant whose ratio exceeds
   the union ratio by more than `0.59`.  The witness therefore fails the exact
   descendant-critical hypothesis at a concrete physical restriction.  This
   is precisely the line that the unrestricted component-pruning proposal
   lacked.

Sources: Brain commit `5d7a75c0b7ae3aab71df5abdafc31832be81321b`,
`ADDENDUM_11_44_COMPONENT_ENTROPY_COUNTEREXAMPLE.md` (blob
`fc36cb9447b4fc17c5ed49d8c6e98cf59d11f7eb`) and
`ADDENDUM_11_45_COMPONENT_RATIO_COUNTEREXAMPLE.md` (blob
`c76c486f8568aa53ee411c2fb1de0275b4037d72`).

## Arbitrary-core and near-tensor tests

- Every finite Boolean core has a maximum-ratio physical descendant, and that
  descendant is critical.  Hence the supremum over critical sources is exactly
  the full FEI supremum.  Criticality is a valid reduction, not a solution.
- If `g` is critical, every disjoint tensor power `g^{tensor m}` is critical.
  Equal-ratio tensor replication therefore survives the structural theorem.
- Starting with an arbitrary nonconstant core `h`, lift it by unused variables
  and flip a single joint truth-table value.  The result is not a product across
  the old/new split, yet its entropy, influence and ratio converge to those of
  `h`.  Thus qualitative primitivity or connectedness cannot control hidden
  tensor curvature.  The construction is not asserted to preserve full
  descendant-criticality.

## Exact unpaid gap

The theorem classifies **exact tensor decompositions** of critical sources and
quantifies approximate criticality of their factors.  It does not prove that a
critical source factors, that a prime critical source has bounded ratio, or
that one-point surgery preserves criticality.  The next useful question is a
paid interface theorem: whether an `eta`-critical function that is close to a
tensor in a quantitative Fourier/interference metric must either have a small
interface cost or yield a higher-ratio physical descendant.

# Restriction review verdict

## Reviewed object

`B09-BIASED-BLOCK-UNCERTAINTY@1` from the original B09 report.

## Verdict

**ACCEPT AT STATED SCOPE.**  The exact physical-child experiment has joint
law

\[
Q(z,T)=\mu_{p_A}(z)\widehat{f_z}_{p_B}(T)^2,
\]

whose `T` marginal equals the parent residual spectral law and whose `Z`
marginal equals the product physical law.  The latter equality uses Boolean
child Parseval.  Fiberwise Maassen--Uffink for the tensor biased transform
then proves

\[
0\le J_A\le M_A+\Delta_A(p).
\]

Zero-mass fibers are omitted, deterministic endpoints are outside the stated
interior-bias domain, and the empty block is trivial.

## Scope boundary

The local inequality does not pay `M_A+Delta_A` by influence and does not
establish a nonreusing stopping tree.  The arbitrary-composition transport and
global FEI implication therefore remain open.

## Repaired source overclaim

The source's `O(p)`-impossibility sentence was not justified by an upper-bound
asymptotic.  The genuine Boolean AND family repairs it:

\[
J-M=4q(1-2q)p\log_2(1/p)+O(p),
\]

so at `q=1/4` the coefficient relative to the B09 tax tends to `1/2`.
Hence every `Cp` replacement fails and every universal multiplier of the
B09 tax is at least `1/2`.  Sufficiency of `1/2` is not claimed.


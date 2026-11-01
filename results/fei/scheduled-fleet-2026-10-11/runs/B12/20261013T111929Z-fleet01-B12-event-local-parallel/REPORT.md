# B12 / A057 — cylinder-safe event-local telescope

**Run:** `20261013T111929Z-fleet01-B12-event-local-parallel`  
**Primary packet:** A057 (Coherent restriction remainder)  
**Gap:** `B12-A057-COHERENT-HIERARCHY-v17`  
**Status:** new compensated hierarchy theorem PROVED; full FEI OPEN.

## Result

The preceding run proved that summing the complete one-node associator at
every reached restriction cannot have any finite source-influence constant.
This run implements the forced repair.

For a restriction node (v), define
\[
 Gamma_v=Omega(s_v)
 -\frac{Omega(s_{v0})+Omega(s_{v1})}{2}.
\]
This event-local charge is exactly zero on unchanged dummy-cylinder steps.
For every complete adaptive restriction tree,
\[
 sum_vw_vGamma_v=Omega(s)+2pln2,
\]
because terminal source values are (0) or (1), with
(Omega(0)=0) and (Omega(1)=-2ln2).

If (s) is a union of three distinct parallel affine cosets, then
\[
 oxed{sum_vw_vGamma_vle8ln2,I(d)}.
\]
The constant is independent of dimension, codimension, physical orientation,
depth, and adaptive query order, and is asymptotically sharp.

## New estimate

The key strengthening over the previous local theorem is
\[
 Omega(s)le4ln2,I(s).
\]
The selector tax then pays the terminal correction exactly:
\[
 4ln2 I(s)+2pln2=8ln2 I(d).
\]

For codimension (kge5), this follows from the exact two-shell spectrum and
the scalar kernel estimate
\[
 C(p)le p-p(1-p)ln4
 le pleft(rac32ln3-rac83ln2ight),
 qquad p=3cdot2^{-k}.
\]
The cases (k=2,3,4) have exact integer log-sign certificates archived in
the proof and checker.

## Verification

`check_event_local_parallel.py` checked:

- all 1,628 parallel affine triples through four variables;
- all 1,628 compensated (8ln2) bounds;
- 1,634 complete ordered-tree telescopes;
- every query order for the three-variable base source;
- the three exact small-codimension integer certificates;
- exact zero event charge on the prior dummy-cylinder control.

No randomness was used.  The computation corroborates the all-dimensional
proof in `EVENT_LOCAL_TELESCOPE.tex`.

## Exact scope and remaining bridge

This theorem pays the compensated event-local charge, not the refuted raw sum
(sum_vw_vOmega(s_v)).  Full FEI still requires the global entropy
decomposition to produce (Gamma_v), or a proof that the difference between
the genuine coherent remainder and (Gamma_v) is covered by the existing
alpha-log envelope and one terminal reserve.

The next step is therefore exact rather than heuristic: rewrite the biased
kernel identity as a consecutive-state difference and identify its
non-telescoping residual.  That residual must vanish on dummy cylinders and
survive the existing shared-coordinate and activation-equivalence controls.


# Source and scope check: side-uniform `K_{2,3}` apex stability

Checked 3 October 2026.

## Established inputs

1. Borcea, Branden, and Liggett, *Negative dependence and the geometry of
   polynomials*, arXiv:0707.2340. This supplies the multiaffine Rayleigh
   characterization of real stability and the standard strong-Rayleigh
   consequences. The present proof uses these general implications, not a
   claimed new version of them.
2. Huang, *On the Stanley--Welsh weighted forest conjecture*,
   arXiv:2311.00965. This records the larger weighted-forest correlation
   problem and graph reductions/special cases; the general conjecture is
   not resolved here.
3. Ciceksiz and Ravichandran, *Negative correlation in weighted uniform
   forests*, arXiv:2610.00549 (submitted 30 September 2026). This is a
   current primary-source checkpoint for general identities and established
   regimes. Nothing here is represented as superseding its general scope.
4. The four-core marked-edge transfer used for the corollary was already
   derived and audited in this repository. The new input is only the exact
   apex real-stability theorem for the theta block.

## Search performed

Targeted primary-source searches used combinations of `K_{2,3}`, `theta
graph`, `apex`, `forest polynomial`, `real stable`, `strongly Rayleigh`, and
`multivariate`. They did not locate a source stating the theorem proved in
the adjacent note: real stability of the apex-spoke forest polynomial of
`K_{2,3}` when the three edges incident to one degree-three-side vertex have
activity `p>0` and the other three have activity `q>0`.

This is an honest limited prior-art search, not a novelty certification.
Terminology varies, indexing services are incomplete, and no external expert
has reviewed the result.

## Exact claim boundary

Proved:

- `K_{2,3}` with the two positive side activities `p,q` just described;
- independent apex-spoke variables and all nonnegative spoke profiles;
- real stability, hence a strongly-Rayleigh spoke marginal;
- the resulting proportional-row two-marked-edge negative-correlation
  corollary.

Not proved:

- arbitrary activities on the six backbone edges (or even three unrelated
  two-edge-arm pairs);
- arbitrary theta subdivisions or series-parallel backbones;
- a two-terminal determinant gluing theorem;
- negative association jointly with backbone or marked edges;
- preservation under arbitrary backbone cylinder conditioning;
- the full forest negative-correlation conjecture.

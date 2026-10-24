# P0083 idea before checker — B7 / B21 / B23

Date: 2026-09-19 UTC

This note is an idea record, not a proved claim.

The current universal metric is `A_whisker_cert=2`; the residual interval is most naturally written with

`p=1/(alpha-1)`, so `alpha>4/3` is `p<3` and stability requires `C^T C >= (p+1)^(-1) I`.

Three unused routes are being tried in this invocation.

1. **B7 TAKE THE LIMIT.** Start at the conjectural endpoint `p=3` on the smallest attached odd-unicycle motif (a triangle with one pendant leaf), then look for inequalities that stay strict on the whole deformation strip `2<=p<=3` rather than treating the numerical endpoint as evidence.
2. **B21 ASK WHO ELSE HAS THIS SHAPE.** The signless-Laplacian literature on non-bipartite unicyclic graphs repeatedly identifies a triangle with a pendant path as an extremal least-eigenvalue shape. The WARM matrix is weighted and nonlinearly constrained, so those theorems cannot be imported directly; use their determinant/perfect-matching viewpoint instead. For a bare odd cycle the weighted incidence determinant should factor into the two cycle matchings and become exactly controllable from equilibrium incidence ratios.
3. **B23 DO WHAT THE PROPOSER DID NOT EXPECT.** Assume the attached triangle has an asymmetric or stable positive branch near `p=3` and derive necessary ratio equations. The target is to force the two nonattachment triangle potentials to coincide, then use a two-edge Rayleigh witness. If the assumed branch survives, it would be a genuine counterexample lead; if it does not, the failure mechanism is itself useful.

Planned exact targets before any checker is written:

- prove every positive equilibrium supported exactly on an odd cycle is linearly unstable for `alpha>4/3` by a determinant bound;
- prove every positive equilibrium on the triangle-plus-one-leaf motif is linearly unstable throughout `2<=p<=3` (`4/3<=alpha<=3/2`), using only exact inequalities;
- only after those proofs are algebraically closed, add a small exact-arithmetic self-check for the fixed polynomial factorizations. The self-check will not be called an independent audit.

Neither target by itself lowers the frozen universal metric below `2`, because attached longer odd unicycles and general diameter-at-least-four trees remain.

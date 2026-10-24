# Supplement — exact target-parent embedding of the residual obstruction

The two-coordinate family in `REPORT.md` is not a target counterexample, but it is an exact **source-valid Schur residual of a target parent**.

For `0<eta<1`, let

`S_eta=(2eta)^(-1)[[1+eta,1-eta],[1-eta,1+eta]]`

and define the three-coordinate parent

`A_eta = [1] direct_sum S_eta`.

Take three independent `Uniform[-1/2,1/2]` inputs. The eigenvalues of `A_eta` are exactly

`1, 1, 1/eta`,

so the parent satisfies the owner hypothesis of at least three eigenvalues of modulus at least one.

Use the first original coordinate as a physical scalar pivot. Its coefficient is exactly one and its cross row is zero, so exact square completion leaves Schur residual **exactly** `S_eta`. Therefore every residual statement refuted in `REPORT.md` is being tested on an object produced by a genuine target parent, with no rotation, moment assumption, support assumption, or altered input law.

In particular, any proposed proof of the full theorem that reaches the normalized Schur residual and then invokes a universal arbitrary-self extension

`H_(1/2)(R) <= C ||B||_F^(-1/2)`

would fail on this target-parent family, because the residual satisfies

`H_eta(0) sqrt(b_eta) ~ log(4/eta) -> infinity`.

This does **not** refute the target theorem: the parent has other valid smoothing routes, and the completed rank-two affine half-Riesz theorem controls the residual using its determinant. It only proves that the arbitrary-self Frobenius-scaling residual lemma is not a valid universal bridge.
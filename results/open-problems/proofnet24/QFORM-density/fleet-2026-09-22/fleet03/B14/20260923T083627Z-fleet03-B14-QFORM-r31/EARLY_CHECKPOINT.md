SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T08:36:27Z.
attacking: a zero-loss localization theorem for an indefinite physical pair whose Schur remainder contains a diffuse rank-two semidefinite bank, preserving all range-compatible translations and arbitrary unbounded fragmented supports.

# Early substantive checkpoint

Full QFORM remains open. This checkpoint records the first nontrivial implication attacked in this run.

Let `U in R^2` be two original independent coordinates and `V in R^m` a disjoint original-coordinate bank. Complete the physical pair with an invertible indefinite `2x2` block `B`; write `D=|det B|`, `kappa=sigma_min(B)`, and suppose that after conditioning on outside original coordinates `Z=z` the Schur remainder on `V` has the form

`R_z(V)=V^T S V + q(z)^T V+d(z)`

with `S` semidefinite of rank exactly two and `q(z) in Range(S)` for every `z`. Put `P=pdet_abs(S)`, the product of the two nonzero eigenvalue magnitudes.

Range-compatible affine terms are free: with `h(z)=1/2 S^+ q(z)`,

`V^T S V+q(z)^T V=(V+h(z))^T S(V+h(z))-h(z)^T S h(z)`.

Conditionally on `Z=z`, translating each original coordinate of `V` by the deterministic vector `h(z)` preserves independence and every marginal density cap `<=1`.

Factor `S=eps L^T L`, `eps in {+1,-1}`, with `L` a `2xm` full-row-rank matrix. Then `det(LL^T)=P`. Fleet02/B05 proved the exact product-projection estimate: after whitening, any two-dimensional Parseval projection of cap-one independent coordinates has density cap `<=e`. Hence

`||p_{LV}||_infinity <= e/sqrt(P)`.

Therefore the definite rank-two quadratic remainder has density

`||p_{R_z}||_infinity <= K := pi e/sqrt(P)`

uniformly in `z`: after the above translation, `R_z=eps |LV'|^2+const`, and polar coarea gives the factor `pi`.

Now use the physical-pair logarithmic envelope in fleet04/B14 r7 / the pair-log theorem:

`p_Q(t) <= 2sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa|t-R|))`.

If `||p_R||_infinity<=K`, layer cake yields for `A=2r^2/kappa`

`E log_+(A/|t-R|) <= Psi(2KA) = Psi(4Kr^2/kappa)`,

where `Psi(z)=z` for `z<=1` and `Psi(z)=1+log z` for `z>=1`.

Thus the first candidate bound is

`||p_Q||_infinity <= inf_{r>0} [2sqrt(2)/r + D^(-1/2) Psi(4Kr^2/kappa)]`.

Optimizing gives the explicit piecewise value

`6 (K/(kappa sqrt(D)))^(1/3)` if `KD/kappa<=1/8`,

and

`D^(-1/2)[3+log(8KD/kappa)]` if `KD/kappa>=1/8`.

Substituting `K=pi e/sqrt(P)` yields a dimension-free aggregate bank estimate depending only on the physical-pair scale and the rank-two Schur pseudo-determinant. No individual bank coefficient, support radius, fragment count, fragment separation or moment enters.

The remaining issue for the full theorem is structural, not localization: the bare three-large-eigenvalue hypothesis does not yet force such a semidefinite rank-two Schur bank with controlled `(D,kappa,P)`, and a kernel component of `q(z)` is not silently removable. This run will now prove the rough-law transfer carefully and stress-test the scale formula.

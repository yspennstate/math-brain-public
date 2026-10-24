# Updated scope after the arbitrary-start upper-bound proof

This addendum supersedes the first open item in `06_literature_and_scope.md`, which was deliberately preserved as the record at completion of the endpoint/count proof.

## Additional theorem

Files `07_stronger_sector_certificate.tex`, `08_count_lyapunov_smoothing.tex`, and `09_full_polymer_tv_upper.tex` prove, at fixed `b>0` and `beta=b/n`,

`t_mix^polymer(epsilon) <= C_b sqrt(n) [(log n)^2 + log(1/epsilon)]`.

The single assembled input is `full_polymer_tv_upper.tex`.

The argument acts on the density of the **actual polymer semigroup**. It uses count strong lumpability only for the layer averages; the labelled-cut construction is used only for its stationary Dirichlet form and orthogonal harmonic projectors. It does not assume the cut process projects to the polymer process, or that a polymer density evolves within individual harmonic sectors.

## New ingredients

1. The degree-ell reciprocal rising-factorial certificate gives every degree-ell comparison-sector eigenvalue the bound `ell sqrt(beta)/6`.
2. The count Lyapunov function `V(k)=[pi_Q(mode)/pi_Q(k)]^(3/4)` satisfies `QV/V <= [C_b-c_b log V]/sqrt(bn)`, including both endpoints. Its moment becomes uniformly bounded in `O_b(sqrt(n) log n)` time. This gives count density squared norm `M(t)<=C_b sqrt(bn)`.
3. Positivity and the constant diagonal of each layerwise harmonic projector give `sum_(ell<=d) ||P_ell F||_2^2 <= binom(n,d) M(t)`.
4. The instantaneous energy identity yields a Nash differential inequality for the polymer density. It reaches polynomial L2 size in `O_b(sqrt(n) (log n)^2)` time; the established polymer gap finishes the TV estimate.

## Further immediate consequence for the count chain

The polynomial count L2 bound followed by the already proved count gap gives worst-case count L2 mixing in `O_b(sqrt(n) [log n + log(1/epsilon)])` time. In particular, the Nash proof could begin after a slightly longer `O_b(sqrt(n) log n)` interval with a constant bound `M(t)<=2`; its final order is unchanged.

## Questions still open

- Remove the extra logarithm between the full-polymer lower bound `sqrt(n) log(n)/(8 sqrt(b)) + O_b(sqrt(n))` and the new `O_b(sqrt(n) (log n)^2)` upper bound.
- Determine whether arbitrary-start polymer TV cutoff occurs at the endpoint/count cutoff time.
- Prove a limiting TV profile or optimality of the `sqrt(n)` endpoint/count window.
- Extend cutoff asymptotics uniformly to varying `b=b_n`.

The proof does not settle those questions.

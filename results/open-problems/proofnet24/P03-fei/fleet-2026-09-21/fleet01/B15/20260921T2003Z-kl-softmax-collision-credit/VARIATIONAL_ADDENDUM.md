# Addendum — the post-KL soft-max residual is itself an optimal gap/information tradeoff

Use the notation of `REPORT.md`. For one recombination fibre, let `lambda` be the conditional source-origin law, let `x_j` be source mesh depths, put `M=max_j x_j`, and set the nonnegative gap-to-frontier

`g_j=M-x_j`.

The report proved

`Psi=-(1/2)log_2 E_lambda[4^{-g}]`.

## Theorem B15-GIBBS-RESIDUAL-03

Exactly,

`boxed{ Psi = inf_{pi << lambda} [ E_pi g + (1/2) D_KL,2(pi||lambda) ] }`.

The unique optimizer on the support of `lambda` is

`boxed{ pi_j^* = lambda_j 4^{-g_j} / E_lambda[4^{-g}] }`.

### Proof

The Gibbs variational identity in natural logarithms is

`-log E_lambda exp(-beta g) = inf_pi [ beta E_pi g + D_KL,e(pi||lambda) ]`.

Set `beta=2 ln 2` and divide by `2 ln 2`. Since `D_KL,e=(ln 2)D_KL,2`, this gives the displayed formula. Direct substitution gives the optimizer. No FEI input is used.

## Why this form is useful

This identifies the exact post-information-credit object as the cheapest possible mixture of two resources:

1. **geometric/arithmetic displacement** `E_pi g`, which is where the fleet02 valuation-tail theorem can enter; and
2. **origin-law information displacement** `(1/2)D(pi||lambda)`, which is where the packet/product negative credits can enter.

The earlier elementary bounds are immediate choices of `pi`:

- `pi=lambda` gives `Psi<=E_lambda g`, i.e. the raw collision cost;
- conditioning `lambda` on `{g<=t}` gives `Psi<=t+(1/2)log_2(1/F(t))`;
- concentrating on a maximal-depth origin gives `Psi<=(1/2)log_2(1/rho)` when that atom/set has conditional mass `rho`.

Thus there is no need to choose in advance between a valuation-gap payment and a rarity/KL payment. The correct local object already performs the optimal interpolation.

## Precise next global target

For every actual unequal-magnitude recombination fibre `v`, let `P_v` be its spectral mass and `Psi_v` the quantity above. A full arithmetic closure along this interface would follow from a source-consistent estimate of the form

`sum_v P_v Psi_v <= C I(f)`

**after** matching the local source-origin KL terms to the exact global packet/product credits without double counting.

The key point is that the variational theorem permits a different `pi_v` in every fibre. A candidate proof can therefore choose `pi_v` to minimize a weighted valuation-tail cost when the depth frontier is cheap, and choose an information projection when the frontier is rare. What remains open is a globally consistent choice whose KL charges telescope into the already-existing negative credits.

This is not a proof of FEI. It is a strict sharpening of the unpaid object: the raw max-minus-average gap has been replaced by its exact entropically regularized distance to the maximal-depth frontier.

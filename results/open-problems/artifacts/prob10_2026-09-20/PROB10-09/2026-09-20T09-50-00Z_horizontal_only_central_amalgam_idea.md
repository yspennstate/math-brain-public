# PROB10-09 idea before code — horizontal-only central extensions

Frozen parent: iid bond percolation on Cayley graphs of finitely generated nonamenable groups; seek `p_c<p_u`. Restricted families remain PARTIAL.

## New observation

The previous central-extension runs always retained the explicit central pair `z^{+-1}`. The immediate predecessor tested deleting that pair and recorded that the `p_c` witness then collapses from the full-fibre bound to the bare free-tree estimate `p_c<=1/(2k-1)`. That observation is correct, but it did not recompute the *uniqueness-side* nonbacktracking bound for the smaller-degree graph. Deleting `z^{+-1}` also reduces the degree by two and removes the `+2` central contribution from the adjacency-norm bound. For the natural horizontal lift sets this improvement is strong enough that the bare free tree already wins.

General target criterion: for a central extension `1 -> Z -> Gamma -> Q -> 1`, let a finite inverse-closed quotient set `S_Q` have `D` elements, choose inverse-compatible lifts `S~` that generate all of `Gamma`, and suppose `S_Q` contains `k` free generator pairs. If `rho=||A_{Q,S_Q}||` and the nonbacktracking growth exponent `beta_D(rho)` satisfies `beta_D(rho)<2k-1`, then

`p_c(Cay(Gamma,S~)) <= 1/(2k-1) < 1/beta_D(rho) <= p_{2->2} <= p_u`.

The operator side should be lift/cocycle-uniform: Fourier transform along the central `Z` produces magnetic quotient adjacencies, pointwise dominated by the ordinary quotient adjacency.

## Surface-central application

For the iterated central surface amalgam

`E(g,e)=< z central, a_{i,j},b_{i,j} | prod_j [a_{i,j},b_{i,j}] = z^{e_i}, 1<=i<=r >`, `g_i>=2`,

use only the horizontal generators and their inverses; do **not** include `z^{+-1}`. These horizontal lifts generate the whole group exactly when `gcd(e_1,...,e_r)=1`. Central shearing of individual horizontal lifts leaves every commutator relator unchanged, so the same condition is shear-uniform.

Let `G=sum_i g_i`, `H=sum_i sqrt(g_i)`, `k=sum_i(2g_i-1)=2G-r`, `D=4G`, `q=D-1=4G-1`, and `t=2k-1=4G-2r-1`. The quotient is the free product of the standard surface groups. Using the preserved rigorous surface spectral estimate `||A_{Gamma_g}||<=4 sqrt(g)` and coset decomposition of each factor adjacency,

`rho <= 4H`.

The intended exact inequality is

`beta_D(4H) < t`.

Two elementary identities make this plausible uniformly. First `q=t+2r`, hence `q/t>1`. Second

`t + q/t - 4H = sum_i (4g_i-2-4sqrt(g_i)) - 1 + q/t
                 = sum_i (4g_i-2-4sqrt(g_i)) + 2r/t > 0`,

because `4g-2>4sqrt(g)` for every integer `g>=2`. Also `t>sqrt(q)`. Therefore the larger-root characterization should give `beta_D(4H)<t` for all `r>=1`, `g_i>=2`.

Smallest new connected horizontal-only case: `r=1,g=2,e=+-1`. Here `D=8,q=7,k=3,t=5,rho<=4sqrt2`, so `beta<=1+2sqrt2<5`. Thus

`p_c<=1/5`, `p_u>=1/(1+2sqrt2)=(2sqrt2-1)/7`,

and the certified gap is at least `(10sqrt2-12)/35`, about `0.0612`.

## Negation test / exact obstruction

If `d=gcd(e_1,...,e_r)>1`, the horizontal lifts do not generate the full central amalgam: their intersection with `<z>` is exactly `<z^d>`, so the horizontal subgroup has index `d`. Thus the no-central-edge construction is not a Cayley graph of the full group in that case. This is a genuine scope boundary, not a proof failure to be hidden.

## Three distinct methods compared in this iteration

1. **Recompute the no-central-edge nonbacktracking threshold** rather than only degrading the `p_c` witness. This is the primary route and appears to close the entire primitive-Euler (`gcd(e)=1`) horizontal family.
2. **Relator-path vertical coarse graining:** use the length-`4g_i` surface relator as a virtual vertical edge and run anisotropic `F_k x Z` percolation. This is logically different but pays a factor `p^{4g_i}` for each virtual vertical crossing and is expected to be quantitatively inferior in the smallest cases; it will be tested only as a negation/backup route.
3. **Arbitrary projected generating sets / Nielsen changes:** the magnetic domination survives, but the visible free subset and standard surface spectral norm need not. Without a generating-set-stable quotient invariant this route does not yet extend to every Cayley graph of the same group. Record this as the remaining structural obstruction rather than claiming all-Cayley closure.

No code or finite arithmetic checker was run before this note was written.
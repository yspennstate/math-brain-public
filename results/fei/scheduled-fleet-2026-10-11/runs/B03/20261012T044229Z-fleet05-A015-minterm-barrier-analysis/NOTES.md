# Stage 2 checkpoint: the barrier after conditioning

Board 2026-10-12 04:39 UTC and B03 lead v2 read. A006 now supplies a majority PI-J posterior bound; A012 supplies the exact balanced activation reference. Stage-1 raw labels are not the remaining best-code obstruction. Do not repeat those class calculations.

For N full-width minterms of density pi=2^-n and lambda=1/N, conditioned nonempty-root probability of exactly one root is

`eta = pi / ((1+pi/N)^N - 1)`.

This cancels both minterm label and root rarity in the one-root sum, up to -log2 eta. Full support/common subset law makes the sum independent of which root was selected. `exp(-pi)<=eta<=1` follows from pi<=D<=pi exp(pi). This strengthens stage 1's unconditioned label-only refund; it does not pay physical subset locations.

A common order chosen uniformly over all permutations gives a one-root/no-child output law `eta/[2 s(s+1) binom(n,s)]`, s>=1. Any exchangeable subprobability reference pays at least E log2 binom(n,|S|), regardless of size optimization.

Actual all-relevant balanced test family: `M_r=y+A_r(z-y)`, p=2^-r, n=r+2. Singleton {y} has mass (1-p)^2, all other {y}+nonempty U and {z}+arbitrary U have mass p^2. H=(1-p)^2 log2(1/(1-p)^2)+2r(2p-p^2), I=1+rp. Thus every exchangeable reference cost/I diverges at least as log2(r+2), even though H/I tends to zero. Influence-sorted common order starts with y; a rational exponent-2 rank reference has a uniformly bounded complete cost. This isolates physical coordinate-location compression after latent gate erasure.

These are preliminary analytic results, validation pending. New generic statement is restricted to exchangeable references, not all complete references. The next universal gap is a function-adapted support/order selection with all posterior, normalizer and terminal-core costs paid.

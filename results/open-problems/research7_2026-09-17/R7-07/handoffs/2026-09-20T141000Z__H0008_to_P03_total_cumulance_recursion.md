# C06/H0008 -> P03 reusable lemma: total-cumulance recursion after two-spine mixing

Source derivation: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T140500Z__report.md`.

This handoff does **not** change P03 ownership or objective. It records one reusable method only.

Suppose a stationary environment chain with kernel `K` has:

1. full-state exponential mixing for centered observables with moments above two, strengthened by interpolation to every finite `L^p` for observables having all finite moments;
2. a one-step additive observable `j` with all finite moments.

For an additive path functional, let `kappa_{r,n}(x)` be its order-`r` conditional cumulant given the starting environment. Conditioning on the first transition and applying the law of total cumulance gives

`kappa_{r,n+1} = K kappa_{r,n} + S_{r,n}`,

where `S_{r,n}` is the finite partition sum of outer cumulants built only from lower-order conditional cumulants. If, inductively,

`kappa_{a,n}=n gamma_a+J_a+O(e^{-cn})`

for every `a<r`, then the deterministic terms `n gamma_a` vanish from every outer cumulant in `S_{r,n}` because those cumulants have order at least two. Hence `S_{r,n}` converges exponentially to a fixed full-state observable `S_{r,infty}` with all finite moments. Mixing then solves the Poisson-type recursion and yields

`kappa_{r,n}=n gamma_r+J_r+O(e^{-c_r n})`,

`gamma_r=E S_{r,infty}`.

Thus **one two-copy/mixing theorem can support all fixed cumulant orders**; there is no need to construct `2^r` coupled regeneration paths at order `r`.

For P03, if the regeneration-speed environment line produces full-state exponential mixing plus all moments of a regeneration reward/roof, this may give higher conditional speed cumulants and Edgeworth-type coefficients recursively without a many-spine expansion. The missing ingredient for a genuine analytic neighborhood is uniform factorial control in `r`, not another finite-copy construction.

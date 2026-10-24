SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T10:15:48Z.
attacking: after the one-heavy equal-bank branch and finite-activity diffuse fragments were excluded, test a genuinely two-heavy/shared-coordinate exact-spectrum family with a critically fragmented bank.

# Early checkpoint — lightlike two-heavy Gaussian-shift stability

Full QFORM remains OPEN. This is a supporting sharp-witness calculation.

Let `(U,V)` have an arbitrary joint probability density `rho<=1` on `R^2`, and let `G_sigma~N(0,sigma^2)` and an arbitrary real random shift `H` be independent of `(U,V)`, with `G_sigma` independent of `H`. Put

`Q=V^2-2U(G_sigma+H)`.

The completed account03/B17 r22 level-set proof extends without changing its geometry to every deterministic bank shift `h`: conditionally on `H=h`,

`K_{s,h}(u,v)= [2 sigma sqrt(2 pi)|u|]^{-1} exp(-(v^2-s-2uh)^2/(8 sigma^2 u^2))`.

For fixed `u`, the superlevel condition is an interval condition on `v^2` centered at `s+2uh`; the r22 bound

`|{v: |v^2-c|<delta}| <= 2 sqrt(2 delta)`

is uniform in the center `c`. Hence the same weak-L^(3/2) computation is uniform in `h`. If `sigma_0^2=1/12` and

`C_x = 2^(13/6) sqrt(3/pi) Gamma(5/4)^(2/3)=4.109270566451296...`,

then

`||p_Q||_infinity <= C_x (sigma_0/sigma)^(2/3)` for every `sigma>=sigma_0`.

The scaling follows because the weak-L^(3/2) level-set constant is proportional to `sigma^(-1)`, and layer cake raises it to the `2/3` power. Averaging over arbitrary `H` cannot increase the bound. In particular the right side is always `<3 sqrt(2)`.

This immediately makes finite-activity Gaussian+compound-Poisson bank limits harmless in the r22 two-heavy geometry. The still-unpaid complementary construction is a growing-activity cap-one fragmented bank with activity `lambda_m->infinity`, `lambda_m=o(m)`. I will prove its bank density converges uniformly to `N(0,1/12+a^2)` and transfer the above output bound uniformly over arbitrary heavy laws.

Required newest-Claude result already applied at the next step: Lemma 1 of `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives `int |hat f|^p <=4 pi/sqrt(p)` for every cap-one physical density. At `p=m` this gives the dimension-free normalized-bank density cap `||h_m||_infinity<=2`, exactly the uniform constant needed by the r22 transfer inequality.

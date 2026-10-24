SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T20:05:16Z.
attacking: the fresh affine-shear caveat in the curved two-sheet tube; retain a disjoint rough scalar and prove a Borel square-root tube profile before any full partner slicing.

# Early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full target OPEN.

Fresh control commit: `math-research-brain@48596c878caf620484499cd94cc1958139d4c258`, OWNER CONTROL revision `2026-09-22.15`. The fresh interactive tube correction shows that an arbitrary induced affine shear `dL` destroys the stronger `O(a r^2)` dyadic tube estimate by a saddle example of size `a r^2 log(1/r)`. This checkpoint records a weaker but summable product-preserving repair.

## Candidate theorem already proved at calculation level

Let `(L,V)` have a joint density `rho` with `||rho||_infinity <= M_2`. Let `P` be independent of `(L,V)`, with probability density `f_P` satisfying `||f_P||_infinity <= M_1`. For arbitrary real `c,d,gamma`, `r>0`, define the shell submeasure

`nu_r(E)=P(r<=|L|<=2r, dL+c+(gamma+V^2)/(2L) in E)`.

For every Borel set `E` of finite Lebesgue measure `m`,

`nu_r(E) <= K_0 M_2 r^(3/2) m^(1/2)`,   `K_0=(8/3)(4-sqrt(2))<6.896`.

Reason: for fixed nonzero `l`, the pushforward of Lebesgue measure under `v -> v^2/(2l)` has density `sqrt(2|l|)|y|^(-1/2)` on the appropriate half-line, hence by decreasing rearrangement the inverse image of any set of length `m` has length at most `2 sqrt(2|l|m)`. Integrating `sqrt(|l|)` over both components of `r<=|l|<=2r` gives the stated constant. The translations `d l+c+gamma/(2l)` disappear completely from the estimate.

Layer cake then yields an actual rough scalar receiver. The restricted law of

`P+dL+c+(gamma+V^2)/(2L)`

has density cap at most

`K_0 M_2 sqrt(M_1) r^(3/2)`.

Indeed, for every `q`, integrate `nu_r({z:f_P(q-z)>t})` over `0<t<M_1` and apply Cauchy-Schwarz together with `integral_0^M1 |{f_P>t}| dt=1`. Consequently its width-`2a` tube has probability at most

`2 K_0 M_2 sqrt(M_1) a r^(3/2)`.

This is Borel, not interval-only, and is uniform in the affine shear `d`. It gives the `alpha=1/2` gain that the fresh correction says is sufficient for dyadic summation whenever the smoothing scalar comes from a disjoint original-coordinate bank.

Next in this run: upgrade the shell statement to a full density theorem for a null hub `2PL` plus an arbitrary two-variable quadratic with nonzero curvature transverse to `L`, identify the invariant partner currency, and apply the newest account03/B05 partner-plane identity without freezing both partner coordinates.

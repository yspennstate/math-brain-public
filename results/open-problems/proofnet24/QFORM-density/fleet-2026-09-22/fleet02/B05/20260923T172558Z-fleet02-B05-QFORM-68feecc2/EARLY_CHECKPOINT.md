SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T17:25:58.911777Z.
attacking: repair the invalid frozen-slice interval receiver by isolating the exact slice regularity needed by a fragmented cap-one hub, then spend the third curvature jointly rather than via a Borel-profile substitution.

# Early checkpoint — frozen-slice interval profile is not a hub receiver

Run `20260923T172558Z-fleet02-B05-QFORM-68feecc2`.

Status: substantive checkpoint; full QFORM open.

## First unpaid implication

The owner correction invalidates the earlier B05 step that promoted a frozen-slice interval estimate `mu_l(I) <= C |I|^(1/2)` to an arbitrary-Borel profile before integrating a rough hub. The live question is to identify a genuinely sufficient slice currency that remains product-valid in the heavy near-null moving-slope branch.

## A sufficient replacement: L2 slice receiver

Let `X` be independent of `(L,Y)`, with density `f_X<=1`. Assume `(L,Y)` has a joint density `q(l,y)`, write `q_l(y)=q(l,y)` and `m(l)=int q_l(y)dy`, and suppose

`sup_l ||q_l||_2 <= K`.

For `a!=0` put `Q=2aXL+Y`. At fixed `l!=0`, the density of `2alX` has mass one and cap `H_l=(2|al|)^(-1)`, hence L2 norm at most `H_l^(1/2)`. Young/Cauchy-Schwarz gives

`||(q_l * p_(2alX))||_infinity <= K / sqrt(2|a l|)`.

The trivial cap bound gives simultaneously

`||(q_l * p_(2alX))||_infinity <= m(l)/(2|a l|)`.

Therefore, for every output point,

`p_Q <= int min( K/sqrt(2|a l|), m(l)/(2|a l|) ) dl`.

Splitting at `|l|=R`, using `int m=1`, and optimizing,

`p_Q <= 2sqrt(2)K sqrt(R/|a|) + 1/(2|a|R)`

with optimum `R=(1/(2sqrt(2)K sqrt(|a|)))^(2/3)`, hence

`boxed: ||p_Q||_infinity <= 3 K^(2/3) |a|^(-2/3).`

Thus uniform strong-L2 control of the *unnormalised frozen slice densities* is sufficient. The same argument with weak-L2 gives a slightly worse absolute constant. This is the precise kind of Borel-stable currency absent from a mere interval Frostman bound.

## Explicit obstruction to interval-profile-only reception

For integer `N>=2` let

`E_N = union_{k=1}^N [3Nk, 3Nk+1/N]`, `f_N=1_{E_N}`.

Then `f_N<=1`, `int f_N=1`, and every interval `J` of length `h` obeys

`|E_N intersect J| <= sqrt(h/N)`.

Proof by three ranges: `h<=1/N` gives `<=h`; `1/N<h<3N-1/N` meets at most one component and gives `<=1/N`; for `h>=3N-1/N`, total mass is at most one and `sqrt(h/N)>1`.

Take independent `X,U,L`, with `X,U` density `f_N` and `L` uniform on `[1/N,1+1/N]`. Given `L=l`, put `Y=-sqrt(2) l U`. Its conditional density is

`g_l(y)=(sqrt(2)l)^(-1) 1_{-sqrt(2)l E_N}(y)`.

For every interval `I`, since `l>=1/N`,

`P(Y in I | L=l) <= 2^(-1/4) |I|^(1/2)`.

So the frozen interval square-root profile is uniform in both `l` and `N`. Nevertheless

`B_N=sqrt(2)L(X-U)`

has

`p_{B_N}(0)=int_{1/N}^{1+1/N} dl/(sqrt(2)l)=2^(-1/2) log(N+1) -> infinity`,

because the difference `X-U` has density one at zero. Hence no law-uniform hub receiver can depend only on the cap of the hub/slope and the frozen interval square-root profile.

This is not a QFORM counterexample: the quadratic matrix of `B_N` has only two nonzero eigenvalues, `+1,-1`.

## Target-valid lift and required pinned result

Add two independent cap-one coordinates `S1,S2` and put

`Q_N = sqrt(2)L(X-U) + (S1+S2)^2/2`.

Its symmetric matrix has spectrum `{1,1,-1,0,0}`. Apply newest-Claude Theorem H from the pinned `e5f71d79...` package with hub `H={L}`, one light square direction `v=(0,0,1/sqrt(2),1/sqrt(2))`, and hub-coupling column `(1/sqrt(2),-1/sqrt(2),0,0)`. The augmented Gram matrix is `I_2` and every physical-row leverage is exactly `1/2`. Therefore

`|phi_Q(t)| <= 4 pi^(3/2) |t|^(-3/2)`

and Fourier inversion gives

`boxed: ||p_{Q_N}||_infinity <= 3*2^(4/3) = 7.5595263...`.

Thus the logarithmic frozen-profile obstruction disappears once the third curvature is spent jointly, exactly as the full conjecture predicts.

Next: formalise the L2 receiver and determine whether the moving-slope same-source transverse geometry can generate its L2 slice currency without conditioning on the third projected coordinate.

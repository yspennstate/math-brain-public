SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T17:48:15Z.
attacking: the exact convex dual and finite-hub obstruction for optimized marginal-balanced projected-crossing Fourier currency, then a dense Hadamard test family.

# account03/B04 r38 — optimized projected-crossing dual and compound-hub certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW SUPPORTING THEOREM / EXPLICIT ROTATED-INDEFINITE ESTIMATE / FULL TARGET OPEN`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. The results below preserve the original independent coordinates and use integrated product-Fourier inequalities, not law-uniform pointwise quadratic-phase decay. The supporting density branches proved here are continuous `C_0`; full-target continuity remains open.

## 1. Sources and exact previous theorem used

Fresh owner control remains QFORM-only, revision `2026-09-22.15`. The live correction inbox was read at blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. In particular I do not use: uniform pointwise van-der-Corput/Fresnel decay for arbitrary cap-one densities; independence after rotating into an eigenbasis; arbitrary-joint coarea; positive moments of conditional projection-density caps; naive fiber-supremum integration; or a fixed fragment-count reduction.

The immediate source is my preceding completed supporting theorem

`yspennstate/math-open-problems@ea2f45957db06473799ce27affa30162fda98982:proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T165007Z-account03-B04-auto11-r37/REPORT.md`.

Its arbitrary-weight projected-crossing theorem says the following. Let `C` have physical rows `c_i`. For a probability law `w=(w_S)` on positive `ell`-row Gram minors

`D_S = det(C_S C_S^T)>0`,

put

`alpha_i(w)=sum_(S contains i) w_S`

and, when every `alpha_i<=1/2`,

`Gamma(w;C)=exp( sum_S w_S log D_S - sum_i alpha_i log alpha_i ).`       (1.1)

In the grouped-hub setup with hub rank `k`, average order `d=k+ell>2`, hub projection density cap `M_H`, hub-to-bank singular-value product `S`, the source theorem gives

`||p_Q||_infinity
 <= [d/(d-2)] 2^((k+3ell)/(2d))
    M_H^(1/d) S^(-1/d) Gamma(w;C)^(-1/(2d)).`                 (1.2)

It also gives `phi_Q in L^1`, hence a continuous density vanishing at infinity.

The missing step left by r37 was to optimize `Gamma` and understand what failure of that optimization means geometrically. That is done below.

## 2. Exact convex dual for optimized marginal-balanced currency

Fix `ell>=1` and let

`E={S: |S|=ell, D_S>0}`.

Assume there is at least one probability law on `E` with every inclusion marginal at most `1/2`. Define

`Gamma_* = Gamma_(ell,1/2)(C)
 := sup { Gamma(w;C): w in Delta(E), alpha_i(w)<=1/2 for all i }.`       (2.1)

Set `d_S=log D_S` and define the scalar convex function

`psi(y)=sup_(0<=a<=1/2) {-a log a + y a}`.                              (2.2)

The one-variable maximization is explicit:

`psi(y)= e^(y-1),                         y<=1-log 2,`
`psi(y)= (y+log 2)/2,                    y>=1-log 2.`                    (2.3)

### Theorem `QFORM-MARGINAL-BALANCED-CURRENCY-DUAL-v1`

The exact optimized currency satisfies

`boxed:
 log Gamma_*
 = inf_(y in R^m)
   [ max_(S in E) {log D_S - sum_(i in S)y_i}
     + sum_i psi(y_i) ].`                                                   (2.4)

Equivalently,

`boxed:
 Gamma_*
 = inf_y exp(sum_i psi(y_i))
         max_(S in E) [D_S exp(-sum_(i in S)y_i)].`                         (2.5)

### Proof

Let

`Phi(a)=-a log a` for `0<=a<=1/2`, and `Phi(a)=-infinity` otherwise.

The closed concave function `Phi` has the exact biconjugate representation

`Phi(a)=inf_y [psi(y)-ya]`,                                                 (2.6)

with `psi` from (2.2). Hence, writing `A` for the subset-incidence matrix,

`log Gamma_*
 = max_(w in Delta(E))
   [sum_S w_S d_S + sum_i Phi((Aw)_i)]`
` = max_w inf_y
   [sum_i psi(y_i)+sum_S w_S(d_S-sum_(i in S)y_i)].`                       (2.7)

The `w`-simplex is compact, the expression is affine (therefore concave) in `w` and convex lower-semicontinuous in `y`. Finite-dimensional minimax/Fenchel duality therefore interchanges max and inf. Maximizing over the simplex selects the largest edge score and yields (2.4). Formula (2.3) follows by differentiating `-a log a+ya`; the unconstrained maximizer is `a=e^(y-1)` until it reaches `1/2`. QED.

At a primal/dual optimum, the KKT interpretation is concrete. If `alpha_i<1/2`, then the corresponding dual potential is in the exponential branch and obeys `y_i=1+log alpha_i`; if `alpha_i=1/2`, then `y_i>=1-log2`. Every minor receiving positive primal weight maximizes the reduced score

`log D_S - sum_(i in S)y_i`.                                                (2.8)

Thus the optimizer is an exact Gibbs/soft-cover object in physical coordinates, with hard saturation only at marginal `1/2`.

## 3. Small optimized currency forces a finite physical compound hub

The dual is useful computationally, but there is also a direct structural consequence.

Let `x_S>=0` be any fractional matching on the positive-minor hypergraph:

`sum_(S contains i) x_S <=1` for every physical row `i`,                  (3.1)

and let `T=sum_S x_S`.

If `T>=2`, normalize `w_S=x_S/T`. Then `alpha_i<=1/T<=1/2`, so `w` is feasible. Also

`sum_i alpha_i=ell`,

and because every positive `alpha_i<=1/T`,

`-sum_i alpha_i log alpha_i >= ell log T.`                                (3.2)

Consequently

`boxed:
 Gamma_*
 >= T^ell exp[ (1/T) sum_S x_S log D_S ].`                                (3.3)

In particular, for a threshold `delta>0`, let

`E_delta={S in E: D_S>=delta}`.

If the fractional matching number of `E_delta` is at least two, then

`boxed: Gamma_* >= delta * nu_f(E_delta)^ell.`                             (3.4)

For an ordinary matching of `r>=2` pairwise disjoint positive minors this specializes to the exact lower bound

`Gamma_* >= r^ell (prod_(j=1)^r D_(S_j))^(1/r).`                           (3.5)

Now take a maximum ordinary matching of `E_delta` and let `H` be the union of its edges. By maximality, `H` meets every edge in `E_delta`. If its size is `r`, then either `r<=1` or (3.5) gives `r<=(Gamma_*/delta)^(1/ell)`. Hence

`boxed:
 |H| <= ell * max{1,(Gamma_*/delta)^(1/ell)},
 and every S with D_S>=delta intersects H.`                                (3.6)

This is the requested **optimized-currency-or-physical-hub** alternative. It pays no reciprocal of one arbitrarily chosen tiny minor.

A sharp two-edge corollary is often enough: every minor with

`D_S > Gamma_*/2^ell`                                                       (3.7)

belongs to a pairwise-intersecting family. Otherwise two disjoint such minors, weighted `1/2,1/2`, would give

`Gamma=2^ell sqrt(D_S D_T)>Gamma_*`.

Thus, whenever the superheavy family is nonempty, one of its own `ell` physical rows is a hitting set for every superheavy minor.

What is *not* proved by (3.6) is that the low-determinant residual automatically enters a paid QFORM endpoint. That remains the full-target bridge.

## 4. Fully dense rotated indefinite Hadamard family: exact optimized currency

The optimized theorem is nonvacuous on a high-dimensional genuinely rotated family, and the currency can be computed exactly.

Let `N=4m=2^r` with `r>=3`. Choose three Walsh-Hadamard characters consisting of the constant character and two independent nonconstant characters, and let `B_N` be the corresponding three columns of `H_N/sqrt(N)`. Thus

`B_N^T B_N=I_3`,                                                           (4.1)

and **every physical coefficient** of the `N x 3` cross block is `+-1/sqrt(N)`, hence nonzero. Put

`A_N = [[0_N,B_N],[B_N^T,0_3]].`                                           (4.2)

Its nonzero eigenvalues are exactly

`{+1,+1,+1,-1,-1,-1}`,                                                     (4.3)

so the owner's spectral hypothesis holds with six eigenvalues of modulus one. This is indefinite and is not diagonal in the independent coordinates.

The row sign patterns of `B_N` are

`(+,+,+), (+,+,-), (+,-,+), (+,-,-)`,                                     (4.4)

each repeated `m` times, all scaled by `1/sqrt(N)`.

Take the `m` rows of type `(+,+,+)` as the physical hub bank `H`. They have rank one. With

`U=m^(-1/2)(1,...,1)^T`,

its hub-to-right block factors as `U M_J` with

`M_J=(1/2)(1,1,1),     S=||M_J||=sqrt(3)/2.`                              (4.5)

The one-dimensional orthogonal projection `W=U^T X_H` has density cap

`M_H<=sqrt(2)`                                                             (4.6)

by the same cap-one product projection theorem used in the source projected-crossing proof.

Project the remaining `3m` physical coefficient rows orthogonally to `(1,1,1)`. Up to the common factor `1/sqrt(N)`, the three residual directions are

`v_1=(2/3, 2/3,-4/3),`
`v_2=(2/3,-4/3, 2/3),`
`v_3=(4/3,-2/3,-2/3),`                                                     (4.7)

each repeated `m` times. A pair from the same class has zero Gram determinant. Every pair from different classes has

`D = det Gram(v_a/sqrt(N),v_b/sqrt(N))
   = 16/(3N^2)
   = 1/(3m^2).`                                                            (4.8)

There are `3m^2` positive physical two-row minors. Choose the uniform law over all of them. Every one of the `3m` active light rows is incident to `2m` of those edges, so

`alpha_i=2/(3m)<=1/2.`                                                     (4.9)

Its currency is

`Gamma = D * exp[-sum_i alpha_i log alpha_i]
       = [1/(3m^2)] * (3m/2)^2
       = 3/4.`                                                             (4.10)

This is in fact the exact optimum. All positive minors have the same `D`, while every feasible law has `sum_i alpha_i=2`. Concavity of `-a log a` gives

`-sum_i alpha_i log alpha_i
 <= -3m*(2/(3m))*log(2/(3m))
 = 2 log(3m/2),`                                                           (4.11)

with equality exactly at the uniform marginals above. Therefore

`boxed: Gamma_(2,1/2)(C)=3/4.`                                             (4.12)

Apply (1.2) with `k=1`, `ell=2`, `d=3`, (4.5), (4.6), and (4.12). The powers simplify exactly:

`||p_(X^T A_N X)||_infinity
 <=3*2^(7/6)*(sqrt2)^(1/3)*(sqrt3/2)^(-1/3)*(3/4)^(-1/6)`
` = boxed: 4*3^(2/3)
 =8.320335292207616... .`                                                  (4.13)

This holds for **every** admissible independent cap-one product law and every `N=2^r>=8`. The characteristic function belongs to `L^1`, hence the density is continuous and vanishes at infinity.

The dimension-free value (4.12) also shows why optimizing the whole minor law matters. Any certificate based on only two disjoint positive pairs has

`Gamma_two=4D=4/(3m^2)`,                                                   (4.14)

which decays as `m^-2`; the diffuse optimized law uses all `3m^2` pairs and keeps `Gamma_*=3/4` independent of dimension.

## 5. Completed peer theorem applied at an actual inequality

The designated partner is `account04/B04`. Fresh direct repository checks found current QFORM login/start evidence (latest observed start commit `476b42beea636c37af63c1be96c002649e36a97f`) but no completed current-QFORM canonical report or shared handoff. I therefore do **not** fabricate a designated-partner theorem and do not wait for it.

I did apply the completed same-role peer result `QFORM-Q1-EXACT-MARGINAL-FACTOR-v1` from

`yspennstate/math-open-problems@b1b60d0a4fe67c2e41a60bd38fb88668bbb9b378:proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T154425Z-account01-B04-QFORM-auto11-r14/REPORT.md`

to the *same* matrix `A_N`.

For the canonical squared `3x3`-minor law of `B_N`, Cauchy-Binet gives

`G=E_3(B_N)=det(B_N^T B_N)=1.`                                              (5.1)

Because `B_N^T B_N=I_3`, the canonical row-inclusion marginal equals the row leverage:

`alpha_i=||row_i(B_N)||^2=3/N<=1/2.`                                       (5.2)

All three right columns are present in every third minor, so `beta_j=1`. The exact marginal factor in the peer theorem is therefore

`R=(1-3/N)^(-(N-3)/2).`                                                    (5.3)

Its actual inequality yields

`boxed:
 ||p_(X^T A_N X)||_infinity
 <=3(1-3/N)^(-(N-3)/6)
 <3 sqrt(e)
 =4.946163812100385... .`                                                  (5.4)

The strict final inequality follows from `-log(1-x)<x/(1-x)` for `0<x<1`, with `x=3/N`. The peer characteristic-function theorem also proves a continuous `C_0` density. Thus the same Hadamard family receives an independent, sharper product-Fourier certificate; equation (4.13) is retained because it is the explicit consequence of the **new dual/hub mechanism**, while (5.4) is the required completed-peer application.

## 6. Scope, failure mode, and next implication

The new theorem does not prove that the bare three-large-eigenvalue hypothesis forces an original-coordinate grouped-hub split with target-scale `M_H`, `S`, and `Gamma_*`. It therefore does not solve the full conjecture.

What is now rigorous is the following intermediate alternative inside the projected-crossing branch:

1. if optimized marginal-balanced currency is quantitatively large, (1.2) gives an explicit continuous-density bound;
2. if it is small, every thresholded family of large physical `ell`-minors has a bounded physical hitting set by (3.6), with the exact size/currency tradeoff;
3. for the particularly heavy threshold `Gamma_*/2^ell`, one physical `ell`-set hits all heavier minors.

The next B04 obligation is therefore

`QFORM-OPTIMIZED-CURRENCY-HUB-TO-PAID-ENDPOINT-v1`:

route the bounded hitting set from (3.6), together with the low-determinant residual, into an already-paid pair/star/ridge/grouped-bank/exact-rank endpoint **without** paying a reciprocal of an arbitrarily small local minor and without deleting an unbounded fragmented-support perturbation.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Full-target continuity remains open separately. Independent review of the new dual/hub theorem is pending.

No Gaussianity, moments, log-concavity, compact support, connected support, diagonal-basis independence, or centered-interval extremality is assumed. No Monte Carlo evidence enters the proof. No scheduler state, email, push notification, public release, paid model/API call, cross-account authentication, permission, or task identity was changed.

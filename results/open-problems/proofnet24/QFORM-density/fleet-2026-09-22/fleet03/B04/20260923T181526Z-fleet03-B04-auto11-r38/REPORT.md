SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T18:15:26Z.
attacking: optimize the arbitrary-weight projected-crossing currency and prove a quantitative dual-or-physical-hub alternative.

# fleet03/B04 r38 — optimized projected-crossing dual and hub certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW SUPPORTING THEOREM / EXPLICIT ROTATED INDEFINITE ESTIMATE / FULL TARGET OPEN`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture is not proved here. The branch below proves a continuous `C_0` density under an optimized projected-crossing certificate and quantifies the physical compound-hub obstruction when that certificate is small. It never rotates the random coordinates and never uses law-uniform pointwise quadratic-phase decay.

## 1. Source boundary


The analytic input from this worker's preceding run is

`yspennstate/math-open-problems@ea2f45957db06473799ce27affa30162fda98982:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T165007Z-fleet03-B04-auto11-r37/REPORT.md`,

which proves the arbitrary-weight projected-crossing estimate. In its notation, for a projected crossing matrix `C`, a probability law `w` on positive `ell`-row Gram minors `D_S=det(C_S C_S^T)>0`, and inclusion marginals `alpha_i<=1/2`, define

`Gamma(w;C)=exp(sum_S w_S log D_S - sum_i alpha_i log alpha_i)`.

In the grouped-hub setup with `d=k+ell>2`, hub density cap `M_H`, hub-crossing singular-value product `S`, the proved Fourier inversion bound is

`||p_Q||_infinity <= [d/(d-2)] 2^((k+3ell)/(2d)) M_H^(1/d) S^(-1/d) Gamma(w;C)^(-1/(2d)).`   (1.1)

It also gives `phi_Q in L^1`, hence `p_Q in C_0`.

## 2. Optimized currency and exact convex dual

Let `E` be the finite family of positive `ell`-minors of `C`. Define

`Gamma_* = sup { Gamma(w;C): w is a probability on E, alpha_i(w)<=1/2 for every i }`,   (2.1)

with `Gamma_*=0` if the feasible set is empty.

### Theorem `QFORM-OPTIMIZED-PROJECTED-CROSSING-DUAL-v1`

If the feasible set in (2.1) is nonempty, then

`log Gamma_*
 = inf_(y in R^m) [ max_(S in E)( log D_S + sum_(i in S)y_i ) + sum_i g(y_i) ],`   (2.2)

where

`g(y)= exp(-1-y)` for `y>=log 2-1`,
`g(y)= (log 2-y)/2` for `y<log 2-1`.                         (2.3)

#### Proof

Introduce independent variables `alpha_i=sum_(S containing i)w_S` and multipliers `y_i` for these equalities, and `mu_i>=0` for `alpha_i<=1/2`. The Lagrangian for the concave maximization is

`L = sum_S w_S log D_S - sum_i alpha_i log alpha_i
     + sum_i y_i(sum_(S containing i)w_S-alpha_i)
     + sum_i mu_i(1/2-alpha_i).`

For fixed `(y,mu)`, maximizing over the simplex in `w` gives

`max_S(log D_S+sum_(i in S)y_i)`.

For each `alpha_i>=0`,

`sup_alpha[-alpha log alpha-(y_i+mu_i)alpha]=exp(-1-y_i-mu_i)`.

Thus the dual is

`inf_(y,mu>=0) { max_S(log D_S+sum_(i in S)y_i)
                 +sum_i[ exp(-1-y_i-mu_i)+mu_i/2 ] }`.        (2.4)

Strong duality follows by applying finite-dimensional convex duality to the relaxed cap `alpha_i<=1/2+epsilon`, for which any feasible point of (2.1) is strict; then let `epsilon downarrow0`. Compactness of the probability simplex and continuity of the primal objective give convergence of primal optima to (2.1), while the dual objectives decrease pointwise to (2.4). Finally minimize (2.4) in each `mu_i`: for `c=exp(-1-y_i)`, the minimum of `c exp(-mu)+mu/2` is `c` if `c<=1/2`, and `1/2+(1/2)log(2c)` otherwise. This is exactly (2.3). QED.

This dual makes the obstruction to product Fourier inversion explicit: small `Gamma_*` means no marginal-balanced fractional packing of physical `ell`-minors has large determinant/entropy currency.

## 3. Canonical disjointness gives either Fourier currency or a physical hub

Let

`Z=sum_(S in E) D_S`,   `nu_S=D_S/Z`,                         (3.1)

and draw independent `S,T~nu`. Put

`delta=P(S intersect T = empty)`.                              (3.2)

### Theorem `QFORM-PROJECTED-CROSSING-DUAL-OR-HUB-v1`

For every projected crossing matrix `C` and every `ell>=1`:

1. If `delta=0`, then every positive minor meets any fixed `S_0` in the support of `nu`; hence deleting the at most `ell` physical rows `S_0` annihilates all `ell`-volume.
2. If `delta>0`, then

`boxed: Gamma_* >= Z exp(-ell) sqrt(delta).`                   (3.3)

3. In all cases there is a physical `ell`-set `S_0` in the support such that the residual `ell`-volume after deleting it satisfies

`boxed: Z_out(S_0) <= delta Z <= exp(2ell) Gamma_*^2/Z.`       (3.4)

Here the last inequality is interpreted trivially when `Gamma_*=0`.

#### Proof

If `delta=0`, the positive-minor support is pairwise intersecting, proving item 1.

Assume `delta>0` and condition `nu x nu` on the event `S intersect T=empty`; call the resulting symmetric law `mu`. Its one-coordinate marginal `w` is the same on both sides. Since `S,T` are disjoint,

`2 alpha_i(w)=P_mu(i in S)+P_mu(i in T)<=1`,                  (3.5)

so `w` is feasible for (2.1). Relative entropy gives

`D(mu || nu x nu)=log(1/delta)
 =2D(w||nu)+I_mu(S;T)`,                                       (3.6)

hence `D(w||nu)<= (1/2)log(1/delta)`.

Since `nu_S=D_S/Z`,

`sum_S w_S log D_S = log Z-H(w)-D(w||nu)`.                   (3.7)

Entropy subadditivity gives `H(w)<=sum_i h(alpha_i)`. Therefore

`H(w)+sum_i alpha_i log alpha_i
 <=sum_i[-(1-alpha_i)log(1-alpha_i)]
 <=sum_i alpha_i=ell`,                                        (3.8)

where `-(1-a)log(1-a)<=a`. Combining (3.6)-(3.8) yields (3.3).

For (3.4), define `q(S)=nu{T:T intersect S=empty}`. Since `E_nu q(S)=delta`, some supported `S_0` has `q(S_0)<=delta`. But exactly

`Z_out(S_0)=Z q(S_0)`.                                        (3.9)

The second inequality in (3.4) is the square of (3.3). QED.

Thus failure of the optimized Fourier certificate has a concrete finite-dimensional residue: a bounded physical hitting set captures almost all compound volume.

### One-hub, second-compound corollary

Take `k=1, ell=2`, so `d=3`. If every physical pair deletion leaves at least `eta Z` of second-compound volume, then `delta>=eta`, hence

`Gamma_* >= e^(-2) sqrt(eta) Z`.                              (3.10)

Substitution into (1.1) gives

`boxed:
 ||p_Q||_infinity
 <=3*2^(7/6)*e^(1/3)*eta^(-1/12)
    M_H^(1/3) S^(-1/3) Z^(-1/6).`                            (3.11)

For `eta=1/16`, the numerical coefficient is

`6 sqrt(2) e^(1/3)=11.842164116238918...`.                    (3.12)

This branch has a continuous `C_0` density.

## 4. Fully dense rotated indefinite example where canonical weighting fails

Let

`r0=(1,1,1,1)/2`,
`u =(1,1,-1,-1)/2`,
`v =(1,-1,1,-1)/2`.                                           (4.1)

These are mutually orthonormal and have no zero physical coordinates. Form a `26 x 4` cross block `B` whose first row (the hub) is `r0`; whose next row is `5u`; whose next sixteen rows are copies of `u`; and whose final eight rows are copies of `v`. Let

`A_*=[[0_26,B],[B^T,0_4]].`                                   (4.2)

Every physical cross coefficient is nonzero. Moreover

`B^T B = r0 r0^T +41 uu^T+8 vv^T`,                            (4.3)

so

`spec_nonzero(A_*)={+-1,+-sqrt(41),+-2sqrt(2)}`.              (4.4)

Thus `A_*` is genuinely rotated and indefinite and has six eigenvalues of modulus at least one.

Project away the hub row `r0`. Because `u,v` are orthogonal to `r0`, the projected crossing matrix `C` is simply the remaining 25 rows. Its positive two-row Gram minors are exactly the `u-v` pairs. Their total currency is

`Z=E_2(C)=(25+16)*8=328`.                                     (4.5)

The canonical minor law factorizes into a `u`-side law with weights

`(25/41,1/41,...,1/41)`                                      (4.6)

and a uniform eight-point `v`-side law. Hence the heavy physical row has canonical inclusion marginal

`25/41=0.609756...>1/2`,                                     (4.7)

so the q=1 canonical projected-crossing theorem is unavailable.

The optimized currency can nevertheless be computed exactly. Any feasible pair law has `u`-marginal `r` and `v`-marginal `c`, and

`log Gamma = [sum_i r_i log d_i-sum_i r_i log r_i]
            +[sum_j c_j log 1-sum_j c_j log c_j],`            (4.8)

where `d=(25,1,...,1)`. Conversely any capped marginals `r_i,c_j<=1/2` are realized by the product coupling `w=r x c`, so the maximization factorizes. The capped entropy optimizer is

`r_heavy=1/2`, `r_light=1/32` for each of sixteen lights,
`c_j=1/8` for each of eight `v` rows.                           (4.9)

The two factors are respectively `40` and `8`; therefore

`boxed: Gamma_*=320.`                                         (4.10)

For this grouped split `M_H<=1`, `S=||r0||=1`, `k=1`, `ell=2`. Equation (1.1) gives, for every admissible independent cap-one product law,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=3*2^(7/6)*320^(-1/6)
 =3*(2/5)^(1/6)
 =2.5751226567976713... <2.576.`                              (4.11)

The density is continuous and vanishes at infinity.

This is genuinely an optimization gain rather than a repackaged canonical estimate. The exact canonical disjointness probability is

`delta=(1040/1681)*(7/8)=910/1681=0.5413444378...`,           (4.12)

and the conditioned-disjoint construction of Section 3 gives `Gamma=295.8810726...`, already enough for `||p_Q||inf<=2.608976`, but the exact dual optimizer improves this to (4.11).

Every two-row deletion also leaves substantial second volume; the smallest remainder is obtained by deleting the heavy `u` row and one `v` row and equals `112=(14/41)Z`. Hence the general corollary (3.11) applies with `eta=14/41`, while the exact optimization is substantially sharper.

## 5. Completed peer result applied at an actual inequality

The designated partner is `fleet04/B04`. Fresh direct lookups still found no completed current-QFORM canonical report or shared handoff for that slot, consistent with the current owner reconciliation note. I do not fabricate a designated-partner theorem.

I did apply the latest completed same-role peer result from fleet01/B04:


On the exact matrix (4.2), its canonical two-volume maximum marginal is `25/41`, so choose

`q=50/41`, `D_q=q+2=132/41`.                                  (5.1)

Because the canonical pair law factorizes across the `u/v` banks, its peer entropy factor is exactly `E(w)=1`. The peer theorem therefore yields the actual inequality

`||p_Q||_infinity
 <= [33/8] 2^(37/33) (50/41)^(-41/132) 328^(-41/264)
 =3.431228664105789...`.                                      (5.2)

Thus the new optimized q=1 weighting in (4.11) improves an already-valid fractional canonical certificate on the same target-valid matrix.

## 6. Scope and remaining implication

The theorem does **not** show that the bare three-large-eigenvalue hypothesis forces a grouped-hub split with target-scale `S*Gamma_*^(1/2)`. Full QFORM therefore remains OPEN, and full-target continuity remains OPEN separately.

The precise next implication is `QFORM-OPTIMIZED-CROSSING-HUB-SPLICE-v1`: when (3.4) produces an at-most-`ell` physical compound hub capturing nearly all crossing volume, promote those rows into the existing grouped-hub/pair/star/ridge cascade without paying a reciprocal of a vanishing local coefficient, and prove that iterating the promotion terminates with a universal target-scale certificate. This is the product-preserving bridge still missing from the unrestricted theorem.

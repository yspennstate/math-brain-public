SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T18:24:51Z.
attacking: heavy-row rotated cross blocks: optimize three-volume currency, apply the pinned fifth-volume bound, and compare both with the partner projected-crossing hub certificate and direct ridge gates on the same physical matrix.

# account02/B04 — heavy-row hub extraction beats globally optimized ambient volume

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW SUPPORTING SEPARATION / EXPLICIT TARGET-VALID ESTIMATE / FULL TARGET OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains open.  The result below is an explicit target-valid mechanism separation: on one dense rotated indefinite family I solve the admissible third-volume entropy optimization globally, apply the pinned fifth-volume theorem, exhibit a valid ridge certificate, and show that extracting one physical hub before applying the newest projected-crossing product-Fourier theorem gains a strictly better power of the large physical scale.  No random variable is rotated and no law-uniform pointwise quadratic-phase decay is used.

## 1. Sources and correction boundary


The pinned Claude/e5 source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I use two completed results from it at actual equations:

* Theorem D, including its arbitrary-weight remark: a physical 3-volume law with constrained-side row marginals at most `1/2` gives the determinant/entropy Fourier certificate.
* Theorem `D_5` from `FOURIER_ROUTE_REPORT.md`: for any physical cross block `M`, with no marginal assumption,

`||p_Q||_infinity <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`.

The arbitrary-weight fractional extension used for the exact three-volume optimization is the completed account03/B04 result

`QFORM-ENTROPY-WEIGHTED-DPRIME-v1`

at `yspennstate/math-open-problems@5b241b14339d94c847043e8ab09d711f56ed2dbe`, which gives, for `1/2<=h<3/4`,

`||p_Q||_infinity <= C_F(h) G_h(M)^(-1/6)`,

`C_F(h)=6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1)`,

where `G_h` is the supremum of the determinant-entropy currency over physical 3x3-minor laws with every constrained-side row marginal at most `h`.

The newest designated-partner input is account03/B04 r38 at

`yspennstate/math-open-problems@62656f0fee1b07c9abf0291ea4a1e12ec9bfb856`, with its late overlap note at `519165c7af84594abee493cdb39992b39c66b6d6`.  The genuinely new r38 statement used below is the canonical-disjointness aggregate-volume alternative

`Gamma_* >= Z exp(-ell) sqrt(delta)`

and

`Z_out(S_0) <= delta Z <= exp(2ell) Gamma_*^2/Z`,

for some actual physical `ell`-set `S_0`, together with the preceding r37 arbitrary-weight projected-crossing density theorem.  The late note explicitly warns that the bare spectral hypothesis does not force a particular singleton/star currency to universal scale; this run does not make that false inference.

The completed ridge theorem used for comparison is `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md@9c1167db05c7b0f520f060796fde921ed769a4e7`.

I do not use the refuted arbitrary-joint coarea bound, conditional projection-cap moments, spectral-basis independence, a uniformly good single physical minor, or uniform pointwise Fresnel decay.

## 2. Dense target family

Let

`V = I_5 - (2/5) 11^T`,

`D_L = diag(L,1,1,1,1)`,

`M_L = D_L V`, with `L>=1`.

Since `(11^T)^2=5(11^T)`,

`V^2=I_5`.

Thus `V` is orthogonal.  Its diagonal entries are `3/5` and every off-diagonal entry is `-2/5`, so **all 25 physical coefficients of M_L are nonzero**.  Also

`M_L M_L^T = diag(L^2,1,1,1,1)`,

so the singular values are exactly

`L,1,1,1,1`.

Embed it as

`A_L = [[0,M_L],[M_L^T,0]]`.

Then

`spec(A_L)={+L,-L,+1,-1,+1,-1,+1,-1,+1,-1}`.

For every `L>=1`, this is genuinely non-diagonal in the physical product coordinates, indefinite, and all ten eigenvalues have modulus at least one.  It therefore lies inside the exact owner target.

## 3. Pinned e5 results on the same matrix

### 3.1 The original q=1 third-volume theorem has no admissible weight

For every probability law `w` on supported physical `3x3` minors, the five constrained-side row inclusion marginals satisfy

`sum_i alpha_i(w)=3`.

If all were at most `1/2`, the sum would be at most `5/2`, impossible.  Hence **the arbitrary-weight form of the pinned Theorem D has no admissible weight at all** on this matrix.  This is an obstruction to that intermediate certificate, not to QFORM.

### 3.2 The pinned fifth-volume theorem gives an actual inequality

Because the five squared singular values are `L^2,1,1,1,1`,

`e_5(M_L^T M_L)=L^2`.

The completed pinned `D_5` theorem therefore gives, for every admissible independent cap-one product law,

`boxed: ||p_(X^T A_L X)||_infinity <= 5 sqrt(2e) L^(-1/5).`      (3.1)

This is the required direct application of a completed e5 result to an actual target-valid inequality.

## 4. Exact global optimization of all admissible third-volume weights

Fix `h` with `3/5<=h<3/4`.  I now solve `G_h(M_L)` globally, including the physical column-minor weights.

For a fixed physical row triple `S`, put

`z_S=sum_(|T|=3) det(M_{S,T})^2`.

Cauchy-Binet and the diagonal row Gram matrix give

`z_S=det((M_L M_L^T)_{S,S})`

and hence

`z_S=L^2` if `1 in S`, while `z_S=1` if `1 notin S`.           (4.1)

Let `w_(S,T)` be any supported minor law and `p_S=sum_T w_(S,T)`.  At fixed `p`, the conditional Gibbs/log-sum identity gives

`sup_(w(.|S)) [sum_(S,T) w_(S,T) log det(M_(S,T))^2 + H(w)]`

`= H(p)+sum_S p_S log z_S`.                                    (4.2)

Equality uses the conditional canonical law proportional to `det(M_(S,T))^2` inside each fixed row triple.  Thus the full physical-minor optimization reduces **exactly**, not approximately, to the ten row triples with effective weights (4.1).

Average any optimizer over permutations of the four light rows.  Concavity of entropy cannot decrease (4.2), and the constraints are invariant.  Let

`a=P_p(1 in S)`.

The six triples containing row 1 then have weight `a/6` each and the four light-only triples weight `(1-a)/4` each.  The marginals are

`alpha_1=a`,

`alpha_2=...=alpha_5=(3-a)/4`.

Hence feasibility is exactly

`3-4h <= a <= h`.                                               (4.3)

The exact currency at parameter `a` is

`G(a)=L^(2a) exp(H_Ber(a)) 6^a 4^(1-a)`.                       (4.4)

The unconstrained maximizer is

`a_nat=3L^2/(3L^2+2)`.

For `L>=sqrt(2)`, `a_nat>=3/4`, so throughout the proved D-prime window the constrained optimum saturates the heavy-row marginal:

`boxed: G_h(M_L)=L^(2h)(6/h)^h(4/(1-h))^(1-h),`

`3/5<=h<3/4, L>=sqrt(2).`                                      (4.5)

Thus the globally optimized D-prime certificate is

`B_vol(h;L)=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) G_h(M_L)^(-1/6).`  (4.6)

Its logarithmic derivative is

`d/dh log B_vol`

`= -1/(2h)+4/(3-4h) -(1/3)log L`

`  -(1/6)log((3/2)(1-h)/h)`,                                  (4.7)

and

`d^2/dh^2 log B_vol`

`=1/(2h^2)+16/(3-4h)^2 +(1/6)(1/(1-h)+1/h) >0.`               (4.8)

So the optimization in `h` is strictly convex and has no hidden local minima.

At the support threshold `h=3/5`,

`(d/dh log B_vol)|_(3/5)=35/6-(1/3)log L`.                     (4.9)

Therefore, throughout the huge range

`sqrt(2)<=L<=exp(35/2)=39824784.3975...`,

the **global optimum over every admissible physical third-minor weight and every D-prime threshold** occurs at

`h_*=3/5`,

with the uniform row-triple law and

`G_(3/5)=10 L^(6/5)`.                                          (4.10)

The exact optimized bound in that range is

`boxed: B_vol,opt(L)`

`=10^(5/6) sqrt(5e/6) L^(-1/5)`

`=10.2539206248... L^(-1/5).`                                 (4.11)

For completeness, when `L` is asymptotically larger than `exp(35/2)`, strict convexity gives a unique interior optimizer `h_L`.  Equation (4.7) yields

`h_L=3/4-3/log L+O((log L)^(-2))`,

and substitution in (4.5)-(4.6) gives

`B_vol,opt(L)=Theta((log L)L^(-1/4)).`                         (4.12)

Thus even allowing **all** physical minor weights and optimizing the fractional exponent cannot reproduce the `L^(-1/3)` power obtained below by first promoting the heavy physical row to a hub.

## 5. Newest partner theorem applied after one physical hub promotion

Take physical left coordinate 1 as the hub.  Its right coefficient row is

`m=L v_1`,

where `v_i` denotes row `i` of `V`.  The hub density cap is `M_H<=1`, and the rank-one hub-crossing singular product is

`S=L`.

Because the rows of `V` are orthonormal, projecting the other four coefficient rows off `span(v_1)` changes nothing.  The projected residual crossing `C` consists of the four orthonormal rows

`v_2,v_3,v_4,v_5`.

For `ell=2`, every one of its six positive pair Gram determinants equals one.  Hence

`Z_2=6`.

Under the canonical pair law, two independent pair minors are disjoint exactly when they are complementary pairs, so

`delta=1/6`.

The newest account03/B04 r38 theorem therefore applies at an actual equation and gives

`Gamma_* >= 6 e^(-2) sqrt(1/6)=sqrt(6)e^(-2)`,                (5.1)

and a physical pair deletion with residual second compound volume at most

`delta Z_2=1`.                                                  (5.2)

Here the exact optimizer can be solved further.  Every feasible pair law has four marginals summing to two and each at most `1/2`; hence every marginal is exactly `1/2`.  Since every pair determinant is one,

`Gamma(w;C)=exp(-sum_i alpha_i log alpha_i)=4`

for every feasible law.  Thus

`boxed: Gamma_*(C)=4.`                                         (5.3)

Insert (5.3) into the completed account03/B04 r37 grouped-hub projected-crossing theorem with `k=1`, `ell=2`, `d=3`, `M_H=1`, `S=L`.  This gives

`boxed: ||p_(X^T A_L X)||_infinity`

`<=3*2^(5/6) L^(-1/3)`

`=5.34539230884... L^(-1/3).`                                 (5.4)

The theorem also gives an `L^1` characteristic function and hence a continuous `C_0` density for this displayed family.  No post-rotation independence is used: the hub is an original physical coordinate and the projection occurs only in deterministic coefficient space.

Equation (5.4) is the key mechanism separation.  On the same physical matrix, the full-block optimized third-volume family has asymptotic order `(log L)L^(-1/4)` at best, while promoting one physical hub exposes a residual pair packet and yields `L^(-1/3)`.

## 6. Ridge certificate on the identical physical cut

For the completed ridge theorem, write `g=gamma^2`.  Since `M_L M_L^T=diag(L^2,1,1,1,1)`,

`K_gamma=diag(k_1,k,k,k,k)`,

`k_1=L^2/(L^2+g)`,

`k=1/(1+g)`,

`theta=k_1+4k`,

`D_gamma=(1+L^2/g)(1+1/g)^4`.                                (6.1)

For every `L>2`, take

`g=1/L`,

`q=2k_1`.

Then `1<q<2` and the leverage gate is saturated:

`max_i K_ii=k_1=q/2`.

The strict trace gap is

`theta-2q=4k-3k_1`

`= L(L-2)^2/(L^3+1) >0`.                                      (6.2)

Thus the completed ridge theorem gives the valid same-matrix certificate

`B_ridge(L)`

`= e/[sqrt(2q) gamma] * theta/(theta-2q) * D_gamma^(-1/(2theta)).`  (6.3)

At this displayed scale,

`B_ridge(L)=(5e/2+o(1)) L^(-1/5)`                             (6.4)

as `L->infinity`.  I do **not** claim that `g=1/L` globally optimizes the ridge theorem; it is a valid explicit scale sufficient for the mechanism comparison.

## 7. Concrete same-matrix hierarchy at L=4096

Take `L=4096`.  The deterministic checks give

`Gamma_(3/5)=216188.1761010309`,

and (4.9) is positive (`3.06074461109...`), so `h=3/5` is rigorously the global optimum of the entire admissible D-prime third-volume family.

The four certified bounds on this exact physical matrix are

`projected-crossing hub: 0.3340870193026273`,

`ridge at g=1/L:          1.2869617567820861`,

`globally optimized D':   1.9427546703383627`,

`pinned D_5:              2.208819631319392`.

So

`boxed: 0.3341 < 1.2870 < 1.9428 < 2.2089.`                   (7.1)

The comparison is not between different matrices or rotated input laws.  It is four certificates for the **same dense physical target matrix A_4096**.

## 8. What this advances and what remains unpaid

This family proves a useful structural lesson for the current compound-hub branch:

**optimizing ambient volume weights is not a substitute for hub promotion.**

Even after optimizing every physical third-minor weight and the full proved fractional D-prime window, the heavy physical direction can only be used through a marginal cap `h<3/4`, leading asymptotically to the `L^(-1/4)` barrier (with a logarithmic factor).  The no-marginal fifth-volume theorem and the displayed ridge scale both pay only `L^(-1/5)`.  Promoting the actual physical heavy row to the grouped hub changes the product-Fourier dimension accounting and exposes a balanced lower-order crossing packet, giving `L^(-1/3)`.

This is not a proof that every low optimized-currency configuration forced by the owner hypothesis has such a promotion.  The newest partner correction explicitly rules out forcing one particular singleton/star scale from the three-large-eigenvalue hypothesis alone.

The first unpaid implication is therefore sharpened to

`QFORM-AGGREGATE-VOLUME-HUB-PROMOTION-WITH-RESIDUAL-PACKET-v1`:

starting from the account03/B04 r38 physical deletion certificate

`Z_out(S_0) <= exp(2ell) Gamma_*^2/Z`,

prove that either a bounded subset of `S_0` can be promoted to a grouped physical hub while a target-scale lower-order projected crossing packet survives, or the low residual compound volume forces a completed `D_5`, ridge, exact-rank, pair, or diagonal-plus-low-rank endpoint.  The promotion must preserve original-coordinate product provenance and must not invert a vanishing local coefficient.

Full unrestricted QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`.  Continuity remains a separate issue outside the explicit branches whose Fourier proofs are integrable.

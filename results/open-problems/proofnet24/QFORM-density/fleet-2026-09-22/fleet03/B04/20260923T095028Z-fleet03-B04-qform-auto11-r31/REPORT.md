# QFORM fleet03/B04 r31 — entropy-dual product-Fourier exit or finite compound hub

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW SUPPORTING THEOREM / FULL TARGET OPEN`  
Execution label: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and this run's first missing implication

The full target remains: for every dimension, independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove that Q=X^T A X has a universally bounded density, or give a valid counterexample. No Gaussianity, moment, compact-support, connected-support, log-concavity, iid, diagonal-basis, or post-rotation independence assumption is used below.

The previous fleet03/B04 run proved a soft-ridge third-volume exit for an original-coordinate cross block M and showed that failure in both orientations creates an aggregate physical row hub and column hub. Its unpaid step was to convert that concentrated geometry into a dimension-free endpoint without selecting a vanishing entry.

This run attacks that step by changing the object being optimized. Instead of using the natural squared-minor law, optimize the determinant-weighted entropy currency over all admissible physical 3x3-minor weights. The convex dual has a useful consequence: either the optimized product-Fourier certificate is already quantitatively large, or a bounded number of physical rows captures almost all third singular volume. Applying the same argument to M^T gives a bounded row/column compound hub. Exact infeasibility gives an even sharper rank-at-most-two deletion statement.

The theorem is supporting, not a solution of the unrestricted conjecture: the final finite-compound-hub payment into a universal target endpoint is still missing.

## 2. Inputs used and correction discipline

The analytic input is the completed volume-sampling Brascamp--Lieb Fourier theorem and its arbitrary-weight determinant remark from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

and the q/Jensen extension in the same commit,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

The exact rank-two fractional-potential theorem used on the support-deficient residue is the completed fleet03/B18 result

`yspennstate/math-open-problems@dfbc17f17b702ed7c7191ba24648a70f67dda851`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T092851Z-fleet03-B18-QFORM-r26/REPORT.md`.

It proves, for disjoint original-coordinate banks and arbitrary measurable same-side terms,

`sup_u E |R-u|^(-1/2) <= [4r/(r-1)] (prod_{ell=1}^r sigma_ell)^(-1/(2r))`

when the physical cross block has rank r>=2. In particular rank two gives `8(sigma_1 sigma_2)^(-1/4)`.

The designated fleet04/B04 worker had current QFORM login/start evidence but no completed current-QFORM canonical report or shared handoff visible in the fresh direct lookup for this run, so no designated-partner theorem is invented.

The proof below respects the live corrections: there is no law-uniform pointwise quadratic-phase decay, no arbitrary-joint coarea shortcut, no independence after spectral rotation, no naive fiber-supremum step, and no claim that the three-large-eigenvalue hypothesis forces a good single physical minor or a rank-three physical cut.

## 3. Cross-block notation and entropy currency

Let I,J be disjoint original-coordinate banks and let

`M=A_{I,J}`.

Let E be the finite set of ordered physical pairs `e=(S,T)` with `S subset I`, `T subset J`, `|S|=|T|=3`, and

`a_e = det(M_{S,T})^2 > 0`.

Write

`Z = sum_{e in E} a_e = e_3(M^T M)`.

We assume Z>0 when discussing third-volume certificates. The natural squared-minor law is

`nu_e = a_e/Z`.

For a probability weight w on E, define its row-inclusion marginals

`alpha_i(w)=sum_{e: i in S_e} w_e`

and its determinant-entropy currency

`G(w)=exp( sum_e w_e log a_e + H(w) )`,

where

`H(w)=-sum_e w_e log w_e`.

Fix `h` with

`1/2 <= h < 3/4`.

Define the feasible polytope

`C_h={w: w is a probability on E and alpha_i(w)<=h for every i in I}`

and

`G_h(M)=sup_{w in C_h} G(w)`,

with `G_h(M)=0` when `C_h` is empty.

Because `nu_e=a_e/Z`, the elementary identity

`log G(w)=log Z-D(w||nu)`                                                    (3.1)

holds for every supported w. Hence `0<G_h<=Z` whenever the feasible set is nonempty.

## 4. Arbitrary-weight q-Fourier theorem

### Theorem 4.1 — QFORM-ENTROPY-WEIGHTED-DPRIME-v1

If `G_h(M)>0`, then the full quadratic form, after conditioning any outside original coordinates, has a continuous density vanishing at infinity and

`||p_Q||_infinity <= C_F(h) G_h(M)^(-1/6)`,                         (4.1)

where

`C_F(h)=6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1)`.

The same statement is valid after transposing M, so one may optimize either physical orientation.

### Proof

Take any feasible w and put `alpha_i=alpha_i(w)`, `beta_j=P_w(j in T)`. The arbitrary-weight determinant step in the completed Theorem D replaces the natural volume Z by exactly

`G(w)=exp(E_w log a_e+H(w))`.

The proof is a weighted AM--GM inequality in the expansion of

`det(D_J+M^T D_I M)`:

for arbitrary positive Gaussian parameters,

`det(D_J+M^T D_I M) >= G(w) prod_i d_i^{alpha_i} prod_j e_j^{1-beta_j}`.       (4.2)

Now let `q=2h`, so `1<=q<3/2`. In the Jensen extension, apply the same Brascamp--Lieb argument to the q-th power of the decoupled product. Since `alpha_i<=h=q/2`, the one-dimensional Fourier exponent `q/alpha_i` is at least two, exactly the range of the completed product characteristic-function L^p lemma. Repeating the source proof with (4.2) gives

`|phi_Q(t)| <= B |t|^{-3/(2q)}`

with the same q-dependent constant and with Z replaced by G(w). Integrating `min(1,B|t|^{-3/(2q)})` and applying Fourier inversion gives

`||p_Q||_infinity <= C_F(h) G(w)^(-1/6)`.

Take a maximizing sequence in the compact feasible polytope; continuity of (3.1) on the supported simplex gives (4.1). The integrable characteristic-function majorant supplied by this proof yields a continuous C0 density. No pointwise one-dimensional Fresnel estimate is used. QED.

At the fixed value

`h=2/3`,

(4.1) becomes

`||p_Q||_infinity <= 9 sqrt(3e) G_{2/3}(M)^(-1/6)`.              (4.3)

## 5. Exact convex dual

### Lemma 5.1 — entropy dual

If `C_h` is nonempty, then

`G_h(M)=inf_{lambda_i>=0} exp(h L) sum_{e in E} a_e exp(-Lambda_e)`,            (5.1)

where

`L=sum_i lambda_i`,

`Lambda_e=sum_{i in S_e} lambda_i`.

### Proof

By (3.1), maximizing G is equivalent to minimizing `D(w||nu)` over the linear constraints `alpha_i<=h`. The Lagrangian is

`D(w||nu)+sum_i lambda_i(alpha_i-h)`.

For fixed nonnegative lambda, the Gibbs variational identity on the finite edge set gives

`inf_w [D(w||nu)+E_w Lambda_e] = -log sum_e nu_e exp(-Lambda_e)`.

Thus strong finite-dimensional convex duality gives

`D_* = sup_{lambda>=0}[-log(sum_e nu_e e^{-Lambda_e})-hL]`.

Since `G_h=Z exp(-D_*)` and `nu_e=a_e/Z`, this is exactly (5.1). QED.

This dual is the useful rearrangement statement: a poor entropy-balanced minor law can only occur if a small collection of physical coordinates receives a large dual penalty.

## 6. Quantitative finite-hub compression

### Theorem 6.1 — QFORM-ENTROPY-DUAL-COMPOUND-HUB-v1

Assume `G_h(M)>0`. Let `m` be an integer with

`m>3/h`.

Then there exists a set H of physical rows, `|H|<=m`, such that

`E_3(M_{H^c,*}) <= Z (G_h(M)/Z)^kappa`,                          (6.1)

where

`kappa=(1-3/m)/(1-h)>0`.                                       (6.2)

### Proof

Let

`D=log(Z/G_h)>=0`.

For arbitrary epsilon>0, choose nonnegative lambda in (5.1) such that, with

`W=sum_e a_e e^{-Lambda_e}` and `F=e^{hL}W`,

we have

`F <= e^epsilon G_h`.                                           (6.3)

Since every edge is a triple, `Lambda_e<=L`; hence

`W>=Z e^{-L}`.                                                   (6.4)

Combining (6.3)--(6.4) gives

`L >= (D-epsilon)/(1-h)`.                                       (6.5)

Define

`H={i: lambda_i>=L/m}`.

Then `|H|<=m`. If an edge avoids H, all three of its row penalties are below L/m, so

`Lambda_e<3L/m`.

Therefore

`E_3(M_{H^c,*})
 =sum_{e:S_e cap H=empty} a_e
 <= e^{3L/m} W
 = e^{(3/m-h)L}F`.                                              (6.6)

Because `3/m-h<0`, substitute the lower bound (6.5) into (6.6), then use (6.3):

`E_3(M_{H^c,*})
 <= Z exp[-kappa D+o_epsilon(1)]`.

There are only finitely many candidate H, so along an epsilon-to-zero subsequence one H recurs; taking the limit yields (6.1). QED.

### Fixed parameters

Take

`h=2/3`, `m=6`.

Then

`kappa=3/2`,

so some six-row set satisfies

`E_3(M_{H^c,*}) <= Z (G_{2/3}(M)/Z)^(3/2)`.                      (6.7)

Equivalently, if for every physical `H` with `|H|<=6` one has

`E_3(M_{H^c,*}) >= eta Z`,                                      (6.8)

then

`G_{2/3}(M) >= eta^(2/3) Z`.                                    (6.9)

Combining (4.3) and (6.9) gives the explicit continuous-density Fourier exit

`boxed: ||p_Q||_infinity <= 9 sqrt(3e) eta^(-1/9) Z^(-1/6)`.    (6.10)

For `eta=1/16`,

`9 sqrt(3e) 16^(1/9) = 34.973692473606214...`.                  (6.11)

Thus either the product-Fourier estimate closes at that scale, or at least `15/16` of third singular volume uses one of at most six physical rows.

## 7. Two-sided compound-hub dichotomy

Apply Theorem 6.1 independently to M and M^T. At `h=2/3`, `m=6`, `eta=1/16`, either at least one orientation satisfies the Fourier exit (6.10), or there are physical sets

`H_r subset I`, `H_c subset J`, `|H_r|,|H_c|<=6`,

such that

`E_3(M_{H_r^c,*}) < Z/16`,

`E_3(M_{*,H_c^c}) < Z/16`.                                     (7.1)

Under the canonical squared-minor law nu, (7.1) says

`P(S cap H_r=empty)<1/16`,

`P(T cap H_c=empty)<1/16`.

Hence by the union bound

`boxed: P(S cap H_r != empty AND T cap H_c != empty)>7/8`.       (7.2)

So failure of the entropy-optimized Fourier exit localizes more than seven eighths of all physical third determinant volume into minors meeting one fixed at-most-six-row and at-most-six-column compound hub. This is dimension-free and does not select or invert one small coefficient.

For the previous fleet01/B20 substantial-third-volume packet, where the recorded lower bound is `Z>=2^(-18)`, (6.10) gives the explicit alternative

`||p_Q||_infinity <= 34.973692473606214 * 8`

`                    = 279.7895397888497...`                    (7.3)

or the `>7/8` finite compound-hub conclusion (7.2). The earlier B04 soft-ridge gate remains numerically better whenever it fires; the point of (7.3) is a new structural exit on its concentrated complement.

## 8. Exact infeasibility gives rank-two deletion

The dual compression above assumed `G_h>0`. The exactly infeasible endpoint has an even cleaner combinatorial description.

Let H_row be the 3-uniform hypergraph on physical rows whose edges are those triples S for which `det(M_{S,T})!=0` for at least one T.

### Lemma 8.1 — support-deficient hub

If `G_{2/3}(M)=0`, then there is a physical row set H with

`|H|<=4`

such that every supported row triple meets H. Consequently

`rank(M_{H^c,*})<=2`.                                           (8.1)

### Proof

A probability w with row marginals at most h exists if and only if the fractional matching number of the support hypergraph is at least `1/h`: if w is feasible, `x_e=w_e/h` is a fractional matching of total weight `1/h`; conversely a fractional matching of total weight tau>=1/h can be normalized to a feasible probability law.

Thus `G_{2/3}=0` implies the fractional matching number is less than `3/2`. By finite LP duality there is a fractional vertex cover `(y_i)` with

`y_i>=0`, `sum_i y_i<3/2`,

and

`sum_{i in S}y_i>=1`

for every supported triple S. Let

`H={i:y_i>=1/3}`.

If a supported triple avoided H, the sum of its three y-values would be strictly less than one, a contradiction. Moreover

`|H|/3 <= sum_i y_i<3/2`,

so `|H|<9/2` and therefore `|H|<=4`. All 3x3 minors of `M_{H^c,*}` vanish, which is equivalent to (8.1). QED.

The transposed assertion gives the analogous at-most-four-column deletion.

### Actual application of an existing-worker theorem

Condition on the finitely many original coordinates in H. If the residual physical cross block `B=M_{H^c,*}` has rank exactly two, the completed fleet03/B18 theorem applies to each conditional form because conditioning changes only same-side and affine terms. If its two nonzero singular values are `sigma_1,sigma_2`, then uniformly in the conditioned hub coordinates,

`sup_u E( |R-u|^(-1/2) | X_H ) <= 8 (sigma_1 sigma_2)^(-1/4)`.  (8.2)

Averaging gives the same unconditional half-Riesz bound. If the residual rank is at most one, the survivor is an exact lower-cross-rank/star geometry. Equation (8.2) is not by itself an L-infinity theorem; it identifies the remaining scalar-square/zero-pivot/grouped-hub payment precisely rather than hiding it in a high-dimensional concentration statement.

## 9. Genuinely rotated indefinite example where natural volume weighting fails

The entropy optimization is not only a structural fallback; it strictly enlarges the direct Fourier scope.

Let `r=9/10` and define the 6x3 matrix U by its rows

`sqrt(r)e_1`, `sqrt(1-r)e_1`,

`2^(-1/2)e_2`, `2^(-1/2)e_2`,

`2^(-1/2)e_3`, `2^(-1/2)e_3`.

Then `U^T U=I_3`. Let

`R=(1/3) [[1,-2,-2],[-2,1,-2],[-2,-2,1]]`.

R is orthogonal and every entry is nonzero. Put

`M=UR`

and form the 9x9 real symmetric matrix

`A=[[0,M],[M^T,0]]`.

All 18 physical entries of M are nonzero. Since the singular values of M are exactly `1,1,1`,

`spec(A)={+1,+1,+1,-1,-1,-1,0,0,0}`.

Thus A is genuinely rotated and indefinite and has six eigenvalues of absolute value one.

Here

`Z=E_3(M)=1`.

Every nonzero 3x3 minor chooses exactly one row from each duplicate pair and all three columns. The natural squared-minor law factors with row-choice probabilities

`(0.9,0.1)`, `(0.5,0.5)`, `(0.5,0.5)`.

Hence its largest natural row marginal is 0.9. The natural Theorem D fails its 1/2 gate, and even the natural D' extension cannot use any `h<3/4`.

Optimize instead over `h=1/2`. Since exactly one row from each duplicate pair is always selected, both members of every pair must then have marginal exactly one half. The information projection leaves the two fair pairs unchanged and changes only `(0.9,0.1)` to `(0.5,0.5)`. Thus

`D_* = D(Ber(1/2)||Ber(9/10))`

`    = (1/2)log((1/2)/(9/10))+(1/2)log((1/2)/(1/10))`

`    = log(5/3)`.

By (3.1),

`G_{1/2}(M)=exp(-D_*)=3/5`.

The arbitrary-weight Theorem 4.1 at h=1/2 now gives, for every admissible independent cap-one input law,

`boxed: ||p_{X^T A X}||_infinity`

`       <=6 sqrt(e) (3/5)^(-1/6)`

`       =6 sqrt(e)(5/3)^(1/6)`

`       =10.771428003025216...`.                                (9.1)

The density is continuous and vanishes at infinity. This is an explicit rotated indefinite target on which natural third-volume marginals fail even the h<3/4 gate, while entropy rearrangement restores an integrable product-Fourier bound with a completely explicit constant.

## 10. What is proved and what remains

New results of this run:

1. `QFORM-ENTROPY-WEIGHTED-DPRIME-v1`: arbitrary determinant weights with row marginals h<3/4 yield the explicit continuous-density bound (4.1).
2. Exact entropy dual (5.1).
3. `QFORM-ENTROPY-DUAL-COMPOUND-HUB-v1`: poor optimized Fourier currency forces a bounded physical row hub, quantitatively (6.1); applying both orientations gives the >7/8 six-by-six compound-hub concentration alternative.
4. `QFORM-SUPPORT-INFEASIBLE-RANK2-DELETION-v1`: exact failure of a 2/3-balanced minor law forces deletion of at most four physical rows after which cross rank is at most two.
5. Equation-level application of the completed fleet03/B18 rank-two half-Riesz theorem to that exact residue, equation (8.2).
6. Explicit rotated indefinite 9-dimensional target (9.1), with all physical cross coefficients nonzero, where natural volume weighting fails but entropy rearrangement succeeds.

Full QFORM remains OPEN. The next exact B04 obligation is

`QFORM-FINITE-COMPOUND-HUB-PAYMENT-v1`:

start from the survivor in which more than 7/8 of third determinant volume meets fixed physical sets of at most six rows and six columns (or, in the exact infeasible case, deletion leaves cross rank at most two), and combine the finite hub coordinates with a completed mixed-hub, scalar-square, zero-pivot, grouped-bank, or Schur/half-Riesz endpoint while preserving a dimension-free quantitative scale. The key remaining issue is not finding a hub; this run produces one. The issue is paying its potentially small individual coefficients without losing the aggregate third-volume scale.

Continuity is proved for the entropy-Fourier exit and the explicit example. It is not proved for the full conjecture or for the rank-two half-Riesz residue alone.

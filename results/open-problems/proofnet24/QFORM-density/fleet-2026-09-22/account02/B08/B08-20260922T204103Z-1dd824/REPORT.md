SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-22T20:41:03Z.
attacking: the grouped factorized determinant-bank payment in the near-rank-two diffuse bicolop branch, before any reciprocal single-minor selection.

# account02/B08 — double-incident rank-two grouped payment

**Run:** `B08-20260922T204103Z-1dd824`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15` at the prepublication refresh  
**Assignment:** Diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The target remains the full arbitrary-product-law statement: for independent real coordinates with probability densities bounded by one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `X^T A X`, or produce a genuine counterexample. No moments, compact support, centering, regularity of the marginal densities, or independence after spectral rotation is assumed.

The previous B08 run reduced one difficult nonzero-pivot branch to a two-sided physical determinant bank but showed that the bank may be spread over arbitrarily many tiny minors, so choosing one good minor is not dimension-free. The designated partner account03/B08 then sharpened the same branch: in its latest completed run `20260922T201956Z-account03-B08-qform-diffuse-r20`, the unpaid state is within `0.010111 gamma` in Hilbert--Schmidt norm of a rank-two cross block and its normalized double-incident determinant bank is quantitatively close to one factorized top-two exterior mode. The partner's exact-rank-two endpoint was already bounded by `<10.575/sqrt(|a| gamma)`.

The first question attacked here is therefore narrower and source-valid:

> Can the entire double-incident determinant bank be spent directly, without ever selecting one physical minor?

The answer is yes for every exact rank-two physical cross bank. This gives a grouped two-sided payment theorem and improves the partner's exact-rank-two endpoint to `<7.712/sqrt(|a| gamma)`. In the strictly higher-rank partner branch it also proves that the *top rank-two mode itself* is already uniformly payable; only restoration of the very small higher-rank tail remains unpaid.

## 2. Sources actually consumed

1. **Designated partner account03/B08 r20.**  
   `yspennstate/math-open-problems@d5547a484fcc9b62341d80e9ba902cbe2e484284`  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T201956Z-account03-B08-qform-diffuse-r20/REPORT.md`.

   The source proves in its surviving bicolop branch, with physical cross block `H`, scale `gamma`, fine scale `g=gamma/16`, normalized cross matrix `Z=H(g^2 I+H^T H)^(-1/2)`, and physical heavy row/column `j,r`, that the factorized top-two exterior slice has squared Frobenius mass

   `mu_1 mu_2 L_j R_r > A0`,

   where

   `A0 = 158518644736 / 173076800625 > 0.915886`.

   It also proves `e_2(x)>=2/3` for `x_nu=min(1,h_nu^2/gamma^2)`, and in the strictly higher-rank unpaid branch

   `sum_(nu>=3) h_nu^2/gamma^2 < 329/3218176`.

2. **Exact rank-two Fourier endpoint.**  
   account03/B06, `QFORM-EXACT-RANK2-CROSSBANK-L3-v1`, canonical source  
   `yspennstate/math-open-problems@1287456c9a709f8c3f117c23faa46e75f4560d01`  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T194649Z-account03-B06-qform-r17/REPORT.md`.

   Its two-dimensional Plancherel calculation is reused below, but with new grouped physical coordinates whose density caps are paid by the whole incident bank rather than by a spectral projection cap.

3. **One-dimensional product projection cap.**  

4. **Dependence-safe outer square smoothing.**  
   account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, source used in the B06 and partner chains: `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

No false arbitrary-joint coarea lemma, conditional projection-density moment, pointwise quadratic-phase decay, post-rotation independence, or reciprocal single-minor selection is used.

## 3. New theorem: spend the whole double-incident rank-two bank

Let `I,J` be disjoint sets of ORIGINAL coordinates and let `C=A[I,J]` have rank exactly two. After conditioning only coordinates outside `I union J`, write the surviving quadratic form as

`R(U,V)=F(U)+2 U^T C V+G(V)+c`,

where `U=X_I`, `V=X_J`, and `F,G` are arbitrary real quadratic-affine functions. The coordinate laws inside each bank remain independent products with one-dimensional density caps one.

Fix `j in I` and `r in J` and define the **double-incident exterior mass**

`Delta_jr(C) = sum_(k in I\{j}) sum_(s in J\{r}) det C[{j,k},{r,s}]^2`.

Assume `Delta_jr(C)>0`.

### Theorem 3.1 — `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`

The conditional law of `R`, uniformly in the outside conditioning, and therefore the unconditional law, has an `L^3` density satisfying

`boxed( ||p_R||_3 <= 3^(2/3) 2^(1/3) Delta_jr(C)^(-1/6). )`      (3.1)

All same-side quadratic terms, all affine terms, and all outside couplings are retained.

### Proof

Because `rank(C)=2`, all row vectors `c_i` of `C` lie in a two-dimensional Euclidean subspace `E` of the right physical coordinate space. Since `Delta_jr(C)>0`, `c_j!=0`. Choose an orthonormal basis `e_1,e_2` of `E` with `e_1 = c_j/||c_j||`. Write

`c_i = alpha_i e_1 + beta_i e_2`,

so `alpha_j=||c_j||` and `beta_j=0`. Put

`d_L = (sum_(i!=j) beta_i^2)^(1/2)`.

Define two ORIGINAL-coordinate grouped left variables

`xi_1 = U_j + sum_(i!=j) (alpha_i/||c_j||) U_i`,
`xi_2 = sum_(i!=j) beta_i U_i`.                                  (3.2)

Then

`U^T C V = ||c_j|| xi_1 z_1 + xi_2 z_2`,                         (3.3)

where `z_l=e_l^T V`.

The key product-law point is that the pair `(xi_1,xi_2)` has a dimension-free joint density cap. Conditional on all `U_i,i!=j`, the first coordinate `xi_1` is a translate of `U_j`, hence has conditional density at most one. Therefore

`p_(xi_1,xi_2)(x,y) <= p_(xi_2)(y)`                              (3.4)

for almost every `(x,y)`. By the one-dimensional Ball--Rogozin bound applied to the independent variables `U_i,i!=j`,

`||p_(xi_2)||_infinity <= sqrt(2)/d_L`.                           (3.5)

Thus

`||p_xi||_infinity <= sqrt(2)/d_L`.                              (3.6)

Now physicalize the right bank as well. Write (3.3) as

`sum_(s in J) xi^T q_s V_s`,

with

`q_s = ( ||c_j|| e_1(s), e_2(s) ) in R^2`.

The hypothesis `Delta_jr(C)>0` implies `q_r!=0`. Let `f_1=q_r/||q_r||` and let `f_2` be a perpendicular unit vector. Rotate `xi` by this orthogonal two-dimensional change of basis; its density cap (3.6) is unchanged. Write

`q_s = a_s f_1+b_s f_2`,

so `a_r=||q_r||`, `b_r=0`, and set

`d_R=(sum_(s!=r)b_s^2)^(1/2)`,
`eta_1=V_r+sum_(s!=r)(a_s/||q_r||)V_s`,
`eta_2=sum_(s!=r)b_s V_s`.                                      (3.7)

Exactly as on the left,

`||p_eta||_infinity <= sqrt(2)/d_R`.                            (3.8)

In the rotated grouped coordinates the entire cross term is exactly

`U^T C V = ||q_r|| zeta_1 eta_1 + zeta_2 eta_2`,                (3.9)

so the effective two-by-two coefficient matrix is `M=diag(||q_r||,1)`.

The determinant bank is exactly the Jacobian currency created by these two groupings. Indeed, for every `k!=j,s!=r`,

`det C[{j,k},{r,s}]
 = beta_k det(q_r,q_s)
 = beta_k ||q_r|| b_s`.                                        (3.10)

Consequently

`Delta_jr(C)=d_L^2 ||q_r||^2 d_R^2`,                            (3.11)

or equivalently

`|det M| d_L d_R = Delta_jr(C)^(1/2)`.                          (3.12)

Disintegrate the left and right product laws over the grouped pairs. The arbitrary self terms remain only in complex conditional amplitudes `alpha_t,beta_t` satisfying

`|alpha_t|<=p_zeta`, `|beta_t|<=p_eta`.

Hence

`||alpha_t||_2 ||beta_t||_2
 <= ( ||p_zeta||_infinity ||p_eta||_infinity )^(1/2)
 <= [2/(d_L d_R)]^(1/2)`.                                      (3.13)

The same two-dimensional Plancherel calculation as in account03/B06 therefore gives

`|phi_R(t)| <= min(1, A/|t|)`,

with

`A = pi [2/(d_L d_R)]^(1/2) |det M|^(-1/2)
  = pi sqrt(2) Delta_jr(C)^(-1/4)`.                             (3.14)

Thus

`int_R |phi_R(t)|^(3/2) dt <= 6A`.                              (3.15)

Using exactly the Fourier convention of the B06 source, inverse Hausdorff--Young yields

`||p_R||_3
 <= (2pi)^(-2/3) (6A)^(2/3)
 = 3^(2/3) 2^(1/3) Delta_jr(C)^(-1/6)`,                        (3.16)

which is (3.1). The estimate is uniform in the outside original-coordinate conditioning, so averaging proves the unconditional statement. QED.

### Why this is the requested aggregate-before-inversion step

No individual determinant is lower-bounded. The two one-dimensional product projections pay `d_L` and `d_R`, while the remaining two-dimensional oscillatory determinant pays `||q_r||`; identity (3.11) multiplies them into the **entire** double-incident squared-minor bank before any negative power is taken. Thus a star with `d` minors of size `1/d` is harmless as long as its total bank stays fixed.

## 4. Outer genuine square: a grouped `L^infinity` endpoint

Suppose the full scalar-Schur configuration also contains the genuine original-coordinate pivot from the B06/B18 chain, so after completing that coordinate the dependence-safe square-kernel inequality applies with coefficient `a!=0`. If the residual cross bank `C` is exact rank two, combine Theorem 3.1 with the B06 `L^3 -> L^infinity` square transducer:

`sup_t int_0^infinity p_R(t+-u) u^(-1/2) du
 <= (2^(4/3)+1) ||p_R||_3^(3/4)`.

This proves

`boxed(
 ||p_Q||_infinity
 <= C_grp |a|^(-1/2) Delta_jr(C)^(-1/8),
)`                                                               (4.1)

where

`C_grp=(2^(4/3)+1) sqrt(3) 2^(1/4) < 7.254`.                    (4.2)

This theorem keeps all arbitrary same-side self blocks and outside couplings allowed by the source scalar-square reduction.

## 5. Direct application of the named partner result

Now apply (4.1) to account03/B08 r20, rather than merely citing it.

In the partner's **exact-rank-two** branch, the normalized exterior matrix has no tail, so its factorized top mode is the entire exterior matrix. Therefore the partner's physical heavy row/column `j,r` satisfy

`Delta_jr(Z)>A0`,                                                (5.1)

where

`A0=158518644736/173076800625`.

For rank two, every two-by-two physical minor of `H` is the corresponding minor of `Z` multiplied by

`sqrt((g^2+h_1^2)(g^2+h_2^2))`.

Hence

`Delta_jr(H)
 = Delta_jr(Z)(g^2+h_1^2)(g^2+h_2^2)
 > A0 h_1^2 h_2^2`.                                             (5.2)

Because in rank two the partner's `e_2(x)>=2/3` is simply `x_1x_2>=2/3` and `h_i^2/gamma^2>=x_i`,

`h_1^2 h_2^2 >= (2/3) gamma^4`.                                (5.3)

Combining (5.1)-(5.3),

`Delta_jr(H)
 > [317037289472/519230401875] gamma^4
 =0.6105907672... gamma^4`.                                     (5.4)

The new grouped theorem gives the residual bound

`||p_R||_3 < 2.845329 gamma^(-2/3)`,                            (5.5)

and the genuine outer square gives the actual full-form inequality

`boxed(
 ||p_Q||_infinity
 < 7.711210 / sqrt(|a| gamma).
)`                                                               (5.6)

This improves the designated partner's source-pinned exact-rank-two endpoint `<10.575/sqrt(|a| gamma)` and, more importantly, proves the bank can be paid *as a bank*, not by a largest-minor argument.

## 6. The strictly higher-rank partner branch: bank payment is no longer the gap

Let `H_2` be the partner's top-two SVD truncation in the strictly higher-rank branch. The r20 source proves

`sum_(nu>=3) h_nu^2/gamma^2 < s_0:=329/3218176`.                (6.1)

Since `x_nu<=h_nu^2/gamma^2`, if `S=sum_(nu>=3)x_nu`, then `S<s_0`. Also `x_1+x_2<=2` and `e_2(x_tail)<=S^2/2`. From `e_2(x)>=2/3`,

`x_1x_2
 > 2/3-2s_0-s_0^2/2
 = 41413921384333/62139940601856
 =0.6664621978...`.                                             (6.2)

The partner's factorized top exterior slice still has squared norm `>A0`; therefore

`Delta_jr(H_2)
 > A0 h_1^2h_2^2
 > [1602753586681571324053/
     2625728054296087260000] gamma^4
 =0.6104034971... gamma^4`.                                     (6.3)

Applying Theorem 3.1 to the **auxiliary exact-rank-two form obtained by replacing `H` with `H_2` while retaining the same self quadratic-affine blocks** gives

`||p_(R_2)||_3 <2.845475 gamma^(-2/3)`,                         (6.4)

and, after the same genuine pivot-square transducer,

`||p_(Q_2)||_infinity
 <7.711506/sqrt(|a| gamma)`.                                    (6.5)

Equation (6.5) is deliberately **not** asserted for the original higher-rank form. The tail cross phase

`2 U^T(H-H_2)V`

still couples the two product fibers. With arbitrary cap-one marginals and no moments, its small coefficient norm cannot be discarded by a pointwise perturbation estimate. What (6.3)-(6.5) establish is that the formerly named “grouped factorized bank transducer” is completely paid for the dominant rank-two exterior mode. The remaining obstruction is only the restoration of the quantitatively tiny higher-rank cross tail.

Thus the first unpaid implication is sharpened to

**`QFORM-DIFFUSE-BICOLOOP-TAIL-STABILITY-v1`:** in the r20 source setting, with

`||H-H_2||_HS < sqrt(329/3218176) gamma <0.010112 gamma`,

transfer the grouped rank-two `L^3`/outer-square payment to the full physical cross phase without moments and without conditioning on spectral coordinates; or construct a genuine product-source counterexample to such a tail-stability statement. A valid proof may use a regularized determinant/ridge estimate on the tail, an operator-valued version of the two-dimensional Plancherel step, or a further original-coordinate grouping, but cannot replace the tail by an arbitrary bounded phase.

## 7. Failure modes explicitly avoided

- **No single-minor extraction.** The theorem is invariant under spreading the bank over arbitrarily many small minors.
- **No arbitrary spectral-coordinate surrogate.** Every grouping starts from original independent coordinates.
- **No post-rotation independence.** Orthogonal changes occur only after a two-dimensional grouped density has already been constructed; they preserve a joint density cap but do not create independence claims.
- **No moment assumption.** The only distributional inputs are one-dimensional density caps and product independence.
- **No false conditional-density moment.** Conditioning is only on outside original coordinates, where product independence genuinely survives.
- **No pointwise perturbative dismissal of the higher-rank tail.** This is stated as the remaining gap rather than hidden.

## 8. Status

**New proved theorem:** `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`.  
**Partner-applied corollary:** `QFORM-BICOLOOP-GROUPED-EXACT-RANK2-v2`, giving `<7.711210/sqrt(|a| gamma)`.  
**Strict higher-rank consequence:** the partner top-two factorized bank is already uniformly payable; only the small tail-phase stability remains.  
**Full QFORM target:** OPEN / not proved / not disproved.  
**Continuity:** not claimed by this `L^3` plus dependent-square endpoint.

The accompanying `check.py` reproduces the exact rational constants and the numerical endpoint constants used in Sections 5--6; `check_output.txt` is its executed output. The checker validates arithmetic only, not the analytic proof.

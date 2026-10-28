SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T11:14:07Z.
attacking: curvature-slope derivative localization—prove exact cap-preserving truncation with zero constant loss, then remove the exact-zero hub restriction by combining a random slope density cap with high/low derivative splitting and the completed account02/B14 physical-pair logarithmic compiler.

# QFORM B14 r35 — exact unbounded-support localization and nonzero-self random-slope hub

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Worker:** account01/B14  
**Run:** 20260923T111407Z-account01-B14-QFORM-r35  
**Status:** NEW SUPPORTING ZERO-LOSS LOCALIZATION THEOREM + NEW TARGET-LEVEL CURVATURE-SLOPE THEOREM; FULL QFORM OPEN.  
**Execution:** WITHOUT_VERIFIED_BRAIN. Continuity for the unrestricted target remains separate.

## 1. Fresh control and sources actually consumed


The completed designated-partner result actually used below is account02/B14 r33:

`yspennstate/math-open-problems@9c77bae76f0d884fc60a2ffee86ad6269b79d690`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T095834Z-account02-B14-QFORM-r33/REPORT.md`.

Its completed physical-pair logarithmic envelope says that if an outer pair consists of two original independent cap-one coordinates and has invertible indefinite block `B`, with

`D=|det B|`, `kappa=sigma_min(B)`,

and if the remainder is represented by a positive submeasure `nu` of total mass `m`, then for every `r>0`, uniformly in all affine translations,

`p_Q^sub(t) <= 2sqrt(2)m/r
              +D^(-1/2) integral log_+(2r^2/[kappa |t-y|]) dnu(y).`       (1.1)

The same partner report also proves the mass-homogeneous random-slope theorem for an exact zero-self hub. This run changes mechanism: instead of requiring the hub self coefficient to vanish, I control the derivative of the full one-variable quadratic polynomial.

I also use the completed product-projection estimate already source-pinned in the preceding B14 run: for independent cap-one original coordinates `V=(V_1,...,V_d)` and deterministic `c !=0`,

`||p_(c^T V)||_infinity <= sqrt(2)/||c||_2`.                              (1.2)

No law-uniform pointwise quadratic Fourier decay, post-rotation independence, arbitrary-joint coarea estimate, bounded support diameter, fixed fragment count, conditional-fiber density moment, or small-coefficient perturbation is used.

## 2. Exact cap-preserving localization to compact support

This is a direct localization lemma for the **full target constant**, independent of every matrix-specific branch below.

For a product probability law `mu=otimes_{i=1}^n f_i(x_i)dx_i`, with `0<=f_i<=1`, and a symmetric target matrix `A`, define

`SB(mu,A) = sup_{a<b} mu{a <= x^T A x <= b}/(b-a)`.                        (2.1)

Let `C_all` be the supremum of (2.1) over every dimension, every legal cap-one product law, and every symmetric `A` having at least three eigenvalues of modulus at least one. Let `C_comp` be the same supremum with the additional condition that every marginal density has compact support.

### Theorem 2.1 — `QFORM-CAP-PRESERVING-TRUNCATION-v1`

`boxed: C_all = C_comp`                                                        (2.2)

with equality also in the value `+infinity`.

Thus a universal compact-support theorem with constant `C` automatically proves the original arbitrary-unbounded-support theorem with **the identical constant**. No moment, centering, support-radius, translation, fragment-count, or fragment-separation factor is introduced.

### Proof

The inequality `C_comp<=C_all` is immediate. For the reverse direction fix one legal product law, target matrix `A`, and interval `I=[a,b]`.

For `R>0` put

`f_(i,R)(x)=f_i(x) 1_{[-R,R]}(x)`,
`m_i(R)=integral f_(i,R)`.                                               (2.3)

Do **not** normalize this truncation. Choose an interval `J_(i,R)` disjoint from `[-R,R]` and of length `1-m_i(R)`, and set

`tilde f_(i,R)=f_(i,R)+1_{J_(i,R)}`.                                   (2.4)

Then `0<=tilde f_(i,R)<=1`, its integral is exactly one, and it has compact support. Let `nu_R` be the positive product submeasure with density `prod_i f_(i,R)` and let `tilde mu_R` be the compactly supported cap-one product probability with density `prod_i tilde f_(i,R)`. Pointwise domination of the factor densities gives

`nu_R(E) <= tilde mu_R(E)` for every measurable `E`.                    (2.5)

Therefore

`nu_R{x^T A x in I} <= C_comp |I|`.                                    (2.6)

As `R` increases, the measures `nu_R` increase setwise to `mu`: their densities are

`prod_i f_i(x_i) 1_{max_i |x_i|<=R}`.                                  (2.7)

Monotone convergence in (2.6) yields

`mu{x^T A x in I} <= C_comp |I|`.                                      (2.8)

Taking the supremum proves (2.2). The same argument applies verbatim to quadratic-plus-affine outputs because no property of the event beyond measurability was used. QED.

### Density consequence

If `C_comp<infinity`, (2.8) for all intervals says the output probability measure is dominated by `C_comp` times Lebesgue measure; equivalently it has a density with essential supremum at most `C_comp`. Hence (2.2) really preserves the target density constant, not merely a weak approximation statement.

### Relation to the live localization corrections

The theorem does **not** assert a universal support radius. The completing intervals `J_(i,R)` and the truncation radius may depend on the law and `R` tends to infinity. It therefore respects the source-valid correction that bounded-diameter localization is false. It likewise imposes no finite bound on the number or separation of support fragments.

## 3. A quadratic random-slope lemma: nonzero hub self-curvature is safe

The previous B14 theorem required an exact zero-self hub. The next lemma removes that restriction without treating `a X^2` as a small perturbation.

Let `X` be an original scalar probability variable with density at most one. Let `mu` be any finite positive measure on a bank space, of mass `m in (0,1]`. Let measurable `S,R` on the bank generate the output submeasure

`Y = a X^2 + S(V) X + R(V)`,                                           (3.1)

where `a` is an arbitrary real number and `X` is independent of the bank variable. No independence between `S(V)` and `R(V)` is assumed. Suppose the slope pushforward `S_#mu` has a density `g` satisfying

`||g||_infinity <= L`, `integral g=m`.                                 (3.2)

For `a!=0`, define

`H_a(L,m)=min{L/m, 1/(2|a|)}`;                                        (3.3)

for `a=0`, take the second entry as `+infinity`, so `H_0=L/m`.

### Lemma 3.1 — `QFORM-CURVATURE-SLOPE-HALF-HOLDER-v1`

For every `t in R` and `rho>0`,

`boxed:
 nu_Y{|Y-t|<=rho}
 <= m min{1, 4 sqrt(2 H_a(L,m) rho)}.
`                                                                        (3.4)

This is uniform in every translation and in the arbitrary correlated remainder `R(V)`.

### Proof

Let

`W=2aX+S(V)`                                                            (3.5)

be the derivative of the scalar quadratic polynomial with respect to `X`. When `a!=0`, the law of `2aX` is a probability density capped by `1/(2|a|)`. Since `S_#mu` has mass `m` and density cap `L`, convolution gives the derivative submeasure a density cap

`G <= min{L, m/(2|a|)} = m H_a(L,m).`                                  (3.6)

For `a=0`, simply `W=S(V)` and `G<=L=mH_0`.

Fix `tau>0`. For a fixed bank point `v`, write

`q_v(x)=a x^2+S(v)x+R(v)-t`.                                           (3.7)

On the set `|q_v'(x)|>tau`, the real line has at most two monotonicity components. On each component the inverse derivative has magnitude at most `1/tau`; hence the preimage of `[-rho,rho]` has length at most `2rho/tau`. Because the density of `X` is at most one,

`P_X{|q_v(X)|<=rho, |q_v'(X)|>tau} <= 4rho/tau`.                       (3.8)

Integrating the bank submeasure contributes at most `4m rho/tau`.

The complementary event is contained in `|W|<=tau`, whose joint submeasure mass is at most `2G tau` by (3.6). Consequently

`nu_Y{|Y-t|<=rho} <= 4m rho/tau+2G tau`.                              (3.9)

Optimizing at `tau=sqrt(2m rho/G)` when `G>0` gives

`4sqrt(2mG rho) <= 4m sqrt(2H_a rho)`.                                (3.10)

Together with the trivial mass bound `m`, this is (3.4). Degenerate `G=0` follows by a limit (and in fact is easier). QED.

The important feature is the interpolation

`H_a <= min{slope-cap-per-unit-mass, curvature scale 1/(2|a|)}`.        (3.11)

Thus a tiny nonzero `a` need not be discarded; as `a->0` the estimate continuously falls back to the random-slope certificate, while for large `|a|` the scalar curvature itself improves the derivative density.

## 4. Logarithmic potential and the completed partner physical-pair theorem

A general elementary layer-cake consequence will be useful. If a positive measure `nu` of mass `m` obeys

`nu{|Y-t|<rho} <= m min{1,K sqrt(rho)}`                               (4.1)

for every center, then for every `A>0`,

`boxed:
 integral log_+(A/|t-y|) dnu(y)
 <= 2m Psi(K sqrt(A)),
`                                                                        (4.2)

where

`Psi(q)=q`, `0<=q<=1`,
`Psi(q)=1+log q`, `q>=1`.                                             (4.3)

Indeed, layer cake gives the integral of `min{1,K sqrt(A)e^{-s/2}}` over `s>=0`; this is `2q` for `q<=1` and `2(1+log q)` for `q>=1`.

Apply (4.2) to Lemma 3.1. Put simply

`H=H_a(L,m)`.                                                         (4.4)

Then `K=4sqrt(2H)`. In the completed partner estimate (1.1), take

`A=2r^2/kappa`.

The argument of `Psi` is therefore

`z=8r sqrt(H/kappa)`.                                                 (4.5)

Substitution into the **completed account02/B14 r33 inequality** (1.1) gives the actual compiler

`boxed:
 ||p_Q^sub||_infinity
 <= m inf_{z>0}
    {16 sqrt(2H/kappa)/z + 2 D^(-1/2) Psi(z)}.
`                                                                        (4.6)

Define

`z_0=8 sqrt(2 D H/kappa).`                                            (4.7)

The optimization is explicit:

`boxed:
 ||p_Q^sub||_infinity <=
  { 8*2^(3/4) m (H/(kappa D))^(1/4),                   z_0<=1,
    2m D^(-1/2) [2+log z_0],                           z_0>=1. }
`                                                                        (4.8)

For `z_0<=1`, minimize `A/z+bz` at `z=sqrt(z_0)`; for `z_0>=1`, minimize `A/z+b(1+log z)` at `z=z_0`. The two formulas agree at `z_0=1`.

Equation (4.8) is the requested actual application of a completed partner result, not a restatement of it.

## 5. Target-level theorem: arbitrary hub self coefficient and arbitrary dense bank curvature

Split the independent original coordinates as

`X=(U_1,U_2,X_0,V,Z)`,                                               (5.1)

where `V in R^d` and `Z` is an arbitrary outside block. Suppose the active original-coordinate principal block is

`A_I = B direct_sum [[a,c^T],[c,Hmat]]`,                             (5.2)

where

- `B=B^T` is an invertible indefinite `2x2` matrix;
- `a in R` is **arbitrary**;
- `c in R^d` is nonzero;
- `Hmat=Hmat^T` is an arbitrary symmetric matrix.

All couplings from the displayed active coordinates to `Z`, and the `Z-Z` block, may be arbitrary.

Condition only on the outside original coordinates `Z=z`. The active conditional form is

`Q_z = U^TBU + affine_U
     + a X_0^2
     + X_0 [s_0(z)+2c^T V]
     + V^T Hmat V + affine_V + C(z).`                               (5.3)

The dense term `V^T Hmat V+affine_V+C` may be arbitrarily correlated with the slope. By (1.2),

`||p_(s_0+2c^T V)||_infinity <= 1/(sqrt(2)||c||_2).`                (5.4)

Set

`H_* = min{ 1/(sqrt(2)||c||_2), 1/(2|a|) }`,                        (5.5)

with the second term interpreted as `+infinity` when `a=0`.

### Theorem 5.1 — `QFORM-NONZERO-HUB-ARBITRARY-BANK-CURVATURE-v1`

With `D=|det B|`, `kappa=sigma_min(B)`, and

`z_*=8 sqrt(2D H_*/kappa)`,                                        (5.6)

every legal cap-one product law satisfies the bound (4.8) with `m=1` and `H=H_*`. Explicitly,

`boxed:
 ||p_Q||_infinity <=
  { 8*2^(3/4) (H_*/(kappa D))^(1/4),                z_*<=1,
    2D^(-1/2)[2+log z_*],                            z_*>=1. }
`                                                                        (5.7)

The estimate is independent of dimension, `Hmat`, all outside couplings, all conditioning-generated translations, support diameter/location, distant fragments, tails, and every moment.

This strictly removes the exact-zero-self assumption of the preceding B14 structural theorem. No perturbative deletion of `aX_0^2` is performed.

### Exact-target universal subfamily

Take the outer physical pair

`B=[[0,1],[1,0]]`,                                                   (5.8)

so `D=kappa=1`, and suppose `||c||_2>=1`. Then `H_*<=1/sqrt(2)`, hence (5.7) gives the uniform numerical bound

`boxed:
 ||p_Q||_infinity <= 4+2 log(8*2^(1/4))
                  = 8.505456673639644... .
`                                                                        (5.9)

This is a genuine family inside the owner's exact three-large-eigenvalue target for **every** `a` and **every** symmetric `Hmat`. The block `B` contributes eigenvalues `+1,-1`. For

`S=[[a,c^T],[c,Hmat]]`,

`||S||_op >= ||S e_0||_2 = sqrt(a^2+||c||_2^2) >=1`,                 (5.10)

so `S` has an eigenvalue of modulus at least one. Thus the active principal block has at least three threshold eigenvalues. Cauchy interlacing preserves the corresponding positive/negative threshold counts after arbitrary outside coordinates and couplings are restored.

For the especially transparent four-coordinate family

`Q=2U_1U_2+aX_0^2+2X_0V+hV^2`,                                    (5.11)

plus arbitrary outside couplings handled by conditioning, the scalar `V` slope has cap at most `1/2` after multiplication by two. Therefore `H_*<=1/2` and

`boxed:
 ||p_Q||_infinity <= 4+2log8
                  = 8.158883083359672...,
`                                                                        (5.12)

uniformly in the two arbitrary self coefficients `a,h` and in all input laws.

## 6. Fragment-mass localization with nonzero self-curvature

The derivative proof is mass-homogeneous. Suppose an active bank decomposition has positive components `mu_j` of masses `m_j`, and on each component the slope pushforward density cap obeys

`L_j <= m_j H_0`.                                                     (6.1)

Then (3.6) gives the derivative cap

`G_j <= m_j min{H_0,1/(2|a|)} = m_j H_a`.                           (6.2)

Every component therefore satisfies (4.8) with a multiplicative factor exactly `m_j`. Summing the positive output submeasures gives the **same whole-law constant** because `sum_j m_j=1`.

This directly extends account02/B14 r33's one-sided conjugate-shear localization. In the partner's notation, if a fragmented coordinate of mass `m_j` is sheared against one whole cap-one smoothing coordinate and the resulting slope cap is

`L_j <= m_j/(2|db|)`,                                                (6.3)

then the present nonzero-self theorem applies with

`H_a=min{1/(2|db|),1/(2|a|)}`                                       (6.4)

and the exact same component summation. Arbitrarily remote fragments therefore cost zero even when the hub has nonzero quadratic self-curvature.

Together with Theorem 2.1, this separates two localization issues cleanly:

1. **global unbounded support:** remove it by cap-preserving truncation/completion with exactly zero constant loss;
2. **active fragment decomposition inside a singular smoothing proof:** retain mass-proportional slope density before reciprocal/logarithmic payment, yielding exact mass homogeneity.

Neither operation normalizes a tiny remote fragment.

## 7. What remains open

The localization/support obstruction is now smaller. Exact zero hub self-curvature is no longer required, and arbitrary dense same-bank curvature is harmless whenever a useful random-slope certificate is exposed behind an invertible indefinite physical pair.

The first unpaid implication is structural:

> From only `s_3(A)>=1`, before active fragment normalization, force either (i) an invertible indefinite original-coordinate physical pair whose Schur remainder contains a hub with a quantitatively useful bank slope density certificate (its hub diagonal may now be arbitrary), or (ii) one of the already completed ridge/cross-volume/mixed-hub/grouped-bank exits.

There is still no proof that the bare spectral hypothesis supplies a uniformly good physical pair or such a slope vector. The live correction inbox contains exact families defeating simpler principal-minor/cross-rank dichotomies. Therefore this run does **not** prove the unrestricted conjecture.

## 8. Integrity/status

- New exact full-target localization lemma: `QFORM-CAP-PRESERVING-TRUNCATION-v1`, equation (2.2).
- New analytic lemma: `QFORM-CURVATURE-SLOPE-HALF-HOLDER-v1`, equation (3.4).
- Completed partner account02/B14 r33 applied to an actual inequality at (4.6)-(4.8).
- New target-level theorem: `QFORM-NONZERO-HUB-ARBITRARY-BANK-CURVATURE-v1`, equations (5.7)-(5.12).
- New mass-restoration extension to nonzero self-curvature: equations (6.1)-(6.4).
- Full QFORM remains OPEN; no continuous-density claim is made beyond what an applicable bounded-density theorem supplies.
- The new theorems are supplied for independent checking; they are not labeled as independently reviewed.
- Uniform pointwise quadratic Fourier decay is not used.
- No bounded support diameter, fixed fragment count, post-rotation independence, moments, or conditional-density supremum is assumed.
- Changed-file allowlist for the canonical repository consists only of this mathematical report under the assigned private QFORM root. Manual privacy review: no credentials, financial/client material, private personal archive, public-release action, account secrets, or machine-local paths are included.

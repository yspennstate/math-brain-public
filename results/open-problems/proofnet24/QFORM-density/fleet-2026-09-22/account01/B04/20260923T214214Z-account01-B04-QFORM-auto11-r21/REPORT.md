SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T21:42:14Z.
attacking: average the exact indefinite-pair logarithmic envelope against a genuinely bounded clean-bank Schur-remainder density and optimize the scale exactly; apply account02/B04 clean-bank rearrangement to the remainder of a dense indefinite test matrix.

# account01/B04 — bounded-remainder averaging of the indefinite pair-log envelope

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement.
Status: `SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_DENSE_INDEFINITE_BOUND / FULL_TARGET_OPEN`.
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not** proved here. The theorem below establishes essential boundedness in a new product-preserving branch. It does **not** establish continuity in this branch. No Gaussian, moment, compact-support, connected-support, log-concavity, centering, or post-rotation independence assumption is introduced.

## 1. Sources and correction state actually used

Fresh owner control remained QFORM-only, revision `2026-09-22.15`. The live correction ledger was read before the derivation. In particular, this report does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, conditional projection-density positive moments, small-operator-tail-as-small-random-error, or independence after rotating physical coordinates.

Two completed inputs are used at equations:

1. **Indefinite physical-pair logarithmic envelope**, source
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   For an invertible indefinite original-coordinate pair block `B`, writing
   `D=|det B|`, `kappa=sigma_min(B)`, completing that pair, and denoting its scalar Schur remainder by `R`, one has for every `r>0`

   `p_Q(t) <= 2 sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa |t-R|)).`      (1.1)

2. **Designated partner account02/B04 clean-bank top-two rearrangement**, source
   `yspennstate/math-open-problems@dfe442ee899867f5677e5ced85a196eca922fe64`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260923T211520Z-account02-B04-qform/REPORT.md`.
   For disjoint original product banks `X,Y` and

   `R=F(X)+2 X^T M Y+b^T Y+c`,                                      (1.2)

   with arbitrary `F(X)` and **no** `Y-Y` curvature, if the two top singular values of `M` are `s1>=s2>0`, then

   `||p_R||_infinity <= 2 sqrt(pi) (s1 s2)^(-1/2).`                  (1.3)

   The proof conditions on the original `X` variables and then uses a deterministic two-dimensional coefficient-space projection plus decreasing rearrangement. It does not assert independence of rotated random coordinates.

The first theorem below compiles any genuine bounded-density estimate for `R` into (1.1). The second calculation specializes the partner rearrangement to an exact two-dimensional physical bank, where its projection-density cap is one rather than the universal cap two.

## 2. Main theorem: exact bounded-remainder averaging of the pair-log singularity

### Theorem 2.1 — `QFORM-PAIRLOG-BOUNDED-REMAINDER-OPT-v1`

Let two original independent cap-one coordinates form an invertible indefinite symmetric pair block `B`. Put

`D=|det B|>0`, `kappa=sigma_min(B)>0`.

Condition on every remaining original coordinate and complete the pair exactly, so that

`Q=(H+B^(-1)LZ)^T B (H+B^(-1)LZ)+R(Z)`                      (2.1)

for some independent pair `H` and remaining original product vector `Z`; arbitrary pair-to-remainder linear coupling is allowed through `L`. Suppose the scalar remainder `R` has a density with

`||p_R||_infinity <= K < infinity.`                                (2.2)

Then `Q` has an essentially bounded density. If

`eta := 8 K D/kappa`,                                                (2.3)

then

`boxed:
||p_Q||_infinity <=
  6 D^(-1/6)(K/kappa)^(1/3),                 if eta<=1,
  D^(-1/2)[3+log eta],                        if eta>=1.`              (2.4)

The two expressions agree at `eta=1`.

### Proof

The pair-log theorem (1.1) applies conditionally on `Z`, because the two physical pair variables remain independent cap-one variables after deterministic translations depending on `Z`. Essential boundedness of `R` implies the uniform interval small-ball estimate

`P(|R-t|<rho) <= min(1,2K rho)`                                    (2.5)

for every `t` and `rho>0`.

Set

`a=2r^2/kappa`, `x=2Ka=4Kr^2/kappa`.                               (2.6)

Layer cake, with no regularity assumption beyond (2.5), gives

`E log_+(a/|t-R|)
 = int_0^infinity P(|t-R|<a e^(-v)) dv
 <= int_0^infinity min(1,x e^(-v)) dv
 = F(x),`                                                           (2.7)

where

`F(x)=x` for `0<x<=1`, and `F(x)=1+log x` for `x>=1`.              (2.8)

Since `r=(1/2)sqrt(kappa x/K)`, (1.1) becomes

`p_Q(t) <= A x^(-1/2)+B0 F(x),`                                    (2.9)

with

`A=4 sqrt(2K/kappa)`, `B0=D^(-1/2)`.                               (2.10)

On `0<x<=1`, differentiation gives the minimizer

`x=(A/(2B0))^(2/3)`                                                  (2.11)

provided `A<=2B0`, equivalently `eta<=1`. Substitution gives

`(3/2) A^(2/3)(2B0)^(1/3)
 =6 D^(-1/6)(K/kappa)^(1/3).`                                      (2.12)

On `x>=1`, differentiation gives

`sqrt(x)=A/(2B0)`, hence `x=eta`,                                  (2.13)

provided `A>=2B0`, equivalently `eta>=1`. At this point

`A x^(-1/2)=2B0`,                                                    (2.14)

and therefore

`p_Q(t)<=B0[2+1+log eta]
 =D^(-1/2)[3+log eta].`                                             (2.15)

This proves (2.4). At `eta=1`, both branches equal `3D^(-1/2)`.

The homogeneity is correct: under scaling of the full matrix by `c!=0`, `D` scales by `c^2`, `kappa` by `|c|`, and a density bound `K` for the scaled Schur remainder by `|c|^(-1)`, so either branch scales by `|c|^(-1)`. QED.

### What this theorem changes

The preceding first-compound route paid the Schur remainder only through a square-root small-ball estimate and consequently produced a fractional power `Z_1^(-1/8)`. Theorem 2.1 says that whenever another product-space mechanism already proves a genuine density cap `K` for the scalar Schur remainder, the logarithmic pair singularity can be averaged at the stronger density scale, with exact optimization and no additional residual-rank factor.

The result is deliberately not stated as a global theorem: the bare spectral hypothesis does not automatically supply a uniformly conditioned indefinite physical pair together with a bounded clean-bank Schur remainder.

## 3. Projection-cap refinement of the partner clean-bank theorem

The partner proof admits the following exact parameter refinement, which is useful for the explicit matrix below.

Let `u1,u2` be the top two left singular vectors of `M` in (1.2), and suppose the deterministic projection

`Z=(<X,u1>,<X,u2>)`                                                  (3.1)

has a joint density cap `L`. No independence of the two coordinates of `Z` is assumed. Conditioning on the original X-bank, the Ball/Rogozin linear-form bound used by the partner gives

`||p_(R|X=x)||_infinity
 <=1/[sqrt(2)||M^T x+b/2||_2].`                                     (3.2)

Projection of the coefficient norm onto the top two right singular directions gives

`||M^T x+b/2||_2
 >= sqrt(s1^2(z1-zeta1)^2+s2^2(z2-zeta2)^2)`                       (3.3)

for a deterministic shift `zeta`. Under

`w=(s1(z1-zeta1),s2(z2-zeta2))`,                                   (3.4)

the density of `w` has cap `L/(s1s2)` and total mass one. Planar decreasing rearrangement against `|w|^(-1)` yields

`int |w|^(-1) p_W(w)dw <=2 sqrt(pi L/(s1s2)).`                       (3.5)

Averaging (3.2) therefore gives

`boxed:
||p_R||_infinity <= sqrt(2 pi L) (s1s2)^(-1/2).`                    (3.6)

The partner theorem is the special case `L<=2`. If the X-bank consists of exactly two original physical coordinates and `u1,u2` are an orthonormal basis of that plane, the orthogonal change of variables preserves the two-dimensional Lebesgue density and the original joint product density is at most one; hence one may take

`L=1.`                                                              (3.7)

This refinement changes only the final rearrangement constant, not the partner theorem's product-provenance argument.

## 4. A fully dense genuinely rotated indefinite target

Use seven original independent coordinates grouped as

`H in R^2`, `X in R^2`, `Y in R^3`.

Define the physical indefinite pair

`B=[[1,3],[3,1]].`                                                   (4.1)

Its eigenvalues are `4,-2`, so

`D=8`, `kappa=2`.                                                    (4.2)

Let

`u=(1,1,1)/sqrt(3)`,
`v=(1,2,-3)/sqrt(14)`,                                               (4.3)

which are orthonormal, and set

`M=2 [u^T; v^T].`                                                    (4.4)

Thus `s1(M)=s2(M)=2`, and every one of its six physical entries is nonzero. Put

`F=(1/10)[[1,1],[1,-1]]`,
`S=[[F,M],[M^T,0_3]].`                                               (4.5)

Finally take the dense physical pair-to-remainder crossing

`L=(1/100)[[1,2,3,4,5],[2,3,5,7,11]]`                              (4.6)

and define the full symmetric matrix

`A_*=[[B,L],[L^T,S+L^T B^(-1)L]].`                                  (4.7)

Every physical entry of `A_*` is nonzero; the smallest absolute entry is `7/10000`. More importantly, (4.7) has the exact square-completion identity

`(h,z)^T A_* (h,z)
 =(h+B^(-1)Lz)^T B(h+B^(-1)Lz)+z^T S z.`                            (4.8)

Hence the scalar Schur remainder is exactly the clean-bank form

`R=z^T S z = X^T F X+2X^T M Y`,                                    (4.9)

with no `Y-Y` curvature.

### 4.1 Target-validity without numerical eigenvalue reliance

Let

`S0=[[0_2,M],[M^T,0_3]].`                                           (4.10)

Since the two nonzero singular values of `M` equal two,

`spec(S0)={2,2,0,-2,-2}.`                                           (4.11)

Also

`||S-S0||_op=||F||_op=sqrt(2)/10.`                                  (4.12)

Therefore `S` has at least two positive and two negative eigenvalues whose absolute values are at least

`2-sqrt(2)/10.`                                                      (4.13)

The block diagonal matrix `diag(B,S)` consequently has at least three positive and three negative eigenvalues of modulus at least `2-sqrt(2)/10`.

Moreover

`A_*-diag(B,S)
 =[[0,L],[L^T,L^T B^(-1)L]],`                                       (4.14)

so

`||A_*-diag(B,S)||_op
 <=||L||_op+||L||_op^2 ||B^(-1)||_op
 <=sqrt(263)/100+263/20000.`                                        (4.15)

Weyl's inequality therefore leaves at least three positive and three negative eigenvalues of `A_*` of modulus at least

`2-sqrt(2)/10-sqrt(263)/100-263/20000
 =1.68325589636042... >1.`                                          (4.16)

Thus this is a fully target-valid, genuinely non-diagonal, indefinite physical form. No rotation of the random variables has been used.

A finite check gives the actual eigenvalues approximately

`-2.080964936, -1.996004703, -1.925616180, 0,
  1.929935787, 2.068706534, 4.008605998`,                            (4.17)

but (4.16), not this numerical list, is the proof of target-validity.

## 5. Actual application of account02/B04 and the new pair-log compiler

The remainder (4.9) lies exactly in the partner theorem's scope. Applying account02/B04 Theorem 2.1 as stated gives

`K_partner=2 sqrt(pi)(2*2)^(-1/2)=sqrt(pi).`                         (5.1)

Substituting this completed partner result into Theorem 2.1 above gives

`eta_partner=8 K_partner D/kappa
 =32 sqrt(pi)>1`,                                                     (5.2)

and hence the actual all-product-law inequality

`||p_(X^T A_* X)||_infinity
 <=(1/sqrt(8))[3+log(32 sqrt(pi))]
 =2.488344417343258... .`                                           (5.3)

This is the required positive equation-level application of the designated partner's completed result.

For this particular remainder, the top-left singular frame of `M` is the entire two-dimensional original X-bank. Thus (3.7) applies with `L=1`, and (3.6) improves (5.1) to

`K_exact=sqrt(2pi)/2=sqrt(pi/2)
 =1.253314137315500... .`                                           (5.4)

Then

`eta_exact=8 K_exact D/kappa
 =32 sqrt(pi/2)
 =40.1060523940960...>1`,                                           (5.5)

so the sharpened explicit estimate is

`boxed:
||p_(X^T A_* X)||_infinity
 <=(1/sqrt(8))[3+log(32 sqrt(pi/2))]
 =2.365812149409690... .}`                                          (5.6)

This holds for **every** choice of independent real input coordinates whose scalar probability densities are bounded by one. No moments or support restrictions occur anywhere in the derivation.

The conclusion in (5.6) is essential boundedness. This argument does **not** prove that the density is continuous; that remains a separate regularity question for this branch.

## 6. Relation to the previous first-compound receiver

The preceding account01/B04 first-compound pair receiver controlled an indefinite pair using only a square-root small-ball bound for a rank-free crossing remainder. The present theorem is complementary: once a true density cap for the remainder is available, it integrates the pair's logarithmic singularity exactly rather than downgrading that cap to a `sqrt(rho)` profile.

On the current test matrix the Schur crossing has `||M||_F^2=8`. The earlier first-compound formula would give a substantially larger constant; the new density-to-logarithm splice therefore pays a genuinely different analytic regime. No claim is made that either certificate is globally optimal.

## 7. Remaining implication

The new result pays a concrete overlap-two / indefinite-pair branch whenever pair completion exposes a clean-bank Schur remainder with two target-scale crossing singular directions. What is **not** proved is the structural implication from the bare three-large-eigenvalue hypothesis to such a pair and remainder.

The next B04 debt is:

`QFORM-PAIRLOG-DENSITY-REMAINDER-OR-ROUGH-CURVATURE-ROUTING-v1`:

> Aggregate the overlap-two mass before selecting a physical pair. Either produce an invertible indefinite pair with controlled `D,kappa` whose Schur remainder has a target-scale clean-bank top-two receiver, or show that failure forces the remainder's same-bank curvature into an already completed projected-crossing / compound-volume / ridge / definite-pair / grouped-hub endpoint. Do this without treating small operator norm as small random quadratic error and without paying a vanishing local minor.

This is a supporting theorem, not a full solution. A full candidate still must cover all signs and degenerate configurations and receive two independent end-to-end reviews.

## 8. Claim ledger for this run

- `QFORM-PAIRLOG-BOUNDED-REMAINDER-OPT-v1`: PROVED in the stated conditional scope.
- `QFORM-CLEANBANK-PROJECTIONCAP-REFINEMENT-v1`: PROVED as a parameter-exact refinement of the partner proof.
- Dense target matrix (4.7): target-valid by the analytic Weyl estimate (4.16); exact all-product-law density cap (5.6).
- Full QFORM theorem: OPEN.
- Full-target continuity: OPEN.
- Continuity in this supporting branch: NOT PROVED.

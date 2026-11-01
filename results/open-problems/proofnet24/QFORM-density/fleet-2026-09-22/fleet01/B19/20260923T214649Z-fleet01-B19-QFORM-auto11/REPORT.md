SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B19, 2026-09-23T21:46:49Z.
attacking: the exact no-coloop finite-core common-plane endpoint; use the partner identity `D=Delta+M^T K M` and the physical two-hub logarithmic transducer to spend every nontrivial common-plane Schur mismatch uniformly through its rank-one degeneration, without deleting a nonzero tail.

# fleet01/B19 — uniform common-plane mismatch receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T214649Z-fleet01-B19-QFORM-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **not claimed for the new pair-log receiver; full-target continuity remains open.**

## 1. Source boundary and exact local state

The live target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moments, bounded support, connected support, identical laws, Gaussianity, log-concavity, or independence after a spectral rotation are assumed.

This report consumes the following source-pinned completed mathematical inputs.

1. **Designated partner fleet02/B19 r36**, at
   `yspennstate/math-open-problems@a12ea856984640d876168e74f6e0a2a3f4780029`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/B19-20260923T190836Z-r36/REPORT.md` and `COLOOP_ADDENDUM.md`.
   In its exact no-coloop zero-height endpoint, after product-safe conditioning, the remaining quadratic polynomial is

   `q(x,y)=x^T B x+2x^T M y+y^T(Delta+M^T K M)y+a^T x+b^T y+c`,      (1.1)

   where `x=(x_1,x_2)` are two literal original coordinates, `y` is an independent original-coordinate product bank, `M` is `2 x m` of rank two, `Delta` is physical diagonal, and `K=K^T` is `2 x 2`. Writing

   `G=MM^T`, `S=sqrt(det G)`, `ell_i=m_i^T G^{-1}m_i`,               (1.2)

   the partner has `S>S0=1/(480 sqrt(7626))` in the live finite-core collar. Its exact classification also identifies the one- and two-coloop alternatives as finite physical star packets rather than diffuse new curvature.

2. **Fresnel--Brascamp--Lieb theorem and fractional potentials**, at
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.
   If `R=diagonal + sum_{j=1}^r lambda_j u_j u_j^T` with orthonormal `u_j` and coordinate leverage at most `1/2`, then

   `|phi_R(t)| <= (4pi)^(r/2) |t|^(-r/2) prod_j |lambda_j|^(-1/2)`. (1.3)

   For `r=2`, its proved fractional-potential lemma gives

   `H_{1/2}(R):=sup_s E|R-s|^(-1/2)
       <=8 sqrt(2) |lambda_1 lambda_2|^(-1/4)`.                    (1.4)

3. **Physical indefinite-pair logarithmic transducer**, at
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   For an invertible indefinite physical pair `B`, put

   `D_B=|det B|`, `kappa=sigma_min(B)`.                             (1.5)

   If the completed remainder obeys

   `sup_s P(|R-s|<rho)<=H sqrt(rho)`,                              (1.6)

   then

   `||p_q||_infinity <=4 sqrt(2H) (D_B kappa)^(-1/4)`.             (1.7)

   The pair translations may depend arbitrarily on the remainder.

4. **Arbitrary-rank quarter-power small ball**, at
   `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.
   For every nonzero real symmetric matrix `R0`, arbitrary affine terms, and independent cap-one inputs,

   `sup_s P(|Y^T R0 Y+linear-s|<rho)
      <=min(1,5 (rho/||R0||op)^(1/4))`.                            (1.8)

   The same source proves the physical-pair theorem for arbitrary extra spectrum. I use (1.8) below at an actual matrix norm, rather than merely citing it.

The live corrections are preserved: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint coarea bound, no positive conditional projection-density moment, no post-rotation independence, no one-good-minor shortcut, and no replacement of a small nonzero coefficient by zero.

## 2. Main new theorem

### Theorem 2.1 — `QFORM-TWOHUB-COMMONPLANE-UNIFORM-MISMATCH-v1`

Assume (1.1)-(1.2), and in addition

`max_i ell_i <= 1/2`.                                             (2.1)

All input coordinates remain arbitrary independent cap-one laws. All diagonal entries of `Delta`, all affine terms, and all signs are arbitrary.

If `B` is definite, then

`||p_q||_infinity <= pi/sqrt(|det B|)`.                            (2.2)

Now assume `B` is invertible indefinite. Define the **normalized Schur-mismatch matrix**

`L=K-B^{-1}`,
`T=G^(1/2) L G^(1/2)`,                                           (2.3)

and order its real eigenvalues so that

`mu=|theta_1| >= |theta_2|`.                                      (2.4)

Then every state with `mu>0` is paid by one of the following two bounds, with no blow-up as `theta_2 ->0`.

**Balanced mismatch:** if `|theta_2|>=mu/8`, then

`boxed:
 ||p_q||_infinity
 <=16*2^(5/8) (D_B kappa mu)^(-1/4)
 <24.676 (D_B kappa mu)^(-1/4).`                                 (2.5)

**Rank-one collar, including the exact rank-one degeneration:** if `|theta_2|<mu/8`, then

`boxed:
 ||p_q||_infinity
 <=3 sqrt(2) 400^(1/3) (D_B^2 kappa mu)^(-1/6)
 <31.261 (D_B^2 kappa mu)^(-1/6).`                               (2.6)

Thus the nonzero second mismatch eigenvalue can tend to zero arbitrarily: the estimate switches to (2.6) rather than dividing by that small tail. The only mismatch state not paid by Theorem 2.1 is

`T=0`, equivalently `K=B^{-1}`.                                  (2.7)

At (2.7), pair completion leaves only the arbitrary physical diagonal `Delta` (plus affine terms) in the light remainder, so no false claim is made that the rank-two logarithmic obstruction has disappeared.

The theorem gives essential boundedness. The invoked pair-log mechanism does not by itself yield an `L1` characteristic function, so continuity is not asserted.

## 3. Proof of Theorem 2.1

### 3.1 Exact completion and the partner equation

Let

`h(y)=My+a/2`.

Since `B` is invertible,

`x^T Bx+2x^TMy+a^Tx
 =(x+B^{-1}h(y))^T B (x+B^{-1}h(y))-h(y)^T B^{-1}h(y)`.           (3.1)

Therefore the completed remainder on the untouched original product bank `y` has quadratic matrix

`R0=Delta+M^T(K-B^{-1})M
   =Delta+M^T L M`,                                               (3.2)

with all induced affine and constant terms retained. This is the actual equation at which the fleet02/B19 common-plane theorem is used.

The two nonzero eigenvalues of `M^T L M` are exactly the eigenvalues of `T=G^(1/2)LG^(1/2)`: nonzero eigenvalues of `M^TLM` equal those of `LMM^T=LG`, and `LG` is similar to the symmetric matrix `T`. If `u,v` are corresponding orthonormal eigenvectors in the physical `y`-coordinate space, then

`M^T L M=theta_1 uu^T+theta_2 vv^T`,                              (3.3)

and `span{u,v}=range(M^T)` whenever `theta_2!=0`. Hence

`u_i^2+v_i^2=ell_i<=1/2`.                                        (3.4)

If `theta_2=0`, the surviving eigenvector still lies in `range(M^T)`, so `u_i^2<=ell_i<=1/2`.

### 3.2 Balanced mismatch: apply the completed rank-two half-Riesz estimate

If `|theta_2|>=mu/8`, then

`|theta_1 theta_2|>=mu^2/8`.                                     (3.5)

The remainder (3.2) is an arbitrary diagonal twist plus a spread rank-two matrix satisfying the exact leverage gate (2.1). By (1.4),

`H_{1/2}(R)
 <=8 sqrt(2) |theta_1 theta_2|^(-1/4)`.                           (3.6)

Since

`1_{|R-s|<rho} <= sqrt(rho)|R-s|^(-1/2)`,                         (3.7)

(1.6) holds with the right side of (3.6) as `H`. Substituting into (1.7) gives

`||p_q||_infinity
 <=16*2^(1/4)(D_B kappa)^(-1/4)|theta_1theta_2|^(-1/8)
 <=16*2^(5/8)(D_B kappa mu)^(-1/4)`,                              (3.8)

which is (2.5). Notice that `theta_1 theta_2` may have either sign.

For reference, before the `mu/8` split the exact determinant form is

`||p_q||_infinity
 <=16*2^(1/4)(D_B kappa)^(-1/4)|det T|^(-1/8)`.                  (3.9)

Since

`det T=S^2 det(K-B^{-1})=S^2 det(I-BK)/det B`,                   (3.10)

(3.9) is equivalently

`||p_q||_infinity
 <=16*2^(1/4)
   [D_B kappa^2 S^2 |det(I-BK)|]^(-1/8)`.                        (3.11)

This gives an invariant combined currency involving the physical pair, partner cross area, and the four-dimensional normalized common-plane determinant.

### 3.3 Rank-one collar: a diagonal-distance lemma

The central new observation is that the second mismatch direction is **not needed** once it is small compared with the first.

#### Lemma 3.1 — diffuse rank-one matrix cannot be hidden by a diagonal

Let `u` be a unit vector with `max_i u_i^2<=1/2`. Then for every real diagonal matrix `D0`,

`||D0+theta uu^T||op >= |theta|/4`.                               (3.12)

More generally, for a unit vector `v` and any real `eps`,

`||D0+theta uu^T+eps vv^T||op >= |theta|/4-|eps|`.                (3.13)

**Proof.** Put

`W=sign(theta)(uu^T-diag(u_i^2))`.

Then `diag W=0` and

`||W||_* <= ||uu^T||_*+||diag(u_i^2)||_*=2`.                      (3.14)

Thus `Z=W/2` has nuclear norm at most one and is orthogonal, in trace pairing, to every diagonal matrix. Operator/nuclear duality gives

`||D0+theta uu^T||op
 >=|tr[Z(D0+theta uu^T)]|
 =|theta|/2 (1-sum_i u_i^4)`.                                    (3.15)

Because

`sum_i u_i^4 <= (max_i u_i^2) sum_i u_i^2 <=1/2`,                (3.16)

(3.12) follows. Adding `eps vv^T` changes operator norm by at most `|eps|`, proving (3.13). QED.

Apply the lemma to (3.2)-(3.3). When `|theta_2|<mu/8`,

`||R0||op >= mu/4-|theta_2| > mu/8`.                              (3.17)

This lower bound is uniform over the arbitrary physical diagonal `Delta`; it is exactly what prevents the diagonal twists from cancelling the surviving common-plane direction.

### 3.4 Spend (3.17) by the completed arbitrary-rank small-ball theorem

Apply (1.8) to the actual remainder matrix `R0`. Uniformly in every affine term,

`sup_s P(|R-s|<rho)
 <=5(8rho/mu)^(1/4).`                                             (3.18)

This is the requested application of completed peer mathematics to an actual new inequality: the source norm parameter is not formal but is supplied by (3.17).

It remains only to combine this quarter-power small ball with the physical pair logarithm. The pair envelope in the source gives, for every cutoff `r>0`,

`p_q(t)<=2sqrt(2)/r
 +D_B^(-1/2) E log_+(2r^2/(kappa|t-R|))`.                         (3.19)

For a small-ball bound `P(|R-s|<rho)<=H rho^(1/4)`, layer cake yields

`E log_+(a/|t-R|)
 <=int_0^infinity H a^(1/4)e^(-v/4)dv
 =4H a^(1/4)`.                                                    (3.20)

With `H=5(8/mu)^(1/4)` and `a=2r^2/kappa`, (3.19) becomes

`p_q(t)
 <=2sqrt(2) r^(-1)
   +40 D_B^(-1/2) kappa^(-1/4) mu^(-1/4) r^(1/2)`.                (3.21)

Minimizing `A/r+B sqrt(r)` gives `3(A B^2/4)^(1/3)`. With `A=2sqrt(2)` this is exactly

`3 sqrt(2) 400^(1/3)
 D_B^(-1/3) kappa^(-1/6) mu^(-1/6)`,                             (3.22)

which is (2.6). QED.

## 4. What has actually been closed

Before this run, the exact common-plane endpoint had a dangerous apparent discontinuity: a rank-two mismatch could be paid by a determinant estimate, while the bound diverged as its second eigenvalue approached zero, even though the exact rank-one endpoint should be easier.

Theorem 2.1 removes that discontinuity **without setting the small eigenvalue to zero**. For every `mu>0`, the whole interval

`0 <= |theta_2| < infinity`

is covered by (2.5) or (2.6). The arbitrary diagonal `Delta` is retained exactly, and no moment or support property of the input laws is used.

The exact latent center is now the single algebraic condition

`boxed: G^(1/2)(K-B^{-1})G^(1/2)=0`,

or equivalently

`boxed: K=B^{-1}`.                                                (4.1)

Thus, inside the low-leverage no-coloop exact partner endpoint, **the only common-plane mismatch not spent is the exact latent rank-two cancellation itself**, not a punctured neighborhood and not a rank-one tube.

For a fixed bookkeeping threshold `mu_0>0`, every state with `mu>=mu_0` has an explicit finite bound depending only on the physical pair currencies and `mu_0`. The theorem deliberately does not treat a tiny physical pair as zero: its dependence on `D_B,kappa` remains visible.

## 5. Compact conditional proof graph after this run

The compatible proof assembly is now:

1. Existing volume/Fourier exits pay diagonal, diffuse rank-three, physical `E_3/E_5`, and several projected-crossing branches. Full QFORM remains open.
2. The finite-core compiler reduces a principal difficult branch to `|H|<=124` with a rank-two `H-L` crossing packet and explicit retained tails.
3. Fleet02/B19 r36 chooses two literal hubs with fixed cross area `S>S0`, pays aggregate leaf-transverse third volume, and classifies the exact zero-height endpoint into no-coloop common plane, one coloop plus one physical star, or two coloops plus two physical stars.
4. In the **no-coloop, low-leverage, exact common-plane chamber**, this run pays every nonzero normalized Schur mismatch `T`, including its exact rank-one degeneration, by Theorem 2.1.
5. A quantitatively strong physical pair is independently paid in the full ambient matrix by the completed arbitrary-rank pair theorem; fleet03/B19 r42 further shows that failure of those pair payments forces a low-rank `H`-side structural collapse. These statements do not by themselves identify the full target's third resource inside the exact latent center.

The first compatible unpaid implication is therefore sharpened to

`QFORM-EXACT-LATENT-CENTER-PLUS-THIRD-CARRIER-v1`:

> In the finite-core two-hub collar, after the transverse and coloop/star exits, suppose the no-coloop low-leverage light block is exactly
> `Delta+M^T B^{-1} M` so that completing the two physical hubs leaves only the physical diagonal `Delta` on the light bank. Spend the full matrix's genuinely third large spectral resource jointly with this exact latent rank-two cancellation, while retaining the conditioned affine data, the nonzero `H\T` cross tail, every diagonal twist, arbitrary extra spectrum, and original-product provenance.

The parallel residues are: high light leverage `>1/2`, one/two-coloop finite-star packets, singular/quantitatively weak hub pairs, and the **near** common-plane state in which the partner's aggregate transverse residual is small but nonzero. None is silently identified with the exact state.

## 6. Corrections preserved and status

- `QFORM-POINTWISE-DECAY-FALSE`: never used.
- `QFORM-FIBER-SUP-DIMENSION-LOSS`: never used.
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: all probabilistic conditioning is on original coordinates; eigenvectors `u,v` are coefficient geometry only.
- `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`: never used.
- `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`: never used.
- `QFORM-GSTAR-SCALE-FORCING-FALSE-v1`: no singleton `G_*` scale is forced.
- `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1`: the remainder is not discarded; it is paid by an actual operator-norm small-ball theorem after (3.17).
- Small nonzero coefficients are never replaced by zero.

This is a supporting theorem and a sharper conditional proof graph, not a proof of the unrestricted conjecture. Global continuity remains open.

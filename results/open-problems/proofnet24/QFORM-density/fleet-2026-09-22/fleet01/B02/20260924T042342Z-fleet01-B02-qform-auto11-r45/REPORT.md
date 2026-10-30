SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-24T04:23:42Z.
attacking: the newest fleet02/B02 fixed physical-hub packet. First derive a law-uniform integrated Fourier norm for one literal scalar square without any pointwise decay, use it to close the partner's physical-diagonal hub at bounded-density level, and sharpen the surviving carrier-aligned off-diagonal hub to a robust hub-disjoint E2 packet.

# fleet01/B02 r45 — scalar-square L3 Fourier integration and robust E2 behind the carrier-aligned hub

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one, arbitrary real symmetric A, and at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moment, support, iid, diagonal-basis, post-rotation independence, or small-tail deletion is used. Continuity is recorded separately from essential boundedness.

## 1. Fresh source pins actually used

The newest completed designated partner available to this slot is fleet02/B02:

`yspennstate/math-open-problems@a9d0b0bd0ae5e9587eaa8aed6a21d871a5b81e56`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260924T031112Z-fleet02-B02-QFORM-auto11/REPORT.md`.

On the current literal full cut `N=A[L,R]`, its inherited source packet has

`x1*x2 > kappa := 247/576`,                                      (1.1)

where `x1>=x2>=...` are the squared singular values of N. Its theorem attacks a literal physical hub i. All transverse cases are already Fourier-L1 paid. The only unpaid alternatives from that theorem are:

1. a physical diagonal `|A_ii|>1/512`;
2. a carrier-aligned off-diagonal hub of size `>1/(512 sqrt(2))`;
3. at most two top-two near-coloops on each side;
4. the separately tracked fixed overlap-one V1 grouped-pivot packet.

The target-level scalar-pivot closure used below is fleet03/B01,

`yspennstate/math-open-problems@28cbe14c4381d5f1b58145b29bbcc160b4d2ea5c`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T233049Z-auto11/REPORT.md`.

It proves, for every target matrix with `s3(A)>=1`, that any literal nonzero physical diagonal `a=A_ii` yields

`||p_Q||_infinity < 137 |a|^(-1/2)`.                            (1.2)

This is essential boundedness; that theorem does not assert Fourier L1 or continuity.

For the new robust-E2 consequence I use fleet02/B06,

`yspennstate/math-open-problems@cd0be625c8f7143a46ad14bb936e9c24bfb19a8d`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260923T192839Z-auto11/REPORT.md`.

For any literal physical cross block M with `Z=e2(M^T M)>0`, it proves the row-gate-free full-ambient fractional-potential estimate

`H_(1/2)(Q):=sup_s E|Q-s|^(-1/2) <= 8 e^(1/4) Z^(-1/8)`.         (1.3)

The same source emphasizes the binding correction: finite E2 / finite half-Riesz credit alone does not imply an L-infinity density; a third smoothing resource is genuinely needed.

## 2. New theorem: a literal scalar square has a uniform L3 Fourier norm

The pointwise law-uniform Fresnel estimate is false for fragmented supports, so do not seek pointwise decay. Instead integrate in frequency first.

Let X be any real random variable with probability density f satisfying `0<=f<=1`. For a real shift c define

`F_c(s)=E exp(i s (X+c)^2)`.                                     (2.1)

### Theorem 2.1 — `QFORM-SCALAR-CHIRP-L3-v1`

Uniformly over every admissible f and every shift c,

`boxed: integral_R |F_c(s)|^3 ds <= 32*pi.`                     (2.2)

Equivalently,

`||F_c||_3 <= (32*pi)^(1/3)`.                                   (2.3)

This is an integrated Fourier statement and uses no pointwise decay.

### Proof

Let `Y=(X+c)^2`. For `y>0` its density is

`g_c(y)=[f(sqrt(y)-c)+f(-sqrt(y)-c)]/(2 sqrt(y))`.               (2.4)

Thus

`int_0^infinity g_c(y)dy=1`,                                    (2.5)

and the cap-one assumption gives the pointwise density envelope

`0<=g_c(y)<=y^(-1/2)`.                                          (2.6)

For any R>0,

`int_0^R g_c(y)^(3/2)dy
 <=int_0^R y^(-3/4)dy
 =4 R^(1/4)`,                                                     (2.7)

while on the tail

`int_R^infinity g_c(y)^(3/2)dy
 <=R^(-1/4) int_R^infinity g_c(y)dy
 <=R^(-1/4)`.                                                     (2.8)

The right side `4R^(1/4)+R^(-1/4)` is minimized at `R=1/16`, giving

`int g_c^(3/2) <=4`,                                             (2.9)

hence

`||g_c||_(3/2)<=4^(2/3)`.                                       (2.10)

With Fourier convention `hat g(s)=int exp(isy)g(y)dy`, Riesz-Thorin between `L1->L_infinity` and Plancherel gives

`||hat g||_3 <=(2*pi)^(1/3)||g||_(3/2)`.                         (2.11)

Since `F_c=hat g_c`, cubing (2.11) and using (2.10) gives

`||F_c||_3^3 <=2*pi*(4^(2/3))^3=32*pi`.                          (2.12)

QED.

### Corollary 2.2 — one arbitrary physical scalar pivot

Write a general quadratic form by completing one ORIGINAL coordinate i with `a=A_ii!=0`:

`Q=a(X_i+h(Z))^2+R(Z)`,                                         (2.13)

where Z is the collection of all other original coordinates. Since `X_i` remains independent of Z,

`phi_Q(t)=E_Z[ exp(itR(Z)) F_(h(Z))(a t) ]`.                     (2.14)

Minkowski in `L3(dt)` and Theorem 2.1 yield

`boxed: ||phi_Q||_3^3 <= 32*pi/|a|,`                            (2.15)

or

`boxed: ||phi_Q||_3 <= (32*pi/|a|)^(1/3).`                      (2.16)

All dense residual curvature and every outside coupling are retained. This does not by itself imply Fourier L1 or continuity.

## 3. Genuine Fourier-L1 corollary: three source-separated physical squares

The new `L3` estimate gives a clean correction-safe Fourier-L1 theorem whenever three literal source coordinates have no mutual cross coefficients.

### Corollary 3.1 — `QFORM-THREE-SEPARATED-SQUARES-FOURIER-L1-v1`

Suppose three ORIGINAL coordinates `i,j,k` satisfy

`A_ij=A_ik=A_jk=0`,                                               (3.1)

and put `a=A_ii`, `b=A_jj`, `c=A_kk`, with `abc!=0`. No restriction is placed on couplings from these coordinates to the remaining coordinates, nor on the quadratic form among the remaining coordinates. Then

`boxed:
 integral_R |phi_Q(t)|dt
 <=32*pi |abc|^(-1/3).
}`                                                                  (3.2)

Consequently Q has a continuous `C0` density and

`boxed: ||p_Q||_infinity <=16 |abc|^(-1/3).`                    (3.3)

### Proof

Condition on all coordinates outside `{i,j,k}`. Because the three mutual cross coefficients vanish, the conditional three-coordinate phase is the sum of three independently shifted scalar squares plus a constant. Therefore its characteristic function is the product of three factors of the form `F_shift(a_r t)`. Holder with exponents `(3,3,3)` and (2.15) gives the conditional L1 bound (3.2), uniformly in the conditioning. Average the conditional characteristic functions and use Minkowski/Tonelli to retain the same bound. Fourier inversion gives (3.3) and continuity. QED.

This theorem is stronger than merely bounding the density on this scoped branch: it proves exactly the unweighted integrated-Fourier property requested by B02, without any scalar pointwise van-der-Corput statement.

## 4. Equation-level application of the completed fleet02/B02 partner

Apply the partner's actual physical-hub alternative. If its diagonal branch occurs,

`|a|=|A_ii|>1/512`.                                               (4.1)

The target-level scalar-pivot closure (1.2) gives immediately

`boxed:
 ||p_Q||_infinity
 <137 sqrt(512)
 =3099.9561287218244.
}`                                                                  (4.2)

This closes the partner's physical-diagonal hub alternative at the level of the owner theorem. Continuity is **not** claimed from (4.2).

The new integrated estimate (2.16) simultaneously gives the genuinely Fourier statement

`boxed:
 ||phi_Q||_3
 <(32*pi*512)^(1/3)
 =37.19831524830804.
}`                                                                  (4.3)

Thus this partner branch is not Fourier-L1 paid, but it now has both a dimension-free target density payment and a source-valid nontrivial integrated Fourier norm. No pointwise scalar decay is used.

This is an actual equation-level application of the designated fleet02/B02 result: its literal inequality (4.1) is fed into (1.2) and (2.16).

## 5. New deterministic theorem behind the carrier-aligned hub

Return to the partner's off-diagonal carrier-aligned alternative on the full physical cut `N=A[L,R]`. Let `u1,u2` be its top two left singular vectors and set

`ell_i=u1(i)^2+u2(i)^2`.                                        (5.1)

The partner has already paid every transverse case. Apart from its at-most-two-per-side near-coloops, we may therefore assume

`ell_i<=3/4`.                                                     (5.2)

Let `N_(-i)` denote N with physical row i deleted.

### Lemma 5.1 — `QFORM-TOPTWO-ROW-DELETION-E2-v1`

For every physical row i,

`boxed:
 E2(N_(-i)) >= x1*x2*(1-ell_i).
}`                                                                  (5.3)

### Proof

Retain only the contribution of the top two singular directions to the complete squared `2x2`-minor mass of `N_(-i)`. Their coefficient is `x1*x2`. Since `u1,u2` are orthonormal, the total squared exterior mass `||u1 wedge u2||^2` equals one. The portion incident to row i is

`sum_(j!=i) (u1(i)u2(j)-u2(i)u1(j))^2
 =u1(i)^2+u2(i)^2
 =ell_i`.                                                         (5.4)

Hence the exterior mass supported entirely away from i is exactly `1-ell_i`, giving (5.3). QED.

Combining (1.1), (5.2), and (5.3), every non-near-coloop carrier-aligned survivor has a literal hub-disjoint physical cross block with

`boxed:
 E2(N_(-i)) > (247/576)*(1/4)
 =247/2304
 =0.1072048611111111.
}`                                                                  (5.5)

This is a robust rank-two currency that does not use the small cross tail and does not delete the hub variable.

## 6. Actual analytic consequence of the robust E2 packet

Apply the completed row-gate-free E2 half-Riesz theorem (1.3) to the **full ambient Q** using the literal block `N_(-i)`. Equation (5.5) gives

`boxed:
 H_(1/2)(Q)
 <8 e^(1/4) (247/2304)^(-1/8)
 =13.57959437414361.
}`                                                                  (6.1)

Therefore, uniformly in the level s and every epsilon>0,

`boxed:
 P(|Q-s|<=epsilon)
 <13.57959437414361 sqrt(epsilon).
}`                                                                  (6.2)

This is not yet a density theorem: the live E2 correction shows exactly why the square-root small-ball profile cannot be promoted to `O(epsilon)` without consuming a third smoothing resource.

There is an additional useful normalization. Since Section 4 already pays **any** physical diagonal with modulus at least `1/512`, every still-unpaid carrier-aligned branch may now be studied under the global coefficient restriction

`boxed: max_j |A_jj| <1/512.`                                    (6.3)

Thus the diagonal-hub alternative is gone from this frontier.

## 7. Correct current B02 frontier

After applying the newest fleet02/B02 theorem and the results above, the live B02 list is sharpened to:

1. the pre-existing fixed overlap-one `V1` grouped-pivot packet;
2. at most four top-two near-coloop coordinates total;
3. a non-near-coloop carrier-aligned physical hub, under the global small-diagonal condition (6.3), with the robust **hub-disjoint** packet
   `E2>247/2304` and the full-law half-Riesz bound (6.1).

The next implication is therefore

`QFORM-SMALLDIAG-CARRIER-HUB-PLUS-DISJOINT-E2-L1-v1`:

use the fixed physical hub jointly with the robust disjoint E2 crossing to obtain either genuine Fourier L1 / `O(epsilon)` small-ball control or another literal physical E3 / grouped-hub receiver. The hub cannot simply be discarded, the small diagonal cannot be replaced by zero, and finite E2 alone cannot be promoted to bounded density.

The present scalar-square `L3` theorem suggests the right integrated-frequency shape when a nonzero pivot is usable, but `L3` plus a critical `|t|^-1` two-direction envelope does not by itself imply L1. A successful proof still has to couple the two mechanisms before taking absolute values.

## 8. Status and continuity ledger

- **Full QFORM:** OPEN / not proved / not disproved.
- **Target-wide universal unweighted Fourier L1:** OPEN / NOT REFUTED.
- **New integrated theorem:** every literal scalar pivot gives the uniform `L3` estimate (2.15).
- **New Fourier-L1 branch:** three source-separated physical squares satisfy (3.2), hence continuous `C0` density.
- **Newest fleet02/B02 transverse branches:** already Fourier-L1 paid by the partner, hence continuous there.
- **Partner physical-diagonal hub:** bounded density paid by (4.2); continuity not proved by this payment. It also satisfies the integrated `L3` estimate (4.3).
- **Carrier-aligned non-near-coloop survivor:** robust `E2>247/2304` and `H_(1/2)<13.58`, but bounded density / continuity remain open on that local interface.

No exact-target counterexample to target-wide Fourier L1 was found. The phase-aligned fragmented-support correction remains fully operative: the new estimates integrate in frequency and never assert a law-uniform pointwise scalar quadratic decay.

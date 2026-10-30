SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T19:28:39Z.
attacking: partner r41's reciprocal near-rank-one two-hub survivor; derive a product-weighted two-bank bilinear receiver from aggregate two-dimensional coefficient area, and isolate exactly where the third large direction is still needed when that area collapses.

# fleet02/B06 auto11 — row-gate-free E2 half-Riesz compiler and the exact third-resource debt

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `b06-20260923T192839Z-auto11`  
Role: Curved fiber integration  
Status: **PROVED SUPPORTING THEOREM / PINNED RESULT APPLIED / PARTNER r41 APPLIED / ROUTE OBSTRUCTION RETAINED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains OPEN. Essential boundedness is not proved here, and continuity is not claimed. The new theorem is a fractional-potential estimate; the live correction `QFORM-E2-HALFRIESZ-ALONE-NOT-LINF-v1` is retained explicitly.

## 1. Fresh scope and source pins

Fresh owner control before the substantive write remained revision `2026-09-22.15`, QFORM-only, with no fleet02/B06 pause. The exact target is the arbitrary independent cap-one, arbitrary-dimensional, arbitrary-sign symmetric-matrix problem with at least three eigenvalues of modulus at least one. No moments, compact support, log-concavity, iid structure, diagonal-basis independence, or independence after rotation is introduced.

The required pinned Claude-era source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

especially `FOURIER_ROUTE_REPORT.md`. Its proved `D_k` estimate says that for a literal original-coordinate cross block `M`, `Z_k=e_k(M^TM)`, natural k-volume row marginals `alpha_i`, and `q>=1` satisfying `alpha_i<=q/2`, the decoupled characteristic function obeys

`|phi_Q(t)|^2 <= [e^(k/2)(2*pi/|t|)^k q^(-k/2) Z_k^(-1/2)]^(1/q)`.

At `k=2,q=1` this becomes

`|phi_Q(t)| <= min(1, 2*pi*sqrt(e) Z_2^(-1/4)|t|^(-1))`             (1.1)

whenever every natural two-volume row marginal is at most one half. The proof retains arbitrary same-bank quadratic blocks, linear terms and outside couplings.

The newer checked grouped-projection theorem used in the heavy-row complement is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its `k=1, ell=1` grouped-hub estimate allows an arbitrary hub function and arbitrary same-bank light curvature. Its exact-rank-two crossing theorem likewise allows arbitrary internal functions on both product banks.

The designated partner result actually used is fleet03/B06 r41,

`yspennstate/math-open-problems@e16064c2d89e7c30e8876283baf6e58047127263`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T181904Z-fleet03-B06-qform-r41/REPORT.md`.

The later correction source retained is fleet02/B20 auto11c, which proves that finite E2 half-Riesz credit by itself does not imply an L-infinity density: a two-large-eigenvalue product quadratic form can have a logarithmically unbounded density despite a fixed positive E2 packet.

## 2. Riesz conversion at the borderline |t|^-1 exponent

For any real random variable `Y`, define

`H_(1/2)(Y)=sup_s E|Y-s|^(-1/2)`.

The exact Riesz representation is

`|x|^(-1/2)=sqrt(2/pi) int_0^infty cos(tx)t^(-1/2) dt`.             (2.1)

Consequently, whenever

`|phi_Y(t)|<=min(1,K/|t|)`,                                         (2.2)

absolute integration in (2.1), split at `t=K`, gives

`H_(1/2)(Y)
 <=sqrt(2/pi)[int_0^K t^(-1/2)dt + K int_K^infty t^(-3/2)dt]
 =4 sqrt(2/pi) sqrt(K).`                                            (2.3)

This is the correct use of a `|t|^-1` endpoint: it gives half-Riesz credit, not Fourier L1 inversion.

## 3. Main theorem: the E2 row-marginal gate can be removed

Let `Q` be any quadratic polynomial in independent original coordinates whose densities are at most one. Let `I,J` be disjoint physical coordinate banks and let

`M=A[I,J]`,
`Z=e_2(M^TM)=sum_(|S|=|T|=2) det(M[S,T])^2>0`.                     (3.1)

All coordinates outside `I union J` may be conditioned on; all estimates below are uniform in the resulting affine terms, so averaging at the end is harmless.

Normalize the squared 2x2 minors by `Z`, and let

`alpha_i=P(i belongs to sampled row-pair)`, `sum_i alpha_i=2`.      (3.2)

### Theorem 3.1 — `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`

Without any row-marginal hypothesis,

`boxed: H_(1/2)(Q) <= 8 e^(1/4) Z^(-1/8).`                         (3.3)

Numerically the universal coefficient is

`8 e^(1/4)=10.2722033335...`.

The theorem retains arbitrary quadratic curvature inside both banks, every additional cross singular direction, arbitrary affine terms, and every conditioned outside coefficient. No individual small minor is inverted.

### 3.1 Diffuse natural two-volume law

If

`max_i alpha_i<=1/2`,                                               (3.4)

apply the required pinned theorem (1.1). With

`K=2*pi*sqrt(e) Z^(-1/4)`,

(2.3) gives exactly

`H_(1/2)(Q)
 <=4 sqrt(2/pi) sqrt(2*pi*sqrt(e)) Z^(-1/8)
 =8 e^(1/4) Z^(-1/8).`                                             (3.5)

This is the requested equation-level use of the completed `e5f71...` result.

### 3.2 Heavy natural row: exact aggregate transfer

Suppose instead that some physical row `i` satisfies

`alpha_i>1/2`.                                                      (3.6)

Write its full cross row as `m=M[i,J]` and put

`C=M[I\{i},J](I-P_m)`, `F=||C||_F`,                               (3.7)

where `P_m` is orthogonal projection onto `span(m)` in the literal coefficient space `R^J`.

For a remaining row `y`, Lagrange's identity gives

`sum_(|T|=2) det([m;y]_T)^2
 =||m wedge y||^2
 =||m||^2 ||y(I-P_m)||^2`.                                        (3.8)

Summing (3.8) over all remaining physical rows yields the exact weighted identity

`boxed: ||m||^2 F^2 = alpha_i Z.`                                  (3.9)

Thus the whole determinant packet is transferred before any reciprocal payment.

#### 3.2a Diffuse projected rows

Assume every row `c_j` of `C` satisfies

`||c_j||^2<=F^2/2`.                                                (3.10)

Use physical coordinate `i` as one hub. In the checked grouped-hub theorem choose the original `J` bank as the rank-one hub-coefficient bank. Its singular-value product is `||m||`; the `ell=1` projected crossing is exactly `C`, with `Z_1=F^2`, and (3.10) is precisely its row-marginal gate. Since the hub is one original cap-one coordinate, its projected density cap is one. The theorem gives

`|phi_Q(t)|
 <=min(1,2*pi (||m||F)^(-1/2)|t|^(-1)).`                           (3.11)

Equation (2.3) and (3.9) therefore give

`H_(1/2)(Q)
 <=8 (||m||F)^(-1/4)
 =8 (alpha_i Z)^(-1/8)
 <8*2^(1/8) Z^(-1/8).`                                             (3.12)

The coefficient `8*2^(1/8)=8.7240618613...` is already smaller than the diffuse-case coefficient in (3.5).

#### 3.2b One projected physical row is concentrated

If (3.10) fails, choose a literal remaining row `y` with residual

`c=y(I-P_m)`, `||c||>F/sqrt(2)`.                                   (3.13)

Then the physical two-row crossing area satisfies

`S_2:=||m wedge y||=||m|| ||c||
 > ||m||F/sqrt(2)
 =sqrt(alpha_i Z/2)
 >sqrt(Z)/2.`                                                       (3.14)

Condition on every same-side original coordinate except the two supporting `m,y`. The remaining active product banks are the two original hub coordinates and the untouched original `J` bank. Their cross block has singular-value product exactly `S_2`. The checked exact-rank-two crossing theorem applies with projection-density caps `M_X<=1` on the two-coordinate hub side and `M_Y<=2` on the two-dimensional orthogonal projection of the product `J` bank. Hence, uniformly in the conditioning,

`|phi(t)|<=min(1,pi*sqrt(2) S_2^(-1/2)|t|^(-1)).`                  (3.15)

Using (2.3),

`H_(1/2)(Q)
 <=2^(11/4) S_2^(-1/4)
 <2^(23/8)(alpha_i Z)^(-1/8)
 <8 Z^(-1/8).`                                                     (3.16)

Averaging the uniform conditional estimate preserves (3.16).

The diffuse case (3.5) dominates both heavy-row branches (3.12), (3.16), proving Theorem 3.1.

## 4. Application to the designated partner r41 at its actual currency

Partner r41's literal complete physical cross block `N` has

`E=||N||_F^2 > E0=11907/16384`,                                   (4.1)

`Z_2=e_2(N^TN) > (31/2048) E^2`,                                  (4.2)

and its identified physical anchor row `i` has natural determinant-pair inclusion marginal

`alpha_i>3/5`.                                                      (4.3)

Therefore this partner packet is automatically in the heavy-row arm of the proof above. The stronger heavy-row estimate, before replacing `alpha_i` by one half, is

`H_(1/2)(Q)<=8(alpha_i Z_2)^(-1/8)`                                (4.4)

(the concentrated projected-row subcase has the smaller coefficient `2^(23/8)`). From (4.1)-(4.3),

`alpha_i Z_2
 >(3/5)(31/2048)(11907/16384)^2
 =13185228357/2748779069440
 =0.004796758132943069...`.                                        (4.5)

Thus the entire r41 ultra-thin packet, before using its `>99.7263%` rank-one conclusion or reciprocal `>0.430993` anchor coordinates, satisfies the dimension-free full-ambient estimate

`boxed: H_(1/2)(Q)<15.594502.`                                     (4.6)

Consequently, for every `epsilon>0`,

`boxed: sup_s P(|Q-s|<=epsilon)<15.594502 sqrt(epsilon).`           (4.7)

This retains the complete nonzero cross tail and every same-bank quadratic term. It improves the older unconditional E2 compiler coefficient `26.334...` and shows that the reciprocal rank-one geometry is no longer needed merely to obtain half-Riesz credit; it must now be spent specifically on the **third smoothing resource** needed for linear small-ball control.

## 5. Why Theorem 3.1 cannot be promoted to density without the third resource

The live B20 correction already proves this abstract implication false. A minimal transparent model is also useful.

Take four independent cap-one centered uniforms and set

`Q_0=(X+U)^2-(Y+V)^2`.                                             (5.1)

Across the original cut `{X,Y}|{U,V}`, the physical cross block is `diag(1,-1)`, hence

`e_2(M^TM)=1`.                                                      (5.2)

Theorem 3.1 therefore gives finite half-Riesz credit. But with

`S=X+U`, `T=Y+V`,

both `S,T` have continuous densities positive near zero and are independent, while

`Q_0=S^2-T^2=(S-T)(S+T)`.                                          (5.3)

The joint density of `(S-T,S+T)` is positive in a neighbourhood of the origin, so the product-density formula contains an `int dp/|p|` term and `p_(Q_0)(q)` diverges logarithmically as `q->0`. The matrix of (5.1) has only two nonzero eigenvalues `+2,-2`; this is a route counterexample, not a QFORM counterexample.

Add one independent cap-one variable `Z`:

`Q_*=(X+U)^2-(Y+V)^2+Z^2`.                                        (5.4)

Now the original matrix has nonzero spectrum `{2,-2,1}`, so this is a genuine QFORM-target family. The grouped variables `S,T,Z` use disjoint original banks, remain genuinely independent, and each has density cap at most one. The pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A applied to the three-variable form

`S^2-T^2+Z^2`

gives the actual all-level bound

`boxed: ||p_(Q_*)||_infinity <=6 sqrt(pi)=10.6347231054... .`       (5.5)

Thus the third direction really repairs this exact logarithmic obstruction when it is source-separated. The open r41 problem is that its third spectral resource is generally coupled to the same original banks and cannot be replaced by an independent square by rotation.

## 6. First unpaid implication after this run

The next B06 debt is

`QFORM-R41-COUPLED-THIRDRESOURCE-AFTER-E2-v1`.

In the partner r41 ultra-thin packet, Theorem 3.1 already pays all two-volume geometry by (4.6). What remains is to use the reciprocal physical anchors, the robust opposite stars/cofactor packet and the actual third large spectral direction **jointly** to upgrade the `sqrt(epsilon)` profile to `O(epsilon)`, while retaining arbitrary same-bank curvature and the complete nonzero tail.

A valid route may be a genuine two-hub-plus-one-projected-crossing grouped theorem with a uniformly positive parameter, or a source-preserving square/hyperbola peel in which the third resource is isolated before the half-Riesz payment. What is not available is an abstract implication `H_(1/2)<infinity => ||p||_infinity<infinity`, a deletion of a small quadratic tail, or independence after spectral rotation.

## 7. Status

- **Proved:** `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`, equation (3.3).
- **Required pinned result applied:** `e5f71...` `D_k` at `k=2,q=1`, equation (3.5); pinned `COUNTEREXAMPLE_SEARCH` Theorem A at (5.5).
- **Designated partner applied:** fleet03/B06 r41 at equations (4.1)-(4.7).
- **Route obstruction retained:** positive E2 and finite half-Riesz do not by themselves imply bounded density.
- **Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.
- **Continuity:** not claimed by the new theorem.

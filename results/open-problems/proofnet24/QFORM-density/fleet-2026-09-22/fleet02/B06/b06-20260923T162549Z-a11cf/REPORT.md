SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T16:25:49Z.
attacking: partner r38 recursive rank-two cross tube: fuse same-bank Fresnel curvature with the complete transverse physical cross-volume before any reciprocal fiber payment.

# fleet02/B06 — Fresnel / cross-volume fusion

**Run:** `b06-20260923T162549Z-a11cf`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed at the substantive checkpoint:** revision `2026-09-22.15`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains OPEN: for arbitrary independent ORIGINAL-coordinate densities bounded by one and symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^TAX`, or give a valid counterexample. No moment, support, log-concavity, iid, diagonal-basis, or post-rotation independence assumption is introduced. Continuity is tracked separately.

## 1. First unpaid implication and source-valid inputs

The fresh designated partner is fleet03/B06 r38:

`yspennstate/math-open-problems@ba023626f934128aadad51710c9ee8428dfe33c7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T144727Z-fleet03-B06-qform-r38/REPORT.md`.

Its recursive debt is to retain the small nonzero tail of an ORIGINAL-coordinate cross block trapped near rank two while also retaining arbitrary same-bank curvature. Its r37 predecessor

`yspennstate/math-open-problems@fa9d5dd3cc78a092484480b536872d332e22c90a`

proves, in the true near-rank-two chamber of the live N3 cross cut `N`, with squared singular values `x_1>=x_2>=...` and `E=||N||_F^2`,

`E > 11907/16384`,
`sum_{j>=3} x_j < E/64`,
`x_2 >= E/64`,

and therefore

`Z_2:=e_2(N^T N) > (31/2048) E^2
                   > 0.007994596888238448`.

The newest-Claude packet actually consumed is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The exact completed ingredients applied below are its Fresnel linearisation and its Lemma 1,

`integral |hat g|^p <= 4 pi / sqrt(p), p>=2,`

for every complex `g` dominated by a cap-one probability density, together with the determinant-weighted Brascamp--Lieb expansion audited in `FOURIER_ROUTE_REPORT.md`. Its `COUNTEREXAMPLE_SEARCH.md`, Theorem C, will also be applied to the exact target family in Section 6 to identify the one-sheet/two-sheet split.

The first unpaid implication attacked here is:

`QFORM-RANK2-TUBE-NONNULL-BANK-THIRD-DIRECTION-v1`,

but only a genuine structured subbranch is claimed paid. The arbitrary-same-bank case remains open.

## 2. Aggregate fusion currency

Let `I,J` be disjoint untouched ORIGINAL-coordinate banks. Suppose, after conditioning only coordinates outside `I union J`, the quadratic part on `I union J` has the form

`Q = X^T (D + V Lambda V^T) X
     + 2 X^T M Y
     + R(Y)
     + ell_X^T X + ell_Y^T Y + c`,                                  (2.1)

where

- `X=(X_i)_{i in I}`, `Y=(Y_j)_{j in J}` retain their original product law and every one-dimensional density is at most one;
- `D` is diagonal in the ORIGINAL `I` coordinates;
- `V` is an `|I| x r` matrix with orthonormal columns;
- `Lambda=diag(lambda_1,...,lambda_r)` is invertible;
- `M` is the complete physical cross block, with no singular tail removed;
- `R(Y)` is an arbitrary quadratic polynomial in the whole `Y` bank.

For an integer `k>=0`, define the physical fused volume

`Z_{r,k}(V,M)
 := sum_{|S|=r+k, |T|=k} det [ V_S , M_{S,T} ]^2`.                    (2.2)

If `Z_{r,k}>0`, put the canonical squared-minor probability

`w_{S,T}=det[V_S,M_{S,T}]^2 / Z_{r,k}`,                               (2.3)

and let

`alpha_i=P_w(i in S)`, `beta_j=P_w(j in T)`.                          (2.4)

Thus `sum_i alpha_i=r+k` and `sum_j beta_j=k`.

### Lemma 2.1 — exact transverse-volume identity

With `P_perp=I-VV^T`,

`boxed: Z_{r,k}(V,M)=e_k(M^T P_perp M).`                              (2.5)

#### Proof

For a fixed `T`, Cauchy--Binet gives

`sum_{|S|=r+k} det[V_S,M_{S,T}]^2
 = det([V,M_T]^T[V,M_T]).`

Since `V^TV=I_r`, the Schur determinant formula gives

`det([V,M_T]^T[V,M_T])
 = det(M_T^T(I-VV^T)M_T).`

Summing over all `|T|=k` is exactly the Cauchy--Binet expansion of
`e_k(M^T P_perp M)`. QED.

The currency therefore counts only cross curvature transverse to the same-bank Fresnel directions. It cannot double-count a cross direction already lying in `span(V)`.

## 3. Main theorem: Fresnel-volume fusion

### Theorem 3.1 — `QFORM-FRESNEL-VOLUME-FUSION-v1`

In (2.1), fix `k>=0` and assume

`Z:=Z_{r,k}(V,M)>0`,
`max_i alpha_i <= 1/2`,                                                (3.1)

and

`a:=k+r/2 >1`.                                                         (3.2)

Then the characteristic function of the conditional form obeys, for `t!=0`,

`boxed:
 |phi_Q(t)|
 <= C_{r,k}
    |det Lambda|^(-1/2)
    Z^(-1/2)
    |t|^(-a),`                                                         (3.3)

where

`C_{r,k}=(4 pi)^(r/2) (2 pi)^k exp(k/2).`                              (3.4)

Consequently the conditional law has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= [a/(pi(a-1))] C_{r,k}^{1/a}
    |det Lambda|^(-1/(2a))
    Z^(-1/(2a)).}`                                                     (3.5)

The same bound is an essential-density bound for a full ambient form after averaging over any coordinates conditioned away before (2.1). No continuity claim is made for that final mixture.

#### Proof

Apply the pinned Fresnel linearisation simultaneously to the `r` squares
`lambda_l <v_l,X>^2`. For every `t!=0`,

`|phi_Q(t)|
 <= prod_l (4 pi |t lambda_l|)^(-1/2)
    integral_{R^r} |Psi_t(u)| du`,                                    (3.6)

where, after conditioning at `Y=y` and discarding only phases of modulus one,

`|Psi_t(u)|
 <= integral prod_j f_j(y_j)
        prod_i H_{i,t}( <v_i,u> + 2t <m_i,y> + c_i(t) ) dy`.           (3.7)

Here `m_i` is row `i` of `M`, and

`H_{i,t}(s)=|hat g_{i,t}(s)|`,
`g_{i,t}(x)=f_i(x) exp(i t d_i x^2 + i t ell_i x)`.                    (3.8)

Thus `|g_{i,t}|=f_i`; all diagonal curvature and all induced affine terms are kept as harmless coordinatewise twists.

Integrate (3.7) jointly in `(u,y) in R^r x R^J`. Associate to row `i` the one-dimensional linear map

`B_i(t)=(v_i, 2t m_i)`,                                                (3.9)

and to coordinate `j` the map `(0,e_j)`. Use Brascamp--Lieb exponents `alpha_i` and `1-beta_j`.

The scaling identity is exact:

`sum_i alpha_i + sum_j(1-beta_j)
 = (r+k)+|J|-k
 = r+|J|`.                                                             (3.10)

For positive Gaussian parameters `d_i,e_j`, the determinant in Lieb's Gaussian formula has the physical expansion

`det( sum_i d_i B_i(t)^T B_i(t)
      + sum_j e_j (0,e_j)^T(0,e_j) )`

`>= (2|t|)^(2k)
    sum_{S,T} det[V_S,M_{S,T}]^2
       prod_{i in S} d_i prod_{j notin T} e_j`.                        (3.11)

Weighted AM--GM with (2.3) makes the right side at least

`(2|t|)^(2k) Z
 prod_i d_i^(alpha_i)
 prod_j e_j^(1-beta_j).`                                               (3.12)

Hence the Brascamp--Lieb constant is at most

`(2|t|)^(-k) Z^(-1/2)
 prod_i alpha_i^(-alpha_i/2)
 prod_j (1-beta_j)^(-(1-beta_j)/2).`                                  (3.13)

Rows with `alpha_i=0` and columns with `beta_j=1` are simply omitted.

Now use the completed newest-Claude `L^p` Fourier lemma at
`p_i=1/alpha_i>=2`:

`||H_{i,t}||_{1/alpha_i}
 <= (4 pi sqrt(alpha_i))^(alpha_i).`                                  (3.14)

Also

`||f_j||_{1/(1-beta_j)}<=1`,                                          (3.15)

because `0<=f_j<=1` and `int f_j=1`. The row factors in (3.13) cancel those in (3.14), while

`prod_j (1-beta_j)^(-(1-beta_j)/2)
 <= exp( (1/2) sum_j beta_j )
 = exp(k/2),`                                                         (3.16)

using `-x log x <=1-x`.

Since `sum_i alpha_i=r+k`, (3.7)--(3.16) give

`integral_{R^r} |Psi_t(u)| du
 <= (4 pi)^(r+k) (2|t|)^(-k) exp(k/2) Z^(-1/2).`                       (3.17)

Multiplying by the Fresnel prefactor in (3.6) yields exactly (3.3)--(3.4).

Finally `|phi_Q(t)|<=1`. For `a>1`,

`integral_R min(1,K|t|^(-a)) dt
 = 2 [a/(a-1)] K^(1/a).`                                              (3.18)

Fourier inversion gives (3.5). QED.

### Sanity endpoints

- `k=0,r=3`, `Z=1`: (3.5) is the pinned Theorem F constant `12 |det Lambda|^(-1/3)`.
- `r=0,k=2`: the new direct two-cross-volume branch below.
- A single bilinear cross direction counts as one full power of `|t|^{-1}`; a Fresnel square counts as one half-power. Thus `r=1,k=1` is already integrable (`a=3/2`), matching the spectral fact that one bilinear singular direction supplies a `+/-` pair.

## 4. Direct two-volume corollary: a nonnull diagonal bank

Set `r=0,k=2`. Then `Z=e_2(M^TM)` and (3.5) gives

`boxed:
 ||p_Q||_infinity <= 4 sqrt(e) Z^(-1/4)}`                              (4.1)

whenever the canonical physical two-minor row marginals are at most `1/2`.

This is strictly stronger in scope than the preceding B06 exact-null-bank receiver on this subbranch: the complete `I`-bank self curvature may now be any ORIGINAL-coordinate diagonal matrix, with arbitrary sizes and signs, while the `J`-bank curvature remains completely arbitrary.

There is also a useful relaxed-marginal version particular to `r=0,k=2`. If

`max_i alpha_i <= h <1`,                                               (4.2)

put `q=max(1,2h)<2`. Since the outer `Y` integral is a probability integral and the product of Fourier moduli is at most one,

`E F <= (E F^q)^(1/q).`

Run the same Brascamp--Lieb determinant estimate on `F^q`. The pinned Fourier lemma is applicable because `q/alpha_i>=2`, and gives

`|phi_Q(t)|
 <= [4e pi^2 q^(-1) Z^(-1/2)]^(1/q) |t|^(-2/q).`                      (4.3)

Therefore

`boxed:
 ||p_Q||_infinity
 <= [4 sqrt(e/q)/(2-q)] Z^(-1/4).}`                                   (4.4)

At `h=1/2`, this is exactly (4.1); at `h=2/3`, the coefficient is `3 sqrt(3e)`.

## 5. Real application to partner r37/r38

On the live true-near-rank-two cut from partner r37,

`Z_2 > 0.007994596888238448.`                                         (5.1)

Therefore, if either physical bank has diagonal same-bank quadratic block and its oriented canonical two-volume row marginals are at most `1/2`, (4.1) gives the actual all-level inequality

`boxed: ||p_Q||_infinity < 22.055052187 < 22.056.`                     (5.2)

If the row marginals are merely at most `2/3`, (4.4) gives

`boxed: ||p_Q||_infinity < 28.650354.`                                 (5.3)

No cross singular tail is deleted: `Z_2=e_2(N^TN)` uses the complete live block.

A second genuine nonnull subbranch uses `r=1,k=1`. Suppose one physical bank has

`A_II=D+lambda vv^T`,                                                  (5.4)

with `D` diagonal in the original coordinates, `||v||=1`, and `lambda!=0`. The fused currency is

`Z_{1,1}=|| (I-vv^T)N ||_F^2`.                                        (5.5)

For every unit `v`, rank-one approximation gives

`||(I-vv^T)N||_F^2 >= sum_{j>=2} x_j >= x_2 >= E/64`.                 (5.6)

Thus, if the fused row marginals are at most `1/2`, Theorem 3.1 gives

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3)e^(1/3)
    |lambda|^(-1/3) Z_{1,1}^(-1/3).}`                                 (5.7)

In particular, on the same live partner cut, whenever `|lambda|>=1`,

`boxed: ||p_Q||_infinity < 46.938074.`                                 (5.8)

This is the requested third-direction payment in a real structured nonnull-bank branch: one same-bank Fresnel direction and one aggregate transverse cross direction are fused before any local inverse minor is taken.

The partner r38 recursive problem is not thereby solved, because a general same-bank block need not equal diagonal plus one controlled rank-one piece, and applying all of its tiny spectral components at once would introduce an uncontrolled product `|det Lambda|`.

## 6. Exact target family with both banks nonnull and all cross edges diffuse

The fusion theorem closes an exact three-large-eigenvalue family that is not an exact-null-bank case.

Let `u,v in R^m` be orthonormal and satisfy

`u_i^2+v_i^2 <=1/2` for every `i`                                    (6.1)

(for example two diffuse Hadamard columns when available), and let `w in R^n` be any unit vector. Define

`A = [[ v v^T,          sqrt(2) u w^T ],
      [ sqrt(2) w u^T,  w w^T        ]].`                             (6.2)

On the invariant orthonormal basis `(v,u,w)`, the nonzero matrix is

`[[1,0,0],
  [0,0,sqrt(2)],
  [0,sqrt(2),1]],`                                                     (6.3)

so

`boxed: spec_nonzero(A)={2,1,-1}.}`                                   (6.4)

This is an exact QFORM target. Both physical same-bank blocks are nonzero and can be highly non-diagonal. If `u,w` are diffuse then every individual cross edge `sqrt(2)u_iw_j` tends to zero with dimension.

Apply Theorem 3.1 with `r=1,k=1`, `V=v`, `lambda=1`, `M=sqrt(2)uw^T`. Since `u perpendicular v`,

`Z_{1,1}=||M||_F^2=2`.                                                 (6.5)

The canonical row marginals are exactly `u_i^2+v_i^2`, hence (6.1) is the required gate. Therefore, for arbitrary independent cap-one input laws,

`boxed:
 ||p_{X^TAX}||_infinity
 <= 6 e^(1/3)
 = 8.3736745506... .}`                                                 (6.6)

This holds at every output level.

The pinned newest-Claude `COUNTEREXAMPLE_SEARCH.md`, Theorem C, applies independently to the same spectral signature and already bounds the one-sheet side (`s>=0`) by `pi sqrt(2)`. Its stated unresolved rank-three geometry is the convex/two-sheet side. Inequality (6.6) therefore supplies an all-level payment, in particular the two-sheet side, for this diffuse product-structured family.

## 7. A necessary heavy-marginal branch

One cannot append the claim that the spectral hypothesis automatically forces the fused row marginals in (3.1) to be diffuse.

Take the three-dimensional coefficient matrix represented in an original-coordinate basis by

`A = [[1,0,0],
      [0,0,sqrt(2)],
      [0,sqrt(2),1]].`                                                 (7.1)

It already has spectrum `{2,1,-1}`. In the `r=1,k=1` fusion description `v=e_1` and the only transverse cross row is `e_2`; the canonical fused minor is supported on the single row pair `{1,2}`, so both row marginals equal one. Thus a deterministic implication

`three large eigenvalues + positive fused volume => max alpha_i<=1/2`

is false.

This is not a QFORM counterexample. It is a localized heavy-hub endpoint, precisely the kind of branch that must be routed to physical-pair / mixed-hub / bounded-dimensional receivers rather than forced through a diffuse Brascamp--Lieb gate.

## 8. What remains

The new theorem pays two source-valid pieces of the partner tail-retaining debt:

1. a complete nonnull ORIGINAL-diagonal bank plus aggregate two-cross-volume; and
2. a diagonal-plus-rank-one bank plus one aggregate cross direction transverse to that rank-one curvature.

It also gives a general `r,k` fusion theorem whenever the same-bank non-diagonal curvature is a controlled low-rank Fresnel piece and the physical fused-volume marginals are diffuse.

The first unpaid implication is now

`QFORM-RANK2-TUBE-ARBITRARY-SAMEBANK-FUSION-v1`:

> In the partner r38 recursive near-rank-two cross tube, retain the complete small cross tail and arbitrary same-bank curvature. Either extract a source-valid low-rank Fresnel component whose transverse fused volume satisfies a diffuse marginal gate, or convert failure of that gate / high-rank same-bank curvature into an already-paid mixed-hub, third-volume, physical-pair, or bounded-dimensional branch, without multiplying a long list of tiny same-bank eigenvalues and without rotating the product law.

The theorem above shows exactly what a successful bridge should preserve: the currency is `e_k(M^T(I-VV^T)M)`, not a local minor and not a worst curved-fiber supremum.

**Full QFORM conjecture: OPEN / NOT PROVED / NOT DISPROVED. Universal continuity: OPEN.**

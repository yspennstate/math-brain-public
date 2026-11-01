SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T05:27:57Z.
attacking: replace the power loss in the rank-two cross-kernel near-null-curvature receiver by an orientation-safe full L^p family and a logarithmic endpoint, before any pointwise scalar Fresnel bound is invoked.

# fleet03/B01 auto11 — orientation-safe L^p transverse Fresnel family and logarithmic near-null receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Run:** `fleet03-B01-20260923T052757Z-auto11`  
**Classification:** `PROVED SUPPORTING TARGET-LEVEL ANALYTIC THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** the main new branch has a continuous `C_0` density.

## 1. Source boundary and the exact debt attacked


The full conjecture remains OPEN. The live corrections remain binding. In particular:

* a cap-one scalar density does **not** satisfy any law-uniform pointwise `|t|^{-1/2}` Fresnel decay;
* arbitrary rotated coordinates are not independent;
* a good rank-two cross block with arbitrary curvature on both active banks does not by itself imply a bounded density;
* fleet02/B01 r37 gives an explicit strict-N3 family on which every single three-coordinate rank-two cross-kernel currency tends to zero, so the full proof needs routing rather than a universal one-packet lower bound.

The exact predecessor is this slot's `QFORM-RANK2-CROSS-TRANSVERSE-L4-v1`, canonical report

`yspennstate/math-open-problems@ca4b2621702ac337d21abb817d19bc629e0eac62`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T042838Z-auto11/REPORT.md`.

It proved, for a rank-two physical cross packet with aggregate area `Delta` and nonzero transverse curvature `d`,

`||p_Q||_infinity <= (15/4)6^(2/5) Delta^(-2/5)d^(-1/5)`.

That theorem used only `p=4`, because `p=4` is the first exponent at which the arbitrary rotated center marginal can be controlled without a dimension/spread loss. The present run observes that **every p>=4 is also source-valid**. Optimizing `p` converts the power blow-up as `d->0` into a logarithm.

A complementary source arrived during this run: fleet01/B01 proved the exact endpoint `d=0` with nonzero transverse linear coupling `g`, giving a continuous density `<5.990 Delta^(-3/8)g^(-1/4)`. Its correction changes only a stale checker constant, not the theorem. The present result is different: it treats every `d>0`, including arbitrarily small `d`, with no assumption on `g`.

The designated partner result actually applied below is fleet04/B01's exact signed-Fejer interface, source

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

## 2. Setup

Choose three ORIGINAL coordinates `I`, a disjoint ORIGINAL-coordinate bank `J`, and condition every remaining original coordinate `W`. For each conditioned value `w`, write

`Q_w = X_I^T B X_I + 2 X_I^T K X_J + L_w^T X_I + G_w(X_J)`,       (2.1)

where `B=B^T` is `3x3`, `K` is `3 x |J|`, `L_w` is arbitrary, and `G_w` is arbitrary. Assume

`rank K=2`.                                                         (2.2)

Let `v` be a unit generator of `ker(K^T)` and put

`Delta = sigma_1(K)sigma_2(K)=sqrt(e_2(KK^T))>0`,                  (2.3)
`d = |v^T Bv|>0`.                                                   (2.4)

No condition is placed on the two same-bank quadratic blocks, affine leakage, signs, support, moments, or the rest of the spectrum.

Rotate only the three-dimensional center so that `v` is the third coordinate. Write the rotated center as `(u,z) in R^2 x R`. Its joint density `rho(u,z)` need not factor, but orthogonal change of variables preserves

`0<=rho<=1`, `int rho=1`.                                          (2.5)

The cross matrix becomes `[[M],[0]]`, where `M` has the same two nonzero singular values as `K`. Define the two-dimensional marginal

`m(u)=int rho(u,z)dz`.                                              (2.6)

Because `m` is an orthogonal two-dimensional projection of three independent cap-one original coordinates, the source-valid product-marginal theorem gives

`||m||_infinity<=2`.                                                (2.7)

This cap is not used at `p=4`; it is exactly what pays the higher-`p` extension.

## 3. Mass-sensitive translated Fresnel L^p input

The previous B01 theorem `QFORM-TRANSLATED-FRESNEL-LP-v1` proves that for every `p>2`, every cap-one probability density, every `a!=0`, and every linear translation,

`|| E exp(it(aZ^2+bZ+c)) ||_(L^p(dt)) <= C_p |a|^(-1/p)`,          (3.1)

where

`C_p=[4*pi*(p-1)]^(1/p) * ((p-1)/(p-2))^((p-1)/p)`.                (3.2)

By normalization and one-dimensional scaling, if `0<=q<=1` has mass `0<=m<=1`, then

`|| int q(z)e^{it(az^2+bz+c)}dz ||_p
 <= C_p m^(1-2/p)|a|^(-1/p)`.                                     (3.3)

Indeed, for `m>0`, `q/m` has cap `1/m`; scaling a probability density of cap `M` to cap one changes the quadratic coefficient by `M^(-2)`, giving an `M^(2/p)` cost. Multiplication back by `m` yields the exponent `1-2/p`.

## 4. Orientation-safe mixed-norm extension for every p>=4

For fixed `w`, let

`h_(t,w)(u)=int rho(u,z) exp(it Phi_w(u,z)) dz`,                    (4.1)

where `Phi_w` contains the entire center quadratic/affine phase. Along each fixed `u`, its `z`-quadratic coefficient has modulus exactly `d`; every other coefficient is an arbitrary translation and is harmless in (3.3). Put

`A_w(t)=||h_(t,w)||_(L^2(du))`.                                    (4.2)

For every `p>=4`, Minkowski (`p>=2`) and (3.3) give

`||A_w||_p^2
 <= int ||h_(.,w)(u)||_p^2 du
 <= C_p^2 d^(-2/p) int m(u)^(2-4/p)du`.                            (4.3)

Set `r=2-4/p`. Since `p>=4`, `r>=1`. Using (2.7) and `int m=1`,

`int m^r <= ||m||_infinity^(r-1) int m
          <= 2^(1-4/p)`.                                           (4.4)

Therefore

`boxed:
 ||A_w||_p <= C_p 2^(1/2-2/p)d^(-1/p),   p>=4.                    (4.5)
`

The same bound holds after averaging over `W`, by Minkowski. At `p=4`, (4.4) is exactly `int m=1`, so (4.5) recovers the preceding orientation-safe `L^4` argument. For `p<4`, the exponent in (4.3) is `<1`, and no dimension/spread-free control follows from probability mass plus a density cap; this is the precise reason the arbitrary-orientation family starts at `p=4`.

## 5. Full L^p density theorem

The rank-two random-gradient Plancherel step of the predecessor theorem is unchanged. For `t!=0`, after averaging over the original-product `J` bank,

`|phi_Q(t)|
 <= sqrt(2)*pi*Delta^(-1/2)|t|^(-1) A(t)`,                         (5.1)

where `||A||_p` obeys (4.5).

Let `p>=4` and let `p'=p/(p-1)`. For every `T>0`, use `|phi_Q|<=1` at low frequency and Holder at high frequency:

`int_R |phi_Q(t)|dt
 <=2T + sqrt(2)pi Delta^(-1/2)||A||_p
          [int_(|t|>T)|t|^(-p')dt]^((p-1)/p).`                     (5.2)

Since

`int_(|t|>T)|t|^(-p')dt
 =2(p-1)T^(-1/(p-1))`,                                             (5.3)

(4.5) yields

`int |phi_Q|
 <=2T + B_p Delta^(-1/2)d^(-1/p)T^(-1/p)`,                        (5.4)

where

`B_p
 =sqrt(2)pi C_p 2^(1/2-2/p)[2(p-1)]^((p-1)/p)
 =2pi 2^(-2/p) C_p [2(p-1)]^((p-1)/p).`                            (5.5)

The exact minimizer of `2T+C T^(-1/p)` is

`T=(C/(2p))^(p/(p+1))`,                                            (5.6)

and the minimum equals `2(p+1)T`. Fourier inversion therefore proves:

### Theorem 5.1 — `QFORM-RANK2-CROSS-TRANSVERSE-LP-v2`

For every `p>=4`, the full ambient quadratic form (2.1) has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= K_p Delta^(-p/[2(p+1)]) d^(-1/(p+1)),                          (5.7)
`

with

`K_p=(p+1)/pi * [B_p/(2p)]^(p/(p+1)).`                             (5.8)

The scaling is exact: under `A -> lambda A`, `Delta -> lambda^2 Delta` and `d->|lambda|d`, so the right side scales as `|lambda|^(-1)`.

At `p=4`,

`K_4=(15/4)6^(2/5)=7.6787719165...`,                               (5.9)

so Theorem 5.1 exactly recovers the predecessor theorem rather than contradicting or weakening it.

It is useful to rewrite (5.7) as

`||p_Q||_infinity
 <= K_p Delta^(-1/2) (sqrt(Delta)/d)^(1/(p+1)).`                   (5.10)

This form exposes the near-null optimization.

## 6. Logarithmic near-null receiver

Define the dimensionless ratio

`R=sqrt(Delta)/d`, `L=log_+ R`.                                    (6.1)

Choose

`p=4+L >=4`.                                                       (6.2)

If `R<=1`, then `R^(1/(p+1))<=1`. If `R>1`, then

`R^(1/(p+1))=exp[L/(5+L)]<=e`.                                    (6.3)

We now bound `K_p` explicitly. Substituting (3.2) into (5.5) gives the exact simplification

`B_p/(2p)
 =2pi ((p-1)/p)(pi/2)^(1/p)
   ((p-1)/(p-2))^((p-1)/p).`                                      (6.4)

For `p>=4`,

`(p-1)/p<=1`,
`(pi/2)^(1/p)<9/8`,
`((p-1)/(p-2))^((p-1)/p)<=3/2`.                                   (6.5)

Hence

`B_p/(2p) <=27pi/8`.                                               (6.6)

Because `27pi/8>1`,

`K_p
 <=(p+1)/pi * (27pi/8)
 =27(p+1)/8
 <=135p/32`.                                                       (6.7)

Combining (5.10), (6.2), (6.3), and (6.7) gives the main compact replacement:

### Corollary 6.1 — `QFORM-RANK2-CROSS-TRANSVERSE-LOG-v1`

Under (2.1)-(2.4),

`boxed:
 ||p_Q||_infinity
 <= (135e/32) Delta^(-1/2)
    [4+log_+(sqrt(Delta)/d)].                                      (6.8)
`

Numerically `135e/32=11.4677514638...`.

Thus the preceding power loss `d^(-1/5)` is replaced by a **logarithmic** loss as the transverse curvature approaches zero. The density is continuous because the proof establishes `phi_Q in L^1` for every fixed `d>0`.

This is materially better for structural routing: a very small nonzero transverse Rayleigh curvature no longer incurs a fractional negative power. It does not close the exact `d=0` endpoint; the just-completed fleet01/B01 theorem pays `d=0,g>0`, while `d=g=0` remains a separate structural state unless another product-preserving packet is present.

## 7. The logarithm is not an artifact of this proof

A rank-two curved bicore can genuinely develop logarithmic density growth when a small transverse square regularizes its endpoint singularity. This is not a QFORM counterexample (it has only two large eigenvalues when the regularizer is small); it shows why no analytic receiver at this exact local scope should be expected to remain uniformly bounded as `d->0`.

Let five independent variables

`x1,x2,y1,y2,z ~ Uniform[-1/2,1/2]`

and set, for `0<epsilon<=1/2`,

`Q_epsilon=(x1+y1)^2-(x2-y2)^2+epsilon z^2`.                       (7.1)

The first two square variables have common density

`h(w)=w^(-1/2)-1`, `0<w<1`.                                       (7.2)

Let `R=(x1+y1)^2-(x2-y2)^2`. For `0<s<=1/8`,

`p_R(-s)=int_0^(1-s)h(u)h(u+s)du`.                                (7.3)

Restrict the integral to `u in [s,1/8]`. Then `u+s<=1/4`, so

`h(u)>=1/(2sqrt(u))`,
`h(u+s)>=1/(2sqrt(u+s))>=1/(2sqrt(2u))`.                           (7.4)

Therefore

`p_R(-s)>=1/(4sqrt(2)) log(1/(8s)).`                               (7.5)

Since `epsilon z^2<=epsilon/4<=1/8`, averaging (7.5) over `z` gives

`p_(Q_epsilon)(0)
 >=1/(4sqrt(2)) int_(-1/2)^(1/2)
       log(1/(8epsilon z^2)) dz
 =1/(4sqrt(2)) [log(1/(2epsilon))+2].`                             (7.6)

Hence

`boxed:
 p_(Q_epsilon)(0) >= (1/(4sqrt(2)))log(1/epsilon)+O(1).             (7.7)
`

The coefficient matrix of (7.1) has nonzero eigenvalues `{2,-2,epsilon}`. Therefore (7.7) does **not** refute the three-large-eigenvalue conjecture. It does prove that the logarithm in a rank-two-cross / vanishing-transverse-curvature receiver reflects a real local singularity, rather than only loose Holder algebra. In a full-target proof the third large direction must be spent elsewhere if `d` is too small.

## 8. Designated partner fleet04/B01 applied to the new inequality

For a probability law `mu`, fleet04/B01 proves the exact signed-Fejer identity

`||p_mu||_infinity = sup_(T>0,y in R) D_T mu(y)`,                  (8.1)

where

`D_T mu(y)=(1/(2pi)) int_(-T)^T (1-|t|/T)
             Re(e^(-ity) muhat(t))dt`,                             (8.2)

with both sides `+infinity` if no bounded density exists.

Applying (8.1) to Corollary 6.1 gives the actual averaged-frequency inequality

`boxed:
 sup_(T>0,y) D_T law(Q)(y)
 <=(135e/32) Delta^(-1/2)
   [4+log_+(sqrt(Delta)/d)].                                       (8.3)
`

This is precisely an averaged-in-frequency replacement for the false pointwise scalar Fresnel bound. The phase-aligned fragmented-support counterexample remains intact; the gain comes from a two-dimensional original-product random gradient plus an integrated transverse Fresnel family.

## 9. What remains

The full conjecture is still OPEN. This result changes the local analytic economics but not the global structural obligation.

The current clean rank-two packet ledger is now:

* `d>0`: the new logarithmic receiver (6.8), continuous density;
* `d=0` and `g=||(I-vv^T)Bv||>0`: fleet01/B01's linear-slice receiver `<5.990 Delta^(-3/8)g^(-1/4)`, continuous density;
* `d=g=0`: `Bv=0`; the cross-kernel direction is also null for the center self-curvature and must be connected to a third product-preserving packet, or routed to an existing grouped-square/hub/null-coloop/diffuse/ridge mechanism.

Fleet02/B01 r37 shows that the bare three-large-eigenvalue hypothesis cannot force one packet with `Delta^2 d` bounded below. Consequently the next B01 structural interface should use (6.8) as a **soft logarithmic receiver inside a routing theorem**, rather than demand a uniformly positive single-packet determinant currency.

No continuity claim is made for the unrestricted conjecture; continuity is proved only for the branch in Theorem 5.1 / Corollary 6.1.

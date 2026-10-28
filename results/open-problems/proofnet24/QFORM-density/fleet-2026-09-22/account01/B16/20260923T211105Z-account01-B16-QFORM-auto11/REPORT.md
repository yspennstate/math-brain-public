# account01/B16 — translated fresh-square stability through a shared observed projection

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T21:11:05.787967Z.
attacking: projection-product interaction at the punctured fresh-hub endpoint; retain one genuine fresh innovation inside a square even when the observed square coordinate shares arbitrary light-source dependence, and compare with the designated account02/B16 zero-pivot receiver.

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T211105Z-account01-B16-QFORM-auto11`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM + STRICT TARGET FAMILY + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** absolute continuity and an essential density bound are proved on the new scope. Continuity for this scope is not proved here; the unrestricted continuity problem remains separate/open.

## 1. Fresh control and source discipline


The two mathematical sources actually used are source-pinned:

1. **Designated partner account02/B16 r36**, `yspennstate/math-open-problems@be8062b160868bcc71aff45a77c56ff2d0501a9a`, report blob `57cf025ef533e6cfad52761553dfc9013d486ec0`. Its theorem `QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1` proves
   
   `||p_Q||_infinity <= 3*2^(2/3) M^(2/3)|gamma^2 kappa|^(-1/3)`
   
   for `Q=2 gamma H L+2LT+alpha L^2+2delta LV+kappa V^2`, where `H` is one untouched independent cap-one physical source and `(L,V)` has joint density cap `M`. The arbitrary twist `T` may depend on the same light sources as `(L,V)`.

2. **Sign-free dependent-pair/fresh-square transducer**, account03/B16 r27, `yspennstate/math-open-problems@4388eeb12a94dd167f305554419fd4c986eda04a`, report blob `d49257cf13a631b4ed9c4e15eeb1b21810678c3e`. It proves the root-collar/Schur estimate when the square coordinate itself is an independent source.

The live corrections are preserved: no independence is inferred after an orthogonal projection; a bounded joint projection density is not inserted directly into an arbitrary indefinite coarea integral; no normalized conditional projection-height cap is used; and no small coefficient multiplying an unbounded source is dropped.

## 2. Main theorem — a fresh innovation survives an arbitrary shared shift inside the square

### Theorem `QFORM-TRANSLATED-FRESH-SQUARE-SIGNFREE-v1`

Let `X`, `Z`, and an arbitrary random object `W` be mutually independent. Assume

`||p_X||_infinity <= L_X`, `||p_Z||_infinity <= L_Z`.

Let `H=H(W)` and `U=U(W)` be arbitrary real measurable functions, with no independence between them, and assume only

`||p_U||_infinity <= L_U`.

Let `G=G(X,W)` be an **arbitrary measurable function**; in particular it may use the same light source vector as `H,U` and it may also depend on the fresh source `X`. Fix nonzero scalars `gamma,sigma` and define

`Y = gamma X + H`,
`V = sigma Z + G(X,W)`.                                           (2.1)

Let

`B=[[a,k,m],[k,l,n],[m,n,b]]`                                   (2.2)

be a real symmetric invertible `3 x 3` matrix with `b!=0`. Deterministic affine terms in `(Y,U,V)` are allowed. Then

`Q=(Y,U,V)^T B (Y,U,V)+r_1Y+r_2U+r_3V+r_0`                       (2.3)

is absolutely continuous and

`boxed:
 ||p_Q||_infinity
 <= 2^(13/4) (L_Z/|sigma|)
    sqrt(L_X L_U/|gamma|)
    (|b det B|)^(-1/4).
`                                                                  (2.4)

Thus the observed square variable `V` need **not** be independent of `(Y,U)`. Only one genuine original-source innovation `sigma Z` inside `V` is required. The shift `G` can be arbitrarily dependent on every other displayed source except `Z`.

### Proof

Multiply `Q` by `-1` if needed, so assume `b>0`. Put

`C=(Y,U)^T`, `r=(m,n)^T`.

The exact algebraic completion is

`C^T [[a,k],[k,l]] C + 2 V r^T C + bV^2 + r_3V
 = b [V + (r^T C+r_3/2)/b]^2
   + C^T ( [[a,k],[k,l]] - rr^T/b ) C
   - (r_3/b) r^T C - r_3^2/(4b).`                                (2.5)

Now condition on `(X,W)`. Then `Y,U,G` are fixed and

`V = sigma Z + G`

is a translate of the genuinely independent original source `sigma Z`; hence its conditional density is bounded by

`K_V=L_Z/|sigma|`.                                                (2.6)

For a cap-`K_V` scalar `R` and any deterministic shift `h`, the positive square pushforward obeys

`p_{b(R+h)^2}(s) <= K_V b^(-1/2) s^(-1/2) 1_{s>0}`.             (2.7)

Applying (2.7) to (2.5), then averaging `(X,W)`, gives exactly

`p_Q(t)
 <= K_V b^(-1/2) E [t-F(Y,U)]_+^(-1/2),`                        (2.8)

where the Schur residual

`F(y,u)=delta y^2+2 kappa yu+lambda u^2+p y+q u+c`               (2.9)

has the deterministic coefficients

`delta=a-m^2/b`, `kappa=k-mn/b`, `lambda=l-n^2/b`,               (2.10)

with the corresponding affine constants. **The arbitrary shared shift `G` has disappeared identically before the singular curved integral is estimated.** This is the key source-provenance step.

Conditional on `W`, the variable `Y=gamma X+H(W)` is a translate of `gamma X`, so

`||p_(Y|W)||_infinity <= L_X/|gamma|`.                            (2.11)

The remainder of the integral (2.8) is precisely the sign-free root-collar calculation of the pinned account03/B16 theorem. For completeness, define

`s(u)=kappa u+p/2`, `r(u)=lambda u^2+qu+c`,
`D_t(u)=delta(t-r(u))+s(u)^2`.                                   (2.12)

If `delta!=0`, the exact identity is

`t-F(y,u)=D_t(u)/delta-delta(y+s(u)/delta)^2.                    (2.13)

The quadratic coefficient of `D_t(u)` is

`theta=kappa^2-delta lambda`,                                   (2.14)

and the Schur determinant identity gives

`det B=b(delta lambda-kappa^2)=-b theta`,
`|theta|=|det B|/b`.                                             (2.15)

The one-dimensional root-collar estimate, uniform in the translating value of `H`, gives

`E([t-F(Y,u)]_+^(-1/2) | W,U=u)
 <= 2 sqrt(2 L_X/|gamma|) |D_t(u)|^(-1/4).`                     (2.16)

For the opposite sign this includes the logarithmic collar before averaging; no fiber supremum is taken. Since `p_U<=L_U`, the absolute quadratic-band estimate yields

`E |D_t(U)|^(-1/4)
 <= 2^(7/4) sqrt(L_U) |theta|^(-1/4).`                           (2.17)

Equations (2.8), (2.16), (2.17), and (2.15) give

`p_Q(t)
 <= K_V b^(-1/2)
    2 sqrt(2L_X/|gamma|)
    2^(7/4) sqrt(L_U)(|det B|/b)^(-1/4)`

`=2^(13/4) K_V sqrt(L_XL_U/|gamma|)
  (b|det B|)^(-1/4).`                                            (2.18)

Insert `K_V=L_Z/|sigma|` from (2.6). The `delta=0` branch is the affine-in-`y` endpoint of the same pinned root-collar proof and has no larger constant. Restoring `|b|` proves (2.4). The conditional square pushforward and Tonelli argument also prove absolute continuity. QED.

### What is genuinely new here

The account03/B16 theorem required the **whole observed variable** `V` to be source-independent of `(H,U)`. The theorem above replaces that by the strictly weaker triangular provenance

`V = sigma Z + G(X,W)`,                                           (2.19)

where only the innovation `Z` is fresh. The shift may share every light source appearing in `H,U`. This matters in the current near-coloop programme because an aggregate observed spectral coordinate may be highly shared while still containing one untouched source-bank innovation.

The proof works because the shift is erased *algebraically* by Schur completion before the half-power kernel is paid. It does not try to bound a conditional density of the shared part.

## 3. Actual product-projection insertion

Let one common leaf source bank consist of arbitrary independent cap-one coordinates, and let

`L=<ell,X_leaf>`, `U=<u,X_leaf>`, `P=<p,X_leaf>`                  (3.1)

where `ell,u,p` are orthonormal coefficient vectors. No independence is claimed among `(L,U,P)`.

The actual one-dimensional bounded-density projection theorem gives

`||p_U||_infinity <= sqrt(2).`                                   (3.2)

Let `X_0,Z_0` be two additional independent original coordinates, independent of the leaf bank, and put for arbitrary real `eta,epsilon`

`Y=X_0+eta L`,
`V=Z_0+epsilon P`.                                               (3.3)

Apply Theorem (2.4) with

`L_X=L_Z=1`, `gamma=sigma=1`, `L_U<=sqrt(2)`.                    (3.4)

For the coefficient matrix

`B_a=4[[a,1,0],[1,0,0],[0,0,1]]`,                               (3.5)

one has the exact identities

`det B_a=-64`, `b=4`, `|b det B_a|=256`,                         (3.6)

independent of `a`. Therefore the quadratic form

`Q_(a,eta,epsilon)
 =4[aY^2+2YU+V^2]`                                               (3.7)

satisfies

`boxed:
 ||p_(Q_(a,eta,epsilon))||_infinity <= 2 sqrt(2)
`                                                                  (3.8)

for **every real** `a,eta,epsilon` and every choice of the cap-one product input laws.

This is a nonlinear projection-product application: the two observed spectral variables `Y,V` both share the same leaf source bank through `L,P`, but the two untouched physical innovations `X_0,Z_0` survive their shifts. The dependence is kept rather than discarded.

## 4. Strict all-`a` target-valid family

The base family (3.7) already has a uniform density bound for every `a`, but for very large `|a|` one of its two hyperbolic eigenvalues can drop below one. Add one additional independent cap-one original coordinate `R` and define

`Q_tilde_(a,eta,epsilon)
 =Q_(a,eta,epsilon)+4R^2`.                                      (4.1)

Since `4R^2` is independent of the base form, convolution cannot increase the essential density height, so

`boxed:
 ||p_(Q_tilde_(a,eta,epsilon))||_infinity <=2 sqrt(2)
`                                                                  (4.2)

for all real parameters.

This is genuinely inside the owner's spectral target for **every** `a,eta,epsilon`. Indeed the coefficient vectors of `Y,U,V,R` are pairwise orthogonal, with

`||Y||=s=sqrt(1+eta^2)`, `||U||=1`,
`||V||=t=sqrt(1+epsilon^2)`, `||R||=1`.                           (4.3)

In their normalized carrier basis the physical matrix is

`4[[a s^2,s,0,0],
   [s,0,0,0],
   [0,0,t^2,0],
   [0,0,0,1]].`                                                  (4.4)

The last two eigenvalues are `4t^2>=4` and `4`. The `2 x 2` block has determinant `-16s^2`, so its two eigenvalues have opposite signs, and the larger absolute value is at least `4s>=4`. Therefore (4.4) has at least **three** eigenvalues of modulus at least `4`, uniformly in every parameter. No post-rotation independence is used in this spectral check.

Thus (4.1) is an arbitrary-parameter, arbitrary-law target family in which two observed quadratic coordinates share a common product bank, yet the density is bounded by `2sqrt(2)`.

## 5. Newest designated partner account02/B16 applied to the same family at the exact zero pivot

Now set `a=0` in (3.7):

`Q_(0,eta,epsilon)
 =8X_0U+8eta LU+4(Z_0+epsilon P)^2`.                              (5.1)

This is a direct instance of the newest designated partner account02/B16 r36 theorem, not just a citation. Use its notation

`H=X_0`, `L_partner=U`,
`T=4 eta L`, `gamma=4`, `kappa=4`, `alpha=delta=0`,
`V_partner=Z_0+epsilon P`.                                      (5.2)

The light object contains the entire leaf bank and `Z_0`, and is independent of the untouched physical source `X_0`, exactly as required.

It remains to insert an actual product-projection inequality for the partner pair `(U,V_partner)`. The orthonormal two-dimensional projection `(U,P)` has a joint density, and because `f_(Z_0)<=1`,

`p_(U,V_partner)(u,v)
 = integral p_(U,P)(u,p) f_(Z_0)(v-epsilon p) dp
 <= integral p_(U,P)(u,p) dp
 =p_U(u)
 <=sqrt(2).`                                                     (5.3)

Hence the partner theorem has `M<=sqrt(2)`. Its bound becomes exactly

`||p_(Q_(0,eta,epsilon))||_infinity
 <=3*2^(2/3)(sqrt(2))^(2/3)|4^2*4|^(-1/3)`

`=3*2/4
=3/2.`                                                           (5.4)

Therefore

`boxed:
 ||p_(Q_(0,eta,epsilon))||_infinity <=3/2.
`                                                                  (5.5)

Adding the independent `4R^2` block in (4.1) preserves the same `3/2` bound at `a=0`.

This is the requested completed-partner-to-actual-inequality application. It also cleanly separates the two mechanisms on one common family:

- the account02/B16 zero-pivot transducer gives the sharper `3/2` at `a=0`;
- the new translated-fresh-square theorem remains finite after adding the genuinely nonzero fresh-hub square and gives `2sqrt(2)` uniformly for all `a`.

## 6. Relation to the true near-coloop debt

This theorem does **not** close `QFORM-PUNCTURED-FRESH-HUB-SQUARE-OVERLAP-STABILITY-v2` for an arbitrary near-coloop survivor. It closes the following real subbranch:

`QFORM-PUNCTURED-HUB-WITH-ONE-TRANSVERSE-FRESH-INNOVATION-v1`.

Whenever, after source-preserving grouping, the observed transverse square coordinate has a decomposition

`V=sigma Z+G(X,W)`                                                (6.1)

with `Z` an untouched original-source innovation of quantitative `|sigma|`, the nonzero hub square is harmless: (2.4) is sign-free and does not deteriorate as the hub pivot tends to zero. The shared shift `G` can be arbitrarily large and arbitrarily dependent on the other light projections.

What remains in the full near-coloop endpoint is precisely the **innovation-free shared-square** case: every candidate transverse square coordinate may be generated entirely by the same light sources as the hub partner, so no quantitative `sigma` survives. The preceding two-bank identity already shows that the natural one-bank innovations can all vanish simultaneously at the exact coloop. The next analytic/compiler step must therefore either extract a fresh innovation by a new source grouping without paying its reciprocal, or build a genuinely shared-square receiver. A marginal cap or a conditional-cap surrogate is insufficient by the live caps-only counterexample.

## 7. Status and source pins

`QFORM-TRANSLATED-FRESH-SQUARE-SIGNFREE-v1`: **PROVED SUPPORTING THEOREM**.  
`QFORM-PUNCTURED-HUB-WITH-ONE-TRANSVERSE-FRESH-INNOVATION-v1`: **PAID** by (2.4).  
Family (4.1): **STRICT ALL-PARAMETER TARGET FAMILY**, `||p||_infinity<=2sqrt(2)`.  
Its zero-pivot member: **designated partner account02/B16 gives `<=3/2`**.  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Global continuity: **OPEN / separate**.

Pinned account02/B16 source: `be8062b160868bcc71aff45a77c56ff2d0501a9a`, report blob `57cf025ef533e6cfad52761553dfc9013d486ec0`.  
Pinned sign-free square source: `4388eeb12a94dd167f305554419fd4c986eda04a`, report blob `d49257cf13a631b4ed9c4e15eeb1b21810678c3e`.

No schedule, enabled/quiet state, notification, email, task, permission, public-release, paid/remote-call, identity, or cross-account-authentication setting is changed in this run.

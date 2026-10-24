SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-23T12:30:56Z.
attacking: true near-coloop shared-bank geometry by quantifying the intrinsic capped-Pluecker loss, then bypassing it with a source-plane/source-line aggregation that keeps a dependent two-dimensional product projection intact through the curved receiver.

# account02/B16 — near-coloop KL barrier and source-plane/source-line compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREMS / FULL QFORM OPEN`  
**Regularity:** the new global family bound proves absolute continuity and essential boundedness via the partner transducer; continuity is not claimed. The pinned ruled theorem supplies its own one-sided density conclusion.  

## 1. Exact target and first unpaid implication

The target remains unchanged: for arbitrary finite `n`, independent real original-coordinate variables with densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No support, moment, log-concavity, identical-law, diagonal-basis, or post-rotation-independence hypothesis is introduced below.

The latest designated-partner reduction account03/B16 r28 leaves the genuine exact-rank-three near-coloop collar `c>63/64` as its structural endpoint. Its capped-basis route already notes that avoiding the hub is rare. The first result below makes that loss exact: **no choice of capped Pluecker basis law can keep its determinant-entropy certificate uniform as the coloop defect `a=1-c` tends to zero**. Thus the next compiler has to use the genuine source scalar before paying that rarity, or aggregate source directions before curvature.

The second result supplies one such compiler for a nontrivial structured shared-bank class: one original-coordinate source plane may carry an arbitrarily dependent pair `(H,U)`, while a disjoint source line supplies the fresh scalar. The proof uses account03/B16 r27 exactly at its intended dependence-preserving interface.

## 2. Theorem: exact KL barrier for capped Pluecker/Fresnel certificates

Let `R` be an `n x 3` matrix with `R^T R=I_3`, and suppose one physical row is

`r_0=sqrt(c)e`, `||e||=1`, `0<c<1`, `a=1-c`.

For every physical triple `S`, set

`v_S=det(R_S)^2`.

By Cauchy--Binet,

`sum_S v_S=1`,

so `v` is a probability law on physical bases (zero determinants simply have zero mass). Let

`E={S:0 notin S}`.

Deleting the hub row leaves Gram matrix

`R_{-0}^T R_{-0}=I_3-c ee^T`,

therefore another Cauchy--Binet application and the matrix determinant lemma give the exact rare-event mass

`v(E)=det(I_3-c ee^T)=1-c=a`.                                  (2.1)

Now let `w` be **any** probability law supported on nonsingular physical triples. The determinant-entropy score in the completed capped-basis Fresnel theorem used by account03/B16 r28 is

`Z_w=exp(H(w)+sum_S w_S log det(R_S)^2)`.

Since `v_S=det(R_S)^2` and `sum v_S=1`,

`log Z_w=sum_S w_S log(v_S/w_S)=-D(w||v)`.                     (2.2)

Assume the hub marginal is capped as required by that theorem:

`alpha_0=w(0 in S)<=1/2`.

Then `q:=w(E)>=1/2`. Data processing of relative entropy to the binary event `E` gives

`D(w||v)>=d(q||a)`.                                             (2.3)

For `a<1/2`, the binary divergence `d(q||a)` is increasing on `q>=1/2`; hence

`d(q||a)>=d(1/2||a)
          =-log(2 sqrt(a(1-a)))`.

Together with (2.2),

`boxed: Z_w <= 2 sqrt(ac).`                                    (2.4)

### Consequence — `QFORM-NEAR-COLOOP-CAPPED-BASIS-KL-BARRIER-v1`

For a target family with `|det Lambda|=1`, the capped-basis theorem has right-hand side

`3e Z_w^(-1/3)`.

Equation (2.4) implies that even the *best certificate obtainable from that theorem* is no smaller than

`3e [2 sqrt(ac)]^(-1/3)`,                                      (2.5)

which diverges like `a^(-1/6)` as `a->0`.

This is **not** a lower bound on the true density and is not a QFORM counterexample. It is an exact obstruction to closing the true near-coloop collar solely by optimizing the capped Pluecker basis law. It quantitatively sharpens the partner-r28 statement that such laws must pay the rarity of bases avoiding the hub.

## 3. Theorem: source-plane/source-line aggregation compiler

This theorem keeps product provenance at the original-coordinate level and allows genuine dependence after a two-dimensional projection.

Assume an exact-rank-three representation

`A=R Lambda R^T`, `R^T R=I_3`,

and choose a physical hub coordinate `0` with

`r_0=gamma e`, `gamma!=0`, `||e||=1`.

Let `C` and `D` be disjoint sets of original coordinates, also disjoint from `{0}`. Suppose the spectral rows on `C` lie in a fixed source plane through the hub direction:

`r_i=alpha_i e+beta_i u`, `i in C`,                       (3.1)

for a fixed spectral vector `u`, while the rows on `D` are collinear:

`r_j=delta_j v`, `j in D`,                                (3.2)

for a fixed spectral vector `v`. Put

`s=(sum_{i in C} beta_i^2)^(1/2)>0`,
`t=(sum_{j in D} delta_j^2)^(1/2)>0`,

`H=sum_{i in C} alpha_i X_i`,
`U=s^(-1) sum_{i in C} beta_i X_i`,
`V=t^(-1) sum_{j in D} delta_j X_j`,

and spectral aggregate vectors

`g=s u`, `h=t v`.

Then the source objects

`X_0`, `(H,U)`, `V`

are mutually independent because they use disjoint original-coordinate sets, while **no independence at all is asserted between `H` and `U`**. The one-dimensional bounded-density projection theorem gives

`||p_U||_infinity, ||p_V||_infinity <=sqrt(2)`.                (3.3)

If the two coefficient vectors inside `C` are linearly independent, the ordinary two-dimensional product-projection theorem also gives a finite joint density bound for `(H,U)` after the obvious Gram normalization; this joint cap is recorded provenance, not an independence substitute and is not needed by the transducer below.

Condition on every original coordinate outside `{0} union C union D`. The remaining spectral vector equals

`e(gamma X_0+H)+g U+h V + constant`.

Set

`Y=gamma X_0+H`,
`P=[e,g,h]`,
`B=P^T Lambda P`,
`b=h^T Lambda h`.

All conditioned outside terms are merely affine in `(Y,U,V)`. If

`det P !=0`, `b!=0`,                                             (3.4)

then account03/B16 r27's completed theorem `QFORM-DEPENDENT-PAIR-FRESH-SQUARE-SIGNFREE-v1` applies with `L_X=1`, `L_U,L_V<=sqrt(2)`. It gives

`||p_Q||_infinity
 <=2^(13/4) sqrt(2) sqrt(sqrt(2)/|gamma|)
   (|b det B|)^(-1/4)`

and hence, using `det B=det Lambda det(P)^2`,

`boxed:
 ||p_Q||_infinity
 <=16 |gamma|^(-1/2)
    [ |b det Lambda| det(P)^2 ]^(-1/4).`                        (3.5)

The conclusion is absolute continuity plus essential boundedness; continuity is not supplied by the partner theorem.

### Why (3.5) is a projection-product statement rather than a rotated-independence statement

The pair `(H,U)` is produced by one original product bank and may be strongly dependent. The proof never conditions on `H` and asks for a conditional density of `U`, never uses a worst fibre, and never rotates `(H,U)` into independent coordinates. The only independence is the genuine source separation

`X_0  independent of  (H,U)  independent of  V`.

Thus (3.5) is a product-preserving compiler for a two-dimensional projected source plane through a genuinely curved three-variable receiver.

## 4. Fully shared Walsh family in the true near-coloop collar

We now apply (3.5) to a family in which **every residual physical coordinate mixes all three spectral directions**, so there is no support-separated pure transverse coordinate.

Let

`0<a<1/64`, `c=1-a`,

and let `m>=132` be divisible by four. Choose signs

`(epsilon_j,tau_j) in {+1,-1}^2`

with all four sign pairs occurring exactly `m/4` times. Define spectral rows

`r_0=(sqrt(c),0,0)`,
`r_j=m^(-1/2)(sqrt(a),epsilon_j,tau_j)`, `1<=j<=m`.              (4.1)

Balanced signs give

`sum_j epsilon_j=sum_j tau_j=sum_j epsilon_j tau_j=0`,

so

`R^T R=diag(c+a,1,1)=I_3`.                                     (4.2)

Every residual transverse leverage is

`h_j=(epsilon_j^2+tau_j^2)/m=2/m<1/64`,                         (4.3)

and `c>63/64`, exactly the true near-coloop scale isolated by partner r28.

Take

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`.                            (4.4)

Its eigenvalues are `{1,-1,1}`. Therefore

`A=R Lambda R^T`

has nonzero spectrum exactly `{1,-1,1}` and is a strict instance of the three-large-eigenvalue target.

Define the three projections of the **same residual product bank**

`L=m^(-1/2) sum_j X_j`,
`U=m^(-1/2) sum_j epsilon_j X_j`,
`T=m^(-1/2) sum_j tau_j X_j`.                                  (4.5)

Then

`boxed: Q=2(sqrt(c)X_0+sqrt(a)L)U+T^2.`                         (4.6)

The coefficient vectors of `(U,T)` are orthonormal, so the completed two-dimensional product-marginal theorem used in the pinned Claude report gives

`||p_(U,T)||_infinity <=2`.                                     (4.7)

Equation (4.7) does **not** say `U` and `T` are independent; generally they are not.

### 4.1 Pinned source results at their exact scopes

The pinned `e5f71d79...` Fresnel theorem F can be applied to the residual coordinates `I={1,...,m}`. Their Gram matrix is

`G_I=diag(a,1,1)`,

and every normalized residual leverage is exactly

`r_j^T G_I^(-1) r_j=3/m<=1/2`.

Thus theorem F gives the valid global but nonuniform estimate

`boxed: ||p_Q||_infinity <=12 a^(-1/3).`                        (4.8)

This is a real inequality and exposes the near-coloop loss of a direct residual Fresnel payment.

Independently, the pinned ruled one-sheet theorem C applies because the exact signature is `(+,+,-)` with unit spectral magnitudes. It gives on the majority-sign side

`boxed: p_Q(s)<=pi sqrt(2) for a.e. s>=0.`                      (4.9)

Its proof uses bounded two-dimensional marginals of the original product law along the rulings; it never infers independence of rotated spectral coordinates. Thus (4.9) is precisely the valid curved use of the two-dimensional projection theorem in this family.

Neither (4.8) nor (4.9) alone gives the desired all-level, near-coloop-uniform bound. The next source grouping does.

## 5. Grouping mixed source directions beats both near-coloop losses

For each sign pair define the normalized original-coordinate bank sum

`Z_{sigma,tau}=(2/sqrt(m)) sum_{j:(epsilon_j,tau_j)=(sigma,tau)} X_j`.   (5.1)

The four variables `Z_{++},Z_{+-},Z_{-+},Z_{--}` are mutually independent source objects, and each has density cap at most `sqrt(2)` by the one-dimensional product-projection theorem.

The spectral contribution of the `++` and `--` banks together is

`(sqrt(a),1,1) Z_{++}/2 +(sqrt(a),-1,-1) Z_{--}/2`

`= e H+u W`,                                                     (5.2)

where

`e=(1,0,0)`,
`u=(0,1,1)/sqrt(2)`,

`H=(sqrt(a)/2)(Z_{++}+Z_{--})`,
`W=(Z_{++}-Z_{--})/sqrt(2)`.                                   (5.3)

The pair `(H,W)` is generally dependent. Its normalized version `(H/sqrt(a),W)` is a genuine two-dimensional projection of the `++ union --` product bank with a bounded joint density (the coefficient Gram is `diag(1/2,1)`), but no independence is used.

Use the `+-` bank as the source line:

`V=Z_{+-}`,
`g=(sqrt(a),1,-1)/2`.                                          (5.4)

Condition on the original coordinates in the remaining `-+` bank. Then

`X_0`, `(H,W)`, `V`

are mutually independent source objects and

`Y=sqrt(c)X_0+H`.                                               (5.5)

The spectral coefficient matrix for `(Y,W,V)` is

`P=[e,u,g]`,

with

`det P=-1/sqrt(2)`, `det(P)^2=1/2`.                             (5.6)

The corresponding curved receiver matrix is

`B=P^T Lambda P`

`=[[0,1/sqrt(2),1/2],
  [1/sqrt(2),1/2,(sqrt(a)-1)/(2sqrt(2))],
  [1/2,(sqrt(a)-1)/(2sqrt(2)),(1+2sqrt(a))/4]]`.                (5.7)

Hence

`det B=-1/2`,
`b=B_33=(1+2sqrt(a))/4>=1/4`,                                  (5.8)

uniformly all the way to the exact coloop limit `a downarrow0`.

Apply the source-plane/source-line compiler (3.5), equivalently partner r27 directly with

`gamma=sqrt(c)`, `L_X=1`, `L_W,L_V<=sqrt(2)`.

Since

`|b det B|=(1+2sqrt(a))/8`,

we obtain

`||p_Q||_infinity
 <=16 c^(-1/4) [8/(1+2sqrt(a))]^(1/4)`

`=2^(19/4)c^(-1/4)(1+2sqrt(a))^(-1/4)`

and therefore, because `c>63/64`,

`boxed:
 ||p_Q||_infinity
 <2^(19/4)(64/63)^(1/4)
 =27.0148360088... <27.015.`                                    (5.9)

This bound is uniform in `m`, in `a in (0,1/64)`, and in all independent cap-one input laws. It proves absolute continuity and a global essential bound for the family; no support or moment assumptions are used.

### 5.1 Why this is genuinely a shared-bank escape

Every residual physical row in (4.1) has nonzero scalar, first-transverse, and second-transverse components. There is no physical residual coordinate supported on a fresh spectral line or plane. The source separation appears only **after grouping whole original-coordinate sign classes**. Inside the `++ union --` plane bank, `(H,W)` remains dependent and is passed intact to the partner theorem.

Thus the valid principle is not "project and declare independence". It is:

**cluster original source directions -> aggregate within each disjoint source cluster -> retain dependence inside the projected plane -> pay the curved receiver.**

## 6. Quantitative obstruction to atom-by-atom payment

Take one physical `++` coordinate `j` and one physical `+-` coordinate `k`, together with the hub. Their spectral-column matrix is

`P_phys=[r_0,r_j,r_k]`,

so

`det(P_phys)^2=4c/m^2`.                                         (6.1)

For the third coordinate

`b_phys=A_kk=(1+2sqrt(a))/m`.                                   (6.2)

Hence

`|b_phys det(A_{\{0,j,k\}})|
 =4c(1+2sqrt(a))/m^3`.                                          (6.3)

Applying the same completely valid partner-r27 theorem **one physical triple at a time** yields only

`2^(11/4)m^(3/4)[c(1+2sqrt(a))]^(-1/4)`,                       (6.4)

which diverges as `m^(3/4)`. By contrast, whole-bank aggregation gives (5.9), below `27.015`.

Thus a uniform near-coloop compiler cannot insist that the fresh-square certificate be visible on one physical scalar atom. A whole mixed source-direction cluster can be the correct unit of payment.

## 7. The family lies arbitrarily deep in the physical no-pivot regime

The physical entries are explicit. First,

`A_00=0`,
`A_0j=sqrt(c) epsilon_j/sqrt(m)`.                               (7.1)

For residual coordinates,

`A_jk=[sqrt(a)(epsilon_j+epsilon_k)+tau_j tau_k]/m`,             (7.2)

so in particular

`|A_jj|=(|1+2epsilon_j sqrt(a)|)/m <=5/(4m)`.                   (7.3)

The hub-residual principal pair determinant is exactly

`det A_{\{0,j\}}=-c/m`,                                        (7.4)

while any residual-residual pair determinant has magnitude at most

`25/(8m^2)`.                                                     (7.5)

Therefore, for every prescribed no-pivot threshold `tau_*>0`, choosing `m` sufficiently large makes **every physical diagonal and every physical two-coordinate principal determinant smaller than `tau_*` in modulus**, while the nonzero spectrum remains exactly `{1,-1,1}` and the density bound (5.9) stays fixed.

So (5.9) is not an easy-pivot artifact; it penetrates the true near-coloop/no-pivot geometry.

## 8. Relation to the capped-basis barrier

For the same family, `|det Lambda|=1`. Section 2 says every basis law acceptable to the capped-basis Fresnel theorem must satisfy

`Z_w<=2sqrt(ac)`,

so that theorem's best possible right-hand side diverges at least like `a^(-1/6)` as `a->0`. The direct residual theorem F in (4.8) loses even faster, like `a^(-1/3)`. Yet the source-plane/source-line grouping remains below `27.015`.

This is the central mechanism change of the run: **near-coloop rarity is a certificate loss, not necessarily a density singularity.** Source aggregation can bypass the rarity before the curved pushforward is paid.

## 9. What remains

The full conjecture is still open. This run closes only a structured exact-rank-three shared-bank family and proves a general source-plane/source-line compiler plus an exact obstruction to the capped-basis route.

The first unpaid B16 implication is now

`QFORM-TRUE-NEAR-COLOOP-APPROXIMATE-DIRECTION-CLUSTER-v1`:

in a general partner-r28 residual frame with `c>63/64` and every residual transverse leverage `<1/64`, either extract two or three **disjoint original-coordinate direction clusters** whose aggregate spectral vectors satisfy a quantitative version of (3.4), or carry the non-collinear within-cluster remainder through a two-dimensional product marginal / mixed-Fresnel receiver without deleting it. Small spectral-row width cannot simply be discarded because the source variables are unbounded, and conditioning on one projected coordinate may destroy all useful density caps.

The exact interface exposed here is therefore:

1. a two-dimensional product marginal is safe as a joint object and can be used on curved ruled fibres;
2. it is not safe to infer independence or uniform conditional caps from it;
3. source-plane dependence can nevertheless be carried through the partner sign-free receiver when an independent source line is present;
4. the remaining task is a stable, approximate version of that source-direction clustering, plus the separate arbitrary-additional-spectrum interface.

No counterexample to QFORM was found. Global continuity remains separate and open.

## 10. Source pins used

1. Pinned Claude source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`. Theorem F is used in (4.8), the two-dimensional product-marginal input in (4.7), and the ruled theorem C in (4.9). A later compatible source update at `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926` leaves theorem F intact and adds finite-dimensional results; none invalidates the arguments above.
2. Designated partner account03/B16 r28: `yspennstate/math-open-problems@c0ba84ebcd6febf0c5a34dc6512e43ea79b957cf`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T105237Z-account03-B16-QFORM-r28/REPORT.md`. Its surviving endpoint is the true near-coloop collar and its determinant-entropy score motivates Section 2.
3. Completed partner transducer account03/B16 r27: `yspennstate/math-open-problems@4388eeb12a94dd167f305554419fd4c986eda04a`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T095010Z-account03-B16-QFORM-r27/REPORT.md`. The theorem is applied quantitatively in (3.5), (5.9), and (6.4).

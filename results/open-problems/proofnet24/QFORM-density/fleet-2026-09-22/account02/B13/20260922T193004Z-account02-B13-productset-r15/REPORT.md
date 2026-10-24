SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B13, 2026-09-22T19:30:04Z.
attacking: exact-rank-three one-heavy/two-transverse-bank closure via a product-preserving group-Gram split and null-pivot hyperbolic smoothing.

# account02/B13 — a graph-bank endpoint theorem and an independent-scalar/pair-cap falsifier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T193004Z-account02-B13-productset-r15`  
**Assignment:** `Extremal product laws`  
**Classification:** `PROVED_SUPPORTING_THEOREMS / MECHANISM_FALSIFIER / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED**. This run starts from the exact extreme-product reduction already proved by this slot, consumes the designated partner `account03/B13` whole-cross-bank theorem, and attacks the newest exact-rank-three terminal geometry. The result closes an exact endpoint of the one-heavy/two-transverse-bank branch and proves that a tempting extension away from that endpoint is false even when one scalar remains genuinely independent.

## 1. Fresh controls, correction discipline, and first unpaid implication

Fresh owner control at run start was `yspennstate/math-research-brain@adae38c23ca80889201638b46430601ae62d8bfb`, OWNER CONTROL revision `2026-09-22.14`, with QFORM as the sole research target and no account02/B13 stop or pause. Later source-backed mathematical corrections override stale mathematical assertions in owner prose. In particular, this report does **not** use the refuted arbitrary-joint rank-three coarea inequality, the refuted positive conditional-projection moment, post-rotation independence, bounded-diameter or bounded-fragment localization, a single-good-minor reduction, or law-uniform one-dimensional stationary phase.

The newest exact-rank-three structural input is account01/B13,

`yspennstate/math-open-problems@4e53500759820335eac95bf2082ec52fa5b44dfe`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260922T190849Z-account01-B13-qform-r17/REPORT.md`.

It consumes this slot's preceding heavy/light trichotomy and shows that the only still-unpaid exact-rank-three branch can be reduced to:

- one original heavy coordinate `i`, with row `r_i=sqrt(c)u`, `c>3/10`;
- two disjoint sets of original light coordinates `L_1,L_2`;
- with `p_j=P_{u^perp}r_j`, each transverse Gram

`G_a=sum_{j in L_a} p_j p_j^T`

satisfying

`G_a >= gamma I_2`, `gamma=7/800`;

- and every normalized transverse atom has leverage below `1/32` before this two-bank split.

The first unpaid implication at the start of this run is therefore `QFORM-RANK3-ONEHEAVY-TWOTRANSVERSE-BANK-CLOSURE-v1`: obtain a universal density bound from this one-heavy/two-independent-bank geometry while retaining original product provenance.

## 2. Extreme-product reduction remains exact

For completeness, the front end used below is the zero-loss B13 reduction from the earlier source-pinned report

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`.

Let

`D={f:R->[0,1]: integral f=1}`

and let `K:R^n->[0,1]` be measurable. Then

`sup_{f_1,...,f_n in D} integral K(x) prod_i f_i(x_i) dx`

` = sup_{|E_1|=...=|E_n|=1} integral_{E_1 x ... x E_n} K(x) dx`.          (2.1)

The proof is coordinatewise bathtub purification. With all factors except `f_i` fixed, the functional is `integral h_i(x) f_i(x) dx` with `0<=h_i<=1`; its supremum over `D` is attained, or approached in the presence of a level-set tie, by an indicator of a set of measure one. Replacing the coordinates successively never decreases the value. The reverse inequality is immediate because indicators are admissible densities. Thus the quadratic slab kernel

`K(x)=1_{a<=x^T A x<=a+epsilon}`

has exactly the same worst probability over cap-one product densities as over arbitrary unit-measure product sets. No interval, centered-uniform, diameter, or fragment-count hypothesis is introduced.

## 3. Designated partner applied: zero physical pairs pay their whole cross bank

The designated partner `account03/B13` completed `QFORM-ZERO-PAIR-CROSSBANK-AGGREGATE-v1` at

`yspennstate/math-open-problems@58dc674aade01aa82bb10fcaf254af03f41575fa`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260922T182042Z-account03-B13-qform-r14/REPORT.md`.

If a physical pair `i,j` obeys

`A_ii=A_ij=A_jj=0`

and `C` is its `2 x (n-2)` cross bank, then with

`D_cross=det(CC^T)>0`

the full arbitrary-ambient form satisfies

`||p_Q||_infinity <= 2 sqrt(e) D_cross^(-1/4)`.                         (3.1)

Here is the exact bridge to rank-three spectral geometry. Write

`A=R Lambda R^T`, `R^T R=I_3`, `min |eig Lambda|>=1`,

and let `r_i,r_j` be the two spectral rows. Because the selected physical `2 x 2` block is zero, deleting its two zero entries does not change either full matrix row. Therefore

`CC^T = [[(A^2)_ii,(A^2)_ij],[(A^2)_ji,(A^2)_jj]]`

`     = Gram(Lambda r_i, Lambda r_j)`.                                  (3.2)

Consequently

`D_cross=||Lambda r_i wedge Lambda r_j||^2`

and, since every singular value of `Lambda` is at least one,

`D_cross >= ||r_i wedge r_j||^2 =: Delta_ij`.                           (3.3)

Applying the partner theorem gives the concrete exact-rank-three corollary

`boxed(||p_Q||_infinity <= 2 sqrt(e) Delta_ij^(-1/4))`                  (3.4)

for every exact zero physical pair. For example, a zero pair with `Delta_ij>=3/8000` is paid by a constant below `23.70`. This genuinely uses the partner's group-before-reciprocal theorem; no individual outside cross minor is selected.

This does not force such a zero pair to exist. It removes that compatible endpoint from the remaining two-bank analysis.

## 4. A new zero-pivot theorem with a two-dimensional aggregate source

The next lemma is the main analytic tool of this run. It extends the completed dependent-pair hyperbolic-square theorem from physical independent coordinates to an arbitrary **two-dimensional aggregate density**, while retaining one genuinely independent scalar.

The source theorem is account03/B10,

`yspennstate/math-open-problems@c1af196adade03e07456c8f6e783f952b0fa0e8d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/account03-B10-20260922T121625Z-qform-r11/REPORT.md`,

whose Theorem 2.1 states that if `X` is independent of `(Y,Z)`, `||p_X||_infinity<=K`, `||p_(Y,Z)||_infinity<=H`, and

`T=2aXY+F(Y)+b(Z+theta(Y))^2`,

then

`||p_T||_infinity <= C0 (KH)^(2/3)|a|^(-2/3)|b|^(-1/3)`,               (4.1)

where

`C0=3*2^(2/3)`.

### Theorem 4.1 — `QFORM-ZERO-PIVOT-LINF2-SOURCE-v1`

Let `X` be independent of a two-dimensional random vector `Y=(Y_1,Y_2)`. Assume

`||p_X||_infinity<=K`, `||p_Y||_infinity<=H`.

Let `M` be a real symmetric invertible `3 x 3` matrix whose first diagonal entry is zero, `M_11=0`. For arbitrary affine `ell` and constant `d`, set

`T=(X,Y)^T M (X,Y)+ell^T(X,Y)+d`.

Then

`boxed(||p_T||_infinity <= C0 (KH)^(2/3)|det M|^(-1/3)).`              (4.2)

#### Proof

Write

`M=[[0,v^T],[v,B]]`, `v in R^2`.

Invertibility forces `v!=0`. Rotate only the two-dimensional **target variable** `Y` by an orthogonal matrix so that `v=(a,0)`, `a=||v||>0`. This changes neither the joint density cap `H` nor independence from `X`; it is not a rotation of the original independent coordinate family.

In the resulting coordinates,

`M=[[0,a,0],[a,b_11,b_12],[0,b_12,b_22]]`.

The determinant is

`det M=-a^2 b_22`,                                                      (4.3)

so `b_22!=0`. The linear term in `X` is absorbed by translating `Y_1`. Completing the square in `Y_2` writes the polynomial exactly as

`2a X Y_1 + F(Y_1)+b_22(Y_2+theta(Y_1))^2`

for measurable affine/quadratic `F,theta`. Apply (4.1) and use (4.3):

`||p_T||_infinity`

` <= C0(KH)^(2/3)|a|^(-2/3)|b_22|^(-1/3)`

` = C0(KH)^(2/3)|det M|^(-1/3)`.

QED.

The theorem needs no independence between the two coordinates of `Y`. The zero scalar pivot is essential; Section 7 below gives a sharp falsifier for the analogous nonzero-pivot claim under only the same low-dimensional density information.

## 5. Product projection input for a transverse bank

For a set `B` of original independent coordinates, let `p_j in R^2` be coefficient vectors and put

`eta=sum_{j in B} p_j X_j`, `G=sum_{j in B} p_j p_j^T`.

If `G` is positive definite, whiten the target plane: the coefficient rows of `G^(-1/2) eta` form an orthonormal two-dimensional projection. The source-valid two-dimensional Livshyts--Paouris--Pivovarov estimate used in account03/B09 and account03/B10 gives density at most `2` for that whitened projection. Hence

`boxed(||p_eta||_infinity <= 2/sqrt(det G)).`                           (5.1)

In the account01/B13 terminal branch, each transverse bank has `G>=gamma I_2`, `gamma=7/800`, so

`||p_eta||_infinity <= 2/gamma =1600/7`.                               (5.2)

This is an aggregate statement in the original product coordinates. No independence between the two components of `eta` is asserted or needed.

## 6. Main branch closure: a rank-two graph bank pays the null heavy pivot

Continue in the account01/B13 terminal exact-rank-three geometry. Fix the selected heavy row

`r_i=sqrt(c)u`, `c>3/10`,

and one of the two disjoint transverse banks `L_a`, with transverse rows

`p_j=P_{u^perp}r_j`, `G_a=sum_{j in L_a}p_jp_j^T>=gamma I_2`.

Choose an orthonormal basis of `u^perp` and write

`r_j=alpha_j u+p_j`.

Define

`b_a=sum alpha_j p_j`, `A_a=sum alpha_j^2`,

and the longitudinal Schur residual

`rho_a=A_a-b_a^T G_a^(-1)b_a >=0`.                                    (6.1)

Equivalently, with `q_a=G_a^(-1)b_a`,

`rho_a=sum_{j in L_a}(alpha_j-q_a^T p_j)^2`.                            (6.2)

Thus `rho_a=0` if and only if every row of that bank lies in one two-dimensional graph plane over `u^perp`:

`alpha_j=q_a^T p_j` for every `j in L_a`.                              (6.3)

### Theorem 6.1 — `QFORM-RANK3-NULL-GRAPH-BANK-v1`

Assume, in addition to the terminal two-bank hypotheses,

`u^T Lambda u=0`                                                       (6.4)

and that at least one transverse bank satisfies `rho_a=0`. Then the **full exact-rank-three quadratic form**, with arbitrary cap-one independent input laws and arbitrary values of every coordinate outside `{i} union L_a`, has density bounded by

`||p_Q||_infinity`

` <= C0 (2/gamma)^(2/3) (c |det Lambda|)^(-1/3)`

` < 266`.                                                              (6.5)

The same constant gives the slab-volume bound on arbitrary unit-measure product sets via (2.1).

#### Proof

Condition on all original physical coordinates outside `{i} union L_a`. This is a genuine product-preserving conditioning step. It produces only affine terms and a constant in the remaining variables.

Let

`eta=sum_{j in L_a} p_j X_j in u^perp`.

Because `rho_a=0`, (6.3) gives the exact spectral aggregate

`sum_{j in L_a} r_j X_j=(q_a^T eta)u+eta`.                              (6.6)

Hence after conditioning, the entire remaining spectral vector depends only on the independent heavy scalar `X_i` and the two-dimensional aggregate `eta`.

In the spectral basis `(u,e_1,e_2)`, define the linear map from `(x,eta_1,eta_2)` into spectral space by

`L=[[sqrt(c),q_1,q_2],[0,1,0],[0,0,1]]`.                               (6.7)

Its determinant is `sqrt(c)`. The quadratic matrix in the three variables `(X_i,eta)` is therefore

`M=L^T Lambda L`.                                                       (6.8)

By (6.4),

`M_11=c u^T Lambda u=0`,                                                (6.9)

while

`|det M|=(det L)^2 |det Lambda|=c|det Lambda|>=c`.                      (6.10)

The heavy variable has density cap one and is independent of the entire bank aggregate `eta`. By (5.1)--(5.2),

`||p_eta||_infinity<=2/sqrt(det G_a)<=2/gamma`.                         (6.11)

Apply Theorem 4.1 conditionally, uniformly in every fixed outside coordinate value. This yields the first inequality in (6.5). Finally use `c>3/10`, `|det Lambda|>=1`, `gamma=7/800`, and `C0=3*2^(2/3)`:

`C0 (2/gamma)^(2/3)c^(-1/3) <265.94<266`.                              (6.12)

Averaging the uniform conditional density bound proves the full assertion. QED.

### Meaning of the new closure

The final exact-rank-three branch is no longer unpaid at its rank-two-bank endpoint. After the account01/B13 two-bank reduction, a genuine counterexample sequence must now satisfy simultaneously:

1. the heavy/null scalar pivot is not already paid by a nonzero-pivot theorem at a fixed scale;
2. no partner-payable exact zero physical pair carries a fixed wedge resource;
3. **both** transverse banks have strictly positive longitudinal Schur residual `rho_1,rho_2>0`.

The last condition is new. It says that each disjoint transverse product bank must carry a genuine third spectral innovation; a bank living exactly on a two-dimensional spectral graph is harmless even though its two projected coordinates may be dependent.

## 7. Genuine mechanism falsifier: nonzero pivot cannot be controlled from an independent scalar plus a bounded 2D pair alone

It is tempting to try to extend Theorem 4.1 continuously to `M_11!=0` using only the same hypotheses `X independent Y`, `||p_X||_infinity<=K`, `||p_Y||_infinity<=H`, and `|det M|>=1`. That implication is false.

### Proposition 7.1 — `QFORM-INDEPENDENT-SCALAR-PAIRCAP-NONZERO-PIVOT-FALSE-v1`

For every `delta in (0,1)`, let

`R_delta=exp(2/delta)`

and define the planar set

`E_delta={(u,v):1<=u<=R_delta, 0<=2uv<=delta}`.                         (7.1)

Its area is exactly one:

`|E_delta|=int_1^{R_delta} delta/(2u) du`

`        =(delta/2) log R_delta=1`.                                    (7.2)

Let `(U,V)` have joint density `1_{E_delta}`, and let `X` be independent Uniform`[0,1]`. Thus the scalar density cap and the two-dimensional pair-density cap are both exactly one.

The pair quadratic variable

`R=2UV`

is exactly Uniform`[0,delta]`. Indeed the change `(u,v)->(u,r=2uv)` has Jacobian `1/(2u)`, so for `0<r<delta`,

`p_R(r)=int_1^{R_delta} du/(2u)=1/delta`.                               (7.3)

Now take

`Q=X^2+2UV`.                                                            (7.4)

Its matrix is

`M=[[1,0,0],[0,0,1],[0,1,0]]`,

which has eigenvalues `{1,1,-1}` and determinant `-1`. Since `X^2` has density `1/(2sqrt(s))` on `(0,1)`, at `t=delta`

`p_Q(delta)`

` =(1/delta) int_0^delta [2 sqrt(delta-r)]^(-1) dr`

` =delta^(-1/2)`.                                                       (7.5)

Thus the output density is unbounded as `delta->0` despite a genuinely independent cap-one scalar, a cap-one two-dimensional pair, and a perfectly conditioned three-eigenvalue quadratic matrix.

This is **not a counterexample to QFORM**, because `(U,V)` is a specially dependent pair and has not been represented as a linear image of the original independent product law. Its role is exact and narrower: it proves that the null graph-bank theorem cannot be extended to a nonzero heavy pivot merely by forgetting the bank's product-projection provenance and retaining only a two-dimensional density cap. This strengthens the correction discipline around low-dimensional projected-density surrogates.

## 8. Group-Gram identities for the surviving branch

The same notation gives a useful exact bookkeeping identity for future runs. The spectral Gram of the heavy coordinate plus one bank is

`T_a=c uu^T+sum_{j in L_a} r_jr_j^T`.

In the block basis `u plus u^perp`,

`T_a=[[c+A_a,b_a^T],[b_a,G_a]]`.

Therefore

`boxed(det T_a=det G_a (c+rho_a)).`                                    (8.1)

Since `G_a>=gamma I_2`, every group is full rank even at `rho_a=0`, and

`det T_a>=c gamma^2`.                                                    (8.2)

Moreover the exact leverage decomposition after the shear `q_a=G_a^{-1}b_a` is

`ell_i=c/(c+rho_a)`,                                                    (8.3)

`ell_j=p_j^T G_a^{-1}p_j + (alpha_j-q_a^Tp_j)^2/(c+rho_a)`.             (8.4)

The innovation fractions in the second term sum to

`rho_a/(c+rho_a)=1-ell_i`.                                              (8.5)

Thus the still-open `rho_a>0` branch is quantitatively a competition between one heavy original atom and a genuine longitudinal innovation distributed across a bank whose transverse directions are already uniformly elliptic. This is more specific than the previous generic "one-heavy/two-diffuse" description.

## 9. Target-level movement and next unpaid implication

**Full target:** still OPEN. Arbitrary additional spectral directions remain a separate debt even after exact rank three is finished.

**Exact-rank-three movement:** the account01/B13 terminal branch is now closed whenever either transverse bank has zero longitudinal Schur residual. The designated account03/B13 theorem also pays every exact zero physical pair at the whole-cross-bank scale (3.4). A false shortcut away from the null pivot was killed by the exact construction in Section 7.

The new first unpaid implication is:

`QFORM-RANK3-TWOBANK-POSITIVE-INNOVATION-v1`:

> In the one-heavy/two-transverse-bank terminal geometry, with `G_1,G_2>=7/800 I_2`, prove a universal density bound when both bank Schur residuals `rho_1,rho_2` are positive, uniformly as either tends to zero, while preserving the original product-linear provenance; or give a genuine cap-one product-law counterexample. In the near-null heavy-pivot regime, the argument must use the two independent banks jointly rather than replace either by an arbitrary bounded two-dimensional density.

A productive next split is to use (8.3)--(8.5): if the innovation in a bank is sufficiently diffuse after normalizing `T_a`, the completed diffuse separable-phase theorem applies; if it is concentrated, isolate only the finitely many innovation-heavy physical atoms while retaining a fixed fraction of the transverse Gram, then return to the graph-bank/hyperbolic endpoint rather than paying a reciprocal local minor.

## 10. Status

- Full QFORM: **OPEN / NOT PROVED**.
- Extreme-product reduction: previously proved, used unchanged.
- Designated partner whole-cross-bank theorem: read in full and applied in Section 3.
- `QFORM-ZERO-PIVOT-LINF2-SOURCE-v1`: **PROVED SUPPORTING THEOREM**.
- `QFORM-RANK3-NULL-GRAPH-BANK-v1`: **PROVED TARGET-VALID SUBCLASS**, explicit bound `<266`.
- `QFORM-INDEPENDENT-SCALAR-PAIRCAP-NONZERO-PIVOT-FALSE-v1`: **EXACT COUNTEREXAMPLE TO AN INTERMEDIATE MECHANISM**, not to QFORM.
- No interval extremality, bounded support, moment condition, post-rotation independence, arbitrary-joint coarea, or single-minor aggregation is used.

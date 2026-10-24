SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B20, 2026-09-23T01:19:56Z.

# account04/B20 r4 — product-partitioned hybrid closure and banked outer-square splice

Run: `20260923T011956Z-account04-B20-QFORM-r4`  
Classification: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and source boundary

The target remains unrestricted: independent real coordinates with probability densities at most one, arbitrary dimension, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. No moment, support, identical-law, sign, or post-rotation-independence assumption is made. Continuity is separate.

Fresh control was read at `yspennstate/math-research-brain@6fda8f39f22a4258db938d2d8d570676098c8ff2`, OWNER CONTROL revision `2026-09-22.15`. The required Claude package was read at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`; commit search also found its earlier source commit `b0cbc2233369b6a3f366cf569d425f485f123e1c`. The later synthesis `472b70df7d1edbb3afac23269bc2e4368ae0e371` and the live review corrections are retained.

The completed account01/B20 input actually used is `QFORM-DOUBLE-WEYL-E3-L3-v1` and its half-Riesz consequence at `yspennstate/math-open-problems@3801530a0437970354a492e8257237902e6619ff`. The completed cross-transverse input is account01/B16 `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1` at `ded9c22e680325b3ea44ef57a973d50f3db88128`.

No full proof is asserted. In particular, neither the ruled one-sheet estimate nor the E3 `L^3` estimate pays the convex/two-sheet or anchor-shear endpoint by itself.

## 2. Product-preserving longitudinal/transverse partition

Let `A=U Lambda U^T` have exact rank three, with `U^T U=I_3` and all three eigenvalues of `Lambda` of modulus at least one. Fix a physical row

`u_0=sqrt(c) e`, `||e||=1`, `c>=1/2`.

Assume the other physical rows admit a disjoint original-coordinate partition `L disjoint_union T` such that

- `u_j=alpha_j e` for `j in L`, and
- `u_j=w_j in e^perp` for `j in T`.

Parseval gives

`sum_{j in L} alpha_j^2=1-c`,  `sum_{j in T} w_j w_j^T=I_{e^perp}`.

Define the original-coordinate banks

`S=sqrt(c)X_0+sum_{j in L}alpha_j X_j`,
`Y=sum_{j in T}w_j X_j in e^perp`.

The two banks are independent because their leaves are disjoint before any deterministic change of basis. Moreover

`||p_S||_infinity <= c^(-1/2)`,

since the density of `sqrt(c)X_0` is at most `c^(-1/2)` and convolution cannot increase the cap. The sharp two-dimensional product-projection theorem gives

`||p_Y||_infinity <=2`.

This exact partition is stronger than a small mixed-row condition; the latter remains open.

## 3. New theorem: partitioned near-null hybrid

### Theorem `QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1`

In the setting of Section 2 put

`a=e^T Lambda e`, `D=|det Lambda|`.

If `|a|<=1/2`, then the density of `Q=X^TAX` is essentially bounded and

`boxed(||p_Q||_infinity <= C_* 2^(7/6) D^(-1/3) <105.463)`,

where `C_*=103680^(1/3)`.

#### Proof

In an orthonormal basis `e direct_sum e^perp`, the effective coefficient is the orthogonal conjugate

`B=O^T Lambda O=[[a,b^T],[b,C]]`.

Rotate only inside `e^perp` so `b=(beta,0)` and write `C=[[gamma,d],[d,eta]]`. Put

`P=beta^2|eta|`.

Account01/B16 proves for a cap-one scalar independent of a two-dimensional receiver of density cap `M` that

`||p_Q||_infinity <= C_* M^(2/3)(DP)^(-1/6)`.

The scalar here has cap `L_0<=c^(-1/2)`. Scale it to cap one. Under this scaling both `D` and `P` are divided by `L_0^2`, so the exact cap-sensitive form of the same inequality is

`||p_Q||_infinity <= C_*(L_0M)^(2/3)(DP)^(-1/6)`.        (3.1)

Account01/B16's spectral lemma applies to the orthogonal conjugate `B` and gives

`P >= (1-|a|)D >= D/2`.                                  (3.2)

Using `L_0<=sqrt(2)`, `M<=2`, and `D>=1` in (3.1)-(3.2) yields

`C_*(2sqrt(2))^(2/3)2^(1/6)D^(-1/3)=C_*2^(7/6)D^(-1/3)`.

Every independence assertion is at the original-coordinate bank level. QED.

## 4. New account01/B20 application: banked outer square plus E3

Account01/B20 proves that if an arbitrary same-side quadratic-affine residual `R(Y)` contains an original-coordinate cross block with

`Z=e_3(M^TM)>0`,

then

`sup_t E|R-t|^(-1/2) <= 6*2^(1/4)*sqrt(e) Z^(-1/12)`.      (4.1)

The published outer-square corollary uses one untouched cap-one coordinate. The same input yields the following product-safe extension.

### Theorem `QFORM-BANKED-OUTER-SQUARE-E3-v1`

Let `S` be independent of `Y` and have density cap at most `L`. If exact physical square completion gives

`Q=a(S+h(Y))^2+R(Y)`, `a!=0`,

and `R` has an original-coordinate cross block of third volume `Z>0`, then

`boxed(||p_Q||_infinity <= 6*2^(1/4)*sqrt(e) L |a|^(-1/2)Z^(-1/12)).`  (4.2)

Indeed, conditional on `Y`, the density of `a(S+h(Y))^2` at displacement `u` from its endpoint is at most

`L |a|^(-1/2)|u|^(-1/2)`.

Averaging this exact envelope against `R(Y)` and applying (4.1) proves (4.2); no conditional density of `R` is invoked.

For the longitudinal bank in Section 2, `L<=c^(-1/2)<=sqrt(2)`. Therefore the live O0-scale inequality is

`|a|>=1/4`, `Z>=1/256`

`implies boxed(||p_Q||_infinity < sqrt(2)*37.349 <52.819).`        (4.3)

This is an actual extension of account01/B20's completed theorem: an independent cap-controlled physical bank replaces the single untouched coordinate. It pays every partitioned large-Rayleigh state whose exact square residual retains the source-valid E3 bank. It does not claim that such E3 volume survives every Schur complement.

## 5. Exact no-coloop witness paid by Theorem 3

Let `Lambda=diag(1,1,-1)` in an eigenbasis `(p_1,p_2,p_3)`, and set

`e=(p_1+p_3)/sqrt(2)`, `f=(p_1-p_3)/sqrt(2)`, `g=p_2`.

Use six physical frame rows

`u_0=(sqrt(3)/2)e`, `u_1=(1/2)e`,

`u_2=u_3=f/sqrt(2)`, `u_4=u_5=g/sqrt(2)`.

Then `sum_j u_j u_j^T=I_3`, every leverage is at most `3/4`, and hence there is no physical coloop. For `A=U Lambda U^T`, the nonzero spectrum is exactly `{1,1,-1}`. In the basis `(e,f,g)`,

`O^T Lambda O=[[0,1,0],[1,0,0],[0,0,1]]`.

Thus

`Q=2SY_1+Y_2^2`,

`S=(sqrt(3)/2)X_0+(1/2)X_1`,

`Y_1=(X_2+X_3)/sqrt(2)`, `Y_2=(X_4+X_5)/sqrt(2)`.

Here `L_0<=2/sqrt(3)`, `M<=2`, and `D=P=1`. Equation (3.1) gives the concrete target-valid estimate

`boxed(||p_Q||_infinity <= C_*(4/sqrt(3))^(2/3)=82.078845441...)`.   (5.1)

This is a genuinely rotated exact-rank-three example with arbitrary independent cap-one input laws; it is not a Gaussian or CLT statement.

## 6. Compact noncircular proof graph and live gaps

The current implications can be arranged without hypothesis recycling:

1. A source-valid physical E3 cross block enters account01/B20's double-Weyl theorem and yields `L^3` plus the half-Riesz bound (4.1), not `L^infinity` by itself.
2. A genuine original-coordinate square independent of that residual converts (4.1) to `L^infinity`; Section 4 permits an independent physical bank of cap `L`, giving (4.2).
3. An exact longitudinal/transverse leaf partition produces such an independent scalar bank and a capped two-dimensional receiver. In the near-null range, the separate account01/B16 determinant resource pays it by Section 3.
4. Claude D'/D5, the diffuse/hub estimates, localized physical pivots, and the ruled one-sheet identity pay only their recorded hypothesis classes; none is used to infer another node's gate.

The first remaining implication after this splice is explicit. In a general approximate-coloop state, some residual physical rows have both longitudinal and transverse components. Then `S` and `Y` share original-coordinate leaves, so neither (3.1) nor (4.2) is available. Taking a worst conditional projection-density supremum is invalid, and account04/B16 has shown that every positive moment of that conditional height may diverge along a target-valid family.

The unpaid full-proof nodes are therefore:

- the mixed-row approximate-coloop/anchor-shear state, requiring an overlap-sensitive substitute for bank independence or a source-valid exit to D'/D5/ridge;
- the exact-rank-three convex/two-sheet side when the one-sheet ruling does not apply and no product partition pays it;
- the structural interaction with arbitrary additional spectrum when no physical residual E3 block survives.

Thus the full conjecture and global continuity remain open. No counterexample is produced.

## 7. Exact checks

The accompanying checker verifies the constants, Parseval identity, leverage list, effective matrix, and nonzero spectrum certificate used in Section 5.


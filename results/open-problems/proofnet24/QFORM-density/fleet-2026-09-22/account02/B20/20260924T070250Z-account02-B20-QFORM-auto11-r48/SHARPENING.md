SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T07:02:50Z.
attacking: the account03/B20 r49 four-cell rank-two grid by paying the exact one-sided-curvature endpoint with original-coordinate projection bounds, then isolating genuinely two-sided curvature as the remaining grid obstruction.

# r48 sharpening — a rank-two crossing already pays the one-sided-curvature endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL_STEP_APPLIED / ONE-SIDED-CURVATURE-R2-ENDPOINT-PAID / TARGET-VALID-R2-GRID-STRESS-PAID / TWO-SIDED-CURVATURE-REMAINS / FULL-QFORM-OPEN**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval is not native learned-memory receiver ingestion.

All random variables below are literal ORIGINAL coordinates. No post-rotation independence is asserted. The proof uses a two-dimensional projection only through its density bound, while conditioning leaves the opposite original-coordinate bank genuinely independent.

## 1. Two source-pinned projection facts

The required pinned package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

records the product-measure projection estimates used here. Its `COUNTEREXAMPLE_SEARCH.md` uses the sharp dimension-two marginal fact that if `U` is an orthonormal two-frame and `X` has independent coordinate densities bounded by one, then

`||p_{U^T X}||_infinity <= 2`.                                  (1.1)

Its `RESULTS.md`, through Rogozin and Ball cube slicing, uses the corresponding one-dimensional linear-form estimate: for independent cap-one coordinates `Z_j` and any nonzero coefficient vector `a`,

`||p_{<a,Z>}||_infinity <= sqrt(2)/||a||_2`.                    (1.2)

Both statements preserve the original product source; neither says that different spectral projections are independent.

## 2. Main theorem

### Theorem 2.1 — `QFORM-R2-CROSS-ONE-SIDED-CURVATURE-ENDPOINT-v1`

Let `I,J` be disjoint original-coordinate banks. Let `X_I,X_J` consist of mutually independent real variables with densities at most one. Let `N` be a real `I x J` matrix with

`sigma_2(N)>0`.                                                   (2.1)

Let `F:R^I -> R` be arbitrary measurable, let `b in R^J`, and define

`Q = F(X_I) + 2 X_I^T N X_J + b^T X_J`.                         (2.2)

Then `Q` is absolutely continuous and

`boxed: ||p_Q||_infinity <= 2 sqrt(pi) / sigma_2(N).`            (2.3)

In particular, after conditioning any outside original coordinates, the theorem applies to a quadratic form whenever the selected `J x J` principal block is zero; the entire `I x I` quadratic block, all conditioned affine terms, every higher singular direction of `N`, and all signs are allowed.

#### Proof

Take the top two singular vectors of `N`:

`N = sum_k sigma_k u_k v_k^T`,

and put

`U=(u_1,u_2)`, `V=(v_1,v_2)`, `Sigma=diag(sigma_1,sigma_2)`.      (2.4)

Condition on the full original vector `X_I=x`. The `X_J`-dependent part of (2.2) is the linear form

`<a(x),X_J>`,  `a(x)=2N^T x+b`.                                 (2.5)

By (1.2), whenever `a(x) != 0`, its conditional density is bounded by

`sqrt(2)/||a(x)||_2`.                                             (2.6)

Projecting `a(x)` onto the physical coefficient plane `span(v_1,v_2)` can only decrease its norm. With

`Y=U^T X_I`, `d=V^T b`,                                         (2.7)

we have exactly

`V^T a(X_I)=2 Sigma Y+d
            =2 Sigma (Y-y_0)`,

`y_0=-(1/2) Sigma^{-1}d`.                                        (2.8)

Therefore

`||a(X_I)||_2 >= 2 sigma_2(N) ||Y-y_0||_2`,                     (2.9)

and hence, after averaging the conditional densities,

`p_Q(t) <= [1/(sqrt(2) sigma_2(N))]
            E ||Y-y_0||_2^{-1}`                                 (2.10)

for almost every `t`. The term `F(X_I)` only shifts the conditional linear law and does not affect (2.6).

Because `U` is an orthonormal two-frame, (1.1) gives a density `g` of `Y` with

`0<=g<=2`, `integral g=1`.                                       (2.11)

The radial decreasing rearrangement / bathtub principle now gives, uniformly in `y_0`,

`integral_R2 g(y)/||y-y_0|| dy
 <= 2 integral_{||z||<=r_0} ||z||^{-1} dz`,                     (2.12)

where the disk has area `pi r_0^2=1/2`, so `r_0=1/sqrt(2pi)`. Thus

`E ||Y-y_0||^{-1}
 <= 2*(2pi r_0)
 =2 sqrt(2pi).`                                                   (2.13)

Combining (2.10) and (2.13) yields

`||p_Q||_infinity <= [2 sqrt(2pi)]/[sqrt(2) sigma_2(N)]
                    =2 sqrt(pi)/sigma_2(N)`,                    (2.14)

which proves (2.3).

Finally, the exceptional set where `a(X_I)=0` is null: by (2.8) it is contained in `{Y=y_0}`, and `Y` has the density (2.11). Thus the conditional absolutely continuous laws mix to an absolutely continuous law, completing the proof. QED.

## 3. Exact application to the newest account03/B20 r49 grid

The newest compatible designated partner is account03/B20 r49, canonical source

`yspennstate/math-open-problems@4bf5217dace0129fcb6995727e1d8afa671c2435`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T065238Z-account03-B20-QFORM-auto11-r49/REPORT.md`.

Its deep-peel grid provides literal original-coordinate partitions `R_1,R_2,C_1,C_2` for which all four cells satisfy

`sigma_2(A[R_a,C_b]) > s_grid`,                                  (3.1)

with the exact expression

`h=1/2-1/(4 sqrt(2))`,

`s_grid=h/126-2^-16
       =0.002550005533980064... .`                               (3.2)

Fix any cell `(a,b)`. Condition every original coordinate outside `R_a union C_b`. If the actual principal block on one selected side vanishes, say

`A[C_b,C_b]=0`,                                                   (3.3)

then Theorem 2.1 applies with `I=R_a`, `J=C_b`, while `F` contains the full arbitrary `R_a x R_a` curvature and every conditioning-generated affine/constant term. From (3.1)-(3.2),

`boxed: ||p_Q||_infinity
 < 2 sqrt(pi)/s_grid
 =1390.1568661610384... <1391.`                                  (3.4)

The transpose statement pays the case `A[R_a,R_a]=0`. Thus the r49 grid endpoint is already closed whenever one robust physical rank-two cell is curvature-free on either side. The remaining grid debt is genuinely **two-sided curvature**, not rank-two crossing itself.

## 4. Target-valid stress family: four robust rank-two cells, no E3, no strong edge

This also gives a clean obstruction to trying to force a third physical crossing direction from the r49 grid plus the target spectrum.

Let `m>=32` be divisible by four. On each of two `m`-coordinate banks choose the orthonormal Walsh two-frame

`u_1=m^{-1/2}(1,...,1)`,

`u_2=m^{-1/2}(1,...,1,-1,...,-1)`,                               (4.1)

with `m/2` plus signs and `m/2` minus signs, and use an identical frame `V` on the second bank. Set

`N=U V^T`,

`A_m = [[0,N],[N^T,0]].`                                         (4.2)

Then the nonzero singular values of `N` are exactly `1,1`, so

`spec(A_m)={1,1,-1,-1,0,...,0}`.                                (4.3)

Hence `A_m` satisfies the exact three-large-eigenvalue target. Its cross block has rank exactly two, so every third exterior volume is zero:

`e_3(N^T N)=0`.                                                   (4.4)

Partition each bank into two equal sets, each containing equal numbers of the `+` and `-` signs from the second Walsh row. Then for each half-bank restriction,

`U_a^T U_a=V_b^T V_b=(1/2)I_2`,                                 (4.5)

so every one of the four literal cells obeys

`sigma_2(N[R_a,C_b])=1/2`.                                      (4.6)

Meanwhile every physical coefficient has magnitude at most `2/m ->0`, and every row leverage is `2/m<=1/16`. Thus neither a dimension-free individual edge nor positive physical E3 follows from the robust four-cell rank-two grid, even under the full target spectrum.

This is not a QFORM counterexample. Theorem 2.1 applies to the **full** crossing `N` with `sigma_2(N)=1` and gives, for every independent cap-one product law,

`boxed: ||p_{X^T A_m X}||_infinity <=2 sqrt(pi)<3.545.`          (4.7)

So the exact rank-two endpoint is analytically benign despite defeating the repeated structural search for a third crossing direction.

## 5. Required pinned fifth-volume exit retained on the live state

Independently, on the literal global r49 physical cut `M_global=A[I,J]`, the pinned D5 theorem in `FOURIER_ROUTE_REPORT.md` gives

`e_5(M_global^T M_global)>=1/1024
 ==> ||p_Q||_infinity<=10 sqrt(2e)=23.3164398159...<23.317`.      (5.1)

Therefore every unpaid r49 grid state may assume

`e_5(M_global^T M_global)<1/1024`.                               (5.2)

This is an equation-level use of the required `e5f71d79...` source on the actual partner-generated physical cut.

## 6. Sharpened first unpaid implication

Combining the parent `REPORT.md` with Theorem 2.1 sharpens the live interface to

`QFORM-R49-ALIGNED-R2-WITH-TWO-SIDED-CURVATURE-PAYMENT-v1`:

> Under the full independent cap-one hypotheses and `s_3(A)>=1`, retain the account03/B20 r49 four-cell grid, `sigma_2(A[R_a,C_b])>s_grid` in every cell, the true nonzero rank-two tail/collar from the parent report, and the unpaid fifth-volume condition (5.2). The transverse-third-energy branch is already paid by the two-row-bank E3 mixture. The exact one-sided-curvature branch is now paid by Theorem 2.1. Prove a universal endpoint bound in the remaining state where the surviving robust rank-two crossing coexists with genuine quadratic curvature on both original-coordinate sides, without deleting the retained coefficient tail, taking a worst fibre, or declaring spectral projections independent.

The stress family (4.2) proves that the next mechanism should **not** try again to force a third cross singular direction or a dimension-free edge. It should instead make the existing two-dimensional product projection estimate stable under two-sided quadratic curvature—most plausibly by a joint Fresnel/BL treatment of the two latent crossing planes and one physical curvature source, or by routing that curvature to a completed physical-pair/hub receiver.

Full unrestricted QFORM remains **OPEN**. No valid target counterexample was found. Unrestricted continuity remains separate.

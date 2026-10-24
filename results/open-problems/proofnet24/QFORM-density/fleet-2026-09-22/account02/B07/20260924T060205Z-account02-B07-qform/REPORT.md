SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T06:02:05Z.
attacking: the r48 global rank-two separator — convert its retained Frobenius tail into an exterior-compound dichotomy, then carry determinant weight into pair-preserving physical coordinate cores without selecting one reciprocal minor.

# account02/B07 — third compound controls the rank-two exterior defect

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / complementary constructions  
Status: **NEW COMPOUND-TAIL INEQUALITY + R48 E3-OR-PLUCKER SEPARATOR + PAIR-PRESERVING LEADING CARRIER + BOUNDED-SUPPORT CORE COMPILER / FULL QFORM OPEN / CONTINUITY OPEN OUTSIDE PAID BRANCHES**.

The unrestricted theorem remains OPEN. No moment, support, log-concavity, iid, diagonal-basis, post-rotation independence, arbitrary-joint coarea, fiber-supremum, or deletion of a nonzero matrix tail is used. Singular vectors appear only in deterministic coefficient algebra.

## 1. Exact incoming state and source pins

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with no account02/B07 stop or reassignment. `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` was consumed. The latest completed designated partner read before this report was account03/B07 r48:

`yspennstate/math-open-problems@ce6e0d491d02d36a023beb94c85ae212a9b74483`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T053826Z-account03-B07-qform-r48/REPORT.md`.

Its still-unpaid non-near-rank-one branch has one literal global physical separator

`M=A[H_M^c,H_M]`

with

`dist_F(M,rank<=2)<2^-16`,                                          (1.1)

`s2(M)>d_*:=0.10429071727552326290...`,                            (1.2)

`s1(M)s2(M)>p_*:=1.19876993884320...`.                             (1.3)

Writing

`Z2=e2(MM^T)`,

r48 also proves `Z2>p_*^2=1.437049366274129...` and partitions the column bank into the actual matched physical pairs. For the normalized complete squared-2-minor law `p`, all but at most two matched pairs `K` have block-inclusion marginal

`beta_K(p):=p{the column pair intersects K}<=2/3`,                 (1.4)

and hence deletion leaves `e2(M_{-K}M_{-K}^T)>0.4790164554...`.

The pinned source required by the owner request was read at the exact revision

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. A completed result from that source is applied at a real target-valid obstruction in Section 7.

For the live E3 payment I use the completed marginal-free original-coordinate crossing theorem

`QFORM-Z3-CROSSING-MARGINAL-FREE-v1`

from account02/B03 at

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`.

For every literal physical cross block `C`, with arbitrary same-side quadratic blocks, affine terms, outside couplings, signs and extra spectrum retained,

`||p_Q||_infinity <= C3 e3(CC^T)^(-1/6)`,                          (1.5)

`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`,                       (1.6)

and that paid branch has an integrable Fourier envelope and hence a continuous density.

## 2. First unpaid implication: ordinary Frobenius rank-two closeness is the wrong invariant

The r48 handoff correctly retains the `2^-16` Frobenius tail because a small matrix tail can carry macroscopic second exterior volume when the leading singular value is large. The first question is whether that regression can still occur after r48 has also forced the **uniform second-singular-value floor** (1.2).

It cannot remain unpaid.

Let the squared singular values of an arbitrary real matrix be

`x1>=x2>=x3>=...>=0`,

and set

`E2=e2(x)`, `E3=e3(x)`,

`R2:=E2-x1*x2`.                                                     (2.1)

Thus `R2` is exactly the squared Hilbert-Schmidt norm of the part of `wedge^2 M` orthogonal to its leading singular component.

### Lemma 2.1 — `QFORM-E3-CONTROLS-EXTERIOR-R2-DEFECT-v1`

For every real matrix,

`boxed: E3 >= (x2/2) R2`,                                         (2.2)

or equivalently

`boxed: R2 <= 2 E3 / s2(M)^2`.                                   (2.3)

Proof. Put

`T=sum_{j>=3}x_j`,
`U=sum_{3<=i<j}x_i x_j`,
`V=e3(x3,x4,...)`.

Then

`R2=(x1+x2)T+U`,                                                   (2.4)

while

`E3=x1*x2*T+(x1+x2)U+V`.                                         (2.5)

Subtracting `(x2/2)R2` gives

`E3-(x2/2)R2`
` =(x2/2)(x1-x2)T+(x1+x2/2)U+V >=0`.                             (2.6)

No coordinate minor has been selected. QED.

The factor `1/2` is asymptotically sharp when `x1=x2` and one tail singular square tends to zero.

This is the key correction to the earlier reciprocal-fan warning: the bad family `(s1,s2,s3)=(n,n^-1,n^-1)` evades a compound conclusion only because `s2->0`. Once `s2` has a fixed positive floor, a macroscopic second-exterior tail automatically forces macroscopic third volume.

## 3. Apply Lemma 2.1 to the actual r48 separator

Choose the convenient relative exterior-defect threshold

`eta=1/144`,

and define

`delta_* := d_*^2 p_*^2 / 288`
`          =5.427133547214097e-5`.                                (3.1)

There are now two exhaustive cases.

### Case A: `Z3:=e3(MM^T)>=delta_*`

The completed marginal-free physical-Z3 theorem (1.5) gives the full ambient law

`boxed: ||p_Q||_infinity`
` <= C3 delta_*^(-1/6)`
` =54.220600709697784... .`                                      (3.2)

Every same-side block, outside coupling and additional spectral direction is retained. Continuity holds on this paid branch.

### Case B: `Z3<delta_*`

By (2.3), (1.2), (1.3), and `Z2>=s1^2s2^2>p_*^2`,

`R2/Z2`
` <=2Z3/(s2^2 Z2)`
` <2 delta_*/(d_*^2 p_*^2)`
` =1/144`.                                                        (3.3)

Thus every unpaid r48 global separator is not merely Frobenius-near rank two: its **entire second exterior compound is 143/144 concentrated in one rank-one exterior singular mode**.

This is `QFORM-R48-E3-OR-EXTERIOR-RANK1-v1`.

Notice that the `2^-16` Frobenius estimate is not used in deriving (3.3). It remains useful afterward because it retains a literal small coefficient tail around the leading rank-two carrier.

## 4. Sharp total-variation transfer to a product Pluecker law

Let

`L=s1 u1 v1^T+s2 u2 v2^T`                                       (4.1)

be the leading rank-two SVD truncation of `M`. In the physical bases, let `z` denote the vector of **all** `2x2` minors of `M` and let

`a=s1s2 (u1 wedge u2)(v1 wedge v2)^T`                            (4.2)

be the leading exterior component. Then

`||z||_2^2=Z2`, `||a||_2^2=s1^2s2^2`, and `a perpendicular (z-a)`.

Normalize

`w=z/sqrt(Z2)`, `v=a/(s1s2)`.                                   (4.3)

Choose the harmless sign of `v` so `<w,v>>=0`. The actual squared-minor law and the leading Pluecker product law are

`p_c=w_c^2`, `q_c=v_c^2`.                                       (4.4)

### Lemma 4.1 — squared-vector TV inequality

For unit real vectors `w,v`,

`(1/2) sum_c |w_c^2-v_c^2|`
` <=(1/2)||w-v||_2 ||w+v||_2`
` =sqrt(1-<w,v>^2)`.                                             (4.5)

Here `<w,v>^2=s1^2s2^2/Z2=1-R2/Z2`, so (3.3) gives

`boxed: d_TV(p,q)<1/12`.                                        (4.6)

This improves the earlier triangle-inequality estimate `sqrt(epsilon(1-epsilon))+epsilon`: orthogonality in exterior SVD gives the exact square-root transfer.

Moreover `q` factorizes exactly:

`q(S,T)=rho(S) kappa(T)`,                                       (4.7)

where

`rho(S)=det(U_S)^2`, `kappa(T)=det(V_T)^2`                       (4.8)

for the two-column orthonormal frames `U=(u1,u2)` and `V=(v1,v2)`. Their coordinate inclusion marginals are the ordinary rank-two leverage scores

`rho{i in S}=||U_{i,*}||_2^2`,
`kappa{j in T}=||V_{j,*}||_2^2`.                                (4.9)

No rotated random variables are introduced; this is solely a deterministic description of coefficient minors.

## 5. Integrate r48 pair-block selection: the dominant rank-two carrier survives every stable pair deletion

Let `K` be any r48 determinant-stable matched physical pair, so (1.4) holds. The event

`E_K={the physical column pair intersects K}`

is an event in the same complete determinant law. Hence (4.6) gives

`q(E_K)<=p(E_K)+d_TV(p,q)<2/3+1/12=3/4`.                         (5.1)

Therefore

`boxed: q{column pair avoids K}>1/4`.                            (5.2)

For the rank-two matrix `L`, summing its squared `2x2` minors over all row pairs and only column pairs avoiding `K` gives exactly

`e2(L_{-K}L_{-K}^T)`
` =s1^2s2^2 q{column pair avoids K}`
` >p_*^2/4`.                                                      (5.3)

Since `L_{-K}` has rank at most two,

`boxed: s1(L_{-K})s2(L_{-K})>p_*/2`
` =0.5993849694216... .`                                         (5.4)

This holds for **every** r48 stable matched pair, hence all but at most two matched physical pairs.

The actual nonzero tail is still present. Because column restriction is contractive,

`boxed: ||(M-L)_{-K}||_F<2^-16`.                                (5.5)

So the correct synchronized survivor is much sharper than “a near-rank-two global cut plus a stable E2 bank”: after any determinant-stable physical pair is removed, a quantitatively nondegenerate **leading rank-two carrier itself** remains, with product `>0.59938`, and the literal coefficient tail remains attached at its true size.

This is `QFORM-R48-PAIR-SEPARATED-LEADING-R2-v1`.

It directly defeats the previous reciprocal-fan regression in the r48 chamber. That regression can make the Frobenius tail compound-large only by sending `s2` to zero; the live partner has already ruled that out.

## 6. Bounded-support coordinate-core extraction without a single-minor inference

The Pluecker approximation also closes the bounded-support **two-direction** spectral subproblem at determinant-weight level.

Let `R0` and `C0` be physical row/column supports for the leading frames `U,V`, and define the leverage tails

`delta_R=sum_{i notin R0}||U_{i,*}||_2^2`,
`delta_C=sum_{j notin C0}||V_{j,*}||_2^2`.                       (6.1)

By a union bound under the pair laws,

`rho{S subset R0}>=1-delta_R`,
`kappa{T subset C0}>=1-delta_C`.                                 (6.2)

Using the product structure (4.7) and total variation (4.6),

`boxed:
 e2(M[R0,C0]M[R0,C0]^T)/Z2
 >=(1-delta_R)(1-delta_C)-1/12.
}`                                                                  (6.3)

No individual minor is selected or inverted.

In particular, if

`delta_R<=1/8`, `delta_C<=1/8`,                                  (6.4)

then

`e2(M[R0,C0]M[R0,C0]^T)`
` >(49/64-1/12)p_*^2`
` =(131/192)p_*^2`
` =0.980486807197453... .`                                       (6.5)

For the leading rank-two carrier itself the stronger exact product-law statement is

`e2(L[R0,C0]L[R0,C0]^T)`
` >=(49/64)s1^2s2^2`,                                            (6.6)

hence

`boxed:
 s1(L[R0,C0])s2(L[R0,C0])>(7/8)p_*
 =1.048923696487800... .
}`                                                                  (6.7)

If `|R0|,|C0|<=m`, the union `R0 union C0` is an actual original-coordinate principal core of size at most `2m`, and its cross rectangle carries the complete aggregate packet (6.5). Writing `r=min(|R0|,|C0|)`, the actual rectangle also obeys the finite-dimensional spectral product estimate

`s1(M[R0,C0])s2(M[R0,C0])`
` >=sqrt( e2(M[R0,C0]M[R0,C0]^T) / binom(r,2) )`                 (6.8)

because every term in `e2` is at most `s1^2s2^2`.

Thus whenever the two leading Pluecker factors have bounded physical supports carrying all but `1/8` leverage on each side, the coordinate-core extraction is complete at two-volume level with an explicit universal packet. The remaining obstruction is genuinely support-diffuse or genuinely a **third-resource** problem; it is not a failure to find one favorable `2x2` minor.

## 7. Required pinned-source application to a real target-valid obstruction

The pinned `e5f71d79...` Theorem D is now applied to an exact family that stresses precisely the old “small Frobenius tail can carry exterior volume” warning while satisfying the r48 `s2` floor.

Let `N>=8` be a Hadamard order. On two disjoint physical banks choose three flat orthonormal vectors `u1,u2,u3` and `v1,v2,v3`, so each row of either three-frame has squared leverage `3/N<=3/8<1/2`. For `t>2^16`, set

`M_t=t u1v1^T+(1/8)u2v2^T+t^(-1)u3v3^T`.                       (7.1)

Then

`s(M_t)=(t,1/8,t^-1)`,                                           (7.2)

`dist_F(M_t,rank<=2)=t^-1<2^-16`,                               (7.3)

`s2(M_t)=1/8>d_*`,                                               (7.4)

`s1(M_t)s2(M_t)=t/8>p_*`,                                       (7.5)

while the second-exterior tail outside the leading `(1,2)` mode is

`R2=1+(64t^2)^(-1)`,                                             (7.6)

which stays of order one even as the matrix Frobenius tail tends to zero. But necessarily

`Z3=e3(M_tM_t^T)=1/64`.                                         (7.7)

For exact rank three, the pinned source identifies the row 3-volume marginals with the physical three-frame leverages, here `3/N<=1/2`. Therefore pinned Theorem D applies directly to the full ambient quadratic form, with arbitrary same-side curvature and affine terms retained, and gives

`boxed:
 ||p_Q||_infinity
 <=6sqrt(e)(1/64)^(-1/6)
 =12sqrt(e)
 =19.78465524840154... .
}`                                                                  (7.8)

To make this an exact owner-target matrix while keeping the same obstruction, form the symmetric bipartite block

`[[0,M_t],[M_t^T,0]]`

and adjoin on a disjoint physical bank any rank-one symmetric block of eigenvalue `+1` (for example `ww^T` with a flat unit vector `w`). The spectrum then contains

`+t,-t,+1`,                                                        (7.9)

so at least three eigenvalues have modulus at least one. The pinned theorem still applies to the original physical cut and pays the full form by (7.8).

This is not a QFORM counterexample. It proves instead that the apparently dangerous absolute compound tail in the r48 chamber is analytically harmless for the correct reason: once `s2` is bounded below, that tail necessarily purchases physical third volume.

## 8. What is now closed and the sharpened first unpaid implication

The structural debt in account03/B07 r48 can be shortened.

Previously one had to retain simultaneously:

- a global physical `2^-16` Frobenius rank-two tube,
- a nondegenerate product `s1s2>1.19877`,
- a pair-stable complete E2 bank,
- and the warning that the small tail might still carry most of the second compound.

The last warning is now eliminated **inside this live chamber**. Either third volume is at least `delta_*` and the full law is already paid by (3.2), or the entire squared-minor law lies within `1/12` total variation of one product Pluecker law. In that unpaid branch every r48 stable physical pair can be removed while the leading rank-two carrier itself retains product `>0.59938`, and every bounded-support `1/8`-tail Pluecker branch carries the explicit physical core packet (6.5)-(6.7).

The sharpened first unpaid implication is therefore

`QFORM-R48-PLUCKER-SEPARATED-PAIR-THIRD-RESOURCE-v1`:

> In the E3-unpaid branch, spend an actual determinant-stable high matched physical rank-one pair `K` together with the disjoint leading rank-two carrier `L_{-K}` satisfying `s1(L_{-K})s2(L_{-K})>0.5993849694` and the retained literal tail `||(M-L)_{-K}||_F<2^-16`, while preserving arbitrary same-side curvature, all outside couplings and all additional spectrum. Alternatively, if the leading left/right Pluecker factors are support-diffuse, use that diffuseness directly as product-law smoothing. Do not rotate the random coordinates and do not delete the nonzero tail.

For a high pair in r48, the existing exact rank-one-pair receiver failure additionally gives `|lambda_K|>=1/32` and kernel-star scale `S_K<1/32`; those hypotheses may be used by the next receiver, but they do not by themselves justify a Schur-complement or independent-square shortcut.

The unrestricted QFORM theorem remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**; continuity is asserted only on branches whose cited Fourier receiver gives an integrable envelope.

## 9. Deterministic checks

`CHECKS.py` verifies (2.2) on 2000 random singular-value lists and the sharp squared-vector TV inequality on 250 random `5x5` matrices by explicit physical `2x2` minor enumeration. The recorded maximum ratio in (2.2) was `0.9942666610674387`, the maximum TV excess was `0.0`, and the captured output ends `STATUS=PASS`.

The checker also recomputes

`delta_*=5.427133547214097e-5`,

live paid bound `54.220600709697784`,

bounded-support actual `E2>0.980486807197453`,

stable-pair leading product `>0.5993849694216`,

bounded-support leading product `>1.0489236964878002`,

and pinned regression bound `12sqrt(e)=19.78465524840154`.

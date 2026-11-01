SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-24T10:40:17Z.
attacking: the r51 bounded-heavy weak-core packet — convert captured top-spectral mass into a quantitative principal/cross singular-value ladder, then spend the mixed branches by determinant-weighted row deletion before any coordinate-minor inversion.

# fleet03/B07 r52 — physical core/boundary singular-value ladder and E2 deletion packets

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW SUPPORTING STRUCTURAL LEMMAS / ONE NEW PAID E3 SUBBRANCH / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, iid, post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea, conditional density cap, deletion of a nonzero coefficient tail, or one-good-minor inversion is used. All coordinates below are original physical coordinates.

## 1. Incoming state and source-pinned dependencies

Incoming worker-owned state:

`yspennstate/math-open-problems@87ddc6e4974103cb1f992bab5cfeccadee810ddb`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260924T093712Z-fleet03-B07-qform-r51/REPORT.md`.

R51 reduced one live near-rank-two-T branch to a literal physical set `K` satisfying

`m:=|K|<=895`,                                                   (1.1)

and, unless the completed physical-core theorem had already paid the full ambient law,

`m<=2` or `s_3(A[K,K])<1/64`.                                  (1.2)

R51 also retained the global target hypothesis `s_3(A)>=1`.

Two completed dependencies are used in exact scope.

**Physical E3 receiver.** fleet02/B03, `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`, source-pinned at

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`.

For any literal physical cut `D=A[I,I^c]` with

`Z3=e_3(DD^T)>0`,

it gives a continuous `C_0` density for the full ambient form and

`||p_Q||_infinity <= C3 Z3^(-1/6)`,                            (1.3)

where

`C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`.                  (1.4)

**Designated partner.** fleet04/B07, `QFORM-PHYSICAL-CORE-SPECTRAL-LEAKAGE-GATE-v1`, read at

`yspennstate/math-open-problems@e5331e6c4246adcded8b07e2722d18a364688a0f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260924T081607Z-fleet04-B07-core-leakage-r3/REPORT.md`.

If `U` contains three orthonormal eigenvectors of `A` with eigenvalue magnitudes at least one, and for a physical set `I`

`B=A[I,I]`, `D=A[I,I^c]`, `delta_I=||U_{I^c}||_op^2`,

then the partner proves

`s_3(B)^2 >= 1-delta_I-||D||_op^2`,                            (1.5)

and, separately, its physical-fiber theorem pays any bounded physical principal block with a quantitative `s_3` lower bound. The new theorem below strengthens the deterministic leakage part (1.5) into a complete three-level singular-value transfer ladder.

## 2. Main new theorem: spectral resource transfer from a principal block to its physical boundary

### Theorem 2.1 — `QFORM-CORE-BOUNDARY-SINGULAR-LADDER-v1`

Let `A=A^T` and choose three orthonormal eigenvectors `u_1,u_2,u_3` whose eigenvalues satisfy `|lambda_j|>=1`. Put their columns in `U`.

For any physical coordinate set `I`, define

`B=A[I,I]`,
`D=A[I,I^c]`,
`a_I=lambda_min(U_I^T U_I)=1-||U_{I^c}||_op^2`.                (2.1)

Then, for `k=0,1,2`,

`boxed: s_{3-k}(D)^2 >= (a_I-s_{k+1}(B)^2)_+ .`               (2.2)

Equivalently,

`s_3(D)^2 >= (a_I-s_1(B)^2)_+`,                               (2.3)

`s_2(D)^2 >= (a_I-s_2(B)^2)_+`,                               (2.4)

`s_1(D)^2 >= (a_I-s_3(B)^2)_+`.                               (2.5)

This is an exact physical-coordinate statement. It does not rotate the random variables and it retains every additional eigenvalue of `A`.

### Proof

Since the selected eigenvalues have squared magnitude at least one, spectral decomposition gives the PSD inequality

`A^2 >= U U^T`.                                                 (2.6)

Taking the `I x I` principal block and using symmetry of `A`,

`(A^2)[I,I]=B^2+DD^T >= U_I U_I^T`.                           (2.7)

The three nonzero eigenvalues of `U_I U_I^T` are those of `U_I^T U_I`, so

`lambda_3(B^2+DD^T) >= a_I`.                                  (2.8)

For PSD matrices `X,Y`, Weyl's upper inequality says

`lambda_{i+j-1}(X+Y) <= lambda_i(X)+lambda_j(Y)`.               (2.9)

Apply (2.9) with `X=B^2`, `Y=DD^T`, and

`(i,j)=(1,3),(2,2),(3,1)`.

Because `lambda_i(B^2)=s_i(B)^2` and `lambda_j(DD^T)=s_j(D)^2`, (2.8) gives (2.3)-(2.5). QED.

The partner leakage inequality (1.5) is exactly the `k=2` endpoint of this ladder. The new content is that the same `A^2` identity quantitatively conserves all three curvature resources: if the principal block contains fewer than three strong singular directions, the missing directions must appear in the literal physical boundary crossing.

## 3. Actual r51 heavy-packet application

Apply Theorem 2.1 to the actual r51 set `K`. Let

`B=A[K,K]`, `D=A[K,K^c]`,
`a_K=lambda_min(U_K^T U_K)`.                                  (3.1)

Use the fixed capture threshold

`a_0=1/4`,
`d=sqrt(a_0/2)=1/sqrt(8)=0.3535533905932738...`.                (3.2)

There are now four exhaustive possibilities.

### 3.1 Spectral escape

If

`a_K<1/4`,                                                       (3.3)

then a unit linear combination of the three selected target eigenvectors has more than `3/4` of its squared mass outside the bounded physical packet `K`. This is now the precise meaning of the residual "spectral escape" branch; it is not conflated with failure of the principal core.

### 3.2 New fully paid branch: weak first principal singular value

Assume

`a_K>=1/4`,
`s_1(B)<=d`.                                                     (3.4)

Then (2.3) gives

`s_3(D)^2 >= 1/4-1/8=1/8`,

so

`s_3(D)>=1/sqrt(8)`.                                            (3.5)

Hence

`Z3=e_3(DD^T)>=s_3(D)^6>=1/512`.                               (3.6)

The completed marginal-free physical-E3 theorem (1.3) therefore pays the **full ambient law**, with a continuous `C_0` density and

`boxed: ||p_Q||_infinity <= C3*sqrt(8)
                              =29.840383692718255... .`          (3.7)

This closes a genuine piece of the previously unpaid r51 heavy-packet branch.

### 3.3 Mixed `1 principal + 2 boundary` branch

Assume

`a_K>=1/4`,
`s_1(B)>d`,
`s_2(B)<=d`.                                                     (3.8)

Then (2.4) gives

`boxed: s_2(D)>=d=1/sqrt(8).`                                  (3.9)

Thus one quantitative principal singular direction and two quantitative boundary singular directions survive simultaneously. This mixed branch is not declared analytically paid below; instead Section 4 spends its determinant weights before any coordinate selection.

### 3.4 Mixed `2 principal + 1 boundary` branch

Assume

`a_K>=1/4`,
`s_2(B)>d`.                                                      (3.10)

On the unpaid r51 state, (1.2) gives `s_3(B)<1/64` whenever `m>=3`; if `m<=2`, `s_3(B)=0` automatically. Hence (2.5) gives

`s_1(D)^2 > 1/4-1/4096=1023/4096`,

or

`boxed: s_1(D)>sqrt(1023)/64
                 =0.4997557997412336... .`                     (3.11)

This is the actual application of the designated fleet04/B07 leakage theorem: its equation (2.3) at the r51 values `a_K>=1/4` and `s_3(B)<1/64` forces exactly the physical-boundary lower bound (3.11). The new ladder additionally identifies when one gets two or three boundary singular directions instead of only operator-norm leakage.

Therefore every unpaid r51 heavy packet is now routed into: spectral escape (3.3), the fully paid continuous-E3 branch (3.4)-(3.7), the mixed `1+2` packet (3.8)-(3.9), or the mixed `2+1` packet (3.10)-(3.11).

## 4. Determinant-weight spending in the mixed `1+2` branch

The point of this section is to avoid immediately choosing a tiny coordinate minor from (3.8)-(3.9).

Let

`R_h=sum_{k in K} B_{hk}^2`,
`R=sum_h R_h=||B||_F^2`.                                       (4.1)

Since `s_1(B)>d`,

`R>d^2=1/8`.                                                     (4.2)

Let

`Z=e_2(DD^T)`.                                                  (4.3)

By `s_2(D)>=d`,

`Z>=s_1(D)^2 s_2(D)^2>=d^4=1/64`.                              (4.4)

For every physical row `h in K`, define its **E2 row-inclusion marginal**

`alpha_h = Z^{-1} sum_{R2 subset K, |R2|=2, h in R2}
                    sum_{C2 subset K^c, |C2|=2}
                    det D[R2,C2]^2`.                            (4.5)

Cauchy-Binet gives

`0<=alpha_h<=1`,
`sum_h alpha_h=2`.                                              (4.6)

Deleting the physical row `h` preserves exactly

`Z_{-h}:=e_2(D[K\{h},:]D[K\{h},:]^T)
        =Z(1-alpha_h)`.                                         (4.7)

Let

`H_2={h:alpha_h>1/2}`.                                         (4.8)

Then `|H_2|<=3`. There is an exhaustive alternative.

**Localized alternative.** If

`sum_{h in H_2} R_h >= R/2`,                                   (4.9)

then at most three physical rows carry principal-block row energy

`sum_{h in H_2}R_h >1/16`.                                    (4.10)

**Determinant-stable alternative.** Otherwise, for every `h notin H_2`, (4.7) gives `Z_{-h}>=Z/2`, and therefore

`sum_{h notin H_2} R_h Z_{-h}
 >= (Z/2)(R/2)
 =RZ/4
 >1/2048`.                                                      (4.11)

Since `m<=895`, some literal physical row satisfies

`boxed: R_h Z_{-h}>1/(2048m)
                   >=5.455656424581005e-7.`                    (4.12)

Moreover some `k in K` satisfies `B_{hk}^2>=R_h/m`, so the same row has a literal physical coefficient with

`boxed: B_{hk}^2 Z_{-h}>1/(2048m^2)
                         >=6.095705502325145e-10.`              (4.13)

Thus the mixed `1+2` branch is reduced without reciprocal-minor selection to either a three-row localized principal-energy packet or one concrete coefficient multiplied by a surviving **aggregate** E2 determinant bank after deleting its row.

Equation (4.13) is structural currency, not yet a density theorem: converting it into a physical E3 crossing must still control the contamination terms created when the coefficient `B_{hk}` is used as a bordered pivot. The earlier projected-two-volume/one-overlap machinery is the natural next receiver; no cancellation is silently ignored here.

## 5. Symmetric determinant-weight spending in the mixed `2+1` branch

There is a companion packet which retains the diffuse boundary star rather than selecting one outside coordinate.

Let

`Z_B=e_2(BB^T)`.                                               (5.1)

Since `s_2(B)>d`,

`Z_B>=s_1(B)^2s_2(B)^2>d^4=1/64`.                              (5.2)

Let

`t_h=||D[h,:]||_2^2`,
`T=sum_h t_h=||D||_F^2`.                                       (5.3)

From (3.11),

`T>=s_1(D)^2>1023/4096`.                                       (5.4)

Define the E2 row-inclusion marginal `beta_h` for the rectangular matrix `B` exactly as in (4.5), so

`sum_h beta_h=2`,                                               (5.5)

and row deletion preserves

`Z^B_{-h}=Z_B(1-beta_h)`.                                       (5.6)

Let `H_B={h:beta_h>1/2}`; again `|H_B|<=3`. Either

`sum_{h in H_B} t_h >=T/2>1023/8192`,                           (5.7)

so at most three physical rows carry more than `0.1248779296875` of the entire boundary-star energy, or there is a row `h notin H_B` satisfying

`boxed:
 t_h Z^B_{-h}
 > [ (1023/4096)(1/64) ]/(4m)
 =1023/(1048576m)
 >=1.0900657270207752e-6.`                                     (5.8)

Thus the mixed `2+1` branch also has a dimension-free determinant-stable packet: either its boundary star localizes on at most three physical rows, or one physical star survives together with a quantitatively large row-deleted principal E2 bank.

As in Section 4, (5.8) is supporting deterministic structure, not by itself a completed analytic receiver.

## 6. Regression checks

A deterministic numerical checker for this run performed:

* 900 random symmetric target-matrix tests with three planted eigenvalues of magnitude at least one and random physical subsets `I`; all three inequalities (2.3)-(2.5) held with zero violations;
* 500 mixed `1+2` packet regressions; the E2 inclusion-marginal identity, `sum alpha_h=2`, deletion formula (4.7), and dichotomy (4.9)/(4.12) held with zero violations;
* 500 mixed `2+1` packet regressions with zero violations.

The largest observed absolute error in `sum alpha_h=2` was below `2e-14`. These finite checks are regression evidence only; the proof is the exact `A^2`/Weyl/Cauchy-Binet argument above.

## 7. What changed and what remains

The r51 bounded-heavy/weak-core survivor is no longer a single opaque packet. At capture level `a_K>=1/4`, the physical principal/boundary resources obey an exact conservation ladder. A weak first principal singular value is now **fully paid** by a literal E3 boundary crossing with continuous density `<29.841`. The other two captured branches are converted into determinant-weighted mixed packets before any inversion, with explicit constants and at most-three-row concentration alternatives.

The first unpaid implication is now

`QFORM-MIXED-1PLUS2-OR-2PLUS1-BORDERED-E3-COMPILER-v1`:

* in (4.13), convert the physical coefficient times surviving row-deleted E2 bank into a genuine physical E3 crossing or a paid bounded core while controlling both row-star and column-star contamination;
* in (5.8), convert the physical boundary star times surviving principal E2 bank into the same type of paid object;
* separately, consume the spectral-escape branch `a_K<1/4` by returning its escaped top-spectral mass to the diffuse finite-carrier machinery.

The r51 T-side three-curvature branch and the earlier `E_star>1` same-bank-star branch remain distinct and unpaid.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** Continuity is proved only on the physical-E3 exit (3.7).

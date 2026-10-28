SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T01:13:28Z.

# account02/B20 — multiplicative low-rank tube compiler and third-mode separation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / R43-MULTIPLICATIVE-TUBE / GIANT-R1-THIRDMODE-SEPARATION / FULL-QFORM-OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`. Full-target continuity remains separate and OPEN.

## 1. Fresh source state and exact live target


The newest compatible completed designated-partner result consumed here is account03/B20 r43, report path

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T004659Z-account03-B20-QFORM-r43/REPORT.md`

at a compatible `math-open-problems` state containing that immutable report. Its live disjoint physical cross block `M` has singular values `s_1>=s_2>=...`, squared singular values `x_i=s_i^2`, and

`E_2(M)=e_2(x)>4/9`,                                              (1.1)

while the already-completed physical-E3 receiver pays the branch

`E_3(M)=e_3(x)>=2^(-18)`                                          (1.2)

with `||p_Q||_infinity<=82.760672`. Therefore the first unpaid E2 packet may assume

`E_2(M)>4/9`, `E_3(M)<delta:=2^(-18)`.                            (1.3)

The same partner proved the exact singular-tail inequality

`T_2 E_2(M) <= 3 E_3(M)`,                                        (1.4)

where

`T_2:=sum_(k>=3)x_k=dist_F(M,{rank<=2})^2`.                       (1.5)

Hence

`T_2<tau:=27/2^20=2.574920654296875e-5`.                         (1.6)

This run strengthens (1.6) in the regimes actually needed by the closure compiler and then uses the global third singular value of the full symmetric matrix rather than trying to force a nonexistent third crossing direction inside `M`.

## 2. Universal exterior-volume inequality retained from r43

For later use, note the exact sub-sum

`E_3(M) >= x_1 x_2 T_2`.                                         (2.1)

Therefore every current unpaid packet, without any branch assumption beyond (1.3), satisfies

`boxed: (s_1 s_2) sqrt(T_2) < 1/512.`                            (2.2)

This is a coefficient/exterior-volume statement only. It does **not** say the random quadratic contribution of the tail can be discarded.

## 3. Robust-rank-two branch: multiplicative tail, not merely absolute tail

Assume the r43 robust-rank-two branch

`s_2>=1/8`, i.e. `x_2>=1/64`.                                    (3.1)

From (2.1),

`x_1 T_2 < delta/x_2 <= 1/4096`.                                 (3.2)

Since `x_2<=x_1`, also `x_2 T_2<1/4096`. Writing the exact decomposition

`E_2(M)=x_1x_2+(x_1+x_2)T_2+e_2(x_3,x_4,...)`                    (3.3)

and using `e_2(x_3,...)<=T_2^2/2<tau^2/2` gives

`x_1x_2 > c_2 := 4/9 - 1/2048 - tau^2/2`                         (3.4)

with

`c_2=0.4439561628629336...`,
`s_1s_2>sqrt(c_2)=0.666300354842269...`.                         (3.5)

Combining (2.2) and (3.5) sharpens the absolute Frobenius tube to

`boxed:
 s_1 s_2 > 0.6663003548,
 (s_1 s_2) dist_F(M,rank<=2) < 1/512,
 dist_F(M,rank<=2) < 0.002931299.`                                (3.6)

In addition (3.2) gives the top-scale tail estimate

`boxed: s_1 dist_F(M,rank<=2)<1/64.`                              (3.7)

Thus the live R2 packet is not just within `0.005075` of rank two: its retained tail is small in the multiplicative scales that enter exterior products with the top singular modes. This is the correct robustness currency for the previous account02/B20 exact-rank-two four-currency compiler; it is not an illegal probabilistic tail deletion.

## 4. Small-second-singular branch: nested concentration/diffusion split

Now assume the r43 giant-near-rank-one branch

`s_2<1/8`.                                                        (4.1)

Let

`R:=sum_(k>=2)x_k=x_2+T_2=dist_F(M,rank<=1)^2`,
`r_0:=1/64+tau=16411/1048576`.                                   (4.2)

By (1.6), `R<r_0`. For `y=(x_2,x_3,...)`,

`E_2(M)=x_1R+e_2(y)`                                              (4.3)

and `e_2(y)<=R^2/2`. Hence

`x_1R > c_1:=4/9-r_0^2/2
       =0.44432197146908137...`,                                  (4.4)

so the giant rank-one packet has the fixed multiplicative residual currency

`boxed:
 s_1 dist_F(M,rank<=1) > sqrt(c_1)
 =0.6665748056063036... .}`                                       (4.5)

The residual itself satisfies a second exact concentration inequality. Since

`E_3(M)=x_1 e_2(y)+e_3(y)`,                                      (4.6)

we have `x_1e_2(y)<delta`. Applying the `k=1` instance of the same outside-tail counting argument as r43,

`T_2 R <= 2e_2(y)`,                                               (4.7)

and combining with (4.4) gives

`boxed:
 T_2 < 2 delta/c_1
 =1.7170869372101035e-5,
 dist_F(M,rank<=2)<0.004143775.}`                                 (4.8)

This improves the r43 rank-two tube even inside its nominal rank-one branch.

There is then a useful exhaustive sub-split.

### 4A. Residual concentrated in `s_2`

If `x_2>=T_2`, then `R<=2x_2`; (4.4) yields

`boxed: s_1s_2 > sqrt(c_1/2)=0.47133956521232195... .}`            (4.9)

Together with (2.2),

`dist_F(M,rank<=2)<1/(512 sqrt(c_1/2))
 <0.004143775`.                                                    (4.10)

So this subbranch is again a genuinely two-direction multiplicative crossing, even though the second singular value can be arbitrarily small in absolute size.

### 4B. Residual diffuse beyond `s_2`

If `x_2<T_2`, then `x_2<R/2`. Therefore

`sum_(k>=2)x_k^2 <= x_2 R < R^2/2`,                              (4.11)

and hence

`e_2(y)=(R^2-sum_(k>=2)x_k^2)/2 > R^2/4`.                        (4.12)

Using (4.6) and (4.4),

`delta>E_3(M)>x_1 R^2/4=(x_1R)R/4>c_1 R/4`,                      (4.13)

so

`boxed:
 R < 4 delta/c_1
 =3.434173874420207e-5,
 dist_F(M,rank<=1)<0.005860183,`                                  (4.14)

and (4.4) forces

`boxed:
 x_1>c_1^2/(4delta)=12938.249131142098...,
 s_1>113.7464246960848... .}`                                     (4.15)

Thus the formerly broad giant-rank-one branch is now either (4.9), a fixed two-direction multiplicative crossing, or (4.14)-(4.15), an ultra-giant rank-one crossing with an extremely small but retained diffuse residual.

### Theorem 4.1 — `QFORM-R43-MULTIPLICATIVE-TUBE-TRICHOTOMY-v1`

Every live r43 packet satisfying (1.3) lies in exactly one of the following source-coordinate coefficient regimes:

1. `s_2>=1/8`, with (3.6)-(3.7);
2. `s_2<1/8` and `x_2>=T_2`, with (4.5), (4.8)-(4.10);
3. `s_2<1/8` and `x_2<T_2`, with (4.5), (4.14)-(4.15).

No projected random coordinates are asserted independent in this theorem.

## 5. Global third-mode separation in the giant-rank-one branch

The target assumption is on the **full symmetric matrix** `A`, not just the crossing `M`: its third singular value obeys

`s_3(A)>=1`.                                                       (5.1)

Let `I,J` be the literal disjoint source-coordinate banks defining `M=A[I,J]`, and put `K=(I union J)^c`. In the branch `s_2(M)<1/8`, choose unit singular vectors `u` on `I`, `v` on `J` for `s_1(M)` and define the symmetric rank-two crossing

`B=s_1( u~ v~^T + v~ u~^T )`,                                    (5.2)

where the tildes mean zero-extension to the full physical coordinate space. Then `rank B<=2`. By the best-rank-two approximation/min-max characterization of singular values,

`||A-B||_op >= s_3(A)>=1`.                                        (5.3)

Let `F=M-s_1uv^T`; the symmetric embedding

`E=F~+F~^T`                                                       (5.4)

has operator norm exactly `||E||_op=||F||_op=s_2(M)<1/8`. Define

`C:=A-B-E`.                                                        (5.5)

Then `C` is exactly the coefficient matrix obtained from `A` by setting the full `I x J` and `J x I` crossing to zero, with every same-bank and outside coupling retained. From (5.3)-(5.5),

`boxed: ||C||_op>7/8.`                                            (5.6)

Write `C` as the sum of its five symmetric block pieces

`C_II + C_JJ + C_KK + C_IK + C_JK`,                              (5.7)

where a cross piece denotes the symmetric embedding of that rectangular physical block. Each cross-piece norm equals the rectangular block norm. Triangle inequality therefore yields

`boxed:
 max{||A[I,I]||_op, ||A[J,J]||_op, ||A[K,K]||_op,
     ||A[I,K]||_op, ||A[J,K]||_op} > 7/40.}`                      (5.8)

This is a deterministic coefficient theorem and does not remove `B`, `E`, or any random term from the law. It says the third target mode cannot disappear into the dominant rank-one `I|J` crossing: after the entire `I|J` crossing is zeroed, a fixed-scale physical same-bank or exterior-crossing resource necessarily remains.

### Theorem 5.1 — `QFORM-R43-GIANT-R1-THIRDMODE-SEPARATION-v1`

Under the full target spectral hypothesis and the r43 giant-rank-one branch `s_2(M)<1/8`, the complementary zero-`I|J` coefficient geometry contains one of the five literal resources in (5.8) at scale `>7/40`.

This is the strongest new closure resource of the run: it converts the global third-eigenvalue assumption into an explicit source-coordinate object exactly where the r43 crossing itself becomes effectively rank one.

## 6. Target-valid stress family: the third mode really can be exterior

A tempting stronger claim would say that the target condition `s_3(A)>=1`, together with (1.3), forces `s_2(M)` to stay bounded below or forces a positive third crossing volume inside `M`. That is false.

Fix `m=3`, `c=1/2` and a large parameter `L`. Let a literal physical cross block have four singular values

`s_1=L`,
`s_2=s_3=s_4=sqrt(c/3)/L=1/(sqrt(6)L)`,                           (6.1)

and no others. Then

`E_2(M)=c+c^2/(3L^4)>1/2>4/9`,                                  (6.2)

while

`E_3(M)=c^2/(3L^2)+c^3/(27L^6)
       =1/(12L^2)+1/(216L^6) ->0`.                               (6.3)

For `L` large, (1.3) holds, `s_2<1/8`, and because the three residual squared singular values are equal,

`x_2<T_2=2x_2`;                                                   (6.4)

thus this is precisely subbranch 4B. Also

`s_1 dist_F(M,rank<=1)=sqrt(c)=1/sqrt(2)`.                        (6.5)

Realize the singular vectors by sufficiently long flat orthogonal sign vectors on the two source banks. Taking their bank sizes much larger than `L` makes every physical crossing entry arbitrarily small. Embed the block symmetrically as

`[[0,M],[M^T,0]]`,                                                (6.6)

and append, on a disjoint original-coordinate bank of size `q>64`, the flat rank-one PSD block `ww^T`, `w=q^(-1/2)(1,...,1)`. The full spectrum then contains

`+L,-L,+1`,                                                       (6.7)

so it satisfies the target requirement of three eigenvalues of modulus at least one. All physical diagonal entries can be made `<1/64`; by spreading the sign vectors, all physical `I|J` entries can also be made `<1/64`, and the appended rank-one block has vanishing 2x2 principal determinants. Hence the construction is compatible with the scalar/pair no-pivot scale as well.

The global third mode in this family is wholly exterior to `M`. This is **not** a counterexample to QFORM; it is a target-valid counterexample to any stronger structural assertion that the third large eigenvalue must manufacture a robust `s_2(M)` or positive `E_3(M)` inside the chosen crossing. Theorem 5.1 identifies the correct resource: here (5.8) is witnessed by the exterior principal block `A[K,K]`, whose operator norm is exactly one.

## 7. Required pinned interactive theorem spent on the live block

The pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed unrestricted fifth-volume theorem states for any literal physical cross block `N`

`||p_Q||_infinity <= 5 sqrt(2e) e_5(N^T N)^(-1/10)`               (7.1)

with no row-marginal hypothesis. Applying (7.1) to the **actual live r43 physical block `M`** gives

`e_5(M^TM)>=1/1024
 => ||p_Q||_infinity <= 10 sqrt(2e) <23.317.`                     (7.2)

Therefore every still-unpaid packet after this run may additionally assume

`boxed: e_5(M^TM)<1/1024.`                                       (7.3)

This exit retains all same-bank quadratic blocks, affine terms, outside couplings, and nonzero tails.

## 8. Updated source-complete first unpaid implication

The previous broad r43 edge

`QFORM-E2-ULTRATHIN-R2-OR-GIANT-R1-PAYMENT-v1`

can now be replaced by the narrower interface

`QFORM-R43-MULTIPLICATIVE-R2-OR-EXTERIOR-THIRDMODE-PAYMENT-v1`:

> Under the original independent cap-one source laws and full symmetric target `s_3(A)>=1`, after the completed E3 and D5 exits, pay either:
>
> **(R2)** a literal physical crossing with `s_1s_2>0.6663003548`, `(s_1s_2)dist_F(rank<=2)<1/512`, and `s_1 dist_F(rank<=2)<1/64`; or
>
> **(R1-concentrated)** a literal physical crossing with `s_1s_2>0.4713395652`, `(s_1s_2)dist_F(rank<=2)<1/512`, together with the complementary fixed-scale resource (5.8); or
>
> **(R1-diffuse)** an ultra-giant literal rank-one crossing satisfying `s_1>113.7464`, `dist_F(rank<=1)<0.005861`, together with the complementary fixed-scale resource (5.8).
>
> In all cases `e_5(M^TM)<1/1024`, all coefficient tails are retained, arbitrary same-bank curvature remains, and no rotated source vector is treated as independent.

The natural next mechanism is now clear. In R2, robustify the previous anchored four-currency Fourier receiver using the multiplicative exterior bounds rather than deleting the tail. In R1, route the guaranteed `>7/40` complementary block into the already-developed two-star / one-anchor / ridge / physical-volume compilers; do not attempt again to force a third singular direction inside `M`, because Section 6 disproves that strategy.

## 9. Verification notes

All constants above were independently recomputed from exact rational expressions:

- `delta=1/262144`;
- `tau=27/1048576=2.574920654296875e-5`;
- `r_0=16411/1048576=0.01565074920654297`;
- `c_2=4/9-1/2048-tau^2/2=0.4439561628629336...`;
- `sqrt(c_2)=0.666300354842269...`;
- `1/(512 sqrt(c_2))=0.0029312981537618367...`;
- `c_1=4/9-r_0^2/2=0.44432197146908137...`;
- `sqrt(c_1)=0.6665748056063036...`;
- `2delta/c_1=1.7170869372101035e-5`;
- `sqrt(c_1/2)=0.47133956521232195...`;
- `4delta/c_1=3.434173874420207e-5`;
- `c_1^2/(4delta)=12938.249131142098...` and its square root `113.7464246960848...`.

Two independent end-to-end reviews of a full-target proof do not exist because no full-target proof is claimed. The theorem-sized statements in Sections 3–5 have complete proofs on the page and use only deterministic singular-value algebra plus already-pinned completed receivers.

## 10. Status

`QFORM-R43-MULTIPLICATIVE-TUBE-TRICHOTOMY-v1`: **PROVED supporting closure theorem**.  
`QFORM-R43-GIANT-R1-THIRDMODE-SEPARATION-v1`: **PROVED supporting closure theorem**.  
Section 6 stronger forcing assertion: **REFUTED by target-valid coefficient family; not a QFORM counterexample**.  
Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.

No FEI, installation, benchmark, email, notification, public release, paid-model/API, cross-account authentication, permission, or scheduler mutation was used in the mathematical work.

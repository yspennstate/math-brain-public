SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T17:21:19Z.
attacking: the newest fleet02/B20 transverse Frobenius-rank-two packet; force a genuine physical E3 payment unless the packet collapses to a rank-one tube or a common four-plane alignment.

# fleet01/B20 — mixed-E3 transverse compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T172119Z-fleet01-B20-QFORM-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / FULL_QFORM_OPEN / GLOBAL_CONTINUITY_OPEN / WITHOUT_VERIFIED_BRAIN**.

The unrestricted conjecture is not claimed proved or disproved. The new paid branch below has a continuous `C_0` density because it exits through the source-pinned marginal-free physical-E3 Fourier theorem. No Gaussianity, moment, iid, compact-support, connected-support, log-concavity, post-rotation independence, law-uniform pointwise quadratic-phase decay, worst-fiber supremum, one-good-minor extraction, or deletion of a nonzero random tail is used.

## 1. Fresh source-pinned inputs

### 1.1 Owner/correction state


### 1.2 Required completed partner fleet02/B20

Newest completed designated-partner mathematics before this publication:

- brain handoff commit `9410aa30113cc4c2e0e9daf562a5b9e53a007741`;
- canonical math commit `yspennstate/math-open-problems@20ec5f8f3ed2028edf27894cd3956d13e4662a9a`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T155833Z-fleet02-B20-QFORM-auto11c/`;
- fresh-partner addendum theorem `QFORM-ALIGNED-TRANSVERSE-R2-FROBENIUS-COLLAR-v1`.

In every still-unpaid transverse self-bank state there is a literal original-coordinate block

`M=A[D1,D2]`, with `D1 disjoint D2` and `D1 union D2=J`,

whose singular values `m1>=m2>=...` obey

`sum_(r>=3) m_r^2 < 1/16384`,                                    (1.1)

and

`m1^2+m2^2 > c_M := 4026400769/4398046511104
                  =0.000915497541654986... .`                    (1.2)

Equivalently, if `M_2` is its best rank-two SVD truncation,

`||M-M_2||_F <1/128`.                                             (1.3)

This partner inequality is consumed quantitatively in Section 5, not merely cited.

### 1.3 Inherited aligned-R2 bicore

The transverse branch above is a descendant of the fleet03/B19/B20 aligned STAR4 R2 state. It retains the old literal physical cross block

`N=A[J,K]`, `J disjoint K`,

with top-two left singular plane `P` and second singular value `n2` satisfying

`n2^2 > c_N := 63 E0/(64*259)
              =63(1-2^-20)^2/(256*259)
              =0.000950167106616394... .`                        (1.4)

The source is `yspennstate/math-open-problems@6dfd43d5519df1fc40ea26f7d0bbe300ad32412d`, fleet03/B19 report `20260923T145843Z-fleet03-B19-QFORM-r36`, equation (3.2), carried into fleet03/B20 and then fleet02/B20.

### 1.4 Marginal-free physical E3 receiver

A same-hour completed peer theorem is

- `yspennstate/math-open-problems@52cef3abd27c641ae6666d6ee3bbc25d90cb4813`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T170106Z-fleet03-B02-qform-r35/REPORT.md`;
- theorem `QFORM-CROSS-E3-MARGINALFREE-L1-v1`.

For every literal original-coordinate cross block `T=A[L,R]`, `L disjoint R`, with

`Z=e_3(TT^T)>0`,

it gives the full ambient law

`||p_Q||_infinity <= C_E3 Z^(-1/6)`,                              (1.5)

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`,                  (1.6)

and genuine Fourier `L^1`, hence a continuous `C_0` density. Its proof retains arbitrary same-bank quadratic terms, outside variables, affine terms and signs. It is conditional only on the source-pinned projected-crossing receiver whose proof was subsequently included in the current owner checkpoint; no post-rotation independence is used.

## 2. New deterministic mixed-volume identity

Let

`M_2 = U diag(m1,m2) V^T`,                                       (2.1)

where the two columns of `U` are supported on `D1` and the two columns of `V` on `D2`. Let `P_U`, `P_V` be the corresponding padded orthogonal projections in `R^J`. Since `D1` and `D2` are disjoint,

`P_U P_V=0`, and `W:=P_U+P_V` is an orthogonal projection of rank four. (2.2)

Write the top-two truncation of the old bicore as

`N_2 = [p1 p2] diag(n1,n2) Q^T`,                                 (2.3)

with orthonormal `p1,p2 in R^J`, and let

`P=p1 p1^T+p2 p2^T`.                                              (2.4)

Let `E1,E2` be the coordinate projections onto `D1,D2`. Define the two literal physical cross blocks

`T1=A[D1, D2 union K]=[M, E1 N]`,                                (2.5)

`T2=A[D2, D1 union K]=[M^T, E2 N]`.                              (2.6)

For the truncated blocks

`T1^0=[M_2,E1 N_2]`, `T2^0=[M_2^T,E2 N_2]`,                     (2.7)

Cauchy-Binet/exterior algebra gives the exact two-M-one-N contributions

`Z1=(m1 m2)^2 ||(I-P_U)E1 N_2||_F^2`,                            (2.8)

`Z2=(m1 m2)^2 ||(I-P_V)E2 N_2||_F^2`.                            (2.9)

Proof of (2.8): for each physical column `z` of `E1 N_2`, summing the squared `3x3` determinants obtained by choosing `z` and any two physical columns of `M_2` is the squared exterior norm

`|| wedge^2(M_2) wedge z ||^2
 =(m1m2)^2 ||(I-P_U)z||^2`.

Summing over the `K` columns gives (2.8). Equation (2.9) is identical after transposition.

Now expand in the left singular basis of `N_2`:

`r1+r2 := ||(I-P_U)E1N_2||_F^2 + ||(I-P_V)E2N_2||_F^2`

`= sum_(a=1)^2 n_a^2 [1-||P_U p_a||^2-||P_V p_a||^2]`

`>= n2^2 [2-Tr(WP)].`                                             (2.10)

Every bracket is nonnegative because `W` is an orthogonal projection.

Finally, the SVD orthogonality gives exact PSD decompositions

`MM^T=M_2M_2^T+(M-M_2)(M-M_2)^T`,                               (2.11)

`NN^T=N_2N_2^T+(N-N_2)(N-N_2)^T`.                               (2.12)

After taking the relevant row principal blocks, (2.11)-(2.12) imply

`Tq Tq^T >= Tq^0 (Tq^0)^T` in Loewner order, `q=1,2`.             (2.13)

Thus no residual cross tail is deleted. In particular

`e_3(TqTq^T) >= e_3(Tq^0(Tq^0)^T) >= Zq`.                        (2.14)

## 3. New theorem — `QFORM-TRANSVERSE-R2-MIXEDE3-OR-COMMON4PLANE-OR-R1-v1`

In every still-unpaid fleet02/B20 transverse state described in Section 1, at least one of the following three alternatives holds.

### (A) Absolute physical rank-one tube

`m2<1/128`, and

`||M-M_1||_F < 1/(64 sqrt(2)) =0.0110485434560...`,               (3.1)

while

`m1^2 > 3757965313/4398046511104
      =0.000854462131092486...`,                                  (3.2)

hence `m1>0.0292311885732...`.

### (B) Common physical four-plane alignment

`m2>=1/128` and

`Tr(WP)>7/4`.                                                     (3.3)

Equivalently, if `Pframe=[p1 p2]`,

`||(I-W)Pframe||_F^2 <1/4`,                                      (3.4)

so every unit vector in the old top-two left singular plane lies within Euclidean distance `<1/2` of the direct sum

`Ran(U) direct_sum Ran(V)`,                                      (3.5)

where the two two-dimensional summands live on the disjoint original-coordinate banks `D1,D2`.

### (C) Full ambient density payment

The full quadratic form has a continuous `C_0` density and

`boxed: ||p_Q||_infinity < 863.854.`                              (3.6)

No marginal hypothesis is required in this branch.

## 4. Proof of the paid mixed-E3 branch

Assume alternative (A) fails, so

`m2>=1/128`.                                                      (4.1)

From the partner top-two-energy bound (1.2),

`m1^2 >= (m1^2+m2^2)/2 > c_M/2`,                                 (4.2)

hence

`(m1m2)^2 > c_M/(2*128^2)=c_M/2^15`.                             (4.3)

If alternative (B) also fails, then

`Delta:=2-Tr(WP)>=1/4`.                                          (4.4)

Insert (1.4), (4.3), and (4.4) into (2.10):

`Z1+Z2
 =(m1m2)^2(r1+r2)
 > (c_M/2^15) c_N (1/4)
 = c_M c_N/2^17`.                                                (4.5)

Therefore one orientation `q in {1,2}` satisfies

`Zq > c_M c_N/2^18`.                                             (4.6)

By (2.14), the **actual** literal physical cross block `Tq`, with every nonzero SVD tail retained, has

`e_3(TqTq^T) > Z_*:=c_M c_N/2^18`.                               (4.7)

The exact rational value is

`Z_* = 39843594176681961455625 /
       12007186485361788890976772761321472`

`    =3.3183122645139323e-12`.                                   (4.8)

Apply the marginal-free E3 receiver (1.5):

`||p_Q||_infinity
 < C_E3 Z_*^(-1/6)
 =863.8530432166586...
 <863.854`.                                                       (4.9)

The receiver also gives `phi_Q in L^1`, hence a continuous density vanishing at infinity. This proves alternative (C).

## 5. Direct application of fleet02/B20's Frobenius collar

It remains to justify the quantitative rank-one alternative, and this is where the newest completed fleet02/B20 collar is used at an actual inequality.

If `m2<1/128`, then the SVD components are Frobenius-orthogonal, so (1.1) gives

`||M-M_1||_F^2
 =m2^2+sum_(r>=3)m_r^2
 <1/16384+1/16384
 =1/8192`.                                                        (5.1)

Thus (3.1) follows. Likewise (1.2) gives

`m1^2
 =(m1^2+m2^2)-m2^2
 > c_M-1/16384`

`= (4026400769-268435456)/4398046511104`

`=3757965313/4398046511104`,                                     (5.2)

which proves (3.2). This is a genuine strengthening of the transverse survivor: the small but nonzero random tail is retained in the exact Frobenius estimate; it is not set to zero.

If instead `m2>=1/128` and the E3 payment fails, Section 4 forces `Delta<1/4`, i.e. (3.3)-(3.5). QED.

## 6. Interpretation and first remaining implication

The newest fleet02/B20 transverse Frobenius-rank-two branch is therefore no longer a single undifferentiated low-rank packet. Its genuinely rank-two, geometrically **misaligned** part is paid uniformly and continuously below `863.854` by a literal original-coordinate E3 block. The only transverse survivors are:

1. an absolute rank-one physical tube with `m1>0.02923` and Frobenius error `<1/(64 sqrt2)`; or
2. a common-four-plane state in which the old rank-two `J-K` left plane is within one-sided subspace gap `<1/2` of the direct sum of the two top singular planes of the internal `D1-D2` block.

The second alternative is precisely the finite-plane/coherent-cycle geometry identified independently in current B19 work: when the plane mismatch is bounded below, physical E3 pays; the true obstruction is the common-plane limit. I do **not** claim the coherent-cycle-with-tail density inequality has been proved.

The first remaining implication for this B20 path is therefore

`QFORM-TRANSVERSE-R1-OR-COMMON4PLANE-WITH-TAIL-PAYMENT-v1`:

> pay either the quantitative rank-one tube (3.1)-(3.2), or the common-four-plane state (3.3)-(3.5), while retaining the actual nonzero cross tails, the original hub/star couplings, arbitrary same-bank curvature, outside couplings and extra spectrum; alternatively route either state to a source-valid physical-E3/ridge/pivot receiver.

The separate in-plane fleet02/B20 carrier `rank(S0)<=5`, `s3(S0)>0.7985866375852596`, `||A-S0||op<0.201414` remains an independent unpaid branch.

## 7. Scope/corrections

The theorem is deterministic coefficient geometry plus a source-pinned physical-cross Fourier receiver. It never treats SVD coordinates as independent random variables. It never invokes law-uniform pointwise quadratic oscillatory decay, arbitrary-joint rank-three coarea, a worst conditional-density supremum, a single-good-minor extraction from aggregate volume, or deletion of any coefficient-small random quadratic term.

Full QFORM: **OPEN**.  
Full-target bounded-density theorem: **NOT PROVED / NOT DISPROVED**.  
Global continuity: **OPEN**.  
Continuity on alternative (C): **PROVED by the cited Fourier-L1 receiver**.

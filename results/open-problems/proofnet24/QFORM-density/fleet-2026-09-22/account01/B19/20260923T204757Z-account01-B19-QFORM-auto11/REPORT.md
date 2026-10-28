SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B19, 2026-09-23T20:47:57Z.
attacking: aggregate the partner two-hub leaf-transverse defects into one literal physical E3 cut, then quantify the surviving no-coloop common-plane collar without deleting the residual.

# account01/B19 — aggregate two-hub leaf-transverse compiler and quantitative common-plane stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL STEP APPLIED; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Full-target continuity: **OPEN**. Continuity is proved only on the physical-E3 payment branch below.

## 1. Fresh frontier and correction boundary


The proof below respects the live corrections. In particular:

- no orthogonal change of the random coordinates is followed by an independence assertion;
- no law-uniform pointwise quadratic-phase decay is used;
- no arbitrary-joint 3D coarea estimate is used;
- no conditional projection-density cap is inferred after conditioning on correlated projected coordinates;
- no small nonzero coefficient is discarded as a small random perturbation;
- the newest `QFORM-B15-NONZERO-SQUARE-AFFINE-SLOPE-RESCUE-FALSE-v1` correction is irrelevant to the proof, and no punctured square-slope estimate is invoked.

### Source-pinned mathematical inputs actually used

1. **Designated partner account02/B19 r36**, commit
   `yspennstate/math-open-problems@85f22101c29c831c4958eef1b2522c78e6966f84`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/B19-20260923T190836Z-r36/REPORT.md`.
   Its Theorem `QFORM-TWOHUB-LEAF-TRANSVERSE-COMPILER-v1` supplies the exact deletion/base-height identity used below.

2. **Marginal-free physical third-volume Fourier theorem**, canonical source
   `yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`, theorem
   `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`.  For every literal original-coordinate cross block `N`, if
   `Z_3=e_3(NN^T)>0`, then
   `||p_Q||_infinity <= C_E3 Z_3^(-1/6)`,
   where
   `C_E3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,
   and the characteristic function is integrable.

3. The earlier Bernoulli aggregate-before-reciprocal principle from account03/B09 r32,
   `QFORM-RANK2-HUBSTAR-AGGREGATE-COMPILER-v1`.  I rederive the needed Bernoulli identity here because the newer marginal-free E3 receiver removes its old hub-leverage gate in the present two-physical-hub setting.

## 2. Partner collar and notation

Use exactly the finite-core rank-two collar of account02/B19 r36. There are disjoint sets of ORIGINAL coordinates

`T={a,b}`, `L`,

with physical two-row cross matrix

`M=A[T,L]`,

`G=MM^T`,

`S=sqrt(det G) > S_0:=1/(480 sqrt(7626))
                 =2.3856699607287348e-5`.                        (2.1)

Let `m_i in R^2` be column `i` of `M`, and define the normalized column leverage

`ell_i=m_i^T G^(-1)m_i`,                                         (2.2)

so

`0<=ell_i<=1`, `sum_i ell_i=2`.                                  (2.3)

Write the completely arbitrary light self block as

`D=A[L,L]`.

For `ell_i<1`, deletion of column `i` leaves the two hub rows independent. Put

`M_-i=M[:,L\{i}]`,
`P_i=projection onto row(M_-i)`,
`r_i=||D[i,L\{i}](I-P_i)||_2`.                                  (2.4)

For an exact coloop `ell_i=1`, put `(1-ell_i)r_i^2:=0`; no value of `r_i` is needed in any formula below.

The partner theorem proves, for the literal three-source/two-hub augmentation

`B_i=A[T union {i}, L\{i}]
    =[M_-i ; D[i,L\{i}]]`,                                       (2.5)

the exact base-height identity

`Gamma_i^2:=e_3(B_i B_i^T)
 =S^2(1-ell_i)r_i^2`.                                            (2.6)

No approximation and no random-coordinate rotation occurs in (2.6).

Define the aggregate transverse resource

`W:=sum_i (1-ell_i)r_i^2`,
`G_*:=sum_i Gamma_i^2=S^2 W`.                                    (2.7)

The partner r36 paid a *single* leaf whenever, for example, `ell_i<=3/4` and `r_i>=1/64`. The point of this run is to pay `W` directly, so a large diffuse collection of tiny `r_i` cannot survive.

## 3. Main theorem — aggregate partner defects compile into one physical E3 cut

### Theorem 3.1 — `QFORM-TWOHUB-LEAF-TRANSVERSE-AGGREGATE-v1`

In the setup of Section 2, for every `W>0`, the full ambient quadratic law has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_E3 (27/256)^(-1/6) (S^2 W)^(-1/6)
 < 15.349 S^(-1/3) W^(-1/6).`                                   (3.1)

All same-bank curvature on `T`, all of `D`, every outside quadratic block/coupling, all signs and degeneracies, and arbitrary affine terms are retained. The input coordinates need only be independent with one-dimensional densities bounded by one.

### Proof

For each `i`, Cauchy--Binet expands (2.6) as

`Gamma_i^2
 =sum_{C subset L\{i}, |C|=3}
   det A[T union {i}, C]^2`.                                     (3.2)

Randomly put each leaf coordinate into a source set `I` with probability `p=1/4`, independently, and let

`J=L\I`.

The two physical hubs `T` are always kept on the source side. For a fixed term in (3.2), with leaf source `i` and receiver triple `C`, that literal minor occurs in the physical cross block

`N_I=A[T union I,J]`                                             (3.3)

whenever

`i in I` and `C subset J`.

The probability is

`p(1-p)^3=(1/4)(3/4)^3=27/256`.                                  (3.4)

Let `Z_sel(I)` be the sum of exactly these selected squared minors. Linearity of expectation gives

`E_I Z_sel(I)
 =(27/256) sum_i Gamma_i^2
 =(27/256) S^2 W`.                                                (3.5)

Hence one actual ORIGINAL-coordinate cut satisfies

`Z_sel(I)>=(27/256)S^2W`.                                        (3.6)

Every selected minor is a genuine `3x3` minor of `N_I`, so

`e_3(N_I N_I^T)>=Z_sel(I)>=(27/256)S^2W`.                        (3.7)

Now apply the completed marginal-free physical-E3 Fourier theorem to the literal cut `(T union I)|J`. It retains every same-side quadratic term and every outside coupling, and gives

`||p_Q||_infinity
 <= C_E3 e_3(N_I N_I^T)^(-1/6)
 <= C_E3(27/256)^(-1/6)(S^2W)^(-1/6)`,                           (3.8)

which is (3.1). The source theorem also gives `phi_Q in L^1`, hence a continuous `C_0` density. QED.

### What is new relative to the partner theorem

The partner's pointwise leaf theorem can leave `r_i` small for every `i` while the sum of their squared transverse contributions is order one. Theorem 3.1 eliminates that possibility. It also has **no hub-row leverage hypothesis**: the later marginal-free E3 theorem pays the literal cut after the Bernoulli compiler.

## 4. Live quantitative payment

Fix

`theta:=2^(-20)`.                                                 (4.1)

If

`W>=theta`,                                                       (4.2)

then (2.1) and (3.1) give

`e_3(N_I N_I^T)
 >=(27/256)S_0^2 2^(-20)
 =5.724592930120713e-17`,                                        (4.3)

and therefore

`boxed: ||p_Q||_infinity < 5374.054 < 5375.}`                    (4.4)

This branch has a continuous `C_0` density.

Thus every still-unpaid two-hub collar state may now assume

`boxed: W<2^(-20).}`                                             (4.5)

Let

`J_0={i in L: ell_i<=3/4}`,
`H_0=L\J_0`.                                                      (4.6)

Since `sum ell_i=2`,

`boxed: |H_0|<=2.}`                                               (4.7)

For every `i in J_0`, `1-ell_i>=1/4`, so (4.5) yields the dimension-free aggregate estimate

`sum_{i in J_0} r_i^2
 <=4W
 <2^(-18)`,                                                      (4.8)

or equivalently

`boxed:
 (sum_{i in J_0}r_i^2)^(1/2)<2^(-9)=1/512.}`                    (4.9)

This is strictly stronger than a rowwise `r_i<1/64` conclusion: it gives one Frobenius-scale collar independent of the number of light coordinates, outside at most two physical high-leverage leaves.

## 5. Quantitative no-coloop/common-plane stability on the low-leverage leaves

The aggregate estimate (4.9) can be converted into a deterministic stability version of the partner's exact common-plane classification whenever the remaining normalized frame is not itself near a coloop.

Normalize the two-row frame by

`V=G^(-1/2)M`,                                                    (5.1)

so its columns `v_i` satisfy

`sum_i v_i v_i^T=I_2`, `||v_i||^2=ell_i`.                        (5.2)

This is only a deterministic coefficient normalization; the random variables are unchanged. Put

`V_0=V[:,J_0]`,
`mu=lambda_min(V_0 V_0^T)`.                                      (5.3)

### Theorem 5.1 — `QFORM-TWOHUB-AGGREGATE-COMMONPLANE-STABILITY-v1`

Assume (4.5) and

`mu>=1/4`.                                                        (5.4)

Then there exist a diagonal matrix `Delta_0` on the physical coordinates `J_0` and a symmetric real `2x2` matrix `K` such that

`boxed:
 ||D[J_0,J_0]-Delta_0-V_0^T K V_0||_F
 <15/512
 =0.029296875.}`                                                 (5.5)

No entry of the residual in (5.5) is deleted in any probabilistic argument; (5.5) is a coefficient-geometry statement only.

### Proof

For each `i in J_0`, choose a least-squares coefficient row `a_i in R^2` in (2.4), after the deterministic normalization (5.1). Restrict its residual from `L\{i}` to `J_0\{i}`. Form the matrix `A_0` whose `i`-th row is `a_i^T`, and define an off-diagonal error matrix `R` on `J_0` by

`R_ij=D_ij-a_i^T v_j` for `i!=j`, `R_ii=0`.                      (5.6)

Then by (4.8)

`||R||_F^2<=sum_{i in J_0}r_i^2=:eps^2`,
`eps<1/512`.                                                      (5.7)

Because `D[J_0,J_0]` is symmetric,

`A_0 V_0-(A_0V_0)^T=R^T-R`,                                      (5.8)

and hence

`||A_0V_0-V_0^T A_0^T||_F<=2eps`.                               (5.9)

Let

`P=V_0^T(V_0V_0^T)^(-1)V_0`                                    (5.10)

be the orthogonal projection onto `col(V_0^T)`, and write

`A_0=A_parallel+A_perp`,
`A_parallel=P A_0=V_0^T K_0`,
`K_0=(V_0V_0^T)^(-1)V_0A_0`.                                    (5.11)

Multiplying (5.8) on the left by `I-P` removes the second term and gives

`||A_perp V_0||_F<=2eps`.                                        (5.12)

Since `V_0V_0^T>=mu I`,

`||A_perp||_F<=2eps/sqrt(mu)`.                                   (5.13)

The skew part of `A_parallel V_0` is bounded by

`||V_0^T(K_0-K_0^T)V_0||_F
 <=2eps+2||A_perp V_0||_F
 <=6eps`.                                                        (5.14)

Again using `V_0V_0^T>=mu I`,

`||K_0-K_0^T||_F<=6eps/mu`.                                      (5.15)

Put

`K=(K_0+K_0^T)/2`.                                               (5.16)

Finally choose the diagonal `Delta_0` so that the diagonal entries of

`D[J_0,J_0]-Delta_0-A_0V_0`

vanish. From (5.6), (5.12) and (5.15), using `||V_0||op<=1`,

`||D[J_0,J_0]-Delta_0-V_0^TKV_0||_F
 <= ||R||_F+||A_perp V_0||_F
    +||V_0^T(K_0-K)V_0||_F`
` <= eps+2eps+3eps/mu`
` <=15eps<15/512`,                                               (5.17)

where the final inequality uses `mu>=1/4`. QED.

### The complementary frame branch

If (5.4) fails, then

`lambda_max(sum_{h in H_0} v_hv_h^T)
 =lambda_max(I_2-V_0V_0^T)>3/4`.                                 (5.18)

Together with `|H_0|<=2`, this says the normalized two-hub frame has more than three quarters of its energy in some coefficient direction carried by at most two literal physical leaves. Thus the complement of Theorem 5.1 is a quantitative one- or two-leaf **near-coloop/finite-anchor** branch, not an unstructured high-dimensional leaf bank.

Equations (4.9), (5.5), and (5.18) give the new exhaustive structural output:

1. the density is paid by `<5375`; or
2. at most two physical leaves carry the near-coloop frame concentration; or
3. off those leaves, the complete self-curvature is within Frobenius `15/512` of `diagonal + same two-dimensional common plane`.

The residual in alternative 3 remains present exactly in the ambient quadratic form.

## 6. Compact conditional full-proof assembly

The current proof graph can be stated without claiming completion.

- The existing global reductions pay target-scale physical third-cross-volume and several diffuse/rank-five branches by integrated Fourier.
- In the finite-core rank-two branch, account03/B19 r38 selects a literal two-row cross packet and pays transverse `H-to-L` Frobenius height at scale `1/64`.
- Account02/B19 r36 then gives the exact leaf-transverse currencies `Gamma_i^2=S^2(1-ell_i)r_i^2` and classifies the exact zero-height endpoint.
- **This run pays their entire aggregate** whenever `W>=2^-20`, with a continuous density bound `<5375`, and otherwise replaces infinitely many separate small-height constraints by the single dimension-free Frobenius collar (4.9).
- In the non-near-coloop part of that collar, Theorem 5.1 forces the low-leverage light self-block into `diagonal + common two-plane + an explicitly retained Frobenius-small coefficient residual`.
- The exact-coloop alternatives of account02/B19 remain finite physical star packets; the nonexact complement is now quantitatively the near-coloop branch (5.18).

This is a conditional compiler, not an end-to-end proof. Other globally recorded rank-one/overlap branches remain as in the current fleet graph.

## 7. First essential missing implication

The first local debt after this run is

`QFORM-TWOHUB-NEARCOMMONPLANE-WITH-RETAINED-RESIDUAL-v1`:

> In the two-hub collar, assume `W<2^-20`. Either spend the at-most-two physical near-coloop leaves from (5.18), or, in the `mu>=1/4` chamber, combine the exact same-plane/diagonal two-hub structure with the retained coefficient residual `E` satisfying `||E||_F<15/512`, **without** treating `E` as a small random perturbation and without replacing any product bank by an arbitrary dependent joint density.

A valid successor must be uniform as the nonzero residual tends to zero. The exact partner endpoint and the moving-ridge correction show why simply setting that residual to zero is not acceptable.

## 8. Continuity ledger

- Theorem 3.1 / the quantitative `W>=2^-20` branch: **continuous `C_0` density**, because the invoked physical-E3 theorem has `phi_Q in L^1`.
- The structural collar (4.9), stability theorem (5.5), and near-coloop alternative (5.18): coefficient statements only; **no continuity claim**.
- Unrestricted theorem continuity: **OPEN**.

## 9. Numerical constants

All constants are direct evaluations of exact formulas:

`S_0=1/(480 sqrt(7626))=2.3856699607287348e-5`,

`C_E3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,

`C_E3(256/27)^(1/6)=15.348718100234715...`,

`(27/256) S_0^2 2^(-20)=5.724592930120713e-17`,

and the resulting density bound is

`5374.053363485854... <5375`.

The derivation is exact linear algebra, Cauchy--Binet, Bernoulli averaging, and the source-pinned Fourier theorem; the decimals are only bookkeeping.

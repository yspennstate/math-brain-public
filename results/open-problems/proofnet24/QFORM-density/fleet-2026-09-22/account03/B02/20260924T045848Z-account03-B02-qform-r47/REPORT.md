SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-24T04:58:48Z.
attacking: raise the diffuse spectral-window scale to 1/19 with an exact MSS/ridge calculation, strengthen the physical-hub alternative, and feed that stronger hub into the live near-rank-two carrier alignment without deleting any quadratic tail.

# account03/B02 r47 — 1/19 spectral-window Fourier theorem and strengthened physical-hub funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **NEW SUPPORTING FOURIER/STRUCTURAL THEOREM; FULL QFORM OPEN; TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moments, compact/connected support, iid assumption, post-rotation independence, arbitrary-joint coarea estimate, conditional projection-density cap, or deletion of a small nonzero quadratic term is used.

## 1. Source-pinned inputs actually used

### 1.1 Parametric ridge-leverage theorem

The complete free-regularizer and spectral-window proof is

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

Its exact ridge criterion says: for a literal ORIGINAL-coordinate cross block `B=A[I,J]`, `gamma>0`,

`K_gamma=B B^T (gamma^2 I+B B^T)^(-1)`, `theta=tr K_gamma`,

if `max_i (K_gamma)_ii<=1/2` and `theta>2`, then the full ambient quadratic form has a continuous `C0` density. In particular, if `B` has three singular values at least `sigma>0`, set `gamma=sigma/sqrt(6)`; then `theta>=18/7`, and the theorem gives

`||p_Q||inf <= 9 sqrt(3e)/(2 sigma)`,                              (1.1)

and, from the same integrable Fourier envelope,

`integral_R |phi_Q(t)|dt <= 9 pi sqrt(3e)/sigma`.                 (1.2)

The same source proves the perturbative ridge-leverage bound: if `B=B0+F`, `||F||op<=eta`, and the projection onto `range(B0)` has diagonal at most `ell`, then

`max_i(K_gamma)_ii <= (sqrt(ell)+eta/gamma)^2`.                    (1.3)

All same-bank blocks and all additional spectral directions remain in the full quadratic form.

### 1.2 Live B02 near-rank-two packet

Immediate completed predecessor:

`yspennstate/math-open-problems@969923934518c728e4611e670ab6244ceea30215`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T030004Z-account03-B02-qform-r45/REPORT.md`.

On its live literal full physical cut `N=A[L,R]`, `L union R=[n]`, the squared singular values satisfy

`x1*x2 > kappa :=247/576`.                                        (1.4)

The r45 physical-E3 and fixed-V1 exits remain available. Its low-transverse endpoint previously used the spectral window `|lambda|>=1/64` and obtained only the physical-hub scale `1/512`; the present theorem replaces that endpoint by a stronger global dichotomy.

The physical-E3 receiver used below is the completed marginal-free theorem source-pinned by r45:

`E3(B)>0 => ||p_Q||inf <= C3 E3(B)^(-1/6)`,

`integral |phi_Q| <=2*pi*C3 E3(B)^(-1/6)`,

`C3=10.345083232147514...`,                                      (1.5)

for every literal disjoint ORIGINAL-coordinate cross block `B`, with a continuous `C0` density.

### 1.3 Designated partner account04/B02

The completed designated partner theorem is

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

On its exact scope, a nonsingular physical principal triple `H0` with a zero diagonal entry gives

`integral_R |phi_Q(t)|^2 dt <= 6*pi*2^(2/3)|det H0|^(-1/3)`.      (1.6)

The theorem also proves continuity in that zero-diagonal-triple branch, but only its quantitative `L2` Fourier credit is used in Section 5.

## 2. Parametric spectral-window compiler

The fixed constants in the published ridge-window theorem are not intrinsic. Keeping its calculation symbolic gives the following statement.

### Theorem 2.1 — `QFORM-PARAMETRIC-SPECTRAL-WINDOW-L1-v1`

Let `0<eta<1`, let

`P_eta = 1_{|A|>=eta}`,

and assume

`max_i (P_eta)_ii <= eps`.                                        (2.1)

Define

`delta = 1-(1/sqrt(2)+sqrt(eps))^2
       = 1/2-eps-sqrt(2 eps)`.                                    (2.2)

Suppose `delta>eta`, and put `sigma=delta-eta`. If

`( sqrt(eps/delta) + sqrt(6)*eta/sigma )^2 < 1/2,`                (2.3)

then every target-law input has

`boxed: ||p_Q||inf <= 9 sqrt(3e)/(2 sigma),`                       (2.4)

`boxed: integral_R |phi_Q(t)|dt <= 9*pi*sqrt(3e)/sigma,`           (2.5)

and `p_Q` is continuous and vanishes at infinity.

#### Proof

Write `A=A_H+E`, where `A_H=P_eta A P_eta=U Lambda U^T` is the spectral truncation and `||E||op<eta`. Every row `u_i` of the physical-coordinate frame `U` obeys `||u_i||^2<=eps`.

Apply the two-part Marcus-Spielman-Srivastava frame partition used in the source theorem. There is a physical partition `I,J` for which both partial frame Gram matrices satisfy

`delta I <= U_I^T U_I, U_J^T U_J <=(1-delta)I`.                  (2.6)

The target condition gives at least three singular values of `Lambda` at least one. Hence for

`B0=A_H[I,J]=U_I Lambda U_J^T`,

` s3(B0)>=delta`.                                                  (2.7)

For the full physical cross block `B=A[I,J]=B0+E[I,J]`, Weyl gives

`s3(B)>=sigma=delta-eta`.                                         (2.8)

Moreover `range(B0)=range(U_I)`, and its physical leverage obeys

`max_i (P_range(B0))_ii
 <= eps/delta`.                                                    (2.9)

Set `gamma=sigma/sqrt(6)`. Equation (1.3), (2.9), and `||E[I,J]||op<=eta` give

`max_i(K_gamma)_ii
 <=(sqrt(eps/delta)+sqrt(6)eta/sigma)^2<1/2`.                    (2.10)

The three singular values in (2.8) give `theta_gamma>=18/7>2`; therefore the exact ridge theorem (1.1)-(1.2) applies. This proves (2.4)-(2.5), retaining the entire matrix `A`. QED.

No random coordinate is rotated in this argument. The frame/spectral rotations occur only in coefficient algebra, and the Fourier theorem is applied after a literal ORIGINAL-coordinate partition has been produced.

## 3. A stronger exact window: eta=1/19, eps=1/72

Take

`eta=1/19`, `eps=1/72`.                                           (3.1)

Then the MSS lower frame bound is exactly

`delta=1/2-1/72-1/6=23/72`,                                      (3.2)

so

`sigma=23/72-1/19=365/1368=0.266812865497...`.                   (3.3)

Also

`eps/delta=1/23`.                                                  (3.4)

The ridge-leverage term is

`L_*=(1/sqrt(23)+72 sqrt(6)/365)^2
    =0.478450870770... <1/2`.                                    (3.5)

For a purely rational certificate of the strict inequality,

`1/sqrt(23)<21/100`, because `441*23>10000`,

`sqrt(6)<49/20`, because `(49/20)^2>6`,

hence

`1/sqrt(23)+72sqrt(6)/365
 <21/100+882/1825
 =5061/7300`,                                                     (3.6)

and

`2*5061^2=51227442 <53290000=7300^2`.                             (3.7)

Thus (2.3) holds with room to spare.

### Corollary 3.1 — `QFORM-1OVER19-SPECTRAL-WINDOW-L1-v1`

If

`boxed: max_i (P_{1/19})_ii <=1/72,`                              (3.8)

then the full ambient target law has a continuous `C0` density and

`boxed: ||p_Q||inf
 <= (6156/365)sqrt(3e)
 =48.1630093577... ,}`                                            (3.9)

`boxed: integral_R |phi_Q(t)|dt
 <= (12312*pi/365)sqrt(3e)
 =302.617112746... .}`                                            (3.10)

This strictly raises the spectral cutoff compared with the previous `1/64` theorem. It does not assume that the remaining spectrum vanishes; every eigenvalue below `1/19`, of either sign and arbitrary multiplicity, stays in the phase.

## 4. Exact global diffuse-or-strong-physical-hub dichotomy

If (3.8) fails, choose an ORIGINAL coordinate `i` with `(P_{1/19})_ii>1/72`. Then

`||A e_i||_2^2=(A^2)_ii
 >=(1/19)^2 (P_{1/19})_ii
 >1/(19^2*72).`                                                   (4.1)

But

`||Ae_i||_2^2=A_ii^2+||A[i,i^c]||_2^2`.                           (4.2)

Since

`2*(1/228)^2 =1/(19^2*72)`,                                      (4.3)

strict inequality in (4.1) implies the literal physical certificate

`boxed: |A_ii|>1/228  OR  ||A[i,i^c]||_2>1/228.`                 (4.4)

Therefore every target matrix satisfies the dimension-free exhaustive dichotomy:

1. **diffuse high spectral window:** (3.8) holds, and (3.9)-(3.10) pay the full law by genuine Fourier `L1`; or
2. **strong physical hub:** an original coordinate satisfies (4.4).

This does **not** solve the full conjecture: the strong physical-hub alternative is not automatically a bounded-density receiver, and the live correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` forbids that shortcut. The value is that the hub scale is now a fixed `1/228`, with no low-rank assumption.

## 5. Apply the stronger hub to the live r45 near-rank-two packet

Return to the literal full cut `N=A[L,R]` from (1.4). Suppose the diffuse window branch is not already paid. If the strong certificate (4.4) is diagonal, retain

`boxed: |A_ii|>1/228.`                                           (5.1)

Now suppose instead

`||A[i,i^c]||_2>a0`, `a0:=1/228`.                                (5.2)

Assume `i in L`; the `i in R` statement is symmetric. Let `u1,u2` and `v1,v2` be the top-two left/right singular vectors of `N`. Put

`ell_i=u1(i)^2+u2(i)^2`,

`q_i=||N[i,:](I-P_{span(v1,v2)})||_2`,                            (5.3)

`b_i=A[L\{i},i]`,

`d_i=dist(b_i,span(u1^(-i),u2^(-i))).`                           (5.4)

Set

`delta0=a0/2=1/456`.                                               (5.5)

The punctured exterior identity, proved by Cauchy-Binet exactly as in r45, gives

`W_i >= x1*x2(1-ell_i)d_i^2`,                                    (5.6)

where a fair physical Bernoulli split converts `W_i` into a literal physical cross block with `E3>=W_i/16`.

There are now four exhaustive alternatives.

### (A) residual crossing row is substantial

If `q_i>=delta0`, then

`E3(N)>=x1*x2 sum_(j>=3)x_j
      >=x1*x2 q_i^2
      > kappa delta0^2
      =247/119771136
      =2.06226648798e-6.`                                        (5.7)

By (1.5),

`boxed: ||p_Q||inf<91.694479954,`                                 (5.8)

`boxed: integral |phi_Q|<576.133409196.`                          (5.9)

### (B) punctured same-bank curvature is substantial

If `ell_i<=3/4` and `d_i>=delta0`, then (5.6) and the `1/16` physical split give a literal cross block `B_i` with

`E3(B_i)> kappa delta0^2/64
        =247/7665352704
        =3.22229138747e-8.`                                      (5.10)

Hence

`boxed: ||p_Q||inf<183.388959908,`                                (5.11)

`boxed: integral |phi_Q|<1152.26681840.`                          (5.12)

Both (A) and (B) have continuous `C0` densities.

### (C) near-coloop

If

`ell_i>3/4`,                                                       (5.13)

retain that literal top-two near-coloop. Since `sum_i ell_i=2`, there are at most two such coordinates on each side of the full cut, hence at most four total.

### (D) carrier-aligned strong hub

Assume none of (A)-(C). Decompose the off-diagonal physical row into three mutually orthogonal coefficient pieces:

- the top-two right-singular-plane part of `N[i,:]`;
- the projection of `b_i` onto the punctured top-two left plane;
- the two residual pieces of norms `q_i` and `d_i`.

Let `g_i` be the Euclidean norm of the first two aligned pieces. Then exactly

`||A[i,i^c]||_2^2=g_i^2+d_i^2+q_i^2`.                            (5.14)

Since `d_i,q_i<delta0=a0/2` and (5.2) is strict,

`g_i^2>a0^2-2delta0^2=a0^2/2`.                                   (5.15)

Therefore

`boxed: g_i>1/(228 sqrt(2))
             =0.00310134553152... .}`                             (5.16)

This is more than twice the previous carrier-aligned scale `1/(512sqrt(2))`. No small singular tail is dropped; the decomposition is an exact coefficient identity.

### Updated unpaid list on the r45 survivor

After the already-paid physical-E3 and diffuse-window exits, the remaining branches are now only:

1. the fixed overlap-one `V1` grouped-pivot packet inherited from r45;
2. a physical diagonal `|A_ii|>1/228`;
3. a carrier-aligned off-diagonal hub `g_i>1/(228sqrt(2))`;
4. at most four top-two near-coloop coordinates.

Everything else in this fork is paid by genuine unweighted Fourier `L1`.

## 6. Equation-level application of designated partner account04/B02

On the exact overlap with a nonsingular zero-diagonal physical triple `H0`, apply the partner estimate (1.6) together with the completed physical-E3 `|t|^{-3/2}` tail. The optimized head/tail split, already proved in r45, is

`||p_Q||inf
 <=2^(8/3) 3^(1/4) e^(1/4)
   |det H0|^(-1/12) E3(B)^(-1/8).`                               (6.1)

This is an actual use of the partner's `L2` Fourier credit, not a citation-only dependency.

At the new stronger E3 threshold (5.7),

`boxed: ||p_Q||inf
 <55.119781993 |det H0|^(-1/12).}`                                (6.2)

At the punctured-curvature threshold (5.10),

`boxed: ||p_Q||inf
 <92.700054174 |det H0|^(-1/12).}`                                (6.3)

Continuity on these overlaps comes from the genuine physical-E3 Fourier-`L1` receiver (and independently from the partner zero-diagonal theorem on its scope); no continuity inference is made from `L2` alone.

## 7. What changed and what remains

The substantive new implication is not a re-run of the old `1/64` spectral-window theorem. The exact free-parameter calculation raises the retained spectral cutoff to `1/19` under leverage cap `1/72`, yielding the global alternative

`continuous C0 density with ||p_Q||inf<48.164 and integral|phi_Q|<302.618`

**or**

`an ORIGINAL physical diagonal/off-diagonal row larger than 1/228`.

Feeding that stronger literal hub back into the live balanced near-rank-two packet improves both E3 payment thresholds and the carrier-aligned residual scale. The full unrestricted QFORM conjecture nevertheless remains **OPEN**. Full-target continuity remains **OPEN**. A universal target-wide unweighted `integral |phi_Q|` bound remains **OPEN / not refuted**; no source-valid exact-target counterexample was found this run.

The first B02 edge is now

`QFORM-FIXEDSCALE-V1-PIVOT-OR-STRONGHUB-L1-v1`:

pay the remaining fixed overlap-one grouped-pivot packet, physical diagonal `>1/228`, carrier-aligned hub `>1/(228sqrt(2))`, and at-most-four near-coloops by coupling them to the robust rank-two crossing without using the refuted one-heavy-row absorption shortcut.

## 8. Correction boundary

This report does not use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, fiber-sup integration, positive conditional projection-height moments, a one-good-minor theorem, coefficient-smallness as a probabilistic perturbation, or the one-heavy-row same-square absorption shortcut. All Fourier `L1` conclusions arise from the completed ridge or literal physical-E3 receivers. The `V1` grouped-pivot and strong-hub branches are explicitly left unpaid rather than silently declared solved.

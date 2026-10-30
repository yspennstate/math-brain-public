SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-24T04:40:09Z.
attacking: the r46 balanced kernel-star energy — test the first missing E3 implication, then replace it by a support-graph matching-or-hub compiler that keeps the full determinant weights.

# fleet03/B07 r47 — balanced kernel-star energy: exact obstruction and matching/low-rank compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW TARGET-VALID CORRECTION + NEW DIMENSION-FREE MATCHING/LOW-RANK ROUTER / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, moment, log-concavity, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea, fiber supremum, or deletion of a small nonzero coefficient is used. The only rotated vectors below are deterministic coefficient vectors used for matrix inequalities; no rotated random coordinates are declared independent.

## 1. Fresh source state and incoming debt


The immediate source is r46, authoritative scope addendum

`yspennstate/math-open-problems@43eab33dc9cd6063c84089b5fc3692abceeadb21`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260924T033639Z-fleet03-B07-qform-r46/PREPUBLICATION_ADDENDUM.md`.

In the rank-one part of the r40 overlap-two packet, each physical pair `K` carries

`r_K := (L_K R_K/S_K)^2`,

where `L_K,R_K` are the two fixed-bank kernel-star norms and

`S_K=||A[K,K^c]^T v_K||_2 >= sqrt(L_K^2+R_K^2)`.

After the completed exact rank-one-pair receiver is spent at scale `delta=2^-10`, every unpaid instance obeys

`R := sum_K r_K >2048`.                                             (1.1)

At slab ratio `rho`, r46 gives the stronger asymptotic version

`R > rho^4/524288`.                                                (1.2)

The analytic third-volume receiver used below is fleet02/B03,

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T184716Z-fleet02-B03-QFORM-auto11/REPORT.md`, theorem `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`. For any literal original-coordinate cross block `C` with

`Z3=e_3(CC^T)>0`,

it retains arbitrary same-side quadratic blocks, affine terms and additional spectrum and gives

`||p_Q||_infinity <= C3 Z3^(-1/6)`,
`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`; the source proof has an integrable Fourier envelope, hence a continuous density in this branch.

The designated partner used below is fleet04/B07,

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`.

Its `r=0` coordinate-core gate says that three literal physical coordinates with diagonal magnitudes at least `1/64` and mutual off-diagonal magnitudes at most `1/768` form a principal block with `s_3>=3/256`, giving the full ambient essential-density bound

`||p_Q||_infinity <=1283.393676611072...`.                         (1.3)

Continuity is not claimed by that partner gate.

## 2. First essential implication tested early: normalized energy does NOT force E3

The natural next conjecture after r46 was that the large aggregate (1.1) itself should force one literal physical rank-three crossing. This is false, even inside the exact owner target and even while every individual rank-one-pair receiver remains below the r46 payment threshold.

### Proposition 2.1 — `QFORM-BALANCED-KERNEL-ENERGY-NO-E3-FORCING-v1`

Let `epsilon=2^-12` and `m=2^41`. Use literal original-coordinate banks

`{h0} disjoint H' disjoint {p,q}`, `|H'|=m`.

Put

`A_h0,h0=1`,
`A_kp=A_kq=epsilon` for every `k in H'`,

and set every other entry to zero, with symmetry understood. Equivalently

`A=e_h0 e_h0^T + r s^T+s r^T`,

where `r=1_H'` and `s=epsilon(e_p+e_q)` have disjoint supports.

Then:

1. The spectrum is exactly

   `{1,+epsilon sqrt(2m),-epsilon sqrt(2m),0,...}
    ={1,+512,-512,0,...}`.                                       (2.1)

   Hence this is a valid target matrix with three eigenvalues of modulus at least one.

2. For every `k in H'`, the physical pair `K={h0,k}` has principal block `diag(1,0)`, so it is rank one with nonzero eigenvalue `lambda_K=1` and kernel vector `v_K=e_k`. Taking the r40 banks `I={p}`, `J={q}` gives

   `L_K=R_K=epsilon`, `S_K=sqrt(2)epsilon`.                       (2.2)

   Thus every individual pair scale is

   `|lambda_K|S_K=sqrt(2)2^-12<2^-10`,                            (2.3)

   while the original determinant-weighted packet and the r46 normalized packet are

   `sum lambda_K^2L_K^2R_K^2 =m epsilon^4=1/128>1/512`,           (2.4)

   `sum (L_KR_K/S_K)^2 =m epsilon^2/2=65536>2048`.                (2.5)

3. Nevertheless **every literal physical coordinate crossing has rank at most two**. Indeed the isolated diagonal term `e_h0 e_h0^T` has zero cross block for every cut, while the bipartite part restricts on any cut `U|U^c` as

   `r_U s_Uc^T+s_U r_Uc^T`,                                      (2.6)

   a sum of two rank-one matrices. Therefore

   `e_3(A[U,U^c]A[U,U^c]^T)=0` for every physical cut.            (2.7)

So (1.1), even together with the exact r40 rank-one packet and the r46 pair-scale failure, cannot by itself imply a positive physical `Z3`. This proposition is a correction to that proposed intermediate route, **not a counterexample to QFORM**.

The obstruction is informative: the entire residual support graph is one enormous hub star, and the kernel-star images all occupy the same two-bank rank-one direction.

## 3. Correct replacement: bounded support degree gives a large pair-disjoint matching

Let `G` be the simple support graph on the physical anchor bank `H`: an edge is a rank-one pair `K` with `r_K>0`, weighted by `r_K`. Fix an integer `D>=1`.

### Lemma 3.1 — weighted matching from bounded support degree

If `Delta(G)<=D`, the edges can be partitioned into at most `2D-1` matchings, hence one matching `M` satisfies

`sum_{K in M} r_K >= R/(2D-1)`.                                  (3.1)

Proof: greedily color the edges. When coloring an edge, at most `2D-2` colors occur on edges adjacent to one of its endpoints, so one of `2D-1` colors is available. Each color class is a matching. Summing their weights gives (3.1). No maximum individual determinant is selected.

Instantiate `D=16`. From (1.1), either

`Delta(G)>=17`,                                                    (3.2)

or there is a pair-disjoint matching `M` with

`R_M:=sum_{K in M}r_K >2048/31`.                                 (3.3)

This is the first dimension-free support split forced by the normalized bank currency.

## 4. A pair-disjoint matching becomes one physical crossing before any inversion

Assume the matching branch (3.3). For each `K in M`, embed its unit physical-pair kernel `v_K` into `R^H`; call that vector `g_K`. Because the pairs in `M` are disjoint, the `g_K` are orthonormal. Let `G_M` be the matrix with these columns.

Use the one literal physical crossing

`C=A[I union J,H]`                                                 (4.1)

and define only for deterministic matrix bookkeeping

`W=C G_M`.                                                        (4.2)

Its column indexed by `K` is the kernel-star image restricted to the two r40 banks, so

`||W_K||_2^2=L_K^2+R_K^2`.                                       (4.3)

Since `S_K^2>=L_K^2+R_K^2`,

`r_K=L_K^2R_K^2/S_K^2
 <=L_K^2R_K^2/(L_K^2+R_K^2)
 <=(L_K^2+R_K^2)/4`.                                              (4.4)

Therefore

`T:=||W||_F^2 >=4R_M >8192/31=264.2580645... .`                  (4.5)

The key point is that the deterministic pair-kernel compression cannot manufacture third exterior volume. Since `G_M^T G_M=I`, `wedge^3 G_M` is an isometry. For the PSD matrix `C^T C`, trace of its compression on `wedge^3 range(G_M)` is at most the full trace. Hence

`boxed: e_3(WW^T)<=e_3(CC^T).`                                   (4.6)

Thus the entire matched determinant bank has been transferred to **one literal physical original-coordinate crossing** before any analytic payment.

If

`e_3(WW^T)>=1/64`,                                                (4.7)

then the physical crossing `C` also has `Z3>=1/64`. The completed fleet02/B03 receiver gives the full ambient form a **continuous** density with

`boxed: ||p_Q||_infinity <=2 C3
 =21.1003376623296... .`                                         (4.8)

## 5. If the matching does not pay, its kernel-star image is quantitatively low rank

It remains to interpret

`e_3(WW^T)<1/64`                                                   (5.1)

under the large trace (4.5). Let `x_1>=x_2>=...>=0` be the squared singular values of `W`, and write

`Z=e_2(x)`, `V=e_3(x)`, `T=sum x_i`.

### Lemma 5.1 — second-compound Newton localization

If `Z>0`, set

`alpha_i=x_i(T-x_i)/Z`.

Then `sum alpha_i=2`. Hence the spectral projection `P` generated by `alpha_i>2/3` has rank at most two. The second Newton transform has eigenvalues

`Z(1-alpha_i)`,

so

`H_2>= (Z/3)(I-P)` on the complement. Newton's identity gives

`tr((WW^T)H_2)=3V`.

Consequently

`dist_F(W,rank<=2)^2
 <=tr((I-P)WW^T)
 <=9V/Z`.                                                        (5.2)

This is a deterministic matrix statement; it does not rotate the random input law.

Now split at `Z=4`.

* If `Z>=4`, (5.1)-(5.2) give

  `boxed: dist_F(W,rank<=2)<3/16=0.1875.`                         (5.3)

* If `Z<4`, use

  `T^2=sum x_i^2+2Z <=x_1T+2Z`.

  Therefore the rank-one squared tail satisfies

  `T-x_1 <=2Z/T <8/T <31/1024`,                                  (5.4)

  using (4.5), and hence

  `boxed: dist_F(W,rank<=1)<sqrt(31)/32
  =0.1739926363... .`                                            (5.5)

Combining Sections 3--5 proves the new router.

### Theorem 5.2 — `QFORM-BALANCED-ENERGY-MATCHING-OR-HUB-v1`

For every unpaid r46 rank-one packet satisfying `R>2048`, at least one of the following holds:

1. the residual support graph has a physical vertex of degree at least `17`;
2. the full ambient form has a **continuous** density bounded by `21.100337663` through a literal physical `Z3>=1/64` crossing;
3. a pair-disjoint matching carrying `>2048/31` normalized determinant weight has kernel-star image `W` with `dist_F(W,rank<=2)<3/16`;
4. such a matching has `dist_F(W,rank<=1)<sqrt(31)/32`.

No term of the determinant packet was divided by a tiny coordinate minor. The r46 obstruction in Proposition 2.1 lands exactly in branch 1, so the theorem is sharp at the level of mechanism: a hub branch cannot simply be omitted.

The same proof has a slab-ratio version: replace `2048` everywhere by `rho^4/524288`. For bounded support degree, the matched Frobenius energy then grows like `rho^4` unless an analytic `Z3` payment occurs.

## 6. The high-degree hub has its own exact physical third-volume identity

The hub branch is not left as a label. Fix a physical hub `h` and incident rank-one pairs `K={h,k}`. On the fixed column bank `I union J`, write

`a=A[h,I union J]`.

If the pair-kernel vector in the physical basis `(h,k)` is `(alpha_k,beta_k)`, define its actual kernel-star row

`z_k=alpha_k a+beta_k A[k,I union J]`.                             (6.1)

For distinct neighbors `k,l`, exterior multilinearity gives exactly

`a wedge z_k wedge z_l
 =beta_k beta_l\, a wedge A[k,I union J] wedge A[l,I union J]`.   (6.2)

Since `|beta_k beta_l|<=1`, summing the squared coordinate minors yields

`boxed:
 e_3(A[{h} union N,I union J]A[{h} union N,I union J]^T)
 >= sum_{k<l}||a wedge z_k wedge z_l||^2.
}`                                                                (6.3)

If `a!=0`, decompose `z_k=gamma_k a+c_k` with `c_k perpendicular a`. Then the right side is exactly

`||a||^2 e_2(CC^T)`,                                              (6.4)

where the rows of `C` are the `c_k`. Thus failure of physical E3 at a high-degree hub forces either a small physical hub star `||a||`, or a quantitatively low-two-volume family of projected kernel-star rows. Proposition 2.1 has `a=0`, demonstrating the genuine endpoint of this identity.

This is the next useful deterministic currency for the hub obstruction; no independence is attached to the vectors `z_k`.

## 7. Required application of fleet04/B07 on the high-degree branch

Suppose branch 1 of Theorem 5.2 occurs at a hub `h` with at least 17 distinct neighbors. Let

`N_hi={k: |A_kk|>=1/64}`.

If `N_hi` contains three vertices `k_1,k_2,k_3` whose three mutual physical edges obey

`|A_kikj|<=1/768`,                                                 (7.1)

the designated fleet04/B07 theorem applies to the literal principal triple `T={k_1,k_2,k_3}` and gives

`s_3(A[T,T])>=3/256`,                                              (7.2)

hence the complete ambient essential-density payment (1.3).

Therefore any **unpaid** degree-17 hub satisfies an explicit complementary structural alternative:

* either `|N_hi|<=2`, so at least 15 of those 17 physical neighbors have `|A_kk|<1/64`; or
* the graph on `N_hi` joining pairs with `|A_kl|>1/768` has independence number at most two. Its complement is triangle-free, so Mantel gives

  `# {large mutual edges}
   >= binom(|N_hi|,2)-floor(|N_hi|^2/4)`.                          (7.3)

This is an equation-level use of the designated partner gate. The explicit obstruction of Section 2 is in the first complementary branch: every neighbor diagonal is zero.

Continuity is not claimed on the partner-core exit.

## 8. Regression checks and scope

A deterministic checker accompanies this report. It verifies the exact powers in Proposition 2.1; samples physical cuts of finite representatives and sees maximum cross rank two; runs 250 bounded-degree weighted-graph coloring regressions; checks 400 random exterior-volume compressions `e3(CG)<=e3(C)`; and stress-tests the Newton-transform low-rank fork on 30,000 random spectra. `CHECKS.txt` ends `STATUS=PASS`. These are regression checks only; the proofs are the algebraic arguments above.

The source audit did not find a prior theorem matching the specific r46 normalized-energy obstruction or Theorem 5.2. The older global correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` is compatible but weaker for this purpose: Proposition 2.1 shows failure **inside the exact r46 residual packet**.

## 9. Remaining debt

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.

The next B07 obligation is

`QFORM-HIGH-DEGREE-KERNEL-STAR-HUB-RECEIVER-v1`:

spend the exact hub identity (6.3)-(6.4) together with the partner-forced low-diagonal/dense-edge alternative, or prove that the matching low-rank branches (5.3)-(5.5) synchronize into a physical bounded-rank carrier with a dependence-safe analytic receiver. The explicit Section 2 family must remain a mandatory stress test: any proposed universal E3-only compiler is already false there.

The other r40 overlap packets and r44 carrier remain distinct debts and are not declared paid here.

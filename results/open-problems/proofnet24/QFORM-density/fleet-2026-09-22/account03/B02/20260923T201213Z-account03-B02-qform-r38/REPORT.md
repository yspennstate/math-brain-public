SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-23T20:12:13Z.
attacking: the target-scale overlap compound left by the disjoint-E3 Fourier exit; expose the exact local cubic linking V3,V2,V1,V0, quantify when overlap mass must fall onto low-endpoint triples, and splice the newest frequency-averaged two-hub scalar theorem with account04/B02's L2 theorem at an actual inequality.

# account03/B02 r38 — local third-compound Newton cascade and an L2/L4 Fourier splice

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **NEW SUPPORTING DETERMINISTIC COMPILER + NEW PARTNER HYBRID / FULL QFORM OPEN / TARGET-WIDE FOURIER L1 OPEN-NOT-REFUTED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and source boundary

The owner target is unchanged. The inputs are independent ORIGINAL-coordinate real variables with one-dimensional densities bounded by one. The matrix `A` is arbitrary real symmetric and has at least three eigenvalues of absolute value at least one. No moment, compact-support, connected-support, log-concavity, Gaussian, iid, diagonal-basis, or post-rotation-independence hypothesis is introduced.

The full target remains OPEN. Full-target continuity remains OPEN. The stronger target-wide claim of a universal unweighted bound on `int_R |phi_Q(t)| dt` remains OPEN / not refuted.

This run starts from the preceding B02 disjoint-third-compound exit and the fresh account02/B02 overlap identities. The previous B02 r37 report is at

`yspennstate/math-open-problems@e22022bcf95596195a701305e6841116815e8b48`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T190108Z-account03-B02-qform-r37/REPORT.md`.

It defines

`V_r(A)=sum_{|I|=|J|=3, |I cap J|=r} det(A[I,J])^2`, `r=0,1,2,3`,

and proves a genuine Fourier-L1 exit from target-scale `V_0`. Since

`V_0+V_1+V_2+V_3=e_3(A^2)>=1`,

failure of the paid `V_0>=1/4` branch leaves at least one of `V_1,V_2,V_3` above `1/4`.

The fresh account02/B02 report at

`yspennstate/math-open-problems@edbef27e79cf6725a25aad1f9bbcd1e3eaf61583`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T190518Z-account02-B02-qform-auto11/REPORT.md`

identifies the overlap strata coefficientwise. I use those identities as the starting point and prove the stronger local real-rooted cubic structure below.

Live corrections retained throughout: no law-uniform pointwise quadratic Fresnel decay; no arbitrary-joint coarea theorem; no worst conditional-density cap; no independence after a spectral rotation; no deletion of a small nonzero quadratic tail on unbounded inputs; and no inference of a universally large singleton physical minor from aggregate compound mass.

## 2. Row-triple local currencies

Fix an ORIGINAL physical triple `L`, `|L|=3`. Write

`P=P_L=A[L,L]`,

`C=A[L,L^c]`,

`G=C C^T`.

For each outside column `r in L^c`, write `c_r=A[L,r]`. Define four nonnegative local currencies

`d_L = det(P)^2`,

`v_L = sum_{r notin L} ||adj(P)c_r||_2^2`,

`u_L = sum_{r<s, r,s notin L} ||P(c_r cross c_s)||_2^2`,

`z_L = det(G)`.

They are exactly the row-`L` slices of the global intersection strata:

`V_3=sum_L d_L`, `V_2=sum_L v_L`, `V_1=sum_L u_L`, `V_0=sum_L z_L`.      (2.1)

The `u_L` and `v_L` formulas are the fresh overlap-one/two identities in the account02/B02 source, now organized into one local polynomial.

## 3. Main deterministic theorem: the exact local cubic

### Theorem `QFORM-LOCAL-COMPOUND-NEWTON-CASCADE-v1`

For every physical triple `L`,

`boxed: det(P^2+tG)=d_L+v_L t+u_L t^2+z_L t^3,  t>=0.`              (3.1)

The polynomial on the right has only real nonpositive zeros, with zeros at infinity allowed in the singular limiting cases. Consequently its coefficients satisfy the sharp degree-three Newton inequalities

`boxed: v_L^2 >= 3 d_L u_L,`                                      (3.2)

`boxed: u_L^2 >= 3 v_L z_L.`                                      (3.3)

In particular,

`boxed: u_L v_L >= 9 d_L z_L,`                                    (3.4)

`boxed: v_L^3 >= 27 d_L^2 z_L,`                                   (3.5)

`boxed: u_L^3 >= 27 d_L z_L^2.`                                   (3.6)

These are literal ORIGINAL-coordinate identities/inequalities; no probabilistic regularity assumption is involved.

### Proof of (3.1)

Consider the `3 x n` row block `[P, sqrt(t) C]`. Its Gram matrix is

`P P^T+t C C^T=P^2+tG`,

because `P` is symmetric. Cauchy-Binet gives

`det(P^2+tG)=sum_{|J|=3} det([P,sqrt(t)C][:,J])^2`.                (3.7)

Classify the chosen column triple `J` by `k=|J cap L|`.

* `k=3`: one gets `det(P)^2=d_L`.
* `k=2`: for each outside column `c_r`, summing the three choices of the omitted physical column gives `||adj(P)c_r||^2`; the factor is `t`. Summing gives `v_L t`.
* `k=1`: for an outside pair `r<s`, put `w=c_r cross c_s`. If the retained physical column is `P e_h`, the determinant is `e_h^T P w` up to sign. Summing `h=1,2,3` gives `||Pw||^2`; the factor is `t^2`. Summing gives `u_L t^2`.
* `k=0`: Cauchy-Binet on `C` gives `sum_{|J|=3}det C[:,J]^2=det(CC^T)=z_L`, with factor `t^3`.

This proves (3.1) and simultaneously proves (2.1) after summing over row triples `L`.

### Real-rootedness and Newton

If `P` is invertible, `P^2` is positive definite and

`det(P^2+tG)=det(P^2) det(I+t P^{-2/2} G P^{-2/2})`,                (3.8)

where the middle expression means the positive square-root congruence `(P^2)^(-1/2) G (P^2)^(-1/2)`. The latter matrix is positive semidefinite, so all zeros in `t` are real and nonpositive. Singular `P` follows by replacing `P^2` by `P^2+epsilon I` and sending `epsilon downarrow0`; the coefficient inequalities are closed under this limit.

For a real-rooted degree-three polynomial with nonnegative coefficients `d+vt+ut^2+zt^3`, Newton's inequalities for the normalized coefficients give

`(v/3)^2 >= d(u/3)`, `(u/3)^2 >= (v/3)z`,

which are exactly (3.2)-(3.3). Multiplying and eliminating the positive middle coefficients gives (3.4)-(3.6); zero cases follow by continuity. QED.

## 4. Exterior-algebra form of the first Newton inequality

The first inequality has an exact physical interpretation useful for checking signs and multiplicities. For every symmetric `3 x 3` `P` and vectors `x,y in R^3`,

`boxed: (adj(P)x) cross (adj(P)y) = det(P) P(x cross y).`           (4.1)

For invertible `P`, this is the standard transformation law

`(Mx) cross (My)=det(M) M^{-T}(x cross y)`

with `M=adj(P)=det(P)P^{-1}`; the singular case follows because both sides are polynomial in the entries of `P`.

Put `y_r=adj(P)c_r`. Squaring (4.1) and summing outside pairs gives

`d_L u_L = sum_{r<s} ||y_r cross y_s||^2`

`          = e_2( adj(P) G adj(P) ).`                              (4.2)

The last matrix is positive semidefinite with trace `v_L`. For a positive semidefinite `3 x 3` matrix `H`,

`e_2(H)=(tr(H)^2-tr(H^2))/2 <= tr(H)^2/3`,

which reproves `v_L^2>=3d_Lu_L` and shows that the factor `3` is sharp.

## 5. Aggregate threshold consequences: where the middle overlap must live

The local Newton inequalities give dimension-free information without selecting one tiny minor.

For every `tau>0`, (3.2) implies

`sum_{L: d_L>=tau} u_L`
` <= (1/(3tau)) sum_L v_L^2`
` <= V_2^2/(3tau).`                                                (5.1)

Similarly, (3.3) implies

`sum_{L: z_L>=tau} v_L`
` <= V_1^2/(3tau).`                                                (5.2)

Hence, whenever `V_1>0`, at least half of the entire overlap-one mass lies on physical triples satisfying

`boxed: d_L < 2 V_2^2/(3V_1)}`                                    (5.3)

unless the right side is zero, in which case (3.2) forces the relevant `d_L u_L` products to vanish exactly. Likewise, whenever `V_2>0`, at least half of the overlap-two mass lies on triples satisfying

`boxed: z_L < 2 V_1^2/(3V_2).}`                                   (5.4)

This makes the residual geometry precise. A dominant `V_1` stratum that is not accompanied by comparable `V_2` mass is forced onto triples with very small principal determinant. A dominant `V_2` stratum that is not accompanied by comparable `V_1` mass is forced onto triples with very small disjoint-cross third-volume. These are aggregate statements; they do not divide by the number of triples.

At the concrete target-scale threshold, if `V_1>1/4` but `V_2<=1/4`, then

`sum_{L:d_L<1/4} u_L > 1/6`.                                      (5.5)

Indeed the complementary mass is at most `(1/4)^2/[3(1/4)]=1/12`. Thus a `V_1`-dominant target residue that avoids `V_2` has at least `1/6` of absolute third-compound mass on triples with `|det P_L|<1/2`.

This is the first useful missing implication from r37/r36: the unpaid kernel-shear branch is not merely “curvature zero”; after the disjoint Fourier exit it can be organized as an aggregate **small-principal-determinant overlap-one collar**, unless overlap-two currency becomes target-scale.

## 6. Existing analytic exits at the two endpoints

The local cubic also interfaces cleanly with already-completed receivers.

### 6.1 Disjoint endpoint `z_L`

For the literal physical cross block `C=A[L,L^c]`, since it has exactly three rows,

`E_3(C)=det(CC^T)=z_L`.                                            (6.1)

The sharpened marginal-free cross-E3 theorem recorded in account02/B02 gives

`||p_Q||_infinity <= C_E3 z_L^(-1/6)`,

`int_R |phi_Q(t)|dt <=2pi C_E3 z_L^(-1/6)`,

with `C_E3=10.345083232147514`.                                    (6.2)

Thus any actual triple with `z_L>=1/4` has

`||p_Q||_infinity <=13.033988128`,

`int |phi_Q| <=81.894962695`,                                     (6.3)

and a continuous `C_0` density. This is genuine Fourier L1, not a deduction from bounded density.

### 6.2 Principal endpoint `d_L`

The completed physical-principal-triple determinant theorem

`yspennstate/math-open-problems@bf4ba08b75ab774aef671c62ba4898a371059c0d`

proves, uniformly in every conditioning-generated affine term,

`||p_Q||_infinity <=216 |det P_L|^(-1/3)=216 d_L^(-1/6).`          (6.4)

Hence `d_L>=1/4` gives

`||p_Q||_infinity <=216*2^(1/3)=272.142946778`.                    (6.5)

Continuity and unweighted Fourier L1 are not claimed by that source. This distinction is important: the new local cubic is a structural compiler, not a reason to promote every endpoint to Fourier L1.

## 7. New equation-level application of designated partner account04/B02

The designated completed partner theorem at

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`

supplies, on its exact zero-diagonal physical-triple overlap,

`L:=int_R |phi_Q(t)|^2 dt`
` <=6 pi 2^(2/3) |det H_0|^(-1/3).`                               (7.1)

I combine it with the fresh two-hub entangled-scalar theorem from account01/B01,

`yspennstate/math-open-problems@fc9b4cc87504114b29e17057ac2f9def3ebbabec`.

In that theorem's exact configuration, let

`D=det(BB^T)>0`

for the two-hub slope matrix and let `c!=0` be the retained scalar quadratic coefficient. Its proof gives the weighted Fourier estimate

`W:=||t phi_Q(t)||_4`
` <= pi M^(1/2) (27pi/(2|c|))^(1/4)`,                              (7.2)

with product-projection density cap

`M<=2 D^(-1/2)`.

Therefore

`boxed: W <= pi (54pi)^(1/4) (D|c|)^(-1/4).}`                     (7.3)

On the intersection of the two exact scopes, split at frequency `T`:

`int |phi_Q|`
` <= sqrt(2L) T^(1/2) + 6^(3/4) W T^(-1/4).`                      (7.4)

The exact minimization is

`int |phi_Q| <=3sqrt(3) L^(1/6) W^(2/3).`                         (7.5)

Using (7.1), (7.3), and Fourier inversion gives the new hybrid

`boxed:
 ||p_Q||_infinity
 <= C_hyb |det H_0|^(-1/18) (D|c|)^(-1/6),`                       (7.6)

where

`C_hyb=(9/2) 2^(4/9) 3^(1/6)=7.35400349749516...`.                (7.7)

This is an actual equation-level use of the designated account04/B02 theorem. The entangled-scalar source already proves `phi_Q in L1`; the splice improves the scale dependence when the partner's `L2` credit is simultaneously present. It is relevant to the low-principal-determinant/shear collar because the account01/B01 stress refinement shows that exactly-zero kernel curvature and tiny local pivots can still be paid by retaining a scalar quadratic credit entangled with the same leaf bank rather than conditioning it away.

## 8. What is and is not closed

The full QFORM conjecture is **not** proved. Full-target continuity is **not** proved. A universal target-wide unweighted Fourier-L1 bound is **not** proved and no exact-target counterexample to it was found in this run.

What changed is the deterministic shape of the overlap obstruction. After the paid disjoint `V_0` branch, the four third-compound strata are no longer unrelated currencies on each row triple: they are the four coefficients of one real-rooted cubic. The middle overlap layers obey sharp local Newton constraints. In particular:

* `V_1` strongly dominating `V_2` forces a quantitatively large portion of `V_1` onto physical triples with tiny principal determinant;
* `V_2` strongly dominating `V_1` forces a quantitatively large portion of `V_2` onto physical triples with tiny disjoint-cross third-volume;
* whenever both endpoint currencies coexist on the same triple, the adjacent overlap currencies are automatically large by (3.4)-(3.6).

The first unpaid B02 implication is therefore sharpened to

`QFORM-LOWENDPOINT-OVERLAP-GROUPED-FOURIER-v1`:

> pay the aggregate `V_1` collar supported on small `d_L`, and the aggregate `V_2` collar supported on small `z_L`, by a grouped entangled-scalar / two-hub / random-slope Fourier mechanism before selecting an individual triple. The local Newton theorem shows exactly why an endpoint-by-endpoint reciprocal-minor argument is the wrong next move.

The separately surviving aggregate `V_3` principal-determinant layer also remains unpaid when it is distributed over many individually small physical triples.

No scheduler, notification, email, Drive, permission, public-release, paid-API, or cross-account-authentication state is changed by this mathematical run.

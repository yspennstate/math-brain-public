SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-23T21:10:34Z.
attacking: account03/B07 r38's moving E2-heavy planes — aggregate every transverse determinant increment before selecting a coordinate, then determine what exact synchronization is actually forced.

# account02/B07 — aggregate mixed-volume physicalization and the real bounded-rank synchronization theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner continuation consumed: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Role: coordinate minor selection / complementary constructions  
Status: **NEW AGGREGATE E3 COMPILER + STRONGER BOUNDED-RANK CORE EXTRACTION + EXACT COMMON-PLANE OBSTRUCTION / FULL QFORM OPEN**  
Brain state: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem is not proved or disproved. All cuts and conditionings below are on ORIGINAL coordinates. No moment, support, log-concavity, diagonal-basis, post-rotation independence, small-random-quadratic-tail deletion, pointwise quadratic Fourier decay, or universally good individual minor is used.

## 1. Sources consumed exactly in scope

The latest completed designated partner found before the main calculation is account03/B07 r38:

`yspennstate/math-open-problems@f822a8dfdb6a2cbc763373954a8b9dadb498568d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T203843Z-account03-B07-qform-r38/REPORT.md`.

Its theorem `QFORM-E2-TAIL-STABLE-TRANSFER-v1` starts from a literal physical crossing

`K=A[L,R]`, `Z=e_2(KK^T)>0`,

and for each physical row `i in L` defines the row-deleted crossing `K_i`, `G_i=K_iK_i^T`, `Z_i=e_2(G_i)`, physical E2 inclusion marginal `mu_i=1-Z_i/Z`, and the rank-at-most-two spectral E2-heavy projector `P_i` of `G_i`. The physical-heavy set

`H={i:mu_i>2/3}`

has size at most two, and for every `i notin H`, `Z_i>=Z/3`. With

`c_i=A[L\{i},{i}]`, `q_i=||(I-P_i)c_i||_2`,

its Newton-transform proof gives

`c_i^T H_2(G_i)c_i >= (Z/9)q_i^2`,                                  (1.1)

where `H_2(G)=G^2-tr(G)G+e_2(G)I`.

The completed marginal-free physical-E3 receiver used below is account02/B03, `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`, path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T184716Z-account02-B03-QFORM-auto11/REPORT.md`.

For any actual physical crossing `M` with `Z3=e_3(MM^T)>0`, arbitrary same-side curvature and affine terms retained,

`||p_Q||_infinity <= C3 Z3^(-1/6)`,

`C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,                        (1.2)

with a continuous density on that branch.

The bounded-dimensional physical-fiber theorem is source-pinned in account04/B07:

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

If an actual principal block on `m` original coordinates has `s_3>=gamma>0`, then

`||p_Q||_infinity <= 2 sqrt(6*pi*m)/gamma`,                           (1.3)

uniformly over everything conditioned outside that block.

The mandatory pinned source was read at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its D' theorem and rank-r Fresnel/Brascamp--Lieb theorem are applied below at actual equations.

The current Claude continuation at `c4c23b784395630c094ba299a50712209921d1ae` was also refreshed. Its single-hub conditional-adaptation proposal remains OPEN and is not used as a premise.

## 2. A general overlap-volume physicalization lemma

The first new point is deterministic and independent of r38.

Let `L,R` be disjoint physical coordinate sets. For integers `k>=1` and `0<=q<=k`, define the admissible mixed determinant bank

`V_{k,q} = sum det A[S, U union T]^2`,                                (2.1)

where the sum is over

- `S subset L`, `|S|=k`,
- `U subset L\S`, `|U|=q`,
- `T subset R`, `|T|=k-q`.

### Theorem 2.1 — `QFORM-OVERLAP-VOLUME-PHYSICALIZATION-v1`

There is a partition `L=I sqcup J` into original coordinates such that

`boxed:
 e_k(A[I,R union J] A[I,R union J]^T)
 >= 2^(-(k+q)) V_{k,q}.`                                             (2.2)

### Proof

Colour every element of `L` independently red/blue with probability `1/2`, and let `I` be red, `J` blue. A fixed determinant in (2.1) appears as a literal cross minor of `A[I,R union J]` whenever all `k` row labels in `S` are red and all `q` self-column labels in `U` are blue. Since `S` and `U` are disjoint, this has probability `2^{-(k+q)}`. Every other Cauchy--Binet term of the crossing is nonnegative. Taking expectations proves

`E e_k(A[I,R union J]A[I,R union J]^T) >=2^{-(k+q)}V_{k,q}`,

so some deterministic colouring attains the expectation. QED.

This is an aggregate-before-inversion statement. It never chooses one good determinant.

## 3. Aggregate upgrade of account03/B07 r38

Return to the r38 notation. Put

`F_i = c_i^T H_2(G_i)c_i`.                                          (3.1)

The rank-one Newton identity and Cauchy--Binet give the exact physical-minor identity

`F_i
 = e_3([K_i,c_i][K_i,c_i]^T)-e_3(K_iK_i^T)
 = sum_{S subset L\{i}, |S|=3}
   sum_{T subset R, |T|=2}
   det A[S,{i} union T]^2.`                                         (3.2)

Thus `sum_i F_i` is exactly `V_{3,1}` from Theorem 2.1. Applying (2.2) with `(k,q)=(3,1)` and then partner inequality (1.1) gives an actual physical partition `L=I sqcup J` for which, with

`M=A[I,R union J]`,                                                  (3.3)

one has

`boxed:
 e_3(MM^T)
 >= (1/16) sum_i F_i
 >= (Z/144) sum_{i notin H} q_i^2.`                                 (3.4)

This is the new theorem

**`QFORM-E2-AGGREGATE-TRANSVERSE-TO-PHYSICAL-E3-v1`.**

It strictly strengthens r38's pointwise compiler. For any `delta>0`, if

`Q_perp := (sum_{i notin H} q_i^2)^(1/2) >= delta`,                  (3.5)

then a single literal physical crossing satisfies

`Z3=e_3(MM^T) >= Z delta^2/144`.                                    (3.6)

The completed marginal-free E3 theorem (1.2) therefore gives the full ambient estimate

`boxed:
 ||p_Q||_infinity
 <= C3 (Z delta^2/144)^(-1/6).`                                     (3.7)

The important contraposition is stronger than r38: if this branch does not fire at scale `delta`, then

`boxed:
 sum_{i notin H} q_i^2 < delta^2.`                                  (3.8)

The TOTAL moving-plane transverse error is Frobenius-small; it is not merely true column by column.

### Current r36/r38 numerical packet

Partner r38 has

`Z>Z0 h^4`,

`Z0=854675.100194511`,

`h=(2sqrt(2)-1)/1572864=1.1624826588606455e-6`,

and uses `delta=h/1024`. Equations (3.6) give

`boxed:
 Z3 > [Z0/(144*1024^2)] h^6
    =0.0056602895272739135 h^6.`                                    (3.9)

Hence the marginal-free receiver yields

`boxed:
 ||p_Q||_infinity <24.991153492 h^(-1)
                   <2.150e7.`                                       (3.10)

This constant is intentionally not optimized; the structural gain is (3.8).

## 4. Actual bounded-rank synchronization after aggregate failure

The aggregate failure can now be converted into a global physical self-block factorization without identifying the planes `P_i` with one another.

Assume (3.8). Let

`L0=L\H`, `K0=K[L0,R]`, `r=rank K`.

For each `i in L0`, put

`p_i=P_i c_i`.

Every spectral direction in `P_i` has positive eigenvalue, so `range(P_i) subset range(K_i)`. Choose `z_i` with

`K_i z_i=p_i`.                                                       (4.1)

Let `Zmat` have columns `z_i`, `i in L0`, and put

`M0=K0 Zmat`.                                                        (4.2)

For `j!=i` in `L0`, equation (4.1) gives

`(M0)_{ji}=p_i(j)`.

Let `S=A[L0,L0]`. Define the diagonal matrix

`D_ii=S_ii-(M0)_ii`,                                                  (4.3)

and let `E0` have zero diagonal and off-diagonal entries

`(E0)_{ji}=S_{ji}-(M0)_{ji}`.                                       (4.4)

Column `i` of `E0` is just the restriction of `c_i-p_i`, hence

`||E0||_F^2 <= sum_{i in L0} q_i^2 < delta^2`.                       (4.5)

Since `S` is symmetric, average `S=M0+D+E0` with its transpose:

`S=D+R0+E`,                                                          (4.6)

where

`R0=(M0+M0^T)/2`, `rank R0<=2r`,                                    (4.7)

`E=(E0+E0^T)/2`, `diag E=0`, `||E||_F<delta`.                       (4.8)

This is exact. No tail of `K` has been discarded; all of it remains inside `M0=K0Zmat`.

Restoring the at-most-two physical-heavy coordinates adds a symmetric matrix supported on their rows and columns, of rank at most four. Thus the entire left self-block has

`A[L,L]=D_ext+R_ext+E_ext`,

`rank R_ext<=2r+4`, `||E_ext||_F<delta`,                              (4.9)

with `D_ext` supported on the nonheavy coordinates.

### Theorem 4.1 — `QFORM-BOUNDEDRANK-MOVINGPLANE-CORE-v1`

Suppose the physical crossing has actual rank `r<infinity` and the aggregate branch (3.5) fails. Let `d>delta`.

Either at least `2r+3` nonheavy diagonal coefficients from (4.3) satisfy `|D_ii|>=d`, in which case there is an ACTUAL original-coordinate principal core `J subset L0`,

`|J|=2r+3`,

such that

`boxed: s_3(A[J,J]) >= d-delta`,                                    (4.10)

and therefore

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(6*pi*(2r+3))/(d-delta);`                                 (4.11)

or there are at most `2r+2` such diagonals and they may be absorbed into the carrier, giving

`boxed:
 A[L,L]=R_1+E_1,
 rank R_1<=4r+6,
 |E_1|_max<d.`                                                       (4.12)

#### Proof of the core bound

Restrict (4.6) to any `J` of `2r+3` large-diagonal nonheavy coordinates. The rank of `R0[J,J]` is at most `2r`, so its kernel has dimension at least three. On that kernel, `D_J+R0[J,J]` acts as `D_J`; hence the max-min characterization gives

`s_3(D_J+R0[J,J])>=d`.                                               (4.13)

Unlike the earlier entrywise-tail core estimate, the aggregate theorem supplies

`||E[J,J]||_op <= ||E||_F <delta`,                                  (4.14)

with no factor `2r+3`. Weyl gives (4.10), and (1.3) gives (4.11).

If fewer than `2r+3` large diagonals exist, absorb at most `2r+2` rank-one diagonal terms together with the at-most-rank-four heavy-row correction and the rank-at-most-`2r` term `R0`. The remaining diagonal has magnitude `<d` and the off-diagonal residual has magnitude `<delta<d`, yielding (4.12). QED.

For the clean choice `d=2delta`, failure of the aggregate E3 branch therefore reduces every exact bounded-rank crossing to either a `(2r+3)`-coordinate genuine spectral core with `s_3>=delta` or

`rank<=4r+6 + entrywise<2delta`.                                    (4.15)

For exact rank two this sharpens the earlier r37 structural fallback from `rank<=18 + entrywise<22delta` to

`boxed: rank<=14 + entrywise<2delta`,                               (4.16)

unless a seven-coordinate actual core with `s_3>=delta` already pays. The full QFORM problem is not solved because the actual r38 survivor may have unbounded nonzero crossing rank; (4.9) retains that rank rather than deleting its tail.

## 5. Exact target-valid stress: the moving planes need not literally coincide

The natural stronger claim

> `q_i=0` for all nonheavy i forces one common rank-two physical plane

is false, even inside the owner target.

Fix `m>=2`. Let

`L=L_1 sqcup L_2 sqcup L_3`, `R=R_1 sqcup R_2 sqcup R_3`,

with every bank of size `m`. Let `u_a` and `v_a` be the normalized all-ones vectors on `L_a` and `R_a`. Put `gamma=1/4` and define the symmetric matrix

`A_m = [[C,K],[K^T,0]]`,                                             (5.1)

where

`K=2 sum_{a=1}^3 u_a v_a^T`,                                        (5.2)

`C=gamma sum_{a<b}(u_a u_b^T+u_b u_a^T)`.                           (5.3)

All physical diagonals vanish; the largest physical coefficient is `2/m`.

### Target spectrum

On the six-dimensional physical range `span(u_1,u_2,u_3,v_1,v_2,v_3)`, the matrix is

`[[gamma(J_3-I_3), 2I_3],[2I_3,0]]`.                                (5.4)

Since `gamma(J_3-I_3)` has eigenvalues `1/2,-1/4,-1/4`, the six nonzero eigenvalues of `A_m` are

`2.265564437074637...`, `-1.765564437074637...`,

and twice each of

`1.878902442735175...`, `-2.128902442735175...`.                     (5.5)

Thus all six have modulus larger than one. This is an exact target-class family.

### The r38 moving planes

The crossing `K` has squared singular values `4,4,4`, so

`Z=e_2(KK^T)=48`.                                                     (5.6)

For `i in L_a`, deleting row `i` changes these to

`4,4,4(1-1/m)`,

so

`Z_i=48-32/m`, `mu_i=2/(3m)<2/3`.                                   (5.7)

The two untouched bank directions have E2 inclusion marginal

`alpha_top=(2-1/m)/(3-2/m)>2/3`,                                    (5.8)

while the damaged bank direction has

`alpha_low=2(1-1/m)/(3-2/m)<2/3`.                                   (5.9)

Hence, for `i in L_a`, the r38 projector is exactly

`P_i=span{u_b,u_c}`, `{a,b,c}={1,2,3}`.                             (5.10)

But the physical self-column is

`c_i=(gamma/sqrt(m))(u_b+u_c)`,                                     (5.11)

so

`boxed: q_i=0 for every i.`                                          (5.12)

The planes nevertheless cycle through

`span(u_2,u_3)`, `span(u_1,u_3)`, `span(u_1,u_2)`.                  (5.13)

No one rank-two plane contains all three physical column directions

`u_2+u_3`, `u_1+u_3`, `u_1+u_2`,                                   (5.14)

which are linearly independent. Thus literal common-plane synchronization is false; rank three is already necessary.

This family also refutes a bounded-cardinality physical-core conclusion from `Z=48` plus exact moving-plane containment. Every entry has magnitude at most `2/m`, so for every fixed cardinality `M`, every principal block `H` with `|H|<=M` satisfies

`||A_m[H,H]||_op <= 2M/m ->0`.                                      (5.15)

For large `m` it lies inside any fixed strict no-pivot threshold. This is an intermediate-mechanism counterexample, not a QFORM counterexample.

## 6. Mandatory pinned-e5 applications

Two completed pinned results are applied at real equations.

### 6.1 D' on the actual aggregate r38 inequality

For the physicalized crossing in (3.3)-(3.9), if its E3 row inclusion marginals are at most `2/3`, pinned D' at `h_marg=2/3` gives

`||p_Q||_infinity <=9sqrt(3e) Z3^(-1/6)`.                           (6.1)

Combining with the actual live inequality (3.9),

`boxed:
 ||p_Q||_infinity <60.880368159 h^(-1)
                   <5.238e7.`                                       (6.2)

The later marginal-free theorem gives the stronger unconditional (3.10); (6.2) is recorded because the assignment requires an equation-level use of the pinned completed source.

### 6.2 The rank-six Fresnel theorem pays the exact common-plane obstruction

The stress family (5.1) has exact rank six. Its physical range is precisely the six bank-constant directions, so every coordinate leverage is `1/m<=1/2`. The product of the absolute nonzero eigenvalues is exactly

`|det(A_m|_range)|=4^3=64`.                                         (6.3)

The pinned rank-r Fresnel/Brascamp--Lieb theorem therefore gives

`|phi_Q(t)| <= (4pi)^3 * 64^(-1/2) |t|^(-3)
             =(2pi)^3 |t|^(-3)`.                                   (6.4)

Integrating the valid envelope `min(1,(2pi)^3|t|^-3)` gives

`int_R min(1,(2pi)^3|t|^-3) dt =6pi`,                               (6.5)

so Fourier inversion yields the universal exact-family estimate

`boxed: ||p_Q||_infinity <=3.`                                      (6.6)

Thus the stress is paid for the correct diffuse product-law reason. Its failure of common-plane/bounded-core extraction is not evidence against QFORM.

## 7. What is now actually unpaid

The partner's pointwise synchronization debt is strictly reduced.

The first unpaid implication is now

**`QFORM-AGGREGATE-MOVING-PLANE-TAIL-SYNCHRONIZATION-v1`.**

In the actual r36/r38 nonexact-tail chamber, assume on both physical sides that the aggregate transverse errors satisfy

`sum q_i^2 < (h/1024)^2`,                                           (7.1)

so the entire off-plane self-column error is Frobenius-small. The exact factorization (4.6)-(4.9) writes the self-block as diagonal plus a symmetrized factor through the FULL crossing `K`, plus that Frobenius residual. The full crossing has r36's determinant-heavy rank-at-most-two carrier but retains a genuinely nonzero higher-rank tail.

What remains is to control the factor

`K0 Zmat`

without replacing `K` by its top modes: naively truncating `K` can amplify its small singular tail through the unknown coefficients `z_i`. A valid next step must either show that this correlated tail has receiver-compatible aggregate volume, or force another physical E3 / finite core. The three-bank stress proves that the target cannot be literal equality of all local rank-two planes: even `q_i=0` may require a rank-three carrier.

The separate global low-rank-plus-entrywise-small chamber remains unpaid for arbitrary rough cap-one laws. Small coefficient norm alone is not a small random quadratic perturbation without moments.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate; continuity is obtained on the E3-paid branch through the cited marginal-free receiver.

## 8. Regression checks

`CHECKS.py` / `CHECKS_OUTPUT.txt` verify, as regression evidence only:

- on a random finite matrix, the average E3 over all physical red/blue colourings exceeds `sum_i F_i/16`;
- the exact six macro eigenvalues and absolute product `64` of the three-bank stress;
- the formulas (5.7)-(5.9) for several bank sizes;
- the live constants `0.0056602895272739135`, `24.991153491`, and `60.880368158`.

The captured output ends `STATUS=PASS`. The proofs are the exact Cauchy--Binet, Newton-transform, rank/nullity, and colouring arguments above; the checks are not proof evidence.

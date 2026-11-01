SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T18:53:27Z.
attacking: the low-leverage common-plane survivor after the latest relative-skew compiler; prove a direct small-s3-to-exact-latent-rank-two stability theorem, spend the complementary branch through the marginal-free physical E3 theorem, and retain the third spectral resource without deleting any small coefficient tail.

# fleet01/B19 auto13 — physical E3 or quantitative latent-rank-two completion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Outcome: **ESSENTIAL_STEP_APPLIED / NEW QUANTITATIVE COMPILER / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved on the physical-E3 paid branches used below; not asserted on the near-latent residue or the unrestricted target.

## 1. Fresh control, source frontier, and corrections


The exact target is unchanged: for arbitrary independent real original-coordinate inputs with densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential density bound for `X^T A X`, or give a valid counterexample. Continuity is tracked separately.

All live route corrections are retained. In particular, nothing here uses independence after rotating the random variables, the refuted arbitrary-joint coarea estimate, conditional projection-density caps, law-uniform pointwise quadratic Fourier decay, a uniformly good single minor, bounded supports or moments, or deletion of a small nonzero coefficient matrix as a small random error. The last warning is essential below: the new stability theorem is coefficient geometry, not probabilistic perturbation theory.

The immediate own predecessor is

`yspennstate/math-open-problems@7090e82b1b4a32ef9c3fb8d1dac4c04eb2304d8b`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260923T174847Z-fleet01-B19-QFORM-auto12/REPORT.md`.

It converted the exact common-plane `2+2+2` cancellation endpoint into the unique latent rank-two square

`[[S,S,I],[S,S,I],[I,I,S^{-1}]]`

and showed that an exact lifted rank-two completion cannot absorb the third target spectral direction: for its lift `L_2`,

`||A-L_2||op >= s_3(A) >= 1`.                                  (1.1)

The latest compatible common-plane refinement used here is fleet03/B20 r37,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T181514Z-fleet03-B20-QFORM-r37/REPORT.md`.

It supplies an original-coordinate quarter split whenever each of the three two-dimensional frame projections has physical row leverage at most `1/64`, and it tracks the deterministic singular-value loss from the normalized common-plane matrix to the literal physical split block.

## 2. Designated partner fleet02/B19 applied to an actual inequality

The designated partner source is fleet02/B19 r36,

`yspennstate/math-open-problems@9157730c1b552b81f58b3cb6ef604b687962e548`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260923T160847Z-fleet02-B19-QFORM-r36/REPORT.md`,

theorem `QFORM-OVERLAP-MIXED-EXTERIOR-VOLUME-v1`.

For disjoint original-coordinate banks `I,J,K`, with

`N=A[I,K]`, `M=A[I,J]`,

and `P_2` a top-two left singular projection of `N`, it proves the exact coefficient inequality

`e_3([M,N]^T[M,N])
 >= (s_1(N)s_2(N))^2 ||(I-P_2)M||_F^2`.                        (2.1)

Apply (2.1) at the actual physical orientation `I=D_1`, `J=D_2`, `K=K` of the common-plane predecessor. At the live constants

`Delta_* = 0.0014419528160955833...`,
`F        = 0.05671470919622164...`,

if

`delta_L^2=||(I-P_1)A[D_1,D_2]||_F^2 >= F/64`,

then

`Z_phys >= Delta_*^2 F/64
       = 1.842543860212322e-9`.                                (2.2)

The completed marginal-free physical-E3 Fourier theorem, fleet03/B02 r35,

`yspennstate/math-open-problems@52cef3abd27c641ae6666d6ee3bbc25d90cb4813`,

gives for every literal original-coordinate cross block `M_phys` with

`Z=e_3(M_phys M_phys^T)>0`

the full ambient bound

`||p_Q||_infinity <= C_E3 Z^(-1/6)`,
`C_E3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,                 (2.3)

and `phi_Q in L^1`. Thus (2.2) yields

`boxed: ||p_Q||_infinity < 301.317`,                            (2.4)

with a continuous `C_0` density. The symmetric `D_2` orientation is identical. Hence the analysis below begins only after the partner theorem has paid fixed transverse leakage; no transverse term is set to zero by approximation.

## 3. Normalized common-plane matrix

After the already-established common-left/common-right-plane compilers, work in the three two-dimensional deterministic coefficient spaces. Normalize the two invertible common-plane legs by coefficient congruence only. The resulting real symmetric matrix is

`K = [[D_1, R, I_2],
      [R^T, D_2, I_2],
      [I_2, I_2, D_3]],`                                      (3.1)

where each `D_j` is an arbitrary real symmetric `2x2` matrix and `R` is arbitrary real `2x2`. This changes no random variables and asserts no independence inside a projected plane.

The preceding B19 report characterized the exact equation `rank K<=2`. This run proves a direct quantitative converse from **only the third singular value of the complete matrix K**, including all three self blocks. It removes the need to control the skew part of `R` separately.

## 4. New theorem: small third singular value forces the unique latent completion

### Theorem 4.1 — `QFORM-COMMONPLANE-SMALL-S3-LATENT-COMPLETION-v1`

Let `K` be (3.1) and put

`epsilon=s_3(K)`.

If `epsilon<1/4`, then there is an invertible real symmetric `2x2` matrix `S` for which

`K_S = [[S,S,I_2],
        [S,S,I_2],
        [I_2,I_2,S^(-1)]]`                                    (4.1)

has rank exactly at most two and

`boxed:
 ||S-R||op <= (28/9) epsilon (1+||R||op),
}`                                                              (4.2)

`boxed:
 ||K-K_S||op <= (73/9) epsilon (1+||R||op).
}`                                                              (4.3)

The theorem includes all signs, singular or repeated spectral degeneracies of `K`, and every symmetric choice of self blocks. It is purely deterministic and has no law assumption.

### Proof

Because `K` is real symmetric, retain in its spectral decomposition the two eigenvalues of largest absolute value. This gives a **symmetric** rank-at-most-two matrix `L` with

`||K-L||op=s_3(K)=epsilon`.                                     (4.4)

Since the `(1,3)` block of `K` equals `I_2`,

`||L_13-I_2||op<=epsilon<1/4`,

so `L_13` is invertible. Hence `rank L=2`. Write

`A=L_13`, `B=L_23`, `H=L_33`.                                  (4.5)

A symmetric rank-two factorization `L=W Lambda W^T`, with `Lambda` the nonsingular `2x2` matrix of retained eigenvalues and `W` of full column rank, shows that invertibility of

`L_13=W_1 Lambda W_3^T`

forces `W_1`, `W_3`, and `Lambda` invertible. Therefore

`H=W_3 Lambda W_3^T`

is invertible. Put

`S=H^(-1)`.                                                     (4.6)

Since `rank L=rank H=2`, the Schur complement of `H` in `L` vanishes exactly. Therefore

`L_11=A S A^T`,
`L_12=A S B^T`,
`L_22=B S B^T`.                                                 (4.7)

Every block of `L-K` has operator norm at most `epsilon`, so

`||A-I||, ||B-I||, ||L_12-R|| <= epsilon`.                     (4.8)

Let

`c=(1-epsilon)^(-1)<=4/3`.

Then `||A^-1||,||B^-1||<=c` and

`||A^-1-I||,||B^-1-I||<=c epsilon`.                            (4.9)

From `S=A^-1 L_12 B^-T`, writing `r=||R||op`,

`||S-R||
 <= c^2 epsilon
    + ||(A^-1-I)R B^-T||
    + ||R(B^-T-I)||`
` <= epsilon {c^2+(c^2+c)r}`
` <= (28/9) epsilon(1+r)`.                                     (4.10)

This proves (4.2). Since `epsilon<=1/4`,

`||S|| <= r+(7/9)(1+r)
       <= (16/9)(1+r)`.                                        (4.11)

Using (4.7),

`||D_1-S||
 <= epsilon+||A S A^T-S||`
` <= epsilon+(2epsilon+epsilon^2)||S||`
` <= 5 epsilon(1+r)`.                                          (4.12)

The same argument gives

`||D_2-S|| <= 5 epsilon(1+r)`.                                 (4.13)

Finally, `S^-1=H`, hence

`||D_3-S^-1||<=epsilon`.                                       (4.14)

The only off-diagonal defect of `K-K_S` is `R-S` in the `(1,2)` block and its transpose. Since the block-norm comparison matrix is symmetric and nonnegative, its operator norm is at most its largest row sum. Equations (4.10)-(4.14) give

`||K-K_S||op
 <= [5+28/9] epsilon(1+r)
 = (73/9) epsilon(1+r)`,                                       (4.15)

which is (4.3).

Finally,

`K_S = [I_2; I_2; S^-1] S [I_2, I_2, S^-1]`,                  (4.16)

so `rank K_S<=2`. QED.

### Why this is stronger than the preceding relative-skew residue

The previous fleet03/B20 compiler proved that a large relative skew `||R-R^T||/(1+||R||)` forces physical third volume. Failure only said that `R` is approximately symmetric. Theorem 4.1 controls **all three arbitrary self blocks simultaneously**: whenever the complete normalized common-plane matrix has small `s_3`, it lies quantitatively near the one exact rank-two cancellation family. No separate case split on skew, determinant, signs, or self-curvature is needed.

## 5. Turn the complementary branch into a literal original-coordinate E3 payment

Assume now that each of the three two-dimensional physical frame projections has maximum row leverage at most `1/64`. Fleet03/B20 r37 proves an original-coordinate quarter split. Let `M_phys=A[L,R']` be its literal physical cross block. Its restricted frame Gramians have eigenvalues in `(1/4,3/4)`. Let

`sigma_*^2 = 0.000356312664981148...`,
`m_*^2 = (63/64)sigma_*^2
      = 0.0003507452795908176...`.                              (5.1)

Undoing the common-plane normalization costs at most the two bicore minimum singular values, and the physical restricted-frame square roots cost another factor `1/2` on each side. Exactly as in the source theorem,

`boxed:
 s_3(M_phys) >= (m_*^2/4) s_3(K).
}`                                                              (5.2)

No tail is dropped in (5.2); `M_phys` is an actual original-coordinate coefficient submatrix.

Since

`e_3(M_phys M_phys^T)
 >= s_1(M_phys)^2 s_2(M_phys)^2 s_3(M_phys)^2
 >= s_3(M_phys)^6`,                                             (5.3)

the marginal-free E3 theorem (2.3) gives, for every `eta>0`,

`s_3(K)>=eta`
` => ||p_Q||infinity
    <= 4 C_E3/(m_*^2 eta)`,                                    (5.4)

and the density is continuous `C_0`.

Choose

`eta=1/512`.                                                     (5.5)

Then the common-plane low-leverage state has the exhaustive alternative

### Paid branch

`boxed:
 s_3(K)>=1/512
 => ||p_Q||infinity < 61,602,386 < 6.161e7,
}`                                                              (5.6)

with continuous `C_0` density.

### Near-latent branch

If `s_3(K)<1/512`, Theorem 4.1 supplies an exact rank-two `K_S` with

`boxed:
 ||K-K_S||op
 < (73/(9*512))(1+||R||op)
 < 0.015843 (1+||R||op).
}`                                                              (5.7)

Thus, **after the fixed transverse leakage has been paid using the designated partner**, every low-frame-leverage common-plane survivor is either already bounded continuously by a universal constant, or the *entire* normalized six-dimensional coefficient matrix—not merely its cross cycle—is quantitatively close to the unique latent rank-two completion.

The constant in (5.6) is deliberately not optimized. Any fixed `eta<1/4` produces a universal paid constant and a corresponding quantitative latent tube.

## 6. Exact endpoint retains the third target spectral resource

At `s_3(K)=0`, undo the deterministic congruence and lift the exact rank-two common-plane completion by zero to the full original coefficient space; call it `L_2`. By Eckart--Young,

`boxed:
 ||A-L_2||op >= s_3(A) >=1.
}`                                                              (6.1)

So the latent completion does **not** destroy the third large direction. What is missing is not spectral existence but a product-preserving analytic receiver that combines the latent two-dimensional square with this retained unit coefficient remainder.

Equation (5.7) must not be converted into `X^T(K-K_S)X=o(1)`: admissible cap-one input laws may have no finite moments and arbitrarily separated unbounded support. This run therefore keeps the complete defect matrix in the next obligation.

## 7. Compact conditional proof graph after this run

Within the current source-pinned common-plane route, the argument is now:

1. Physical-pivot, spectral-window, diffuse cross-volume and D5 exits already pay their stated scopes.
2. The STAR4/common-plane compilers produce disjoint original-coordinate banks with two quantitative rank-two legs.
3. Fleet02/B19 r36 plus the marginal-free E3 theorem pays fixed transverse overlap by (2.1)-(2.4).
4. Right-plane mismatch is paid or reduced to one common two-dimensional third bank by fleet03/B19 r37.
5. If one common-plane frame has physical row leverage `>1/64`, record a genuine heavy physical anchor.
6. Otherwise the physical quarter split exists. This run pays `s_3(K)>=1/512` by the literal physical E3 estimate (5.6).
7. Every remaining low-leverage common-plane state lies in the quantitative latent tube (5.7), and the exact centre of that tube has a retained coefficient remainder of operator norm at least one by (6.1).

This is a conditional compiler for the common-plane branch, **not** a full proof of the conjecture. Other globally recorded residues, including relative-rank-one/low-cross-rank branches outside this common-plane chamber, remain as recorded by the fleet. No two independent end-to-end full-target reviews exist.

## 8. First essential missing implication

The first local debt has sharpened to

`QFORM-LATENT-R2-PLUS-UNIT-REMAINDER-PRODUCT-RECEIVER-v2`:

> For the low-leverage common-plane state in the tube (5.7), retain the complete defect and all outside coefficients. Use either the latent rank-two square itself or the guaranteed unit third spectral remainder (6.1) to produce a product-coordinate Fourier/small-ball receiver with a universal bound, without rotating the random variables, replacing their projection by an arbitrary bounded joint density, or treating a small coefficient defect as a small random variable.

The parallel local debt is the physical frame-leverage `>1/64` anchor. The current ridge-window theorem can already pay the entire form when the high-spectral-window projection has maximum coordinate leverage at most `1/32`; hence any ultimately unpaid state is also forced into a genuinely heavy spectral-window coordinate. This is useful structure but is not yet the required rough-law analytic closure.

## 9. Checks and scope

The constants in Sections 4-5 were recomputed directly. A 5,000-example finite regression check of the spectral-truncation construction was also run: no violation occurred; the largest observed ratio of the left side of (4.3) to its proved right side was about `0.111`, and the largest observed ratio in (4.2) was about `0.240`. The proof itself is the exact algebra above, not the numerical test. The checker is saved beside this report.

No scheduler state, enabled/quiet state, task identity, notification setting, email, account authentication, permission, public visibility, paid/remote compute, or other research programme was changed. Full QFORM status remains **OPEN / NOT PROVED / NOT DISPROVED**.

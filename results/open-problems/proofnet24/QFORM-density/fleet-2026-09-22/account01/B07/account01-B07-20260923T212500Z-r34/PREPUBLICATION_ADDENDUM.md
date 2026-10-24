# r34 prepublication addendum — source precedence and sharpened common-pair tube

This addendum is part of run `account01-B07-20260923T212500Z-r34` and supersedes only the novelty attribution of REPORT Sections 3-4 and the constants/thresholds in REPORT Section 7-8. The exact calculations in the original report are preserved.

## 1. Final source refresh: designated partner completed the same aggregate compiler

After the initial r34 report was committed, the newest completed designated partner account02/B07 appeared:

`yspennstate/math-open-problems@b2d2cccb46aa3fc83162b2cc4fba61a5e040ebd2`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T211034Z-account02-B07-qform-mixedvolume/REPORT.md`.

It independently proves the more general overlap-volume physicalization theorem and, at `(k,q)=(3,1)`, exactly the r34 random-colouring implication

`e3(A[I,R union J]A[I,R union J]^T)
 >= (1/16) sum_i F_i
 >= (Z/144) sum_i q_i^2`.

Accordingly, r34 no longer claims novelty for REPORT Theorem 3.1 or the arbitrary-moving-plane application in REPORT Section 4. The partner theorem is now the source of record for that exact scope. Applying it to the live `delta=h/1024`, `Z>Z0 h^4`, `Z0=854675.100194511`, gives the actual inequality

`Z3>0.0056602895272739135 h^6`,

hence the marginal-free E3 receiver gives

`||p_Q||_infinity <24.991153492 h^(-1)<2.150e7`,

with a continuous density. This is the required equation-level use of the newest completed designated partner result.

The same partner also gives a target-valid counterexample to the stronger assertion that the row-deleted E2-heavy planes must literally coincide. r34 does not use or assert that false statement.

## 2. Nonduplicate r34 step: aggregate a fixed global heavy singular pair

The genuinely new r34 branch starts from the completed account02/B07 two-heavy carrier inequality already present in its preceding source

`yspennstate/math-open-problems@726fef06d05f2d3024bd1565c736df43efb45d62`:

`x_p x_q>Z/3`,

with the physical E2 marginal law `mu_i` and sharpened heavy set

`H={i:mu_i>2/7}`, `|H|<=6`.

For nonheavy `i`, let

`ell_i=u_p(i)^2+u_q(i)^2`,

`d_i=dist(A[L\{i},{i}],span{hat u_p,hat u_q})`.

Since the `(p,q)` pair contributes nonnegatively to the physical E2 marginal,

`mu_i>(1/3)ell_i`, so `ell_i<6/7` and

`||hat u_p wedge hat u_q||^2=1-ell_i>1/7`.

The moved-column packet therefore has the fixed-pair lower bound

`F_i >= x_p x_q(1-ell_i)d_i^2 >(Z/21)d_i^2`.                       (2.1)

Now apply the newest partner's overlap-volume physicalization theorem, rather than re-proving the colouring lemma. For

`D_perp^2=sum_{i notin H}d_i^2`,

some literal physical crossing satisfies

`boxed: Z3>(Z/336)D_perp^2.`                                      (2.2)

Thus `D_perp>=delta` is continuously paid by

`||p_Q||_infinity<C_E3(Z delta^2/336)^(-1/6)`.

At `delta=h/1024`,

`Z3>0.002425838368831677 h^6`,

`boxed: ||p_Q||_infinity<28.781655200 h^(-1)<2.476e7.`             (2.3)

This does not identify the moving planes `P_i`. It uses one fixed global pair from the two-heavy singular branch, and if the partner's cycling-plane obstruction is present then either (2.2) fires or this two-heavy branch hypothesis itself is absent.

## 3. Failure of fixed-pair aggregate volume gives a common rank-16 plus Frobenius-small self block

If `D_perp<delta`, the exact construction in REPORT Section 6 remains valid:

`A[L,L]=D_0+R_0+E`,

`rank R_0<=16`,

`diag E=0`,

`boxed: ||E||_F<delta.`                                           (3.1)

The key point is that this common-plane conclusion is conditional on failure of the **fixed-pair aggregate packet (2.2)**, not on `q_i=0` for varying row-deleted planes. Hence it is compatible with the newest partner's counterexample.

## 4. Sharpened finite-core / operator-tail alternative

The newest partner report explicitly source-pins the physical-fiber theorem:

if an actual principal block on `m` original coordinates has `s_3>=gamma>0`, then

`||p_Q||_infinity <=2sqrt(6 pi m)/gamma`,                           (4.1)

uniformly over everything conditioned outside the block.

Use (3.1) directly rather than feeding only the entrywise bound to the older coordinate-core interface.

If at least nineteen diagonal entries of `D_0` satisfy

`|D_0(ii)|>=2delta`,                                               (4.2)

restrict to any nineteen of those coordinates. On that block `rank R_0<=16`, so `ker R_0` has dimension at least three. On this kernel,

`||(D_0+R_0)x||=||D_0x||>=2delta||x||`.

The max-min characterization therefore gives

`s_3(D_0+R_0)>=2delta`.

Since `||E||_op<=||E||_F<delta`, Weyl gives

`boxed: s_3(A[J,J])>delta.`                                       (4.3)

Applying (4.1) at `m=19` gives

`boxed: ||p_Q||_infinity<2sqrt(114 pi)/delta.`                     (4.4)

This is an essential-boundedness conclusion; continuity is not promoted.

If (4.2) fails, at most eighteen exceptional diagonal entries have modulus at least `2delta`. Absorb them into the rank term. The remaining diagonal has operator norm `<2delta`; hence

`boxed:
 A[L,L]=R_L+T_L,
 rank R_L<=34,
 ||T_L||_op<3delta.
`                                                                    (4.5)

This supersedes REPORT (7.4), which had the weaker `21delta` tail because it passed through an entrywise-only interface.

At the live scale,

`boxed: ||T_L||_op<3h/1024=3.40571091463e-9.`                     (4.6)

## 5. Two-sided full-matrix tube, sharpened

Apply the fixed-pair construction on both sides of the physical cut. The low-E3 two-heavy carrier source retains a rank-two crossing approximation `K_2` with

`||K-K_2||_F<0.003245045040 h`.

If neither side pays by (2.3) or (4.4), then

`A=R+T`,

with

`rank R<=34+34+2 rank(K_2)<=72`,                                  (5.1)

and

`boxed:
 ||T||_op
 <3delta+0.003245045040 h
 =(3/1024+0.003245045040)h
 =0.00617473254 h
 <7.179e-9.
`                                                                    (5.2)

Weyl therefore gives the rank-at-most-72 carrier `R` at least three eigenvalues of absolute value `>1-7.179e-9`.

No probabilistic smallness of `X^T T X` is inferred from (5.2). The tail remains genuine, and arbitrary cap-one inputs may have no moments.

## 6. Current first unpaid implication

On the two-heavy low-E3 sibling, the remaining analytic debt is now

`QFORM-R72-OPSMALL-ROUGHLAW-RECEIVER-v2`:

consume a target-valid decomposition

`A=R+T`, `rank R<=72`, `s_3(A)>=1`, `||T||_op<7.179e-9`,

for arbitrary independent cap-one laws without deleting `T`; or convert `T` into fresh physical E3 / grouped-hub currency.

The newest designated partner's separate general moving-plane chamber and its cycling-plane obstruction remain separate obligations. The rank-one-heavy interface sibling is also separate. Full QFORM and full continuity remain OPEN.

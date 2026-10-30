# fleet01/B12 — iterated Schur-pivot closure for arbitrary coupled additions

**Programme:** QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.5  
**Run:** B12-20260922T151637Z-r12  
**Assignment:** Additional eigenvalue control  
**Classification:** PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN  

## 1. Exact target and source discipline

The universal conjecture remains open: for every dimension, independent real coordinates with densities bounded by one, and every real symmetric A with at least three eigenvalues of absolute value at least one, prove a universal L-infinity density bound for X^T A X. Continuity is tracked separately.

No spectral rotation is used to preserve independence. All elimination below is in the original coordinate system. The live corrections excluding pointwise van-der-Corput decay, post-rotation independence, naive fiber suprema, and the false local-block/cross-rank dichotomy are respected.

## 2. Two completed inputs

### 2.1 Dependent square smoothing

From `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`:

If R has density at most M and, conditionally on R=r, V has a density at most one, then for every a != 0,

    ||p_{R+aV^2}||_infinity <= 2 sqrt(M/|a|).                 (2.1)

No independence between R and V is required.

### 2.2 Required partner fleet02/B12

From `yspennstate/math-open-problems@e962f1e44ab23c8ad3e9a9b6cd58f21ed574930d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T144812Z-qform-extraeig-r11/REPORT.md`:

If a residual physical cross block has a base certificate

    s_{5+r}(A0[I,J]) >= sigma > delta,

and the added residual matrix is E=R+S with rank(R)<=r and ||S||op<=delta, then the final residual quadratic form has a continuous density satisfying

    M_* := ||p||_infinity <= 5e/[2(sigma-delta)].             (2.2)

This is the partner result actually used below.

## 3. One-step Schur extension

Let U be a vector of independent original coordinates, and let X be one further independent original coordinate with density at most one. Consider an arbitrary affine quadratic polynomial

    Q(X,U)=aX^2+2X b^T U+dX+R_0(U),

where a != 0 and R_0 is any quadratic-affine function of U. Completing the square only in the original coordinate X gives

    Q = a V^2 + R(U),

    V = X + a^{-1}(b^T U+d/2),

where R(U) is the exact Schur-complement residual.

Because X is independent of U, conditional on U the variable V is a translate of X and has density at most one. Conditioning further only on the scalar R(U) mixes such translates, so the conditional density of V given R remains at most one. Hence (2.1) gives:

### Lemma 3.1 — QFORM-SCHUR-EXTENSION-v1

If the residual R has density bounded by M, then

    ||p_Q||_infinity <= 2 sqrt(M/|a|).                        (3.1)

The statement is uniform in every affine tilt and in all couplings b. It proves essential boundedness; continuity is not asserted.

Equivalently, if a symmetric block is written

    A = [[a,c^T],[c,D]],

then only the Schur complement

    S = D - c c^T/a

enters the residual certificate. Thus an arbitrary coupled one-coordinate extension is paid by one scalar pivot a, not by the spectrum of A.

## 4. Iterated original-coordinate Schur chain

Choose distinct original coordinates i_1,...,i_m. Starting from the selected principal quadratic matrix, eliminate them in this order. Let A^(0) be the current matrix and recursively write

    A^(j-1) = [[a_j, c_j^T],[c_j,D_j]],
    A^(j)   = D_j - c_j c_j^T/a_j,

with every a_j != 0. The remaining variables are still untouched original independent coordinates.

Assume the terminal residual A^(m), with arbitrary affine tilt, has density cap M_m. Applying Lemma 3.1 backwards yields

    M_{j-1} <= 2 |a_j|^{-1/2} M_j^{1/2}.                     (4.1)

Induction gives the exact closed-form certificate

    M_0 <= 4^(1-2^(-m)) M_m^(2^(-m))
           prod_{j=1}^m |a_j|^(-2^(-j)).                     (4.2)

Indeed the coefficient of log M_m is 2^(-m), that of log|a_j| is -2^(-j), and the log 2 coefficients sum to 2(1-2^(-m)).

A useful invariant form is even simpler. For every a !=0 and M>0,

    2 sqrt(M/|a|) <= max{M,4/|a|}.                            (4.3)

Therefore

    boxed{ M_0 <= max( M_m, max_{1<=j<=m} 4/|a_j| ) }.       (4.4)

In particular, if all |a_j|>=eta>0, then an arbitrarily long chain of extra coupled coordinates satisfies

    boxed{ M_0 <= max(M_m,4/eta) }.                           (4.5)

There is no growth with the number of added coordinates. Pivot signs are arbitrary.

## 5. Applying the completed fleet02/B12 partner theorem

Apply (4.4) with the terminal cap (2.2). If the terminal Schur residual obeys the partner cross-spike-plus-tail hypotheses with gamma=sigma-delta>0, then the full quadratic form before all m Schur extensions satisfies

    boxed{
      ||p_Q||_infinity
      <= max{ 5e/(2 gamma), max_j 4/|a_j| }.
    }                                                         (5.1)

Equivalently, if every pivot satisfies

    |a_j| >= 8 gamma/(5e) = 0.588607105874... gamma,          (5.2)

then **arbitrarily many coupled additions cost nothing at all in the final constant**:

    boxed{ ||p_Q||_infinity <= 5e/(2 gamma). }                (5.3)

This is a direct use of the named fleet02/B12 result, not a citation-only dependency.

The same lifting mechanism applied to its definite-triple spike-plus-tail branch, whose terminal cap is C_*/(L-delta) with C_*=24.183038289961516..., shows that all Schur pivots with

    |a_j| >= 4(L-delta)/C_* = 0.165405188216... (L-delta)     (5.4)

leave that terminal cap unchanged.

## 6. Why this is genuine additional-eigenvalue control

Schur pivots are not eigenvalues, and no claim equating them is made. The point is that the theorem tolerates spectral changes far larger than the pivot scale.

For example, start with a controlled positive residual B=I and make the one-step extension

    A_M = [[1,M],[M,1+M^2]].                                  (6.1)

Its Schur complement at the first coordinate is exactly 1. Its two eigenvalues have product one and satisfy

    lambda_max(A_M) ~ M^2,
    lambda_min(A_M) ~ M^(-2).

Thus one original-coordinate Schur extension simultaneously creates an arbitrarily large eigenvalue and an arbitrarily small eigenvalue, yet the density cap is controlled uniformly by (3.1). Changing the pivot sign gives equally large mixed-sign spectral spread. Iterated unit-pivot congruence extensions can have arbitrarily bad spectral condition number while (4.5) remains dimension-free.

So additional eigenvalues are not harmless because of convolution after rotation; they are harmless here because each added original coordinate enters through a conditional translation followed by a square whose conditional density cap is source-valid.

## 7. Arbitrary outside completion

All statements above persist after arbitrary completion outside the selected pivot-plus-terminal coordinates. Condition on every outside original coordinate first. Outside quadratic terms become constants and outside cross couplings become affine tilts in the selected variables; neither changes the Schur pivots or the terminal quadratic matrices. Since every bound above is uniform in affine tilts, averaging the conditional densities preserves the same cap.

Hence all outside eigenvalues, signs, magnitudes and couplings are unrestricted once the selected original-coordinate Schur chain and terminal certificate are present.

## 8. What remains open

This is a real stability theorem, not a full solution. The bare hypothesis of three eigenvalues with absolute value at least one does not guarantee an elimination order whose Schur pivots stay above a universal floor before reaching a partner-certified residual. The known diffuse bank family has tiny physical pivots and is controlled instead by aggregate smoothing, so a universal proof needs a heavy-pivot versus diffuse-aggregate decomposition rather than a claim that such a pivot chain always exists.

The new unpaid implication is therefore:

> prove that every target matrix can be reduced either through a bounded-below original-coordinate Schur chain to an existing terminal certificate, or into one of the already controlled diffuse/bank aggregate regimes, with dimension-free constants.

Full QFORM remains OPEN. Continuity is not established by the Schur-chain lift itself, although the terminal partner density is continuous before lifting.

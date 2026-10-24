# Further Fourier consequences, obstructions, and exact continuation target

17 September 2026. **PARTIAL; full Lyons conjecture OPEN.** Self-checks only. Frozen global three-site `B_Phi` remains UNMEASURED. Model and reasoning settings are not independently exposed. This phase uses moves 18 (bivariate counts), 20 (identify exactly why a sufficient bound fails), and 30 (separate favorable and adverse mean directions).

## 1. A third complete affine-family consequence: two convex cones

Fix the measured diagonal `t in [0,1]` and write

    a=t+z, b=t-z,
    K=F diag(t+z+x,t-z+y,t+z-x,t-z-y) F*.

**Corollary.** The configuration entropy is jointly concave in `(z,x,y)` on each of the two closed convex sets

    Omega_+ = {physical contractions,  2z >= sqrt(x^2+y^2)},
    Omega_- = {physical contractions, -2z >= sqrt(x^2+y^2)}.

The physical constraints are that the four displayed affine eigenvalues lie in `[0,1]`. Each set is the intersection of a polytope and a second-order cone, hence is convex.

Proof: every direction in this fixed-diagonal affine space has `a'=z'` and `b'=-z'`. Within either cone, `Delta=2(x^2+y^2-4z^2)<=0`, so `log(O/P)<=0`. The final term in equation (13) of `FOURIER_ALL_MEANS.md` is consequently

    -4(z')^2 log(O/P)>=0.

Every other term there is nonnegative. Integrating the Hessian inequality proves interior-segment concavity. For `0<t<1`, each cone contains a strict contraction with `x=y=0` and a sufficiently small `z` of the indicated sign. Contract any boundary segment toward that point and use entropy continuity. At `t=0,1` only the zero kernel or identity is possible. This proves the complete closed-set assertion.

This is a three-variable statement with the opposite edge allowed to vary, distinct from the common-pair-mean theorem where that edge is zero. It does not cover the region `4z^2<x^2+y^2` under arbitrary opposite-edge motion.

## 2. A compact bivariate count formulation

Partition the measured coordinates into the opposite pairs `A={0,2}` and `B={1,3}`. Let `N_A,N_B` be their occupation counts. Define two independent random vectors `U,V in {0,1}^2` by the respective probability tables

    law(U) = [[(1-a)^2-x^2, a(1-a)+x^2],
              [a(1-a)+x^2, a^2-x^2]],

    law(V) = [[(1-b)^2-y^2, b(1-b)+y^2],
              [b(1-b)+y^2, b^2-y^2]].

Rows and columns correspond to the occupations on `A` and `B`. These are ordinary two-site DPP laws with kernels `[[a,x],[x,a]]` and `[[b,y],[y,b]]`; a phase on the second coupling does not change these two-site laws. The physical bounds on `x,y` make all entries nonnegative.

Then `(N_A,N_B)` has exactly the law of `U+V`. Its 3-by-3 table is

    [[f_0, 2c_1, O],
     [2c_1, 4P, 2c_3],
     [O, 2c_3, f_4]].                              (1)

This follows by multiplying the two bivariate generating polynomials; the nine coefficient identities are checked exactly in `verify_fourier_barriers.py`. The table also follows by applying a Hadamard change of basis separately within `A` and `B`, which preserves their counts and splits the kernel into two two-site blocks.

The measured law is uniform conditional on the two counts, so its entropy is exactly

    H = H(N_A,N_B)
          + E log[binom(2,N_A) binom(2,N_B)].        (2)

The count marginals are both the sum of independent `Bern(a)` and `Bern(b)` variables. In particular, the two measured-pair marginal entropies are both `E_2(a,b)`, the binomially weighted two-trial count entropy. Hence

    I(A;B)=2E_2(a,b)-H.                             (3)

Theorem A is equivalently convexity of this mutual information in `(x,y)` for every fixed `a,b`. A bivariate extension of the local count method could still prove more. Equation (2) alone does not supply such a theorem.

## 3. Two exact warnings against stronger substitutions

These examples disprove sufficient proof shortcuts, not the source conjecture.

### Discarding all remaining local Fisher terms is too costly

Take eigenvalues `(1,99,99,1)/100`, hence `a=b=1/2`, `x=-49/100`, `y=49/100`, and use pair-coordinate velocity

    (a',b',x',y')=(-5,2,-1,2).

Let `alpha,beta` have the meanings of `FOURIER_ALL_MEANS.md`, and let `I_excess` be the excess measured Fisher information over count Fisher information. The tempting sufficient lower bound

    B=I_excess+g_0^2/f_1+g_3^2/f_3
            +sum_k(h_k^+ beta_k+h_k^- alpha_k)
            +4a'b' log(O/P)                       (4)

is strictly less than `-1` here (approximately `-1.293175295715097`). The actual negative entropy curvature is greater than `1700` (approximately `1780.3578584089057`). In fact

    (h_0,h_1,h_2)=(-19602,-396,-2)/625.

Thus the omitted local Fisher terms matter even though all three acceleration coefficients have the easier sign. The bound is valid, but its global nonnegativity is false.

### Mutual information need not be convex when the pair means move

Take eigenvalues `(1/100,3/5,1/100,1/100)`, so

    a=1/100, b=61/200, x=0, y=59/200,
    (a',b',x',y')=(1,-1,0,0).

The overall diagonal mean stays fixed. Nonetheless the second derivative of `I(A;B)` is less than `-2/5` (approximately `-0.4559144082245647`). The actual negative entropy curvature is greater than `68` (approximately `68.83937540321775`). Consequently (3) cannot be completed into a global proof by declaring the mutual information jointly convex.

Both statements are verified with rational probability jets and exact logarithm enclosures by `verify_fourier_barriers.py`. The output is `fourier_barriers_certificate.json`. The verifier also checks the pair marginal directly from the full atom jets, so the subtraction in (3) is not inferred from approximate spectra.

## 4. A sharper local remainder that is still only a candidate route

There is more positive curvature in the Hillion-Johnson inequality than was used in (4). Put

    rho_k=sqrt(f_k f_(k+2))/f_(k+1),
    L_k=-2log rho_k,
    X_k=g_k/sqrt(f_k), Y_k=g_(k+1)/sqrt(f_(k+2)),
    eta_k=1-rho_k L_k/(1-rho_k^2)>=0.

The precise source inequality gives

    h_k(1-rho_k^2)
       <=rho_k Q_k-rho_k(1+rho_k)(X_k-Y_k)^2.

Therefore, for `h_k>=0`,

    Q_k-h_k alpha_k
      >=eta_k Q_k
           +rho_k L_k/(1-rho_k)(X_k-Y_k)^2
           +h_k beta_k.                           (5)

For `h_k<=0`, retain the exact `Q_k+(-h_k)alpha_k`. Inserting these expressions into equation (13) gives a stronger rigorous lower bound than (4). Its universal sign in the adverse cone has not been proved. `explore_fourier_local_remainder.py` searches that specific remaining bound and records numerical results only.

An unconditional replacement of *every* local term by a bound in `Q_k` alone loses the positive negative-acceleration terms near repeated eigenvalues. Numerical tests produced negative values near opposite changes of the two means. Such a replacement is not used in any proved theorem.

## 5. Exact restart point

The full four-eigenvalue Fourier problem still requires

    R >= -4a'b' log(O/P),

where `R` is the full nonnegative expression in Section 7 of `FOURIER_ALL_MEANS.md`. The global source conjecture requires much more than this commuting four-site family. The unrestricted three-site milestone is still open in this continuation.

Next useful directions are a proof of the sign of the strengthened bound (5), or a bivariate weighted-count inequality compatible with (1)-(2). The two exact failures above exclude replacing these tasks by positivity of (4) or global mutual-information convexity. Restricted theorems already proved should be reused, not rediscovered.

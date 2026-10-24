SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T06:20:09Z.
attacking: heavy non-coloop two-sheet branch — route residual longitudinal curvature through a disjoint product bank and isolate the exact same-coordinate overlap obstruction.

# Early substantive checkpoint: support-separated heavy-row closure

Full QFORM remains open. The immediately preceding account02/B05 r22 closed only the leverage-one coloop endpoint. The first new calculation here is a strict non-coloop extension under an exact original-coordinate support separation.

Let an exact-rank-three form be `A=R Lambda R^T`, `R^T R=I_3`, with all three active eigenvalues of modulus at least one. Suppose row `i` has leverage `c=||r_i||^2>=1/2`. Choose the first active basis vector `e1=r_i/sqrt(c)`. Assume the remaining physical rows split into disjoint sets `J0,Jperp`, with rows in `J0` parallel to `e1` and rows in `Jperp` orthogonal to `e1`. Parseval gives

`sum_(j in J0) r_j r_j^T=(1-c)e1e1^T`,

and the transverse row family on `Jperp` is a two-dimensional Parseval frame. Hence the first spectral coordinate is

`S=sqrt(c) X_i + sqrt(1-c) U`,

where `U` is a normalized linear projection of the product law on `J0`, while the transverse pair `(C,D)` is an orthonormal two-dimensional projection of the disjoint product bank `Jperp`. Therefore `S` is genuinely independent of `(C,D)`,

`||p_S||inf <=1/sqrt(c)<=sqrt(2)`,

and, by the two-dimensional product-projection bound used in the required newest Claude source,

`||p_(C,D)||inf<=2`.

Rotate only inside the already-dependent transverse pair so that the coefficient matrix is

`B=[[a,beta,0],[beta,alpha,delta],[0,delta,gamma]]`.

This does not claim independence of `C,D`. Since the eigenvalues of `B` are the three active eigenvalues,

`||B^(-1)||op<=1`, `|det B|>=1`, and `a^2+beta^2=||Be1||^2>=1`.

The branch calculation is now:

1. If `|a|>1/16`, complete the square only in the genuinely independent scalar `S`. The Schur pair has determinant `det B/a`. The rank-two half-Riesz theorem for the orthonormal product projection `(C,D)` gives

`||p_Q||inf <=16 sqrt(30) ||p_S||inf |a det B|^(-1/4)
             <=32 sqrt(60)<247.871`.

2. If `|a|<=1/16` and `|gamma|>=1/2`, then `beta^2>=255/256`. Normalize the scalar by `S'=L S`, `L=||p_S||inf<=sqrt(2)`, and apply account02/B05 r21's scalar/dependent-pair theorem. Scaling gives

`||p_Q||inf <=31 M^(2/3)L^(2/3)|beta^2 gamma det B|^(-1/6)`,

with `M<=2`, hence `<69.639`.

3. If `0<|a|<=1/16` and `|gamma|<1/2`, the r22 inverse certificate is purely matrix-theoretic and still applies. For `x=B^(-1)e3`, the first and third equations of `Bx=e3` give `|a delta|/|beta|>1/2`; the cofactor `(B^(-1))_31=beta delta/det B` gives `|det B|>=|beta delta|`. Thus

`|a det B|>beta^2/2>=255/512`.

The same scalar-square plus rank-two half-Riesz estimate gives

`||p_Q||inf <=16 sqrt(60)(512/255)^(1/4)<147.530`.

4. If `a=0`, invertibility forces `beta gamma!=0` and `det B=-beta^2 gamma`. The exact-null scalar/dependent-pair endpoint (account02/B16, also incorporated in r21) after the same scalar normalization gives

`||p_Q||inf <=31 M^(2/3)L^(2/3)|det B|^(-1/3)
             <=31*2^(5/6)<55.24`.

Therefore this exact support-separated heavy-row class has the full-line essential bound `<248`, including the convex/two-sheet side. The support split is the real hypothesis: if the same original residual coordinates carry both longitudinal and transverse coefficients, the scalar `S` and pair `(C,D)` are dependent and none of the four payments above may be transferred by a conditional-density cap.

Required source result applied at a real inequality: Theorem C of math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 already gives `P(Q in J)<=pi sqrt(2)|J|` on the ruled majority-sign half-line for every exact-rank-three instance. The new checkpoint therefore targets only the opposite full-line obstruction rather than reproving the paid one-sheet calculation.

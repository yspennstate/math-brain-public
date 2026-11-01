SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B15, 2026-09-22T18:04:30Z.
attacking: the scalar-Q' conditional-supremum implication in owner revision 2026-09-22.11; construct or rule out a source-valid rare-level blow-up.

# fleet02/B15 — scalar-Q' worst-level conditioning fails on a 4-cube corner


## 1. First unpaid implication and result

The current owner message proposes splitting three large spectral coordinates from the remaining scalar quadratic part,

Q = Q3 + Q',

and using

p_Q(t) = E[ p_{Q3|Q'}(t-Q') ]

followed by

||p_Q||_infinity <= sup_b ||p_{Q3|Q'=b}||_infinity.

It asks for a dimension-free bound on this scalar-conditioned supremum. The exact mixture identity and the displayed inequality are valid, but the proposed uniform supremum is false even for one four-dimensional target instance with iid uniform physical coordinates, simple spectrum, invertible A, and no zero physical entries.

The correct surviving inequality is the average

||p_Q||_infinity <= E[ ||p_{Q3|Q'}||_infinity ],

and, when the rank-three coarea estimate is applicable conditionally,

||p_Q||_infinity <= K E[ ||rho_{123|Q'}||_infinity^(2/3) ].

This report proves that replacing this weighted average by a worst scalar level loses an essential rare-event factor.

## 2. Exact source-valid target

Let X_1,...,X_4 be independent Uniform[0,1] variables. Define the orthonormal Hadamard spectral directions

u1=(1,1,-1,-1)/2,
u2=(1,-1,1,-1)/2,
u3=(1,-1,-1,1)/2,
u4=(1,1,1,1)/2,

and Y_j = u_j dot X. Take eigenvalues

(lambda_1,lambda_2,lambda_3,lambda_4)=(1,2,-3,1/2).

Thus

Q3 = Y_1^2 + 2Y_2^2 - 3Y_3^2,
Q' = (1/2)Y_4^2,
Q = Q3 + Q' = X^T A X,

with the exact physical matrix

A=(1/8) [[1,5,9,-11],[5,1,-11,9],[9,-11,1,5],[-11,9,5,1]].

Its eigenvalues are exactly 1,2,-3,1/2. Hence A satisfies the owner target with exactly three eigenvalues of modulus at least one; it is invertible, has simple spectrum, and every physical entry is nonzero.

## 3. Exact cube-corner conditional law

Because Y_4=(X_1+X_2+X_3+X_4)/2, take any y in (3/2,2) and put

r = 4 - 2y in (0,1).

Writing Z_i=1-X_i, conditioning on Y_4=y is equivalent to

Z_i>=0,  sum_i Z_i=r.

The physical joint density is one on the unit cube, and the Hadamard map is orthogonal. Therefore, conditional on Y_4=y, W=Z/r is uniform on the standard three-simplex

Delta_3={w_i>=0, sum_i w_i=1}.

The Euclidean three-volume of the section {z_i>=0, sum z_i=r} is r^3/3, so

p_{Y4}(y)=r^3/3,

and the conditional density rho_y of (Y_1,Y_2,Y_3) is uniform on its tetrahedral image with

||rho_y||_infinity = 3/r^3.                                      (3.1)

For j=1,2,3, u_j dot (1,1,1,1)=0, hence

Y_j = -r (u_j dot W).

Consequently

Q3 | (Y4=y) = r^2 V(W),

where

V(W)=(u1 dot W)^2 + 2(u2 dot W)^2 - 3(u3 dot W)^2.                 (3.2)

The affine coordinates z_j=u_j dot W identify the simplex hyperplane with R^3, and V=z_1^2+2z_2^2-3z_3^2 has gradient zero only at z=0. Thus the pushforward V(W) is absolutely continuous; the single critical point causes no atom.

Moreover u4 dot W=1/2 and orthogonality gives

sum_{j=1}^3 (u_j dot W)^2 = ||W||_2^2 - 1/4 <= 3/4.

Therefore

-9/4 <= V(W) <= 3/2,

so the support of V has length at most 15/4. Since every probability density supported on an interval of length L has essential supremum at least 1/L, (3.2) implies

||p_{Q3|Y4=y}||_infinity >= 4/(15 r^2).                            (3.3)

## 4. The scalar-Q' supremum diverges

On y in (3/2,2), the map b=Q'=(1/2)y^2 is one-to-one. Therefore conditioning on Q'=b is the same conditional law as conditioning on Y4=y=sqrt(2b). Put

r(b)=4-2 sqrt(2b).

As b increases to 2, r(b) decreases to zero, and (3.3) yields

boxed( ||p_{Q3|Q'=b}||_infinity >= 4/[15 r(b)^2] -> infinity ).

Hence for this single admissible target instance

boxed( sup_b ||p_{Q3|Q'=b}||_infinity = infinity ).                (4.1)

Likewise, from (3.1),

boxed( sup_b ||rho_{123|Q'=b}||_infinity^(2/3) = infinity ).       (4.2)

This is a counterexample to the proposed scalar-conditioning worst-level proof gate, not to the QFORM conjecture itself.

## 5. The missing rare-level weight is exactly visible

The failure is caused by conditioning on a vanishing-probability corner shell. Since db/dy=y,

p_{Q'}(b)=p_{Y4}(y)/y = r^3/(3y).                                  (5.1)

Combining (5.1) with the exact conditional projection height (3.1) gives

p_{Q'}(b) ||rho_{123|Q'=b}||_infinity^(2/3)
 = [r^3/(3y)] [3^(2/3)/r^2]
 = 3^(-1/3) r/y.                                                    (5.2)

Thus the coarea-cost density tends to zero linearly at the very levels where the conditional supremum blows up quadratically. Equivalently, after changing variables from b to r, the endpoint contribution to

E ||rho_{123|Q'}||_infinity^(2/3)

is a constant times integral r dr and is finite.

This identifies the exact loss in the owner-proposed supremum reduction: it discards the scalar-level probability weight that compensates the sharpened three-dimensional section.

## 6. Corrected conditional implication

For any regular conditional densities for which the identity is defined,

p_Q(t)=integral p_{Q3|b}(t-b) d mu_{Q'}(b)

implies the source-exact bound

boxed( ||p_Q||_infinity <= E H(Q'),  H(b)=||p_{Q3|Q'=b}||_infinity ).

If the established rank-three coarea inequality gives

H(b) <= K ||rho_{123|Q'=b}||_infinity^(2/3)

for almost every b, then the sufficient scalar-conditioned statement is

boxed( E ||rho_{123|Q'}||_infinity^(2/3) <= C_0 ).                 (6.1)

Unlike the vector-conditioning moment already declared dead in the current owner message, (6.1) conditions only on the one-dimensional scalar Q'. The present corner example does not refute (6.1); it demonstrates exactly why averaging rather than taking sup_b is necessary. Proving (6.1) uniformly, or producing a genuine target counterexample to it, is the next live implication from this mechanism.

## 7. Compatible completed partner result applied

The assigned partner fleet03/B15 run 20260922T173720Z-fleet03-B15-r14, canonical math-open-problems commit 065b515da52986860a862ed50261bfc35b9caa0b, proves that finite algebraic nondegeneracy conditions can be imposed on smooth compactly supported targets without changing the optimal universal height constant, provided the final estimate is uniform in the genericity gap. It uses fleet04/B15's exact equality C_all=C_C0=C_sm.

Applied here, this means the full height problem may be sought on the smooth/generic closure class without separately paying exact zero pivots. The present scalar-sup obstruction is stronger than an exact-degeneracy warning: its matrix already has simple spectrum, is invertible, and has no zero physical entries. Therefore the failure cannot be repaired merely by removing the common algebraic degeneracies licensed by the partner theorem.

A further exact normalization is available on any homogeneous genericity class. If s=s_3(A)>=1 is the third singular value and B=A/s, then s_3(B)=1 and

||p_{X^T B X}||_infinity = s ||p_{X^T A X}||_infinity >= ||p_{X^T A X}||_infinity.

Thus, combined with the partner genericization and smooth-envelope theorem, the extremal universal-height search can be normalized to s_3(A)=1 without loss, while keeping homogeneous nonvanishing conditions. This still does not control the conditional worst-level quantity (4.1).

## 8. Status

FULL QFORM: OPEN. Scalar-Q' worst-level conditional-density bound: REFUTED by the exact source above. Absolute continuity / continuity statements remain separate and are not used to infer the universal height bound.

The mechanism-level replacement is weighted scalar conditioning, equation (6.1), not another regularity assertion. A valid proof must retain the rare-level weight rather than take a supremum over scalar residual levels.

from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write(r'''

## B. Stronger classification: arbitrary continuous displacement costs

The radial assumption can be removed for costs continuous at zero. Let C:R^2->R be continuous. For an oriented red-blue edge use cost C(b-r). Require the universal weak uncrossing inequality

C(b2-r1)+C(b1-r2) <= C(b1-r1)+C(b2-r2)                (B1)

for every proper crossing in general position.

**Theorem.** Property (B1) holds if and only if C(v)=B+h(v), where B is constant and h is continuous, positively homogeneous (h(tv)=t h(v) for t>=0), and subadditive (h(x+y)<=h(x)+h(y)). The strict property holds if and only if, additionally, h(x+y)<h(x)+h(y) whenever x and y are linearly independent. If C is coercive, meaning C(v)->+infinity when |v|->infinity, then there is m>0 with C(v)-C(0)>=m|v| for every v.

**Proof, necessity of positive homogeneity.** Fix a unit vector u and choose unit vectors v_theta tending to u but not parallel to u. Apply (B1) to r1=-a u,b1=b u,r2=-c v_theta,b2=d v_theta, with a,b,c,d>0. Continuity gives precisely (A1) for the ray function f_u(t)=C(tu). Interchanging b,d gives equality. The midpoint and dyadic argument in Section A proves f_u(t)=A_u t+B_u for t>0; the conclusion of affinity in that argument precedes and does not need the scalar sign restriction. By continuity of C at zero, B_u=C(0)=B for every direction. Define h(v)=C(v)-B, including h(0)=0. The ray formula proves h(tv)=t h(v) for t>=0. The coefficient A_u may initially have either sign; no radial symmetry or monotonicity was used.

**Proof, necessity of subadditivity.** For linearly independent x,y and any epsilon>0, put

r1=-x, b1=epsilon x, r2=-epsilon y, b2=y.

The origin is a proper intersection and all endpoints are distinct and in general position. Old edge vectors are (1+epsilon)x and (1+epsilon)y; the swapped vectors are x+y and epsilon(x+y). Substituting C=B+h and using homogeneity, (B1) becomes

(1+epsilon) h(x+y) <= (1+epsilon)(h(x)+h(y)).

Division by the positive 1+epsilon gives subadditivity. For linearly dependent x,y, approximate them by pairs of linearly independent vectors and use continuity of h. Such approximation is possible in R^2 including when one vector is zero; the zero cases also follow directly from h(0)=0. This proves subadditivity everywhere. If (B1) was strict, the same independent-vector configuration proves strict subadditivity for every linearly independent x,y.

**Proof, sufficiency.** Translate an arbitrary proper crossing point to the origin. Write r1=-a u,b1=b u,r2=-c v,b2=d v, where a,b,c,d>0 and u,v are linearly independent unit vectors. The two swapped edge vectors are a u+d v and c v+b u. Subadditivity followed by positive homogeneity gives

h(a u+d v)+h(c v+b u)
 <= a h(u)+d h(v)+c h(v)+b h(u)
 = h((a+b)u)+h((c+d)v).

Adding 2B proves (B1). If h is strictly subadditive on independent vectors, both applications here are strict, giving the strict property. This also proves its asserted converse. No differentiability, symmetry, or positivity of h is needed.

**Proof, coercive growth.** For each unit vector u, if h(u)<=0, then C(tu)=B+t h(u) does not tend to +infinity as t tends to infinity. Coercivity therefore forces h(u)>0 for every unit u. Continuity and compactness of the unit circle give m=min_{|u|=1}h(u)>0. Homogeneity yields h(v)=|v|h(v/|v|)>=m|v| for nonzero v, and the inequality at zero is automatic.

**Corollary: finite-coercive-cost planarity route is impossible.** Let M_n be stationary planar partial matchings on the prescribed independent Poisson input law with unmatched intensity u_n->0. Suppose C satisfies the preceding universal weak uncrossing property, is continuous and coercive, and

sup_n E sum_{r in R_n intersect [0,1)^2, matched} C(M_n(r)-r) <= K < infinity.

The negative part of C is bounded because C=B+h and h>=m|v|>=0. Let lambda_n=1-u_n be the matched red intensity. Then

m E sum_{matched red r in unit square} |M_n(r)-r|
 <= E sum_{matched red r in unit square} (C(M_n(r)-r)-B)
 <= K+|B|.

Consequently the mean matched-length intensities are uniformly bounded by H=(K+|B|)/m. Markov's inequality gives t_n(T)<=H/T. The compactness criterion in ATTEMPT.md Section 3 therefore produces an invariant perfect planar limit.

To verify that this limit has finite mean, rather than only finite-length partners, choose a nonnegative compactly supported continuous f(r), and continuous radial psi:[0,infinity)->[0,1] nonincreasing, equal to one on [0,1] and zero on [2,infinity). Define q_T(v)=|v|psi(|v|/T) for T>=1. The integrand f(r)q_T(b-r) has compact support on the product space. Its integral against eta_n converges along the joint vague subsequence. Its magnitude is bounded by 2T||f||_infinity R_n(supp f), so the Poisson second-moment bound permits passage of expectations. Stationarity and the bound H give E integral f(r)q_T(b-r) eta_n<=H integral f. This bound passes to the limit. As T increases, q_T increases pointwise to |v| because psi is nonincreasing. Monotone convergence yields E integral f(r)|b-r| eta<=H integral f. Stationarity identifies this coefficient as the typical red edge's mean length. Hence that mean is finite, contrary to Theorem 2 of Poisson Matching in d=2.

Thus no such planar nearly perfect family with a uniform expected C-cost can exist. This corollary assumes planarity of the partial matchings: a weak uncrossing cost can have ties, so minimization alone does not force planarity. With the strict property, finite minimizing matchings are automatically planar and the same obstruction applies directly to their proposed uniform cost bound.

**Scope.** This closes the entire continuous, translation-invariant, additive, coercive displacement-cost strategy with universal uncrossing. It does not exclude constructing a planar matching with infinite expected cost, nor minimizing explicitly under non-crossing constraints using a slow cost which itself fails universal uncrossing. The desired tightness requires only a vanishing tail, not any finite first moment.
''')

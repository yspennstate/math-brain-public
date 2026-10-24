# Scalar intersections and a weighted rank-one spectral lead

Status: exact deductions from C006, plus an explicitly open reduction. Root notes do not count as agent executions. No historical novelty is claimed.

## 1. Entire affine lines through a physical diagonal kernel

Let K(s)=K0+sA be Hermitian, and let J be its interval of positive contractions. Suppose K(s0)=D is diagonal and physical for some s0 in J. C006 proves entropy concavity on every segment from D to any other point of J. Every interior point on either side of s0 belongs to the interior of such a segment, so its entropy second derivative is nonpositive whenever the atoms are positive. At a strict diagonal point the Hessian is -sum_i Aii^2/[Dii(1-Dii)] <=0. Thus the full line is concave, including across s0; continuity and common regularization cover boundary points. The same conclusion follows directly by the monotonic one-sided derivatives at s0. If the line lies in a proper spectral face, regularize the whole line and D together, apply the strict argument, and pass to the limit.

In particular let P be ANY fixed orthogonal projection, and K(t)=a(t)P+c(t)(I-P), where both scalars are affine and physical. Write their slopes u,v. If u!=v, the infinite line meets a scalar kernel at

    d = (u*c - v*a)/(u-v).

If d belongs to [0,1], C006 proves concavity on the entire physical part of the line. When u*v<=0 and the slopes are not both zero, d is a convex combination of a and c; consequently EVERY opposite-sign two-value spectral direction is covered, in every dimension and for arbitrary P. Equal slopes with a!=c do not meet a scalar kernel. Same-sign slopes can meet it outside the physical interval; C006 does not settle those cases. A new arbitrary-two-value proof must handle these remaining directions, not just reprove the scalar-intersection consequence.

## 2. Arbitrary rank-one projection as weighted placement of one Bernoulli bit

Let u be a unit vector, w_i=|u_i|^2, P=uu*, and K=a(I-P)+cP with 0<a,c<1. Draw J with probability w_j. Conditional on J=j, draw independent bits with mean c at j and mean a at all other coordinates. This mixture is EXACTLY P_K.

To prove it, set x=a/(1-a) and r=c(1-a)/(a(1-c)). Then L=K(I-K)^(-1)=x[I+(r-1)P]. The determinant lemma gives det L_S=x^|S|[1+(r-1)sum_(i in S) w_i], while det(I-K)=(1-a)^(n-1)(1-c). The mixture's atom at S is

    a^|S|(1-a)^(n-|S|) * [ (c/a) w(S) + ((1-c)/(1-a))(1-w(S)) ],

which equals the L-ensemble atom. Continuity covers a,c in the closed square.

For uniform w, C075 proves the full Hermitian Hessian theorem. For general w the representation reduces joint spectral concavity to a nonuniform distinguished-bit placement entropy inequality. Concavity of each component law's entropy does not imply concavity of the mixture along nonlinear probability paths: its mixing-information term must also be controlled. Section 1 already handles opposite-sign slopes; the missing cases have same-sign slopes with scalar intersection outside [0,1], including common scalar shifts.

This note supplies no proof of that remaining inequality. It is a precise creative lead for the two-value and fixed-eigenbasis assignments.

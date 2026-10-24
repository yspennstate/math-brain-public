SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T15:04:36Z.
attacking: the unpaid N3 one-heavy/shared-diffuse boundary — derive an exact cone-tip extremizer kernel and test whether this near-null stress family can beat 3sqrt(2).

# Early substantive checkpoint

Fix 0<a<=1, d=sqrt(1-a^2), J=diag(1,1,-1), and the orthonormal frame

r=(sqrt((1-a)/2),0,sqrt((1+a)/2)),
b=(sqrt((1+a)/2),0,-sqrt((1-a)/2)),
c=(0,1,0).

In the (r,b,c) physical frame, J has matrix

[[-a,d,0],[d,a,0],[0,0,1]].

Thus if X has any probability density f<=1 and B,C are independent N(0,1/12), independent of X, then the Gaussianized one-heavy limit is

Q_a=-aX^2+2dXB+aB^2+C^2.

Completing the square gives

Q_a=a(B+dX/a)^2+C^2-X^2/a.

For fixed X=x, polar coarea in (sqrt(a)(B+dx/a),C) yields the exact cone-tip kernel

K_a(x)=1/(4*pi*v*sqrt(a)) int_0^{2*pi} exp[-x^2 F_a(theta)/(2v)] dtheta,

v=1/12,
F_a(theta)=(cos(theta)-d)^2/a^2+sin(theta)^2/a.

For every a>0, F_a(theta)>0. Hence K_a is even and strictly decreasing in |x|. The bathtub principle therefore gives the exact cap-one heavy-law optimizer

sup_{0<=f<=1, int f=1} p_{Q_a}(0)=C(a):=int_{-1/2}^{1/2} K_a(x)dx,

uniquely (a.e.) at X~Unif[-1/2,1/2]. Equivalently,

C(a)=sqrt(3/(2*pi*a)) int_0^{2*pi} F_a(theta)^(-1/2) erf(sqrt(3F_a(theta)/2)) dtheta.

This is already a source-valid analytic constraint on an unpaid N3 stress class. The exact finite-dimensional provenance uses one row r, m copies b/sqrt(m), and m copies c/sqrt(m): R_m^T R_m=I_3, so A_m=R_m J R_m^T has exact nonzero spectrum {1,1,-1}. Its 2x2 determinant for the heavy coordinate and any b-bank coordinate is exactly -1/m; all other physical pair determinants are <=1/m, while the heavy diagonal is -a. Thus for any fixed tau>a and all m>1/tau the family lies inside the no-pivot N3 inequalities |A_ii|<tau and |det A_{ij}|<tau.

Remaining this run: prove an analytic strict ceiling at a sharp endpoint, apply account04/B17's weighted local Edgeworth theorem to a finite cap-one family at an actual equation, and record only numerical diagnostics (not proof) for interior a.

# Checks and attempts to break the argument

## The symmetry step

Rotational invariance alone was not used as a justification for averaging
classifiers. Robust 0–1 loss is nonlinear, and a majority vote need not preserve
the loss. The argument instead bounds every classifier below by the average
loss of its meridian sections. The same quotient distribution is present in
each section because the angle is independent of both the label and the
quotient coordinates.

The axis r=0 was checked separately: it does not prevent the ball-image
identity, since the target perpendicular direction can be chosen arbitrarily.
The d=2 case uses a two-point angular law. Coincident means do not require
estimating a direction: choose any line. Both sides of the reduction use
infima, so no unproved existence of a Bayes minimizer is needed.

As a finite independent check, 4,096 arbitrary classifiers were enumerated on
a 12-point space, against the 8 classifiers constant on its angular orbits.
The optimal error numerators at radii 0, .25, .75, 1.1, 2 were respectively
12, 12, 12, 32, 32, each over denominator 64, in both searches. These are
finite analogues, not numerical proofs of the continuous theorem.
An angular law that reveals the label was also tested: unrestricted error
becomes zero while invariant classifiers have error 1/2. The independence
assumption is therefore necessary for the stated proof.

## Geometry and the factors of two

The distance between points with quotient coordinates (t,r) and (s,u), with
angle phi between their perpendicular components, is

\[
 (t-s)^2+r^2+u^2-2ru\cos\phi.
\]

Its minimum over phi is (t-s)^2+(r-u)^2. This derives the quotient metric
independently of the reverse-triangle-inequality argument in PROOF.md.
Direct coordinate checks in dimensions 2, 3, 7, 31 gave maximum aligned
distance error 8.882e-16 over 320 cases, including zero source/target radii.

For the graph construction there are two distinct triangle inequalities.
A source point is within h of its representative. To protect it at radius e,
the interpolation must protect radius e+h around the representative; two
opposite representatives must then be farther than 2(e+h). In the other
direction, witnesses robust at radius e+2h cannot have representatives within
2(e+h), because their own distance would be at most 2(e+2h). Their midpoint
would require both labels. Closed balls mean that equality is a conflict,
so graph edges use <= and independent pairs have strict > separation.

A one-dimensional fault case catches omission of the first factor two:
centers at 0 and 1.5 with attack radius 1 have overlapping balls. Treating
them as independent would wrongly count both as correct. The check detects
the change from independent-set weight 1 to the incorrect weight 2.

For l_infinity the quotient metric used here fails. Starting at perpendicular
coordinate (1,0), the change (.1,.1) has l_infinity norm .1 but changes the
radial coordinate by sqrt(1.22)-1=.1045361017. Thus the Euclidean quotient
ball argument cannot be silently extended to l_infinity.

## An independent derivation of the dilation bound

The proof uses Gaussian KL and Pinsker. A different derivation uses the
derivative of a scaled density. If p is the density of N(mu,sigma^2 I) and
p_a(x)=a^d p(ax), then

\[
 \partial_a\log p_a(x)=\frac1a
 \left[d-\frac{(ax)\cdot(ax-\mu)}{\sigma^2}\right].
\]

Under p_a, put ax=mu+sigma G. The expression in square brackets becomes
d-||G||^2-(mu/sigma) dot G. Its mean is zero and its variance is
2d+||mu||^2/sigma^2: the mixed term vanishes by oddness of Gaussian third
moments. Therefore Cauchy–Schwarz and integration of the density derivative
give

\[
 \operatorname{TV}(P_a,P_1)
 \le\frac12\sqrt{2d+\|\mu\|^2/\sigma^2}\log a
 \le(a-1)(\sqrt d+\|\mu\|/\sigma),\quad a\ge1.
\]

The derivative has integrable Gaussian polynomial moments, so this
integration is justified; its integral is a uniform bound on the L1
difference of the endpoint densities. This independently confirms the
constant K_0 used to remove radius slack. It also shows the restriction
a<=2 in the KL proof is more than is needed for this weaker final bound.

Direct quadrature of expectations of log density ratios agrees with the
closed-form dilation KL in three unequal-mean/scale examples to better than
1e-11. The maximum tested ratio of the scalar dilation expression to its
bound 2t^2 was .998335581, so the check includes a nearly tight case.

## Statistical estimates and graph weights

The mean-error bound was re-derived by writing each coordinate of the sample
mean as sigma G_i/sqrt(m), giving sigma^2 chi_d^2/m for its squared error.
For the scale estimate, the complete sum is sigma^2 chi_{ld}^2, whose mean
is ld sigma^2 and variance 2ld sigma^4. These reproduce the coordinatewise
moment calculations in the proof.

The four estimation events each fail with probability at most alpha/8:
two means and two scales give total alpha/2. The synthetic sampling step
uses failure probability alpha/2. A TV discrepancy b is paid twice when
transferring an excess risk: once for the returned classifier, once for
the optimal risk. With b=eta/8 and population excess eta/2, total excess
is 3eta/4, leaving slack in the stated eta guarantee.

The graph optimizer was checked against exhaustive enumeration of all
1,024 vertex subsets on each of 80 integer-weighted problems. Zero weights,
coincident centers, complete graphs, and distance-equality edges were
included. Max-flow and exhaustive optima agreed in every case.

The interpolation step was checked independently of the training grid on
N(-2,1) versus N(2,1). For e=.25, h=.2, sources truncated to [-6,6],
the script builds the graph classifier, merges its positive intervals,
and integrates its eroded/dilated decision region using normal CDFs.
It verifies the nonvacuous inequality (8) against the exact robust optimum
at e+2h. For this benchmark, the latter is Phi(e+2h-2): the sign classifier
achieves it, and an attacker shifting the two labels toward each other by
e+2h gives the ordinary Bayes lower bound. All parameters are below mean
2, so this benchmark formula is used within its valid range.

## Remaining limitations

The theorem is in a real-arithmetic model and has polynomial dependence on
numeric bounds M,S,1/e; it is not a polynomial bit-complexity theorem uniform
over exponentially ill-scaled inputs. It gives additive error and a crude
sample bound, not an optimal minimax rate. No general covariance theorem,
natural-distribution hardness result, or l_infinity extension was obtained.
The literature check is too short to establish novelty of the assembled
spherical-Gaussian result. The mathematical result is self-contained.

The program checks the proof's geometry, constants, and finite optimization
components. It does not implement or benchmark the full high-dimensional
learner; its worst-case polynomial grid can be impractically large.

# Independent checks of the centered insertion bound

## The energy identity using replacement pairs

Let X_i' be an independent uniform replacement, and write L_n^{(i)}
for the resulting optimum tour length. Conditional on S_i=X_{-i},
the two insertion costs d(X_i;S_i) and d(X_i';S_i) are independent
with the same law. Therefore

\[
 \frac12\mathbb E[(L_n-L_n^{(i)})^2]
 =\mathbb E\operatorname{Var}(d(X_i;S_i)\mid S_i).
\]

The orthogonal expansion makes the left side equal to
sum_{A:i in A} E h_A^2. Summing over i gives exactly
E_n=sum_j j V[n,j]. Thus the factor n in (6) of PROOF.md is correct;
there is no additional factor 2 in the new bound.

This also independently rechecks the previous result: nonnegative
insertion costs bounded by 2R give
(d-d')^2<=d^2+(d')^2<=4R^2+4(R')^2.
Half the sum over i is at most 4n E R^2. With the exact nearest-distance
limit n E R^2 -> 1/pi, the previous 4/pi bound follows.

## The constant from truncated moments

Let Z have tail exp(-pi z^2), and put W=pi Z^2. Then W has the
exponential density exp(-w) on w>=0. Write a=sqrt(pi)c.
Direct integration, rather than the tail formula for H_c, gives

\[
 \mathbb E[W\mathbf1_{W>a^2}]=(a^2+1)e^{-a^2},
\]

and, substituting w=t^2 and integrating by parts,

\[
 \mathbb E[\sqrt W\mathbf1_{W>a^2}]
 =\int_a^\infty2t^2e^{-t^2}\,dt
 =ae^{-a^2}+\frac{\sqrt\pi}{2}\operatorname{erfc}(a).
\]

Since the endpoint (2Z-c)^2 exceeds c^2 precisely when Z>c,

\[
 \begin{split}
 \pi\mathbb E H_c(Z)
 &=a^2+4\mathbb E[(W-a\sqrt W)\mathbf1_{W>a^2}]\\
 &=a^2+4e^{-a^2}-2a\sqrt\pi\operatorname{erfc}(a).
 \end{split}
\]

Dividing by pi agrees with F(c) in PROOF.md. At c=0 it is 4/pi,
recovering the old estimate exactly. For large c, F(c)>=c^2, so its
minimum cannot run off to infinity.

As another check, at the stationary point E[2Z 1_{Z>c_*}]=c_*.
Its variance computed without the centered-square expression is

\[
 4\mathbb E[Z^2\mathbf1_{Z>c_*}]-c_*^2
 =4(c_*^2+1/\pi)e^{-\pi c_*^2}-c_*^2.
\]

Using the stationary equation to eliminate erfc in F(c_*) yields
this same expression. This checks the center, threshold, and coefficients
independently of the integral in (11).

## The derivative checked through threshold moments

For fixed z, the larger endpoint is c^2 when z<c and (2z-c)^2
when z>c. The values agree at z=c, so differentiation under the
Rayleigh integral gives

\[
 F'(c)=2c-4\mathbb E[Z\mathbf1_{Z>c}].
\]

The density of Z is 2pi z exp(-pi z^2). Consequently

\[
 F''(c)=2+4c(2\pi c)e^{-\pi c^2}
        =2+8\pi c^2e^{-\pi c^2}.
\]

These are exactly the derivatives in PROOF.md. In particular strict
convexity, rather than an unverified numerical minimization, proves
uniqueness of c_*.

## The strict bound checked as a direct integral inequality

Set c=1/sqrt(pi). The truncated-moment formula above gives

\[
 \pi F(c)=1+4/e-4\int_1^\infty e^{-t^2}\,dt.
\]

The identity

\[
 \frac{d}{dt}\left(\frac{e^{-t^2}}t\right)
  =-2e^{-t^2}-\frac{e^{-t^2}}{t^2}
\]

integrated from 1 to infinity implies

\[
 1/e=2I+J<3I,
 \quad I=\int_1^\infty e^{-t^2}\,dt,
 \quad J=\int_1^\infty t^{-2}e^{-t^2}\,dt<I.
\]

Thus pi F(c)<1+8/(3e)<2. The sign of the strict inequality and
both factors of 2 agree with the main proof. This establishes a strict
factor-of-two improvement over the old 4/pi upper bound, without using
floating-point values of pi, e, or erfc.

## Endpoint and conditional-centering tests

- If d=0, the new squared error is c^2 after scaling, exactly one
  endpoint of H_c. If d=2R, it is (2sqrt(n)R-c)^2, the other
  endpoint. For an intermediate d, convexity bounds it by their maximum.
  The threshold is Z=c, not Z=c/2: solving
  (2Z-c)^2=c^2 gives Z=0 or Z=c.
- At n=2, the base set is a singleton and d=2R identically. The exact
  identity is E_2=2 E[Var_X(2|X-Y| | Y)]. The centering step reads
  2 Var_X(2|X-Y| | Y)<=E_X[(2sqrt(2)|X-Y|-c)^2 | Y],
  which follows from the elementary least-squares property for every Y.
  Thus the case attaining the insertion bound does not invalidate the
  nonzero center. No asymptotic claim is applied at n=2.
- Conditional centering requires a constant only with respect to X.
  T(S)+c/sqrt(n) is such a constant. It need not equal the actual
  conditional mean, and no sign or asymptotic value of that mean is used.
- Nonnegativity d>=0 is essential. An absolute bound |d|<=2R alone
  would permit negative endpoints and would not justify H_c.

## Boundary and limit checks

- The homothetic area estimate is valid up to distance sqrt(2), including
  corners. No quarter-disk formula at large radii is assumed.
- The Rayleigh limit is only used for almost every fixed interior point.
  The boundary has area zero, but that fact alone would not control
  expectations. The separate uniform Gaussian tail exp(-r^2/4)
  supplies the needed integrable majorant for (10).
- n-1 points remain after deletion; the normalization sqrt(n) gives
  (1-pi r^2/n)^{n-1}, whose limit is exp(-pi r^2). Replacing n by
  n-1 in the limit would give the same law, but no such replacement is
  made in a finite-n identity.
- c_* is a fixed number independent of n. There is no unjustified
  interchange of an infimum and a limit: (11) is applied at that one c_*.
- Repeated locations, ties between nearest points, and nonunique tours
  are harmless; the insertion competitor and shortcut argument do not
  use uniqueness.

## Attempts to infer more than the bound

The scalar sharpness example in PROOF.md prevents improving kappa using
only the limiting marginal nearest distance and the constraint 0<=Y<=2Z.
It is not a TSP model, does not enforce spatial continuity of insertion
costs, and does not show the actual interaction energy approaches kappa.

A stronger energy bound still does not force convergence. For an explicit
test, let independent signs Z_i take values +/-1 equally likely, and set
G_n=(a_n/sqrt(n))sum_i Z_i, with a_n=1/10 for even n and 1/5 for
odd n. This symmetric product-space variable has only order-one energy,
and its variance alternates between 1/100 and 1/25. To check that these
values fit below the new bound, the scalar feasible choice Y=Z has
Var(Z)=1/pi-1/4, so kappa>=1/pi-1/4>3/44>1/25 using pi<22/7.
This example is only a test of the abstract inference. It shows why the
new bound leaves the geometric convergence problem intact.

No contradiction to the new inequality or the earlier reduction was found.
No simulation or numerical claim about the limiting TSP variance is made.

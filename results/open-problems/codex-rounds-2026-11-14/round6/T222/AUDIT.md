# Independent checks of the energy–projection tradeoff

All checks below are analytic. No numerical optimization, simulation,
or exact-TSP computation was run.

## 1. A scalar moment problem gives the coefficient independently

Let Z have survival function exp(-pi z^2). For each m in [0,1], let
psi(m) be the largest E Y^2 over all couplings with
0<=Y<=2Z and E Y=m. For 0<m<1 define t>0 by

\[
 m=M(t):=\mathbb E[2Z\mathbf1_{Z>t}]
       =2t e^{-\pi t^2}+\operatorname{erfc}(\sqrt\pi t).
 \tag{A1}
\]

M decreases continuously from 1 to 0, since
M'(t)=-4pi t^2 exp(-pi t^2)<0 for t>0. Thus t exists and is unique.

The endpoint maximum of the convex function y^2-2ty on [0,2z] is
4z(z-t)1_{z>t}. Therefore every admissible Y satisfies

\[
 \mathbb E Y^2\le2tm+4\mathbb E[Z(Z-t)\mathbf1_{Z>t}].
 \tag{A2}
\]

Equality holds for Y=2Z1_{Z>t}, whose mean is m by construction.
Using the exponential variable pi Z^2 gives

\[
 \psi(m)=4\mathbb E[Z^2\mathbf1_{Z>t}]
       =4(t^2+1/\pi)e^{-\pi t^2}.
 \tag{A3}
\]

At the endpoints psi(0)=0 and psi(1)=4/pi, by nonnegativity of Y
and 2Z-Y. The formulas extend continuously there.
Differentiating (A3) in t gives -8pi t^3 exp(-pi t^2), so division
by M'(t) gives

\[
 \psi'(m)=2t,\qquad
 \psi''(m)=-\frac1{2\pi t^2e^{-\pi t^2}}\le-\frac e2.
 \tag{A4}
\]

The last inequality uses s exp(-s)<=1/e, with s=pi t^2.
The upper bound on the second derivative is attained at t=1/sqrt(pi).
Thus the factor e/2 has the correct direction and factor of two.

The minimizer equation for c_* is exactly M(c_*)=c_*. In particular
c_* lies in (0,1), psi'(c_*)=2c_*, and

\[
 \psi(c_*)-c_*^2=\kappa.
 \tag{A5}
\]

For (A5), substitute erfc(sqrt(pi)c_*)=c_*-2c_* exp(-pi c_*^2)
into F(c_*). Integrating (A4) twice around c_* gives

\[
 \psi(m)\le\psi(c_*)+2c_*(m-c_*)
                           -\frac e4(m-c_*)^2.
 \tag{A6}
\]

For interior m this follows by Taylor's formula with integral remainder;
continuity supplies m=0 and m=1. Hence every coupling above satisfies

\[
 \mathbb E(Y-c_*)^2+\frac e4(\mathbb E Y-c_*)^2\le\kappa.
 \tag{A7}
\]

This independently recovers the profile penalty e/4 from a constrained
moment maximization, rather than from F's upper curvature. If the
Rayleigh conditional law held exactly at every query position, applying
(A7) at each position and integrating would give (29) in PROOF.md
with zero error. The real finite-sample law is not exactly Rayleigh;
the uniform error in that proof is essential to transfer the inequality.

## 2. A second expansion through the quadratic dual

Put G(c)=F(c)-c^2, using the negative-center extension in PROOF.md.
For c<0, G(c)=-2c+4/pi and G''(c)=0. For c>=0,

\[
 G''(c)=8\pi c^2e^{-\pi c^2}\le8/e=2/\alpha.
\]

Also G'(c_*)=-2c_*. The global Taylor bound becomes

\[
 G(c_*+v)\le G(c_*)-2c_*v+v^2/\alpha.
 \tag{A8}
\]

The scalar endpoint inequality can be written as
y^2<=2cy+H_c(z)-c^2. At a fixed query position with mean u, the
limiting right side is 2cu+G(c). Choose
c=c_*-alpha(u-c_*), write a=u-c_*, and use (A8):

\[
 \begin{split}
 2cu+G(c)
 &\le2c_*u-2\alpha au+G(c_*)+2\alpha c_*a+\alpha a^2\\
 &=2c_*u+G(c_*)-\alpha a^2.
 \end{split}
\]

After subtracting 2c_*u-c_*^2 this is again (A7). At finite n,
integration incurs at most D_n(M). This checks the adaptive-center
sign and the cancellation yielding exactly alpha, without expanding
the same square as the main proof.

## 3. Conditional variances and normalization

Let X,X' be independent query points given S. Since Y_n is sqrt(n)
times insertion cost,

\[
 \tfrac12\mathbb E(Y_n(X,S)-Y_n(X',S))^2
       =\mathbb E_S\operatorname{Var}_X(Y_n\mid S)=E_n.
 \tag{A9}
\]

For the other conditioning, first average over S. The corresponding
replacement-pair identity is

\[
 \tfrac12\mathbb E(U_n(X)-U_n(X'))^2=V_{n,1}.
 \tag{A10}
\]

These are not interchangeable. Independently decomposing around the
common mean mu_n gives

\[
 \operatorname{Var}_{X,S}(Y_n)=E_n+W_n.
\]

Consequently the left side of the adaptive-center inequality is exactly
`E_n+W_n+alpha V[n,1]+(1+alpha)(mu_n-c_*)^2`.
The coefficient of the squared mean error is 1+alpha, not 1-alpha.
No additional n multiplies V[n,1] or W_n.

## 4. Boundary, centers, and smallest sample size

The uniform envelope argument uses a deterministic function of x:
U_n(x) already averages over S. It would be invalid to condition the
nearest-distance law on an arbitrary center that also depends on S.
That dependence does not occur here.

The centers are uniformly bounded because U_n lies in [0,2sqrt(2)].
They need not converge. Their possible negativity is handled by the
exact formula H_c(z)=(2z-c)^2 for c<0. Its expected value is
c^2-2c+4/pi; at zero its value and first two derivatives agree with
the positive-center formula. Omitting this extension would leave a
gap for small n or near the boundary.

For every n>=2, the whole-square domination exp(-r^2/4) applies.
The integral of (8r+4M) times this Gaussian tail is finite. The boundary
itself has area zero, but that fact alone would not justify discarding
a shrinking strip with potentially large values. The uniform Gaussian
domination justifies convergence of the entire double integral (17).
It also controls the unbounded r range. No full-disk binomial formula
is used at a boundary point or before the disk fits.

At n=2 the base S is a singleton and insertion equals 2R exactly.
The finite-n endpoint inequality remains valid; D_2(M) need not be
small. Thus no asymptotic nearest-distance law has been applied to a
singleton sample. Repeated sample locations, nonunique nearest points,
and nonunique tours leave all inequalities unchanged.

## 5. Total-variance constant by weighted quadratic minimization

The exact spectral subtraction is

\[
 E_n+V_{n,1}-2\operatorname{Var}(L_n)
                  =\sum_{j\ge3}(j-2)V_{n,j}\ge0.
\]

For an independent check of the completion in (34), set
a=1-alpha, b=1+alpha. Both are positive and a+b=2. Maximizing

\[
 a\mu(1-\mu)-b(\mu-c_*)^2
\]

is the same as minimizing
a(mu-1/2)^2+b(mu-c_*)^2, then adding a/4. The minimum of those
two weighted squares is
ab(c_*-1/2)^2/(a+b). This gives

\[
 \frac{1-\alpha}{4}
                -\frac{1-\alpha^2}{2}(c_*-1/2)^2.
\]

Division by two gives the coefficients 1/8 and 1/4 in the final
variance bound. The maximizer is
mu=1/2+(1+alpha)(c_*-1/2)/2; no convergence to it is asserted.

The old isolated-site deficit obeys
eta(c)<=1/(5184 pi e^2), rederived from the maximum of t^2 exp(-t)
at t=2 with t=9pi c^2. The simpler new bound differs from the old
one by exactly e/32-eta(c_*)/2>0. Its sign already follows from
1/32>1/10368, using pi>1 and e>1. The further squared-mean correction
only strengthens the comparison. No decimal optimization is hidden in
the statement.

## 6. Attempts to infer convergence fail

The new inequalities still permit multiple subsequential spectra.
For example, at the level of these numerical constraints set
mu_n=c_*, W_n=0, V[n,1]=0 and all energies except order two equal
to zero. Let V[n,2] alternate between kappa/8 and kappa/16.
Then E_n alternates between kappa/4 and kappa/8, and the tradeoff
holds with room to spare. The prior first-projection inequality also
holds because 0<c_*<1. These arrays are not claimed to arise from
TSP insertion costs; they show that the proved inequalities do not
force uniqueness of a subsequential variance limit.

The scalar extremizer 2Z1_{Z>c_*} has mean c_* and makes (A7) an
equality with no profile variation. Nearby two-type conditional means
c_*+h and c_*-h have maximal second moments averaging to
psi(c_*)+psi''(c_*)h^2/2+o(h^2). Equation (A4) makes the quadratic
loss at least (e/4)h^2. This verifies the direction of the penalty:
variation of conditional means reduces achievable insertion error.
It does not force that variation to vanish for actual tours.

No counterexample to the theorem or its finite-n error estimate was
found. No convergence of V[n,1], E_n, W_n, mu_n, fixed-noise covariance,
or Var(L_n) is established.

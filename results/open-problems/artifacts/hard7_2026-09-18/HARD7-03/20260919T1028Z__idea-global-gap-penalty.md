# HARD7-03 idea before code — replace the hard local-minimum event by a global negative-gap penalty

The preceding checkpoint lower-bounded the exact fresh-layer triple slack only on

\[
E_d=\{S_d\le S_{d-1},\ S_d\le S_{d+1}\},
\]

where both predecessor gaps

\[
u=S_{d-1}-S_d,\qquad v=S_{d+1}-S_d
\]

are nonnegative.  This still throws away every configuration outside `E_d`, even though the exact conditional slack

\[
\Phi_\theta(u,v)=\theta\int_0^\infty e^{\theta t}(1-e^{-t})
 e^{-(t-u)_+-(t-v)_+}\,dt
\]

is positive everywhere.

The new route is to avoid another hard sufficient event.  For every real `u` and every `t>=0`,

\[
e^{-(t-u)_+}\ge e^{\min(u,0)}e^{-t}.
\]

The same inequality for `v` gives the global pointwise envelope

\[
\boxed{\Phi_\theta(u,v)\ge
 \kappa(\theta)e^{\min(u,0)+\min(v,0)}},\qquad
\kappa(\theta)=\frac{\theta}{(2-\theta)(3-\theta)}.
\]

It is exact throughout the southwest quadrant `u<=0,v<=0`; hence no larger universal multiplicative constant can replace `kappa` in this particular separable envelope.

For the sliding maxima here the two downward penalties cannot occur simultaneously: if `S_d>S_{d-1}`, the endpoint entering the middle window from the right is responsible for the strict increase and is also present in the right-neighbour window, so `S_{d+1}>=S_d`; the reflected statement is identical.  Thus

\[
D_d=(S_d-S_{d-1})_+ +(S_d-S_{d+1})_+
\]

has at most one nonzero summand, and the full correction becomes

\[
R_d(\theta)\ge \kappa(\theta)
 E[e^{\theta S_d-D_d}].
\]

This strictly contains the preceding local-minimum contribution: on `E_d`, `D_d=0`; on its complement one pays exactly one exponential gap instead of discarding the configuration.

Three unused section-B moves drive this iteration:

- **B7 TAKE THE LIMIT.** Send one predecessor gap to `-infinity` in the exact `Phi` integral.  The surviving first-order factor is `e^{u}` (and `e^{u+v}` when both gaps are negative), which identifies the correct exponential gap penalty rather than another indicator event.
- **B9 RANDOMIZE.** Introduce an independent `Z~Exp(1)`.  Since `e^{-D_d}=P(Z>D_d | D_d)`, the soft penalty is a randomized acceptance rule that keeps *all* predecessor configurations.  This is the probabilistic replacement for the previous deterministic local-minimum filter.
- **B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.** Conditional on the first-layer `A` variables, the complement terms are transforms of maxima of shifted independent exponentials.  The same inclusion-exclusion / hypoexponential order-statistic algebra that produced the earlier target-max weights gives finite rational cone integrals for these new soft-penalty terms.  In particular the edge complement has an independent closed form, providing a nontrivial exact identity check.

Before writing a checker, the complement decompositions to integrate are:

\[
P_2=E[e^{(\theta-1)Y_1+Y_2};\ Y_1>Y_2],
\]

\[
P_{10}=E[e^{(\theta-1)Y_0+\max(Y_1,Y_2)};\ Y_0>\max(Y_1,Y_2)],
\]

\[
P_{12}=E[e^{(\theta-1)Y_2+\max(Y_{-1},Y_0,Y_1)};
 Y_2>\max(Y_{-1},Y_0,Y_1)],
\]

and, for the central triple,

\[
P_{01}=E[e^{(\theta-1)Y_1+\max(Y_{-2},Y_{-1},Y_0)};
 Y_1>\max(Y_{-2},Y_{-1},Y_0)],
\]

with reflection supplying the other half.  Therefore the proposed global four-step correction is

\[
H_{\rm full}=H_{\rm loc}+\kappa(\theta)
\{2P_2+2(P_{10}+P_{12})+2P_{01}\}.
\]

The next step is an exact six-order-cone integration of these four transforms and then a single rational Chernoff certificate.  No simulation or finite-size particle-system inference is involved.
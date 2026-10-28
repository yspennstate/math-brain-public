# P0266/P0267: critical-noise endpoint review

The numbered general questions are the targets. No additional restricted continuity
variant is claimed resolved.

## Exact hypotheses and source scope

The complete observed candidate was read. Its committed hash 5a4a9e118c4d87d2aa641c3b2d038179779ffc8d326b99fd16ca1a2a294c190a
was compared against the observed 3afdb8adf2e2b58a7778f807a90283741394c8203e9541e160ca7cc6f55be870:
only five replacements of encoding artifacts in Allen-Cahn, Ito and Holder differed.
All equations remained identical. The journal PDF was archived and its hash
recorded. Pages 65–69, 71–75 and 130–132 were read; page 131 was also rendered and
visually inspected. Assumption 6.1 and Theorem 6.4 impose exactly the local
Lipschitz and coercivity conditions used below. The explicit model in Problem 4
allows a scalar Brownian driver on the one-dimensional torus.

Take the real Gelfand triple V=H=V*=R, A=I, B=0, F(v)=2v-v^3, G(v)=sqrt(2)v^2.
Finite-dimensional real Hilbert spaces are allowed. For beta=2/3 and rho=2 the
critical-index inequality is an equality. The polynomial local Lipschitz estimate
holds, since all interpolation norms on this triple are proportional to absolute
value. Linear coercivity holds with theta=1, M=0. Nonlinear coercivity is

    v(Av-F(v)) - |G(v)|^2/2 = -v^2 >= v^2 - 2v^2 - 2.

Thus theta'=1 and M'=2 are valid. In particular, the absence of a strict extra
noise margin is permitted by Theorem 6.4. Subsection 6.3.1 explains why adding
such a margin would be a stronger hypothesis; it is not silently available here.

For the torus model, use V=H^1, H=L^2 and A=I-Delta. The constant subspace is
invariant. The same nonlinear coercivity calculation gives ||grad v||^2-||v||^2.
Real interpolation at beta=2/3 embeds into H^(1/3), and in one dimension the latter
embeds into L^6. This bounds the cubic drift in L^2, hence H^-1, and the quadratic
diffusion in L^2 by using L^4. The finite-dimensional example already suffices to
refute both general assertions; the torus example also matches the explicit model.

## Independent transformation through the inverse square

Starting directly from dU=(U-U^3)dt+sqrt(2)U^2 dW, let X=U^-2. Ito differentiation
gives

    dX = (8-2X)dt - 2 sqrt(2X)dW.

The contribution six in the drift comes from the second derivative; omitting it
would give the wrong Bessel dimension. Reversing Brownian sign, this is a CIR
process. Its explicit squared-Bessel representation is

    X_t = 2 exp(-2t) Y_s(t),   s(t)=(exp(2t)-1)/2,
    dY_s = 4 ds + 2 sqrt(Y_s)dB_s,
    Y_0 = 1/(2a^2).

The square root R=sqrt(Y) is BES(4). Inverting X recovers the candidate's formula
U_t=exp(t)/(sqrt(2) R_s(t)). This route independently checks the coefficient,
dimension and time scale. A four-dimensional Brownian radial construction gives
a weak positive solution. Local pathwise uniqueness and localization yield a
global strong solution for a prescribed scalar Brownian driver. Countably many
positive deterministic starts may therefore use the same driver.

The radial process does not hit zero. One direct justification uses the bounded
stopped local martingale |x+B|^-2 at first entrance into the ball of radius b>0.
It bounds the probability of that entrance before any fixed S by b^2/r^2. Letting
b decrease to zero proves non-hitting over each finite interval. Continuous paths
therefore have a strictly positive minimum on each compact interval, excluding
finite-time explosion of U. This does not imply integrability of its supremum.

## Independent Gaussian potential calculation

Let |x|=r>0 and let Z be a centered four-dimensional Gaussian with covariance SI.
Newton's shell identity gives the spherical average of |x-Z|^-2 at radius rho as
1/max(r,rho)^2. For rho<r this follows from the mean-value property of the harmonic
kernel in its source variable; for rho>r the shell potential is constant inside
the shell and equals rho^-2 at the center. The radial Gaussian density is
rho^3 exp(-rho^2/(2S))/(2S^2). Consequently

    E |x+Z|^-2
      = r^-2 integral_0^r rho^3 exp(-rho^2/(2S))/(2S^2) d rho
        + integral_r^infinity rho exp(-rho^2/(2S))/(2S^2) d rho
      = (1-exp(-r^2/(2S)))/r^2.

This is a second route to the candidate's Laplace-transform calculation. The
checker differentiates both radial primitives and verifies the combined formula.
It also checks the radial heat equation and the finite limit 1/(2S) at the origin.
No stochastic simulation, sampled tail fit or numerical integral establishes it.

## Finite-horizon tail, with stopping justified

For 0<b<r, stop h(R)=R^-2 at tau_b, the first entrance into radius b. The stopped
process is bounded by b^-2 and is therefore a true martingale on every finite
interval. At time S it gives exactly

    P(tau_b<=S)/b^2 = 1/r^2 - E[R_S^-2; tau_b>S].

The terminal inverse square is integrable by the preceding Gaussian calculation.
Non-hitting and continuity imply that the indicator on the right tends to one
almost surely as b decreases to zero. Dominated convergence therefore yields

    lim_b->0 P(tau_b<=S)/b^2 = exp(-r^2/(2S))/r^2 > 0.

This constant is strictly positive for every S>0, however small. The identity is
finite-horizon throughout; the eventual hitting probability is not substituted.
For M_S=sup_{s<=S} 1/(2R_s^2), the tail is asymptotic to
exp(-r^2/(2S))/(2r^2 x). Its integral diverges logarithmically. Since exp(2t)>=1,
the expected supremum of U_t^2 on [0,T] is also infinite for every a,T>0.

## Consequences, and the moment distinction

Problem 4 fails even for a smooth deterministic positive constant initial function.
For Problem 5, use a_n=1/n and the zero limit with a common Brownian driver. The
zero solution stays zero. Every positive-start solution has infinite expected
squared uniform norm on [0,T], so convergence in the stated L^2 energy topology
is impossible. The time-integrated term cannot repair a norm that already contains
this uniform-in-time term. Probability convergence and p<2 conclusions are untouched.

At any fixed positive time the second moment is finite and is exactly the candidate's
formula. The fourth moment is infinite: the four-dimensional Gaussian density is
positive near the origin, while inverse fourth power gives the radial integral of a
positive multiple of rho^-1 near zero. Thus 'all fixed-time moments are finite' would be
wrong.

The original SDE generator also gives L(U^2)=2U^2. Treating its unlocalized
stochastic term as an integrable, mean-zero martingale would incorrectly infer an
equality for the second moment. The strict local-martingale loss is exactly what
the explicit Gaussian formula detects. A moment identity from formal Ito algebra
alone is not a valid expectation argument.

## Limits and strongest counter-case

An extra coercivity margin, a different integration convention, or excluding
spatially constant scalar noise could defeat the candidate. The exact numbered
questions and their hypotheses were checked directly and do not impose them.
The surrounding prose after Problem 5 discusses additional mapping conditions;
this review claims only the numbered general statement, not every narrower variant.

The 2026 singular-times paper was checked in selected introduction and main-result
pages, not in full. Its energy assumptions and fractal-dimension conclusions in
those pages do not settle this endpoint question. The survey's reference 43 is
the 2012 parabolicity paper by Brzezniak and Veraar; only its primary abstract was
reviewed here. Focused searches did not verify a later resolution. None of this
proves present-day openness or originality. The Bessel mechanism is classical;
the novelty question concerns its application to these exact survey questions.

Primary references:

- https://repository.tudelft.nl/file/File_783e6459-5d3b-4957-bcd3-64da5b8d9025
- https://arxiv.org/abs/2501.18561
- https://arxiv.org/abs/2602.21981
- https://arxiv.org/abs/1104.2768

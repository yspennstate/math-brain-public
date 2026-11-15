# Checks and attempted failures

The result is confined to a strict invariant cone in dimension one. It is
not a solution for a full Gaussian law in general dimension.

1. **Risk normalization:** direct Gaussian integration gives a half-line
   input second moment 1/2, so the half-square-loss risk is sum e_s^2/4.
   Independently, the particle product rule gives -R'=sum e_s^2 q_s/4,
   equal to the squared transport velocity. The exact fraction arithmetic
   in verify.py checks the same equality without numerical differentiation.

2. **Gaussian conditioning and sector masses:** polar radial independence
   gives q_s=1 and m_s=0. Independently, Cartesian integration uses
   integral_{-w}^w phi(a) da=erf(w/sqrt(2)) and
   integral_{-w}^w a^2 phi(a) da=erf(w/sqrt(2))-2w phi(w).
   The conditional density has factor 2. These yield the two independently
   computed q values in LOG.md. The omitted q tail beyond 10 is bounded
   by 2(10+2/10)phi(10)<1.6e-21 in the Cartesian integral, using
   integral_T^infinity phi <= phi(T)/T. The polar q tail is exactly
   51 exp(-50)<1.0e-20. Both are far below the numerical tolerances.

3. **Invariant and rate constants:** multiplication of the hyperbolic matrix
   gives q^2-4m^2=D^2. Independently, the product rule gives
   m'=-eq/2 and q'=-2em, whose invariant derivative is identically zero.
   Therefore (e^2)'=-q e^2 and the exponent in risk is D, while the exponent
   in the W2 distance is D/2. The time normalization is R=half square loss;
   changing that convention changes the time scale.

4. **Parameter law versus risk:** convergence is established by an explicit
   coupling of limiting and current characteristics. No compactness argument
   or identification of a weak limit is substituted for W2 convergence.
   Uniform second moments follow from bounded hyperbolic clocks. The
   sharper coupling constant Q comes from an L2 path integral, and the
   deterministic grid also checks the coupling cost directly.

5. **The metric meaning of the flow:** a transport Taylor estimate handles
   arbitrary destinations, including displacements crossing w=0, because
   the source law has |a|<|w|. This verifies the local metric slope and the
   energy dissipation identity. Well-posedness is claimed in the explicit
   self-consistent characteristic class. The proof does not assert that all
   possible nonsmooth metric definitions everywhere have a common flow.

6. **No uniform cone margin:** individual particles can start arbitrarily
   close to the boundary or the origin. Positivity of each of b+a and b-a
   suffices. The uniqueness argument is per initial particle and avoids
   assuming a positive first collision time for the entire population.

7. **Outside-cone failure:** (a,b)=(2,1) reaches b=0 at
   u=-atanh(1/2), leaving a=sqrt(3). This is a genuine obstruction to the
   sector-preserving calculation for a full Gaussian. Absorbing that mass
   would change q' and can be incompatible with a metric steepest-descent
   interpretation. No such extension is claimed.

8. **Balanced boundary failure:** for a=-b, b>0, positive teacher c, a
   one-neuron law has m=-b^2, q=2b^2 and D=0. Its evolution satisfies
   b'=-(b^2+c)b/2, so b tends to zero and the risk tends to c^2/4. Thus
   permitting the closed cone without another nondegeneracy condition
   would invalidate the theorem. This is outside its strict-cone hypothesis.

9. **Zeros and signs:** c_+,c_- can have either sign independently. A sector
   with m_s^0=c_s has u_s^*=0 and is stationary; no division by its residual
   occurs. An absent sector can fail to fit a nonzero target coefficient,
   which is why the theorem assumes positive mass in both sectors.

10. **Prior-work memory:** the whole-card recall confirms the conditional
    nature of the Chizat-Bach theorem and gives the individual balance law.
    An older finite-particle numerical card includes the assertion that
    particles with a=0 are frozen. That assertion is false for the present
    equations: if b>0 and e_s!=0 then a'=-e_s b/2!=0. It is not used here.
    The simulations and their power-law fits are also not used as evidence
    for this theorem. General mistakes recall produced low-separation leads,
    not an applicable theorem.

No identity or audit check failed. The attempted extension to a full Gaussian
fails at the explicit kink collision. Novelty within the existing special-case
one-dimensional literature has not been established.

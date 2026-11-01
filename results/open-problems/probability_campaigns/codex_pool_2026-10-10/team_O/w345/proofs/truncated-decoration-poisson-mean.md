# C0005: Exact truncated expectation and infinite full expectation for exponential decoration growth

Label: proof; author checked only. Independent audit: PENDING w347.

For Poisson heights of intensity z*exp(-alpha*h) dh, with z>=0 finite and alpha>0, and independent identically distributed nonnegative decoration marks K(s), the truncated sum S_t^H=sum_(-t<=h_i<=H) K_i(t+h_i), H>=-t, has expectation z*exp(alpha*t)*integral_0^(t+H) exp(-alpha*s)*E K(s) ds. If z>0 and exp(-alpha*s)*E K(s)->c>0, the full sum over h_i>=-t has infinite expectation for each fixed t. With E K(s)=exp(alpha*s), the truncated mean is exactly z*exp(alpha*t)*(t+H).

Assumptions: A marked Poisson process with the displayed intensity; Nonnegative measurable marks independent of the height process; alpha>0 and H>=-t

For a nonnegative marked-Poisson integral, Tonelli and the Poisson first-moment identity give E S_t^H=z*integral_(-t)^H exp(-alpha*h)*E K(t+h) dh, allowing either side to be infinite. Put s=t+h to obtain the displayed identity with exp(-alpha*s), not exp(+alpha*s). Sending H to infinity and applying monotone convergence gives the full expectation z*exp(alpha*t)*integral_0^infinity exp(-alpha*s)*E K(s) ds. A strictly positive limiting integrand makes this integral diverge. The special exponential mark makes the integrand identically one, proving the exact truncated formula.

Limits: Infinite expectation does not imply an infinite realized sum: only finitely many heights exceed -t almost surely, and finite decorations can yield a finite realized total. No DGFF decoration moment asymptotic is proved here.

Existing card: math:probability.gaussian:open-problem-c0005-size-of-deep-extremal-level-sets-of-the-2d-dgff-converges-to-the-extre
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:8541

P0289 second-order sign criterion

Auditor: w346; KEEP S1.w342.001. This certifies the coefficient criterion only, not full-workload ordering.

Let R:[0,infinity)->R be continuous and Psi(c)=integral_0^1 (1-u)R(cu)du for c>0. Then Psi'(c)=c^(-3) integral_0^c (2v-c)R(v)dv. Consequently Psi is nonincreasing exactly when that integral is nonpositive for every c>0. This criterion orders only the second-order coefficient of a light-traffic workload expansion; it is not a criterion for ordering full Cox workloads.

Proof: Write A(c)=integral_0^c (c-v)R(v)dv. Substitution v=cu gives Psi(c)=A(c)/c^2. Continuity gives A'(c)=integral_0^c R(v)dv. Differentiation yields Psi'(c)=(cA'(c)-2A(c))/c^3, the displayed integral. A continuously differentiable function on (0,infinity) is nonincreasing iff its derivative is everywhere nonpositive.

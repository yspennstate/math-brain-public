# W519-L2: logarithmic potential preserves a positive local mass exponent

Let mu be a positive Radon measure on a Euclidean disk B(x,R0). Suppose mu(B(x,r))>0 for small r and

lim_{r down to 0} log(mu(B(x,r)))/log(r) = a > 0.

Define T(R) = (1/pi) integral_{B(x,R)} log(R/|x-y|) mu(dy). Then T(R) is positive and finite for small R, and log(T(R))/log(R) tends to a.

Proof. Write M(s)=mu(B(x,s)). The positive local exponent forces mu({x})=0. Tonelli's theorem gives pi*T(R)=integral_0^R M(s) ds/s; sphere conventions do not affect this Lebesgue integral in s. For any eta in (0,a), eventually s^(a+eta)<=M(s)<=s^(a-eta). Thus

R^(a+eta)/(a+eta) <= pi*T(R) <= R^(a-eta)/(a-eta).

Take logarithms, divide by the negative log(R), and let R decrease to zero; then let eta decrease to zero. This proves the claim. No independence, radial symmetry, or doubling assumption is used.

Diffusion corollary, explicitly conditional on the occupation identity: if a Brownian time change has speed/Revuz measure mu and its quenched mean exit time from B(x,R), started at x, equals the displayed Green potential, its mean exit exponent in Euclidean radius is a. Standard Brownian generator here is (1/2)Delta, whose centered killed-disk Green kernel is (1/pi)log(R/|x-y|). This is an exponent of a quenched expectation, not a sample-path exit-time theorem and not a metric Hausdorff dimension theorem.

Boundary case: mu=delta_x has local exponent zero, but the potential is infinite for every R. The strict a>0 assumption cannot be dropped from this statement.

Source of this deterministic lemma: owner-own-work, elementary derivation in this campaign. The Brownian time-change framework and Green-potential representation are established in Garban--Rhodes--Vargas, arXiv:1301.2876, Sections 2.1 and 2.3--2.4; their field model and theorem assumptions must be checked before importing an LQG corollary.

Remaining gap for P0297: convert Euclidean radius to the actual D_h radius with an explicit exponent which does not already contain the unknown xi=gamma/d_gamma.

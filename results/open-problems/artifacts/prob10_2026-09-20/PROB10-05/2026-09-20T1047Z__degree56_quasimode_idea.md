Runtime request: GPT-6 / maximum. The execution environment identifies GPT-5.6 Sol; reasoning level is UNVERIFIED, so this checkpoint does not claim GPT-6 maximum.

# PROB10-05 idea checkpoint — finite-polynomial Perron quasimode before code

Frozen source model: H=1/4, centered standard fBM B_{1/4}, I(t)=int_0^t B_{1/4}(s)ds, and the continuous one-sided fixed-barrier event. The published/source bracket remains 1/8 <= theta_{2,1/4} <= 1/4. The current strongest repository self-certified candidate found on master is the neighboring NM13-09 degree-40 min-max certificate theta_{2,1/4}>53683/312500=0.1717856; no ownership transfer is made.

This run will not repeat the degree-40 min-max route as its main mechanism. It compares three distinct nonexhausted attacks:

1. **Finite-polynomial Perron quasimode (main route).** Keep the already source-valid Lamperti/Slepian comparator (r=7/8, s=24861/25000, c=74583/80000), but replace the inherited degree-48 Perron trial vector by a degree-56 Rayleigh-Ritz vector. The key new point is to exploit that the trial function is an actual finite polynomial: compute <f,Kf> and <Kf,Kf> from finite Gaussian truncated-moment identities, with outward rational interval arithmetic. This directly addresses the previous generic Hermite-tail obstruction and should reduce the Temple residual without requiring a new trace estimate. High-precision diagonalization may select the polynomial, but no floating-point sign will be theorem evidence.

2. **Signed two-mode continuous covariance comparator.** Test whether a stationary Gaussian Markov/state-space covariance with a signed two-exponential representation can lie below the exact Lamperti covariance while remaining positive definite. Positive OU mixtures have an inherited tail obstruction; allowing a signed coefficient changes the category and may evade it. The first mathematical task is to impose spectral-density nonnegativity and compare both the t->0 and t->infinity expansions. Any impossibility proved here is auxiliary mechanism progress, not an exponent bound.

3. **Reverse interpolation / missed-crossing rate.** Investigate the missing sampled-to-continuous direction needed for an upper bound. At fixed mesh, a per-interval missed-crossing probability bounded only by an unconditional q(Delta)>0 cannot yield an exponentially relative correction: a union bound is O(n q(Delta)), while persistence is exponentially small in n. A usable proof must instead control the crossing conditional on long grid survival, or send Delta to zero with a quantitatively uniform discrete spectral-radius approximation. I will try to make this obstruction precise from the local covariance regularity rather than pretending that discrete persistence is continuous persistence.

Main measurable quantity: the self-certified repository bracket width U-L with U=1/4. Before this run, the strongest current master candidate is L=53683/312500=0.1717856, hence width 0.0782144. The primary-literature bracket is kept separately and is not changed merely by a self-check.

No code has been written for the new degree-56 claim at the time of this checkpoint.
# Handoff notes for the parent session

Verified mathematics, not yet written to shared brain because the worker rules prohibit external writes:

- In an exchangeable spectral law on n coordinates, B-D <= kappa_n I, where D is within-level entropy and kappa_n=min_{a>0}[a+1/(n(exp(a)-1))]/ln 2=O(n^-1/2). This statement does not require the law to come from a Boolean function. The proof is the log tangent bound followed by a geometric series for C(j,k)/C(n,k).
- For a symmetric Boolean function the derivative's alternating nonzero values imply mean derivative Fourier degree >=(n-1)/2. Jensen on the concave decreasing function r(x)=-(1-x)ln(1-x)/x then improves the earlier analytic within-level bound to D<3I. Combine with the prior Bessel envelope to obtain B<=3.462071I using an integer-only finite census through dimension 24.
- L1 contraction of further derivatives gives Gamma<=H/2+Var log_2(I/n), with equality for thresholds. A geometric bound on level entropy makes this Gamma<=D/2+O(n^-2/3)I. Together with the finite census and derivative envelope, Gamma<=(8/5)I. The last improvement also uses E_q(1/X)=1/rho and Jensen, with a short split for dimensions 25 through 39.
- These bounds do not improve the supplied FEI constant through Theorem 1. Three-variable AND already has B/I=15/4-(3/2)log_2 3 >1.3252155. Large-dimensional witnesses are much higher.

Implementation scars: parity-times-threshold convolutions require the constant tail for outside weight t>r, not only nonnegative coefficient indices. A direct finite-difference comparison caught this; only v2 parity outputs are valid. For rare thresholds at n=2000, influence itself underflows binary64, but W/I ratios can still be computed accurately by dividing exact integer numerators. Report log2 influence in that case. /usr/bin/time -l may return nonzero in this sandbox because sysctl kern.clockrate is denied even when the timed numerical command succeeded; do not chain essential work to that diagnostic's exit status.

The final cancellation constant is 8/5. The intermediate 1.638 bound improves by adding E_q(1/X)=1/rho (q is the derivative spectral law and rho=I/(n Var)); Jensen gives E_q ln(1/X)<=ln(1/rho). A split at rho=4/15 in dimensions 25..39 and the analytic envelope above dimension 39 closes Gamma<=(8/5)I. sharpen_gamma_constants.py checks its constants with exact fractions and positive-series remainders.

Stable rare-spectrum logs need exact integer differences, not merely more displayed decimal places. symmetric.py uses log1p((Q 2^(n-k)-F^2)/F^2) for B, log1p((L-|F|)/|F|) for Gamma, and log1p of the exact complement for near-one dyadic probabilities. It agrees at 80 and 720 digits even on AND_2000 and parity times AND_2000. Parity-family v3 keeps log2 ratios when linear values fall below binary64 range.

The exhaustive finite suprema are now fully certified: census_interval.c uses outward integer log bounds to retain every possible maximizer; exact rational log-expression maps prove all 299 remaining candidate ties. certify_suprema.py evaluates the 188 defined suprema by positive-series intervals at scale 2^440, certifying 100 decimal places. Product-checked integer decompositions suffice for the equality certificate; primality of their labels is not needed.

The final B bound is 3.459354I, from the unsimplified decreasing envelope E(n), maximized at n=25. Its derivative bound is explicit; B_final_constant_certificate.json verifies the endpoint with exact fractions. Earlier 3.462071 and 3.463 are valid but weaker intermediate bounds.

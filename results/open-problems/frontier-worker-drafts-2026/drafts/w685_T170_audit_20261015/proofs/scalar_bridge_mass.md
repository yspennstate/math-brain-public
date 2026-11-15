# Exact scalar mass of irreducible height bridges (C014-v2; unaudited)

This lemma concerns a one-dimensional weighted sign-walk count. It does not by itself prove an FPP lower bound. The remaining hard step for C013 is a contracting, correctly interpreted all-length operator, including its initial and terminal factors.

Let a,z>0, d a positive integer, b=d/a, and weight a sign word of length n and final height ell by b^n z^ell. A strict positive bridge starts at 0, ends at ell>=1, and has every intermediate height strictly between 0 and ell. It is irreducible when every interior height 1,...,ell-1 is visited at least twice. The one-step word + is irreducible.

Let N(n,ell) count strict bridges. N(1,1)=1, and N(n,1)=0 otherwise. For ell>=2 and n>=ell with matching parity, the reflection principle for the walk killed at 0 and ell gives

N(n,ell) = sum over integers k of [binom(n-2,(n+ell-4)/2+k ell) - binom(n-2,(n+ell-2)/2+k ell)].

The binomial coefficient is zero outside its integer range. This follows by fixing the first and last positive steps, then reflecting walks from 1 to ell-1 that cross either absorbing endpoint; successive reflections give the two translated image families. The implemented sum includes all nonzero images. An independent killed-walk dynamic program checks this formula for every n<=30 and ell<=n.

Define A_n = sum_ell N(n,ell)b^n z^ell, and let B_n be the same count restricted to irreducible bridges. Every strict bridge has a unique decomposition at the interior heights visited exactly once. These heights occur in increasing order: returning below one after its unique visit would visit it again. Between consecutive such heights the word is a strict bridge with no uniquely visited interior height. Conversely concatenating irreducible strict bridges gives exactly these cuts. We therefore have the formal length-series identity A=B+BA, equivalently

B_n = A_n - sum_{j=1}^{n-1} B_j A_{n-j}.

No infinite-series convergence or analytic continuation is used to compute a finite coefficient. If a=A/D and z=Z/Q in lowest terms, every length-n weight has denominator (A Q)^n. The implementation computes all numerators with integer arithmetic. Positivity of every resulting B_n is checked. Exhaustive strict irreducible profiles through length 15 independently reproduce these coefficients.

For an irreducible length-n bridge, n-1>=2(ell-1), so its negative-step count m=(n-ell)/2 is at least (n-1)/4. For any t>=1, its quota factor t^(4m-n+1) is at least one. Summing over all sign words gives

B_n <= t [d(z+t^4/z)/(a t)]^n.

At the exact rational d=21 point in logs/height_bridge_tail_certificate.json, t=7/5 and the bracket is strictly below 9/10. Hence the omitted sum n>400 is at most (7/5)(9/10)^401/(1/10). Compute each B_n through n=400, round it downward to a multiple of 10^-40, and sum. The lower endpoint is this sum; the upper endpoint adds 400*10^-40 and the displayed geometric tail. Every rounding operation is integer floor division.

The exact endpoints, point, checks, and resource timing are saved in logs/scalar_bridge_mass_certificate.json. Both endpoints round to 1.0121310147533509 at ordinary double precision; that rounded display is not the certificate. The interval width is below 10^-15. Reproduce with python -X utf8 scripts/certify_scalar_bridge_mass.py.

The point was originally selected using a superseded five-slab axis comparison. It is now a fixed method probe. No present axis threshold, new dimension, or independently reviewed theorem is asserted by this scalar lemma.

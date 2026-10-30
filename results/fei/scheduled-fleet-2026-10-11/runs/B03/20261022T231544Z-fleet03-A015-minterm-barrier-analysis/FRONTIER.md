# Why a bounded coordinate cover does not remove the minterm barrier

The new two-root certificate pays a uniform O(n) code length. The rare-tail
influence inequality is an essential second hypothesis. It cannot be inferred
from the existence of two covering original primes.

Take m=2k even, t=k, r=0 in the SAME threshold-product family, now outside
the rare-tail theorem. Two original primes whose omitted k-sets are disjoint
still cover all 2m coordinates. Write

    a_k=binom(2k,k)/4^k, q=(1+a_k)/2, b=q^2.

Direct pivotal counting gives I=2m q a_k and Var=4b(1-b). Thus the uniform
dimension budget has ratio

    (2m) Var/I=4q(1-q^2)/a_k.

Here a_1=1/2 and a_(k+1)/a_k=(2k+1)/(2k+2), so q is between 1/2 and3/4.
Moreover a_k<=1/sqrt(k+1), proved by induction: the squared step inequality
[(2k+1)/(2k+2)]^2 <= (k+1)/(k+2) reduces to 3k+2>=0.
It follows that

    (2m) Var/I >= (7/8) sqrt(k+1) -> infinity.

This is a lower bound for the crude uniform dimension budget ONLY. It does
not lower-bound the actual queue cost, optimized ranks, or H/I. In particular
it is not an FEI counterexample. It rigorously locates the missing compression:
a central-band proof must pay the actual expected subset/rank length rather
than multiply the whole ambient dimension by all nonempty spectral mass.
Two covering primes and leafless incidence alone do not imply the needed
dimension/variance payment.

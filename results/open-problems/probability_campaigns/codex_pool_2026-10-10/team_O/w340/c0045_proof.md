# C0045: homogeneous drift gives exponential box exit bounds

Label: proof of a homogeneous-environment special case, awaiting w346. It does not address genuinely random iid environments or justify the earlier regeneration-moment equivalence.

Let X be a nearest-neighbour random walk on Z^d with iid increments, with E[X_(n+1)-X_n] dot e1=mu>0. All coordinates of an increment are bounded by one. Start at zero, use an integer L, and stop on hitting longitudinal coordinate +L, longitudinal coordinate -L, or any transverse coordinate with absolute value at least L^3. Then for all sufficiently large L the probability of exiting anywhere but +L is at most

exp(-theta L)+exp(-mu^2 (L^3-1)/8),

for some theta>0 depending on the increment law. It is therefore at most L^(-M) for every fixed M>0 and all sufficiently large L.

Proof: With Y the first-coordinate increment, m(theta)=E[exp(-theta Y)] has m(0)=1 and m'(0)=-mu<0. Choose theta>0 with m(theta)<1. The process exp(-theta X_n dot e1) is a nonnegative supermartingale. Stopping it at the first hit of -L, truncated at an arbitrary n, bounds the probability of that hit by exp(-theta L); let n increase. This also bounds backward exit before forward exit.

A transverse exit needs at least L^3 steps from zero. Thus a transverse exit before +L entails that the longitudinal coordinate has not hit +L by n=L^3-1. In particular X_n dot e1<L. For L large enough that mu n>=2L, Hoeffding's inequality for iid [-1,1] increments gives P(X_n dot e1<L)<=exp(-mu^2 n/8). Union bound proves the claim.

This is a concrete polynomial-exit condition for the stated boxes. Checking the exact source definition of (P)_M still matters, including its starting region and tilted boxes. The iid-increment argument is not valid for the annealed increments in a general iid random environment: a revisited site reuses its transition probabilities, and the exponential process need not be a supermartingale with one fixed theta. Positive limiting velocity alone does not provide that conditional drift inequality. This identifies a precise missing step rather than asserting a regeneration-moment equivalence.

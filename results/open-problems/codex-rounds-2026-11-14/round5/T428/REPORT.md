VERDICT: PARTIAL Uniform time-resolved Brownian signed pair limit for N-dependent profiles with unchanged critical tuning

The round 4 fixed-profile theorem holds on independent re-derivation.
The new result makes it uniform over all real measurable profiles with

    |f(x)|<=C exp(-a|x|),       integral f>=m_0>0,

for fixed C,a,m_0. It therefore covers arbitrary N-dependent profiles
f_N in this class, without convergence of the profiles, their sign
multipliers or their leading projections. The Brownian gap generator
is still Delta.

For L=log N, u_N=sqrt(|f_N|), v_N=sgn(f_N)u_N and
P_N=u_N tensor v_N/integral f_N, retain each profile's original
sharp-time eigenvalue Lambda_N(f_N) and exactly the original tuning

    alpha_N L Lambda_N(f_N)=1+(theta+epsilon_N)/L,
    epsilon_N -> 0.

For Q_N(t)=M_{u_N} exp(t Delta)M_{v_N} and the signed convolution
series R_N=sum_{k>=1}alpha_N^k Q_N^{*k}, the conclusion is

    sup_{delta<=t<=T}
      ||N R_N(Nt)/L-g_theta(t)P_N|| -> 0,

for every 0<delta<T<infinity, where

    g_theta(t)=integral_0^infinity
                  exp((theta-gamma)s)t^(s-1)/Gamma(s) ds.

The statement is uniform over the entire profile class, with tuning
errors bounded by any given e_N tending to zero. There is also uniform
operator-norm convergence against continuous time tests with a finite
limit at infinity, damped by exp(-bt) for b>exp(theta-gamma).
The full proof is in [PROOF.md](PROOF.md).

The new work is the uniformity argument. Explicit common moment bounds,
projection bounds and contour estimates make all spectral and transform
errors uniform. The time reconstruction compares against moving positive
rank-one operators A_N=P_N J_N. Their norms are bounded by
2 pi C/(a^2 m_0), so one polynomial approximation and one finite time
partition suffice for all profiles. A limit of A_N or J_N is not assumed.

The previous theorem was checked independently through a Schur complement
for the tuned inverse and scalar quadratic forms for the time squeeze.
The scalar denominator is still
(log z+gamma-theta-epsilon_N)/L+O(L^-2), uniformly. The signed correction
from the sharp-time eigenvalue cancels. No retuning by absolute mass is
made, and novelty of the Brownian pair theorem is not claimed.

Reproduce the scalar checks with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 -B verify.py
```

Exit 0; 45-digit precision; 0.781 seconds; peak RSS 26,968,064 bytes;
all four thread settings one. The wrapper's extra priority adjustment
was refused, while libc verified inherited nice 20 before computation.
The script uses a 90-second CPU cap and scalar quadrature only.
Output is in [verification.json](verification.json), and the command,
re-derivations and audit are in [LOG.md](LOG.md).

The checks independently recover the previous log(81/32) correction,
test four signed Gaussian profiles and twelve finite-N overlaps, verify
the uniform scalar overlap bound 70/N, and compare the two time-density
representations. All exact-equality checks pass at tolerance 1e-32.
These are scalar normalization checks, not a numerical proof of the
uniform operator theorem.

The lower mass bound cannot simply be dropped from this proof:
f_delta=(1+delta)phi_1-phi_2 has a common exponential envelope but

    ||P_{f_delta}||=1+1/[2 delta(1+delta)] -> infinity.

This formula was checked by direct radial integration and exact Gaussian
tail masses. It is a limitation of the result, not a counterexample to
the original conjecture. No defect or failed numerical assertion was found.
No vertical-line inversion or spatial endpoint calculation was attempted.

A web-tool literature check under five minutes found no later resolution
of the particular conjecture. The opened current record of Hindy Drillick,
Jonathan Hou and Shalin Parekh, *A universality result for the critical 2d
stochastic heat flow*, [arXiv:2609.15832](https://arxiv.org/abs/2609.15832),
still lists only v1; its [HTML](https://arxiv.org/html/2609.15832v1)
retains Conjecture 1.17. The opened abstract of Quentin Berger, Francesco
Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu, Shuta
Nakajima, Rongfeng Sun, Li-Cheng Tsai, Zuodi Xie and Nikos Zygouras,
*The Critical 2D KPZ Process*,
[arXiv:2610.31614](https://arxiv.org/abs/2610.31614), concerns a renormalised
Cole–Hopf construction rather than an announced signed-kernel universality
extension. This bounded search does not establish absence of other work.

What remains unproved: Conjecture 1.17 in its discrete and continuum
forms; general N-dependent gap processes; diffusive spatial endpoints;
third and fourth moment convergence; any positive-time rate; and
estimates uniform down to zero time. No KPZ field is constructed and
no undefined logarithm of the singular flow is used.

The next worker should prove small-time integrability in operator norm
for this same Brownian class, retaining the signed tuning. A precise
target is

    lim_{delta down to 0} limsup_{N to infinity}
      sup_{f in F, |epsilon|<=e_N}
        integral_0^delta ||F_{N,f,epsilon}(t)||dt = 0.

The present proof controls the norm of a positive operator-valued total
mass, which is insufficient to assert this target. A new estimate on
the semigroup sandwich is needed; comparison with |f| loses the critical
cancellation. Such a bound would allow time-integrated compositions to
be treated near zero, beyond the present compact positive time intervals.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, 09:22 +04 (Asia/Tbilisi; first recorded local clock).

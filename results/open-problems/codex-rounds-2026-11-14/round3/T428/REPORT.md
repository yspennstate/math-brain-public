VERDICT: PARTIAL Brownian signed pair-renewal Laplace limit with unchanged critical tuning

The earlier Brownian spectral lemma holds. Its operator expansion was
re-derived, and the signed Gaussian example's correction
4 pi I(f)=log(81/32) was independently recomputed by finite-interval
Gaussian-log quadrature. No defect was found in the earlier result.

The new result is a Laplace-transform limit for an actual signed pair
renewal density, for the same fixed real Brownian profile satisfying
|f(x)|<=C exp(-a|x|) and m=integral f>0. With L=log N, use the earlier
sharp-time eigenvalue Lambda_N and tune

    alpha_N L Lambda_N = 1+(theta+epsilon_N)/L,   epsilon_N -> 0.

Here alpha_N is the earlier beta_N^2. Set

    u=sqrt(|f|),   v=sgn(f)u,   P=u tensor v/m,
    Q(t)=M_u exp(t Delta) M_v,
    R_N(t)=sum_{k>=1} alpha_N^k Q^{*k}(t).

For Re z>exp(theta-gamma), the theorem proves

    integral_0^infinity exp(-zt) [N/L R_N(Nt)] dt
        -> P/(log z+gamma-theta)

in operator norm, locally uniformly in z, with error
O_K(1/L+|epsilon_N|). The algebraic resolvent limit also holds on compact
subsets of Re z>0 away from exp(theta-gamma).

The two new ingredients in [PROOF.md](PROOF.md) are:

- A direct heat-kernel comparison between exponential time damping and
  the sharp cutoff. Its finite part is -gamma-log z and its weighted
  operator remainder is O(N^-1/2). The signed leading projection is
  retained throughout.
- Identification of the finite-time renewal series with
  alpha_N M_u exp(t(Delta+alpha_N f)) M_v. A self-adjoint quadratic-form
  argument justifies its critical-scale Laplace integral. Finite-time
  absolute convergence alone would not justify that integral.

This extends the earlier spatially integrated spectral calculation to
a genuine renewal transform. It does not replace f by |f| or change
the sharp-time coefficient Lambda_N. Novelty is not claimed.

Reproduce the scalar checks with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py
```

Exit 0; 45-digit precision; 0.614 seconds; peak RSS 24,592,384 bytes;
one thread. The shell refused a further nice increment, but libc reported
inherited nice 20 with errno zero. Results are in
[verification.json](verification.json), and the command, numerical output
that matters, independent Schur-complement derivation and adversarial
audit are in [LOG.md](LOG.md). These are scalar checks, not a numerical
operator proof. All exact scalar identities tested agree to better than
1e-34. No numerical assertion failed.

A web-tool literature check of less than five minutes found no later
resolution. The current record of Hindy Drillick, Jonathan Hou and Shalin
Parekh, *A universality result for the critical 2d stochastic heat flow*,
[arXiv:2609.15832](https://arxiv.org/abs/2609.15832), still lists v1,
whose HTML states Conjecture 1.17. The check also opened Quentin Berger,
Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu,
Shuta Nakajima, Rongfeng Sun, Li-Cheng Tsai, Zuodi Xie and Nikos Zygouras,
*The Critical 2D KPZ Process*,
[arXiv:2610.31614](https://arxiv.org/abs/2610.31614). Its stated result
concerns a renormalized Cole–Hopf construction; it is not a stated
resolution of the signed-kernel conjecture and predates the earlier
report. This bounded search does not establish absence of other work.

What remains uncertain or unproved: Conjecture 1.17 in both its discrete
and continuum forms; inverse Laplace estimates on unbounded vertical
lines; pointwise time-resolved renewal estimates; diffusive spatial
endpoints; arbitrary N-dependent profiles and gap processes; and third
and fourth moments. The result requires positive total mass. It does not
construct a KPZ field or take an undefined logarithm of the singular flow.

The next worker should try to prove a uniform vertical-line resolvent
bound strong enough for time inversion, or first derive a precise weak
time-integrated pair limit from this transform theorem. The semigroup
representation may help control signed matrix elements. Compact-set
Laplace convergence alone must not be presented as pointwise time
convergence.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 03:53 +04 (Asia/Tbilisi;
first recorded local clock reading).

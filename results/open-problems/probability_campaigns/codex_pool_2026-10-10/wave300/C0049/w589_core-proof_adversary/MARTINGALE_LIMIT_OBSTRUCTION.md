# A pathwise martingale limit can lose its martingale property

Independent C0049 adversary derivation, saved 2026-10-10. This elementary counterexample identifies an integrability premise; it is not a counterexample to FK convergence.

Let N be a unit-rate Poisson process. For integer n>=1 and 0<=t<=1, put

    M^n_t = 1 - t + n N_{t/n},
    F^n_t = sigma(N_{s/n}: 0<=s<=t), completed in the usual way.

Each M^n is a nonnegative cadlag true martingale in its natural filtration, since N_{t/n}-t/n is a compensated Poisson martingale and 1-t>=0. Let S be the first jump time of N. Almost surely S>0. For every n>1/S there are no jumps on [0,1/n], so M^n_t=1-t for all 0<=t<=1. Consequently M^n converges uniformly almost surely to the continuous deterministic process M_t=1-t. The latter is not a martingale in any filtration, because its expectations change with time.

The failure is uniform integrability. For fixed t>0, E[M^n_t]=1 but E[M_t]=1-t. For any K>1 and n>K, on {N_{t/n}>=1} we have M^n_t>=n, so

    E[M^n_t 1_{M^n_t>K}] >= n(1-exp(-t/n)) -> t > 0.

Thus even uniform pathwise convergence to a continuous process does not justify passing discrete conditional martingale identities to the limit. One needs uniform integrability after specified localization, plus joint convergence of the histories used for conditional testing. A delta-dependent bound such as |(2delta)^(-sigma) f_delta|<=(2delta)^(-sigma) supplies no uniform bound by itself.

NEXT: Check whether the paired proof derives a delta-uniform bound on stopped, renormalized slit-domain observables rather than relying on the unscaled bound |f_delta|<=1.

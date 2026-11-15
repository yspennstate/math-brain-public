# C35 candidate: persistent blocks and fresh downward copies

Status: sketch, not audited. Target: 2. No T4 conclusion.
Frontier check T2_PERSISTENT_FRONTIER_CHECK.txt returned exit 0.

Partition the tree into rooted blocks of height L. In each block copy retain
its awake mask permanently. Every downward exit creates a fresh child-block
copy, with a pointer back to this exact parent copy. Every upward return
re-enters the existing parent; no parent resident is born again. Each site
has one resident per copy, and every frog retains ordinary motion. This is
intended as an upper comparison by first-upper-birth coupling, as in C33,
but its coupling and recursive law still need a full proof.

Finite-height numerical boundary: all motion below the last block is
sterile until its possible return, with probability beta=1/d. This gives
finite-height approximations to the candidate, not an upper bound for the
ordinary infinite frog model. Recursive population error is unbounded.

The L=1 star has one root and d leaves. Let X be the upward return count of
a fresh child star with one seed; phi(z)=E[z^X], m=E[X]. A personal clan is
the seed together with all fresh child-block responses that it creates,
excluding the other residents in this star. Different clans use independent
randomness. Resident activation is their range-reachability closure.

For a permitted set consisting of the root and k specified leaves, a clan's
joint avoidance/upward-count generating functions a_k(z), b_k(z) should be
the minimal nonnegative solutions

    a_k = p*z + k*q*b_k,
    b_k = p*a_k + (1-p)*phi(b_k),
    q = (1-p)/d.

With two root clans (seed and resident), let t_k(z) be the joint upward-count
PGF and probability that exactly a specified set of k leaves is activated.
The independent unused-clan identity gives the candidate triangular formula

    t_0 = a_0^2,
    t_k = a_k^2*b_k^k
          - sum_(i<k) binom(k,i)*t_i*b_k^(k-i),
    Phi(z) = sum_(k=0..d) binom(d,k)*t_k(z).

At z=1, when m < mcrit=(1-p*(1-p))/(1-p), the sterile clan has finite mean.
Put D=1-p*(1-p)-(1-p)*m. Its upward means from root and leaf are

    u_root=p*(1-(1-p)*m)/D,   u_leaf=p^2/D.

If A=sum_(k>=1) binom(d-1,k-1)*t_k(1) is the activation probability of a
specified leaf, the candidate output mean is

    M = 2*u_root + d*A*u_leaf.

Only numerical screening is authorized by these notes. The scalar fixed
points, range-closure identity, minimal-solution interpretation, first-birth
upper coupling and exceptional global-root criterion all need checking
before a proof is queued. No inference from an infinite mean to recurrence.

First checks: d=2,4,5,6; z=1 normalization and z=0 extinction atom; L=0
reduction to a fresh-downward-copy branching process; a completely sterile
child response must agree with direct finite-star SRW simulations. The
hardest open piece is an infinite-height finite-mean supersolution at d=4.

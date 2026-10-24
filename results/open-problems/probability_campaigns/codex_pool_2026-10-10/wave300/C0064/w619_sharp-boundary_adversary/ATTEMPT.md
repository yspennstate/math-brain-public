# C0064: independent sharp-boundary obstruction

Author: w619. Date: 2026-10-10. This derivation was saved before reading w618's proof. Status: proof draft awaiting w620's independent mathematical check; novelty unverified. This is a counterexample to an auxiliary inference about kernels, not to nearest-neighbour Bernoulli percolation.

## Statement recovered from the primary theorem

Fitzner and van der Hofstad, arXiv:1506.07977v2, Theorem 1.1, prove for nearest-neighbour bond percolation on Z^d, d >= 11, the existence of finite dimension-dependent constants such that, uniformly for 0 <= p <= p_c(d),

    tauhat_p(k) <= A1(d)/(chi(p)^(-1) + p(1-Dhat(k))),
    tauhat_p(k) <= A2(d)/(1-Dhat(k)).

Here Dhat(k) = d^(-1) sum_i cos(k_i). At criticality the Fourier transform needs its limiting interpretation; the singular mode k=0 is not a finite-valued assertion. C0064's dated ranking asks for the remaining d=7,8,9,10. Current openness is UNKNOWN pending the local record and current-status checks. The primary theorem proves the implication from the uniform infrared bound to triangle finiteness; it does not state the converse for abstract kernels.

## Independent proposition: even an arbitrarily small triangle does not force an infrared bound

Fix any integer d >= 7 and eta > 0. There exists a family f_p: Z^d -> [0,1], 0 <= p <= 1, with all the following properties:

1. f_p(0)=1, f_0=delta_0, f_p is even and invariant under signed coordinate permutations, and each f_p is positive definite.
2. f_p(x) increases in p for every x, and f_p(x) tends to f_1(x) as p increases to 1.
3. For every p, its triangle sum is at most 1+eta.
4. For p<1, f_p is summable with susceptibility chi_f(p), and (1-p)chi_f(p) tends to a strictly positive finite constant.
5. No finite constant A bounds (1-Dhat(k)) fhat_1(k) near zero, and no finite A works uniformly over p<1 for (1-Dhat(k)) fhat_p(k). The susceptibility-regularized form with denominator chi_f(p)^(-1)+p(1-Dhat(k)) also has no uniform constant.

These are abstract kernels. No realization as connection probabilities of independent bond percolation is asserted. A route using only these listed properties is insufficient.

## Proof

All torus integrals below use dk/(2 pi)^d. Let L=(delta_0+D)/2 be the lazy nearest-neighbour walk and write q(k)=1-Lhat(k). Then Lhat is in [0,1] and

    |k|^2/(d pi^2) <= q(k) <= |k|^2/(4d),    k in [-pi,pi]^d.

The inequalities follow from 2t^2/pi^2 <= 1-cos(t) <= t^2/2 on [-pi,pi]. In particular q has its only zero at k=0.

Set s=9/8. For 0<=r<1 define

    G_r(k)=(1-r Lhat(k))^(-s),
    g_r(x)=integral exp(-i k.x) G_r(k) dk/(2 pi)^d,
    Z_r=g_r(0).

The binomial expansion gives

    g_r(x)=sum_{n>=0} (s)_n/n! r^n L^{*n}(x).

For r<1 this series converges in l1 because its total mass is (1-r)^(-s). Thus g_r is nonnegative, has the lattice symmetries, and increases in r pointwise. For j=1,2,3 put

    J_j=integral q(k)^(-js) dk/(2 pi)^d.

These integrals are finite: the only possible singularity is at zero and 2js <= 6s = 27/4 < 7 <= d. Let G=q^(-s), g(x)=its Fourier coefficient, and Z=J_1. Dominated convergence by G gives g_r(x)->g(x), Z_r->Z. Consequently g is nonnegative and g_r<=g. Z>=1, because the n=0 coefficient already contributes 1.

Choose

    0<a<=min{1/(2Z), sqrt(eta/(3J_2+J_3))}.

Define u_r=g_r-Z_r delta_0 and u=g-Z delta_0. All these sequences are nonnegative and vanish at zero. Define

    f^{(r)}=delta_0+a u_r,
    f^{(1)}=delta_0+a u.

For r<1, their Fourier transforms are 1-a Z_r+a G_r; the critical transform is 1-a Z+a G. All are at least 1/2, hence the sequences are positive definite. Their zero coefficient is 1, so positive definiteness implies |f^{(r)}(x)|<=1, including r=1. Nonnegativity also follows directly from u_r>=0. The lattice symmetries and pointwise monotonicity are inherited from g_r off the diagonal; the diagonal stays equal to 1.

For r<1, Fourier convolution and monotone convergence give

    (g*g*g)(0)=lim_{r->1} (g_r*g_r*g_r)(0)
             =lim_{r->1} integral G_r(k)^3 dk/(2 pi)^d=J_3.

Every passage here is justified either by nonnegative coefficients in physical space or by 0<=G_r<=G and the finite majorant G^3. Likewise sum_x g(x)^2=J_2 by Plancherel. Since 0<=u<=g, (u*u*u)(0)<=J_3. Expanding the triangle for f=delta_0+a u, with u(0)=0, gives

    (f*f*f)(0)
      =1+3a^2 sum_x u(x)^2+a^3(u*u*u)(0)
      <=1+3a^2 J_2+a^3 J_3
      <=1+a^2(3J_2+J_3)<=1+eta.

Here a<=1/(2Z)<=1/2, so a^3<=a^2. The same bound holds for every r<1 because f^{(r)}<=f^{(1)} pointwise and the triangle sum is a sum of nonnegative products. For an even translation-invariant kernel its triangle sum is exactly (f*f*f)(0).

Now reparameterize by r(p)=1-(1-p)^(1/s), for 0<=p<1, and set f_p=f^{(r(p))}, f_1=f^{(1)}. This is increasing in p and starts at delta_0. Its susceptibility is

    chi_f(p)=1-a Z_{r(p)}+a(1-r(p))^(-s)
            =1-a Z_{r(p)}+a/(1-p).

Since Z_{r(p)}<=Z<infinity, (1-p)chi_f(p)->a. Thus even the mean-field susceptibility exponent 1 does not rescue the abstract implication.

At criticality,

    (1-Dhat(k)) fhat_1(k)
      =2q(k)(1-a Z)+2a q(k)^(1-s).

Since s>1 and q(k)->0 as k->0, this quantity is unbounded on every punctured neighbourhood of zero (indeed on sets of positive measure). No ambiguity about the value at k=0 changes the failure.

The uniform subcritical failure has an explicit witness. Let delta=1-r in (0,1), take all coordinates of k_delta equal to 2 arcsin(sqrt(delta)), and take p_delta=1-delta^s. Then q(k_delta)=delta and

    1-r Lhat(k_delta)=2delta-delta^2,
    fhat_{p_delta}(k_delta)>=a(2delta-delta^2)^(-s),
    (1-Dhat(k_delta))fhat_{p_delta}(k_delta)
      >= a 2^(1-s) delta^(1-s) -> infinity.

Multiplying the last expression by p_delta->1 proves the failure of the susceptibility-regularized uniform bound too, because its other denominator term is nonnegative.

This finishes the independent derivation. The hardest missing ingredient for C0064 is still an actual percolation-specific estimate controlling the Fourier denominator uniformly as p approaches p_c in d=7..10. Triangle finiteness or smallness for comparison kernels is not that estimate.

## Review sequence

Independent derivation saved first. Next: freeze its hash, ask w620 to check the positive-definiteness and critical-limit steps, then inspect w618's actual proof and determine whether it uses the refuted auxiliary inference or a stronger percolation-specific premise.

# Early calculation — r44 E2 packet cannot disappear quietly into its rank-two carrier

Incoming completed partner: fleet03/B07 r44, `20260924T023904Z-fleet03-B07-qform-r44/REPORT.md`.
It supplies literal original-coordinate banks `I,J`, the crossing `K=A[I,J]`,

`Z=E2(K):=e2(K K^T) >= zeta:=2^-12`,

and, for a slab-ratio witness `rho`, after taking `theta=(2 C3/rho)^6`, its top-two SVD carrier
`K0=P2 K Q2` with

`eps^2:=||K-K0||_F^2 < 3 theta/zeta`,

where `C3=3*2^(4/3)*e^(1/3)`.

## Exterior-square stability

For any real rectangular matrices `B,E`, regard `wedge^2 B` as the restriction of `B tensor B` to the second exterior power. Since orthogonal projection/restriction is contractive in Hilbert-Schmidt norm,

`||wedge^2(B+E)-wedge^2 B||_HS`
` <= ||B tensor E + E tensor B + E tensor E||_HS`
` <= 2 ||B||_F ||E||_F + ||E||_F^2`.                         (1)

Also `||wedge^2 M||_HS^2=e2(M M^T)` by Cauchy-Binet.  Since `rank K0<=2`,
`||K0||_F<=sqrt(2)||K0||_op`.  Hence

`|sqrt(E2(K))-sqrt(E2(K0))|`
` <= 2 sqrt(2) ||K0||_op eps + eps^2`.                           (2)

Assume `eps^2 <= sqrt(zeta)/4`.  If `E2(K0)<zeta/4`, then (2) and `E2(K)>=zeta` force

`2 sqrt(2)||K0||_op eps + eps^2 > sqrt(zeta)/2`,

so

`||K0||_op > sqrt(zeta)/(8 sqrt(2) eps)`.                         (3)

Thus every such state obeys the exact alternative

`E2(K0)>=zeta/4`

or

`||K0||_op > sqrt(zeta)/(8 sqrt(2) eps)`.                         (4)

For the r44 high-ratio scale,

`eps <= sqrt(3/zeta) (2 C3)^3 rho^-3`.

The condition `eps^2<=sqrt(zeta)/4` already holds for `rho>=255.413`, hence throughout r44's inherited high-ratio regime.  Substitution into (4) gives

`boxed:  s1(K0)s2(K0) >= 1/128`

or

`boxed:  s1(K0) > rho^3/(113246208 sqrt(6) e)`
`             = 1.3261914514e-9 rho^3`.                         (5)

This is the first unpaid implication for the run.  It does not discard the tail `K-K0`: failure of two-volume retention is routed to a quantitatively ultra-large rank-two carrier singular value.

## Mandatory pinned-e5 payment on the same literal K

The completed `D_k` extension at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, with `k=2,q=2`, gives

`|phi_Q(t)| <= min(1,(2 e pi^2)^(1/4) Z^(-1/8)|t|^-1/2)`.

Combining it with its completed fractional-potential Lemma 4.1 yields

`H_{1/4}(Q):=sup_s E|Q-s|^-1/4`
` <= 3.92913177045 Z^-1/16`
` <= 6.60798564167`.                                             (6)

The decoupling theorem is applied to the actual original-coordinate crossing `K`, so arbitrary same-bank curvature, affine terms, outside couplings and all additional spectrum remain.  (6) is fractional-potential currency, not a density bound.

Full QFORM remains open.

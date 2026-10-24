# Sharp rank-two optimization and rank-three obstructions for K(5,5) minus C(10)

Date: 18 September 2026. Status: **restricted computer-assisted theorems and exact obstructions; the unrestricted target is not proved**. These are same-assistant derivations and self-checks, not two independent audits. Publication novelty is unverified.

## 1. Source boundary and target

Let H have left vertices x_0,...,x_4 and right vertices y_0,...,y_4, with y_i adjacent to x_i,x_(i+1),x_(i+2), indices modulo five. This is K(5,5) minus a ten-cycle. For a bounded symmetric nonnegative kernel W on a probability space, let

    t_H(W) = integral product_{xy in E(H)} W(z_x,z_y).

The target is t_H(W) >= (integral W)^15 for arbitrary such kernels. This note works first with 1-regular kernels, integral W(x,y)dy=1 a.e., and then restricts the operator rank to at most two. It does not prove a reduction of arbitrary rank to rank two.

**Already in the repository:** C30's report `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T17-58-00Z__report.md`, blob `b94c3d3e41eedcb647d9a69edaf7a404f3002648`, proves Sidorenko for every rank-at-most-two regular kernel, gives the polynomial below, proves the sharp third-moment envelope, and obtains t_H(W)>=1+5 lambda^4. Reconstructing those facts is not new progress.

**Additional results here:** the exact minimum at each prescribed nonconstant eigenvalue; a sharp sixth-order remainder; and explicit rank-three counterexamples to monotonicity under spectral addition and to additivity of rank-two slacks. The last two explain why the rank-two argument does not simply combine into a full proof.

The original graph's difficulty and its failure to be weakly norming are discussed by Lee and Schuelke, *Convex graphon parameters and graph norms*, arXiv:1910.08454. These facts do not supply the inequality being sought.

## 2. Rank-two normalization and exact polynomial

A nonconstant bounded symmetric 1-regular rank-two kernel has the form

    W(x,y)=1+lambda u(x)u(y),   E u=0, E u^2=1.

The Markov-operator contraction, by Jensen followed by integration, implies |lambda|<=1. For nonzero lambda the eigenfunction is bounded: apply the bounded integral kernel to u and divide by lambda. Put z=(E u^3)^2.

Expand over edge subsets F of H. A degree-one vertex contributes E u=0. Every other vertex has degree 0,2,or3; its factor is respectively 1,1,or E u^3. The number of degree-three vertices is even. Enumeration of all 32768 edge subsets leaves precisely 625 nonzero terms, including the empty set. Thus

    P(lambda,z) = t_H(W)
      =1+5 lambda^4+15 lambda^6+30 lambda^8+13 lambda^10
       +z(5 lambda^7+10 lambda^8+60 lambda^9+70 lambda^10+95 lambda^11)
       +z^2(15 lambda^10+60 lambda^11+145 lambda^12)
       +z^3(10 lambda^12+75 lambda^13)
       +15 z^4 lambda^14+z^5 lambda^15.                         (2.1)

The exact subset counts and a second direct kernel calculation are in `check_sidorenko.py` and `sidorenko_checks.json`. The polynomial is also the one in the cited earlier C30 report.

For lambda=-r<0, positivity of W implies |u|<=M=r^(-1/2) a.e.: a positive-measure set on which u>M, or u<-M, would produce a negative kernel on its square. Hence 0<r<=1. Integrating

    (M-u)(u+1/M)^2 >=0,    (M+u)(u-1/M)^2 >=0

shows

    |E u^3| <= M-1/M,  or  0<=z<=(1-r)^2/r.                  (2.2)

The upper bound is attained by u=M with probability r/(1+r) and u=-1/M with probability 1/(1+r), or its sign reversal. Equality in the integrated nonnegative polynomial forces this two-point law. At r=1, |u|<=1 and E u^2=1 force the balanced Rademacher law.

## 3. Exact extremizer at every fixed eigenvalue

### Theorem 3.1

For every fixed 0<r<=1, the minimum of t_H over bounded symmetric nonnegative 1-regular kernels whose only nonconstant eigenvalue is -r is

    P(-r,(1-r)^2/r).                                        (3.1)

It is attained by the two-block kernel

             [ 0      1+r  ]
    W_r =    [ 1+r    1-r^2],

with block probabilities r/(1+r) and 1/(1+r). For 0<r<1 any minimizer has the corresponding two-point eigenfunction, up to sign and measure-preserving rearrangement.

For fixed 0<lambda<=1 the minimum instead is

    1+5 lambda^4+15 lambda^6+30 lambda^8+13 lambda^10,         (3.2)

attained whenever E u^3=0 and the kernel is admissible, in particular by a balanced two-point u.

### Proof

For 0<r<1 write z=v(1-r)^2/r, 0<=v<=1, and form the polynomial

    Q(r,v)=[P(-r,v(1-r)^2/r)-1]/r^4.

The powers with apparent negative exponents cancel. Define

    D(r,v)=-Q_v(r,v)/[r^2(1-r)^2].                           (3.3)

Again this is a polynomial, of bidegree (12,4). Its tensor-product Bernstein expansion on [0,1]^2 has 65 rational coefficients, all at least 125/33. Therefore D>0 on that square. It follows that Q_v<0 whenever 0<r<1. The minimum over the complete feasible moment interval (2.2) is at v=1. The two-point law above attains that endpoint; its kernel is exactly W_r. Its weighted row sums equal one, and every entry is nonnegative. Strict monotonicity and the equality case in (2.2) give the characterization.

For r=1 the feasible moment interval consists only of z=0, so the same formula follows directly. For positive lambda all z-dependent coefficients of (2.1) are nonnegative, and the coefficient of z is strictly positive. This gives (3.2). QED, with the finite rational certificate in Section 5.

This is an optimization theorem on an already solved restricted class, not a proof for arbitrary graphons.

## 4. A sharp sixth-order remainder

### Theorem 4.1

Every kernel in Section 2 satisfies

    t_H(W) >= 1+5 lambda^4+10 |lambda|^6.                    (4.1)

The coefficient 10 is the largest universal coefficient in (4.1) when the coefficient of lambda^4 is fixed at 5. A further valid, not asserted optimal, improvement is

    t_H(W) >= 1+5 lambda^4+10 |lambda|^6+10 |lambda|^7.       (4.2)

### Proof

For negative lambda, the polynomial

    R(r,v)=[Q(r,v)-5]/r^2

has bidegree (14,5). All 90 tensor Bernstein coefficients are at least 10. This proves (4.1). The Bernstein coefficients of R-10-10r, at the same degrees, are all nonnegative; this proves (4.2).

For positive lambda, use (3.2). The extra inequality needed for (4.2) is

    15 lambda^6+30 lambda^8-10 lambda^6-10 lambda^7
      =5 lambda^6(1-2 lambda+6 lambda^2)>0.

The lambda^10 term is nonnegative. The constant kernel is immediate.

For sharpness, the feasible two-block extremizer has the expansion

    t_H(W_r)=1+5 r^4+10 r^6+20 r^7-40 r^8+O(r^9),  r downarrow 0.

Consequently (t_H(W_r)-1-5r^4)/r^6 tends to 10, so no larger universal sixth-order coefficient can hold. This family remains bounded (entries at most two) although its smaller block shrinks. QED.

## 5. Reproducible rational certificate

For a polynomial p(r,v)=sum c_ab r^a v^b of bidegree at most (n,m), its degree-(n,m) Bernstein coefficient at (i,j) is exactly

    b_ij=sum_{a<=i,b<=j} c_ab binom(i,a)/binom(n,a)
                                  *binom(j,b)/binom(m,b).

The basis functions binom(n,i)r^i(1-r)^(n-i) times binom(m,j)v^j(1-v)^(m-j) are nonnegative and sum to one on the square. A lower bound on every coefficient is a global bound, not a sampled-grid assertion.

`check_sidorenko.py` uses Python integers and Fraction only. It reconstructs the polynomial from every Bernstein expansion and checks equality of power coefficients, as well as the following exact inequalities:

| Polynomial | Degrees | Number of coefficients | Verified lower bound |
|---|---|---:|---:|
| D in (3.3) | (12,4) | 65 | 125/33 |
| R in Section 4 | (14,5) | 90 | 10 |
| R-10-10r | (14,5) | 90 | 0 |

All coefficients of D and R are saved in the JSON. The program regenerates the third array and verifies it, rather than trusting a stored minimum. It also computes t_H(W_r) by all 2^10 vertex assignments at six rational r, independently of (2.1). All checks passed. This finite certificate supplies the finite algebraic step in the two theorems; it is not an independent audit of the analytic reduction.

## 6. Why independent spectral directions do not combine

### 6.1 Truncation can destroy the positivity hypothesis

On three equal blocks define

    F=[ [3/2,-3/2,0], [-3/2,3/2,0], [0,0,0] ],
    G=[ [1/2,1/2,-1], [1/2,1/2,-1], [-1,-1,2] ].

These are orthogonal normalized rank-one kernels under the uniform measure. Let J be the all-ones kernel. Then

    J-F+G=[ [0,3,0], [3,0,0], [0,0,3] ]

is nonnegative and 1-regular, but J-F has an entry -1/2. Thus a theorem requiring positivity of each rank-two truncation cannot be applied automatically to arbitrary positive kernels.

### 6.2 Even admissible additions need not increase the density

All three kernels

    A_1=J-(3/5)F,  A_2=J-(1/5)G,
    A=J-(3/5)F-(1/5)G
      =[ [0,9/5,6/5], [9/5,0,6/5], [6/5,6/5,3/5] ]

are nonnegative and 1-regular. Direct exact integration gives

    t_H(A)   =86497056981/30517578125,
    t_H(A_1) =28616512/9765625,
    t_H(A_2) =985357817649/976562500000.

In particular,

    t_H(A)-t_H(A_1) = -2929543019/30517578125 <0,             (6.1)
    t_H(A)-t_H(A_1)-t_H(A_2)+1
                       = -102540694257/976562500000 <0.     (6.2)

So neither monotonicity on adding a negative eigencomponent nor additive accumulation of rank-two slacks is available. The checker obtains these fractions through the five-variable triple-moment contraction, not by the rank-two polynomial.

These are counterexamples to proposed proof mechanisms, **not to Sidorenko**: all displayed H-densities exceed one. They occur within the earlier equal-three-block setting and are consistent with its proved stability result.

## 7. Remaining full-problem obligation

For a finite-rank regular kernel, the expansion involves the mixed third-moment tensor E[u_i u_j u_k], not just the scalar skewness E u^3. A successful extension must control its interactions while respecting positivity of the whole kernel. The exact examples (6.1)-(6.2) are mandatory tests for such a proposal. Neither increasing the small-host enumeration nor summing the new sharp rank-two bounds eliminates this obstruction.

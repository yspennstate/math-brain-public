# The normalized collision lower-bound proposal already implies full FEI

Date: 2026-09-30. Independently mathematically audited. This is a one-way implication/admission test, not a proof of the proposed inequality and not a claim of equivalence in both directions. Full FEI remains open.

## Definitions matched to the collision route

Let f be Boolean with full Walsh support. Put P_S=fhat(S)^2, q_i=Inf_i(f), and let Q be the independent Bernoulli law with marginals q_i. Full support ensures 0<q_i<1. Write s_S=sign(fhat(S)), b_S=s_S sqrt(Q_S), and

    C_U=sum_S b_S b_(S symmetric_difference U),
    v_U=C_U^2, Z=sum_U v_U,
    L=sum_U v_U log2(1/v_U), T=L/Z,
    K=D_KL,bits(P||Q)=sum_i h2(q_i)-H(P).

In particular T=H(v/Z)-log2 Z; it is NOT H(v/Z). No support-conditioned reference is needed here because support is full.

## Theorem

If there is a finite constant kappa>=0 such that every full-support Boolean function with I(f)<=1/16 satisfies

    K >= T/4-kappa I(f),                                         (A)

then every Boolean function satisfies

    H(f)<=(kappa+2+log2 e) I(f).                                 (B)

Thus even the small-total-influence, full-support subdomain of (A) retains the entire unrestricted FEI obligation.

## 1. Local low-influence estimate

Put t=sum_i q_i and S=sum_i q_i log2(1/q_i). For any U, the triangle inequality and factorization of Q give

    |C_U|<=sum_A sqrt(Q_A Q_(A triangle U))
          =product_(i in U) 2sqrt(q_i(1-q_i)).

Therefore

    v_U<=product_(i in U) 4q_i(1-q_i),
    1<=Z<=product_i[1+4q_i(1-q_i)]<=exp(4t).                     (1)

Also |C_U|<=1 by Cauchy-Schwarz, so every entropy summand in L is nonnegative.

For a singleton U={i}, separating its two bit values gives

    C_{i}=2sqrt(q_i(1-q_i)) E_(Q_-i)[s_A s_(A union {i})].

The empty atom of Q_-i has mass at least 1-t. Regardless of all other signs, the absolute expectation is at least 1-2t. Consequently

    4q_i(1-5t)<=v_i<=4q_i.                                     (2)

Here (1-q_i)(1-2t)^2 >=1-q_i-4t>=1-5t. When 0<t<=1/16, the logarithms log2(1/(4q_i)) are positive. Retaining only singleton terms in L and using both sides of (2) yields

    L>=4(1-5t) sum_i q_i log2(1/(4q_i))
      =4(1-5t)(S-2t).

The quantity S-2t is positive, since q_i<=t<=1/16. Combining with (1), exp(-4t)>=1-4t, and (1-5t)(1-4t)>=1-9t,

    T/4>=(1-9t)(S-2t).                                        (3)

The elementary entropy bound h2(q)<=q log2(1/q)+(log2 e)q gives

    K<=S+(log2 e)t-H(f).

Insert (A) and (3) and rearrange:

    H(f)<=(kappa+2+log2 e)t+9tS-18t^2
         <=(kappa+2+log2 e)t+9tS.                              (4)

Finally entropy concavity gives S<=t log2(n/t).

## 2. Full-support tensor seeds

Fix an arbitrary nonconstant Boolean seed g in dimension d. Tensor m independent copies, with N=dm. Its entropy is mH(g) and its influence is mI(g).

For N>=2, if a Boolean truth table has an odd number of negative values, every unnormalized Walsh sum is 2 modulo 4 and hence nonzero. Thus by flipping at most one truth-table point of the tensor we obtain u_m with full Walsh support.

The perturbation has Fourier coefficient l2 distance at most 2^(1-N/2). By Cauchy-Schwarz, the total variation between the squared-coefficient distributions is at most the same number. The elementary finite-alphabet entropy continuity bound

    |H(P)-H(P')|<=h2(tau)+tau log2(2^N-1)

therefore tends to zero. It follows, for sufficiently large m, by coupling the two distributions with disagreement probability tau and applying the entropy chain rule. Flipping one physical point changes at most N incident edges, giving influence difference at most 2N 2^-N. Hence

    H(u_m)=mH(g)+o(1), I(u_m)=mI(g)+o(1).                       (5)

These modifications are a proof construction, not a computational enumeration.

## 3. Rare activation

Take r=ceil(sqrt(m)), p=2^-r, A(z)=1{z=0} on r controls, and

    F_m(x,z)=1+A(z)(u_m(x)-1).

All Walsh coefficients are nonzero: nonempty data coefficients are p uhat_m(T); empty-data/nonempty-control coefficients are p(Eu_m-1), nonzero because u_m is nonconstant; and the fully empty coefficient is 1-p+pEu_m>0 for r>=2. This is again a genuine Boolean function.

The exact influence identity is

    t_m=I(F_m)=p[I(u_m)+r(1-Eu_m)].                            (6)

Write w0=(Eu_m)^2. Summing only nonempty-data Fourier packets gives entropy exactly

    p[H(u_m)-w0 log2(1/w0)+2r(1-w0)].

All other entropy contributions are nonnegative, and x log2(1/x)<=1/(e ln2), so

    H(F_m)>=p[H(u_m)-1/(e ln2)].                               (7)

Since I(g)>0 is fixed,

    t_m=p[mI(g)+O(sqrt(m))],
    n_m=dm+r,
    log2(n_m/t_m)=r+O(1),
    t_m log2(n_m/t_m)->0.                                     (8)

In particular (4) applies for sufficiently large m. Divide it by pm and use (5)-(8). The main influence term tends to (kappa+2+log2 e)I(g). The error satisfies

    9t_m S_m/(pm)
       <=9[t_m/(pm)] t_m log2(n_m/t_m)->0.

The lower entropy bound (7) tends to H(g), proving (B). Constant seeds are trivial. QED.

## Independent review and interpretation

A separate reviewer checked all local inequalities, coefficient 1/4, parity perturbation, entropy continuity, full-support preservation, exact activation formulas and limiting factors. No substantive gap was found. The hypothesis only needs the stated small-influence full-support domain.

This does not reject the collision route. It prevents treating its universal normalized lower bound as already materially easier than FEI merely because it is tensor-additive. A proof of (A) with any finite kappa would be a complete FEI proof through the reduction above.

The tensor-and-sparse-activation architecture also has earlier literature: Shalev, On the Fourier Entropy Influence Conjecture for Extremal Classes, arXiv:1806.03646, establishes that suitable small-influence FEI classes imply unrestricted FEI. The specific normalized collision admission estimate (1)-(4) is what is checked here; no priority claim is made for the underlying activation reduction.

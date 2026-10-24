# Remaining Fourier route: a count-Fisher inequality and one nuisance variance

17 September 2026. **PARTIAL; all global claims below are explicitly conditional.** The full Lyons conjecture and the remaining Fourier region are open in this work. This note preserves the last concrete route after the proved ratio-domain theorem. No independent audit or historical-priority claim is made.

## 1. The sufficient inequality

Let `I_N` be the 4-by-4 Fisher information matrix of the total count law, using affine coordinates `(a,b,x,y)`. For `O<P`, set `l=log(P/O)>0`. The unproved candidate is

    (2/5) I_N - 2l(e_a e_b^T+e_b e_a^T) >= 0.       (1)

Equivalently, in every direction `(c,d,u,v)`,

    (2/5) I_count >= 4cd log(P/O).                  (2)

For `cd<=0`, this is automatic. The proved local estimate in `FOURIER_POSITIVE_IMBALANCE.md` gives

    -H'' >= (2/5)I_count+I_excess-4cd log(P/O).

Therefore a proof of (1) throughout the negative-imbalance domain, combined with the already proved nonnegative-imbalance theorem, would prove concavity for the complete four-site Fourier family. It would still not prove Lyons's conjecture for arbitrary kernels.

The elementary Cramer-Rao estimate already proves (1) when `Var(N) log(P/O)<=8/5`. The only needed extension is outside that domain.

## 2. An exact scalar version of the count-Fisher candidate

First assume the four eigenvalues are pairwise distinct, so the count probability map has full rank. Let

    V_A=lambda_0(1-lambda_0)+lambda_2(1-lambda_2),
    V_B=lambda_1(1-lambda_1)+lambda_3(1-lambda_3).

The mean-coordinate block of the inverse count Fisher matrix has the exact form

    (I_N^(-1))_{a,b}
       =[[V_A/4+tau, -tau],[-tau,V_B/4+tau]],       (3)

where `tau>=0`. One way to see the form is to note that `a+b=E(N)/2`. Under a common log-odds shift of all four Bernoulli parameters the count score is `N-E N`; its derivative of `a` is `V_A/2`, and similarly for `b`. The resulting row-sum identities are `U_aa+U_ab=V_A/4` and `U_bb+U_ab=V_B/4`. Data processing of Fisher information gives `U_aa>=V_A/4`, so `tau=-U_ab>=0`.

For more explicit verification, an influence function determining tau is given in the next section. It also proves these identities without treating the inverse matrix as a black box.

Whiten the rank-two mean correction in (1) by `I_N^(-1/2)`. Its only positive eigenvalue is

    2l[ sqrt((V_A/4+tau)(V_B/4+tau))-tau ].         (4)

Thus (1) is equivalent, on this generic domain, to the single inequality

    2l[ sqrt((V_A/4+tau)(V_B/4+tau))-tau ] <= 2/5.  (5)

If this were proved for all distinct eigenvalues, continuity of the original count Fisher matrix would extend (1) to collisions. One must use (1), not a potentially singular inverse, at those collisions.

## 3. Tau from a four-term observable of the count

Put

    A=a^2-x^2, B=b^2-y^2,
    C=A-B, E=aB-bA,
    D=C^2+4(a-b)E.

Here A and B are the probabilities that both spectral trials in their respective groups succeed. D is the resultant of the two pair generating polynomials, and is nonzero when no eigenvalue in one group equals an eigenvalue in the other.

Define four coefficients

    kappa=(4aE+AC, -2E, -C, 2(a-b)),

and the frozen observable on `k=0,1,2,3,4`

    Z(k)=sum_(j=1)^4 kappa_j binom(k,j),
    phi_a(k)=Z(k)/(2D).

Subtract its expectation when taking covariance. The count generating polynomial in the variable `w=z-1` is

    (1+2aw+Aw^2)(1+2bw+Bw^2).

Differentiating its four coefficients in coordinates `(a,b,A,B)` gives the exact relations

    2kappa_1+4b kappa_2+2B kappa_3=2D,
    2kappa_1+4a kappa_2+2A kappa_3=0,
    kappa_2+2b kappa_3+B kappa_4=0,
    kappa_2+2a kappa_3+A kappa_4=0.                 (6)

Thus the centered phi_a has covariance one with the `a` score and covariance zero with the other three coordinate scores. On the full-rank count model, the centered score space is the entire four-dimensional space of centered observables on five count values. Consequently phi_a is the efficient influence function for a, and

    tau=Var(Z)/(4D^2)-V_A/4.                      (7)

The corresponding influence function for b is `N/2-phi_a`, up to centering. Direct polynomial expansion also gives

    Cov(Z,N)=D V_A,
    V_A=2a+2A-4a^2, V_B=2b+2B-4b^2.              (8)

Equations (7)-(8) recover every entry of (3). They make (5) an explicit scalar inequality in four real parameters involving only rational functions, one square root, and `log(P/O)`.

## 4. What the experiments establish, and what they do not

`explore_fourier_count_fisher.py` targets (1) specifically in the uncovered region `Var(N)log(P/O)>8/5`. Three differential-evolution runs used seeds 901, 902, and 903, each with 4840 evaluations. They found no negative candidate, approached the boundary of the already proved region, and hit their iteration limits without optimizer convergence. Output is in `fourier_count_fisher_exploration.json`. This is not a global proof.

An additional exploratory scan of 18,000 logit samples with seed 95 found a largest required coefficient in (4) of about 0.26513, below the available 0.4. This scan was used only to formulate (5), not to assert its sign. Its extremal eigenvalues were approximately `(0.88556079,0.04808845,0.75495167,0.12645179)`.

Replacing the logarithm by `(P-O)/sqrt(PO)` is too crude at nearly complementary projection pairs: numerical tests of that stronger sufficient matrix bound produced negative values. No such substitution is part of the proved theorem.

`verify_fourier_fisher.py` checks the polynomial identities (6)-(8), the resultant identity, the influence-function covariance against an exactly inverted rational Fisher matrix, and selected instances of (1) with exact logarithm enclosures. Those finite instances and identities do not settle (5) globally.

The remaining mathematical obligation is to prove (5), find a counterexample to this sufficient inequality and return to the full scalar criterion `Phi_F`, or find a certified negative value of the actual Fourier entropy Hessian. A counterexample to (1) alone would not refute Lyons.

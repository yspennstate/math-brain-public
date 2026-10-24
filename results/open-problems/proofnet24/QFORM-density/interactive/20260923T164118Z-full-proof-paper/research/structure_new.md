# New grouped-projection and arbitrary-rank crossing estimates

All statements below are mathematical deductions, not claims of literature novelty. Fourier convention: hat f(xi)=integral exp(i xi.x) f(x) dx. Product coordinates have probability densities bounded by one. We use the orthonormal projection bound p_{PX} <= 2^{r/2} in dimension r, and the scalar Fourier bound integral |psi|^p <= 4 pi/sqrt(p), p>=2. Neither a pointwise Fourier bound nor independence after rotation is used.

## 1. Exact-rank crossing block with arbitrary internal functions

Let X and Y be independent random vectors. Let B=U S V^T have exact rank r, U,V orthonormal column frames, and S=diag(s_1,...,s_r)>0. Assume U^T X and V^T Y have densities bounded by M_X and M_Y. For arbitrary measurable real F,G, let Q=F(X)+2 X^T B Y+G(Y). Then

    |phi_Q(t)| <= min(1, (pi/|t|)^(r/2) (M_X M_Y)^(1/2) (s_1...s_r)^(-1/2)).

For r>2 it follows that

    ||p_Q||_infty <= r/(r-2) (M_X M_Y/(s_1...s_r))^(1/r).

For independent scalar coordinates on both sides, this is at most 2r/(r-2) (s_1...s_r)^(-1/r). If one side consists of exactly r original coordinates, its projection density bound is one and the constant improves accordingly.

Proof. Push the complex measure exp(itF(X))dP_X onto u=U^TX; it has an L1 density a_t with |a_t|<=p_U, hence ||a_t||_2^2<=M_X. The analogous density b_t satisfies ||b_t||_2^2<=M_Y. Fubini gives phi_Q(t)=integral hat a_t(2tSv)b_t(v)dv. Cauchy--Schwarz and Plancherel give the displayed estimate, because integral |hat a_t(2tSv)|^2dv=(pi/|t|)^r(det S)^(-1)||a_t||_2^2. Integrating min(1,K|t|^(-r/2)) gives the density bound. Complex pushforwards can be defined by disintegration or Radon--Nikodym; no conditional density bound is assumed. QED.

## 2. Weighted-subset Fourier lemma (arbitrary row rank)

Let D have independent scalar coordinates with densities <=1. Let M be a k by m full-row-rank matrix, with product of singular values S_M. Let A have rows a_i and C=A(I-Pi), where Pi is orthogonal projection onto row(M). For an integer ell>=1 put

    Z_ell = sum_{|S|=ell} det(C_S C_S^T) >0,
    w_S = det(C_S C_S^T)/Z_ell,
    alpha_i = sum_{S containing i} w_S.

Assume alpha_i<=1/2 for every i. Let psi_i be characteristic functions of independent scalar laws of density<=1. If kappa is any nonnegative probability density on R^k, then for t !=0,

    E[kappa(MD) product_i |psi_i(2t<a_i,D>)|]
      <= [2^((k+ell)/2) (2pi)^ell exp(ell/2)]
          / [S_M sqrt(Z_ell) |t|^ell].                    (WS)

For ell=1 the factor exp(ell/2) may be omitted.

Proof. Rows with alpha_i=0 have c_i=0 and their factors may be discarded. Weighted Holder for the finite positive measure kappa(Md)dP_D(d), using weights w_S, bounds the left side by product_S I_S^{w_S}, where

    I_S=E[kappa(MD) product_{i in S}|psi_i(2t<a_i,D>)|^(1/alpha_i)].

Indeed the exponent of the i-th factor in the product is sum_{S containing i}w_S/alpha_i=1. Zero weights are omitted. Write a_i=c_i+lambda_i M. The random vector (MD,(<c_i,D>)_{i in S}) has a joint density at most

    2^((k+ell)/2)/(S_M sqrt(det(C_S C_S^T))).

This follows by factoring the linear map into an orthonormal (k+ell)-projection followed by an invertible matrix; its Gram determinant is S_M^2 det(C_S C_S^T), since the c_i are perpendicular to row(M). Change the last ell coordinates by the shifts lambda_i x for each x=MD, integrate kappa, and apply the scalar Lp bound. Thus

    I_S <= [2^((k+ell)/2) (2pi)^ell]/[S_M |t|^ell]
             * (product_{i in S}sqrt(alpha_i))/sqrt(det(C_S C_S^T)).

Taking the weighted geometric mean yields the same first factor times

    Z_ell^(-1/2) exp{[H(w)+sum_i alpha_i log alpha_i]/2}.

Regard S as a random subset with distribution w. Entropy subadditivity for its indicator coordinates gives H(w)<=sum_i[-alpha_i log alpha_i-(1-alpha_i)log(1-alpha_i)]. Since -(1-a)log(1-a)<=a and sum_i alpha_i=ell, the exponent is at most ell/2. For ell=1, w_{i}=alpha_i and the entropy expression cancels exactly. QED.

## 3. Grouped hubs with an arbitrary-rank projected crossing remainder

Let X_H and X' be independent. Suppose X' has independent coordinates with densities<=1, and U has k orthonormal columns in the hub coordinate space. Suppose W=U^T X_H has density bounded by M_H. No independence is assumed among the coordinates of W. Let

    Q = F(X_H)+2 <W, M X'+beta> + R(X'),

where F is arbitrary measurable, M is k by m of rank k, and R is an arbitrary quadratic polynomial with matrix A_R. Split the light coordinates into I,J, with M_J of rank k and singular-value product S. Define

    C=(A_R)_{I,J}(I-Pi_row(M_J)),
    Z_ell=e_ell(CC^T),

and let alpha_i be the ell-volume row marginals of C. Suppose Z_ell>0 and every alpha_i<=1/2. Set d=k+ell. Then

    |phi_Q(t)| <= min(1, K |t|^(-d/2)),
    K = M_H^(1/2) 2^((k+3ell)/4) pi^(d/2) exp(ell/4)
             S^(-1/2) Z_ell^(-1/4).

For d>2,

    ||p_Q||_infty <= d/(d-2) 2^((k+3ell)/(2d)) exp(ell/(2d))
                       M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d)).       (GC)

For ell=1 omit the exponential factors. C need not have exact rank ell. All terms in A_R internal to I or internal to J, every diagonal, every linear term, and arbitrary internal hub functions are allowed.

Proof. Let a_t be the complex density obtained by pushing exp(itF(X_H))dP_H onto W. Then |a_t|<=p_W and ||a_t||_2^2<=M_H. Define h_t(l)=hat a_t(2t(l+beta)). Plancherel gives integral |h_t|^2 <= M_H(pi/|t|)^k. Let mu_t(l) be the density of the complex measure E[exp(itR(X')); M X' in dl]. Its modulus is bounded by the density of MX', so mu_t belongs to L2. Then phi_Q(t)=integral h_t(l)mu_t(l)dl and |phi_Q(t)|^2 <= M_H(pi/|t|)^k integral |mu_t|^2.

To estimate the latter integral, convolve mu_t with a nonnegative normalized even compactly supported approximate identity k_h in R^k. Write m_h(l)=E[exp(itR(X'))k_h(l-MX')]. Conditional Cauchy--Schwarz in X_I, followed by integration in l and an independent copy X_J*, gives

    integral |m_h|^2 <= E[exp(it(R(X_I,X_J)-R(X_I,X_J*))) kappa_h(M_J D_J)],

where D_J=X_J-X_J*, kappa_h=k_h*k_h is a nonnegative probability density. All terms purely in I cancel. The terms purely in J give a phase of modulus one. Averaging the I coordinates and taking absolute values therefore bounds the expression by

    E[kappa_h(M_J D_J) product_{i in I}|psi_i(2t<(A_R)_{i,J},D_J>)|].

The coordinates of D_J are independent with densities at most one. Apply (WS), uniformly in h, and pass to the limit using L2 approximate-identity convergence. This bounds integral |mu_t|^2 by 2^((k+ell)/2)(2pi)^ell exp(ell/2)/(S sqrt(Z_ell)|t|^ell). Combine with the hub Plancherel estimate. The density bound follows by integrating the minimum. QED.

## 4. Specific consequences and limits

* One original hub, ell=2: for arbitrary-rank C with 2-volume row marginals<=1/2,

      ||p_Q||_infty <= 3*2^(7/6)*exp(1/3) (|w_J|^2 Z_2)^(-1/6) < 9.4 (|w_J|^2 Z_2)^(-1/6).

  This removes the exact-rank-two hypothesis in the previous projected crossing estimate. In particular, additional dense crossing terms are admissible when their volume marginals remain spread.

* Arbitrarily many original hubs, exact-rank-two crossblock B=UM: every internal hub quadratic or measurable function is allowed. If the projected light crossing C has F>0 and each squared row norm<=F^2/2, then

      ||p_Q||_infty <= 3*2^(5/6) M_H^(1/3)(S F)^(-1/3).

  For product hub laws M_H<=2, giving constant 3*2^(7/6)<6.74. This handles arbitrary internal hub couplings in the exact-rank-two group, not merely hub functions depending on U^T X_H.

* More generally k+ell>2 is the threshold in (GC). This recovers the gain from either three hub directions, two hub directions plus one projected crossing direction, or one hub plus two crossing directions.

* The theorem does NOT show that every no-pivot matrix with three large eigenvalues admits such a split with S and Z_ell uniformly bounded below and marginals<=1/2. It also does not remove the small-leak parameter in Q_eps=2X_hL+V^2+2eps LP: the second projected crossing direction has size proportional to eps, so the displayed bound still deteriorates as eps tends to zero. Nearly rank-two hub crossblocks still require work.

## Addendum, 2026-09-23T17:05:55Z: correction to the skeleton identity

The current structure/REPORT.md Theorem 3.1 states an exact volume-sampled skeleton identity. Its valid general form is an upper bound:

    E_{S,T} sum_{l,m outside S union T, l!=m} (A-P^{ST})_lm^2
       <= (r+1)^2 V_{r+1}(A)/V_r(A).

Here V_r is the sum of squared disjoint r-minors, the sampling probability is det(A_ST)^2/V_r, zero weights are omitted, and P^{ST}=A_{.,T}A_ST^{-1}A_{S,.}. The issue is that a singular r-minor can have a nonsingular (r+1)-extension. Such a seed has zero sampling probability but contributes a positive term to the proposed right-side equality.

Full proof of the corrected inequality: for each nonsingular seed, the bordered determinant formula gives det(A_{S+l,T+m})^2=det(A_ST)^2(A-P^{ST})_lm^2. On summing, each disjoint pair of (r+1)-sets is counted at most (r+1)^2 times, according to the deleted distinguished row and column. Deletions leaving a singular seed are absent. Division by V_r proves the inequality.

Exact counterexample to equality: A is the 4-by-4 adjacency matrix with edges 1--3 and 2--4, all other entries zero, and r=1. Then V_1=4, V_2=4. Every nonzero seed leaves two residual off-diagonal unit entries, so the left side is 2. The claimed right side is 4. A fractions-only Python calculation verifies these exact integers; no floating point is used.

The robust corollary survives unchanged: choosing a seed with residual Frobenius norm <=(r+1)sqrt(V_{r+1}/V_r), symmetrizing its rank-r light block, taking a best rank-r symmetric approximation, and retaining the 2r skeleton coordinates gives A=D+R+E with rank R<=4r and ||E||_F<=3(r+1)sqrt(V_{r+1}/V_r). The complete proof, including the range containment needed for the rank bound, is in paper_work/structure.tex, Theorem robust-skeleton.

The grouped crossing arguments above were independently read in full by a second researcher in this session; no gap was reported. This is one preliminary check, not a completed literature review or unrestricted-conjecture closure.

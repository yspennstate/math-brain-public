# B14 r27 substantive checkpoint: subprobability homogeneity of the D_k volume certificate

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

## First unpaid implication attacked

Can a Claude D_k cross-volume exit be applied *after* arbitrary product-fragment localization without paying a support/fragment tax? The calculation below shows the exact homogeneity. It gives both a safe-coordinate criterion and a sharp obstruction: fragmenting every volume-active coordinate forces an N^2 certificate loss for equal N-way fragments, independently of k.

## Subprobability D_k calculation

Let I,J be disjoint original-coordinate sets and M=A_{I,J}. Let f_l be one-dimensional subprobability densities with 0<=f_l<=1 and masses m_l in (0,1]. Put

  nu(dx)=prod_l f_l(x_l) dx_l,

and let Phi(t)=int exp(it Q(x)) dnu(x), where all self blocks and affine terms of Q are arbitrary. Let Z_k=e_k(M^T M)>0, let w_ST=det(M_ST)^2/Z_k be the k-volume sampling law, and let alpha_i=P_w(i in S), beta_j=P_w(j in T). Assume q>=1, q<k/2, and alpha_i<=q/2 for all i.

For every cap-one subdensity f of mass m and p>=2,

  int |fhat(s)|^p ds <= (4 pi/sqrt(p)) m^(p-1).                 (1)

Indeed h(y)=f(my) is a cap-one probability density, fhat(t)=m hhat(mt), and Claude's completed L^p lemma applies to h.

Cauchy-Schwarz in the I variables gives

  |Phi(t)|^2 <= m_I int prod_i |fhat_i(2t(Mw)_i)| prod_j g_j(w_j) dw, (2)

where m_I=prod_{i in I}m_i and g_j=f_j*f_j_tilde has mass m_j^2 and cap <=m_j. Writing F for the product of the Fourier factors and using Holder against the finite measure prod_j g_j,

  int F dg <= (int F^q dg)^(1/q) m_J^(2-2/q).                 (3)

The same Brascamp-Lieb/determinant step as Claude D_k, together with (1), gives

  int F^q dg
   <= e^(k/2) (2pi/|t|)^k q^(-k/2) Z_k^(-1/2)
      prod_i m_i^(q-alpha_i) prod_j m_j^(2-beta_j).           (4)

Hence, with a=k/(2q)>1,

  |Phi(t)| <= C_tail |t|^(-a)
      prod_i m_i^(1-alpha_i/(2q))
      prod_j m_j^(1-beta_j/(2q)),                             (5)

where C_tail is exactly the probability-case D_k Fourier constant. The trivial bound is |Phi(t)|<=W:=prod_l m_l. Integrating min(W,C|t|^-a) and dividing by 2pi yields

  ||p_{Q#nu}||_infty
  <= C_{k,q} Z_k^(-1/(2k))
     prod_i m_i^(1-alpha_i/k)
     prod_j m_j^(1-beta_j/k),                                 (6)

  C_{k,q}=2sqrt(e) [a/(a-1)] q^(-1/2).

The striking point is that the mass exponents 1-alpha_i/k and 1-beta_j/k are independent of the Holder/Jensen parameter q.

## Exact fragment tax and safe localization criterion

Partition each marginal into subdensities of masses m_{l,r}, sum_r m_{l,r}=1, and apply (6) separately on every Cartesian product cell before summing. The resulting certificate is multiplied by

  prod_i [sum_r m_{i,r}^(1-alpha_i/k)]
  prod_j [sum_r m_{j,r}^(1-beta_j/k)].                        (7)

Thus a fragmented coordinate is zero-tax exactly when its relevant volume marginal is zero. If every active coordinate is split into N equal fragments, (7) is

  N^{(sum_i alpha_i+sum_j beta_j)/k}=N^2,                     (8)

because both marginal sums equal k. This N^2 loss is universal in k: D_5 removes the marginal gate but does not remove the localization homogeneity deficit.

Target-valid witness for the final report: A=[[0,I_5],[I_5,0]] has eigenvalues +1 and -1, each fivefold. Claude D_5 gives the whole cap-one product law ||p_Q||_infty<=5sqrt(2e). If every one of the ten marginals is a union of N distant intervals of length 1/N and one first decomposes into the N^10 product cells, then (6) has alpha_i=beta_j=1 and gives 5sqrt(2e)N^-8 per cell; summing the black-box bounds gives 5sqrt(2e)N^2. The law itself remains uniformly controlled by direct D_5. This is a proof-order obstruction, not a QFORM counterexample.

Next: read/apply the newest account03/B14 partner whole-bank theorem to show a complementary aggregate-before-inversion branch that remains uniform on the same rough-support class, then publish the full proof and handoff.

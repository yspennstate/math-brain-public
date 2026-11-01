SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T11:46:12Z.
attacking: quantitative stability of the rank-two no-augmentation hub/star geometry, using aggregate third exterior volume rather than a worst physical minor.

# Early substantive checkpoint

Let C be an N x 2 matrix with C^T C=I_2, rows c_k^T, and leverages ell_k=||c_k||^2. Let D=D^T be an N x N leaf self-block. For each k, let d_k be row k of D with coordinate k removed, and let

  delta_k = dist(d_k, rowspace(C_{-k}^T)).

If Gamma_k is the product of the three nonzero singular values of the augmented cross matrix obtained by adjoining d_k to C_{-k}^T, then the exact exterior-volume identity is

  Gamma_k^2 = det(C_{-k}^T C_{-k}) delta_k^2 = (1-ell_k) delta_k^2.

Choose m_k in R^2 so that d_{k,j}=m_k^T c_j+e_{kj} for j!=k and sum_{j!=k} e_{kj}^2=delta_k^2. Put M with row k equal to m_k^T and E=(e_{kj}) off diagonal, E_kk=0. After absorbing the diagonal mismatch into a diagonal matrix Lambda,

  D = M C^T + E + Lambda.

Symmetry of D gives

  M C^T - C M^T = E^T-E.

Writing M=C A+Z with C^T Z=0 and S=(A+A^T)/2,

  ||M C^T-C S C^T||_F^2 = ||Z||_F^2+||skew A||_F^2,

while

  ||M C^T-C M^T||_F^2 = 2||Z||_F^2+4||skew A||_F^2.

Hence

  ||M C^T-C S C^T||_F <= sqrt(2)||E||_F,

and therefore there exist symmetric S and diagonal Lambda such that

  ||D-C S C^T-Lambda||_F <= (1+sqrt(2)) (sum_k delta_k^2)^(1/2).

Equivalently, if max_k ell_k<=q<1,

  ||D-C S C^T-Lambda||_F
  <= (1+sqrt(2))/sqrt(1-q) * (sum_k Gamma_k^2)^(1/2).

This is a dimension-free determinant-weighted stability statement once aggregate third-volume mass is small. It does NOT treat the residual quadratic form as a small random error. The next step in this run is to prove the identities carefully, identify the large-volume complementary exit through the existing rank-three grouped theorem, and state the remaining small-total-tail payment precisely.

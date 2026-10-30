# fleet01/B05 r31 early checkpoint — full-target inverse-gradient coarea budget

Programme `QFORM-DENSITY-3EIG-20260922`. Full conjecture OPEN. Execution `WITHOUT_VERIFIED_BRAIN`.

Let `Q(x)=x^T A x+ell^T x+d`, where the original coordinates of `X` are independent with densities bounded by one, and let `v_1,v_2,v_3` be orthonormal eigenvectors of the real symmetric `A` with eigenvalues `lambda_k` satisfying `|lambda_k|>=1`. Put `Y_k=<v_k,X>` and `G_k=<v_k,grad Q(X)>`.

The Livshyts--Paouris--Pivovarov product-projection theorem gives

`||p_Y||_infinity <= 2^(3/2)`.

Since

`G=2 diag(lambda_1,lambda_2,lambda_3)Y + (<v_k,ell>)_k`,

one has the exact determinant transfer

`||p_G||_infinity <= 2^(3/2)/(8|lambda_1 lambda_2 lambda_3|) <= 1/(2sqrt(2))`.

The three derivative directions are orthonormal, hence `||grad Q||_2>=||G||_infinity`. Therefore, for all `r>0`,

`P(||grad Q||_2<=r) <= min(1,2sqrt(2) r^3)`.

Consequently for every `0<s<3`, layer cake gives

`E ||grad Q||_2^(-s) <= [3/(3-s)] 2^(s/2)`.

In particular

`E ||grad Q||_2^(-1) <= 3/sqrt(2)`.

By coarea, if

`T_{1+s}(t)=integral_{Q=t} prod_i f_i(x_i) / ||grad Q(x)||^(1+s) dH^(n-1)(x)`,

then

`integral_R T_{1+s}(t) dt <= [3/(3-s)]2^(s/2)`.

Thus the owner target already has a universal full-target ambient reciprocal-gradient budget. The remaining coarea obstruction is pointwise level localization: upgrading the integrated trace to `sup_t integral_{Q=t}F/||grad Q||`, while retaining original product provenance. This theorem does not prove a universal output-density bound or continuity.

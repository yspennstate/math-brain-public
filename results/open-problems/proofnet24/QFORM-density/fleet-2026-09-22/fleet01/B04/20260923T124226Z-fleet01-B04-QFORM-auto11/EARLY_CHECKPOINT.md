SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T12:42:26Z.
attacking: optimize an admissible projection/volume-weight certificate on the actual matrix by downshifting fourth-volume sampling to a strict third-volume Fourier weight.

# Early substantive checkpoint

Let M=A[I,J] be an original-coordinate cross block with E4(M)=e4(M^T M)>0. For a physical three-row set S write

    a_S = det(M[S,:] M[S,:]^T)

and for a four-row set R write

    d_R = det(M[R,:] M[R,:]^T).

For a_S>0 let V_S be the span of the three physical row vectors and put

    tau_S = sum_j dist(m_j,V_S)^2.

The Gram height identity gives, for j notin S,

    d_{S union {j}} = a_S dist(m_j,V_S)^2,

hence

    b_S := sum_{j notin S} d_{S union {j}} = a_S tau_S.

Cauchy--Binet gives sum_R d_R=E4(M), and counting the four faces of every four-set gives

    sum_S b_S = 4 E4(M).

Therefore

    mu(S)=a_S tau_S/[4 E4(M)]

is a probability law on physical row triples. Equivalently: sample a canonical squared fourth-volume four-row set R with probability d_R/E4(M), then delete one of its four rows uniformly.

If rho_i is the row inclusion probability under that fourth-volume law, the downshifted triple law has the exact marginal identity

    alpha_i=(3/4) rho_i.

Lift mu to full physical 3x3 minors by retaining the canonical conditional column law

    w(S,T)=mu(S) det(M[S,T])^2/a_S.

Then the entropy-adjusted determinant currency is exactly

    G(w)=exp(sum_{S,T} w log(det(M[S,T])^2/w(S,T)))
        = 4 E4(M) / tau_geo,

where tau_geo=exp(sum_S mu(S) log tau_S). Since tau_S<=||M||_F^2,

    G(w)>=4 E4(M)/||M||_F^2.

Thus the already-completed entropy-weighted third-volume Fourier theorem applies whenever rho_*:=max_i rho_i<1, with

    q4=max{1,(3/2)rho_*}<3/2,

because alpha_*=(3/4)rho_*=q4/2 when the second term dominates. It yields a continuous density and the explicit prospective bound

    ||p_Q||inf <= [3e/((3-2q4)sqrt(q4))]
                 [4 E4(M)/tau_geo]^(-1/6)

and hence the simpler Frobenius certificate with tau_geo replaced by ||M||_F^2.

The exact endpoint rho_*=1 is not paid by this downshift itself. The next work is to verify all zero-face cases carefully, apply the theorem to a genuinely rotated target-valid family, and compare it on the same matrix with a completed fleet02/B04 product-Fourier theorem.

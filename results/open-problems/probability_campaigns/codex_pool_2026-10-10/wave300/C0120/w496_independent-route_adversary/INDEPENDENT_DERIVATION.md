# C0120: independently derived spectral criterion and common-layer split

Recorded 2026-10-10 before reading any w495 claim/proof. Source model: g_v are independent N(0,1), and M_n is the maximum of sum_{v in p} g_v over up-right paths with n vertices starting at (0,0). Each path visits exactly one vertex of V_t={(i,t-i):0<=i<=t} for t=0,...,n-1. The endpoint is free. This is the ground-state model in Section 8 of arXiv:0810.4221v2, rather than a positive-temperature partition function.

## 1. Gaussian Sobolev and chaos identities

There are finitely many paths. Two distinct path sums have a nonzero Gaussian difference, so ties have probability zero. Outside the finite union of tie hyperplanes, the gradient of M_n is the indicator of its unique maximizing path. Hence ||grad M_n||^2=n almost surely. M_n is globally sqrt(n)-Lipschitz and belongs to the Gaussian first-order Sobolev space.

Expand F_n=M_n-E M_n in normalized multivariate Hermite polynomials. Let v_{n,k} be its squared L2 mass of total degree k, k>=1. Orthogonality and the derivative identity D_i H_alpha=sqrt(alpha_i) H_{alpha-e_i} give

    Var(M_n)=sum_{k>=1} v_{n,k},
    sum_{k>=1} k v_{n,k}=E||grad M_n||^2=n.

The derivative identity holds first for polynomial truncations and then in the Sobolev norm; equivalently the Hermite expansion diagonalizes the closed Gaussian Dirichlet form. This is the only analytic closure input. No per-layer probability product is used.

For an integer K>=1, write L_n(K)=sum_{1<=k<=K} v_{n,k}. Then

    Var(M_n) <= L_n(K) + n/(K+1).

Thus a bound L_n(ceil(n^delta))<=C n^(1-delta), uniform in n, would prove Var(M_n)<= (C+1)n^(1-delta). The missing model-specific input is suppression of chaos mass through a degree growing polynomially with n. Merely changing the representation does not supply it. Conversely a power variance bound controls every L_n(K), so this criterion is a useful proof obligation, not an independently easier theorem.

For g^u=e^(-u)g+sqrt(1-e^(-2u))g', the same orthogonality gives

    O_n(u)=E<grad M_n(g),grad M_n(g^u)>
          =sum_{k>=1} k v_{n,k} e^(-(k-1)u).

Here O_n(u) is the expected intersection size of the two maximizing paths. Consequently Var(M_n)=integral_0^infinity e^(-u)O_n(u)du. The exponential integration factor must be retained. All series are nonnegative, so Tonelli justifies this identity. O_n is decreasing, even though path indicators need not be independently coupled across layers.

## 2. Exact layer-average decomposition

Let A_t=(t+1)^(-1) sum_{v in V_t} g_v and R_v=g_v-A_t for v in V_t. Cov(A_t,R_v)=0 for every residual on that layer. The complete vector is jointly Gaussian, and layers are independent; therefore (A_t)_t is independent of the complete residual vector R. This derives the joint independence explicitly, rather than inferring it from separate conditional means.

Every path visits one vertex of each V_t, so pointwise

    M_n(g)=sum_{t=0}^{n-1} A_t + M_n(R).

It follows exactly that

    Var(M_n)=H_n+Var(M_n(R)),    H_n=sum_{t=0}^{n-1}1/(t+1).

The residual coordinates within each layer are correlated, with covariance I-J/(t+1). The original iid Gaussian theorem must not be silently reapplied to R. This decomposition gives Var(M_n)>=H_n and identifies a path-independent Gaussian component; it gives no upper bound on the residual variance. In particular a bounded-variance claim for this source model is false, but the desired n^(1-delta) bound with 0<delta<1 is compatible with H_n.

## 3. A spectral obstruction, explicitly outside the polymer class

Let k_n=ceil(log n) and F_n=sqrt(n/k_n) H_{k_n}(G), where H_k is the normalized one-dimensional probabilists' Hermite polynomial and G~N(0,1). Then Var(F_n)=n/k_n and E|F_n'|^2=n. Every fixed chaos degree eventually has zero mass, yet no fixed power improvement holds. Its normalized gradient covariance is e^(-(k_n-1)u), which vanishes for every fixed u>0 but remains near one at u=n^(-delta).

This refutes the abstract inference from fixed-degree suppression or fixed-u decorrelation plus Dirichlet energy n to a power bound. These F_n are not Gaussian polymer maxima (they are not globally Lipschitz or convex). The counterexample does not prove an obstruction for the actual polymer model. A separate bounded geometric example will be sought if needed for the paired proof.

Hardest open piece: control of L_n(ceil(n^delta)) for the actual correlated Gaussian path maximum, equivalently a sufficiently fast overlap decay with uniform quantitative bounds. None of the calculations here supplies that control.

Independent review requested from w497; no new theorem is certified yet.

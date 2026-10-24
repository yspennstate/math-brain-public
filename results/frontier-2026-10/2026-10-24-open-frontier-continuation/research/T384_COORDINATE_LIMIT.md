# T384: training on finitely many coordinate inputs

**Scope:** fixed `k=d`, standard coordinate inputs `x_j=e_j` in the iid stable coordinate basis, one hidden layer, both layers trained, continuous squared-loss gradient flow, explicit absorption at ReLU zero gates, and `0<alpha<2`. This is not a theorem for arbitrary orthogonal inputs: iid non-Gaussian stable coordinates are not rotation invariant.

The two component proofs are `T384_orthogonal_initialization.md` and `T384_orthogonal_dynamics.md`. The filenames retain their working names; their mathematical hypotheses are the coordinate inputs above. Separate reviews are in `../reviews/T384_orthogonal_probability_review.md` and `../reviews/T384_orthogonal_dynamics_review.md`.

## Statement and exact limiting law

Initialize all `W_i,U_ij` independently with characteristic function `exp(-|z|^alpha)` and use

`f_j,m(t)=(m log m)^(-1/alpha) sum_i W_i(t)(U_ij(t))_+`,

learning rate `(log m)^(2/alpha)`, and loss `sum_j(y_j-f_j,m)^2/2`, for any fixed label vector y. Put `b=alpha/2`, `c=Gamma(alpha)sin(pi alpha/2)/pi`, and `g=Gamma(1-b)`.

Construct mutually independent primitive random objects:

- F_1,...,F_k iid symmetric alpha-stable, `E exp(it F_j)=exp(-c|t|^alpha)`;
- C_1,...,C_k iid positive b-stable, `E exp(-s C_j)=exp(-c g s^b)`;
- a Poisson random measure N on `(R\{0}) x R^k` with intensity `alpha c |z|^(-1-alpha) dz product_j Law(U)(du_j)` on both signs of z.

Let `sigma_j=sgn(y_j-F_j)` and define

`Q_j=C_j+int z^2 1{u_j>0,sgn(z)=sigma_j} N(dz,du)`.

The integrals are finite almost surely. For each fixed T, the output vector converges in `C([0,T];R^k)` to

`f_j(t)=y_j-(y_j-F_j)exp(-Q_j t)`, `j=1,...,k`.

For each `delta>0`, the full rate-scaled kernel converges on `[delta,T]` to the constant diagonal matrix `diag(Q_1,...,Q_k)` in the J1 topology; more precisely, its uniform distance from the corresponding width-dependent diagonal rate tends to zero in probability. At initialization its limit is diagonal with entries

`C_j+int z^2 1{u_j>0}N(dz,du)`.

The removed mass in coordinate j is the integral over the opposing sign of z, and is positive almost surely. Record the initial and positive-time kernels separately; an instantaneous drop at zero cannot be represented by a right-continuous macroscopic-time kernel having both values.

## The rate vector is not independent of the initialization vector

Conditional on F, let `B_j` be independent Bernoulli(1/2). For nonnegative lambda_j,

`E[exp(-sum_j lambda_j Q_j)|F]`

`=exp{-c g [sum_j lambda_j^b`

`  + E_B(sum_{j:sigma_j=+1}lambda_j B_j)^b`

`  + E_B(sum_{j:sigma_j=-1}lambda_j B_j)^b]}`.

Each marginal Q_j has Laplace transform `exp[-(3c/2)g lambda^b]` and is independent of the entire F vector. But the joint rate-vector law depends on the partition of residual signs. For example, two coordinates with opposite signs use disjoint Poisson half-axes; with equal signs they can share atoms. Consequently F and Q are generally dependent as vectors. Replacing Q by independent coordinate rates would give a different joint training law.

## Why the scalar argument extends in this geometry

The first-layer kernel is exactly diagonal because gradients with respect to distinct hidden coordinates have disjoint support. The second-layer kernel freezes by a global normalized-energy bound. Its initial off-diagonal entry is a normalized sum of independent-coordinate products. Choosing `alpha/2<p<min(alpha,1)` gives

`P(m^(-2/alpha)sum_i U_ij+ U_il+ >epsilon) <= const m^(1-2p/alpha) ->0`, `j!=l`.

Thus the off-diagonal forcing on each residual is negligible. Variation of constants preserves each initially nonzero residual sign on a fixed interval after localization. All extreme output weights keep their initial signs because their normalized motion is small. Supporting active coordinates survive; an opposing extreme surviving to positive time would require an independent hidden coordinate of order `(log m)^(1/alpha)`, an event eliminated by the same tail argument as in the scalar proof. Small output weights contribute vanishing normalized kernel mass. Near-zero initial residual coordinates are handled directly by the small forcing bound, not by assuming uniform sign separation everywhere.

The joint initialization proof separately removes potential dependence from the shared W_i in the products W_i U_ij+. Its critical bound is `m P(two different normalized product jumps exceed fixed cutoffs)=O(1/log m)`. The output limits are independent, while common endpoint W extremes remain as the shared marked Poisson process in the rate vector.

## What remains open

General orthogonal rotations, nonorthogonal inputs, deep networks, discrete learning-rate limits and smooth-activation analogues are not covered. In particular the coordinate argument cannot be transferred by rotating iid stable coordinates. The assembled theorem is internally reviewed mathematical work; external priority and expert review remain unverified, and the full T384 catalog row must remain open.

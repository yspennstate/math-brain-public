# First-stage returns for `k` orthonormal inputs: generic transversality

## Deterministic measure-zero lemma

Let `k>=2`, fix a symmetric positive-definite `k x k` matrix `Q`, and put

`E(t)=exp(-Qt)`, `G(t)=Q^(-1)(I-E(t))=int_0^t exp(-Qs)ds`,

`r(t)=E(t)r0`, `J(t)=G(t)r0` for `t>=0`.

For every coordinate `j`, the set

`D_j(Q)={r0 in R^k: there exists t>0 with J_j(t)=r_j(t)=0}`       (1)

has `k`-dimensional Lebesgue measure zero. For any distinct `j,l`, so does

`D_jl(Q)={r0: there exists t>0 with J_j(t)=J_l(t)=0}`.       (2)

These conclusions hold for **each fixed** positive-definite `Q`; no genericity assumption on its entries or eigenvalues is needed. In particular, an absolutely continuous `r0` almost surely has no positive-time grazing return and no simultaneous returns of two coordinates during this constant-`Q` phase.

**Spectral rank of the grazing constraints.** Define the two row vectors

`a_j(t)=e_j^T G(t)`, `b_j(t)=e_j^T E(t)`.

Let `Pi_lambda` be the orthogonal projector onto the eigenspace of a distinct eigenvalue `lambda>0`, and write `u_lambda=Pi_lambda e_j`. By symmetry,

`a_j(t)=sum_lambda [(1-exp(-lambda t))/lambda]u_lambda^T`,

`b_j(t)=sum_lambda exp(-lambda t)u_lambda^T`.       (3)

The nonzero `u_lambda` are mutually orthogonal. If the two rows were proportional at some `t>0`, their coefficient ratio would have to be the same for every active eigenvalue:

`[(1-exp(-lambda t))/lambda]/exp(-lambda t)=(exp(lambda t)-1)/lambda`

`=int_0^t exp(lambda s)ds =: g_lambda(t)`.       (4)

For each `t>0`, `g_lambda(t)` is *strictly increasing* in `lambda`, since its derivative is `int_0^t s exp(lambda s)ds>0`. Thus `a_j(t),b_j(t)` are linearly independent for **every** positive time unless `e_j` has a projection on only one distinct eigenspace. In that exceptional case `Qe_j=lambda e_j`; the coordinate is an isolated eigenvector, and

`J_j(t)=[(1-exp(-lambda t))/lambda]r0_j`, `r_j(t)=exp(-lambda t)r0_j`.

Then (1) is exactly the hyperplane `{r0_j=0}`. This also covers repeated eigenvalues: what matters is the number of *distinct eigenvalues active in* `e_j`, not the multiplicity of an eigenspace.

**Union over the continuum of times.** In the rank-two case, form the smooth `2 x k` matrix `M_j(t)` with rows `a_j(t),b_j(t)`. At every `t>0` some `2 x 2` column minor is nonzero. On a neighborhood where one such minor stays nonzero, solve `M_j(t)r0=0` for those two coordinates of `r0` in terms of `t` and the remaining `k-2` free coordinates. This parametrizes all solutions there by a `C^1` map from an open subset of `R^(k-1)` to `R^k`. Countably many neighborhoods cover `(0,infinity)`; exhausting each free-coordinate domain by compact boxes gives countably many locally Lipschitz images of dimension at most `k-1`, hence Lebesgue-null images in `R^k`. This proves (1). The eigenvector case was handled directly. The argument also works for `k=2`, where each local solution set is a curve.

For (2), `G(t)` is positive definite for every `t>0`, with eigenvalues `(1-exp(-lambda t))/lambda>0`. Its distinct rows `e_j^TG(t)` and `e_l^TG(t)` are therefore independent. Apply exactly the same rank-two/one-parameter argument. A finite union over coordinates and coordinate pairs remains null.

## Sign-dependent random first-stage matrix

The stochastic initialization requires a small conditioning step. Suppose `r0=y-F` has a Lebesgue density and is independent of a random environment `E`, from which one defines a positive-definite matrix `Q_sigma(E)` for each sign vector `sigma in {+,-}^k`. The actual first-stage matrix is `Q=Q_sgn(r0)(E)`. For every realized environment and each *fixed* orthant `O_sigma`, `Q_sigma` is fixed. Hence

`Pr(r0 in O_sigma intersect D_j(Q_sigma) | E)=0`, and similarly for `D_jl`,

because the conditional law of `r0` is absolutely continuous. Summing over finitely many orthants proves the almost-sure assertions even though the *selected* `Q` depends on `r0` through its signs. Equivalently, conditional on `(E,sigma)`, the residual has a density restricted to `O_sigma`; it is not necessary, and generally incorrect, to claim unconditional independence of `r0` and the selected `Q`.

For the stable-network initialization, `E` consists of the frozen second-layer matrix and the output-weight endpoint process; the earlier joint-initialization result makes `F` independent of `E`. The selected masses `P_j(sigma)` then give `Q_sigma=C+diag(P_1(sigma),...,P_k(sigma))`. The argument applies whenever that joint initialization and full-dimensional density are available. In the proposed finite-coordinate ray extension, the ray vectors `h_ell^±=(±(x_{1,ell},...,x_{k,ell}))_+` span `R^k`: their differences are the coordinate rows of the rank-`k` orthonormal input matrix. Therefore the putative stable `F=sum h_ell^± Z_ell^±` has an integrable characteristic function bounded by `exp(-c'||t||^alpha)` and hence a density; the positive-stable ray Gram matrix is positive definite almost surely. These observations do not replace a full joint-initialization proof for `k>=3`.

On the probability-one event above, every coordinate with `r0_j!=0` has `sigma_j J_j(t)>0` for sufficiently small positive `t`, and every positive zero of `J_j` is simple (`r_j(t)!=0`). Such zeros are isolated. If a first positive return among all coordinates exists, it is attained at one coordinate only and is transversal in the absorbing direction: for its index `j_*`, `sigma_j* r_j*(tau)<0`, because `sigma_j* J_j*` was positive before its first zero. On each fixed finite horizon there are only finitely many first-stage zeros: `J_j` is analytic, its zero at the origin is simple, and it cannot accumulate in a compact interval. Thus the first switching coordinate and time are locally stable under perturbations that keep that switch inside a compact time interval. The exceptional eigenvector case cannot return at all when `r0_j!=0`.

## What this extends, and what it does not

This proves **generic first-stage transversality and absence of simultaneous first-stage returns for every finite `k`**, conditional on the stated joint initialization. It removes the particular “first candidate touches zero without crossing” obstruction to identifying the first macroscopic gate loss. It does not establish a global `k>=3` training limit: after one population is absorbed, the residual and cumulative integrals follow a new matrix and may experience further returns. The two-dimensional mixed-sign invariant cone used in `TWO_INPUT_LIMIT.md` no longer forbids additional switches.

There is a useful exact identity at a switch. During a constant phase, `r0-r(t)=Q J(t)`. If the matrix changes from `Q` to `Q'=Q-P_j e_j e_j^T` when `J_j(tau)=0`, then `Q'J(tau)=QJ(tau)`; thus the same relation `r0-r(t)=Q'J(t)` holds throughout the next constant phase. In particular, if that next phase were continued forever, its integrated limit would be `Q'^(-1)r0`. This identity makes subsequent switches possible rather than ruling them out.

For an explicit **deterministic matrix illustration**, without a claim that this exact `C` belongs to a particular stable-network Gram support, take `k=3`, `C=I+11^T`, `P=(1/2,1/2,1/2)`, `r0=(1,6/5,10)`, so `Q0=(3/2)I+11^T` is positive definite with positive off-diagonal entries. Set `mu=(r01+r02+r03)/3=61/15`. In its first phase,

`J_j(t)=(2mu/9)(1-exp(-9t/2))+(2/3)(r0_j-mu)(1-exp(-3t/2))`.

Both `J_1(infinity)` and `J_2(infinity)` are negative, while `J_l(t)-J_1(t)=(2/3)(r0_l-r01)(1-exp(-3t/2))>0` for `l=2,3` and `t>0`. Therefore `J_1` returns first, at `tau≈0.21003179`, with `J_2(tau)>0`. Remove `P_1` there. The new matrix `Q1=Q0-(1/2)e_1e_1^T` has `(Q1^(-1)r0)_2=-67/75<0`, so `J_2` subsequently returns, numerically at `t≈0.26876740`, with `r_2≈-0.70164`. These values were executed using `code/d04_three_input_demo.py`; its raw stdout is `outputs/d04_three_input_demo.txt`. The first-stage lemma controls the first return but says nothing about the later-phase grazing or collision exceptional sets. Proving that those are null requires a new analysis of the switch-time-dependent row constraints (and of the conditional state after previous switches), not merely another application of the fixed-`Q` lemma.

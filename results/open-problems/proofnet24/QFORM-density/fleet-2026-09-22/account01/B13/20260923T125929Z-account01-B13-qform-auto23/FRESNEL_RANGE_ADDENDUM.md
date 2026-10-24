# Addendum: rigorous Fresnel regularization and range-form compiler

This addendum belongs to account01/B13 run `20260923T125929Z-account01-B13-qform-auto23`. It supplies the regularization needed for the oscillatory Fresnel identities in `REPORT.md` and strengthens Theorem 5.1 to an invariant range-form statement.

Status: proved supporting theorem; full QFORM remains OPEN.

## A. Rigorous Fresnel pairing lemma

Let `L` be an invertible real symmetric `d x d` matrix, `t!=0`, and let `mu` be a finite complex Borel measure on `R^d`. Define

`H(xi)=int exp(i xi dot y) mu(dy)`.

Assume `H in L1(R^d)`. Then

`| int exp(i t y^T L y) mu(dy) |
 <= (4 pi |t|)^(-d/2) |det L|^(-1/2) int |H(xi)| dxi`.            (A.1)

### Proof

For `eps>0` put

`Phi_eps(y)=exp(i t y^T L y-eps |y|^2)`.

Using the Fourier convention

`hat Phi(xi)=int exp(-i xi dot y) Phi(y) dy`,
`Phi(y)=(2pi)^(-d) int exp(i xi dot y) hat Phi(xi) dxi`,

the complex Gaussian formula gives

`hat Phi_eps(xi)
 = pi^(d/2) det(eps I-i t L)^(-1/2)
   exp[-(1/4) xi^T(eps I-i t L)^(-1)xi]`,                         (A.2)

with the continuous square-root branch; only its modulus matters. Since `L` is real symmetric,

`Re (eps I-i t L)^(-1) >=0`,                                     (A.3)

and

`|det(eps I-i t L)|^(1/2)
 = prod_r (eps^2+t^2 lambda_r^2)^(1/4)
 >= |t|^(d/2)|det L|^(1/2)`.                                     (A.4)

Hence, uniformly in `eps>0` and `xi`,

`(2pi)^(-d)|hat Phi_eps(xi)|
 <= (4 pi |t|)^(-d/2)|det L|^(-1/2)`.                             (A.5)

Fourier inversion for the Schwartz function `Phi_eps`, followed by Fubini against the finite measure `mu`, gives

`int Phi_eps(y) mu(dy)
 =(2pi)^(-d) int hat Phi_eps(xi) H(xi) dxi`.                       (A.6)

Taking absolute values and using (A.5) gives the right side of (A.1), uniformly in `eps`. On the left, `Phi_eps(y)->exp(i t y^T L y)` and `|Phi_eps|<=1`; dominated convergence with respect to the total variation of `mu` finishes the proof. QED.

Thus every Fresnel use in `REPORT.md` can be read through (A.1). The relevant Fourier transform is proved `L1` by the geometric Brascamp--Lieb estimate before `eps` is sent to zero. No conditionally convergent Fubini interchange is required.

## B. Arbitrary invertible curvature on an augmented leaf range

The block-diagonal matrix `diag(K,Lambda)` in Theorem 5.1 is unnecessary.

Let `U=(U_1,...,U_r)` and `V=(V_1,...,V_m)` be disjoint banks of original coordinates, all independent, with scalar probability densities bounded by one. Let `Z` be any other independent coordinates. Let `R` be a real symmetric `m x m` matrix of rank `d>=3`. Suppose the physical cross matrix `B` from `U` to `V` satisfies

`row(B) subset range(R)`.                                         (B.1)

Let `P_R` denote the orthogonal projection onto `range(R)` and assume the coordinate leverage bound

`max_j (P_R)_{jj} <=1/2`.                                         (B.2)

Consider

`Q = F(U,Z)
     + sum_j [d_j V_j^2+c_j(Z)V_j]
     +2 U^T B V
     +V^T R V`,                                                    (B.3)

with arbitrary measurable `F`, arbitrary real diagonal twists `d_j`, and arbitrary affine coefficients `c_j(Z)`.

### Theorem B.1 — `QFORM-RANGE-CURVATURE-FRESNEL-BL-v1`

Under (B.1)--(B.3), `Q` has a continuous density and

`boxed:
 ||p_Q||_inf
 <= [4d/(d-2)] |pdet(R)|^(-1/d).
`                                                                      (B.4)

Here `pdet(R)` is the product of the nonzero eigenvalues; only its absolute value is used.

### Proof

Choose any full-row-rank `d x m` matrix `A` whose row space is `range(R)`. Since `R` is symmetric, vanishes on `range(R)^perp`, and is nondegenerate on its own range, there is an invertible symmetric `d x d` matrix `L` with

`R=A^T L A`.                                                       (B.5)

By (B.1) there is an `r x d` deterministic matrix `J` such that

`B=J A`.                                                          (B.6)

Put `G=AA^T`, let `a_j` be the columns of `A`, and define

`ell_j=a_j^T G^(-1)a_j`.                                          (B.7)

These are exactly the coordinate projection leverages `(P_R)_{jj}`, so `ell_j<=1/2`; moreover

`sum_j ell_j=d` and, after `v_j=G^(-1/2)a_j/sqrt(ell_j)`,
`sum_j ell_j v_j v_j^T=I_d`.                                     (B.8)

Fix `Z=z`. Absorb all phases not involving the selected leaf quadratic form into a finite complex measure `mu_t` on

`y=A V in R^d`.

Its Fourier transform has, after integrating the independent leaves,

`H_t(xi)
 = int f_U(u) exp(i phase(u))
     prod_j g_{j,t}(a_j dot (xi+2t J^T u)+t c_j(z)) du`,           (B.9)

where

`g_{j,t}(tau)=int exp(i t d_j v^2+i tau v) f_{V_j}(v) dv`.         (B.10)

Translate `s=xi+2t J^T u`. For each fixed `u`, `dxi=ds`, so the product loses every `u` dependence. Since `int f_U=1`,

`int |H_t(xi)| dxi
 <= int_Rd prod_j |g_{j,t}(a_j dot s+t c_j(z))| ds`.               (B.11)

Normalize `s` by `G^(1/2)`. With

`F_j(q)=|g_{j,t}(sqrt(ell_j)q+t c_j(z))|^(1/ell_j)`,               (B.12)

the completed twisted one-dimensional estimate

`int |g(s,tau)|^p d tau <=4pi/sqrt(p), p>=2`,                     (B.13)

and `p=1/ell_j>=2` give

`int F_j(q)dq <=4pi`.                                              (B.14)

Geometric Brascamp--Lieb using (B.8) yields

`int |H_t(xi)|dxi
 <= det(G)^(-1/2)(4pi)^d`.                                        (B.15)

Apply Lemma A.1 to `mu_t` and the quadratic phase `y^T L y`:

`|phi_Q(t)|
 <= (4pi|t|)^(-d/2)|det L|^(-1/2)
     det(G)^(-1/2)(4pi)^d
 = (4pi)^(d/2)
   [|det L|det G]^(-1/2)|t|^(-d/2).`                              (B.16)

The nonzero eigenvalues of `A^T L A` are the nonzero eigenvalues of `L AA^T`; hence

`|pdet(R)|=|det L|det G`.                                         (B.17)

Together with `|phi_Q(t)|<=1`, and `alpha=d/2>1`,

`int_R min(1,K|t|^-alpha)dt
 =2 alpha/(alpha-1) K^(1/alpha)`.                                 (B.18)

Fourier inversion gives

`||p_Q||_inf
 <= alpha/[pi(alpha-1)]
    [(4pi)^(d/2)|pdet(R)|^-1/2]^(2/d)
 =4d/(d-2)|pdet(R)|^-1/d`,                                        (B.19)

and `phi_Q in L1` gives a continuous representative. QED.

## C. Relation to the Nystrom Schur chamber

For an invertible physical two-hub block `H0`, the selected hub/leaf quadratic form is

`u^T H0 u+2u^T Bv+v^T C v`,                                      (C.1)

with Schur remainder

`T=C-B^T H0^(-1)B`.                                               (C.2)

Suppose, for some diagonal `D0`,

`R=C-D0=B^T H0^(-1)B+(T-D0)`                                     (C.3)

has rank `d>=3`, its range contains `row(B)`, and its range projection has maximum coordinate leverage at most `1/2`. Then Theorem B.1 applies directly and gives

`boxed:
 ||p_Q||_inf <=[4d/(d-2)] |pdet(C-D0)|^(-1/d).
`                                                                      (C.4)

This strictly strengthens the block-diagonal low-rank formula in `REPORT.md`: arbitrary cross-coupling between the Nystrom two-plane and the transverse low-rank Schur directions is allowed. Only the actual range, its coordinate leverage, and the nonzero determinant currency remain.

If `T-D0` has rank `k` and the sum in (C.3) has the maximal possible rank `d=k+2`, then its range automatically equals

`row(B)+range(T-D0)`,                                              (C.5)

so the required inclusion of `row(B)` is automatic. Thus every exact diagonal-plus-rank-`k` Schur remainder whose Nystrom sum has rank `k+2>=3` is paid whenever the resulting `(k+2)`-dimensional range is coordinate-diffuse.

The constant is at most `12` for every `d>=3` and decreases to `4` as `d` grows.

## D. High-leverage exact volume star

For any `d`-dimensional subspace `S=range(R)`, choose an orthonormal-row matrix `A` spanning `S`. Then `AA^T=I_d`, `ell_j=(P_S)_{jj}`, and Cauchy--Binet gives

`1=det(AA^T)=sum_{|I|=d} det(A[:,I])^2`.                           (D.1)

For each physical coordinate `j`, deletion plus the matrix determinant lemma yields

`sum_{|I|=d, j in I} det(A[:,I])^2=ell_j`.                        (D.2)

Therefore failure of the diffuse gate has the exact consequence

`max_j ell_j>1/2
 => exists j_* with
    sum_{I contains j_*} det(A[:,I])^2>1/2`.                       (D.3)

So the complement of Theorem B.1 is again a single **physical coordinate volume star**, now for the complete augmented curvature range. This is the invariant form of the two-way `beta/tau` star split recorded in `REPORT.md`.

The designated account02/B13 identity is still applied nontrivially in the two-hub component: if its hub leverage `beta_(j_*)>1/4`, then

`sum_{s!=j_*} det(b_(j_*),b_s)^2
 > (1/4) det(BB^T)`,                                               (D.4)

so the same original coordinate carries a quantitative physical two-hub determinant star.

## E. Remaining gap

The newest account02/B13 Schur-crosscut theorem supplies, in the invertible-hub high-density chamber, a strong physical cross cut of the Schur remainder with `s1>=1/4`, `s7=O(rho^-1)`, and either `s5=O(rho^-1)` or a physical third-volume row/column bi-hub. Theorem B.1 now closes the corresponding **exact global low-rank range** endpoint whenever that residual can be upgraded to a diagonal-plus-finite-rank global representation with diffuse range.

What is still unpaid is the passage from cutwise approximate low rank plus max-norm-small global residual to such an exact global range statement, without deleting the residual. The alternative high-leverage state is localized by (D.3)/(D.4) to one physical coordinate. This is `QFORM-CUTWISE-LOWRANK-TO-RANGE-OR-STAR-CLOSURE-v1`.

No pointwise law-uniform quadratic oscillatory decay, post-rotation independence, arbitrary-joint coarea, conditional projection cap, fixed fragment count, or perturbative deletion of a max-norm-small matrix is used.

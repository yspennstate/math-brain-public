# T384: orthogonal fixed inputs, joint initialization, and the effective clock

Fix an integer `k=d>=1`, inputs `x_j=e_j`, and `0<alpha<2`. For each `i`, let `W_i,U_{i1},...,U_{ik}` be mutually independent standard symmetric `alpha`-stable variables, with characteristic function `exp(-|t|^alpha)`; all rows are iid. Write

`c=c_alpha=Gamma(alpha)sin(pi alpha/2)/pi`, `beta=alpha/2`, `a_m=m^(1/alpha)`, `b_m=(m log m)^(1/alpha)`, `d_m=m^(2/alpha)`.

For `j=1,...,k`, set

`F_{j,m}=b_m^(-1) sum_i W_i (U_{ij})_+`, `C_{j,m}=d_m^(-1) sum_i (U_{ij})_+^2`,

and `N_m=sum_i delta_(W_i/a_m, (U_{i1},...,U_{ik}))` on `E=(R\{0})xR^k`.

**Joint theorem.** In the vague point-process topology on `E`, jointly with the `2k` real coordinates,

`(N_m,(F_{j,m})_{j<=k},(C_{j,m})_{j<=k}) => (N,(F_j)_{j<=k},(C_j)_{j<=k})`.  (1)

The limit `N` is a Poisson random measure with intensity

`mu(dz,du_1...du_k)=alpha c |z|^(-1-alpha) dz product_{j=1}^k P_U(du_j)`

on **each** half-axis in `z`. The `2k+1` limit objects `N,F_1,...,F_k,C_1,...,C_k` are mutually independent. In particular, the `F_j` are iid with characteristic function `exp(-c|t|^alpha)`, while the `C_j` are iid positive `beta`-stable with Laplace transform `exp[-c Gamma(1-beta)s^beta]`. Standard stable one-sided tails obey `P(U>x)~c x^(-alpha)`, and the same for `W` and their negatives. Thus the use of the same `W_i` in every coordinate does **not** persist as dependence among the product-initialization limits.

## The axis-separation proof

The iid Laplace-functional proof of the marginal `N_m=>N` uses `mP(W/a_m in dz)=>alpha c|z|^(-1-alpha)dz` vaguely away from zero and independence of the vector mark `U_i` from `W_i`. The mark law is the `k`-fold product distribution. For a test function with `|z|>=eta`, marks beyond `max_j|u_j|>L` have expected count at most `C eta^(-alpha) P(max_j|U_j|>L)` for large m, so compact-mark approximation is legitimate.

For `X_j=W(U_j)_+`, the two one-sided product tails are

`P(X_j>t)=P(X_j<-t) ~ alpha c^2 t^(-alpha) log t`.  (2)

One direct derivation integrates `P(W>t/u)` against the positive-U distribution and uses `E[U_+^alpha 1_{U_+<=t}]~alpha c log t`; endpoint ranges contribute lower-order terms after first restricting `u` to `[t^h,t^(1-h)]` and then taking `h->0`. Consequently, for fixed `x>0`,

`mP(X_j/b_m>x)->c^2 x^(-alpha)`, `mP(X_j/b_m< -x)->c^2 x^(-alpha)`,  (3)

and `mP((U_j)_+^2/d_m>x)->c x^(-beta)`. The corresponding Lévy measures are `alpha c^2|x|^(-1-alpha)dx` on each signed half-axis and `beta c x^(-1-beta)dx` on the positive half-axis, respectively.

Fix positive jump cutoffs `epsilon,delta` and restrict each `F_{j,m}` to `|X_{ij}|>epsilon b_m`, each `C_{j,m}` to `(U_{ij})_+^2>delta d_m`. Also fix a compactly supported test function of `N_m` whose support has `|z|>=eta`. **Any two retained categories arise from distinct sample rows with asymptotic probability one.** More precisely, after multiplication by `m`, each pairwise one-row overlap probability tends to zero:

* `N/F_j`: Split `|W|>eta a_m` at `L a_m`. The first part `|W|>L a_m` has `limsup mP<=2cL^(-alpha)`; on `|W|<=L a_m`, a product jump requires `(U_j)_+>(epsilon/L)(log m)^(1/alpha)`. Send `m->infinity`, then `L->infinity`.
* `N/C_j`: Independence gives `mP(|W|>eta a_m,(U_j)_+>sqrt(delta)a_m)=O(m^(-1))`.
* `F_j/C_j`: Split `(U_j)_+>sqrt(delta)a_m` at `L a_m`. The upper part has `limsup mP<=cL^(-alpha)`; below `L a_m`, a product jump requires `|W|>(epsilon/L)(log m)^(1/alpha)`, whose probability vanishes. For `j!=ell`, `F_j` and `C_ell` depend on independent `U_j,U_ell` after grouping `(W,U_j)` against `U_ell`, so the overlap is `O(m^(-1))`.
* `C_j/C_ell`, `j!=ell`: The independent U endpoints give overlap `O(m^(-1))`.
* `F_j/F_ell`, `j!=ell`: This is the important shared-W case. Conditionally on `W=w`, the two U variables are independent and each product-jump probability is at most `K min(1,(|w|/b_m)^alpha)`. Hence

  `mP(|X_j|>epsilon b_m,|X_ell|>epsilon b_m)`

  `<= K m E[min(1,(|W|/b_m)^alpha)^2]`

  `<= K m {b_m^(-2alpha) E[|W|^(2alpha)1_{|W|<=b_m}]+P(|W|>b_m)}`

  `=O(m/b_m^alpha)=O(1/log m)`.  (4)

Here `E[|W|^(2alpha)1_{|W|<=b}]<=K b^alpha` follows by integrating the stable tail. All bounds hold for each fixed pair of positive cutoffs; constants may depend on those cutoffs and on k.

Expand a one-row mixed Laplace/Fourier transform as a product of the endpoint test factor and the `2k` retained jump factors. Each mixed term contains at least two nonzero factors and is bounded by a constant times one of the preceding pairwise overlap probabilities. Thus, multiplied by `m`, the mixed terms vanish. The surviving `2k+1` axis terms converge via (3) and regular variation; raising the one-row transform to its mth power gives the **product** of the marked-PPP Laplace functional and `2k` compound-Poisson transforms. This proves the joint independence at fixed cutoffs.

Cutoff removal is uniform in m in the necessary sense. Symmetry of W gives `E[X_j 1_{|X_j|<=epsilon b_m}]=0`, and independence between rows, together with `P(|X_j|>t)<=K t^(-alpha)(1+log t)` for large t, gives

`limsup_m E[(F_{j,m}-F_{j,m}^{(epsilon)})^2]<=K epsilon^(2-alpha)`.  (5)

Likewise the positive jumps satisfy

`sup_{m sufficiently large} E[C_{j,m}-C_{j,m}^{(delta)}]<=K delta^(1-beta)`.  (6)

For fixed k, sum the Chebyshev/Markov error bounds and then let `epsilon,delta` decrease to zero. The symmetric Lévy measure in (3) has exponent `c|t|^alpha`, because a standard symmetric alpha-stable law has one-sided tail constant c. The positive beta-stable Lévy measure gives exponent `c Gamma(1-beta)s^beta`. This proves (1), including mutual independence, with no centering term at any alpha.

## Conditional law of the effective Q vector

Let deterministic `y_1,...,y_k` be fixed and set `sigma_j=sgn(y_j-F_j)`; the value at zero is immaterial because `F_j` has a continuous law. Define

`Q_j=C_j+int_E z^2 1_{u_j>0, sgn(z)=sigma_j} N(dz,du)`.  (7)

The integral is finite almost surely. For `|z|<=epsilon`, its expectation is at most `2alpha c epsilon^(2-alpha)/(2-alpha)`; an atom with `|z|>R` occurs with probability at most `2cR^(-alpha)`. These bounds also hold simultaneously for finitely many coordinates, with a factor k. The analogous finite-m small-z bound is `m a_m^(-2) E[W^2 1_{|W|<=epsilon a_m}]<=K epsilon^(2-alpha)`. Alongside product-mark tail truncation, these bounds justify truncation of (7). The boundaries `u_j=0`, `F_j=y_j`, and the annulus cutoffs have zero limit probability; hence (1) also implies joint convergence of the analogous effective-Q construction using `N_m,F_m,C_m`.

Condition on the complete F vector. Let `B_1,...,B_k` be independent Bernoulli(1/2), representing the positive signs of the independent U marks of a single atom. For nonnegative `lambda_1,...,lambda_k`, the exponential formula for N and the independence of C give

`E[exp(-sum_j lambda_j Q_j) | F]`

`=exp{-c Gamma(1-beta) [sum_j lambda_j^beta`

`    + E_B (sum_{j:sigma_j=+1} lambda_j B_j)^beta`

`    + E_B (sum_{j:sigma_j=-1} lambda_j B_j)^beta]}`.  (8)

Indeed, on the positive or negative z half-axis set `x=z^2`. Its Lévy intensity becomes `beta c x^(-1-beta)dx`. For a fixed sign group, integrate `1-exp(-x sum lambda_j B_j)` over x to obtain `c Gamma(1-beta)(sum lambda_j B_j)^beta`, then average over B. The C part contributes `c Gamma(1-beta)sum lambda_j^beta` independently.

**Dependence warning.** For `k=1`, (8) is `exp[-(3/2)c Gamma(1-beta)lambda^beta]`, independent of `sigma_1`; the scalar Q is therefore independent of its F. For `k>=2`, the conditional joint Q law generally changes with the relative signs of `y_j-F_j`. Equal signs share Poisson atoms, while opposite signs use independent z half-axes. Thus the Q vector is generally **not** independent of the F vector, even though the primitive limits `N`, all `F_j`, and all `C_j` are mutually independent.

This note addresses the **initialization and effective-Q distribution**. A dynamical derivation that identifies the actual time-dependent first-layer weights or a joint path-space limit is a separate step.

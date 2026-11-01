# P0151 analytic artifact — log-age Doob transform and killed-PPT spectral window

This is a self-derived analytic artifact for `HARD7-04`. It proves a spectral statement for the **Pólya-point-tree mean-offspring operator**, not a critical-window theorem for the finite fixed-outdegree preferential-attachment graph. It does not close the source problem and has not received the independent audits required for closure.

## Proposition

Fix integer `m>=2` and `delta>0`. Put

`a:=m+delta`, `A:=2m+delta`, `chi:=a/A`, `alpha:=chi-1/2=delta/(2A)`.

For the two Pólya-point-tree types `O,Y`, write Ray's mean-offspring matrix constants as

`c:=c_OO=c_YY=m*a/A`,
`d:=c_OY=m*(a+1)/A`,
`e:=c_YO=(m-1)*a/A`,
`g:=sqrt(d*e)`,
`lambda0:=c+g`.

The extended mean-offspring kernel on ages `x,y in (0,infinity)` is

`kappa((x,s),(y,t))
 = c_st * [1_{x>y,t=O}+1_{x<y,t=Y}]
   /[(x max y)^chi (x min y)^(1-chi)]`.

Its spectral radius is `lambda0/alpha`, hence the exact percolation threshold is

`pi_c=alpha/lambda0
     =delta/[2(m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)))]`.

Let `T_L` be this kernel restricted in both variables to the finite age interval

`e^{-L} <= x,y <= 1`.

Equivalently, `T_L` is the same restriction of the actual Pólya-point-tree operator on ages `(0,1]`; the use of the extended operator is only to expose the exact positive harmonic function before killing at the two interval boundaries.

Define

`q:=c/lambda0`, `p:=g/lambda0`, `rho:=q-p=(c-g)/(c+g)`.

Then `q+p=1`, `-1<rho<1`. Let

`R_L:=pi_c T_L`.

For all sufficiently large `L`, the Perron root `z_L:=r(R_L)` satisfies

`z_L
 = 1 - C_spec/L^2 + O(L^-3)`,                                    (P.1)

where

`C_spec := pi_math^2/[alpha^2(1-rho)]
         = (pi_math^2/2) sigma^2`,                                 (P.2)

and

`sigma^2 := 2/[alpha^2(1-rho)] = lambda0/(alpha^2 g)`.             (P.3)

Here `pi_math=3.14159...`, distinguished from the percolation parameter.

More precisely, `z_L` is the positive principal solution of

`omega_L^2 = alpha^2 (1-z_L)(z_L-rho)/z_L^2`,                     (P.4)

`cos(omega_L L)
 + [alpha(z_L-q)/(z_L omega_L)] sin(omega_L L)=0`,                 (P.5)

with `omega_L L in (pi_math/2,pi_math)`.

Consequently, for every fixed real `lambda`, if one perturbs the retention probability on the finite-age operator by

`pi_L(lambda):=pi_c(1+lambda/L^2)`,                               (P.6)

then

`r(pi_L(lambda) T_L)
 = 1 + [lambda-C_spec]/L^2 + O(L^-3)`.                            (P.7)

Thus the **local mean-operator spectral crossing** occurs on the scale `L^-2`. With the finite-graph age cutoff `L=log n`, this is exactly a `(log n)^(-2)` spectral scale. This is an auxiliary operator result only: no finite-graph exploration coupling, component-size theorem, or critical-window theorem is inferred from it.

---

## 1. Exact critical harmonic function on the extended operator

The `2x2` matrix

`M=[[c,d],[e,c]]`

has Perron eigenvalue `lambda0=c+sqrt(de)=c+g` and positive right eigenvector

`pvec=(sqrt(d),sqrt(e))`.

Indeed,

`d sqrt(e)=sqrt(d) sqrt(de)=g sqrt(d)`,
`e sqrt(d)=sqrt(e) sqrt(de)=g sqrt(e)`.

Therefore

`M pvec=lambda0 pvec`.

Set

`h_s(x):=pvec_s x^{-1/2}`.                                        (1.1)

For `t=O`, only `0<y<x` contributes. Since `chi>1/2`,

`int_0^x
 c_sO/[x^chi y^(1-chi)] * pvec_O y^-1/2 dy
 = c_sO pvec_O x^-chi int_0^x y^(chi-3/2)dy
 = [c_sO pvec_O/alpha] x^-1/2`.                                  (1.2)

For `t=Y`, only `y>x` contributes on the **extended** age space. Similarly,

`int_x^infinity
 c_sY/[y^chi x^(1-chi)] * pvec_Y y^-1/2 dy
 = c_sY pvec_Y x^(chi-1) int_x^infinity y^(-chi-1/2)dy
 = [c_sY pvec_Y/alpha] x^-1/2`.                                  (1.3)

Summing (1.2)--(1.3) and using `M pvec=lambda0 pvec` gives

`Tbar h=(lambda0/alpha) h`.                                       (1.4)

Thus at `pi=pi_c=alpha/lambda0`,

`pi_c Tbar h=h`.                                                    (1.5)

This is the exact extended-space eigenfunction underlying Ray's spectral-radius computation. Restricting to `x<=1` kills the part of the transformed process that exits through `x>1`; restricting further to `x>=e^-L` also kills exits through the small-age boundary.

---

## 2. B18 recoding: the critical operator is a centered two-state Markov additive process

Write log-age

`u:=-log x`, `v:=-log y`.

The extended age space becomes the full line `u in R`. Define the critical Doob transform by

`K((u,s),d(v,t))
 := pi_c kappa((e^-u,s),(e^-v,t))
    [h_t(e^-v)/h_s(e^-u)] e^-v dv`.                               (2.1)

### Positive jumps

If `t=O`, then `y<x`, equivalently `v>u`. Put `z=v-u>0`. Direct substitution gives

`K((u,s),d(u+z,O))
 = pi_c c_sO (pvec_O/pvec_s) e^-alpha*z dz`.                       (2.2)

### Negative jumps

If `t=Y`, then `y>x`, equivalently `v<u`. Put `z=v-u<0`. Then

`K((u,s),d(u+z,Y))
 = pi_c c_sY (pvec_Y/pvec_s) e^-alpha*|z| dz`.                     (2.3)

Since `pi_c/alpha=1/lambda0`, integration of (2.2)--(2.3) gives the type transition matrix

`Q_st = c_st pvec_t/(lambda0 pvec_s)`.

Using `pvec=(sqrt(d),sqrt(e))`, this simplifies exactly to

`Q=[[q,p],[p,q]]`,                                                 (2.4)

where `q=c/lambda0`, `p=g/lambda0`, `q+p=1`.

Conditional on the next type, the magnitude of the log-age jump is `Exp(alpha)` and is independent of the current type; its sign is `+` when the next type is `O` and `-` when the next type is `Y`.

The type chain (2.4) is symmetric, hence its stationary distribution is `(1/2,1/2)`. Therefore the stationary one-step log-age drift is exactly zero:

`E Delta u = (1/2)(1/alpha)+(1/2)(-1/alpha)=0`.                   (2.5)

So the critical mean operator is not merely analogous to a random walk: after the exact harmonic gauge it becomes a **centered two-state Markov additive process with exponential jumps**.

Let

`S_k=+1` on type `O`, `S_k=-1` on type `Y`,

and let `E_k` be the independent `Exp(alpha)` jump magnitude. Then the increment is

`X_k=S_k E_k`.

The nontrivial eigenvalue of `Q` is

`rho=q-p=(c-g)/(c+g)`.                                            (2.6)

In stationarity,

`E[S_0 S_j]=rho^j`,
`E E_k=1/alpha`,
`E E_k^2=2/alpha^2`.

Hence the asymptotic variance per step is

`sigma^2
 = 2/alpha^2 + 2 sum_{j>=1} rho^j/alpha^2
 = 2/[alpha^2(1-rho)]`.                                          (2.7)

This proves (P.3). Since `1-rho=2g/lambda0`, the equivalent form

`sigma^2=lambda0/(alpha^2 g)`

follows.

---

## 3. Fourier check: exact quadratic dispersion

For completeness, the Fourier matrix of the full-line Markov-additive kernel is

`Khat(xi)
 = Q diag(alpha/(alpha-i xi), alpha/(alpha+i xi))`.                (3.1)

Its trace and determinant are

`tr Khat(xi)
 = (1+rho) alpha^2/(alpha^2+xi^2)`,                               (3.2)

`det Khat(xi)
 = rho alpha^2/(alpha^2+xi^2)`.                                   (3.3)

Let `lambda_+(xi)` be the eigenvalue satisfying `lambda_+(0)=1`. Put `x=xi^2/alpha^2`. The characteristic equation and (3.2)--(3.3) give, by substituting `lambda_+(xi)=1-kx+O(x^2)`,

`k=1/(1-rho)`.

Thus

`lambda_+(xi)
 = 1 - xi^2/[alpha^2(1-rho)] + O(xi^4)
 = 1 - (sigma^2/2) xi^2 + O(xi^4)`.                              (3.4)

The linear term vanishes because the transformed process is exactly centered.

---

## 4. B7: solve the killed finite-log-age eigenproblem

The actual PPT ages satisfy `x<=1`, i.e. `u>=0`. Imposing the additional cutoff `x>=e^-L` restricts to

`0<=u<=L`.

Because multiplication by the positive function `h` is an invertible similarity on this compact interval, the spectrum of `R_L=pi_c T_L` is the spectrum of the Markov-additive kernel `K` killed upon exiting `[0,L]`.

Let `z` be an eigenvalue with positive eigenfunction `f=(f_O,f_Y)`. Define

`A(u):=int_u^L alpha e^-alpha(v-u) f_O(v) dv`,                     (4.1)

`B(u):=int_0^u alpha e^-alpha(u-v) f_Y(v) dv`.                     (4.2)

The eigenvalue equations are

`z f_O=q A+p B`,
`z f_Y=p A+q B`.                                                   (4.3)

Differentiating (4.1)--(4.2),

`A'=alpha A-alpha f_O`,
`B'=alpha f_Y-alpha B`.                                           (4.4)

Substitute (4.3):

`d/du [A;B]
 = alpha [[(z-q)/z,-p/z],[p/z,(q-z)/z]] [A;B]`.                   (4.5)

The matrix in (4.5) has trace zero. Its square is

`-omega^2 I`,

where

`omega^2
 = alpha^2 (1-z)(z-rho)/z^2`.                                   (4.6)

The boundary conditions inherited from (4.1)--(4.2) are

`B(0)=0`, `A(L)=0`.                                                (4.7)

Start with `A(0)=A0>0`, `B(0)=0`. Matrix exponentiation in (4.5) yields

`A(u)
 = A0[cos(omega u)
      + alpha(z-q)/(z omega) sin(omega u)]`,                       (4.8)

`B(u)
 = A0[alpha p/(z omega)] sin(omega u)`.                            (4.9)

The condition `A(L)=0` is exactly (P.5).

For the principal mode, choose the root with

`theta_L:=omega_L L in (pi_math/2,pi_math)`.                       (4.10)

Indeed, (P.5) is equivalent to

`tan(theta_L)
 = - z_L omega_L/[alpha(z_L-q)]`.                                 (4.11)

For the large-`L` root near `z=1`, the right side is negative and of order `L^-1`, so the first positive branch lies in `(pi_math/2,pi_math)`.

Positivity is explicit. From the boundary equation,

`alpha(z_L-q)/(z_L omega_L)=-cot(theta_L)`.

Therefore (4.8) becomes

`A(u)=A0 sin(theta_L-omega_L u)/sin(theta_L)>0`

for `0<=u<L`, while (4.9) is positive for `0<u<=L`. Then (4.3) gives `f_O,f_Y>0` in the interior. The killed kernel is a positive Hilbert--Schmidt kernel on a finite interval and is irreducible after two steps. Hence its unique positive eigenfunction corresponds to the Perron root. Thus the root described above is `z_L=r(R_L)`.

---

## 5. Large-L expansion and the `L^-2` constant

From (4.11), for the principal root,

`theta_L=pi_math+O(L^-1)`                                         (5.1)

with the approach from below. Consequently

`omega_L=pi_math/L+O(L^-2)`.                                      (5.2)

Equation (4.6) gives

`1-z_L
 = omega_L^2 z_L^2/[alpha^2(z_L-rho)]`.                       (5.3)

Because `omega_L=O(L^-1)`, (5.3) first implies `1-z_L=O(L^-2)`. Insert this back into (5.2)--(5.3):

`1-z_L
 = [pi_math^2/L^2+O(L^-3)]
   /[alpha^2(1-rho+O(L^-2))]`

`= pi_math^2/[alpha^2(1-rho)L^2] + O(L^-3)`.                      (5.4)

This is (P.1)--(P.2).

The coefficient can also be read from the full-line dispersion relation (3.4): the first killed mode has wave number `pi_math/L+O(L^-2)`, and its quadratic dispersion is `(sigma^2/2) xi^2`.

---

## 6. B5: near-critical percolation interpolation on the killed operator

Percolation multiplies the mean-offspring operator by the scalar retention parameter. Thus for fixed `lambda` and

`pi_L(lambda)=pi_c(1+lambda/L^2)`,

`r(pi_L(lambda)T_L)
 = (pi_L(lambda)/pi_c) z_L`.

Using (P.1),

`r(pi_L(lambda)T_L)
 = [1+lambda/L^2]
   [1-C_spec/L^2+O(L^-3)]`

`=1+[lambda-C_spec]/L^2+O(L^-3)`.                                 (6.1)

This proves (P.7). In particular the finite-log-age mean operator changes from subcritical to supercritical, to first order, at the explicit relative shift

`lambda=C_spec`.                                                    (6.2)

With `L=log n`, the operator calculation therefore singles out `(log n)^-2` as the natural local spectral scale.

---

## 7. Why this does not yet solve the finite-graph source problem

The calculation above is exact for the killed PPT mean operator, but the source asks for the **finite sequential fixed-outdegree preferential-attachment graph**. Three obligations remain unpaid:

1. **finite-graph exploration coupling:** couple component exploration in the fixed-`m` sequential graph, through the relevant size scale, to the killed two-type log-age process with an error `o(L^-2)` at the spectral level or a comparably sharp probabilistic replacement;
2. **dependency control:** the `m` outgoing edges of each arriving vertex are sequential and fixed in number, not independent Bernoulli connections to all earlier vertices; this is exactly why the 2025 independent-edge growing-graph critical-window theorem cannot simply be imported;
3. **nonlinear component control:** a near-critical mean-operator crossing alone does not prove the scale, tightness, or limiting law of the largest components.

The neighboring Jorritsma--Maillard--Mörters theorem for independently attached growing random graphs uses a branching-random-walk exploration killed outside an interval of length `log n` and obtains a `(log n)^-2` window. The calculation here identifies the same killed-centered-walk mechanism **inside the exact fixed-outdegree model's local limit**, but a new quantitative transfer theorem is still needed.

Therefore this artifact is **auxiliary progress / PARTIAL**, not source closure and not a claim that the finite fixed-outdegree window has already been proved.
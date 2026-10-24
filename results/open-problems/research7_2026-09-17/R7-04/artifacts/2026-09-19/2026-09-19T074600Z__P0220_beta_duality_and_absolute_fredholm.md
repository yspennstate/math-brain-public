# P0220 — terminal-parameter tilt, finite-row duality, and an absolute Fredholm-series boundary

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED**. The owner requested GPT-6 / maximum, but no authenticated model-family or reasoning-effort telemetry or binding selector is exposed, so this artifact does not claim GPT-6 or maximum reasoning.

Date: 2026-09-19 UTC  
Slot: R7-04 Constructive Model Research  
Native ID: `6aabe7ea6e1881919a65503f8445a813`  
Target: P0220 — David Aldous, *A one-dimensional drift-jump particle process*  
Status: **OPEN / PARTIAL** under the campaign closure protocol  
Methods: **B5 / B11 / B29**  
Frozen metric: `K_Bessel = infinity -> infinity` (**NO MOVEMENT**)

This note assumes only the already proved source-native identification

\[
(X_1,\ldots,X_k)_{\rm stat}\overset d=(\tau_1,\ldots,\tau_k),
\qquad
\tau_j=\inf\{t:\Lambda_1(t)\ge j\},
\tag{0.1}
\]

where `Lambda(t)` is rate-one poissonized Plancherel growth. Stationarity of the source process was proved independently from finite-time source convergence and the Feller semigroup, so none of the arguments below is used circularly to establish (0.1).

The preceding R7-04 work also established the forward Okounkov--Reshetikhin auxiliary factor

\[
\Phi(t,z)=e^{z-t/z}
\tag{0.2}
\]

and the associated extended kernel. The purpose here is not to create another scalar marginal formula. It is to expose a useful deformation, a complementary finite-particle representation of the arbitrary joint constraints, and a direct absolute-convergence argument at the infinite half-line boundary.

---

## 1. B5 — terminal Plancherel parameter and exact time dilation

Let `rho_c` denote the Plancherel specialization characterized by

\[
H(\rho_c;u)=e^{cu}.
\]

Fix observation times

\[
0=t_0<t_1<\cdots<t_r=T
\]

and a nested partition path

\[
\varnothing=\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\subset\lambda^{(r)}.
\]

For `beta>0`, define the beta-deformed path law

\[
\mathbb P_\beta(\lambda^{(1)},\ldots,\lambda^{(r)})
=
 e^{-\beta T}
 \left(\prod_{a=1}^r
 s_{\lambda^{(a)}/\lambda^{(a-1)}}(\rho_{t_a-t_{a-1}})
 \right)
 s_{\lambda^{(r)}}(\rho_\beta).
\tag{1.1}
\]

The Cauchy identity gives total mass one. Since a Schur function of degree `n` is homogeneous under Plancherel scaling,

\[
s_\lambda(\rho_\beta)=\beta^{|\lambda|}s_\lambda(\rho_1).
\tag{1.2}
\]

Writing `N_T=|\lambda^{(r)}|`, comparison with the ordinary (`beta=1`) path law gives the exact Radon--Nikodym identity

\[
\boxed{
\frac{d\mathbb P_\beta}{d\mathbb P_1}
=
 e^{-(\beta-1)T}\beta^{N_T}.
}
\tag{1.3}
\]

On the other hand,

\[
s_{\mu/\lambda}(\rho_{\beta u})
=
\beta^{|\mu|-|\lambda|}s_{\mu/\lambda}(\rho_u).
\tag{1.4}
\]

Multiplying (1.4) over all path increments shows that (1.1) is exactly ordinary Plancherel growth run at speed `beta`:

\[
\boxed{
(\Lambda_\beta(t_1),\ldots,\Lambda_\beta(t_r))
\overset d=
(\Lambda_1(\beta t_1),\ldots,\Lambda_1(\beta t_r)).
}
\tag{1.5}
\]

This is not an asymptotic statement; it is an identity of every finite-dimensional path law.

### 1.1 The deformed Schur kernel is a pure gauge plus time dilation

Under the same forward OR convention as the preceding run, the terminal specialization `rho_beta` changes the auxiliary factor to

\[
\boxed{
\Phi_\beta(t,z)=e^{\beta z-t/z}.
}
\tag{1.6}
\]

Let `K_beta` be the corresponding extended kernel. Starting from the double-contour formula and substituting

\[
z'=\beta z,\qquad w'=\beta w,
\]

all Jacobian and Cauchy factors cancel except the particle-coordinate gauge. One obtains

\[
\boxed{
K_\beta((t,x),(s,y))
=
\beta^{x-y}K_1((\beta t,x),(\beta s,y)).
}
\tag{1.7}
\]

Thus every finite gap determinant is invariant under the diagonal gauge and simply experiences the time dilation in (1.5).

### 1.2 Conditional box-count identities from differentiating the deformation

Let

\[
E=\bigcap_{a=1}^r\{X_{k_a}>t_a\}
=
\bigcap_{a=1}^r\{\Lambda_1(t_a)<k_a\}
\]

with all `t_a>0`, and write

\[
p(t_1,\ldots,t_r)=\mathbb P_1(E),
\qquad
\mathcal D=\sum_{a=1}^r t_a\partial_{t_a}.
\]

By (1.5),

\[
\mathbb P_\beta(E)=p(\beta t_1,\ldots,\beta t_r).
\tag{1.8}
\]

By (1.3), the same quantity is

\[
\mathbb E_1\left[1_E e^{-(\beta-1)T}\beta^{N_T}\right].
\tag{1.9}
\]

Differentiating `log` at `beta=1` gives

\[
\boxed{
\mathbb E[N_T\mid E]-T
=
\mathcal D\log p.
}
\tag{1.10}
\]

For the second derivative, the score is `-T+N_T/beta` and its beta derivative is `-N_T/beta^2`. Hence

\[
\boxed{
\operatorname{Var}(N_T\mid E)-\mathbb E[N_T\mid E]
=
(\mathcal D^2-\mathcal D)\log p.
}
\tag{1.11}
\]

Combining (1.10) and (1.11) yields the particularly simple equivalent formula

\[
\boxed{
\operatorname{Var}(N_T\mid E)
=
T+\mathcal D^2\log p.
}
\tag{1.12}
\]

These identities turn derivatives of the source stationary survival law into exact conditional Plancherel box-count moments. They also provide independent diagnostics for any proposed Fredholm or tableau formula.

**B5 outcome: SUCCESS.** The terminal parameter is not a new model; it is an exactly solvable exponential tilt/time dilation. It yields the kernel gauge (1.7) and conditional moment identities (1.10)--(1.12).

---

## 2. B11 — dualize arbitrary joint width constraints to nondecreasing finite row caps

Assume observation times are sorted:

\[
0<t_1<\cdots<t_r.
\]

The first row `Lambda_1(t)` is nondecreasing in time. Define suffix-min thresholds

\[
\kappa_a=\min_{b\ge a}k_b.
\tag{2.1}
\]

Then `kappa_1<=...<=kappa_r`, and monotonicity gives the exact simplification

\[
\boxed{
\bigcap_{a=1}^r\{\Lambda_1(t_a)<k_a\}
=
\bigcap_{a=1}^r\{\Lambda_1(t_a)<\kappa_a\}.
}
\tag{2.2}
\]

Indeed a later stricter first-row bound automatically implies the same stricter bound at every earlier time.

Now transpose every partition:

\[
\mu(t)=\Lambda(t)'.
\]

Plancherel growth is invariant under transposition because `f^{lambda'}=f^lambda` and the add-one-box transition probabilities transpose. Therefore `mu(t)` has the same path law as `Lambda(t)`. Since the first-row length of `Lambda` equals the number of rows of `mu`, (2.2) becomes

\[
\boxed{
E
=
\bigcap_{a=1}^r\{\ell(\mu(t_a))\le m_a\},
\qquad
m_a=\kappa_a-1,
}
\tag{2.3}
\]

with

\[
m_1\le m_2\le\cdots\le m_r.
\]

So every arbitrary collection of stationary-coordinate thresholds is equivalent to a Plancherel path constrained by a **nondecreasing finite row cap**.

### 2.1 Finite-particle Jacobi--Trudi transfer representation

Put `m=m_r`. Extend every partition with zeros to `m` rows and define strict particle coordinates

\[
x_i(\mu)=\mu_i-i,\qquad 1\le i\le m,
\]

with empty state

\[
e_i=-i.
\]

Define the one-particle Poisson kernel

\[
p_u(a,b)=
\begin{cases}
\displaystyle \frac{u^{a-b}}{(a-b)!},&a\ge b,\\
0,&a<b.
\end{cases}
\tag{2.4}
\]

Jacobi--Trudi under the Plancherel specialization gives, for partitions with at most `m` rows,

\[
\boxed{
s_{\mu/\lambda}(\rho_u)
=
\det\bigl[p_u(x_i(\mu),x_j(\lambda))\bigr]_{i,j=1}^m.
}
\tag{2.5}
\]

The cap `ell(mu)<=m_a` is exactly the pinning condition

\[
x_i(\mu)=-i\qquad(i>m_a).
\tag{2.6}
\]

Let `Delta_a=t_a-t_{a-1}` and `T=t_r`. Substituting (2.5) into the positive Schur-path formula yields

\[
\boxed{
\begin{aligned}
\mathbb P(E)
&=e^{-T}
\sum_{x^{(1)},\ldots,x^{(r)}}
\det[p_{\Delta_1}(x_i^{(1)},e_j)]\\
&\qquad\times
\prod_{a=2}^r
\det[p_{\Delta_a}(x_i^{(a)},x_j^{(a-1)})]
\det[p_1(x_i^{(r)},e_j)],
\end{aligned}
}
\tag{2.7}
\]

where the sum is over strict `m`-particle configurations corresponding to partitions and, at checkpoint `a`, coordinates `i>m_a` are pinned to `-i` as in (2.6). Skew Schur determinants automatically vanish for inadmissible non-growing transitions, so no extra sign convention is being inserted.

Equation (2.7) is an exact complementary representation of the same source joint law using only finitely many noncolliding particles, though each particle lives on a countable half-line.

### 2.2 Why the scalar determinant collapses but a generic joint threshold does not collapse naively

If every cap is the same value `m`, monotonicity makes all intermediate constraints redundant: only the final row-count bound matters. In (2.7), unrestricted intermediate sums can then be collapsed by repeated Cauchy--Binet/semigroup composition, producing the known finite Toeplitz/Bessel determinant.

For genuinely varying caps, (2.6) inserts checkpoint projections/pinnings between transfer kernels. Those projections prevent the same one-line semigroup collapse. This is an exact structural obstruction to the **naive** attempt to replace every arbitrary joint survival probability by the same kind of single finite Toeplitz determinant used for one coordinate.

A minimal witness is `s<t`, `k_1=2`, `k_2=3`. A growth path with

\[
\Lambda_1(s)=2,\qquad \Lambda_1(t)=2
\]

satisfies the final constraint `Lambda_1(t)<3` but violates the early constraint `Lambda_1(s)<2`; hence final-time data alone cannot encode this joint event.

This does **not** prove that no other finite determinant formula exists. It identifies the precise object a future finite-determinant reduction must absorb: a product of noncolliding Poisson transfer matrices with changing row-cap projections.

**B11 outcome: SUCCESS / REDUCTION.** Arbitrary joint stationary thresholds are exactly nondecreasing finite-row-cap events after transposition, with the finite-particle transfer formula (2.7). The remaining algebraic issue is the inserted projection structure, not an uncontrolled infinite Young-diagram sum.

---

## 3. B29 — direct absolute convergence of the infinite-half-line Fredholm series

The earlier B8 run justified the source Fredholm gap law by finite spatial truncation plus a Poisson-tail error. Here the infinite half-line is handled directly at the level of the Fredholm series.

For a partition `lambda`, use Maya particles

\[
\mathfrak S(\lambda)=\{\lambda_i-i+\tfrac12:i\ge1\}.
\]

For `k>=1`, let

\[
H_k=\{k-\tfrac12,k+\tfrac12,k+\tfrac32,\ldots\},
\qquad
M_k(\lambda)=|\mathfrak S(\lambda)\cap H_k|.
\tag{3.1}
\]

Every particle counted by `M_k` comes from a nonzero row, so

\[
\boxed{M_k(\lambda)\le |\lambda|.}
\tag{3.2}
\]

Let

\[
A=\bigsqcup_{a=1}^r\{t_a\}\times H_{k_a},
\qquad
T=\max_a t_a,
\]

and let `N_A` be the total number of space-time particles in `A`. Since the Plancherel size process is nondecreasing and

\[
N(T)=|\Lambda(T)|\sim\operatorname{Pois}(T),
\]

(3.2) gives the pathwise bound

\[
\boxed{N_A\le rN(T).}
\tag{3.3}
\]

Therefore

\[
\boxed{
\mathbb E[2^{N_A}]
\le
\mathbb E[2^{rN(T)}]
=
\exp\{T(2^r-1)\}<\infty.
}
\tag{3.4}
\]

### 3.1 Absolute Fredholm expansion

For distinct points `u_1,...,u_q` in the discrete space-time set, determinantal-process theory gives the correlation function

\[
\rho_q(u_1,\ldots,u_q)
=
\det[K(u_i,u_j)]_{i,j=1}^q\ge0.
\tag{3.5}
\]

Moreover

\[
\sum_{u_1,\ldots,u_q\in A\atop\text{distinct}}
\rho_q(u_1,\ldots,u_q)
=
\mathbb E[(N_A)_q].
\tag{3.6}
\]

Hence the absolute sum of the countable Fredholm series is

\[
\begin{aligned}
\sum_{q=0}^\infty\frac1{q!}
\sum_{u_1,\ldots,u_q\in A\atop\text{distinct}}
\left|\det[K(u_i,u_j)]\right|
&=
\sum_{q=0}^\infty\frac{\mathbb E[(N_A)_q]}{q!}\\
&=
\mathbb E[2^{N_A}]<\infty.
\end{aligned}
\tag{3.7}
\]

For every integer `n`,

\[
1_{\{n=0\}}
=
\sum_{q=0}^{n}(-1)^q\binom nq.
\tag{3.8}
\]

Using (3.7) to justify Fubini and taking expectation of (3.8) with `n=N_A` gives directly

\[
\boxed{
\mathbb P(N_A=0)
=
\sum_{q=0}^\infty\frac{(-1)^q}{q!}
\sum_{u_1,\ldots,u_q\in A\atop\text{distinct}}
\det[K(u_i,u_j)].
}
\tag{3.9}
\]

By (0.1), `N_A=0` is exactly the stationary survival event `X_{k_a}>t_a` for all `a`. Thus (3.9) proves the infinite-half-line Fredholm **series** directly, without first truncating the spatial half-lines.

### 3.2 Certified truncation by Fredholm order

If the Fredholm series is truncated after order `M`, its absolute remainder satisfies

\[
R_M
\le
\mathbb E\left[2^{N_A}1_{\{N_A>M\}}\right]
\le
\mathbb E\left[2^{rN(T)}1_{\{rN(T)>M\}}\right].
\tag{3.10}
\]

Let

\[
q_M=\left\lfloor\frac Mr\right\rfloor+1.
\]

For `N~Pois(T)` and `a>0`, exponential tilting gives

\[
\mathbb E[a^N1_{\{N\ge q\}}]
=e^{T(a-1)}\Pr\{\operatorname{Pois}(aT)\ge q\}.
\tag{3.11}
\]

Taking `a=2^r` in (3.10) yields the explicit certificate

\[
\boxed{
R_M
\le
 e^{T(2^r-1)}
 \Pr\!\left\{\operatorname{Pois}(2^rT)\ge
 \left\lfloor\frac Mr\right\rfloor+1\right\}.
}
\tag{3.12}
\]

Thus arbitrary finite-coordinate stationary survival probabilities have not only a convergent infinite-half-line Fredholm expansion, but a direct certified truncation in Fredholm order.

Important scope statement: (3.7)--(3.12) prove **absolute convergence of the Fredholm series and the gap identity**. They do not assert, and do not require here, that the raw multi-time block kernel defines a trace-class operator in a particular Hilbert-space realization.

**B29 outcome: SUCCESS.** The analytic boundary at infinity is closed at the level actually needed for the source probability, with an explicit Poisson-tail remainder.

---

## 4. What these three methods add, and what they do not add

The cumulative source-answer candidate now has three complementary joint-law presentations:

1. the extended-Schur gap Fredholm series/determinant, now with the direct absolute-convergence proof (3.7)--(3.12);
2. the positive Young-diagram path/dynamic-program representation from earlier runs;
3. the finite-particle row-cap transfer formula (2.7).

The beta deformation (1.3)--(1.12) links these representations to exact conditional moments and confirms the time normalization independently.

None of these changes the frozen scalar metric because `K_Bessel` had already reached infinity. In particular,

\[
K_{\rm Bessel}:\quad \infty\longrightarrow\infty.
\]

This is therefore the sixth ordinary unchanged P0220 run under the owner protocol, despite genuine strengthening of the joint-law package.

The protocol consequence is worker-local retirement/handoff from active P0220 research after this run. That is **not** a mathematical verdict that P0220 is solved, known, refuted, or released to another worker. Campaign closure still requires at least:

- source-specific prior-art reconciliation beyond bounded negative searches;
- an actual independent P26 full-proof audit;
- a distinct OTHER-track full-proof audit;
- a self-contained source-scope paper package if closure is promoted.

The living Aldous page still states the request for a fairly explicit stationary distribution. R7-04 therefore keeps the mathematical label **OPEN / PARTIAL** and hands off the cumulative candidate answer without claiming novelty or closure.

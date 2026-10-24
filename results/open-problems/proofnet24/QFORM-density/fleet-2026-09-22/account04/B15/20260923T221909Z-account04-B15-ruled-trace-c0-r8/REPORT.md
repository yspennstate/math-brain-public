SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-23T22:19:09Z.
attacking: rough-product interval/trace transport for ruled estimates and same-constant C0 closure of paid target branches.

# account04/B15 — rough ruled trace transport and same-constant target regularity

Programme: QFORM-DENSITY-3EIG-20260922  
Run: 20260923T221909Z-account04-B15-ruled-trace-c0-r8  
Status: ROUGH_TRACE_COMPILER_PROVED / TARGET_REGULARITY_IMPLICATION_CLOSED / PARTNER_APPLIED / FULL_QFORM_OPEN  
Execution: WITHOUT_VERIFIED_BRAIN.

## 1. Result

Two gaps are closed.

First, every smooth ruled/coarea interval estimate whose constant is uniform over cap-preserving smooth approximations passes to arbitrary measurable cap-one product densities. The passage is made at the level of measures of intervals. It never evaluates a representative of a rough density on a level surface. A moving majority sheet is also allowed, provided its limiting boundary is null; this includes both the nonsingular ruled theorem and the minority-null limit used by account01/B15.

Second, the completed fixed-matrix rank-three regularity theorem turns any already-paid interval estimate into a continuous density with exactly the same height constant. Thus continuity is no longer an additional quantitative gap after a target branch has established

$$
\Pr\{Q\in I\}\le M|I|.
$$

Applying this to the completed account01/B15 minority-null theorem gives a new cross-coupled endpoint: if a physical $3\times3$ block is rank-two semidefinite, its outside cross block lies in its range, and the full matrix has rank at least three, then

$$
p_Q\in C_0(\mathbb R),\qquad
\|p_Q\|_\infty\le {2\pi\over\sqrt{\lambda_1\lambda_2}}.
$$

The previous account01 continuity corollary required block diagonality. The conclusion above permits arbitrary nonzero range-aligned cross coupling and arbitrary outside quadratic curvature.

The unrestricted universal-height conjecture remains open.

## 2. Sources and corrections retained

Fresh controls were read from yspennstate/math-research-brain with owner-control revision 2026-09-22.15; the current request continues to mark the full conjecture open.

The source-pinned inputs used here are:

1. the ruled one-sheet theorem and its exact coarea parametrisation in math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837, especially COUNTEREXAMPLE_SEARCH.md;
2. the completed fixed-matrix theorem in math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056, proving that every rank-at-least-three quadratic form under cap-one product inputs has an instance-dependent density in $C_0\cap L^\infty$;
3. the completed account01/B15 semidefinite minority-null theorem in math-open-problems@fc9d06c78e03b4e1ad924f49fb9ab0f03018d2cd;
4. the newest grouped determinant and rough ruled audit in math-open-problems@58b7dd57dc1282bcf84fd0ceb0c314baca3a5abe;
5. the previous account04/B15 rough conditional-convolution theorem in math-open-problems@d734abaae2eedafe9572b4215107c9637807acaa.

The proof below uses no arbitrary-joint coarea height theorem, no post-rotation independence, no pointwise evaluation of a rough density trace, no moment or support assumption, and no inference of continuity merely from essential boundedness.

## 3. Cap-preserving approximation of a rough product

Let $f_1,\dots,f_m$ be arbitrary probability densities on $\mathbb R$ with $0\le f_j\le1$. Choose a standard nonnegative mollifier $\rho_\eta$ and put

$$
f_{j,\eta}=f_j*\rho_\eta.
$$

Then $f_{j,\eta}$ is smooth, is a probability density, and

$$
0\le f_{j,\eta}\le1,\qquad
\|f_{j,\eta}-f_j\|_1\longrightarrow0.
$$

No truncation or support hypothesis is needed. For the product densities

$$
F_\eta(x)=\prod_{j=1}^m f_{j,\eta}(x_j),\qquad
F(x)=\prod_{j=1}^m f_j(x_j),
$$

a telescoping expansion and the fact that every marginal has mass one give

$$
\boxed{\ \|F_\eta-F\|_1
\le\sum_{j=1}^m\|f_{j,\eta}-f_j\|_1\longrightarrow0.\ }
\tag{3.1}
$$

Thus the product laws converge in total variation. Deterministic translations produced by conditioning or completing a square preserve every norm in (3.1). In particular, the approximation does not rotate the independent coordinates.

## 4. Interval/trace transport lemma

### Theorem 4.1 — rough moving-sheet transport

Let $F_k,F$ be probability densities on $\mathbb R^m$ with $\|F_k-F\|_1\to0$. Let $q_k,q,h_k,h$ be measurable real functions such that

$$
q_k(x)\to q(x),\qquad h_k(x)\to h(x)
$$

for $F(x)dx$-almost every $x$, and assume

$$
\int_{\{h=0\}}F(x)\,dx=0.
\tag{4.1}
$$

Define subprobability measures

$$
\nu_k(E)=\int {\bf1}_{\{q_k(x)\in E\}}
{\bf1}_{\{h_k(x)\ge0\}}F_k(x)\,dx
$$

and

$$
\nu(E)=\int {\bf1}_{\{q(x)\in E\}}
{\bf1}_{\{h(x)\ge0\}}F(x)\,dx.
$$

If for every open interval $I$

$$
\nu_k(I)\le M|I|
\tag{4.2}
$$

with one constant $M$ independent of $k$, then

$$
\boxed{\ \nu(E)\le M|E|\quad\hbox{for every Borel }E.\ }
\tag{4.3}
$$

Hence $\nu$ has an essentially bounded density of height at most $M$.

#### Proof

For a bounded continuous test function $\varphi$,

$$
\left|\int\varphi(q_k){\bf1}_{\{h_k\ge0\}}F_k
-\int\varphi(q_k){\bf1}_{\{h_k\ge0\}}F\right|
\le\|\varphi\|_\infty\|F_k-F\|_1.
$$

Outside the null set in (4.1), the sign indicators converge. Dominated convergence therefore gives

$$
\int\varphi\,d\nu_k\longrightarrow\int\varphi\,d\nu.
$$

Thus $\nu_k\Rightarrow\nu$. Portmanteau applied to an open interval $I$ yields

$$
\nu(I)\le\liminf_k\nu_k(I)\le M|I|.
$$

The same holds for every open set by disjoint interval decomposition, and outer regularity gives (4.3).

This proof is entirely at interval/measure level. It never chooses a pointwise version of a rough output density.

### Fixed-sheet corollary

If $q_k=q$ and $h_k=h$, condition (4.1) is unnecessary for total-variation convergence of the restricted pushforwards:

$$
\|q_\#({\bf1}_{\{h\ge0\}}F_kdx)
-q_\#({\bf1}_{\{h\ge0\}}Fdx)\|_{TV}
\le\|F_k-F\|_1.
\tag{4.4}
$$

This is the form needed to pass a smooth ruled estimate to arbitrary rough cap-one inputs.

## 5. Where coarea enters, and where it does not

For a smooth approximating density $F_k$ and a nonconstant quadratic-affine polynomial $q$, coarea gives

$$
\int_{{q}^{-1}(E)}F_k(x)\,dx
=\int_E\left(\int_{q^{-1}(t)}
{F_k(x)\over|\nabla q(x)|}\,d\mathcal H^{m-1}(x)\right)dt.
\tag{5.1}
$$

The critical set $\{\nabla q=0\}$ is a proper affine subspace and hence has zero mass under the absolutely continuous product law. In the ruled one-sheet theorem, the source-pinned parametrisation gives the exact trace measure $(1/2)d\theta\,ds$ after the coarea Jacobian and ruling speed are combined. The projection-density bound is then applied to the remaining line integral for each smooth approximation.

Equation (5.1) justifies the smooth trace calculation. Equations (3.1) and (4.4) transport only the resulting interval inequality. They do not assert that $F$ has a meaningful pointwise restriction to $q^{-1}(t)$, and they do not interchange an arbitrary rough trace with a limiting operation.

For the account01/B15 minority-null passage one takes

$$
q_\varepsilon=Q_\varepsilon,\qquad
h_\varepsilon=Q_\varepsilon-c_*(W).
$$

The limit is $q=Q$ and $h=Q-c_*(W)\ge0$. Its boundary is the affine kernel line of the rank-two semidefinite active block for each fixed $W$, hence has zero conditional three-dimensional Lebesgue measure and therefore zero product probability. Theorem 4.1 is exactly the required moving-sheet justification.

## 6. Same-constant continuous-representative compiler

### Theorem 6.1

Let $A$ be a fixed real symmetric matrix with $\operatorname{rank}A\ge3$, and let the coordinates of $X$ be independent with arbitrary probability densities bounded by one. Suppose a separate argument proves

$$
\Pr\{X^TAX\in I\}\le M|I|
\tag{6.1}
$$

for every interval $I$. Then the law of $X^TAX$ has a canonical representative $p\in C_0(\mathbb R)$ and

$$
\boxed{\ \|p\|_\infty\le M.\ }
\tag{6.2}
$$

#### Proof

The completed fixed-matrix theorem at commit 9b8bb7e... supplies a density $p\in C_0(\mathbb R)$ for this exact rough product instance. Equation (6.1) says that the same law is dominated by $Mdt$, so $p\le M$ almost everywhere. If $p(t_0)>M$, continuity would give an open interval on which $p>M$, contradicting (6.1). Thus (6.2) holds pointwise.

The theorem claims no law- or matrix-uniform modulus of continuity. It says that once a branch pays a uniform interval constant, continuity costs nothing further.

### Full-target logical implication

Every matrix in the owner target has rank at least three. Consequently, a proof of the universal essential-density estimate automatically yields, for every target instance, a $C_0$ density with the same universal height constant. Hence there is no separate quantitative regularity obstruction after the universal interval theorem is proved. The unresolved problem is the universal value of $M$, not qualitative continuity.

This implication uses the quadratic/product fixed-instance theorem; it is not the false general statement that every bounded density has a continuous representative.

## 7. Completed account01/B15 theorem applied at an actual inequality

Split original coordinates as $X=(U,W)$ with $U\in\mathbb R^3$ and write

$$
A=\begin{pmatrix}B&C\\ C^T&D\end{pmatrix}.
$$

Assume $B$ is positive or negative semidefinite of rank two, with nonzero eigenvalue magnitudes $\lambda_1,\lambda_2$, and

$$
\operatorname{Range}(C)\subseteq\operatorname{Range}(B).
\tag{7.1}
$$

The completed account01/B15 theorem proves directly at interval level

$$
\Pr\{Q\in I\}\le
{2\pi\over\sqrt{\lambda_1\lambda_2}}|I|.
\tag{7.2}
$$

Suppose now only that the full matrix has rank at least three. Applying Theorem 6.1 to the actual inequality (7.2) gives

$$
\boxed{
p_Q\in C_0(\mathbb R),\qquad
\|p_Q\|_\infty\le
{2\pi\over\sqrt{\lambda_1\lambda_2}}.
}
\tag{7.3}
$$

This strictly extends the continuity corollary recorded in the account01 report: $C$ need not vanish, and $D$ is arbitrary. Only the exact range condition (7.1) and rank at least three are used.

### Concrete full-target family

For arbitrary $u,v\in\mathbb R$, let

$$
A_{u,v}=\begin{pmatrix}
1&0&0&u\\
0&1&0&v\\
0&0&0&0\\
u&v&0&-1
\end{pmatrix}.
\tag{7.4}
$$

Its eigenvalues are

$$
0,\quad1,\quad\sqrt{1+u^2+v^2},\quad-\sqrt{1+u^2+v^2}.
\tag{7.5}
$$

Thus it has three eigenvalues of modulus at least one for every $u,v$, including arbitrarily large cross coupling. Its physical triple $B=\operatorname{diag}(1,1,0)$ satisfies (7.1). Therefore, for every four independent cap-one real inputs,

$$
Q_{u,v}=X_1^2+X_2^2+2uX_1X_4+2vX_2X_4-X_4^2
$$

has

$$
\boxed{\ p_{Q_{u,v}}\in C_0(\mathbb R),\qquad
\|p_{Q_{u,v}}\|_\infty\le2\pi,\ }
\tag{7.6}
$$

uniformly in $u,v$ and in the four input laws. The inactive $X_3$ simply records the minority-null physical direction; no rotation of the product law is used.

## 8. Relation to the newest grouped receiver

The account02 grouped determinant theorem at 58b7dd57... proves a stronger constant in a different chamber: for a physical block

$$
\begin{pmatrix}C&M\\M^T&0\end{pmatrix},\qquad M\in GL_d,
$$

it gives

$$
\|p_Q\|_\infty\le {d\over d-1}|\det M|^{-1/d}
$$

and a separate $C_0$ conclusion. Theorem 6.1 shows that the continuity step can equivalently be viewed as a general target-level closure once the interval estimate is paid. The hard remaining issue in that route is still a nonzero leaf-leaf quadratic block or a structural theorem producing a determinant-paid group; regularity is not the obstruction.

## 9. Exact status

- Rough ruled/coarea interval transport: proved in Theorem 4.1 and Section 5.
- Pointwise rough density trace: neither needed nor asserted.
- Fixed-instance target continuity: supplied by the completed rank-at-least-three theorem.
- Same-constant continuity after any paid target interval bound: proved in Theorem 6.1.
- Range-aligned semidefinite endpoint with nonzero cross coupling: continuous with the account01 height constant by (7.3).
- Concrete full-target family (7.4): $C_0$ density and height at most $2\pi$ uniformly in the cross coupling.
- Universal density cap for all target matrices: OPEN.
- Counterexample: none produced.

The first remaining mathematical gap is still a product-preserving universal interval estimate in the dense transverse-coupling geometry where no already-paid physical receiver has a quantitative determinant/minor/volume gate. The present result removes rough trace and qualitative regularity from that gap.


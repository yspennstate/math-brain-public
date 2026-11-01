Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — METRIC MOVEMENT on active R09 successor G0013: `U_* = 580249/5337500 = 0.108711756440281... -> 1289727882057511/11918000000000000 = 0.1082168050056646...`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B8 GO THE OTHER WAY AND DISCRETIZE, B14 FIND THE GROUP ACTING, B20 FIND WHY THE ALGORITHM FAILS.** GPT-6 / maximum was requested in prompt text, but this runtime identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry, so I do not claim GPT-6 or maximum reasoning.

# R09 CLOSABLE OUTSIDE — G0013: optimized box penalty, D4 constraints, and the joint-Brenier obstruction

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, and mandatory run-start reads

I did **not** reopen Pengfei Tang, Question 4.11. Its periodic-tree target remains retired from this R09 slot at the frozen metric `UNBOUNDED_ABOVE`, supported retirement count `6`. I also did not reopen G0002 / Cerf Conjecture 53.1, which remains handed off at `Delta_8=UNMEASURED`.

The controlling current exclusive claim is `operations/claims/G0013.md`. R09 owns the Catalano--Lavenant uniform-copula Wasserstein question. With
\[
\lambda=\mathrm{Unif}[0,1],\qquad \nu=\lambda\otimes\lambda,
\]
write
\[
M=\sup_{\pi\in\Pi(\lambda,\lambda)}W_2^2(\pi,\nu).
\]
The source conjecture is
\[
M=\frac1{10},
\]
with the diagonal and antidiagonal couplings as maximizers. The fixed R09 metric is

`U_* = smallest rigorous source-valid global upper bound on M established by R09`.

The preceding complete report was
`runs/R09/20260917T1932Z_g0013_two_sided_box_projection_c7e4b2.md`,
with
\[
U_*^{\rm old}=\frac{580249}{5337500}=0.108711756440281\ldots.
\]

Before doing new mathematics I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/G0013.md`;
- the newest complete R09 report above;
- the newest searchable neighboring R08 report, `runs/R08/20260917T1930Z_f0083_stuck1_corner_recovery_3d7a91.md`;
- the newest searchable R10 successor/ownership state (current searches recover the I0068 successor claim and earlier rotation reports; no newer 17 September R10 run was indexed in the bounded search);
- the preserved G0013 intake/attempt history, including G0013-A001/A002 and the finite-grid/permutation searches recorded in the claim.

The intake corpus is too large to render verbatim through the connector; I used exact target/source/ID searches and preserved the claim's prior-attempt summary rather than pretending to have re-read every JSON byte. Root `RESULTS.md` is stale on R09 relative to the active G0013 claim; per policy this attacking worker does not edit shared roots.

## 2. Fresh source and current-literature check — 17 September 2026

Primary source: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034v1 (7 October 2025), Remark 3. I re-opened the primary PDF and checked the actual Remark 3 page. It states that for two uniform marginals on `[0,1]` with Euclidean quadratic Wasserstein distance, computing
\[
\sup_{\gamma\in\Gamma(\lambda,\lambda)}W(\gamma,\lambda^2)
\]
is open and conjectures that one of the two diagonals attains the supremum; it explicitly says a proof is lacking.

Later primary source: Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1 (9 September 2026). Its abstract still says that Catalano and Lavenant **conjectured** the monotone and antimonotone uniform couplings are farthest from independence and proves the Gaussian analogue instead.

Fresh bounded searches on 17 September 2026 used the exact titles/authors, `uniform copula farthest independence Wasserstein`, `Catalano Lavenant 1/10`, `Couplings Farthest from the Independent Gaussian`, and combinations of the conditional-CDF / clipped-affine / Chatterjee-xi terminology. I found no later source claiming a resolution of the exact uniform conjecture. This is bounded status evidence only; **publication novelty remains UNVERIFIED**.

A particularly relevant adjacent paper is Jonathan Ansari and Marcus Rockel, *The exact region and an inequality between Chatterjee's and Spearman's rank correlations*, J. Multivariate Analysis 214 (July 2026), 105630. Their exact xi-rho boundary is described by asymmetric piecewise-linear / diagonal-band copulas. Thus clipped-affine conditional structures are **not** to be advertised as a generic new phenomenon. What is new in this run's argument, subject to later prior-art review, is their use inside the specific Brenier/Jacobi upper-bound mechanism and the joint-compatibility obstruction below.

## 3. Inherited full-class reduction

For a positive smooth copula density, let
\[
T=\nabla\phi=(u,v)
\]
be the Brenier map from the independent uniform square to \(\pi\). For \(t,s\in[0,1]\), define
\[
q_t(y)=\lambda\{x:u(x,y)\le t\},\qquad
r_s(x)=\lambda\{y:v(x,y)\le s\}.
\]
Uniform output marginals give
\[
\int_0^1q_t(y)\,dy=t,\qquad
\int_0^1r_s(x)\,dx=s.
\tag{3.1}
\]
Put
\[
I_1=\int_0^1\operatorname{Var}(q_t)\,dt,\qquad
I_2=\int_0^1\operatorname{Var}(r_s)\,ds.
\]
The earlier R09 calculation established
\[
\boxed{W_2^2(\pi,\nu)=I_1+I_2=:S.}
\tag{3.2}
\]

For each \(t\), write
\[
q_t(y)-t=A_t\Bigl(y-\frac12\Bigr)+g_t(y),
\qquad g_t\perp\{1,y-\tfrac12\},
\]
and let
\[
h_t=\|g_t\|_2^2,\qquad H_1=\int_0^1h_t\,dt,
\]
with the analogous \(H_2\) for \(r_s\). The Jacobi spectral-gap plus positive-semidefinite Brenier-Hessian argument gives
\[
2I_1+I_2+4H_1\le\frac16,
\qquad
I_1+2I_2+4H_2\le\frac16.
\tag{3.3}
\]
Hence, with \(H=H_1+H_2\),
\[
\boxed{S\le\frac19-\frac43H.}
\tag{3.4}
\]

The preceding report solved exactly the scalar box obstacle. For a measurable \(q:[0,1]\to[0,1]\) of mean \(t\), with
\[
m=\min(t,1-t),\qquad a=|A|,
\]
the smallest higher-mode mass is
\[
h_{\min}(m,a)=
\begin{cases}
0,&0\le a\le2m,\\[1mm]
\dfrac{(a-2m)^3}{12(6m-a)},
&2m<a\le6m-8m^2,\\[3mm]
m(1-m)-\dfrac L6-\dfrac{a^2}{12},
&6m-8m^2<a\le6m(1-m),
\end{cases}
\tag{3.5}
\]
where in the last regime
\[
L=\sqrt{12m(1-m)-2a}.
\tag{3.6}
\]
The unique minimizer is the appropriate clipped affine profile.

This run asks a different question: how far can (3.5) itself be pushed, and where exactly does any one-coordinate optimization stop being capable of solving the source conjecture?

## 4. B8 — discretize only after the analytic reduction: a sharper global bound

Choose the rational stationary point
\[
u_0=\frac{17}{12}.
\]
For the one-sided-ramp regime parameterize
\[
a=2mu,\qquad 1<u\le3-4m.
\]
For a penalty \(k>0\), define
\[
\Psi_k(m,a)=\frac{a^2}{12}-k h_{\min}(m,a).
\tag{4.1}
\]
Then in the one-sided-ramp regime
\[
\Psi_k(m,2mu)=m^2G_k(u),
\qquad
G_k(u)=\frac13\left[u^2-k\frac{(u-1)^3}{3-u}\right].
\tag{4.2}
\]
The stationary condition is especially clean. Put
\[
K(u)=\frac{u(3-u)^2}{(u-1)^2(4-u)}.
\tag{4.3}
\]
Direct differentiation gives
\[
K'(u)=\frac{12(u-3)}{(u-4)^2(u-1)^3}<0,
\qquad 1<u<3.
\tag{4.4}
\]
Moreover the sign of \(G_k'(u)\) is the sign of \(K(u)-k\). Therefore choosing
\[
\boxed{k=K(17/12)=\frac{6137}{775}}
\tag{4.5}
\]
forces the unique one-sided interior maximizer to be \(u_0=17/12\), and exact arithmetic gives
\[
G_k(u_0)=\frac{17}{31}.
\tag{4.6}
\]
The transition at which the admissible endpoint \(3-4m\) reaches \(u_0\) is
\[
\boxed{m_0=\frac{3-u_0}{4}=\frac{19}{48}.}
\tag{4.7}
\]
Consequently, for \(0\le m\le m_0\), the exact pointwise envelope is
\[
f_k(m):=\sup_a\Psi_k(m,a)=\frac{17}{31}m^2.
\tag{4.8}
\]
(The no-clipping branch gives only \(m^2/3\), so it is strictly smaller away from zero.)

### 4.1 The tail is a one-variable concave maximization

Let
\[
c=1+k=\frac{6912}{775},
\qquad
r=\frac{k}{c}=\frac{6137}{6912}.
\tag{4.9}
\]
In the two-sided clipped regime write
\[
a=6m(1-m)-\frac{L^2}{2},\qquad 0\le L\le2m.
\]
Then
\[
F(m,L)
=\frac{c}{12}a^2-km(1-m)+\frac{k}{6}L.
\tag{4.10}
\]
Its derivative is
\[
\partial_LF(m,L)=\frac{k-caL}{6},
\tag{4.11}
\]
while
\[
\partial_L(aL)=6m(1-m)-\frac32L^2\ge6m(1-2m)\ge0.
\tag{4.12}
\]
Hence \(aL\) is increasing and \(F\) is concave in \(L\). For \(m\ge m_0\), the unique maximizer \(L_m\in[0,2m]\) is characterized by
\[
\boxed{L_m\left(6m(1-m)-\frac{L_m^2}{2}\right)=r.}
\tag{4.13}
\]
At \(m=m_0\), \(L_{m_0}=2m_0=19/24\), so this branch glues exactly to (4.8).

The tail envelope is monotone in \(m\). By the envelope theorem, at (4.13),
\[
\frac{d}{dm}f_k(m)
=(1-2m)(ca-k)
=k(1-2m)\left(\frac1{L_m}-1\right)\ge0,
\tag{4.14}
\]
since \(0<L_m\le2m\le1\).

This is where B8 is useful: the original infinite-dimensional copula problem has now been reduced analytically to one monotone scalar function on the short interval \([19/48,1/2]\). Discretizing **here**, rather than enumerating copulas or permutation grids, produces a source-valid full-class certificate.

### 4.2 Exact 18,432-cell upper sum

Define
\[
B_k=2\int_0^{1/2}f_k(m)\,dm.
\tag{4.15}
\]
The factor 2 is the symmetry \(m=\min(t,1-t)\).

On \([0,m_0]\), (4.8) integrates exactly. On \([m_0,1/2]\), split into \(N=18432\) equal cells of width
\[
\Delta=\frac5{884736}.
\]
At each right endpoint \(m_j\), exact rational bisection brackets the unique root \(L_{m_j}\) of (4.13). If \([\ell_j,h_j]\) is the bracket with \(F_L(\ell_j)\ge0\ge F_L(h_j)\), concavity gives the rigorous tangent cap
\[
f_k(m_j)
\le F(m_j,\ell_j)
+F_L(m_j,\ell_j)(h_j-\ell_j).
\tag{4.16}
\]
Monotonicity (4.14) then makes the right-endpoint sum an upper bound for the integral.

The exact checker executes all 18,432 rational cells, with root brackets of width at most
\[
2^{-42}=\frac1{4398046511104},
\]
and obtains the exact rational upper sum
\[
B_k<
\boxed{\frac{4442834905081}{10^{14}}}
=0.04442834905081.
\tag{4.17}
\]
The exact computed upper sum before the simple decimal cap is approximately
\[
0.044428349050804276,
\]
and the exact positive cap margin is about \(5.72524\times10^{-15}\).

### 4.3 Convert the scalar bound into a full global Wasserstein bound

For every level,
\[
\frac{A_t^2}{12}-k h_t\le f_k(m_t).
\]
Therefore
\[
\operatorname{Var}(q_t)
=\frac{A_t^2}{12}+h_t
\le f_k(m_t)+(1+k)h_t.
\]
Integrating gives
\[
I_1\le B_k+cH_1,
\qquad
I_2\le B_k+cH_2,
\tag{4.18}
\]
so
\[
S\le2B_k+cH.
\tag{4.19}
\]
Use the certified cap (4.17) and combine (4.19) with (3.4). The increasing and decreasing affine bounds intersect at
\[
H_0=rac{310449061482401}{143016000000000000}
=0.002170729579084865\ldots,
\]
and yield
\[
\boxed{
S=W_2^2(\pi,\nu)
\le
U_*^{\rm new}
:=\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\tag{4.20}
\]
The usual marginal-preserving circular smoothing argument from the preceding reports passes the positive-smooth-density estimate to arbitrary copulas.

Therefore the full source-level bracket is now
\[
\boxed{
\frac1{10}
\le M
\le
\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\tag{4.21}
\]
This is strict metric movement:
\[
U_*^{\rm old}-U_*^{\rm new}
=rac{2518800921442803}{5088986000000000000}
=0.0004949514346164055\ldots>0.
\tag{4.22}
\]
The remaining gap to the conjectured value is
\[
U_*^{\rm new}-\frac1{10}
=rac{97927882057511}{11918000000000000}
=0.008216805005664626\ldots .
\tag{4.23}
\]
This is **PARTIAL**, not closure.

## 5. B20 — find why the scalar algorithm fails: nesting alone is not the missing constraint

The previous run suggested that the pointwise clipped-affine optimizer might fail to glue into one nested conditional-CDF family. That would have supplied an extra deficit. This run checks the opposite possibility first.

It turns out the pointwise maximizers **do glue**.

For \(0\le m\le m_0\), let
\[
L_0=\frac{19}{24},\qquad \alpha_0=1-L_0=\frac5{24},
\]
and define
\[
q_m^+(y)=\frac{2m}{L_0^2}(y-\alpha_0)_+.
\tag{5.1}
\]
Because \(2m/L_0\le1\) precisely up to \(m_0\), this is `[0,1]`-valued, has mean \(m\), and realizes the lower-ramp optimizer \(a=2mu_0\).

For \(m_0\le m\le1/2\), let \(L_m\) be the root in (4.13), put
\[
\alpha_m=1-m-\frac{L_m}{2},
\]
and define
\[
q_m^+(y)=
\operatorname{clip}_{[0,1]}
\left(\frac{y-\alpha_m}{L_m}\right).
\tag{5.2}
\]
This is exactly the two-obstacle optimizer. At \(m=m_0\), (5.1) and (5.2) coincide.

Differentiate (4.13). With
\[
D=6m(1-m)-\frac32L_m^2>0,
\]
we get
\[
L_m'=-\frac{6(1-2m)L_m}{D}\le0.
\tag{5.3}
\]
Moreover
\[
L_m'\ge-2
\]
is equivalent to
\[
L_m^2+2(1-2m)L_m-4m(1-m)\le0.
\]
The left side factors exactly as
\[
(L_m-2m)(L_m+2-2m),
\tag{5.4}
\]
which is nonpositive because \(0<L_m\le2m\). Thus
\[
-2\le L_m'\le0.
\tag{5.5}
\]
On the interior ramp in (5.2), writing \(p=q_m^+(y)\in(0,1)\),
\[
\partial_m q_m^+(y)
=\frac{1+L_m'(1/2-p)}{L_m}\ge0
\tag{5.6}
\]
by (5.5). The two breakpoints also move left, so the clipped profiles are pointwise nondecreasing in \(m\). The lower branch (5.1) is visibly nondecreasing in \(m\).

For \(t\in[0,1/2]\) set \(q_t=q_t^+\), and for \(t\in[1/2,1]\) set
\[
q_t(y)=1-q_{1-t}^+(1-y).
\tag{5.7}
\]
The centered \(m=1/2\) profile satisfies the same symmetry, so (5.7) glues continuously. For every fixed \(y\), \(t\mapsto q_t(y)\) is a genuine CDF; and the moment constraints give
\[
\int_0^1q_t(y)\,dy=t.
\]
Hence this nested family is realized by a bona fide copula of \((Y,U)\) with both marginals uniform.

**Consequence.** For this chosen penalty, the one-coordinate inequality
\[
I\le B_k+cH
\tag{5.8}
\]
is sharp at the level of arbitrary bivariate copulas: the pointwise clipped-affine maximizers can be chosen coherently across every threshold. Therefore another run that merely adds the CDF nesting constraint to the scalar obstacle cannot improve the full upper bound. The missing information must couple the `q` and `r` families through the fact that they come from the **same Brenier map**.

This is a useful failure result, not a source theorem.

## 6. B20 continued — the exact joint-Brenier slope obstruction

The shared Brenier Hessian gives the missing pointwise constraint explicitly. Write
\[
D^2\phi=
\begin{pmatrix}a&b\\b&c\end{pmatrix}\succeq0.
\]
At a regular interior point, put
\[
t=u(x,y),\qquad s=v(x,y).
\]
Along a horizontal slice, \(q_t(y)=x\); implicit differentiation gives
\[
\partial_y q_t(y)=-\frac ba.
\tag{6.1}
\]
Similarly
\[
\partial_x r_s(x)=-\frac bc.
\tag{6.2}
\]
Therefore
\[
\boxed{
\partial_yq_{u(x,y)}(y)\,
\partial_xr_{v(x,y)}(x)
=rac{b^2}{ac}\in[0,1].
}
\tag{6.3}
\]
In particular the two linked slopes have the same sign and their absolute-value product is at most one.

This exposes why simultaneous scalar saturation is impossible on overlapping active ramps. The tail extremizers (5.2) have active-ramp slope magnitude
\[
\frac1{L_m}>1
\]
away from the endpoint \(L=1\). If both linked conditional families were simultaneously in such scalar-extremal ramp regions at the same source point, their slope product would exceed one, contradicting (6.3).

So the new target is no longer vague: quantify the measure of the overlap forced between the active regions of the two conditional families, then charge a definite deficit whenever (6.3) prevents both scalar penalties from saturating. That is a genuinely joint two-coordinate obligation.

## 7. B14 — D4 symmetry produces exact Spearman constraints

There is a second expression of the same joint restriction using the dihedral symmetries of the source square.

Center source and target coordinates:
\[
Z=(X-\tfrac12,Y-\tfrac12),
\qquad
\widetilde T=(U-\tfrac12,V-\tfrac12).
\]
Brenier monotonicity gives
\[
(T(z)-T(z'))\cdot(z-z')\ge0.
\tag{7.1}
\]
Pair each source point with its image under a source-square reflection and integrate, using invariance of the uniform square.

Let
\[
d=\rho_S(X,U)+\rho_S(Y,V),
\qquad
c_\times=\rho_S(X,V)+\rho_S(Y,U),
\]
where \(\rho_S\) is Spearman correlation (ordinary correlation here because every coordinate is uniform).

- reflection in the vertical midline gives \(\rho_S(X,U)\ge0\);
- reflection in the horizontal midline gives \(\rho_S(Y,V)\ge0\);
- diagonal swap \((x,y)\mapsto(y,x)\) gives \(d-c_\times\ge0\);
- anti-diagonal swap \((x,y)\mapsto(1-y,1-x)\) gives \(d+c_\times\ge0\).

Thus
\[
\boxed{d\ge|c_\times|.}
\tag{7.2}
\]
The transport cost determines \(d\) exactly:
\[
S
=\mathbb E|Z-\widetilde T|^2
=\frac13-\frac d6,
\qquad
\boxed{d=2-6S.}
\tag{7.3}
\]
The new bound (4.20) therefore implies the rigorous global lower bound
\[
\boxed{
d\ge
\frac{8048816353827467}{5959000000000000}
=1.3506991699660122\ldots .
}
\tag{7.4}
\]
The diagonal extremizer would have \(d=7/5=1.4\).

There is also an exact link to the first Jacobi coefficients:
\[
\rho_S(Y,U)=-\int_0^1A_t\,dt,
\qquad
\rho_S(X,V)=-\int_0^1\widetilde A_s\,ds.
\tag{7.5}
\]
Indeed \(E[U\mid Y=y]=\int_0^1(1-q_t(y))dt\), and the definition of \(A_t\) gives (7.5).

The adjacent Ansari--Rockel theorem says that each cross copula separately lies in an exact `(xi,rho)` region, with
\[
\xi(Y,U)=6I_1,
\qquad
\xi(X,V)=6I_2.
\tag{7.6}
\]
However, the generic xi-rho region allows the two cross Spearman correlations to have opposite signs and cancel in \(c_\times\). Therefore (7.2) plus the generic exact region does **not** by itself improve (4.20). This is the precise reason B14 does not independently close the conjecture this run.

What B14 does add is a clean global diagnostic for a future near-saturation theorem: scalar-envelope extremizers have coherent orientation, so proving that near-saturation forces the two Brenier-linked orientations to agree on most mass would turn (7.2) into an additional quantitative deficit.

## 8. What moved, what did not, and why this is not closure

Tracked source-valid metric:
\[
\boxed{
U_*:
\frac{580249}{5337500}
\longrightarrow
\frac{1289727882057511}{11918000000000000}.
}
\]
Supported stagnation count on G0013 resets to `0`.

Status remains **PARTIAL / OPEN_CURRENT**. I have **not** proved \(M=1/10\), and I have not proved the equality-case classification required by the source. No restricted shuffle, grid, or scalar-copula statement is being mislabeled as source closure.

The important structural conclusion is now sharper than before:

1. the full scalar `[0,1]` box obstacle is solved exactly;
2. its pointwise optimizers can be assembled into a globally nested uniform-marginal conditional-CDF family, so nesting alone supplies no extra deficit;
3. the first genuinely unused condition is joint Brenier compatibility, concretely the slope-product inequality (6.3) and its global D4/Spearman counterpart (7.2).

This changes the next research target from “improve the one-dimensional obstacle again” to “quantify the unavoidable joint deficit.”

## 9. Exact checker and archive

The finite arithmetic / discretization self-check is

`artifacts/R09/20260917T2031Z_g0013_optimized_penalty_exact.py`

created at commit

`6f110b44f5c90a39dfdc74e4edcf3487d03460f7`.

It was executed before upload. Its archived output is

`artifacts/R09/20260917T2031Z_g0013_optimized_penalty_exact.out`

created at commit

`f8ba35a32b7a27cf874ff015a720c3d0e9e2a2b6`,

and ends

`SELF_CHECK_ONLY / PASS`.

The checker certifies the finite algebra, the 18,432-cell exact rational upper sum, the positive cap margin, the new global constant, and the strict comparison with the previous constant. It is explicitly a self-check, not one of the two independent closure audits.

## 10. Next genuinely different methods

Do **not** repeat B8/B14/B20 next run. The next three methods are:

- **B25 COUNT THE SAME THING TWICE:** express the joint slope-product deficit both in source coordinates `(x,y)` and in level coordinates `(t,s)`; seek an exact double-counting identity for the overlap of the two active conditional ramps.
- **B11 DUALIZE:** formulate the simultaneous `q/r` saturation problem as a two-field convex dual with multiplier for `|q_y r_x|<=1` (or its Hessian form `b^2<=ac`), so that the missing `1/10` gap becomes a dual-certificate problem.
- **B15 BREAK THE SYMMETRY ON PURPOSE:** search asymmetric near-extremizers where one conditional family is close to scalar saturation and the other is not. If every asymmetric attempt pays a definite deficit, the diagonal/antidiagonal equality mechanism becomes visible; if not, it may expose a counterexample to the conjecture.

## 11. Model / scheduler / permission status

The model-control limitation is still present in the interface available to this run. The scheduler update schema exposes title, prompt, schedule, timing mode, and enabled state; it exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Thus GPT-6 / maximum remains prompt text only and cannot honestly be asserted here. This run identifies as GPT-5.6 Sol; reasoning effort remains UNVERIFIED.

There is one important correction to older wording about P26. Current root `RESULTS.md` records that P26's full prompt update **did succeed in one authorized context**, while historical probes in another context returned `You cannot modify this task`. Therefore the permission error is context/ownership dependent, not proof that P26 is globally immutable. The lawful workaround remains to use the authorized owning context, an ownership/admin transfer, or platform support. No scheduler modification, permission bypass, duplicate task, email, Drive action, public posting, purchase, or workflow execution was attempted in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R09
  allocation: CLOSABLE_OUTSIDE
  active_claim: G0013
  source: "Catalano--Lavenant, arXiv:2510.06034, Remark 3"
  source_status: OPEN_CURRENT
  status: PARTIAL
  metric_name: U_star_global_upper_bound_on_M
  before: "580249/5337500 = 0.108711756440281..."
  after: "1289727882057511/11918000000000000 = 0.10821680500566462..."
  movement: true
  strict_improvement: "2518800921442803/5088986000000000000 = 0.0004949514346164055..."
  conjectured_target: "1/10"
  remaining_gap: "97927882057511/11918000000000000 = 0.008216805005664626..."
  supported_unchanged_count: 0
  methods_used: [8, 14, 20]
  new_structural_results:
    - "optimized rational scalar penalty k=6137/775 with exact monotone tail envelope"
    - "pointwise scalar extremizers glue into a nested uniform-marginal conditional-CDF family"
    - "joint Brenier slope product q_y*r_x=b^2/(ac) in [0,1]"
    - "D4 Brenier monotonicity gives direct Spearman sum >= absolute cross Spearman sum"
  checker:
    source: "artifacts/R09/20260917T2031Z_g0013_optimized_penalty_exact.py"
    source_commit: "6f110b44f5c90a39dfdc74e4edcf3487d03460f7"
    output: "artifacts/R09/20260917T2031Z_g0013_optimized_penalty_exact.out"
    output_commit: "f8ba35a32b7a27cf874ff015a720c3d0e9e2a2b6"
    verdict: "SELF_CHECK_ONLY / PASS"
  predecessor_tang:
    status: RETIRED_FROZEN
    metric: UNBOUNDED_ABOVE
    supported_retirement_count: 6
  predecessor_g0002:
    status: HANDED_OFF
    metric: Delta_8=UNMEASURED
  shared_roots_edited: false
  next_methods: [25, 11, 15]
```

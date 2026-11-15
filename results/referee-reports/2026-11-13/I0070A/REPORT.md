PROVED

# I0070 — Time regularization in Hilbert spaces

13 November 2026. The extension holds under the other hypotheses of Theorem 5.7. The proof below uses local cutoffs and higher unweighted maximal regularity; it avoids the endpoint weight. In fact the extra growth hypothesis (5.21) is not needed in this Hilbert case. This is a proof developed here, not a claim of a printed resolution.

## Source, version, and pagination

Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, **Nonlinear Differential Equations and Applications NoDEA 32** (2025), issue 6, article 123, **150 pages**, published online 1 September 2025, DOI [10.1007/s00030-025-01090-2](https://doi.org/10.1007/s00030-025-01090-2). The version of record is saved, as extracted text only, in `sources/survey_published.txt`. Throughout this report, survey page numbers refer to its printed “Page ... of 150” numbering, which agrees with the PDF page index. Theorem 5.7 and its proof are on **pp. 59–60**; Assumption 4.1 on **pp. 38–39**, Theorem 4.7 on **pp. 42–43**; Assumption 6.1 and (6.1) on **pp. 64–65**; Problem 6 on **p. 130**.

The corresponding preprint is [arXiv:2501.18561v5](https://arxiv.org/abs/2501.18561v5), submitted 30 January 2025, version 5 dated **27 August 2025**. Its 103-page layout differs from the published layout; it is saved separately as `sources/survey_v5.txt`. In v5, Theorem 5.7 is on p. 42 (proof continuing on p. 43), (6.1) is on p. 46, and Problem 6 is on p. 92. No preprint page number is silently substituted for a published one.

Bibliographic correction to the question: Agresti–Veraar Part I appeared in **Nonlinearity 35** (2022), 4100–4210, DOI [10.1088/1361-6544/abd613](https://doi.org/10.1088/1361-6544/abd613). Part II appeared in **J. Evol. Equ. 22** (2022), article 56, 96 pages, DOI [10.1007/s00028-022-00786-7](https://doi.org/10.1007/s00028-022-00786-7). The saved arXiv versions are 2001.00512v5 and 2012.04448v4; Part II's published text is also saved. An initial log entry called the latter preprint v3; inspection of its first page corrected this to **v4**.

## Exact mathematical content of the survey's hypotheses and claim

The following is a mathematical restatement, retaining all parameters and hypotheses rather than a verbatim prose quotation. Write

\[
 X_\theta=[X_0,X_1]_\theta,\qquad
 X_{\theta,q}=(X_0,X_1)_{\theta,q},\qquad
 w_\kappa^a(t)=(t-a)^\kappa,\quad w_\kappa(t)=t^\kappa.
\]

The bracket and parenthesis constructions are complex and real interpolation, respectively. In particular, the second real interpolation index **1** in $X_{\beta_j,1}$, the trace index **p**, and the index **infinity** in (5.21) are distinct. The time spaces are Bochner spaces with measure $t^\kappa\,dt$; $H^{\theta,p}$ is the Bessel potential space, not an assertion of an ordinary time derivative. Work on a filtered probability space with the usual conditions, with a cylindrical Brownian motion $W$ on the noise Hilbert space $\mathcal U$, adapted to that filtration. Initial random variables are strongly $\mathcal F_0$-measurable. $L^0$ means measurability, without a moment assumption.

The equation is (4.1),

\[
 du+Au\,dt=F(u)\,dt+(Bu+G(u))\,dW,\qquad u(0)=u_0.
\tag{E}
\]

The survey's semilinear formulation has coefficients independent of $t,\omega$. The densely and continuously embedded couple $X_1\hookrightarrow X_0$ has $X_0$ UMD of type 2; some $\lambda_0\ge0$ makes $\lambda_0+A$ sectorial on $X_0$, and $X_1=D(A)$, with the domain norm. Also

\[
 A\in\mathcal L(X_1,X_0),\qquad
 B\in\mathcal L(X_1,\gamma(\mathcal U,X_{1/2})),\qquad
 F:X_1\to X_0,\quad G:X_1\to\gamma(\mathcal U,X_{1/2}).
\]

Here $\gamma$ denotes radonifying operators; for Hilbert targets it is the Hilbert–Schmidt class. In the intended endpoint case $X_0$ is Hilbert, hence so is $X_1$ up to an equivalent graph norm, and $X_{1/2,2}=X_{1/2}$ up to equivalent norms.

**Assumption 4.1.** Take

\[
 p\in[2,\infty),\quad \kappa\in[0,p/2-1)\cup\{0\},\quad
 m\in\mathbb N,\quad
 \beta_j\in(1-(1+\kappa)/p,1),\quad \rho_j\ge0.
\]

For each integer $n\ge1$, a constant $L_n>0$ must give, for all $u,v\in X_1$ with both trace norms at most $n$,

\[
\begin{split}
 &\|F(u)-F(v)\|_{X_0}
 +\|G(u)-G(v)\|_{\gamma(\mathcal U,X_{1/2})}\\
 &\quad\le L_n\sum_{j=1}^m
 (1+\|u\|_{X_{\beta_j,1}}^{\rho_j}
     +\|v\|_{X_{\beta_j,1}}^{\rho_j})
 \|u-v\|_{X_{\beta_j,1}},
\end{split}
\tag{A4.1}
\]

where the trace norm is $\|\cdot\|_{X_{1-(1+\kappa)/p,p}}$, and

\[
 \frac{1+\kappa}{p}\le
 \frac{(1+\rho_j)(1-\beta_j)}{\rho_j},\qquad 1\le j\le m.
\tag{4.3}
\]

For $\rho_j=0$, the nonsingular equivalent formulation is

\[
 \rho_j\bigl(\beta_j-1+(1+\kappa)/p\bigr)+\beta_j\le1.
\tag{4.4a}
\]

The pair is critical if equality holds for at least one $j$, and subcritical if all inequalities are strict. Thus saying that just *one* term is subcritical does not remove a different critical term.

**Theorem 4.7, inherited by Theorem 5.7.** In addition to Assumption 4.1, the pair must belong to $\mathcal{SMR}^{\bullet}_{p,\kappa}$. For every

\[
 u_0\in L^0_{\mathcal F_0}(\Omega;X_{1-(1+\kappa)/p,p})
\]

there is a unique maximal local $L^p_\kappa$-solution $(u,\sigma)$, $\sigma>0$ almost surely. For every localizing sequence $\sigma_n\uparrow\sigma$, when $p>2$,

\[
 u\in H^{\theta,p}(0,\sigma_n,t^\kappa dt;X_{1-\theta})
      \cap C([0,\sigma_n];X_{1-(1+\kappa)/p,p}),
 \qquad 0\le\theta<1/2,
\]

almost surely. At positive times one also has (4.9),

\[
 u\in H^{\theta,p}_{\rm loc}((0,\sigma);X_{1-\theta})
       \cap C((0,\sigma);X_{1-1/p,p}).
\]

For $p=2$, the admissible weight is **only $\kappa=0$**, and the theorem states

\[
 u\in L^2(0,\sigma_n;X_1)\cap C([0,\sigma_n];X_{1/2})
 \quad\hbox{almost surely}.
\tag{energy}
\]

The maximal solution means that any other local solution in the specified class agrees up to its lifetime and cannot have a longer lifetime; it is not a global existence assertion. The local solution is progressive, has the displayed integrability and continuity, its nonlinear terms have the required local $L^p_\kappa$ integrability, and the integrated equation holds in $X_0$ along the localizing sequence. No coercivity of the full nonlinear equation is required for this local theorem.

**Meaning of the maximal regularity assumption.** Definitions 3.7–3.8, pp. 27–28, require existence, uniqueness, and the zero-initial-data estimate

\[
 \|v\|_{L^q(\Omega;L^q(a,\tau,w_\alpha^a;X_1))}
 \le C_T\bigl(
 \|f\|_{L^q(\Omega;L^q(a,\tau,w_\alpha^a;X_0))}
 +\|g\|_{L^q(\Omega;L^q(a,\tau,w_\alpha^a;
           \gamma(\mathcal U,X_{1/2})))}\bigr)
\]

for $dv+Av\,dt=f\,dt+(Bv+g)\,dW$, uniformly over $a\in[0,T]$, stopping times $\tau\in[a,T]$, and progressive data. The bullet also requires $H^{\theta,q}(a,b,w_\alpha^a;X_{1-\theta})$ estimates for every $0<\theta<1/2$ on deterministic intervals if $q>2$. For $(q,\alpha)=(2,0)$, the additional requirement is an $L^2(\Omega;C([a,b];X_{1/2}))$ estimate. The constants are uniform over interval endpoints inside a fixed finite horizon. These are estimates for *appropriately integrable input*, not a claim that arbitrary $L^2$ data become $L^q$ data.

**Theorem 5.7, pp. 59–60.** Set **$p\in(2,\infty)$** and **$\kappa=0$** in all the conditions of Theorem 4.7, and let $(u,\sigma)$ be its maximal $L^p_0$-solution. For each $n\ge1$ there must be $C_n>0$ such that, for all $x\in X_1$ with $\|x\|_{X_{1-1/p,\infty}}\le n$,

\[
 \|F(x)\|_{X_0}+\|G(x)\|_{\gamma(\mathcal U,X_{1/2})}
 \le C_n\sum_{j=1}^m
       (1+\|x\|_{X_{\beta_j,1}}^{\rho_j+1}).
\tag{5.21}
\]

The $\beta_j,\rho_j,m$ are those of Assumption 4.1. Further require

\[
 (A,B)\in\mathcal{SMR}^{\bullet}_{r,\alpha}
 \quad\text{for every }r\in(2,\infty),\quad
                   \alpha\in[0,r/2-1).
\tag{all-MR}
\]

Then, almost surely,

\[
 u\in H^{\theta,r}_{\rm loc}((0,\sigma);X_{1-\theta})
       \cap C^{\theta-\varepsilon}_{\rm loc}((0,\sigma);X_{1-\theta}),
 \quad 0\le\theta<1/2,\quad 2\le r<\infty,\quad0<\varepsilon<\theta.
\tag{R}
\]

At $\theta=0$, the Sobolev assertion means local $L^r(X_1)$; the Hölder clause has no admissible $\varepsilon$ there. The assertion is local on compact subintervals of the open random interval $(0,\sigma)$, with no bound at zero or at an explosion time, and no unlocalized moment estimate. The survey explicitly points out that (5.21) is additional: a bound on balls of $X_{1-1/p,p}$ does not imply the same bound on the larger balls of $X_{1-1/p,\infty}$.

**Condition (6.1), p. 65, with its context.** Let $V\hookrightarrow H\hookrightarrow V^*$ be a Gelfand triple of real Hilbert spaces, densely and continuously embedded, using the $H$-inner product as the duality pairing. Here $X_0=V^*, X_1=V$, and

\[
 [V^*,V]_{1/2}=(V^*,V)_{1/2,2}=H,
 \quad V_{\beta,1}=(V^*,V)_{\beta,1}.
\]

Assumption 6.1 requires $A\in\mathcal L(V,V^*)$, $B\in\mathcal L(V,\mathcal L_2(\mathcal U,H))$, and constants $\vartheta>0, M\ge0$ with

\[
 \langle u,Au\rangle-\tfrac12\|Bu\|_{\mathcal L_2(\mathcal U,H)}^2
 \ge\vartheta\|u\|_V^2-M\|u\|_H^2\quad(u\in V).
\]

For each $n\ge1$, it requires a constant $L_n\ge0$ such that, whenever $u,v\in V$ have $H$-norms at most $n$,

\[
\begin{split}
 &\|F(u)-F(v)\|_{V^*}
 +\|G(u)-G(v)\|_{\mathcal L_2(\mathcal U,H)}\\
 &\quad\le L_n\sum_{j=1}^m
 (1+\|u\|_{V_{\beta_j,1}}^{\rho_j}
     +\|v\|_{V_{\beta_j,1}}^{\rho_j})
       \|u-v\|_{V_{\beta_j,1}},
\end{split}
\]

where $\beta_j\in(1/2,1),\rho_j\ge0$, and exactly

\[
 \boxed{(2\beta_j-1)(\rho_j+1)\le1,
          \qquad j\in\{1,\ldots,m\}.}
\tag{6.1}
\]

It is equivalent to $2\beta_j\le(\rho_j+2)/(\rho_j+1)$ and to (4.3) at $(p,\kappa)=(2,0)$, interpreted via (4.4a) when $\rho_j=0$. Equality is possible only when $\rho_j>0$, and then $\beta_j=(\rho_j+2)/(2(\rho_j+1))$. No further growth bound or monotonicity is included in Assumption 6.1. Linear coercivity gives the endpoint maximal regularity; it does **not** on its own assert (all-MR).

**What extension means.** In Theorem 5.7 replace the initial exponent by $p=2$, retain its other applicable hypotheses, including (all-MR) and (5.21) with $X_{1/2,\infty}$, assume $X_0$ Hilbert, $u_0\in L^0_{\mathcal F_0}(\Omega;X_{1/2})$, and allow equality in (6.1). The requested conclusion is exactly $R$, on the **same spatial scale and the same maximal lifetime** as the endpoint energy solution. This is stronger than (energy), stronger than improving moments of an energy norm, and different from $H^{\theta,r}(X_{1-\delta-\theta})$ with a positive spatial loss $\delta$.

## Proof

The following argument has been checked against the cited linear estimates and blow-up criterion. It uses only unweighted higher-exponent maximal regularity, spatial interpolation, local existence and uniqueness, and the printed trace-limit blow-up criterion. No simulation is used.

### Claim

Suppose $X_0$ is Hilbert, the endpoint $(p,\kappa)=(2,0)$ hypotheses of Theorem 4.7 hold, and (6.1) holds for all $j$, with equality permitted. Suppose also that $(A,B)\in\mathcal{SMR}^{\bullet}_{q,0}$ for an unbounded sequence of finite $q>2$. Then the endpoint maximal solution satisfies (R).

This implies the requested extension, since (all-MR) supplies these unweighted estimates. The proof does not use the additional bound (5.21); in particular it proves the assertion when that bound is retained. It does not assume a self-adjoint principal operator, nonlinear coercivity, or an extrapolated spatial scale.

### 1. Small relative growth on trace balls about domain vectors

Put $E=X_{1/2}=X_{1/2,2}$, with equivalent norms understood. For $a_j=2\beta_j-1\in(0,1)$, reiteration, or Lemma 4.3 of the survey at $p=2$, gives

\[
 \|w\|_{X_{\beta_j,1}}
 \le c_j\|w\|_E^{1-a_j}\|w\|_{X_1}^{a_j},
 \qquad w\in X_1.
\tag{1}
\]

Fix an integer $N\ge1$ and a desired $\eta>0$. There is a radius $d=d(N,\eta)>0$, $d\le1$, with this property: for **every** $y\in X_1$ with $\|y\|_E\le N$, there is a finite $C_y\ge0$ such that

\[
 \|F(y+w)-F(y)\|_{X_0}
 +\|G(y+w)-G(y)\|_{\gamma(\mathcal U,E)}
 \le \eta\|w\|_{X_1}+C_y
 \quad\text{if }\|w\|_E\le2d.
\tag{2}
\]

The radius is independent of the $X_1$-norm of $y$; the additive constant need not be.

Indeed, use (A4.1) for (y+w,y), whose $E$-norms are at most (N+2). The triangle inequality and the elementary inequality $(s+t)^\rho\le c_\rho(s^\rho+t^\rho)$, for $\rho\ge0$, bound the left side by

\[
 C_N\sum_j\left[
   (1+\|y\|_{X_{\beta_j,1}}^{\rho_j})
           \|w\|_{X_{\beta_j,1}}
       +\|w\|_{X_{\beta_j,1}}^{\rho_j+1}\right].
\tag{3}
\]

The first summands have $X_1$-exponent $a_j<1$ after (1); Young's inequality makes each at most an arbitrarily small multiple of $\|w\|_{X_1}$ plus a finite constant depending on $y$. The last summand is bounded by

\[
 c_j^{\rho_j+1}
 \|w\|_E^{(1-a_j)(\rho_j+1)}
 \|w\|_{X_1}^{a_j(\rho_j+1)}.
\tag{4}
\]

If (6.1) is strict, its top-norm exponent is below one, so Young's inequality applies again. If equality holds, then

\[
 a_j(\rho_j+1)=1,\qquad
 (1-a_j)(\rho_j+1)=\rho_j>0,
\]

and (4) is at most $c_j^{\rho_j+1}(2d)^{\rho_j}\|w\|_{X_1}$. Choose $d$ small enough for the finitely many critical terms, then allocate the remaining small coefficients to the subcritical terms and the first summands. This proves (2). The constants multiplying the critical powers depend on $N$, the fixed exponents, and the couple, but not on $y$. This proves the required uniformity of the radius.

### 2. Cutoff equations have higher time integrability throughout a fixed horizon

Fix $T<\infty$ and a finite $q>2$ for which

\[
 a:=1-1/q>\max_j\beta_j,
 \qquad (A,B)\in\mathcal{SMR}^{\bullet}_{q,0}.
\tag{5}
\]

An unbounded sequence of admissible $q$'s supplies arbitrarily large such choices. Set $E_q=X_{a,q}$. Since $a>\beta_j$,

\[
 E_q\hookrightarrow X_{\beta_j,1},\qquad E_q\hookrightarrow E.
\tag{6}
\]

Choose a scalar Lipschitz function $\chi:[0,\infty)\to[0,1]$ which equals one on $[0,1]$ and zero on $[2,\infty)$. For a domain vector $y$ as in Step 1, define on $X_1$

\[
\begin{split}
 F_y(x)&=F(y)+\chi(\|x-y\|_E/d)\,[F(x)-F(y)],\\
 G_y(x)&=G(y)+\chi(\|x-y\|_E/d)\,[G(x)-G(y)].
\end{split}
\tag{7}
\]

They equal the original coefficients on the closed $E$-ball of radius $d$ about $y$. By (2), throughout $X_1$ they satisfy

\[
 \|F_y(x)\|_{X_0}+\|G_y(x)\|_{\gamma(\mathcal U,E)}
 \le \eta\|x\|_{X_1}+K_y,
\tag{8}
\]

where $K_y<\infty$ incorporates $F(y),G(y),C_y,\eta\|y\|_{X_1}$. Where the cutoff vanishes, only the fixed values $F(y),G(y)$ remain.

There is also a local existence theorem for this modified equation at exponent $q$. To check this without an exponent shortcut, (A4.1) and (6) show that $F,G$, initially on $X_1$, are Lipschitz on every bounded subset of $E_q\cap X_1$, with respect to the $E_q$-norm. Their values are bounded there, by comparison with zero. Density of $X_1$ in $E_q$ extends them locally Lipschitz to $E_q$; the same holds for (7). Thus the modified equation satisfies Assumption 4.1 at $(q,0)$, for example by taking **new** parameters

\[
 \rho'=0,\qquad \beta'\in(a,1),
\]

and using $X_{\beta',1}\hookrightarrow E_q$ for its difference norm. This is the nonsingular subcritical case of (4.4a). The cutoff need not preserve the original polynomial Lipschitz exponents; no such preservation is being assumed.

Here is the precise continuation estimate needed. For a deterministic start $s<T$, nonzero-initial-data linear maximal regularity gives a constant $M_{q,T}$, uniform in $s\in[0,T]$, such that

\[
 \|v\|_{L^q(\Omega\times(s,T);X_1)}
 \le M_{q,T}\left(
 \|\xi\|_{L^q(\Omega;E_q)}
 +\big\|\,\|f\|_{X_0}+\|g\|_{\gamma(\mathcal U,E)}\,\big\|_{L^q(\Omega\times(s,T))}\right)
\tag{9}
\]

for the linear equation starting at $\xi\in L^q_{\mathcal F_s}(\Omega;E_q)$. The constant absorbs the harmless factor between the sum of the two forcing norms and the norm of their pointwise sum (at most a factor of two). This is the unweighted form of the linear estimates in Part I, Proposition 3.10 (preprint pp. 22–23), and Part II, Proposition 3.9 (published pp. 21–23). Here is also a direct construction that avoids any extra assumption on the principal operator's functional calculus. Choose a positive invertible self-adjoint reference operator $A_*$ on $X_0$ with $D(A_*)=X_1$, as in the proof of survey Theorem 3.13. This exists for every dense Hilbert couple. Let $e(t)=e^{-(t-s)A_*}\xi$; deterministic trace theory gives its $W^{1,q}(X_0)\cap L^q(X_1)$ bound. Solve for $z=v-e$ using zero initial data and forcing
\[
 f+(A_*-A)e,\qquad g+Be.
\]
The drift correction and the noise correction are both required; both are bounded by the trace norm of $\xi$. This gives (9). The bullet time estimate and the stochastic trace embedding give continuity in $E_q$ for the zero-initial-data part; the deterministic extension has that continuity too. These are the same trace estimates used in Proposition 3.11 of the survey and the cited nonzero-initial-data propositions. The reference operator is only an initial-data extension device and is not an extra hypothesis that $A$ itself is self-adjoint. We use finite deterministic horizons throughout, not a uniform-in-$T$ estimate.

Choose $\eta>0$ in Step 1 so small that $M_{q,T}\eta\le1/2$. Let $(v,\tau)$ be the maximal $L^q_0$-solution of the modified equation. First suppose $\xi\in L^q(\Omega;E_q)$. Stop along $\tau_n\uparrow\tau\wedge T$ so that $v$ has a bounded $L^q(s,\tau_n;X_1)$-norm; intersect with a usual localizing sequence. Define

\[
 f_n=\mathbf1_{[s,\tau_n]}F_y(v),\qquad
 g_n=\mathbf1_{[s,\tau_n]}G_y(v).
\]

These have finite $L^q(\Omega\times dt)$-norms by (8) and the stopping. Solve the linear equation on all of $[s,T]$ with initial value $\xi$ and forcing $f_n,g_n$, calling its solution $V_n$. Linear uniqueness yields $V_n=v$ up to $\tau_n$. Therefore (8)–(9), using the product forcing norm in (9), which is bounded by (8) and Minkowski, give

\[
\begin{split}
 \|v\|_{L^q(\Omega\times(s,\tau_n);X_1)}
 &\le M_{q,T}\left(
 \|\xi\|_{L^q(\Omega;E_q)}
 +K_yT^{1/q}
 +\eta\|v\|_{L^q(\Omega\times(s,\tau_n);X_1)}\right),\\
 \|v\|_{L^q(\Omega\times(s,\tau_n);X_1)}
 &\le 2M_{q,T}\left(\|\xi\|_{L^q(\Omega;E_q)}+K_yT^{1/q}\right).
\end{split}
\tag{10}
\]

This is an expectation-space estimate. No pathwise boundedness of a stochastic solution operator is invoked. Monotone convergence/Fatou gives finite $L^q(\Omega\times(s,\tau\wedge T);X_1)$-norm. Equation (8) then gives finite $L^q$-norms of both nonlinear forcings up to $\tau\wedge T$. Extend those forcings by zero beyond $\tau$, and solve the linear equation on $[s,T]$. Its solution $V$ is continuous in $E_q$ and agrees with $v$ before $\tau\wedge T$. On $\{\tau\le T\}$, $v(t)\to V(\tau)$ in $E_q$. **Theorem 5.1(1) of the survey** rules out that finite explosion. This supplies a modified solution on $[s,T]$, with all its $H^{\theta,q}(X_{1-\theta})$ regularity. One could instead use the same small-linear-growth continuation argument as in Part II, Theorem 4.15, but (9)–(10) make the required smallness and the stopping explicit.

For merely measurable initial data in $E_q$, partition into $\mathcal F_s$-events where its norm is bounded, solve with the corresponding bounded initial values, and use local uniqueness to paste. For the application below it is enough to use the bounded initial values separately, so no global moment claim for the original solution is needed.

### 3. Comparison covers every strictly positive time of the endpoint solution

The original endpoint solution satisfies

\[
 u\in C([0,\sigma);E)\cap L^2_{\rm loc}([0,\sigma);X_1).
\tag{11}
\]

By Fubini applied along its localizing sequence, for Lebesgue-almost every deterministic $s>0$, $\mathbf1_{\{s<\sigma\}}u(s)$ is an $X_1$-valued, strongly $\mathcal F_s$-measurable random variable. Choose a **countable dense subset $D$** of this full-measure set of times. The argument does not assume $u(s)\in X_1$ at every rational time. Since $X_1\hookrightarrow E_q$, for $s\in D$ and integer $k\ge1$ the data

\[
 \xi_{s,k,q}
   =\mathbf1_{\Gamma_{s,k,q}}u(s),\qquad
 \Gamma_{s,k,q}
   =\{s<\sigma,\ \|u(s)\|_{E_q}\le k\}\in\mathcal F_s
\tag{12}
\]

are bounded in $E_q$. The indicators in (12) do not require future information.

Use an unbounded countable sequence of exponents satisfying (5), integer (N,T), and a countable collection of centers $y\in X_1$ dense in the relevant $E$-space. For each combination use the cutoff radius from Steps 1–2, which depends on (N,q,T) but not on the high spatial norm of $y$, and construct the modified solutions with data (12). All the comparison and regularity properties can now be imposed on a **single probability-one set**.

Separability of the whole Hilbert space is unnecessary here. If needed, take the deterministic closed separable subspace of $E$ containing the essential ranges of the countably many variables $\mathbf1_{\{t<\sigma\}}u(t)$ at rational $t\ge0$. Continuity implies that every path value before $\sigma$ lies in this subspace outside one null set. Approximate a countable dense set of its points by vectors of $X_1$, obtaining the required countable centers in the ambient $E$. Within a fixed $E$-norm bound $N$ these approximate every path value of norm below $N$; the uniformity of $d(N,\eta)$ in Step 1 is what permits this use of density.

Fix a sample point in the resulting probability-one set, an arbitrary $t\in(0,\sigma)$, and an exponent $q$ under consideration. Choose an integer $T>t$ and an integer $N>\|u(t)\|_E+2$. Choose a center $y$ with $\|y\|_E\le N$ and

\[
 \|u(t)-y\|_E<d(N,q,T)/4.
\]

Continuity in (11) gives a neighborhood of $t$, lying inside $(0,\sigma\wedge T)$, on which $\|u(\cdot)-y\|_E<d/2$. Choose $s\in D$ in that neighborhood with $s<t$, and $b>t$ in the same neighborhood. Choose $k$ large enough that the sample point belongs to $\Gamma_{s,k,q}$. Let $v$ be the corresponding higher-$q$ modified solution from Step 2.

On $\Gamma_{s,k,q}$, the two initial values agree. The $L^q$-solution is an endpoint energy solution on finite intervals: time $L^q(X_1)\hookrightarrow L^2(X_1)$, $C(E_q)\hookrightarrow C(E)$, and the nonlinear forcing has the same inclusion. Stop both solutions at their first exits from the $E$-ball of radius $d$ about $y$, also before $\sigma\wedge T$. In this region the two equations have identical coefficients by (7). Local $L^2$ pathwise uniqueness gives equality up to the first exit. Since the original path remains in the ball of radius $d/2$ on $[s,b]$, continuity and that equality prohibit an earlier exit of the modified solution. Hence $u=v$ on $[s,b]$ on the event in question.

Thus **every** $t\in(0,\sigma)$ has an open neighborhood carrying the higher-$q$ regularity of a modified solution. Finite covering and localization of Bessel potential spaces give

\[
 u\in H^{\theta,q}_{\rm loc}((0,\sigma);X_{1-\theta}),
 \qquad 0\le\theta<1/2,
\tag{13}
\]

for each of the unbounded sequence of $q$'s, on the same lifetime as the original solution. There is no assumption of global existence.

### 4. All exponents and the Hölder conclusion

On a compact time interval, $H^{\theta,q}(X_{1-\theta})\hookrightarrow H^{\theta,r}(X_{1-\theta})$ when $q\ge r\ge2$. Consequently (13) gives all finite $r\ge2$. The assertions can be made simultaneous in $\theta$ by first taking a countable sequence increasing to (1/2), and interpolating those bounds with $L^q(X_1)$. Hilbert-couple interpolation gives exactly the intermediate space $X_{1-\theta}$, so there is no hidden spatial loss in this step.

For $0<\varepsilon<\theta<1/2$, choose one of the admissible $q$'s with $1/q<\varepsilon$. The one-dimensional time Sobolev embedding gives

\[
 H^{\theta,q}(I;X_{1-\theta})
  \hookrightarrow C^{\theta-1/q}(I;X_{1-\theta})
  \hookrightarrow C^{\theta-\varepsilon}(I;X_{1-\theta})
\]

on compact intervals $I\subset(0,\sigma)$. Together with (13), this is $R$. This completes the proof.

## What was checked, and limits of the conclusion

The exponent calculation was derived twice. Starting from interpolation, the top-norm exponent is \((2\beta_j-1)(\rho_j+1)\). Starting instead from (4.3) at \(p=2\), multiplication gives \(2\beta_j(\rho_j+1)\le\rho_j+2\), which gives exactly the same inequality. At equality the remaining trace exponent is \(\rho_j>0\). This positivity supplies the small parameter in (2); the case \(\rho_j=0\) is automatically strictly subcritical.

The stopped estimate was checked in the product norm of the two forcing spaces, with its norm-equivalence factor included in \(M_{q,T}\). Substitution of \(v=e+z\), \(e'=-A_*e\), independently checks the signs of both corrections \(+(A_*-A)e\) and \(+Be\). The continuation argument uses a continuous trace extension and the exact printed Theorem 5.1(1); finiteness of a time integral alone is not asserted to be a blow-up criterion. The comparison uses only adapted initial-data events and stopped local uniqueness. Fubini supplies deterministic regular start times; countability and trace continuity upgrade the conclusion to every positive time.

The source statements were checked in the saved page-separated texts, with the journal and arXiv layouts distinguished. This caught the Part I journal error, the Navier–Stokes pagination discrepancy, the sign typo in survey Remark 5.8(1), the stronger real-interpolation ball in (5.21), and the initial-smoothness hypothesis of Proposition 5.9. The published 2026 temporal-threshold note has different theorem numbering from its preprint: Theorem 1 on p. 372 and Theorem 3 on p. 374. Its journal range is 371–379, although its preprint is eight pages.

The file data/proof_audit.txt records the mathematical checks. The script code/audit_artifacts.py verifies source provenance and page separators, the first-line status, math delimiter balance, and absence of PDFs and image files. Its result is in data/artifact_audit.json. This artifact check does not purport to machine-verify the proof. The manifest data/source_manifest.jsonl records each successfully fetched source's URL, retrieval time, original byte hash, and extracted page count; data/page_index.json locates results in the saved texts. LOG.md records the order of work and corrections. Source files are plain text only. PDF bytes were held in memory for text extraction and never saved as files.

The affirmative result retains the higher-exponent linear maximal regularity assumption of Theorem 5.7. In particular, it is not an unconditional regularity theorem for every coercive critical variational equation satisfying Assumption 6.1 alone. It applies to the autonomous semilinear survey setting. It gives local path regularity on \((0,\sigma)\), without a uniform global moment estimate, a gain at \(t=0\), or the temporal endpoint \(\theta=1/2\). No numerical experiment, simulation, publication, push, or additional agent was used.

## Literature audit completed before the new argument

1. **Agresti–Veraar I.** [arXiv:2001.00512v5](https://arxiv.org/abs/2001.00512v5), 29 April 2022, Theorem 4.8, preprint **pp. 31–32**, and the inherited regularity in Theorem 4.7, p. 31, provide endpoint local existence in the energy class. Proposition 3.10, preprint pp. 22–23, supplies the nonzero-initial-data linear estimates; Proposition 3.12, pp. 23–24, gives the localization identities. They do not state the full critical endpoint bootstrap. Preprint pages are used here because the saved Part I is the author preprint, not the 111-page journal layout.

2. **Agresti–Veraar II.** Theorem 6.3, published **pp. 70–74**, Corollary 6.5, **pp. 74–75**, and Proposition 6.8, **pp. 76–80**, give the main bootstrap mechanisms. In Proposition 6.8, one requires the nonlinearities and linear maximal regularity on a second spatial couple $(Y_0,Y_1)$, with
   \[
    Y_\delta=X_0,\quad Y_1=X_{1-\delta},\quad
    \frac1p=\frac{1+\alpha}{r}+\delta,
    \quad r>2,\quad0\le\alpha<r/2-1.
   \]
   At $p=2$, necessarily $\delta=1/2-(1+\alpha)/r>0$; the result explicitly excludes $p=2,\delta=0$. There are further conditions, including (6.22), the shifted version of Hypothesis $H$, Assumption 4.7 there, and maximal regularity in the shifted couple for $q\in[2,r]$. Its conclusion is $H^{\theta,r}_{\rm loc}(X_{1-\delta-\theta})$ and the corresponding improved trace continuity. Thus this is a substantive critical $p=2$ result under extra structure, with a spatial loss which can be recovered in concrete equations by further arguments; it is not the unrestricted assertion $R$. Theorem 4.15, published **pp. 39–41**, proves global existence under sufficiently small linear growth in the top spatial norm. This estimate will be useful below; it does not itself state an answer to Problem 6.

3. **Portal–Veraar**, *Stochastic maximal regularity for rough time-dependent problems*, Stoch. Partial Differ. Equ. Anal. Comput. **7** (2019), **541–597**, DOI [10.1007/s40072-019-00134-w](https://doi.org/10.1007/s40072-019-00134-w), [arXiv:1810.01183](https://arxiv.org/abs/1810.01183). Theorem 3.9, **pp. 556–559**, transfers suitable deterministic maximal regularity through a reference stochastic operator; Lemma 2.7, **pp. 551–552**, includes fractional time regularity of stochastic integrals at $p=2$. Theorems 4.5 and 5.3, **pp. 569–570 and 574–575**, include $p=q=2,\alpha=0$ in the stated coefficient settings. These give mixed time/space regularity for linear equations when the forcing has the corresponding integrability. They do not upgrade arbitrary critical nonlinear $L^2$ forcing to $L^{2+\epsilon}$ forcing. In particular, boundedness of a linear solution operator on $L^r$ must not be confused with a map from arbitrary $L^2$ input into $L^r$ output.

4. **Classical variational theory.** Krylov–Rozovskii, *Stochastic evolution equations*, original Russian 1979 article, Itogi Nauki i Tekhniki 14, **71–146**, English translation **J. Soviet Math. 16** (1981), **1233–1277**, DOI [10.1007/BF01084893](https://doi.org/10.1007/BF01084893). The English PDF was not accessible through the tested publisher URL; the Russian full-text endpoint returned HTTP 403. Consequently I do not claim a direct reading of an unavailable original or invent original theorem page numbers. The classical result is explicitly reproduced, with attribution to **Theorems II.2.1 and II.2.2**, in Liu–Röckner 2010, Theorem 4.1, preprint **p. 17**. Under monotonicity/coercivity and the corresponding growth conditions it gives a continuous $H$-valued solution with the energy integral and the Itô identity. At quadratic coercivity this is $C(H)\cap L^2(V)$, not the all-$r$ assertion $R$.

5. **Liu–Röckner**, *SPDE in Hilbert space with locally monotone coefficients*, J. Funct. Anal. **259** (2010), **2902–2922**, [arXiv:1005.0632](https://arxiv.org/abs/1005.0632), Definition 1.1 and Theorem 1.1, preprint **pp. 3–4**. Under (H1)–(H4), (1.2), and the stated moment assumptions, the solution is continuous in $H$, belongs to time $L^\alpha(V)$, and satisfies $\mathbb E\sup_t\|u(t)\|_H^p+\mathbb E\int\|u\|_V^\alpha<\infty$. In the nondegenerate quadratic setting $\alpha=2$; increasing that theorem's **moment** exponent $p$ is not time $L^p(V)$ regularization. The book *Stochastic Partial Differential Equations: An Introduction* (2015), DOI [10.1007/978-3-319-22354-4](https://doi.org/10.1007/978-3-319-22354-4), Theorem 4.2.4, is the variational theorem cited for the endpoint linear estimate by Agresti–Veraar's Lemma 4.1. The tested book URLs returned HTML instead of a PDF; its theorem is referenced through the explicit citation in the accessible critical-variational paper, not claimed as directly read.

6. **Agresti–Veraar**, *The critical variational setting for stochastic evolution equations*, Probab. Theory Related Fields **188** (2024), **957–1015**, DOI [10.1007/s00440-023-01249-x](https://doi.org/10.1007/s00440-023-01249-x), [arXiv:2206.00230](https://arxiv.org/abs/2206.00230). Theorem 3.3, **pp. 968–969**, gives the critical local energy solution and an energy blow-up criterion. Theorems 3.4–3.5, **pp. 969–970**, give global energy solutions under their respective coercivity conditions; Theorem 3.8, **p. 971**, gives continuous dependence. Lemma 4.1, **p. 972**, is the linear $L^2(\Omega;C(H))\cap L^2(\Omega\times dt;V)$ estimate. No arbitrary same-scale $L^r(V)$ bootstrap is contained in these statements.

7. **Concrete instantaneous regularization.** Agresti–Veraar, *Stochastic Navier–Stokes equations for turbulent flows in critical spaces*, Commun. Math. Phys. **405** (2024), article 43, 57 pages, DOI [10.1007/s00220-023-04867-7](https://doi.org/10.1007/s00220-023-04867-7), [arXiv:2107.03953](https://arxiv.org/abs/2107.03953). Theorem 2.4 and the proof of Theorem 4.1, **Part $C$, published pp. 34–35**, implement critical $p=q=2$ regularization by moving to a rougher scale, adding weights, then recovering regularity. The survey cites pp. 43–44 for this argument, but those are not the pages of the saved published CMP layout; the actual published Part $C$ starts on p. 34. This is an affirmative result for that concrete equation with its scale-compatible coefficient assumptions; it is not a theorem for every Hilbert couple and every nonlinearity in Problem 6.

8. **Later potential counterexample checked.** Agresti–Veraar, *A note on a threshold for temporal regularity of stochastic PDEs*, [arXiv:2509.07803v3](https://arxiv.org/abs/2509.07803v3), 29 May 2026, 8 pages; also C. R. Math. **364** (2026), 371–379, DOI [10.5802/crmath.833](https://doi.org/10.5802/crmath.833). Theorem 1.1, preprint **p. 2** (published **Theorem 1, p. 372**), says, for positive invertible self-adjoint $A$ on $X$ and constant noise $g=x\in X$,
   \[
    u\in L^2(\Omega;W^{\alpha,2}(0,T;D(A^{1/2})))
      \quad\Longleftrightarrow\quad x\in D(A^\alpha),
       \qquad0\le\alpha<1/2.
   \]
   Theorem 1.3, preprint **pp. 3–4** (published **Theorem 3, p. 374**), translates this into the variational setting. This disproves a stronger energy-domain time-regularity conjecture associated with Breit–Hofmanová. It does **not** disprove $R$: in the variational couple $X_0=V^*,X_1=V$, $R$ uses $X_{1-\theta}$, which is rougher than $V$ when $\theta>0$. Constant noise is also subcritical and has every time integrability exponent. A fabricated critical exponent assigned to a constant nonlinearity would not turn this different regularity failure into a counterexample to Problem 6.

9. **Other later citing work checked.** Agresti, [arXiv:2602.21981v3](https://arxiv.org/abs/2602.21981v3), *Fractal dimension of singular times for SPDEs: Energy bounds, criticality, and weak-strong uniqueness*, 28 October 2026, Lemma 3.11, **pp. 22–23**, assumes the instantaneous regularization property it uses. Agresti–Germ–Veraar, [arXiv:2606.07417v3](https://arxiv.org/abs/2606.07417v3), *An optimal local theory for reaction-diffusion equations driven by non-trace-class noise*, 9 November 2026, Theorem 4.8, **p. 30**, still assumes $p\in(2,\infty)$. Its Theorem 2.12, **p. 15**, is a concrete regularization result within that framework. Its reference to *Stochastic evolution equations in critical spaces*, “in preparation, 2026”, is not an accessible printed resolution. Search queries included the exact Problem 6 wording, “2501.18561” with Hilbert/critical/regularization/Meyers, and author publication lists. No checked printed theorem answers Problem 6; this is a bounded search finding, not a claim of exhaustive knowledge of all literature.


**Fractional time regularity already available at the endpoint.** The energy conclusion is not a claim of complete absence of time smoothness. Lemma 2.7 of Portal–Veraar gives, after localization, \(W^{\theta,2}(X_0)\) regularity for \(0<\theta<1/2\) from the integrated equation. In the Hilbert couple one can obtain the sharper familiar mixed assertion
\[
 u\in H^{\theta,2}(0,\sigma_n;X_{1-\theta}),\qquad0\le\theta<1/2,
\]
by the reference-operator method: choose a positive invertible self-adjoint \(A_*\) on \(X_0\) with \(D(A_*)=X_1\), rewrite the drift forcing as \((A_*-A)u+F(u)\) and the noise forcing as \(Bu+G(u)\), and apply the linear Hilbert-space maximal regularity result (the \(p=2\) case underlying Portal–Veraar's Theorem 3.9). Both forcings have local time \(L^2\) integrability by (6.1) and the energy bounds; localization handles their moments. This does not give higher time integrability in \(X_1\), and \(H^{\theta,2}\) with \(\theta<1/2\) alone gives no positive Hölder exponent in the same \(X_{1-\theta}\) space. The missing conclusion in Problem 6 is the all-\(r\), same-scale assertion (R), not the \(r=2\) mixed Sobolev assertion. Conversely, the 2026 note genuinely rules out a general \(W^{\theta,2}(V)\) assertion even for constant additive noise; the spatial loss in (R) is essential.

## The endpoint obstruction in the printed method

Keeping the trace smoothness unchanged while moving from $p$ to $r>p$ requires

\[
 \frac{1+\alpha}{r}=\frac1p.
\]

At $p=2$ this forces $\alpha=r/2-1$, exactly the excluded endpoint of the admissible weight range. Pointwise interpolation at the critical exponent gives

\[
 \|F(u)\|+\|G(u)\|\lesssim_n 1+\|u\|_{X_1},
 \qquad\|u\|_{X_{1/2}}\le n.
\]

This only gives time $L^2$ from time $L^2(X_1)$. It supplies no strict exponent gain. Theorem 3.13 of the survey, **pp. 31–33**, does ensure all linear maximal regularity exponents for analytic $A$ on a Hilbert space when $B=0$, but that operator boundedness alone does not improve the nonlinear input. For $B\ne0$, endpoint coercivity alone must not be silently promoted to (all-MR).

The survey's Proposition 5.9, **pp. 60–61**, obtains $R$ if the nonlinear growth on bounded $X_{1/2}$-balls is bounded by $C_n(1+\|x\|_{X_1}^{\phi})$, $\phi<1$, **and** $u_0\in L^0_{\mathcal F_0}(\Omega;X_{1/2+\epsilon})$ for some $\epsilon>0$, together with (all-MR). Strict inequality in (6.1) for every term supplies that sublinear top-norm growth. The initial smoothness hypothesis must not be omitted from its printed statement. Also, Remark 5.8(1), p. 60, prints the sign of the spatial shift backwards; p. 57 correctly gives $\delta=1/2-(1+\alpha)/r>0$.

Task: “Open problem I0070.” — session started 2026-11-13 16:21 +04.

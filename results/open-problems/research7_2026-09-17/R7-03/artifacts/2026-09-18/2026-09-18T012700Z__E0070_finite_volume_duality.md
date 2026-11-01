Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning telemetry or binding model/effort selector is exposed.

# E0070 / Björklund Problem 2 — finite-star deformation and a dual boundary-flux proof

Date: 2026-09-18 UTC  
Worker: R7-03 Boundary-Case Research  
Canonical target: E0070  
Source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 2, printed p.24.  
Prior source-level construction: `research7_2026-09-17/R7-03/artifacts/2026-09-18/2026-09-18T003400Z__E0070_star_transposition_solution.md`.

This note gives a second proof architecture for the already-complete source candidate.  It does not change the frozen metric `C_E0070=1`; its purpose is to expose the conservation mechanism behind the star construction and to remove any impression that the proof relies on a delicate choice of the tail `p_n`.

## 1. Recalled construction

Let

\[
X=\mathbb N_0,\qquad
G=\operatorname{Sym}_{\mathrm{fin}}(X),\qquad
H=\operatorname{Stab}_G(0).
\]

For `n>=1` let `tau_n=(0 n)`.  Let `(p_n)_{n>=1}` be any strictly positive probability vector and put

\[
\mu(\tau_n)=p_n,
\qquad \sum_{n\ge1}p_n=1.
\]

Every `tau_n` is an involution, hence `check(mu)=mu`.  The map `gH -> g(0)` identifies `G/H` with `X`.  Under this identification the left convolution operator is the symmetric infinite-star kernel

\[
(Pu)(0)=\sum_{n\ge1}p_nu(n),
\tag{1.1}
\]

and, for `k>=1`,

\[
(Pu)(k)=p_ku(0)+(1-p_k)u(k).
\tag{1.2}
\]

For a source-valid quotient function the center integral is a complex Lebesgue integral, so

\[
\sum_{n\ge1}p_n|u(n)|<\infty.
\tag{1.3}
\]

The preceding artifact proved directly from the leaf equations that every solution of `Pu=u+c` satisfying (1.3) has `c=0` and is constant.  We now recover that conclusion from a finite-volume conservation law.

## 2. B6 — deform to finite star quotients

For `N>=1`, define

\[
S_N:=\sum_{n=1}^N p_n,
\qquad
r_{n,N}:=\frac{p_n}{S_N}\quad(1\le n\le N).
\]

Let

\[
G_N=\operatorname{Sym}(\{0,1,\dots,N\}),
\qquad
H_N=\operatorname{Stab}_{G_N}(0),
\]

and let `mu_N(tau_n)=r_{n,N}`.  Then `G_N/H_N` is the finite star `X_N={0,1,...,N}` and its transition operator is

\[
(P_Nu)(0)=\sum_{n=1}^N r_{n,N}u(n),
\]

\[
(P_Nu)(k)=r_{k,N}u(0)+(1-r_{k,N})u(k).
\]

The matrix of `P_N` is symmetric, hence doubly stochastic.  Therefore for every complex-valued `u` on `X_N`,

\[
\sum_{x\in X_N}(P_Nu)(x)=\sum_{x\in X_N}u(x).
\tag{2.1}
\]

If

\[
P_Nu=u+c
\tag{2.2}
\]

for a constant `c`, summing (2.2) over all `N+1` states and using (2.1) gives

\[
0=(N+1)c,
\]

so `c=0`.  The finite star is irreducible because every `r_{n,N}>0`, and the leaf equation then gives `u(k)=u(0)` for every `k`.  Thus every finite approximant has exact constant-defect rigidity.

The groups satisfy

\[
G=\bigcup_{N\ge1}G_N,
\qquad
H=\bigcup_{N\ge1}H_N
\]

under the natural inclusions, while `r_{n,N}->p_n` for each fixed `n`.  What changes at the limit is precisely that `[G:H]` becomes infinite, as required by Björklund's problem.  The next section identifies the exact boundary term that replaces the finite identity (2.1), so no unjustified limiting argument is needed.

**B6 outcome:** success.  The infinite construction is a direct-limit deformation of finite quotients on which constant-defect rigidity follows from an exact conservation law; the only new issue at infinity is a tail flux.

## 3. B11 — dualize: the exact boundary-flux identity

Put

\[
q_N:=\sum_{n>N}p_n=1-S_N.
\]

### Theorem 3.1 — finite-volume conservation identity

Let `u:X->C` satisfy the source-integrability condition (1.3).  Then for every `N>=0`,

\[
\boxed{
\sum_{x=0}^N\bigl((Pu)(x)-u(x)\bigr)
=
\sum_{n>N}p_n\bigl(u(n)-u(0)\bigr).
}
\tag{3.1}
\]

In particular,

\[
\boxed{
\sum_{x=0}^N\bigl((Pu)(x)-u(x)\bigr)\longrightarrow0.
}
\tag{3.2}
\]

#### Proof

Using (1.1) and (1.2),

\[
\begin{aligned}
\sum_{x=0}^N((Pu)(x)-u(x))
&=\left(\sum_{n\ge1}p_nu(n)-u(0)\right)
 +\sum_{k=1}^N p_k(u(0)-u(k))\\
&=\sum_{n>N}p_nu(n)-(1-S_N)u(0)\\
&=\sum_{n>N}p_n(u(n)-u(0)).
\end{aligned}
\]

This proves (3.1).  By (1.3),

\[
\sum_{n>N}p_n|u(n)|\to0,
\]

and `q_N|u(0)|->0`, hence the right side of (3.1) tends to zero.  This proves (3.2). ∎

### Dual interpretation

Let `chi_N` denote the indicator of `{0,1,...,N}`.  The kernel is symmetric with respect to counting measure:

\[
P(0,n)=p_n=P(n,0),
\]

and all remaining off-diagonal entries vanish.  Consequently (3.1) is exactly the finitely supported duality identity

\[
\langle \chi_N,(P-I)u\rangle
=
\langle (P-I)\chi_N,u\rangle.
\tag{3.3}
\]

The dual defect `(P-I)chi_N` is supported only at the center and the omitted leaves:

\[
(P-I)\chi_N(0)=-q_N,
\qquad
(P-I)\chi_N(n)=p_n\quad(n>N),
\]

and is zero on `1,...,N`.  Thus the entire obstruction to finite conservation is an explicit boundary flux through the omitted tail.

### Corollary 3.2 — constant defects vanish

Suppose in addition that

\[
Pu=u+c
\tag{3.4}
\]

for a constant `c in C`.  Then the left side of (3.1) equals `(N+1)c`.  Therefore

\[
\boxed{
(N+1)c
=
\sum_{n>N}p_n(u(n)-u(0)).
}
\tag{3.5}
\]

The right side tends to zero by source integrability, so necessarily `c=0`.  With `c=0`, the leaf equation (1.2) gives

\[
p_k(u(0)-u(k))=0.
\]

Since `p_k>0`, `u(k)=u(0)` for every `k>=1`.  Hence `u` is constant.

This gives a second complete proof of the analytic core of E0070.  Unlike the first proof, it kills the constant defect before solving the individual leaf equations.

**B11 outcome:** success.  Dualizing against finite-volume indicators reveals a conserved total mass with a tail boundary term that vanishes exactly under the source integrability hypothesis.

## 4. Quantitative version: every nonzero formal defect has linear L1 blowup

For comparison with the dual proof, suppose one formally solves `Pu=u+c` using only the leaf equations, without assuming (1.3).  Then

\[
u(n)=u(0)-\frac{c}{p_n}.
\tag{4.1}
\]

Consequently, for every `N`,

\[
\begin{aligned}
\sum_{n=1}^N p_n|u(n)|
&=\sum_{n=1}^N |p_nu(0)-c|\\
&\ge N|c|-\left(\sum_{n=1}^Np_n\right)|u(0)|\\
&\ge N|c|-|u(0)|.
\end{aligned}
\tag{4.2}
\]

Thus any nonzero constant defect forces at least linear divergence of the truncated center `L1(mu)` cost:

\[
\boxed{
\liminf_{N\to\infty}
\frac1N\sum_{n=1}^N p_n|u(n)|
\ge |c|.
}
\tag{4.3}
\]

The contradiction is therefore quantitatively coercive, not a delicate cancellation argument.

## 5. B24 — identify the extremal/admissible star-support family

The original proof used an arbitrary strictly positive vector `(p_n)`.  We now show that strict positivity is not an artificial strengthening: within the star-transposition support family it is exactly the measured-group admissibility condition.

### Proposition 5.1 — complete classification inside the star family

Let `mu` be any probability measure supported on

\[
\mathcal S=\{\tau_n=(0\ n):n\ge1\}
\]

and write `p_n=mu(tau_n)`.  Then

\[
\boxed{
\operatorname{supp}(\mu)\text{ semigroup-generates }G
\iff
p_n>0\text{ for every }n\ge1.
}
\tag{5.1}
\]

Hence **every** source-admissible probability law supported on the star transpositions solves Björklund Problem 2 with `H=Stab_G(0)`.

#### Proof

If every `p_n>0`, every `tau_n` belongs to `supp(mu)`, and for distinct `i,j`,

\[
\tau_i\tau_j\tau_i=(i\ j).
\]

Thus the semigroup generated by `supp(mu)` contains every finitary transposition and therefore all of `G`.

Conversely, suppose `p_m=0` for some `m`.  Every supported generator `tau_n` with `n\ne m` fixes the point `m`.  Hence every semigroup word in the support fixes `m`.  But `G` contains `tau_m`, which does not fix `m`.  Therefore the support cannot semigroup-generate `G`.

Combining (5.1) with Corollary 3.2 proves the final assertion. ∎

So, inside this natural support class, there is no exceptional tail regime and no fine tuning: the entire admissible infinite-dimensional probability simplex gives the desired quotient.  The explicit choice `p_n=2^{-n}` is merely one convenient point in that simplex.

**B24 outcome:** success.  The construction is robust over the full source-admissible star-support family; the only forbidden boundary faces of the simplex are exactly those on which semigroup generation fails.

## 6. Source normalization remains exact

For a quotient function `u:G/H->C`, let `tilde u(g)=u(gH)`.  Björklund's left quasi-harmonic normalization is

\[
\int_G\widetilde u(sg)\,d\check\mu(s)
=
\widetilde u(g)+
\int_G\widetilde u(s)\,d\check\mu(s).
\tag{6.1}
\]

Because `check(mu)=mu`, this is `Pu=u+c` with

\[
c=\int_G\widetilde u(s)\,d\mu(s)=\sum_{n\ge1}p_nu(n).
\]

Theorem 3.1 and Corollary 3.2 apply directly.  Setting `g=e` in (6.1) also gives `u(H)=0`, so a source-normalized quasi-harmonic solution is actually the zero function.  Ordinary harmonic functions correspond to `c=0` and are constant.

Nothing in the new proof weakens the source scope: unbounded functions are allowed, and the only analytic assumption used is precisely the source's required `mu`-integrability.

## 7. What this run changes and what it does not

New mathematical content:

1. an exact finite-star deformation showing that constant-defect rigidity is already a finite conservation phenomenon;
2. the boundary-flux identity (3.1), giving an independent dual proof of the infinite quotient theorem;
3. the quantitative linear divergence bound (4.2)-(4.3) for every formal nonzero defect;
4. the iff classification (5.1) showing that every measured-group-admissible star-supported law works.

The frozen metric does **not** move because the preceding run had already supplied a complete source-level construction:

\[
\boxed{C_{E0070}:1\to1\quad\text{(no movement).}}
\]

Mathematical status remains **PROVED CANDIDATE / protocol closure open**.  The remaining protocol requirements are external: one actual independent P26 audit and one distinct OTHER-track audit.  This note is an R7-03 self-strengthening and does not count as either audit.

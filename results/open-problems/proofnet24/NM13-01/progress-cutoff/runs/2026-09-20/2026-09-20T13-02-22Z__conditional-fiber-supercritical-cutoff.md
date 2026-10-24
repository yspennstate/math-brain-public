Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — no separately authenticated maximum-effort metadata is exposed.

# NM13-01 / LIVE20 T08 — conditional-fiber transfer beyond the global hidden-information barrier

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run and after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A–C and the explicit degree-20 class below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. The transfer and class are new relative to the repository state read in this run. No publication-priority claim is made.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.

## 0. Short handoff and partner split

The latest complete own report read before this run was

`2026-09-20T12-50-00Z__noncommuting-switched-fiber-cutoff.md`.

That report proved a persistently noncommuting switched-fiber theorem by a pathwise common-gap `L^2` contraction. Its explicit degree-15 class had a growing hidden factor, but the proof still paid the point-mass prefactor `sqrt(|K|)`. It therefore left a concrete obstruction: in a **supercritical noncommuting hidden-information regime**, the global hidden-state `L^2` prefactor can overwhelm the available contraction even though a sharper decomposition might still mix abruptly.

This run attacks that obstruction rather than producing another common-gap example. The new move is to extract an exact growing quotient first and apply `L^2` only to the **conditional residual fiber**. The growing quotient may itself carry the later cutoff front and may be arbitrarily larger than the residual fiber. The voltage acting along that quotient need not normalize the residual refresh walk, and the two corresponding Markov operators may have a commutator bounded away from zero.

The newest relevant P26 report read was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_14-57-03__biregular-line-finite-orbit-green-transfer.md`.

P26 now has a finite-orbit shell Green theorem and a two-state Markov-additive radial clock for line graphs of `(9,3)` Ramanujan bigraphs. That route is covering-space / Green-function / shell-radial. The present route is algebraic and transitivity-specific: exact normal quotients, conditional fibers, voltage holonomy and Dirichlet-form variance decomposition. It does not use P26's shell estimates.

The root `POSTED.md` registry was read. No posted claim is reopened. In particular Salez Problem 2.4 / the Abelian-Cayley product-condition manuscript remains excluded.

## 1. Exact source convention and current primary boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), defines the continuous-time chain by inserting independent mean-one exponential waiting times between discrete jumps. If `T` is the discrete transition matrix, then

\[
P_t=e^{-t}\sum_{k\ge0}\frac{t^kT^k}{k!}=e^{t(T-I)}.
\tag{1.1}
\]

Problem 2.3 in the same source is exactly

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree, and spectral gap bounded away from zero.

Fresh primary-source screening on 20 September 2026 leaves the parent problem open.

* Dylan J. Altschuler, `arXiv:2609.14945`, submitted **14 September 2026**, proves an explicit Gaussian cutoff profile for every fixed-degree **long-range expander** sequence. The same paper proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Thus long-range expansion is not equivalent to Salez's arbitrary spectral-expander hypothesis.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted **6 July 2026**, prove a local-product / non-equilibrium-Poincare cutoff criterion. The checked statement does not derive its non-equilibrium constant from vertex transitivity plus an ordinary fixed spectral gap.
* Tali Kaufman and Alexander Lubotzky, `arXiv:1108.2960`, Theorem 3, prove that for every prime power `q` and every integer `alpha` with `q^alpha>17`, there are `(q+1)`-regular edge-transitive Ramanujan Cayley graphs on `PSL_2(q^alpha)` (and also a `PGL_2` branch). We use the `PSL_2`, `q=5` branch.

The source-level target therefore stays strictly broader than every theorem used below.

## 2. Original problem before/after versus mechanism progress

### Original problem: before

Salez Problem 2.3 was `OPEN`. NM13-01 already contained several bounded-degree vertex-transitive spectral-but-not-LRE cutoff classes. The immediate `12:50` theorem removed persistent noncommuting path ordering as an obstruction when every switched hidden kernel has a common stationary law and a common positive gap, but its point-source estimate retained the global factor `sqrt(|K|)`.

### Original problem: after

Salez Problem 2.3 remains `OPEN`. No theorem here says that an arbitrary vertex-transitive spectral expander has the quotient structure used below.

The restricted source-valid scope is enlarged to a degree-20 Cayley family with all of the following simultaneously:

1. a fixed ordinary spectral gap at least `1/20`;
2. rate-one source-continuous-time cutoff at
   \[
   \boxed{T_j=5\log_5 m_j
   =50\log_5 n_j+O(1)
   =\frac{25}{6}\log_5 N_j+O(1)};
   \tag{2.1}
   \]
3. window
   \[
   \boxed{O(\sqrt{\log N_j})};
   \tag{2.2}
   \]
4. failure of every fixed positive long-range-expansion constant;
5. a nonnormalizing voltage whose growing-quotient operator and residual refresh operator have the size-independent commutator
   \[
   \boxed{\|[K_{\rm volt},K_{\rm ref}]\|_{2\to2}=\frac{\sqrt3}{8}};
   \tag{2.3}
   \]
6. a total hidden space so large that the one-block point-mass `L^2` prefactor is polynomially **growing** at the cutoff front, while the conditional-fiber prefactor is polynomially **decaying**.

Items 5–6 are the mechanism-level movement. They are not a claim that the parent conjecture is solved.

## 3. Conditional-fiber voltage transfer

Let

\[
G=\operatorname{Cay}(\Gamma,S),\qquad |S|=d,
\]

and

\[
L=\operatorname{Cay}(\Lambda,V),\qquad |V|=\ell,
\]

be finite connected undirected Cayley graphs. Let `A` be a finite group, let `W=W^{-1}` be a generating set of size `r`, and write

\[
F=\operatorname{Cay}(A,W),\qquad \operatorname{gap}(F)\ge\eta.
\]

Choose an arbitrary voltage map

\[
\phi:V\to A
\]

satisfying only the inverse compatibility

\[
\phi(v^{-1})=\phi(v)^{-1}.
\tag{3.1}
\]

There is **no** normalization assumption `phi(v) W phi(v)^{-1}=W` and no commutation assumption.

On the direct-product group

\[
\Omega=\Gamma\times\Lambda\times A
\]

take the inverse-closed generating set

\[
\Sigma=
\{(s,e,e):s\in S\}
\cup
\{(e,v,\phi(v)):v\in V\}
\cup
\{(e,e,w):w\in W\}.
\tag{3.2}
\]

Assume the three displayed sets are disjoint; this is automatic in the explicit application. Since `W` generates `A`, voltage can be cancelled inside the fiber and connectivity follows from connectivity of `G,L,F`.

Set

\[
D=d+\ell+r,\qquad
 a=\frac dD,\quad h=\frac\ell D,\quad b=\frac rD.
\tag{3.3}
\]

All continuous-time chains below use Salez's rate-one convention.

### Lemma 3.1 — conditional finite/growing fiber contraction

Fix an arbitrary deterministic sequence of times

\[
0<t_1<\cdots<t_k<t
\]

and arbitrary right translations `R_1,...,R_k` of `A`. Between those times evolve by the continuous-time refresh semigroup

\[
e^{b s(P_W-I)}.
\]

Starting from any density `f_0` with respect to the uniform law `pi_A`, the resulting time-ordered evolution satisfies

\[
\boxed{
\|f_t-1\|_{2,\pi_A}
\le e^{-b\eta t}\|f_0-1\|_{2,\pi_A}.
}
\tag{3.4}
\]

In particular, from a point mass,

\[
\boxed{
\|\mu_t-\pi_A\|_{TV}
\le \frac12\sqrt{|A|-1}\,e^{-b\eta t}.
}
\tag{3.5}
\]

#### Proof

Every right translation is a permutation of `A`, hence preserves the uniform law and is an isometry on `L^2(pi_A)`. On a refresh interval of length `s`, the spectral-gap inequality gives, on mean-zero functions,

\[
\|e^{b s(P_W-I)}g\|_2\le e^{-b\eta s}\|g\|_2.
\]

Multiplying the contraction factors over the intervals gives `e^{-b eta t}` because their lengths sum to `t`; inserting the translation isometries changes no norm. For a point mass, `||f_0-1||_2=sqrt(|A|-1)`, and Cauchy–Schwarz gives TV at most half the `L^2` norm. `QED`

The point is that the translations may be violently nonnormalizing: they do not have to commute with the refresh semigroup.

### Theorem A — exact two-quotient / conditional-fiber TV sandwich

Let `d_G,d_L,d_H` denote worst-start total-variation distances for the source-continuous-time walks on `G,L,H=Cay(Omega,Sigma)`. Then for every `t>=0`,

\[
\boxed{
\max\{d_G(at),d_L(ht)\}
\le d_H(t)
\le d_G(at)+d_L(ht)
+\frac12\sqrt{|A|-1}\,e^{-b\eta t}.
}
\tag{3.6}
\]

#### Proof

Use independent Poisson thinning for the three generator types in (3.2). The first clock has rate `a`, the voltage clock rate `h`, and the refresh clock rate `b`.

The `Gamma` coordinate changes only at the first clock and receives iid uniform labels in `S`. Hence it is exactly the source rate-one walk on `G` run for time `at`.

The `Lambda` coordinate changes only at voltage events and receives iid uniform labels in `V`. Hence it is exactly the source rate-one walk on `L` run for time `ht`.

Moreover, the two quotient coordinates are independent: their clocks and labels arise from disjoint independent thinnings. Therefore their joint law is

\[
\mu^G_{at}\otimes\mu^L_{ht}.
\tag{3.7}
\]

Projection from `Omega` to either quotient cannot increase total variation, giving the lower bound in (3.6).

For the upper bound, condition on the complete voltage-clock path, including all `V` labels. The fiber then receives a deterministic sequence of right-translation kicks

\[
R_{\phi(v_1)},R_{\phi(v_2)},\ldots
\]

at the conditioned voltage times. Independently, its refresh dynamics is the rate-`b` walk with kernel `P_W`. Lemma 3.1 applies pathwise, so every such conditional fiber law is within

\[
\varepsilon_A(t):=rac12\sqrt{|A|-1}e^{-b\eta t}
\]

of `pi_A` in TV.

Replace the conditional fiber law by `pi_A` for each quotient path and average. This changes the joint law by at most `epsilon_A(t)`. After replacement, the endpoint law is exactly

\[
\mu^G_{at}\otimes\mu^L_{ht}\otimes\pi_A.
\]

Finally,

\[
\|\mu^G_{at}\otimes\mu^L_{ht}-\pi_G\otimes\pi_L\|_{TV}
\le d_G(at)+d_L(ht)
\]

by the standard product coupling / triangle inequality. This proves (3.6). `QED`

The theorem is insensitive to all commutators between voltage kicks and refresh dynamics. The only dimension paid in the `L^2` prefactor is the **conditional fiber size `|A|`**, not the growing quotient size `|Lambda|`.

## 4. Spectral-expander transfer

### Theorem B — gap bound

Let

\[
\gamma_G=\operatorname{gap}(G),\qquad
\gamma_L=\operatorname{gap}(L).
\]

Then

\[
\boxed{
\operatorname{gap}(H)
\ge\min\{a\gamma_G,\,h\gamma_L,\,b\eta\}.
}
\tag{4.1}
\]

#### Proof

All stationary laws are uniform. For `f=f(g,l,x)` define its fiber average

\[
\bar f(g,l)=\mathbb E_{x\sim\pi_A}f(g,l,x).
\]

Variance decomposes exactly as

\[
\operatorname{Var}(f)
=\mathbb E_{g,l}\operatorname{Var}_A(f(g,l,\cdot))
+\operatorname{Var}(\bar f).
\tag{4.2}
\]

The refresh contribution to the Dirichlet form is at least

\[
b\eta\,\mathbb E_{g,l}\operatorname{Var}_A(f(g,l,\cdot)).
\tag{4.3}
\]

For a voltage edge `(l,x)->(lv,x phi(v))`, Jensen's inequality and the fact that `x->x phi(v)` permutes `A` give

\[
\mathbb E_x\big(f(g,l,x)-f(g,lv,x\phi(v))\big)^2
\ge
\big(\bar f(g,l)-\bar f(g,lv)\big)^2.
\tag{4.4}
\]

The same averaging inequality is immediate for pure `G` edges. Therefore the sum of the `G` and voltage Dirichlet contributions is at least the Dirichlet form of the quotient kernel

\[
Q_{quot}=aP_G\otimes I+hI\otimes P_L+bI
\]

on `bar f`. Its one-sided gap is

\[
\min\{a\gamma_G,h\gamma_L\},
\]

because its nonconstant eigenmodes have energy

\[
a(1-\lambda_G)+h(1-\lambda_L).
\]

Combining this with (4.2)–(4.3) proves (4.1). `QED`

Thus the voltage class is automatically a spectral-expander class whenever both growing quotients and the residual refresh family have fixed gaps.

## 5. Cutoff corollary and the conditional information budget

Suppose `G_n,L_n` have source-continuous-time cutoff centers/windows

\[
(T^G_n,w^G_n),\qquad (T^L_n,w^L_n),
\]

with `w=o(T)` for each factor. Put

\[
M_n=\max\left\{\frac{T^G_n}{a},\frac{T^L_n}{h}\right\},
\qquad
W_n=\max\left\{\frac{w^G_n}{a},\frac{w^L_n}{h},1\right\}.
\tag{5.1}
\]

### Corollary C — conditional-fiber cutoff transfer

If

\[
\boxed{
 b\eta_nM_n-\frac12\log(|A_n|-1)\longrightarrow+\infty,
}
\tag{5.2}
\]

then `H_n` has cutoff at `M_n` with window `O(W_n)`.

#### Proof

For the lower side, choose a factor attaining the maximum in (5.1). At time `M_n-CW_n` that factor is `C` factor-windows before its cutoff, so the corresponding projection lower bound in (3.6) tends to one as `C->infinity`.

For the upper side, at time `M_n+CW_n` both quotient factors are at least `C` of their own rescaled windows past their centers, hence both terms in the upper bound (3.6) tend to zero as first `n->infinity` and then `C->infinity`. Condition (5.2) makes the residual fiber term already `o(1)` at `M_n`, and it only decreases at later times. `QED`

The conceptual difference from the preceding global hidden-state argument is visible in (5.2): only the information volume of the residual conditional fiber `A_n` is charged. A growing exact quotient may contain much more information and may create the later cutoff front rather than being dissipated before it.

## 6. Explicit persistently noncommuting degree-20 class

We now instantiate the theorem so that the old global hidden-information estimate is not merely suboptimal but asymptotically useless.

For `j` sufficiently large, let

\[
R_j=PSL_2(5^j),\qquad
Q_j=PSL_2(5^{10j}).
\]

By Kaufman–Lubotzky Theorem 3, choose inverse-closed six-element generating sets

\[
S_j\subset R_j,\qquad V_j\subset Q_j
\]

whose Cayley graphs are 6-regular edge-transitive Ramanujan graphs. Let

\[
n_j=|R_j|,\qquad m_j=|Q_j|.
\]

For odd `q`,

\[
|PSL_2(q)|=\frac{q(q^2-1)}2,
\]

so

\[
\log_5 m_j=10\log_5 n_j+O(1),
\qquad
m_j=n_j^{10+o(1)}.
\tag{6.1}
\]

Take a second copy of `R_j` inside the residual fiber and set

\[
A_j=R_j\times S_3.
\]

Write

\[
a=(12),\qquad b=(23),\qquad c=(13)\in S_3.
\]

Give `A_j` the eight-element refresh generating set

\[
W_j=
\{(u,e):u\in S_j\}
\cup
\{(e,a),(e,b)\}.
\tag{6.2}
\]

Finally assign the **constant voltage**

\[
\phi(v)=z:=(e,a)\in A_j
\qquad(v\in V_j).
\tag{6.3}
\]

Because `a=a^{-1}`, (3.1) holds automatically.

The output Cayley graph is

\[
H_j=\operatorname{Cay}(R_j\times Q_j\times A_j,\Sigma_j),
\tag{6.4}
\]

where

\[
\Sigma_j=
\{(s,e,e):s\in S_j\}
\cup
\{(e,v,z):v\in V_j\}
\cup
\{(e,e,w):w\in W_j\}.
\tag{6.5}
\]

It is a simple **20-regular Cayley graph**, hence vertex-transitive.

### 6.1 Residual refresh gap

Let `P_R` be the six-regular Ramanujan kernel on the residual copy of `R_j`, and let

\[
P_{ab}=\frac12(R_a+R_b)
\]

be the two-generator kernel on `S_3`. The Cayley graph `Cay(S_3,{a,b})` is a 6-cycle, with eigenvalues

\[
1,\;\frac12,\;\frac12,\;-\frac12,\;-\frac12,\;-1,
\]

so its one-sided gap is `1/2`.

The normalized refresh kernel on `A_j` is

\[
P_A=\frac34 P_R\otimes I+\frac14 I\otimes P_{ab}.
\tag{6.6}
\]

The degree-six Ramanujan bound gives

\[
\gamma_R\ge1-\frac{2\sqrt5}{6}=\frac{3-\sqrt5}{3}.
\tag{6.7}
\]

Hence

\[
\operatorname{gap}(P_A)
\ge
\min\left\{\frac34\frac{3-\sqrt5}{3},\frac14\frac12\right\}
=\boxed{\frac18}.
\tag{6.8}
\]

### 6.2 Persistent nonnormalization and noncommutation

The voltage does not normalize the refresh set. Indeed

\[
a\{a,b\}a^{-1}=\{a,c\}\ne\{a,b\}.
\tag{6.9}
\]

Thus the normalizing-voltage theorem from the `10:30` run does not apply.

More strongly, right translation by `a` does not commute with the `S_3` refresh kernel. Exact regular-representation algebra gives

\[
\|[R_a,P_{ab}]\|_{2\to2}=\frac{\sqrt3}{2}.
\tag{6.10}
\]

Since the `R_j` part of (6.6) commutes with `R_z=I\otimes R_a`,

\[
\boxed{
\|[R_z,P_A]\|_{2\to2}
=\frac14\frac{\sqrt3}{2}
=\frac{\sqrt3}{8}.
}
\tag{6.11}
\]

The voltage event operator on `Q_j\times A_j` is

\[
K_{\rm volt}=P_{Q_j}\otimes R_z,
\]

whereas refresh is `K_ref=I\otimes P_A`. Because `||P_{Q_j}||_{2->2}=1`,

\[
\boxed{
\|[K_{\rm volt},K_{\rm ref}]\|_{2\to2}=\frac{\sqrt3}{8}
}
\tag{6.12}
\]

for every `j`. The class is therefore not approaching a commuting regime.

There is also nontrivial voltage holonomy. The connected Cayley graph on `PSL_2(5^{10j})` cannot be bipartite: a connected bipartite Cayley graph would give an index-two subgroup, while `PSL_2(q)` is simple for these `q`. Hence it has an odd cycle, and the constant order-two voltage accumulates to `z` around that cycle. In particular the voltage cannot be removed by the natural vertex-gauge transformation that trivializes an exact cocycle.

### 6.3 Fixed spectral gap of the output

Here

\[
D=6+6+8=20,\qquad a=h=\frac3{10},\qquad b=\frac25.
\tag{6.13}
\]

Apply Theorem B, (6.7) and (6.8):

\[
\operatorname{gap}(H_j)
\ge
\min\left\{
\frac3{10}\frac{3-\sqrt5}{3},
\frac3{10}\frac{3-\sqrt5}{3},
\frac25\frac18
\right\}
=\boxed{\frac1{20}}.
\tag{6.14}
\]

Thus `(H_j)` is a bounded-degree vertex-transitive spectral-expander sequence.

## 7. Quantitative cutoff proof

Every degree-six Ramanujan factor is long-range expanding by Altschuler and has the Ramanujan cutoff theorem. In the source rate-one convention its center is

\[
\frac{6}{6-2}\log_5 |V|
=\frac32\log_5|V|
\tag{7.1}
\]

with `O(sqrt(log |V|))` window. The exact Gaussian profile is not needed here.

The first quotient `R_j` runs in `H_j` at rate `3/10`, hence its rescaled center is

\[
\frac{10}{3}\frac32\log_5n_j
=5\log_5n_j.
\tag{7.2}
\]

The second quotient `Q_j` also runs at rate `3/10`, so its rescaled center is

\[
\boxed{T_j=5\log_5m_j}.
\tag{7.3}
\]

By (6.1), the separation between (7.3) and (7.2) is `Theta(log n_j)`, much larger than either square-root logarithmic window. Hence the `Q_j` quotient is the unique late macroscopic front.

It remains to verify that the conditional residual fiber is mixed there. From (6.8) and (6.13),

\[
b\eta=\frac25\frac18=\frac1{20}.
\tag{7.4}
\]

Also

\[
|A_j|=6n_j.
\]

At `t=T_j+O(sqrt(log n_j))`, Lemma 3.1 gives

\[
\begin{aligned}
\log\varepsilon_A(t)
&\le O(1)+\frac12\log n_j-\frac{t}{20}\\
&=\left(\frac12-\frac{5}{2\log 5}\right)\log n_j+o(\log n_j)\\
&=-1.0533373363\ldots\,\log n_j+o(\log n_j),
\end{aligned}
\tag{7.5}
\]

where unadorned logarithms in the exponent are natural. Thus

\[
\varepsilon_A(t)=o(1)
\]

uniformly across every fixed multiple of the `sqrt(log n_j)` window.

Theorem A now sandwiches the full distance between the late `Q_j` quotient and the sum of the two quotient distances plus `o(1)`. The early `R_j` distance is already `o(1)` throughout the late window. Therefore `H_j` cuts off at (7.3) with

\[
\boxed{O(\sqrt{\log m_j})=O(\sqrt{\log N_j})}
\tag{7.6}
\]

window. In fact the late quotient's Gaussian profile transfers after the deterministic time rescaling, but the theorem claimed here only needs the window.

Finally

\[
N_j=|H_j|=n_jm_j(6n_j)=6n_j^2m_j.
\tag{7.7}
\]

Using (6.1),

\[
\log_5N_j=12\log_5n_j+O(1),
\]

and hence

\[
\boxed{
T_j
=50\log_5n_j+O(1)
=\frac{25}{6}\log_5N_j+O(1).
}
\tag{7.8}
\]

This proves the advertised quantitative cutoff theorem.

## 8. The class is not long-range expanding

The output degree is 20, so Altschuler's long-range branching benchmark is `19^r`.

Every output generator changes at most one of the three growing degree-six coordinates (`R_j`, `Q_j`, and the residual `R_j`) by one base edge. The `S_3` coordinate has only six states. Therefore, if an output word has length at most `r`, the sum of the three base-coordinate distances is at most `r`. A degree-six ball of radius `k` has size at most `C 5^k`. Summing over the `O((r+1)^3)` possible distance triples gives the uniform bound

\[
|B_{H_j}(x,r)|
\le C(r+1)^3 5^r.
\tag{8.1}
\]

Take

\[
r_j=\left\lfloor\frac12\log_{19}N_j\right\rfloor.
\]

Then `19^{r_j}=N_j^{1/2+o(1)}<3N_j/4`, while

\[
\frac{|B_{H_j}(x,r_j)|}{19^{r_j}}
\le
(\log N_j)^{O(1)}
N_j^{-\beta+o(1)},
\tag{8.2}
\]

with

\[
\boxed{
\beta=\frac12\left(1-\frac{\log5}{\log19}\right)
=0.2266987151\ldots>0.
}
\tag{8.3}
\]

Thus no fixed positive long-range-expansion constant can hold along this sequence. This is an ordinary spectral-expander cutoff family lying strictly outside Altschuler's hypothesis.

## 9. Obstruction removed: total hidden information is the wrong dimension

The new theorem isolates the exact flaw in the previous one-block hidden-state estimate.

Regard `Q_j x A_j` as one combined hidden state. Its size is

\[
m_j|A_j|=6m_jn_j=m_j^{1.1+o(1)}.
\tag{9.1}
\]

At the true cutoff front `T_j=5 log_5 m_j`, the residual contraction factor from (7.4) is

\[
e^{-T_j/20}
=m_j^{-1/(4\log5)}.
\tag{9.2}
\]

A one-block point-mass `L^2` prefactor based on the entire hidden size would therefore scale as

\[
\sqrt{m_j|A_j|}\,e^{-T_j/20}
=m_j^{\,0.55-1/(4\log5)+o(1)}
=\boxed{m_j^{0.3946662663\ldots+o(1)}}.
\tag{9.3}
\]

It diverges polynomially and is useless.

After extracting and conditioning on the exact `Q_j` quotient, only the residual fiber remains. Since `|A_j|=m_j^{0.1+o(1)}`, the corresponding term is

\[
\sqrt{|A_j|}\,e^{-T_j/20}
=m_j^{\,0.05-1/(4\log5)+o(1)}
=\boxed{m_j^{-0.1053337336\ldots+o(1)}}.
\tag{9.4}
\]

It decays polynomially. Simultaneously the voltage/refresh commutator remains exactly `sqrt(3)/8` by (6.12).

So the mechanism-level conclusion is not merely that one more product graph cuts off. It is:

> **Persistent nonnormalizing/noncommuting hidden dynamics and supercritical total hidden information volume can coexist with cutoff. The relevant `L^2` information budget is conditional on the sharp quotient; charging the entire hidden state can be wrong by a polynomial factor.**

This removes the specific obstruction recorded at `12:50`.

What remains for the general conjecture is structurally narrower. An arbitrary vertex-transitive spectral expander need not display an exact normal quotient carrying a sharp front with a conditionally small/gapped residual fiber. A genuinely general transitivity argument now has to do one of two things:

1. extract an analogous conditional-information decomposition from stabilizer-orbit / representation structure without assuming a pre-existing Cayley quotient; or
2. control the exact stabilizer-quotient likelihood varentropy directly, so that the large quotient information is handled by Salez's information criterion rather than point-mass `L^2`.

That is complementary to P26's Green/shell transfer program.

## 10. Sanity checks

The executed checker

`2026-09-20T13-02-22Z__conditional-fiber-supercritical-check.py`

and archived output

`2026-09-20T13-02-22Z__conditional-fiber-supercritical-check.out`

verify:

* the `S_3` refresh spectrum `1,1/2,1/2,-1/2,-1/2,-1` and gap `1/2`;
* exact nonnormalization `a{a,b}a^{-1}!={a,b}`;
* `||[R_a,P_{ab}]||=sqrt(3)/2` and the residual weighted commutator `sqrt(3)/8`;
* residual refresh gap `1/8` and output gap lower bound `1/20`;
* the center coefficient `25/6` in `log_5 N`;
* the non-LRE exponent `0.2266987151...`;
* the sign reversal between the naive global-hidden `L^2` exponent `+0.3946662663...` and the conditional residual exponent `-0.1053337336...`;
* on a 96-state finite toy voltage lift, exact symmetry/stochasticity, the gap lower bound, and the TV sandwich at six times.

The checker ends `ALL_CHECKS_PASS`. The finite model is a sanity check only; no finite experiment is used as evidence for the asymptotic theorem.

## 11. Durable handoff

Parent source status: **OPEN -> OPEN**.

New restricted result: **CANDIDATE_FULL pending independent review**.

Publication novelty: **UNVERIFIED**.

The immediate next T08 target is no longer “beat the full hidden-state `sqrt(|K|)` prefactor.” That prefactor has now been shown to be the wrong object in a source-valid persistently noncommuting supercritical class. The next useful attack is to seek a canonical conditional quotient inside an arbitrary vertex-transitive expander — most naturally from the root-stabilizer orbit chain or a bounded-dimensional representation block — and prove a conditional varentropy or conditional `L^2` estimate that depends on fiber complexity rather than ambient volume.

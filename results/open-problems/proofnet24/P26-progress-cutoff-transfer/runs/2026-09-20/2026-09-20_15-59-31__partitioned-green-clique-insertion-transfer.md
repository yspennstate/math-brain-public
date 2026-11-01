Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — no separately authenticated effort metadata is exposed.

# P26 / LIVE20 T08 — partitioned Green transfer and cutoff on clique-inserted edge-transitive Ramanujan Cayley graphs

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run; `PARTIAL / OPEN` after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A--D below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded dated search for combinations of `clique-inserted`, `line graph of subdivision`, `Ramanujan`, `random walk`, and `cutoff` found spectral/chemical graph-operation papers but no matching ordinary-SRW cutoff theorem. This is negative evidence only, not a priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff, C28/NM13-01 coordination, and preserved failures

The newest own substantive report read was

`2026-09-20_14-57-03__biregular-line-finite-orbit-green-transfer.md`.

It proved a finite-orbit shell Green transfer and applied it to line graphs of fully Ramanujan `(9,3)` arithmetic bigraphs. Its recorded obstruction was that arbitrary transitivity plus a fixed ordinary spectral gap does not itself provide a small **global** late-shell Green defect. Its proposed next mechanism was positive matrix-valued smoothing across shell types, motivated by slow positive exceptional modes.

The newest relevant historical-C28 successor report read was NM13-01's

`2026-09-20T12-50-00Z__noncommuting-switched-fiber-cutoff.md`.

NM13-01 now owns a complementary algebraic route: common-gap contraction for noncommuting switched hidden kernels, an explicit degree-15 semidirect Cayley class, and a next attack through root-stabilizer representation decomposition. P26 therefore stays on covering-space shells, conditional Green defects and radial clocks. The present run does not use a hidden-fiber factorization or common-gap switching.

Two failed/unproved routes are preserved rather than relabeled as progress: the Ihara/first-repeated-directed-edge tangle argument remains incomplete, and global point-mass heat-kernel `L^2` remains too strong for the parent problem. The positive-exceptional-mode obstruction also remains in general.

The new observation in this run is different from the proposed matrix filter and is decisive for a new class: a finite quotient/color can force **every individual shell to stay macroscopically far from global equilibrium forever**, even though the shell is already Green-small *inside its current quotient cell*. One should condition the Green estimate on the quotient cell and mix the finite quotient separately in exact continuous time.

There is no three-unchanged-run trigger: the preceding run introduced finite-orbit shells and a Markov-additive clock, and the present run changes the transfer quantity itself from global shell Green to quotient-conditioned shell Green.

The root `POSTED.md` exclusion registry was read. In particular, the posted Salez Problem 2.4 Abelian-Cayley/product-condition claim is not reopened.

## 1. Exact source convention and current exact boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), inserts independent mean-one exponential holding times between discrete transitions. Thus for a discrete SRW kernel `P`, the exact convention is

\[
H_t=e^{t(P-I)}=e^{-t}\sum_{j\ge0}\frac{t^jP^j}{j!}.
\tag{1.1}
\]

His Problem 2.3 is exactly

> Prove that all vertex-transitive expanders exhibit cutoff.

The surrounding definition takes an expander sequence to have diverging size, uniformly bounded degree, and one-sided spectral gap bounded away from zero.

The freshly checked 20 September 2026 boundary is still strictly narrower.

* Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves Gaussian-profile cutoff for every fixed-degree **long-range expander** sequence. The same paper proves the strict hierarchy `Ramanujan => long-range => spectral`, with neither converse. Long-range expansion is therefore not synonymous with Salez's spectral-expander hypothesis.
* Francesco Pedrotti--Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a local-product/non-equilibrium-Poincare theorem with window `O(1/gamma_*)`; the checked theorem does not derive the needed `gamma_*` estimate from vertex transitivity plus the ordinary spectral gap alone.
* Lubetzky--Peres, `arXiv:1507.04725`, prove cutoff for every regular Ramanujan graph and give the nonbacktracking spectral decomposition used below.
* Kaufman--Lubotzky, `arXiv:1108.2960`, Theorem 3, construct `(q+1)`-regular edge-transitive Ramanujan Cayley graphs `Cay(G,S)` with `S` a regular orbit of a nonsplit torus `T` of order `q+1`; the `PGL_2` branch is bipartite. We use `q=5`.

## 2. Parent before/after and mechanism-level advance

### Parent before

Salez Problem 2.3 was open. P26 already had several special spectral-but-not-long-range cutoff classes, including the immediately preceding finite-orbit line-graph class. All pointwise shell-Green theorems, however, still required late shells themselves to become close to the **global** uniform law (or to become so after an explicit scalar smoothing step).

### Parent after

Salez Problem 2.3 remains open. The proved source-valid scope is enlarged by a new sequence:

> For the degree-six bipartite edge-transitive Ramanujan Cayley graphs of Kaufman--Lubotzky, the clique-inserted graphs `Y_n=L(Sd(G_n))` are degree-six Cayley spectral expanders, fail every fixed long-range-expansion constant, and ordinary rate-one continuous-time SRW on `Y_n` has an explicit Gaussian cutoff profile.

Writing `N_n=|V(Y_n)|`, the cutoff center is

\[
\boxed{T_n=12\log_5 N_n+O(1)}
\tag{2.1}
\]

with `Theta(sqrt(log N_n))` window, and on the normalization `sqrt(log_5 N_n)` the profile is

\[
\boxed{
 d_{Y_n}\!\left(12\log_5N_n+z\sqrt{\log_5N_n}\right)
 \longrightarrow \Phi\!\left(-\frac{z}{\sqrt{198}}\right).
}
\tag{2.2}
\]

The output one-sided gap is at least

\[
\boxed{
\gamma_Y\ge
\frac23-\frac{\sqrt{10+2\sqrt5}}6
=0.0326289891\ldots>0.
}
\tag{2.3}
\]

### Mechanism-level advance

The reusable theorem is a **partitioned (quotient-conditioned) Green-to-TV transfer**. The lifted endpoint shells need not approach global equilibrium. It is enough that each late shell approaches uniformity inside a finite quotient cell, while the actual quotient coordinate of the continuous-time walk mixes independently on a smaller scale.

This is not a cosmetic relaxation in the application: every shell is supported on one bipartition-tail color, so for every radius

\[
\chi^2(\nu_r\Vert\pi)\ge1,
\qquad
\|\nu_r-\pi\|_{TV}\ge\frac12.
\tag{2.4}
\]

Thus the previous pointwise **global** shell criterion cannot have a vanishing error on this class. The new conditional criterion does.

## 3. Theorem A — quotient-conditioned shell Green transfer

Let `Y_n` be a finite transitive regular graph with uniform stationary law `pi_n`. Let

\[
\mathcal C_n=\{C_{n,c}:c\in\mathsf C\}
\]

be a partition into a fixed finite set of cells. Put

\[
\rho_n(c)=\pi_n(C_{n,c}),
\qquad
\pi_{n,c}=\pi_n(\,\cdot\mid C_{n,c}).
\]

Suppose the rate-one continuous-time SRW, started from `x`, has an exact shell/type decomposition

\[
\delta_xH_t
=\sum_{r\ge0}\sum_{\sigma\in\Sigma}
 p_{n,t}(r,\sigma)\,\nu^x_{n,r,\sigma},
\tag{3.1}
\]

where `Sigma` is fixed and every shell law is supported in one cell

\[
\operatorname{supp}(\nu^x_{n,r,\sigma})
\subset C_{n,c(r,\sigma)}.
\tag{3.2}
\]

Let `R_t=r` and let `C_t=c(r,sigma)` on the corresponding summand. Assume that for every `h>=0`,

\[
\sup_x\sup_{\sigma}\sup_{r\ge\ell_n+h}
\chi^2\!\left(
\nu^x_{n,r,\sigma}\middle\|\pi_{n,c(r,\sigma)}
\right)
\le G_n(h),
\tag{3.3}
\]

and that the union of all shell supports with `r<=ell_n-h` lies in a set `A_{n,x}(h)` satisfying

\[
\sup_x\pi_n(A_{n,x}(h))\le L_n(h).
\tag{3.4}
\]

Finally define the quotient mixing error

\[
\alpha_n(t)=\sup_x
\left\|\mathcal L_x(C_t)-\rho_n\right\|_{TV}.
\tag{3.5}
\]

Then for every `t,h>=0`,

\[
\boxed{
\Pr_x(R_t\le\ell_n-h)-L_n(h)
\le d_n(t)
\le
\Pr_x(R_t<\ell_n+h)
+\alpha_n(t)+\frac12\sqrt{G_n(h)}.
}
\tag{3.6}
\]

Here `d_n(t)` is worst-start TV; transitivity makes the start immaterial in the application.

### Proof

The lower bound is unchanged from the ordinary shell squeeze. Let `A=A_{n,x}(h)`. By the support hypothesis,

\[
\delta_xH_t(A)\ge\Pr_x(R_t\le\ell_n-h),
\]

whereas `pi_n(A)<=L_n(h)`. Testing TV against `A` gives the left side of (3.6).

For the upper bound put

\[
q=\Pr_x(R_t<\ell_n+h).
\]

Replace each late shell `nu_{r,sigma}` by its conditional stationary law `pi_{c(r,sigma)}` and replace the early part arbitrarily by the same cellwise stationary mixture. More explicitly, define

\[
\widetilde\mu_t
=\sum_{r,\sigma}p_{n,t}(r,\sigma)
\pi_{n,c(r,\sigma)}.
\tag{3.7}
\]

The early mass costs at most `q` in TV. For every late shell, Cauchy--Schwarz and (3.3) give

\[
\|\nu_{r,\sigma}-\pi_{c(r,\sigma)}\|_{TV}
\le\frac12\sqrt{G_n(h)}.
\]

Convexity therefore yields

\[
\|\delta_xH_t-\widetilde\mu_t\|_{TV}
\le q+\frac12\sqrt{G_n(h)}.
\tag{3.8}
\]

Because the cells are disjoint and the coefficient of `pi_{n,c}` in (3.7) is exactly `Pr(C_t=c)`, one has the exact identity

\[
\|\widetilde\mu_t-\pi_n\|_{TV}
=\left\|\mathcal L(C_t)-\rho_n\right\|_{TV}.
\tag{3.9}
\]

The triangle inequality proves the upper bound. `QED`

### Quantitative profile consequence

Suppose `w_n->infinity`, there exists `h_n=o(w_n)` such that

\[
G_n(h_n)+L_n(h_n)\to0,
\tag{3.10}
\]

and at profile times `T_n+z w_n`,

\[
\alpha_n(T_n+zw_n)\to0.
\tag{3.11}
\]

If the radial front satisfies

\[
\Pr(R_{T_n+zw_n}<\ell_n+o(w_n))\to F(z),
\tag{3.12}
\]

then (3.6) gives

\[
\boxed{d_n(T_n+zw_n)\to F(z).}
\tag{3.13}
\]

There is also an entropy version: if the conditional relative entropy in (3.3) is at most `E_n(h)`, Pinsker replaces the last term by `sqrt(E_n(h)/2)`.

## 4. The clique-inserted graph and its canonical covering geometry

Let `G` be a connected `d`-regular graph. Subdivide every edge once and write `Sd(G)` for the resulting `(d,2)`-biregular graph. Define

\[
Y=L(Sd(G)).
\tag{4.1}
\]

A vertex of `Y` is an incidence between a base vertex and a base edge, hence canonically a directed arc `(v,w)` of `G`. Two arcs are adjacent precisely when either

1. they have the same tail and different heads,
   \[
   (v,w)\sim(v,w'),\qquad w'\ne w,
   \tag{4.2}
   \]
   giving `d-1` **clique moves**, or
2. one is the reversal of the other,
   \[
   (v,w)\sim(w,v),
   \tag{4.3}
   \]
   giving one **reversal move**.

Thus `Y` is `d`-regular.

Let `T_d->G` be the universal tree cover. Subdivision followed by taking a line graph induces a genuine graph cover

\[
Z_d:=L(Sd(T_d))\longrightarrow Y,
\tag{4.4}
\]

because incident edges at each endpoint are carried bijectively by a graph cover. We use `Z_d` as the canonical cover for the walk. It is not a tree—it contains the `d`-cliques corresponding to base vertices—but its root spheres are explicit.

Fix a root arc. A geodesic word in the letters `C` (clique move) and `R` (reversal) cannot contain `CC`, since two clique moves in one tail clique shortcut to one, and cannot contain `RR`, which returns immediately. Hence every geodesic alternates. Writing `q=d-1`,

\[
\boxed{
|\mathcal S_{2m}|=2q^m\quad(m\ge1),
\qquad
|\mathcal S_{2m+1}|=d q^m\quad(m\ge0).
}
\tag{4.5}
\]

In particular

\[
|B_{Z_d}(o,r)|\le C_d q^{r/2}.
\tag{4.6}
\]

If `N=|V(Y)|=d|V(G)|`, the entropic radius is

\[
\boxed{
\ell_N=\log_{\sqrt q}N+O(1)=2\log_qN+O(1).
}
\tag{4.7}
\]

The early-support term in Theorem A therefore satisfies

\[
\boxed{L_N(h)\le C_d q^{-h/2}.}
\tag{4.8}
\]

There are two shell orbits at positive radii, corresponding to which alternating geodesic word occurs. Conditional on radius and orbit type, automorphisms of the rooted regular tree make the lifted walk uniform on that orbit.

## 5. The two shell orbits are base NBRW laws, but only conditionally mix

Let `P_NB` be the normalized directed-edge nonbacktracking kernel of the base `d`-regular graph. Pairing the alternating letters shows the following exact identities.

* `(RC)^m` is an `m`-step base NBRW path from the root arc.
* `(RC)^mR` is the reversal of such an endpoint.
* `(CR)^m` is the reversal of an `m`-step NBRW path from the reversed root arc.
* `(CR)^mC` is an `(m+1)`-step NBRW path from the reversed root arc.

Thus each shell orbit law in (4.4), after projection to `Y`, is an `m`- or `(m+1)`-step directed-edge NBRW endpoint law, possibly followed by the reversal bijection, with

\[
m\ge \lfloor r/2\rfloor-1.
\tag{5.1}
\]

Now assume the base is bipartite. Color an output arc `(v,w)` by the bipartition side containing its tail `v`. An NBRW path alternates tail side deterministically. Hence every shell orbit above is supported in exactly one of the two equal color cells. Consequently, for global uniform `pi_Y`, every shell law satisfies

\[
\boxed{
\|\nu_{r,\sigma}-\pi_Y\|_{TV}\ge\frac12,
\qquad
\chi^2(\nu_{r,\sigma}\Vert\pi_Y)\ge1.
}
\tag{5.2}
\]

This proves that the new partitioned theorem is genuinely doing work: no pointwise global-shell Green estimate can tend to zero.

Suppose further that the base is Ramanujan. Lubetzky--Peres' nonbacktracking spectral decomposition says that, after removing the two trivial periodic modes `+(d-1)` and `-(d-1)` in the bipartite case, every nontrivial `2x2` block has eigenvalues of modulus `sqrt(q)`, with off-diagonal entry uniformly `O_d(q)`, while the additional `+/-1` sectors are smaller. Therefore the normalized NBRW kernel obeys, on the orthocomplement of the two color indicators,

\[
\boxed{
\|P_{NB}^m-\Pi_m\|_{2\to2}
\le C_d(m+1)q^{-m/2},
}
\tag{5.3}
\]

where `Pi_m` maps to the uniform law on the parity/color class accessible at time `m`. This is the bipartite periodic version of the standard Ramanujan NBRW `2`-normal estimate; it follows directly from the same block decomposition because the extra eigenvalue `-q` is absorbed into `Pi_m` rather than treated as error.

Starting from one directed arc, the appropriate color cell has `N/2` states. Hence

\[
\boxed{
\chi^2(P_{NB}^m(e,\cdot)\Vert u_m)
\le C_d N(m+1)^2q^{-m}.
}
\tag{5.4}
\]

Combining (5.1), (5.4), and (4.7), for every shell radius `r>=ell_N+h`,

\[
\boxed{
G_N(h)
\le C_d(\ell_N+h+2)^2q^{-h/2}.
}
\tag{5.5}
\]

Indeed `m>=log_qN+h/2-O(1)`. Taking, for example,

\[
\boxed{h_N=8\log_q\ell_N}
\tag{5.6}
\]

gives

\[
G_N(h_N)+L_N(h_N)=o(1),
\qquad
h_N=O(\log\log N)=o(\sqrt{\log N}).
\tag{5.7}
\]

## 6. The finite quotient mixes exponentially in the exact continuous-time convention

A clique move preserves tail bipartition color and a reversal flips it. There are `d-1` clique neighbors and one reversal neighbor. Thus the discrete quotient kernel is exactly

\[
K_{col}
=\begin{pmatrix}(d-1)/d&1/d\\1/d&(d-1)/d\end{pmatrix},
\tag{6.1}
\]

whose nonconstant eigenvalue is `1-2/d`. Under Salez's exact rate-one semigroup, the nonconstant quotient mode therefore decays as

\[
\exp\{-2t/d\}.
\]

From a fixed color,

\[
\boxed{
\alpha_N(t)=\frac12e^{-2t/d}.
}
\tag{6.2}
\]

At the logarithmic radial mixing time this is polynomially small. This is one point at which the exact continuous-time convention is structurally useful: it automatically randomizes the otherwise deterministic bipartite shell parity through the Poisson number of reversal opportunities.

## 7. Exact Markov-additive radial clock on the clique-inserted tree

The cover `Z_d=L(Sd(T_d))` is the `k=1`, `K=d-1` specialization of a biregular line tree, but we derive the clock explicitly here.

Away from the root there are two shell types `A,B`. In type `A`, the `d` neighbors have radial increments

\[
\{-1:1,\ 0:d-2,\ +1:1\},
\tag{7.1}
\]

while in type `B` they have

\[
\{-1:1,\ +1:d-1\}.
\tag{7.2}
\]

The type transition matrix is

\[
K_{type}
=\frac1d
\begin{pmatrix}d-2&2\\d&0\end{pmatrix},
\tag{7.3}
\]

with stationary law

\[
\pi_A=\frac{d}{d+2},
\qquad
\pi_B=\frac{2}{d+2}.
\tag{7.4}
\]

The one-jump tilted matrix, with `theta` marking radial displacement, is

\[
M_\theta
=\frac1d
\begin{pmatrix}
 d-2&e^{-\theta}+e^\theta\\
 e^{-\theta}+(d-1)e^\theta&0
\end{pmatrix}.
\tag{7.5}
\]

Let `lambda(theta)` be its Perron eigenvalue. For a rate-one Poisson clock, the cumulant exponent per unit **continuous** time is

\[
\lambda(\theta)-1,
\tag{7.6}
\]

not `log lambda(theta)`. Direct differentiation gives

\[
\boxed{
v=\lambda'(0)=\frac{2(d-2)}{d(d+2)},
}
\tag{7.7}
\]

and

\[
\boxed{
\sigma^2=\lambda''(0)
=\frac{4(d^3+2d^2+12d-8)}{d(d+2)^3}.
}
\tag{7.8}
\]

The root is only a finite boundary perturbation. Since `v>0`, for sufficiently small `a>0` one has `lambda(-a)<1`. The positive Perron vector of `M_{-a}` gives an exponential supermartingale outside the boundary region. Optional stopping bounds the probability of descending from radius `r` to the boundary by `C e^{-ar}`, and each departure from the boundary has a fixed positive escape probability. Hence the total number of boundary visits has a geometric tail, and the difference between the actual radial process and the unrestricted Markov-additive process is `O_P(1)`.

The standard finite-state Markov-additive CLT, or equivalently analytic perturbation of `lambda(theta)`, therefore yields

\[
\boxed{
\frac{R_t-vt}{\sqrt{\sigma^2t}}\Longrightarrow N(0,1).
}
\tag{7.9}
\]

Combining (7.9) with Theorem A and (5.7) gives the Gaussian profile at center `ell_N/v`, with window `sqrt(ell_N)` and profile variance parameter

\[
\tau^2=\frac{\sigma^2}{v^3}.
\tag{7.10}
\]

## 8. Output spectrum and a fixed one-sided gap

Let `A_G` be the base adjacency matrix and let `M` be the vertex-edge incidence matrix of `G`. The subdivision graph has biadjacency `M`, and

\[
MM^T=dI+A_G.
\tag{8.1}
\]

If `theta` is a base adjacency eigenvalue, the corresponding singular value obeys `s^2=d+theta`. Let `C` be the unoriented vertex-edge incidence matrix of `Sd(G)`. Since

\[
A_Y=C^TC-2I,
\tag{8.2}
\]

the paired normalized output eigenvalues associated with a nonzero singular sector are

\[
\boxed{
q_\pm(\theta)
=\frac{d-2\pm\sqrt{(d-2)^2+4(d+\theta)}}{2d}
=\frac{d-2\pm\sqrt{d^2+4+4\theta}}{2d}.
}
\tag{8.3}
\]

The rectangular-incidence kernel contributes only `0` modes and the line-incidence kernel contributes the flat mode `-2/d`; neither affects the largest nonconstant eigenvalue. The bipartite base eigenvalue `-d` gives `(d-2)/d` and `0`.

For `d=6`,

\[
q_+(\theta)=\frac13+\frac{\sqrt{10+\theta}}6.
\tag{8.4}
\]

On a degree-six Ramanujan base, every nontrivial eigenvalue other than `-6` satisfies

\[
\theta\le2\sqrt5.
\]

Since `q_+` is increasing,

\[
q_{max}
=\frac13+\frac{\sqrt{10+2\sqrt5}}6,
\]

and therefore

\[
\boxed{
\operatorname{gap}(Y)
\ge
\frac23-\frac{\sqrt{10+2\sqrt5}}6
>0.0326289.
}
\tag{8.5}
\]

Thus the outputs are genuine fixed-degree spectral expanders.

## 9. Theorem D — explicit degree-six Cayley class

Kaufman--Lubotzky Theorem 3 states that for every prime power `q` and suitable extension parameter `alpha`, with

\[
G_\alpha=PGL_2(q^\alpha),
\]

there is a symmetric generating set

\[
S=\{t\gamma t^{-1}:t\in T\},
\qquad |T|=|S|=q+1,
\tag{9.1}
\]

such that `Cay(G_alpha,S)` is `(q+1)`-regular, Ramanujan, edge-transitive and bipartite. Take `q=5`, so the degree is six.

Because the torus `T` has order six and acts transitively on the six generators, it acts **regularly** on `S`. Therefore the semidirect automorphism group

\[
G_\alpha\rtimes T
\tag{9.2}
\]

acts transitively on directed arcs of the Cayley graph: left translation moves the tail, and the torus moves the generator label. Its order is exactly the number of directed arcs, so this action is regular.

Now let

\[
Y_\alpha=L(Sd(Cay(G_\alpha,S))).
\tag{9.3}
\]

The vertices of `Y_alpha` are precisely those directed arcs, and every automorphism of the base acts on incidences. Hence the regular action (9.2) makes `Y_alpha` a **Cayley graph**. It is six-regular and, by (8.5), has a fixed one-sided spectral gap.

Put

\[
N_\alpha=|V(Y_\alpha)|.
\]

For `d=6,q=5`, (7.7)--(7.8) give

\[
\boxed{v=\frac16,\qquad \sigma^2=\frac{11}{24}.}
\tag{9.4}
\]

Also

\[
\ell_N=2\log_5N+O(1).
\tag{9.5}
\]

Therefore

\[
\boxed{
T_N=\frac{\ell_N}{v}=12\log_5N+O(1).
}
\tag{9.6}
\]

On the natural `sqrt(ell_N)` scale,

\[
\tau^2=\frac{\sigma^2}{v^3}=99.
\tag{9.7}
\]

Since `sqrt(ell_N)=sqrt(2) sqrt(log_5N)(1+o(1))`, the profile on the more conventional `sqrt(log_5N)` time scale is

\[
\boxed{
 d_{Y_\alpha}\!\left(
 12\log_5N_\alpha+z\sqrt{\log_5N_\alpha}
 \right)
 \longrightarrow
 \Phi\!\left(-\frac{z}{\sqrt{198}}\right).
}
\tag{9.8}
\]

This is ordinary simple random walk in Salez's exact rate-one continuous-time convention. The base Ramanujan/NBRW theorem supplies only the conditional shell Green front.

## 10. The outputs are not long-range expanders

The output degree is six, so a degree-six long-range expander has singleton tree benchmark `5^r`. But (4.6) gives, for every quotient ball,

\[
|B_{Y_\alpha}(x,r)|\le C5^{r/2}.
\tag{10.1}
\]

Take

\[
r_\alpha=\left\lfloor\frac12\log_5N_\alpha\right\rfloor.
\]

Then `5^{r_alpha}=O(sqrt(N_alpha))`, so the macroscopic saturation branch of the long-range definition is inactive, while

\[
\frac{|B_{Y_\alpha}(x,r_\alpha)|}{5^{r_\alpha}}
\le C5^{-r_\alpha/2}\longrightarrow0.
\tag{10.2}
\]

Hence no fixed positive long-range-expansion constant can hold. The class is genuinely

\[
\boxed{\text{vertex-transitive spectral expander but not long-range expander}.}
\]

Altschuler's theorem therefore does not apply directly to these outputs.

## 11. Exact sanity checks executed

The exact checker

`2026-09-20_15-59-31__partitioned-green-clique-insertion-check.py`

was executed before archival. It verifies:

1. the exact degree-six output spectral transform and gap lower bound;
2. the two-state radial type kernel and stationary law `(3/4,1/4)`;
3. exact rate-one radial speed `v=1/6`;
4. exact continuous-time variance rate `sigma^2=11/24`;
5. profile parameters `tau^2=99` on `sqrt(ell)` and `198` on `sqrt(log_5N)`;
6. the exact color decay exponent `1/3`;
7. sphere sizes `[1,6,10,30,50,150,250,750,1250]` through radius eight;
8. the full line-of-subdivision spectrum on a finite `K_{6,6}` toy, including rectangular-incidence zero modes and the flat `-2/d` band.

The finite toy is only a sanity check; it is not used to infer the asymptotic theorem. The numerical spectral transform error is `1.11e-15`, and the terminal marker is

`P26_T08_PARTITIONED_GREEN_CLIQUE_INSERTION_EXACT_PASS`.

Checker creation commit: `62bf986a654c061459e5869d27eb018176cb4a73`.
Archived output creation commit: `e679ed71f3b0c20d1bde462cf78654b129240042`.

## 12. Residual obstruction and next attack

This run removes a specific obstruction that global shell criteria misdiagnose: **persistent finite quotient information does not need to be erased inside each shell**. It can be split off exactly, with shell Green measured conditionally and the finite quotient mixed on its own clock. The application makes this strict because the global shell `chi^2` never drops below one.

What remains for the parent is harder. After conditioning on every bounded finite quotient, an arbitrary transitive spectral expander may still have slow **positive** exceptional NBRW modes inside each cell. The present theorem does not manufacture a conditional Green front from transitivity alone.

The next P26 attack is therefore the matrix-filter idea in a sharper quotient-orthogonal form: for a finite shell-type/quotient decomposition, study the vector of conditional likelihood ratios after projecting out the exact quotient stationary subspace, and seek a positive matrix polynomial

\[
A(z)=\sum_{j=0}^{J}A_j z^j,
\qquad A_j\ge0,
\qquad J=o(\sqrt{\log n}),
\tag{12.1}
\]

whose action damps the **positive exceptional quotient-orthogonal sector** while the induced radial smoothing costs only `o(sqrt(log n))`. This remains complementary to NM13-01's root-stabilizer hidden-kernel representation route: P26 acts on long nonbacktracking shell densities, not on a visible-factor/hidden-fiber time evolution.

If this conditional matrix-filter route fails twice, preserve the failures and switch scope as required by LIVE20. No such two-failure trigger has occurred yet.

## 13. ledger_delta

```yaml
ledger_delta:
  parent: T08 Salez arXiv:2508.21055 Problem 2.3
  parent_before: OPEN/PARTIAL
  parent_after: OPEN/PARTIAL
  source_convention: "rate-one continuous time H_t = exp(t(P-I))"
  restricted_status: CANDIDATE_FULL_pending_independent_review
  publication_novelty: UNVERIFIED
  substantive_advances:
    - "partitioned/quotient-conditioned shell Green-to-TV squeeze with explicit quotient-mixing term"
    - "strict example where every global shell has TV >= 1/2 and chi^2 >= 1, but conditional shell Green decays"
    - "exact clique-inserted canonical-cover shell geometry and Markov-additive radial clock"
    - "proved degree-six Cayley spectral-expander class from bipartite edge-transitive Ramanujan Cayley bases"
    - "explicit Gaussian profile: center 12 log_5 N + O(1), variance parameter 198 on sqrt(log_5 N) scale"
    - "proved output gap >= 2/3-sqrt(10+2sqrt(5))/6 and proved non-LRE by sqrt(5) versus 5 branching"
  concrete_application:
    base: "Kaufman-Lubotzky q=5 bipartite edge-transitive Ramanujan Cayley graphs"
    output: "Y=L(Sd(G)), equivalently clique-inserted directed-arc graphs"
    output_degree: 6
    cutoff_center: "12 log_5 N + O(1)"
    window: "Theta(sqrt(log N))"
    profile: "Phi(-z/sqrt(198)) on time offset z sqrt(log_5 N)"
  c28_coordination:
    live_successor: NM13-01
    nm_route: "noncommuting switched hidden kernels / stabilizer representations"
    p26_route: "conditional shell Green / quotient removal / covering radial clocks"
  preserved_failures:
    - "Ihara first-repeat tangle bound remains unproved"
    - "global point-mass heat-kernel L2 remains too stringent"
    - "positive exceptional quotient-orthogonal shell modes remain unresolved"
  not_counted_as_advances:
    - source recovery
    - literature receipts
    - repeated exact checks
    - commit hashes
  next_attack: "positive matrix-valued filtering of quotient-orthogonal conditional shell likelihood ratios"
  checker_commit: 62bf986a654c061459e5869d27eb018176cb4a73
  checker_output_commit: e679ed71f3b0c20d1bde462cf78654b129240042
```

End of complete P26 substantive T08 report.

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.

# NM13-01 / LIVE20 T08 — incidence-strong-product cutoff and a polynomial obstruction to the raw NBRW trace route

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Restricted results in this report:** `CANDIDATE_FULL` pending later independent review.

**Publication novelty:** `UNVERIFIED`. The results below are new to the checked repository state; bounded literature searches did not locate the exact strong-product/line-graph transfer or the polynomial trace obstruction, but this is not a worldwide priority claim.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.
Pre-write master observed before this run's artifact writes: `d0b619ed2756c1eda46198108f011389d2a22f4d`.

## 0. Short continuity handoff and route change

LIVE20 assigns NM13-01 to T08. The pre-LIVE20 P0292 history and terminal handoff remain preserved and untouched.

The newest own substantive report before this run was

`2026-09-20T03-03-00Z__strong-product-nbrw-trace-cutoff.md`.

It proved cutoff for strong squares `G boxtimes G` of suitable transitive LRE bases and, separately, the exact vertex-transitive identity

\[
\chi^2(K_r(x,\cdot)\|\pi)=\sum_{i=2}^N p_r(\lambda_i)^2
\]

for the endpoint law of length-`r` nonbacktracking walk. It proposed as the next route deriving a polylogarithmic bound on this empirical NBRW trace from transitivity plus spectral information.

The newest relevant P26 report available to this run is

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_05-56-17__distance-set-shell-profile-transfer.md`.

P26 now develops same-vertex finite-range distance kernels and shell/profile entropy transfer. This run does **not** redo that route. Instead it uses a transitivity/product-specific conditional-driver decomposition and then tests the previous NM13-01 spectral-trace proposal against the resulting class.

There are two substantive advances:

1. a new source-valid non-LRE transitive cutoff class
   \[
   H_n=G_n\boxtimes L(G_n),
   \]
   with an explicit center and `O(sqrt(log N))` window; and
2. a proof that the raw output-degree NBRW trace criterion from the previous run can fail **polynomially** on an explicit member of this cutoff class. Hence that criterion is sufficient but is not necessary and cannot be deduced from vertex transitivity plus ordinary spectral expansion alone.

The second point is a decisive route correction rather than another attempt to squeeze the same trace estimate.

## 1. Exact source convention and current primary boundary

Fresh primary checks on 20 September 2026 recover the following.

### Salez source

Justin Salez, `arXiv:2508.21055v1`, submitted 28 August 2025, uses the rate-one continuous-time convention

\[
P_t=e^{t(T-I)}=e^{-t}\sum_{k\ge0}\frac{t^kT^k}{k!},
\tag{1.1}
\]

so the number of discrete transitions by time `t` is `Pois(t)`. His Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree, and spectral gaps bounded away from zero.

### Newer primary results

Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves Gaussian-profile cutoff for every fixed-degree fixed-constant long-range-expander sequence. The paper also proves the strict hierarchy

\[
\text{Ramanujan}\Longrightarrow\text{long-range expansion}
\Longrightarrow\text{spectral expansion},
\]

with neither converse. Thus LRE is strictly stronger than the hypothesis of Salez Problem 2.3.

Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove that their local-product / non-equilibrium Poincare condition implies cutoff, with a window controlled by `1/gamma_*`. No checked theorem there derives the needed condition solely from vertex transitivity and an ordinary spectral gap.

For explicit symmetric inputs, Kaufman--Lubotzky, `arXiv:1108.2960`, Theorem 3, construct for each fixed prime power `q` edge-transitive `(q+1)`-regular Ramanujan Cayley families on `PSL_2(q^alpha)` or `PGL_2(q^alpha)`. Their theorem explicitly records the PGL branch as bipartite. For the PSL branch with `q^alpha>17`, simplicity rules out a connected bipartite Cayley graph (a bipartition would give an index-two subgroup), and the Ramanujan bound therefore gives a uniform lower spectral edge as well as the upper gap.

The exact posted Abelian-Cayley Problem-2.4 line is not reopened.

### Bounded novelty check

Repository searches for `strong product`, `line graph`, `G boxtimes L(G)`, and neighboring cutoff constructions recovered the prior strong square, line-graph, Cartesian/tensor, finite-fiber and P26 distance-kernel work, but not the theorem below. Fresh web searches for combinations of `strong product line graph random walk cutoff`, `G boxtimes L(G) cutoff`, and `strong product mixing Ramanujan` recovered general strong-product graph theory but no exact cutoff theorem of this form. This is bounded negative evidence only.

## 2. Original problem before / after

### Before this run

Salez Problem 2.3 was `OPEN`. Positive checked scope included Ramanujan and LRE sequences and the repository's restricted non-LRE constructions: line graphs, truncations, fixed finite/twisted fibers, same-vertex finite-range rewiring, graph squares and strong squares. The newest NM13-01 mechanism reduced one route toward the general conjecture to obtaining a polylogarithmic empirical NBRW spectral trace.

### After this run

Salez Problem 2.3 remains `OPEN`.

The positive theorem scope is enlarged by the following class.

> **Incidence-strong class.** Fix `d>=3`. Let `(G_n)` be connected `d`-regular graphs which are both vertex-transitive and edge-transitive, are fixed-constant long-range expanders, and satisfy a uniform lower spectral edge `lambda_min(P_n)>=-1+eta`. Set
> \[
> H_n=G_n\boxtimes L(G_n).
> \]
> Then `(H_n)` is a bounded-degree vertex-transitive spectral-expander sequence, is not a fixed-constant long-range-expander sequence, and its rate-one continuous-time SRW has total-variation cutoff at
> \[
> \boxed{
> T_n=\frac{2d^2+d-2}{(d-2)(d+1)}\log_{d-1}|V(G_n)|
> }
> \tag{2.1}
> \]
> with window `O(sqrt(log |V(G_n)|))=O(sqrt(log |V(H_n)|))`.

Since

\[
|V(H_n)|=\frac d2 |V(G_n)|^2,
\]

(2.1) is equivalently

\[
T_n=
\frac{2d^2+d-2}{2(d-2)(d+1)}
\log_{d-1}|V(H_n)|+O_d(1).
\tag{2.2}
\]

For the explicit degree-six Kaufman--Lubotzky PSL Ramanujan family,

\[
\deg H_n=76,\qquad |V(H_n)|=3n^2,\qquad
T_n=\frac{19}{7}\log_5 n
=\frac{19}{14}\log_5|V(H_n)|+O(1).
\tag{2.3}
\]

The mechanism-level after-state is stronger: the previous raw NBRW trace condition is proved **not necessary**. For the same explicit degree-76 cutoff class, at the output NBRW entropic scale the trace is at least `c N^kappa` with an explicit `kappa>0.0697`.

## 3. The two factor inputs

Write `n=|V(G)|`, `q=d-1`, and let `P` be SRW on `G`.

### 3.1 Base walk

Under the LRE and lower-edge hypotheses, Altschuler's non-lazy discrete theorem gives cutoff for `P` at

\[
\tau_G=\frac d{d-2}\log_q n
\tag{3.1}
\]

with `Theta(sqrt(log n))` Gaussian window. Only the following consequence is needed below: if

\[
k_n-\tau_G\gg\sqrt{\log n},
\]

then the worst-start discrete TV distance `d_G^{disc}(k_n)` tends to zero.

### 3.2 Line factor

The first NM13-01 LIVE20 report proved, by the exact incidence intertwining, that for

\[
R=\text{SRW on }L(G)
\]

rate-one continuous time has cutoff at

\[
\tau_L=\frac{2(d-1)}{d-2}\log_q n
\tag{3.2}
\]

with `O(sqrt(log n))` window.

For reference, if `C` chooses a uniform endpoint of an edge and `D` chooses a uniform incident edge of a vertex, then

\[
DC=\frac{I+P}{2},
\qquad
R-I=\frac d{d-1}(CD-I).
\tag{3.3}
\]

Thus the visible line spectrum associated with a base normalized eigenvalue `lambda` is

\[
\mu(\lambda)
=\frac{d\lambda+d-2}{2(d-1)},
\tag{3.4}
\]

and the remaining line modes have eigenvalue `-1/(d-1)`.

In particular, if the base one-sided gap is `gamma`, then

\[
\operatorname{gap}(L(G))\ge
b\gamma,
\qquad
b:=\frac d{2(d-1)}.
\tag{3.5}
\]

## 4. A conditional-driver lemma for strong products

This is the new transfer mechanism used in the run.

Let `P` and `R` be transition kernels on finite spaces with stationary laws `pi_P,pi_R`. Fix nonnegative `w_1,w_2,w_3` summing to one and consider

\[
Q=w_1(P\otimes I)+w_2(I\otimes R)+w_3(P\otimes R).
\tag{4.1}
\]

Define marginal jump rates

\[
a_P=w_1+w_3,
\qquad
a_R=w_2+w_3.
\tag{4.2}
\]

Let `d_Q^{ct}(t)` denote worst-start TV for the rate-one continuous chain generated by `Q-I`; define `d_R^{ct}` analogously, and let `d_P^{disc}(k)` be worst-start discrete TV for `P^k`.

### Lemma 4.1 — conditional-driver decoupling

For all `t>=0`,

\[
\boxed{
d_R^{ct}(a_Rt)
\le d_Q^{ct}(t)
\le d_R^{ct}(a_Rt)
 +\mathbf E\,d_P^{disc}(Z_t),
}
\tag{4.3}
\]

where

\[
Z_t\sim\operatorname{Pois}(a_Pt).
\tag{4.4}
\]

The same inequality holds with the roles of `P` and `R` exchanged.

### Proof

Realize the rate-one `Q`-walk with three independent Poisson clocks:

- type `10`, rate `w_1`, applying an independent `P` transition to the first coordinate;
- type `01`, rate `w_2`, applying an independent `R` transition to the second coordinate;
- type `11`, rate `w_3`, applying independent `P` and `R` transitions simultaneously.

The union of the clocks affecting the second coordinate is Poisson of rate `a_R`; hence the second marginal is exactly rate-`a_R` continuous-time `R`. Projection cannot increase TV, which proves the lower bound in (4.3).

For the upper bound, condition on the **entire second-coordinate driver**: the `01/11` event times and types and all `R` transition labels. Let `M` be the resulting number of type-`11` events. Conditional on this driver, the second endpoint is fixed, while all first-coordinate labels at the `11` events remain independent of it. Averaging also over the independent type-`10` clock, the conditional first-coordinate law from `x` is

\[
\nu_M=\delta_x P^M e^{w_1t(P-I)}.
\tag{4.5}
\]

Replace `nu_M` by `pi_P` while leaving the second driver unchanged. TV disintegration and convexity give

\[
\|\mathcal L(X_t,Y_t)-\pi_P\otimes\mathcal L(Y_t)\|_{TV}
\le
\mathbf E\,\|\nu_M-\pi_P\|_{TV}.
\tag{4.6}
\]

If `N_1~Pois(w_1t)` is the independent number of type-`10` events, then

\[
\|\nu_M-\pi_P\|_{TV}
\le\mathbf E[d_P^{disc}(M+N_1)\mid M].
\tag{4.7}
\]

Averaging in `M~Pois(w_3t)` gives `M+N_1~Pois(a_Pt)`. Finally

\[
\|\pi_P\otimes\mathcal L(Y_t)-\pi_P\otimes\pi_R\|_{TV}
=d_R^{ct}(a_Rt),
\]

and the triangle inequality proves (4.3). `QED`

This lemma is useful precisely when the slow coordinate is at its cutoff front while the other coordinate is already macroscopically post-cutoff. It handles the common synchronous clock without pretending that the coordinates are independent.

## 5. Applying Lemma 4.1 to `G boxtimes L(G)`

Let

\[
e:=2(d-1)
\]

be the degree of `L(G)`. The strong product

\[
H=G\boxtimes L(G)
\]

has degree

\[
D=d+e+de=2d^2+d-2.
\tag{5.1}
\]

Its normalized SRW kernel is exactly

\[
Q=rac dD(P\otimes I)
 +\frac eD(I\otimes R)
 +\frac{de}{D}(P\otimes R).
\tag{5.2}
\]

Therefore

\[
a_G=\frac{d(e+1)}D
=\frac{d(2d-1)}D,
\tag{5.3}
\]

\[
a_L=\frac{e(d+1)}D
=\frac{2(d^2-1)}D.
\tag{5.4}
\]

The line coordinate is the slow front. Define

\[
T:=\frac{\tau_L}{a_L}.
\]

Using (3.2) and (5.4),

\[
T=
\frac{2(d-1)}{d-2}\frac{D}{2(d^2-1)}\log_q n
=
\boxed{\frac{D}{(d-2)(d+1)}\log_q n},
\tag{5.5}
\]

which is (2.1).

### Lower half

At

\[
t=T-C\sqrt{\log n},
\]

projection to the line coordinate and (4.3) give

\[
d_H^{ct}(t)
\ge
 d_L^{ct}(a_Lt)
=
 d_L^{ct}(\tau_L-a_LC\sqrt{\log n}).
\]

The line-factor theorem therefore yields

\[
\lim_{C\to\infty}\liminf_{n\to\infty}
 d_H^{ct}(T-C\sqrt{\log n})=1.
\tag{5.6}
\]

### Upper half

At

\[
t=T+C\sqrt{\log n},
\]

Lemma 4.1 gives

\[
d_H^{ct}(t)
\le
 d_L^{ct}(\tau_L+a_LC\sqrt{\log n})
 +\mathbf E\,d_G^{disc}(Z_t),
\tag{5.7}
\]

with `Z_t~Pois(a_Gt)`.

The first term vanishes in the cutoff limit. For the second, compare the mean at the center with the base discrete center (3.1):

\[
a_GT
=
\frac{d(2d-1)}{(d-2)(d+1)}\log_q n
=
\frac{2d-1}{d+1}\,\tau_G.
\tag{5.8}
\]

Since

\[
\frac{2d-1}{d+1}-1=\frac{d-2}{d+1}>0,
\tag{5.9}
\]

the first coordinate is already **Theta(log n)** past its own cutoff when the line coordinate reaches its front. A Poisson lower-tail bound shows that, with probability `1-o(1)`,

\[
Z_t\ge\tau_G+c_d\log n
\]

for some fixed `c_d>0`, uniformly for bounded-below `C`. Since discrete TV is nonincreasing in the number of steps and Altschuler's base profile has only `Theta(sqrt(log n))` width,

\[
\mathbf E\,d_G^{disc}(Z_t)\longrightarrow0.
\tag{5.10}
\]

Hence

\[
\lim_{C\to\infty}\limsup_{n\to\infty}
 d_H^{ct}(T+C\sqrt{\log n})=0.
\tag{5.11}
\]

Equations (5.6) and (5.11) prove cutoff with the asserted `O(sqrt(log n))` window in Salez's source convention.

The argument also shows conceptually why synchronous strong-product jumps are harmless here: they correlate the two clocks, but conditioning on the full slow-factor driver leaves independent first-coordinate labels; by the time the slow factor is critical, that conditional first coordinate is already well mixed.

## 6. Vertex transitivity, spectral expansion and failure of LRE

### 6.1 Vertex transitivity

The base `G` is vertex-transitive. Since it is also edge-transitive, `L(G)` is vertex-transitive. The coordinatewise product of the two transitive automorphism actions is transitive on

\[
V(G)\times E(G)=V(H).
\]

Thus `H` is vertex-transitive.

### 6.2 Uniform spectral gap

Let the base one-sided gap be at least `gamma`. By (3.5), the line gap is at least `b gamma` with

\[
b=\frac d{2(d-1)}.
\]

The Dirichlet form of (5.2) satisfies

\[
\mathcal E_Q
\ge
\frac dD\mathcal E_{P\otimes I}
+
\frac eD\mathcal E_{I\otimes R},
\tag{6.1}
\]

because the `P tensor R` Dirichlet term is nonnegative. Tensorization of variance then gives

\[
\operatorname{gap}(H)
\ge
\min\left\{\frac dD\gamma,
\frac eD b\gamma\right\}.
\]

But `e b=d`, so

\[
\boxed{
\operatorname{gap}(H)\ge\frac dD\gamma.
}
\tag{6.2}
\]

This is a uniform positive constant for fixed `d` and base LRE constant.

### 6.3 Quantitative failure of every fixed LRE constant

Strong-product distance is the maximum of factor distances:

\[
d_H((x,e),(y,f))
=\max\{d_G(x,y),d_{L(G)}(e,f)\}.
\tag{6.3}
\]

Hence balls factor exactly. The universal degree bounds give

\[
|B_G(x,r)|\le C_d(d-1)^r,
\qquad
|B_{L(G)}(e,r)|\le C'_d(d-1)^r.
\tag{6.4}
\]

Therefore

\[
|B_H((x,e),r)|\le C''_d(d-1)^{2r}.
\tag{6.5}
\]

The output degree is `D=2d^2+d-2`, so its tree branching benchmark is

\[
D-1=2d^2+d-3.
\]

For every `d>=3`,

\[
(d-1)^2<D-1.
\tag{6.6}
\]

Taking `r` a fixed positive fraction of `log_{D-1}|V(H)|` in the singleton test from the LRE definition, (6.5)--(6.6) make the ratio to the required `(D-1)^r` growth tend to zero. Thus no fixed positive LRE constant can hold along this output sequence.

This is a genuine source-scope extension beyond Altschuler's hypothesis, not a change of terminology.

## 7. Explicit degree-76 family

Take `q=5` in Kaufman--Lubotzky Theorem 3 and let

\[
G_\alpha=\operatorname{Cay}(PSL_2(5^\alpha),S_\alpha)
\]

along `alpha` with `5^alpha>17`. These are 6-regular Ramanujan Cayley graphs and are edge-transitive. They are vertex-transitive because they are Cayley graphs.

They are nonbipartite: `PSL_2(5^alpha)` is nonabelian simple in this range, while a connected bipartite Cayley graph would yield an index-two subgroup via parity of word length. Thus there is no exceptional `-1` eigenvalue. Ramanujan gives every nontrivial normalized eigenvalue in

\[
\left[-\frac{2\sqrt5}{6},\frac{2\sqrt5}{6}\right],
\]

so the uniform lower-edge hypothesis is satisfied. Altschuler gives LRE because every Ramanujan graph is LRE.

For

\[
H_\alpha=G_\alpha\boxtimes L(G_\alpha),
\]

we have

\[
d=6,\quad e=10,\quad D=76,
\quad N=|V(H_\alpha)|=3n^2.
\]

Formula (5.5) becomes

\[
\boxed{
T_n=\frac{19}{7}\log_5 n
=\frac{19}{14}\log_5N+O(1),
}
\tag{7.1}
\]

with `O(sqrt(log N))` window.

## 8. The previous raw NBRW trace route fails polynomially on this cutoff class

The preceding NM13-01 report proved the following exact identity. If `X` is a `D`-regular vertex-transitive graph with normalized adjacency eigenvalues

\[
1=\theta_1\ge\theta_2\ge\cdots\ge\theta_N,
\]

and `K_r` is the length-`r` NBRW endpoint kernel, then

\[
K_r=p_r(P_X),
\]

where

\[
p_0(z)=1,\quad p_1(z)=z,
\quad p_2(z)=\frac{Dz^2-1}{D-1},
\]

\[
p_r(z)=\frac D{D-1}z\,p_{r-1}(z)
-\frac1{D-1}p_{r-2}(z),
\tag{8.1}
\]

and transitivity makes the collision trace start-independent:

\[
\boxed{
\chi^2(K_r(x,\cdot)\|\pi)
=\sum_{j=2}^N p_r(\theta_j)^2.
}
\tag{8.2}
\]

That report gave a sufficient cutoff criterion requiring this trace to be at most polylogarithmic from the output entropic NBRW radius onward. The new class proves that requirement is far from necessary.

### 8.1 A positive-density visible line sector

Specialize to `d=6`. Let

\[
1=\lambda_1,\lambda_2,\ldots,\lambda_n
\]

be the normalized base eigenvalues. The `n` visible line-graph eigenvalues are, by (3.4),

\[
\mu_i=\frac{3\lambda_i+2}{5}.
\tag{8.3}
\]

Because the base graph is simple and loopless,

\[
\sum_{i=1}^n\lambda_i=\operatorname{tr}P=0,
\]

so

\[
\frac1n\sum_{i=1}^n\mu_i=\frac25.
\tag{8.4}
\]

Also every `mu_i<=1`. If a fraction `f` of the visible eigenvalues is at least `3/8`, then

\[
\frac25
\le f\cdot1+(1-f)\frac38,
\]

hence

\[
f\ge\frac1{25}.
\tag{8.5}
\]

After removing the single trivial mode, for all sufficiently large `n` there are at least `n/50` nontrivial visible modes with

\[
\mu_i\ge\frac38.
\tag{8.6}
\]

### 8.2 These modes stay large in the strong product

For `H=G boxtimes L(G)`, normalized product eigenvalues corresponding to a base eigenvalue `lambda` and line eigenvalue `mu` are

\[
\theta(\lambda,\mu)
=\frac{6\lambda+10\mu+60\lambda\mu}{76}.
\tag{8.7}
\]

Pair the **constant base mode** `lambda=1` with the line modes in (8.6). Then

\[
\theta_i
=\frac{6+70\mu_i}{76}
\ge\frac{6+70(3/8)}{76}
=\boxed{\frac{129}{304}}.
\tag{8.8}
\]

Thus the output has at least `n/50` nontrivial eigenvalues at or above `129/304`.

### 8.3 Exact NBRW-polynomial lower bound

Here `D=76`, so (8.1) has characteristic equation

\[
z^2-\frac{76}{75}\theta z+\frac1{75}=0,
\]

with roots

\[
z_\pm(\theta)
=\frac{76\theta\pm\sqrt{76^2\theta^2-300}}{150}.
\tag{8.9}
\]

At

\[
\theta_0=\frac{129}{304},
\]

we have

\[
76^2\theta_0^2-300=\frac{11841}{16},
\]

and therefore

\[
z_+(\theta_0)
=\frac{129+\sqrt{11841}}{600}
>\frac{129+108}{600}
=\boxed{\frac{79}{200}}.
\tag{8.10}
\]

For `theta in [theta_0,1]`, write

\[
p_r(\theta)=A z_+(\theta)^r+B z_-(\theta)^r.
\]

Since `z_-<z_+<=theta`, the initial conditions give `A>=1` and `B<=0`, with `A+B=1`. Hence

\[
\frac{p_r(\theta)}{z_+(\theta)^r}
=A+B\left(\frac{z_-}{z_+}\right)^r
\ge A+B=1,
\]

so every mode in (8.8) satisfies

\[
p_r(\theta_i)\ge\left(\frac{79}{200}\right)^r.
\tag{8.11}
\]

### 8.4 Polynomial trace at the entropic radius

Let `N=3n^2=|V(H)|` and choose

\[
r_N=\lceil\log_{75}N\rceil.
\]

This is only `O(1)` beyond the canonical degree-76 NBRW entropic radius. From (8.2), (8.6) and (8.11),

\[
\mathcal C_{r_N}(H)
:=\sum_{j=2}^N p_{r_N}(\theta_j)^2
\ge
\frac n{50}\left(\frac{79}{200}\right)^{2r_N}.
\tag{8.12}
\]

Since `r_N<=log_75 N+1` and `n=sqrt(N/3)`, this yields

\[
\boxed{
\mathcal C_{r_N}(H)
\ge c\,N^\kappa,
\qquad
\kappa=rac12+2\log_{75}\left(\frac{79}{200}\right),
}
\tag{8.13}
\]

where

\[
c=\frac{(79/200)^2}{50\sqrt3}>0.
\]

The exponent is rigorously positive because

\[
75\left(\frac{79}{200}\right)^4
=\frac{116850243}{64000000}>1.
\tag{8.14}
\]

Numerically,

\[
\kappa=0.0697176276\ldots.
\tag{8.15}
\]

Thus the exact trace is polynomial, not polylogarithmic, at the output entropic NBRW scale.

### Consequence

The degree-76 sequence in Section 7 is vertex-transitive, is a spectral expander, and has the continuous-time cutoff proved in Sections 4--7, yet it violates the previous raw NBRW trace condition by a polynomial factor. Therefore:

> **The raw output-degree NBRW collision trace is not a necessary cutoff mechanism and cannot be forced by vertex transitivity plus an ordinary spectral gap.**

This removes the precise obstruction/target left by the previous NM13-01 run. The source conjecture needs a criterion stable under product/factor decompositions rather than a universal tree-rate collision bound for the output graph itself.

Conceptually, the failure is informative: the output degree `76` suggests a tree branching factor `75`, but its effective transport is inherited from structured factors with base branching `5`. The large NBRW trace is detecting this excess local/product geometry, not failure of total-variation cutoff.

## 9. Exact sanity check

The run executed exact rational arithmetic before archiving the checker.

Files:

- `2026-09-20T04-22-00Z__incidence_strong_trace_exact.py`
- `2026-09-20T04-22-00Z__incidence_strong_trace_exact.out`

The checker verifies for `d=3,...,9`:

- `D=d+2(d-1)+2d(d-1)`;
- the marginal rates `a_G,a_L`;
- the center identity
  \[
  \tau_L/a_L=D/((d-2)(d+1));
  \]
- strict macroscopic separation of the base cutoff front;
- the gap coefficient `d/D`.

For `d=6` it verifies exactly:

- the visible line-sector mass lower bound `1/25`;
- `theta_0=129/304`;
- discriminant `11841/16`;
- `z_+>79/200`;
- `75(79/200)^4=116850243/64000000>1`;
- `kappa>0`.

The archived output ends

`ALL_EXACT_ALGEBRA_CHECKS_PASS`.

These are sanity checks for the algebraic core; the asymptotic theorem is proved on the page above and is not inferred from finite experimentation.

## 10. What obstruction remains

The parent conjecture is not closed. What remains after this run is sharper than before.

The preceding route asked for a universal polylogarithmic bound on

\[
\sum_{i\ge2}p_r(\lambda_i)^2.
\]

Section 8 proves that such a bound is false even for explicit transitive spectral expanders **with cutoff**. The correct object must therefore quotient out or condition on structured factors/fibers before measuring collision or entropy.

The next attack is to formulate and prove an **automorphism-equivariant conditional entropy/collision criterion** with the following two properties:

1. it is stable under synchronous strong products and the finite-state extensions already constructed by NM13-01; and
2. for a general vertex-transitive graph it can be expressed using stabilizer-orbit (orbital) data rather than an externally supplied product decomposition.

The conditional-driver inequality (4.3) is the first exact model of such a criterion: a slow transitive factor carries the cutoff front while the conditional transverse law is already mixed. The unresolved step is to extract an analogous factor/conditional structure from arbitrary vertex transitivity plus spectral expansion.

## 11. Compact ledger delta

- parent source: Salez `arXiv:2508.21055v1`, Problem 2.3;
- parent status before/after: `OPEN -> OPEN`;
- source-level gain: new non-LRE incidence-strong class `G boxtimes L(G)` with center (2.1) and `O(sqrt(log N))` window;
- explicit example: degree `76`, center `(19/14)log_5 N+O(1)`;
- mechanism gain: conditional-driver TV inequality (4.3), resolving synchronous-clock correlation when cutoff fronts are separated;
- obstruction removed: raw NBRW trace criterion shown non-necessary by the polynomial lower bound (8.13);
- exact checker: PASS;
- restricted theorem label: `CANDIDATE_FULL`, pending later independent review;
- publication novelty: `UNVERIFIED`;
- failed recovery routes this run: `0`;
- next attack: quotient-stable / conditional orbital entropy criterion for arbitrary transitive spectral expanders.

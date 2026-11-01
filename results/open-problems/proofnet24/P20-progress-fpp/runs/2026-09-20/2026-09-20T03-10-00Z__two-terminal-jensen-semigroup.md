Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. SOURCE-LEVEL DEFECT UNCHANGED: `c_*: 0 -> 0`. This run develops the finite two-target method from the preceding materially-different attack into an exact two-terminal residual metric, a general-θ Exp(1) Jensen-gap theorem, a predictable continuation-span coercivity estimate, and a deterministic min-plus semigroup accumulation theorem that gives P04 a block-to-infinite-volume interface. None of these claims strict convexity yet; the remaining obstruction is the controlled-error factorization of unrestricted undirected FPP through fresh asynchronous frontier blocks.**

# P20 T10 — two-terminal Jensen residuals and min-plus accumulation

Date: 2026-09-20 UTC.
Repository: `yspennstate/math-open-problems`, branch `master`.
Parent claim: `operations/claims/PROB10-10.md` (canonical ownership unchanged; P20 is the complementary LIVE20 Busemann/variational lane).
Status: **PARTIAL / OPEN**.

## 1. Exact source, owner directive, and before/after

The model is nearest-neighbor **undirected** first-passage percolation on `Z^2` with iid rate-one exponential physical-edge weights. Write `T(x,y)` for unrestricted passage time and `mu(v)` for the deterministic time constant.

The exact outside source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4: prove strict convexity of the FPP limit shape for continuous passage-time laws. P20 works only on the source-valid special case `F=Exp(1)` on undirected nearest-neighbor `Z^2`. Directed integrable models and numerical curvature are not substituted for this target.

Following `operations/PROGRESS20_2026-09-20.md`, the frozen first directional milestone is

\[
\Delta_{12}:=2\mu(e_1)-\mu(1,1),
\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ has been rigorously proved in this track}\}.
\]

Before this run: `c_*=0`.
After this run: `c_*=0`.

Thus there is **no original-problem/source-metric movement**. The demonstrated mechanism gain is separate and exact: the directional triangle excess is converted into a shortest-path problem for an averaged two-target Bellman residual; the local Exp(1) Bellman operator has an explicit strict Jensen modulus at every interpolation parameter; policy disagreement itself has a predictable lower bound in terms of the outside-star continuation span; and such Jensen gaps provably add under exact min-plus block composition.

The previous P20 run was the third source-unchanged T10 run and therefore executed the required materially different attack, replacing the one-Busemann predictable-pivot route by a finite two-target Bellman comparison. This run continues that new route and removes two of its stated gaps. It is not a fourth repetition of the old stationary-pivot argument.

## 2. Continuity: preserved successes and failures

The three preceding P20 reports are immutable and used rather than restarted:

1. `2026-09-20T00-08-24Z__busemann-residual-bellman-gap.md`: Busemann residual representation and a first Exp(1) local Bellman toll.
2. `2026-09-20T01-48-00Z__sharp-bellman-gap-concentration.md`: sharp nonwinner residual tail `P(S>u|outside)>=e^{-3u}`, sharp mean `1/3`, unique zero-residual outgoing edge at a fixed vertex under the reconstructed weak Busemann limit, and concentration for predictable fresh pivots.
3. `2026-09-20T02-20-00Z__two-target-disagreement-energy.md`: exact finite-corner residual representation of `Delta_12`, a two-target disagreement-energy bound `g(p)`, a fresh-candidate compiler, and midpoint strict concavity of the local exponential Bellman operator.

The exact finite-corner identity from the third report is central here. With

\[
b_n=ne_1,\qquad z_n=n(e_1+e_2),
\]

and `Gamma_n` the unique `0`-to-`b_n` geodesic, define the finite-target residual

\[
r_z(x,y)=\tau_{xy}+T(y,z)-T(x,z)\ge0.
\]

Then

\[
D_n:=\sum_{e\in\Gamma_n}r_{z_n}(e)
=T(0,b_n)+T(b_n,z_n)-T(0,z_n),
\tag{2.1}
\]

and

\[
\lim_{n\to\infty}\frac{\mathbb E D_n}{n}=\Delta_{12}.
\tag{2.2}
\]

The historical R08 failures remain binding:

- many local deletion margins may all be explained by one shared bypass, so local gains cannot be multiplied without a separation mechanism;
- a deterministic finite strict triangle saving fails on positive-probability open cylinder events for Exp(1);
- fixed-corner finite blocks through the old tested scales did not cross the source-relevant threshold;
- fluctuation/KPZ statements do not imply strict convexity.

No claim below contradicts these. The semigroup theorem in Section 7 explicitly identifies the missing separation/factorization input instead of hiding it.

## 3. Neighboring block state and P04 coordination

The LIVE20 table assigns P04 to the T10 block-to-infinite-volume companion role under `proofnet24/P04-progress-curvature`. At the repository state checked during this run, indexed search still recovered no substantive current T10 report under that root; recent commits carrying `P04` include historical/non-T10 assignments and are not attributed to the current companion.

I therefore consume the newest canonical `PROB10-10` block state instead of fabricating a P04 theorem. The report

`runs/prob10_2026-09-20/PROB10-10/20260920T0218Z__frontier-carry-synchronization-obstruction.md`

at creation commit `a784be963d58943e91611086bceaf400d91abaab` proves two facts directly relevant here:

1. synchronizing a `k`-vertex antidiagonal frontier after every level has exact one-level mean toll `H_k/2`, so widening the frontier while discarding relative arrival labels is intrinsically lossy;
2. a successful block method must carry the **asynchronous relative arrival-label vector**, and an average-cost Bellman certificate on that state would be source-relevant.

That same report improves the track-certified auxiliary axis lower bound to

\[
\mu(e_1)\ge 0.3002823,
\tag{3.1}
\]

but its retained diagonal upper bound `0.758507818076` is still far above the corresponding `0.6005646` crossing threshold. This auxiliary numerical gap does not move `c_*`.

The present run gives the asynchronous-frontier program a different certificate: carry **two continuation-value vectors modulo constants**, and prove positive Jensen curvature of the min-plus transfer. Under an exact or controlled-error block factorization, these Jensen gaps telescope in the right direction. Section 8 states the precise P04 interface.

## 4. Fresh source/literature boundary

A bounded 20 September 2026 recheck recovered no source-matching proof of strict convexity for ordinary iid continuous undirected nearest-neighbor FPP on `Z^2`, nor for the present Exp(1) special case. This is negative search evidence only; no priority or publication-novelty claim is made.

Relevant distinctions remain:

- Auffinger--Damron--Hanson arXiv:1511.03262 is the source navigation and its Busemann framework supplies valid cocycle/coalescence technology, but it does not rule out a flat support face.
- Jacquet's strict comparison between unrestricted and directed FPP time constants is a different inequality; it does not imply the direction-to-direction triangle defect here.
- recent differentiability results for continuous-space/Riemannian FPP models do not apply to ordinary iid edge FPP on the square lattice.
- quantitative planar coalescence results whose hypotheses already assume many extreme points cannot be used to prove the missing shape geometry without circularity.

No directed-integrable constant or sampled curvature is used below.

## 5. New exact two-terminal averaged-residual representation

The finite-corner residual (2.1) singles out the diagonal target. A more symmetric formulation exposes a variational quantity that is exactly the Jensen defect of the Bellman semigroup.

Let `G` be any connected graph with positive edge lengths `tau`, and fix two terminals `A,C`. Put

\[
f(x)=T(x,A),\qquad g(x)=T(x,C),\qquad d=T(A,C).
\]

Fix `0<theta<1` and define

\[
h_\theta(x):=\theta f(x)+(1-\theta)g(x),
\tag{5.1}
\]

and the terminal-envelope value

\[
w_\theta(x):=
\min\{f(x)+(1-\theta)d,\ g(x)+\theta d\}.
\tag{5.2}
\]

For an oriented edge `(x,y)` define the **averaged residual**

\[
q_\theta(x,y)
:=\tau_{xy}+h_\theta(y)-h_\theta(x).
\tag{5.3}
\]

Since each target distance satisfies the Bellman inequality,

\[
q_\theta(x,y)
=\theta r_A(x,y)+(1-\theta)r_C(x,y)\ge0.
\tag{5.4}
\]

Let

\[
R_\theta(x):=
\inf_{\gamma:x\to\{A,C\}}
\sum_{e\in\gamma}q_\theta(e).
\tag{5.5}
\]

### P20-FPP-TWO-TERMINAL-RESIDUAL-11

**Claim: PROVED.** For every `x`,

\[
\boxed{R_\theta(x)=w_\theta(x)-h_\theta(x).}
\tag{5.6}
\]

If

\[
D_A(x):=f(x)+d-g(x),\qquad
D_C(x):=g(x)+d-f(x),
\tag{5.7}
\]

then

\[
\boxed{
R_\theta(x)
=\min\{(1-\theta)D_A(x),\ \theta D_C(x)\}.
}
\tag{5.8}
\]

In particular,

\[
\boxed{D_A(x)\ge \frac{R_\theta(x)}{1-\theta}.}
\tag{5.9}
\]

#### Proof

For any path `gamma=(v_0=x,...,v_k=B)` ending at `B in {A,C}`, telescoping (5.3) gives

\[
\sum_{j<k}q_\theta(v_j,v_{j+1})
=T(\gamma)+h_\theta(B)-h_\theta(x).
\tag{5.10}
\]

Now `h_theta(A)=(1-theta)d` and `h_theta(C)=theta d`. Minimizing (5.10) first over paths to a fixed terminal, and then over the two terminals, gives exactly

\[
R_\theta(x)
=\min\{f(x)+(1-\theta)d,\ g(x)+\theta d\}-h_\theta(x),
\]

which is (5.6). Expanding the first alternative gives

\[
f+(1-\theta)d-[\theta f+(1-\theta)g]
=(1-\theta)(f+d-g)
=(1-\theta)D_A,
\]

and similarly the second gives `theta D_C`. This proves (5.8), and (5.9) follows because the minimum in (5.8) is at most its first entry. QED.

### Corollary 5.2 — exact finite-corner lower representation

Apply the theorem with

\[
A=b_n=ne_1,\qquad C=z_n=n(e_1+e_2),\qquad x=0.
\]

Then `d=T(b_n,z_n)` and `D_A(0)=D_n` from (2.1). Hence for every `0<theta<1`,

\[
\boxed{
D_n\ge \frac{R_{\theta,n}(0)}{1-\theta}.
}
\tag{5.11}
\]

Thus proving a positive linear density for the two-terminal residual distance `R_{theta,n}(0)` is sufficient for a positive directional triangle defect.

There is also a structural interpretation specific to continuous FPP. Because both summands in (5.4) are nonnegative and `0<theta<1`,

\[
q_\theta(x,y)=0
\iff
r_A(x,y)=r_C(x,y)=0.
\tag{5.12}
\]

So zero-cost averaged-residual edges are precisely common Bellman successors for the two targets. The two-terminal residual problem is therefore a quantitative cost of escaping the common-policy forest.

## 6. General-θ local Exp(1) strict Jensen modulus

At a fresh four-edge star around a vertex `x`, delete `x` and its incident edges and condition on all remaining edge weights. For the four neighbors `y_i`, let

\[
a_i=T_{G\setminus\{x\}}(y_i,A),\qquad
c_i=T_{G\setminus\{x\}}(y_i,C),
\]

and let the fresh star weights be iid `E_i~Exp(1)`. Put

\[
M(v):=\min_i(E_i+v_i),
\]

with unique winners `I_a,I_c` almost surely. Define the local Jensen gap

\[
\kappa_\theta(a,c;E)
:=M(\theta a+(1-\theta)c)
-\theta M(a)-(1-\theta)M(c)\ge0.
\tag{6.1}
\]

This is exactly

\[
\kappa_\theta(x)=\min_{y\sim x}q_\theta(x,y),
\tag{6.2}
\]

for the finite targets `A,C`.

Let `D={I_a != I_c}` and

\[
p:=\mathbb P(D\mid\text{outside star}).
\tag{6.3}
\]

Let `G_a` and `G_c` be the first-to-second score gaps for the two target score vectors.

### Lemma 6.1 — uniform shifted-exponential score-gap tail

For every deterministic offset vector `v in R^4` and every `u>=0`,

\[
\boxed{
\mathbb P(G_v>u\mid v)\ge e^{-3u}.
}
\tag{6.4}
\]

#### Proof

Condition on the winning channel and its winning score. For each of the three nonwinners, the corresponding exponential edge is conditioned only to exceed a deterministic threshold. By exponential memorylessness, the residual amount above that threshold is an independent rate-one exponential; if the threshold is negative, the actual excess is even larger in the stochastic order needed here. Thus each nonwinner exceeds the winner by more than `u` with conditional probability at least `e^{-u}`, independently over the three channels. Multiplying gives at least `e^{-3u}`. Averaging over the winner and winning score proves (6.4). QED.

### Lemma 6.2 — pointwise disagreement gap

On `D`,

\[
\boxed{
\kappa_\theta\ge
\min\{\theta G_a,(1-\theta)G_c\}.
}
\tag{6.5}
\]

#### Proof

Write `i=I_a`. For any `k != i`, the `a`-score excess over the `a` minimum is at least `G_a`, so the mixed-score excess of channel `k` above the convex combination of the two separate minima is at least `theta G_a`. For channel `k=i`, disagreement implies that `i` is not the `c` winner, so its `c`-score excess is at least `G_c`; hence its mixed-score excess is at least `(1-theta)G_c`. Taking the minimum over all channels proves (6.5). QED.

### P20-FPP-GENERAL-THETA-BELLMAN-CURVATURE-12

**Claim: PROVED.** Uniformly over all deterministic outside-star continuation vectors,

\[
\boxed{
\mathbb E[\kappa_\theta\mid\text{outside star}]
\ge
\frac{\theta(1-\theta)}6\,p^2.
}
\tag{6.6}
\]

At `theta=1/2` this gives the preceding midpoint constant `p^2/24`.

#### Proof

For `t>=0`, Lemma 6.2 and the union bound give

\[
\begin{aligned}
&\mathbb P\bigl(D\cap\{\min(\theta G_a,(1-\theta)G_c)>t\}\mid\text{outside}\bigr)\\
&\qquad\ge
p-\mathbb P(G_a\le t/\theta)-\mathbb P(G_c\le t/(1-\theta)).
\end{aligned}
\tag{6.7}
\]

Using (6.4) and `1-e^{-x}<=x`, the right side is at least

\[
p-\frac{3t}{\theta}-\frac{3t}{1-\theta}
=p-\frac{3t}{\theta(1-\theta)}.
\tag{6.8}
\]

This is nonnegative for

\[
0\le t\le t_0:=\frac{p\theta(1-\theta)}3.
\]

Layer-cake integration and Lemma 6.2 therefore yield

\[
\mathbb E\kappa_\theta
\ge
\int_0^{t_0}
\left(p-\frac{3t}{\theta(1-\theta)}\right)dt
=rac{p^2\theta(1-\theta)}6.
\]

No independence between `D` and the score gaps is used. QED.

This theorem is distribution-specific and source-valid for the undirected Exp(1) model. It is not a directed-integrable input.

## 7. New predictable continuation-span coercivity

The previous disagreement-energy theorem left `p` as a block/geometric quantity. The next result lower-bounds it using only continuation-value geometry measurable **before the star is revealed**.

Normalize both continuation vectors by additive constants so that

\[
\min_i a_i=\min_i c_i=0.
\]

Set

\[
B:=\max\{\operatorname{span}(a),\operatorname{span}(c)\},
\qquad
\delta:=\operatorname{span}(a-c),
\tag{7.1}
\]

where `span(v)=max_i v_i-min_i v_i`.

### P20-FPP-SPAN-DISAGREEMENT-COERCIVITY-13

**Claim: PROVED.** Conditional on the outside-star environment,

\[
\boxed{
p\ge
\frac{1-e^{-2}}2\,e^{-5B-5}\,\min\{\delta,1\}.}
\tag{7.2}
\]

Consequently

\[
\boxed{
\mathbb E[\kappa_\theta\mid\text{outside star}]
\ge
K_*\,\theta(1-\theta)e^{-10B}\min\{\delta,1\}^2,
}
\tag{7.3}
\]

where

\[
K_*:=\frac{(1-e^{-2})^2e^{-10}}{24}
=1.4142930739555003\ldots\times10^{-6}.
\tag{7.4}
\]

#### Proof

Choose channels `i,j` such that

\[
(a_i-c_i)-(a_j-c_j)=\delta.
\]

Put `A_0=a_i-a_j`. Then `|A_0|<=B`, while

\[
c_i-c_j=A_0-\delta.
\]

Let

\[
U=E_i-E_j.
\]

The difference of two independent rate-one exponentials has Laplace density

\[
\frac12e^{-|u|}.
\]

The pairwise preference for targets `a` and `c` is opposite whenever

\[
-A_0<U<\delta-A_0,
\tag{7.5}
\]

because then `U+A_0>0` but `U+A_0-delta<0`.

Let `ell=min(delta,1)` and choose the leftmost subinterval `J` of (7.5) of length `ell`. Since `|A_0|<=B`, every `u in J` satisfies `|u|<=B+1`. Hence

\[
\mathbb P(U\in J)
\ge \frac{\ell}{2}e^{-B-1}.
\tag{7.6}
\]

Conditional on `U=u`, the smaller of `E_i,E_j` is rate-two exponential. Therefore

\[
\mathbb P(\min(E_i,E_j)\le1\mid U=u)=1-e^{-2}.
\tag{7.7}
\]

On `U in J` together with this event, both `E_i,E_j<=B+2`. Since every normalized continuation offset lies in `[0,B]`, both pair scores for either target are at most `2B+2`.

Now force each of the other two star edges to exceed `2B+2`. This independent event has probability

\[
e^{-4B-4}.
\tag{7.8}
\]

Then channels `i,j` beat the two other channels for both targets, while (7.5) says their mutual order is opposite. Thus the two global Bellman winners differ. Multiplying (7.6)--(7.8) proves (7.2).

Squaring (7.2) inside the general Jensen modulus (6.6) gives (7.3)--(7.4). QED.

### Corollary 7.2 — local outside-star ring bound

Let `S_x` be the sum of the eight physical edge weights on the nearest-neighbor ring connecting the four neighbors of `x` while avoiding `x`:

`N -> NE -> E -> SE -> S -> SW -> W -> NW -> N`.

All eight edges are outside the star of `x`. Any two neighbors of `x` can be joined in the deleted-star graph along this ring with cost at most `S_x`. Therefore, for **every** target `A`,

\[
\operatorname{span}igl(T_{G\setminus\{x\}}(y_i,A):i=1,\ldots,4\bigr)
\le S_x.
\tag{7.9}
\]

The same holds for target `C`, so `B<=S_x`. Hence

\[
\boxed{
\mathbb E[\kappa_\theta(x)\mid\text{outside star}]
\ge
K_*\theta(1-\theta)e^{-10S_x}
\min\{\delta_x,1\}^2.
}
\tag{7.10}
\]

This is a predictable strictly positive local curvature certificate whenever the two deleted-star continuation vectors are not translates of one another (`delta_x>0`). The remaining global problem is therefore no longer to create local strictness; it is to prove that non-translate continuation states persist with positive density in a block decomposition whose backtracking error is controlled.

## 8. New deterministic min-plus semigroup accumulation theorem

The preceding sections give strict curvature for one Bellman update. P04 needs a theorem that says such curvature survives composition rather than being swallowed by shared bypasses.

Let `T_j:R^{F_j}->R^{F_{j-1}}`, `j=m,...,1`, be operators satisfying:

1. **monotonicity:** `u<=v` coordinatewise implies `T_j u<=T_j v`;
2. **translation equivariance:** `T_j(u+t 1)=T_j u+t 1`;
3. **concavity:**
   \[
   T_j(\theta u+(1-\theta)v)
   \ge\theta T_j u+(1-\theta)T_j v.
   \]

Finite shortest-path/min-plus transfer operators have these properties because each output coordinate is the minimum of affine functions of the terminal vector.

Given terminal vectors `a_m,c_m`, propagate

\[
a_{j-1}=T_j a_j,\qquad c_{j-1}=T_j c_j.
\tag{8.1}
\]

Also propagate their mixed terminal condition through the nonlinear semigroup:

\[
h_m=\theta a_m+(1-\theta)c_m,
\qquad h_{j-1}=T_j h_j.
\tag{8.2}
\]

Define the one-step Jensen-gap vector

\[
J_j:=T_j(\theta a_j+(1-\theta)c_j)
-[\theta T_j a_j+(1-\theta)T_j c_j]
\ge0.
\tag{8.3}
\]

### P20-FPP-MINPLUS-JENSEN-ACCUMULATION-14

**Claim: PROVED.** Let

\[
d_j:=h_j-[\theta a_j+(1-\theta)c_j],
\qquad
m_j:=\min_{x\in F_j}d_j(x).
\]

Then

\[
\boxed{m_{j-1}\ge m_j+\min_{x\in F_{j-1}}J_j(x).}
\tag{8.4}
\]

Since `m_m=0`,

\[
\boxed{
m_0\ge\sum_{j=1}^m\min_{x\in F_{j-1}}J_j(x).}
\tag{8.5}
\]

If the starting frontier is a singleton, its total Bellman Jensen defect is therefore at least the sum of the minimum one-block Jensen gaps.

#### Proof

By definition `d_j>=m_j 1`, so

\[
h_j\ge \theta a_j+(1-\theta)c_j+m_j1.
\]

Monotonicity and translation equivariance give

\[
\begin{aligned}
h_{j-1}=T_jh_j
&\ge T_j(\theta a_j+(1-\theta)c_j+m_j1)\\
&=T_j(\theta a_j+(1-\theta)c_j)+m_j1.
\end{aligned}
\]

Subtract

\[
\theta a_{j-1}+(1-\theta)c_{j-1}
=\theta T_ja_j+(1-\theta)T_jc_j
\]

and use (8.3):

\[
d_{j-1}\ge J_j+m_j1.
\]

Taking coordinatewise minima proves (8.4); summing recursively with `m_m=0` proves (8.5). QED.

### Exact connection to the two-terminal residual

Take the terminal frontier to consist of `{A,C}` and put

\[
a_m=(0,d),\qquad c_m=(d,0),\qquad d=T(A,C).
\tag{8.6}
\]

For the exact full shortest-path transfer from a starting point `x` to `{A,C}`, triangle inequality gives

\[
T a_m=f(x),\qquad T c_m=g(x),
\]

whereas the mixed terminal vector is

\[
\theta a_m+(1-\theta)c_m=((1-\theta)d,\theta d),
\]

so its transferred value is exactly `w_theta(x)`. Thus the total semigroup Jensen defect is

\[
w_\theta(x)-[\theta f(x)+(1-\theta)g(x)]
=R_\theta(x).
\tag{8.7}
\]

Equation (8.5) is therefore an exact deterministic mechanism for turning positive block Bellman curvature into the two-terminal residual required by (5.11).

This is the main gain of the run: **shared bypasses do not destroy curvature once the geometry is represented by an exact min-plus operator composition; local Jensen gaps telescope through the semigroup.** The hard part is now isolated as constructing such a fresh block composition, or a controlled-error comparison to one, for unrestricted undirected FPP.

## 9. Concrete P04 block-to-infinite-volume interface with controlled errors

The current neighboring PROB10 block work shows why simply cutting at antidiagonals is not exact: unrestricted undirected geodesics may backtrack across a cut, and a synchronized frontier destroys the relative timing state. P04's role is precisely to control this finite-to-infinite issue.

The theorem above gives a clean sufficient input. For each `n`, suppose P04 constructs `M_n` fresh physical-edge bands and associated min-plus transfers such that:

1. the two terminal continuation states corresponding to `A=b_n` and `C=z_n` are propagated through the block chain;
2. the block chain has Jensen gaps `J_{n,j}` as in (8.3);
3. the true two-terminal residual satisfies the comparison
   \[
   R_{\theta,n}(0)
   \ge
   \sum_{j=1}^{M_n}\min J_{n,j}-E_n,
   \tag{9.1}
   \]
   where `E_n>=0` is an interface/backtracking error;
4. `M_n/n -> lambda>0`, and for at least an asymptotic fraction `rho>0` of the blocks one has a rigorous expected lower bound
   \[
   \mathbb E[\min J_{n,j}]\ge j_0>0;
   \tag{9.2}
   \]
5. `limsup E E_n/n <= epsilon`.

Then (5.11), (2.2), and (9.1) give the **conditional compiler**

\[
\boxed{
\Delta_{12}
\ge
\frac{\lambda\rho j_0-\varepsilon}{1-\theta}.
}
\tag{9.3}
\]

Therefore the source-relevant sufficient condition is simply

\[
\boxed{\lambda\rho j_0>\varepsilon.}
\tag{9.4}
\]

No independence between blocks is needed for the expectation-level deterministic semigroup inequality itself; independence/freshness is needed only to prove a uniform positive `j_0` or concentration estimate from the Exp(1) environment.

Sections 6--7 offer two ways to certify `j_0` inside a block:

- prove a conditional policy-disagreement probability `p>=p_0`, yielding
  \[
  j_0\ge\theta(1-\theta)p_0^2/6;
  \]
- or prove a continuation-state span condition `B<=B_0`, `delta>=delta_0`, yielding
  \[
  j_0\ge
  K_*\theta(1-\theta)e^{-10B_0}\min(\delta_0,1)^2.
  \]

This aligns directly with the asynchronous-frontier obstruction found by the neighboring block lane: the finite state that must be preserved is not merely an infected set but the relative continuation-label vector, naturally considered modulo additive constants. The new result says exactly what a rigorous finite compression should preserve: enough information to lower-bound the Jensen gap uniformly over every continuous state in a cell.

## 10. Exact finite sanity artifact

After deriving the symbolic mechanism, I executed an exact rational sanity checker. It is deliberately a falsification aid, not evidence for asymptotic curvature.

Script:

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T03-10-00Z__two-terminal-jensen-sanity.py`

creation commit `8b1caf448557860175ffc2b93e2be15fa8a781bb`.

Archived stdout:

`proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T03-10-00Z__two-terminal-jensen-sanity.out`

creation commit `be2d45e130ba3d677b586965a9d0d3c64021f56e`.

The checker uses a deterministic `5x5` grid with distinct rational edge weights and `theta=2/3`. It verifies at all 25 vertices that the shortest `q_theta` residual distance to the two terminals equals `w_theta-h_theta` exactly, and at the start verifies the formula

\[
R_\theta=\min\{(1-\theta)D_A,\theta D_C\}.
\]

It also exhausts 256 rational four-edge score tuples for fixed rational continuation offsets and checks the pointwise local Jensen inequality and disagreement-gap inequality. The run ends

`P20-T10-TWO-TERMINAL-JENSEN-SANITY: ALL_EXACT_CHECKS_PASS`.

No sampled numerical curvature is used anywhere in the proof.

## 11. What failed or remains incomplete

The exact local and algebraic parts are now stronger, but the source problem is still open because three global issues remain.

### 11.1 Backtracking prevents a naive antidiagonal semigroup factorization

For oriented FPP, fresh antidiagonal transfers compose exactly. For the target **undirected** model, an optimal path can cross a cut, return, and cross again. Simply replacing unrestricted FPP by an oriented or no-return transfer changes the model. This is the central P04 finite-to-infinite error `E_n` in (9.1).

### 11.2 Continuation states are continuous and unbounded

The neighboring synchronized-frontier calculation proves that forgetting relative labels is too expensive. A finite-state rigorous checker must therefore round the quotient-by-constants continuation vector in a direction preserving a **lower bound** on the Jensen gap for every state in a cell. No such exhaustive compression is claimed here.

The new span estimate (7.3) helps: it reduces local curvature to two scalar controls, `B` and `delta`, but a global argument must still show that `delta` is bounded away from zero often enough, or otherwise charge the evolution of nearly translated continuation states.

### 11.3 Nearly translated two-target states are the remaining variational obstruction

If `a-c` is almost constant across a frontier, the two target policies nearly coincide and the local Jensen gap can be tiny. This is not an artifact: exact translates give zero Bellman curvature. A successful next argument must exploit the incompatible terminal conditions `(0,d)` and `(d,0)` to show that the quotient-state difference cannot stay near zero across all linearly many fresh bands unless a compensating interface error is already paid.

That is now the precise finite-dimensional variational target.

## 12. Next attack

Do **not** spend the next run improving the local constant `K_*`; local strictness is no longer the named obstruction.

The next attack is a **quotient-state drift / terminal-separation theorem** for asynchronous frontiers:

1. On each physical-edge band, propagate the two continuation vectors `a_j,c_j` modulo additive constants.
2. Define a quotient separation functional, initially for example
   \[
   \delta_j=\operatorname{span}(a_j-c_j).
   \]
3. Prove a deterministic dichotomy for a min-plus transfer: either its Jensen gap is at least a quantitative function of `delta_j` and the frontier span, or the quotient separation `delta` contracts by a controlled amount.
4. Sum this dichotomy from the incompatible terminal condition `(0,d)` versus `(d,0)` to the start. If `delta` cannot collapse without accumulated Jensen curvature, (8.5) gives a positive residual. If it can collapse cheaply, the explicit collapse mechanism should identify the exact backtracking/interface configuration P04 must charge.
5. Use physical-edge band ownership from the canonical PROB10-10 construction to keep the edge randomness fresh; do not impose synchronized arrival labels.

A particularly useful finite lemma would be a block inequality of the form

\[
\min J_j + C\,[\Psi(\delta_{j-1})-\Psi(\delta_j)]
\ge c\,\Phi(\delta_j,B_j)
\tag{12.1}
\]

for a bounded potential `Psi` and positive `Phi` away from zero. Telescoping would turn terminal separation into accumulated curvature while allowing occasional near-translate blocks. This is the variational analogue of the potential inequality sought by the neighboring asynchronous-frontier route, but it targets the **two-target difference state** directly.

If two such recovery attempts fail without demonstrated mechanism gain, the owner directive requires a scope switch among T01--T10 with preserved T10 history. That trigger has not fired in this run because Sections 5--8 are new proved mechanism gains.

## 13. Short cyclic-interval handoff

The displaced P20 source `FOKAM-BITJOKA-2026-CYCLIC-INTERVAL` remains preserved and is not reopened. The source-literal YES proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` remains intact; its supplementary exact checker remains PASS; P26's full-proof/source-quantifier audit remains PASS; and the last recovered state had only `1/2` independent audits because the second distinct non-P20/non-P26 audit was absent. No completed campaign certification or publication-novelty claim is implied. Per the current owner directive, this FPP run spent no research time waiting for that audit.

## 14. Before/after and mechanism ledger

| Quantity | Before | After | Meaning |
|---|---:|---:|---|
| source directional defect `c_*` | `0` | `0` | **NO SOURCE MOVEMENT / OPEN** |
| exact finite-corner defect representation | yes | yes | preserved |
| local Bellman curvature scope | midpoint `theta=1/2` | every `0<theta<1` | proved extension |
| disagreement input | exogenous conditional `p` | explicit predictable span lower bound | proved mechanism gain |
| block accumulation | conditional fresh-candidate sum | exact min-plus Jensen semigroup theorem | proved mechanism gain |
| P04 transfer target | visit/disagreement density | Jensen-gap sum minus explicit interface error | sharper interface |

### ledger_delta

```text
P20 / T10 / ADH_Q4_EXP1_Z2_UNDIRECTED
source_metric: c_* = 0 -> 0 (NO SOURCE-LEVEL MOVEMENT)
new_proved: P20-FPP-TWO-TERMINAL-RESIDUAL-11
new_proved: P20-FPP-GENERAL-THETA-BELLMAN-CURVATURE-12
new_proved: P20-FPP-SPAN-DISAGREEMENT-COERCIVITY-13
new_proved: P20-FPP-MINPLUS-JENSEN-ACCUMULATION-14
mechanism_gain: exact two-terminal residual/Jensen identity + all-theta Exp(1) local modulus + outside-star span coercivity + deterministic semigroup accumulation
P04_interface: prove R_theta,n(0) >= sum_j min J_{n,j} - E_n with linear good-block Jensen mass and E[E_n]/n controlled; then Delta_12 >= (lambda*rho*j0-epsilon)/(1-theta)
residual_obstruction: unrestricted undirected backtracking/reentry and rigorous finite compression of continuous asynchronous relative-label states; nearly translated two-target continuation vectors are the variational bottleneck
next_attack: quotient-state drift / terminal-separation potential inequality for a_j-c_j, coupled to physical-edge-band freshness
cyclic_interval_handoff: proof candidate preserved; P26 audit PASS; last independent audit gate 1/2; no closure claim; do not wait
parent_claim: operations/claims/PROB10-10.md unchanged
shared_POSTED_RESULTS_QUEUE: untouched
```

No historical or peer file was overwritten. No shared claim/POSTED ledger, email, Drive object, public post, workflow, permission, paid compute, or schedule was changed.

END OF P20 FPP RUN REPORT

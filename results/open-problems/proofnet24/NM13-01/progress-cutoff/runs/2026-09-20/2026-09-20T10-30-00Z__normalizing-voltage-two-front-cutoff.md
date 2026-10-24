Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated runtime metadata establishes that setting.**

# NM13-01 / LIVE20 T08 — normalizing-voltage two-front cutoff beyond the hidden L2 information budget

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run and after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A–C and the explicit degree-14 class below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. The mathematical claim is new relative to the repository state read in this run; bounded external searches did not establish worldwide priority.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Prewrite master observed immediately before this run's writes: `72623e774cf7068f8034a68db0b2402c01658bdf`.

## 0. Short handoff and partner split

The latest complete NM13-01 report read was

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T09-13-06Z__growing-automorphism-memory-cutoff.md`.

That report proved a growing hidden-memory semidirect transfer from an exact base quotient by paying the point-mass hidden `L^2` cost

\[
\frac12\sqrt{|K_n|-1}\,e^{-b\eta_nt}.
\]

It therefore handled polynomial hidden memory only when

\[
\frac12\log |K_n|
<\frac{b\eta_n}{a}T_n
\]

by a fixed proportional margin. It explicitly left the critical/supercritical information-volume regime as a genuine obstruction.

The newest substantive P26 result read is commit `157090eb32dfaafb96d2316be81732e2459708a8`, which proves a weighted-exceptional Green transfer and an exact-distance-six cutoff class; newer P26 checker commits continue the exact-distance program. P26 is therefore still on NBRW shells, spherical polynomials, radial clocks and weighted Green functions. This run is deliberately complementary: an algebraic/transitivity argument on Cayley voltage lifts, with no shell Green estimate.

The materially different attack is to stop paying hidden state-space cardinality at all. If the edge monodromy normalizes the hidden generating set, the deterministic hidden kicks commute with the hidden heat semigroup. The hidden error is then its **actual total-variation distance**, not a point-mass `L^2` upper bound. This exposes two genuine cutoff fronts and removes the previous subcritical-memory restriction.

## 1. Exact source convention and current primary boundary

Salez, `arXiv:2508.21055v1`, inserts independent mean-one exponential waiting times between discrete jumps. If `T` is the discrete transition matrix, then

\[
P_t=e^{-t}\sum_{k\ge0}\frac{t^kT^k}{k!}=e^{t(T-I)}.
\tag{1.1}
\]

Problem 2.3 asks exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree and spectral gaps bounded away from zero.

The fresh primary boundary checked in this run remains:

* D. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026: every fixed-degree **long-range expander** sequence has cutoff with an explicit Gaussian profile, and
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Thus long-range expansion is strictly stronger than the arbitrary spectral-expander hypothesis in Salez Problem 2.3.
* F. Pedrotti--J. Salez, `arXiv:2607.05345`, submitted 6 July 2026: a local-product/non-equilibrium-Poincare criterion gives a general cutoff window bound, but the checked statement does not derive its hypothesis merely from vertex transitivity plus an ordinary fixed spectral gap.
* T. Kaufman--A. Lubotzky, `arXiv:1108.2960`, Theorem 3: for prime power `q` and sufficiently large exponents there are `(q+1)`-regular edge-transitive Ramanujan Cayley graphs on `PSL_2/PGL_2` type groups. We use the `q=5` degree-six family below.

The root `POSTED.md` exclusion for Salez Problem 2.4 / the Abelian Cayley product-condition manuscript was read and respected. Nothing below reopens that posted claim.

## 2. Parent problem before / after

### Before

Salez Problem 2.3 was `OPEN`. NM13-01 had already proved several non-LRE cutoff classes, including fixed and subcritical-growing automorphism memories. The strongest growing-memory theorem still required a hidden `L^2` information budget; for hidden size `|K_n|=n^{\alpha+o(1)}` only a bounded range of `\alpha` was covered from a hidden spectral gap alone.

### After

Salez Problem 2.3 remains `OPEN`, but the proved restricted scope expands to **normalizing voltage lifts with a genuinely growing second macroscopic cutoff factor**, with no hidden-cardinality budget. The explicit class in Section 7 is 14-regular, vertex-transitive, a uniform spectral expander, has

\[
|K_j|=n_j^{2+o(1)},
\]

lies outside every fixed long-range-expansion constant, and has source-continuous-time cutoff at

\[
\boxed{
T_j=\frac73\log_5 N_j+O(1)
}
\tag{2.1}
\]

with

\[
\boxed{O(\sqrt{\log N_j})}
\tag{2.2}
\]

window.

The previous `L^2` budget, applied with the same degree-six Ramanujan ingredients, would only cover

\[
\alpha<\frac{3-\sqrt5}{\log 5}=0.4746576532\ldots,
\]

whereas the explicit class has `\alpha=2`. Thus the new class is decisively outside the preceding theorem's quantitative regime.

## 3. Theorem A — normalizing-voltage TV transfer

Let

\[
G=\operatorname{Cay}(\Gamma,S),\qquad |S|=d,
\]

and

\[
F=\operatorname{Cay}(K,T),\qquad |T|=s,
\]

be finite connected undirected Cayley graphs, so `S=S^{-1}` and `T=T^{-1}`. Let

\[
\phi:S\to K
\]

satisfy the inverse-compatibility condition

\[
\phi(u^{-1})=\phi(u)^{-1}.
\tag{3.1}
\]

Define a Cayley graph on the direct product by

\[
H=\operatorname{Cay}(\Gamma\times K,\Sigma),
\qquad
\Sigma=\{(u,\phi(u)):u\in S\}\cup\{(e,t):t\in T\}.
\tag{3.2}
\]

Assume that every voltage normalizes the hidden generating set:

\[
\boxed{
\phi(u)T\phi(u)^{-1}=T\qquad(u\in S).
}
\tag{3.3}
\]

Put

\[
D=d+s,\qquad a=\frac dD,\qquad b=\frac sD.
\]

Let `d_G,d_F,d_H` denote worst-start TV distance for the source rate-one continuous-time walks. Since these are Cayley graphs, all starts are equivalent.

### Theorem A

For every `t>=0`,

\[
\boxed{
 d_G(at)\le d_H(t)\le d_G(at)+d_F(bt).
}
\tag{3.4}
\]

### Proof

Thin the rate-one Poisson clock of `H` into independent cross and vertical event processes, of rates `a` and `b`. At a cross event choose `u` uniformly from `S`; at a vertical event choose `t` uniformly from `T`.

The first coordinate ignores all vertical events and, at every cross event, is right-multiplied by an independent uniform `u\in S`. Therefore its law is exactly the rate-`a` continuous-time SRW on `G`. Projection contracts TV, giving

\[
d_H(t)\ge d_G(at).
\tag{3.5}
\]

For the upper bound, condition on the complete cross event times and labels

\[
u_1,\ldots,u_m.
\]

The base endpoint is now deterministic. The hidden coordinate alternates vertical heat-semigroup pieces with deterministic right translations by `\phi(u_i)`.

Write `W` for hidden discrete SRW, acting by right convolution,

\[
Wf(k)=\frac1s\sum_{z\in T}f(kz),
\]

and `R_h f(k)=f(kh)`. Condition (3.3) implies

\[
WR_{\phi(u)}=R_{\phi(u)}W.
\tag{3.6}
\]

Indeed,

\[
WR_hf(k)=\frac1s\sum_{z\in T}f(kzh)
       =\frac1s\sum_{z\in T}f\bigl(kh(h^{-1}zh)\bigr)
       =R_hWf(k)
\]

because `h^{-1}Th=T`.

Hence all deterministic voltage kicks commute through all vertical heat pieces. If the total elapsed time is `t`, the conditional hidden law is simply a right translate of

\[
\delta_{k_0}e^{bt(W-I)}.
\]

Uniform measure on `K` is translation-invariant, so the conditional hidden TV distance from uniform is exactly `d_F(bt)`, independently of the conditioned base path.

Replace, for each conditioned path, the hidden endpoint law by uniform. The replacement costs at most `d_F(bt)` in TV. After averaging over cross labels, the replacement law is precisely

\[
\bigl(\delta_{g_0}e^{at(P_G-I)}\bigr)\otimes u_K.
\]

Its TV distance from `u_\Gamma\otimes u_K` is `d_G(at)`. The triangle inequality gives the upper bound in (3.4). `QED`

### Why this differs from the preceding NM13-01 transfer

No factor `\sqrt{|K|}` appears. The previous growing-memory proof allowed arbitrary hidden isometric kicks and therefore knew only that vertical evolution contracts mean-zero `L^2`; a point mass then costs `\sqrt{|K|-1}`. Here the normalizer relation (3.3) allows the entire kick sequence to be moved past the vertical semigroup, exposing the **true hidden TV profile**. This is the mechanism that reaches the supercritical information-volume regime.

## 4. Theorem B — spectral-gap transfer

The same construction is a spectral expander whenever the two input factors are. The normalizer assumption is not needed for this part.

Let `\gamma_G` and `\gamma_F` be the normalized discrete-time spectral gaps of `G` and `F`.

### Theorem B

\[
\boxed{
\operatorname{gap}(H)
\ge
\min\{a\gamma_G,b\gamma_F\}.
}
\tag{4.1}
\]

### Proof

For `f:\Gamma\times K\to\mathbb R`, put

\[
\bar f(g)=\mathbb E_{k\sim u_K}f(g,k).
\]

The variance decomposition is

\[
\operatorname{Var}(f)
=\operatorname{Var}_g(\bar f)
 +\mathbb E_g\operatorname{Var}_k(f(g,k)).
\tag{4.2}
\]

The vertical part of the Dirichlet form is at least

\[
\gamma_F\,\mathbb E_g\operatorname{Var}_k(f(g,k)).
\tag{4.3}
\]

For the cross part, fix `u\in S`. Since right multiplication by `\phi(u)` is a permutation of `K`, Jensen gives

\[
\mathbb E_k\bigl(f(gu,k\phi(u))-f(g,k)\bigr)^2
\ge
\bigl(\bar f(gu)-\bar f(g)\bigr)^2.
\tag{4.4}
\]

Averaging over `g,u` gives at least the base Dirichlet form of `\bar f`, hence at least

\[
\gamma_G\operatorname{Var}_g(\bar f).
\tag{4.5}
\]

Weighting the cross and vertical forms by `a,b` and using (4.2) proves (4.1). `QED`

## 5. Theorem C — a two-macroscopic-front voltage class

Theorem A becomes especially useful when the hidden graph splits as a fixed voltage coordinate times a second growing macroscopic factor.

Let

* `G_n=Cay(\Gamma_n,S_n)` be `d`-regular;
* `L_n=Cay(\Lambda_n,U_n)` be `\ell`-regular;
* `A=Cay(A,R)` be a fixed `r`-regular Cayley graph;
* `\phi_n:S_n\to A` satisfy inverse compatibility.

Take

\[
K_n=A\times\Lambda_n,
\qquad
T_n=(R\times\{e\})\cup(\{e\}\times U_n),
\]

and use only voltages `(\phi_n(u),e)` in (3.2). Suppose those voltages normalize `R`; this is automatic when `A` is Abelian. Put

\[
D=d+r+\ell.
\]

Then both macroscopic coordinates are exact Markov projections:

\[
\Gamma_n\text{-rate}=\frac dD,
\qquad
\Lambda_n\text{-rate}=\frac\ell D.
\tag{5.1}
\]

The hidden continuous-time generator factorizes because its discrete kernel is

\[
W=\frac r{r+\ell}P_A+\frac\ell{r+\ell}P_{L_n},
\]

so after multiplying by hidden event rate `(r+ell)/D`, the two hidden coordinates run independently at rates `r/D` and `ell/D`.

Consequently Theorem A and projection give the exact sandwich

\[
\boxed{
\max\left\{
 d_{G_n}\left(\frac dD t\right),
 d_{L_n}\left(\frac\ell D t\right)
\right\}
\le d_{H_n}(t)
}
\tag{5.2}
\]

and

\[
\boxed{
 d_{H_n}(t)
\le
 d_{G_n}\left(\frac dD t\right)
+d_{L_n}\left(\frac\ell D t\right)
+d_A\left(\frac rD t\right).
}
\tag{5.3}
\]

Here the upper product estimate uses

\[
d_{A\times L_n}(s)\le d_A(s_A)+d_{L_n}(s_L).
\]

### Cutoff consequence

Assume `G_n` has cutoff at `T_n^G` with window `w_n^G=o(T_n^G)`, and `L_n` has cutoff at `T_n^L` with window `w_n^L=o(T_n^L)`. Since `A` is fixed, `d_A(rt/D)` is exponentially small on any diverging logarithmic time scale. Define scaled fronts

\[
C_n^G=\frac DdT_n^G,
\qquad
C_n^L=\frac D\ell T_n^L,
\qquad
C_n=\max\{C_n^G,C_n^L\}.
\tag{5.4}
\]

Then (5.2)--(5.3) imply cutoff at `C_n`, with window

\[
\boxed{
O\left(\max\left\{\frac Dd w_n^G,\frac D\ell w_n^L,1\right\}\right).
}
\tag{5.5}
\]

To see this, on the pre-cutoff side use in (5.2) whichever factor realizes the maximum in (5.4). On the post-cutoff side, time `C_n+cW_n` lies at least `cW_n` past the later scaled front and no earlier than the corresponding post-front of the other factor; (5.3) makes all three terms small. If the two fronts are separated by much more than `W_n`, the limiting profile is inherited from the later factor. If they coalesce on the window scale, the sandwich still proves cutoff but need not identify a one-factor profile.

This theorem has **no restriction whatsoever on the cardinality ratio** `|\Lambda_n|/|\Gamma_n|`. A gigantic hidden cutoff factor simply becomes the later macroscopic front.

## 6. A nontrivial fixed voltage assignment

For the explicit class, take

\[
A=C_2\times C_2=\{0,e_1,e_2,e_1+e_2\},
\]

with generating set

\[
R=\{e_1,e_2\}.
\]

This is the four-cycle and has normalized gap `1`.

Given any symmetric six-element generating set `S=S^{-1}`, inversion partitions `S` into orbits of size one or two. There are at least three inversion orbits. Choose two of them and set

\[
\phi=e_1\quad\text{on the first orbit},
\qquad
\phi=e_2\quad\text{on the second orbit},
\]

and `\phi=0` on all remaining orbits. Since every element of `A` is an involution,

\[
\phi(s^{-1})=\phi(s)=\phi(s)^{-1},
\]

and the voltage image spans all of `A`.

For the `PSL_2/PGL_2` groups used below, the abelianization is trivial in the `PSL_2` case (for the present sufficiently large odd fields) and has order at most two in the `PGL_2` case. Hence no homomorphism from the base group to `C_2^2` can extend this spanning voltage assignment. In particular, the twist is not removable by the natural homomorphic moving-frame gauge. This observation is not needed for the cutoff proof; it only rules out the most immediate collapse to an untwisted direct-product generating set.

## 7. Explicit degree-14 supercritical-memory class outside LRE

Use Kaufman--Lubotzky's `q=5` edge-transitive Ramanujan Cayley family. For all sufficiently large `j`, let

\[
G_j=\operatorname{Cay}(\Gamma_j,S_j)
\]

be the degree-six member at field exponent `j`, and let

\[
L_j=\operatorname{Cay}(\Lambda_j,U_j)
\]

be the degree-six member at exponent `2j`.

Write

\[
n_j=|\Gamma_j|,
\qquad
m_j=|\Lambda_j|.
\]

The orders of the relevant `PSL_2/PGL_2` groups are a constant factor times `Q(Q^2-1)` with `Q=5^j`. Therefore

\[
\boxed{
\log m_j=2\log n_j+O(1),
\qquad
m_j=n_j^{2+o(1)}.
}
\tag{7.1}
\]

On

\[
\Gamma_j\times A\times\Lambda_j
\]

use the 14-element symmetric generating set consisting of

* six voltage-coupled base generators `(s,\phi_j(s),e)`, `s\in S_j`;
* two fixed-voltage generators `(e,e_1,e),(e,e_2,e)`;
* six second-factor generators `(e,0,u)`, `u\in U_j`.

Call the resulting graph `H_j`. It is connected because the vertical generators generate `A\times\Lambda_j` and then

\[
(s,0,e)=(s,\phi_j(s),e)(e,\phi_j(s)^{-1},e).
\]

It is a 14-regular Cayley graph, hence vertex-transitive.

### 7.1 Uniform spectral expansion

For a degree-six Ramanujan graph, the nontrivial normalized adjacency eigenvalues have absolute value at most

\[
\frac{2\sqrt5}{6}=\frac{\sqrt5}{3},
\]

so

\[
\gamma_6\ge1-\frac{\sqrt5}{3}=\frac{3-\sqrt5}{3}.
\tag{7.2}
\]

The hidden vertical graph on `A\times\Lambda_j` has normalized kernel

\[
W=\frac14P_A+\frac34P_{L_j}.
\]

Its gap is at least

\[
\min\left\{\frac14\cdot1,\frac34\gamma_6\right\}
=\frac{3-\sqrt5}{4},
\tag{7.3}
\]

because `(3-sqrt5)/4<1/4`.

In Theorem B,

\[
a=\frac6{14}=\frac37,
\qquad
b=\frac8{14}=\frac47.
\]

Both terms in (4.1) equal the same quantity:

\[
\frac37\frac{3-\sqrt5}{3}
=\frac47\frac{3-\sqrt5}{4}
=\frac{3-\sqrt5}{7}.
\]

Thus

\[
\boxed{
\operatorname{gap}(H_j)
\ge\frac{3-\sqrt5}{7}
=0.1091331460\ldots.
}
\tag{7.4}
\]

So `(H_j)` is a bounded-degree vertex-transitive spectral-expander sequence in the exact sense of Salez Problem 2.3.

### 7.2 Exact two-front TV sandwich

Here `d=ell=6`, `r=2`, `D=14`, so (5.2)--(5.3) become

\[
\boxed{
\max\left\{
 d_{G_j}(3t/7),d_{L_j}(3t/7)
\right\}
\le d_{H_j}(t)
}
\tag{7.5}
\]

and

\[
\boxed{
 d_{H_j}(t)
\le
d_{G_j}(3t/7)+d_{L_j}(3t/7)+d_A(t/7).
}
\tag{7.6}
\]

Since `A` is the four-cycle, the elementary `L^2` estimate gives

\[
d_A(t/7)\le\frac{\sqrt3}{2}e^{-t/7}.
\tag{7.7}
\]

This fixed term is negligible on the logarithmic front.

### 7.3 Cutoff center and window

Altschuler's theorem applies to each degree-six Ramanujan factor (Ramanujan implies LRE) in Salez's rate-one convention. Each factor of size `M` has cutoff center

\[
\frac{6}{6-2}\log_5M
=\frac32\log_5M
\tag{7.8}
\]

and `O(\sqrt{\log M})` window, with an explicit Gaussian profile.

After the outer rate factor `3/7`, the two fronts of `H_j` are

\[
C_j^G=\frac72\log_5 n_j,
\qquad
C_j^L=\frac72\log_5 m_j.
\tag{7.9}
\]

By (7.1), the second is later by order `\log n_j`:

\[
C_j^L=7\log_5 n_j+O(1),
\qquad
C_j^G=\frac72\log_5n_j.
\]

Therefore the base `G_j` is already far past its own window when the `L_j` front arrives, and (7.5)--(7.7) squeeze the full TV profile to the rescaled `L_j` profile. In particular,

\[
\boxed{
T_j^H=\frac72\log_5 m_j
=7\log_5n_j+O(1)
}
\tag{7.10}
\]

with

\[
\boxed{
O(\sqrt{\log m_j})=O(\sqrt{\log N_j})
}
\tag{7.11}
\]

window.

Since

\[
N_j=4n_jm_j=n_j^{3+o(1)},
\]

we may rewrite the center as

\[
\boxed{
T_j^H=\frac73\log_5N_j+O(1).
}
\tag{7.12}
\]

The Gaussian limiting profile of the later degree-six Ramanujan factor transfers under the deterministic `3/7` time rescaling.

### 7.4 Failure of every fixed LRE constant

This output is not covered by Altschuler's long-range-expander theorem.

One output step changes at most one of the two growing macroscopic coordinates `\Gamma_j,\Lambda_j` by one edge: a voltage-coupled base move changes only `\Gamma_j` among those two, while a `U_j` move changes only `\Lambda_j`. Hence any endpoint at output distance at most `r` has macroscopic distances `i,j` satisfying

\[
i+j\le r.
\]

The universal degree-six sphere bound gives `O(5^i)` choices in the first factor and `O(5^j)` in the second. The fixed `A` coordinate contributes a factor at most four. Summing over `i+j<=r`,

\[
\boxed{
|B_{H_j}(x,r)|\le C(r+1)5^r
}
\tag{7.13}
\]

for an absolute constant `C`.

But `H_j` has degree 14, so its LRE tree benchmark is `13^r`. Take

\[
r_j=\left\lfloor\frac12\log_{13}N_j\right\rfloor.
\]

Then `13^{r_j}=N_j^{1/2+o(1)}`, which is below the `3N_j/4` cap in the LRE definition, while

\[
\frac{|B_{H_j}(x,r_j)|}{13^{r_j}}
\le(\log N_j)N_j^{-\beta+o(1)},
\]

where

\[
\boxed{
\beta=\frac12\left(1-\frac{\log5}{\log13}\right)
=0.1862632184\ldots>0.
}
\tag{7.14}
\]

Thus no fixed `c>0` can satisfy the LRE lower bound even for singleton sets along this sequence. The class is genuinely spectral-expanding but not long-range expanding.

## 8. Obstruction removed relative to the preceding run

The previous growing-memory theorem's sufficient condition, specialized to degree-six visible base, hidden vertical degree eight and hidden gap `(3-sqrt5)/4`, was

\[
\alpha<
\frac{2s\eta}{(d-2)\log(d-1)}
=\frac{3-\sqrt5}{\log5}
=0.4746576532\ldots
\tag{8.1}
\]

for `|K_n|=n^{\alpha+o(1)}`.

The present explicit class has

\[
|K_j|=4m_j=n_j^{2+o(1)},
\tag{8.2}
\]

so `\alpha=2`, more than four times the preceding threshold. Nevertheless it has a square-root cutoff window, because the large hidden component does not need to be erased before the visible front. It carries its own sharp macroscopic front, and exact normalizer commutation exposes that front directly in TV.

Therefore:

\[
\boxed{
\text{critical or supercritical hidden information volume is not itself an obstruction to cutoff.}
}
\tag{8.3}
\]

What remains is more structural. A plausible general obstruction must involve at least one of:

1. **nonnormalizing monodromy**, so hidden kicks continually rotate the hidden geometry and cannot be commuted through its heat semigroup;
2. **absence of a sharp macroscopic factor**, so there is no second cutoff front to inherit;
3. **genuinely inseparable stabilizer representations**, where no exact projection/fiber decomposition captures the root-start likelihood variable.

This narrows the general transitive-expander problem in a way that is complementary to P26's Green-function program: P26 controls how mass propagates through shells; the present argument controls how transitive algebraic monodromy can or cannot preserve a second information phase.

## 9. Sanity checks actually executed

The archived checker is

`2026-09-20T10-30-00Z__normalizing-voltage-check.py`

with output

`2026-09-20T10-30-00Z__normalizing-voltage-check.out`.

It uses the finite model

\[
\Gamma=\mathbb Z/7,\quad
S=\{\pm1,\pm2\},\quad
A=C_2^2,\quad
\Lambda=\mathbb Z/3,
\]

with the two inverse-pairs carrying independent `C_2^2` voltages. Exact rational checks verify stochasticity/symmetry, the two projection rates, normalizer commutation, and that the voltage span is all of `C_2^2` while `Hom(Z_7,C_2^2)=0`. Numerical matrix exponentials verify the TV sandwich at six times. The class constants are also evaluated. The archived output ends

`ALL_CHECKS_PASS`.

These finite calculations are **sanity checks only**. The asymptotic theorem is proved analytically in Sections 3--7 and does not infer an asymptotic statement from the finite experiment.

## 10. Failed/avoided routes and next attack

The prior `L^2`-only attempt is now understood as quantitatively wasteful when the hidden coordinate has a meaningful TV profile: it pays `\sqrt{|K|}` before using any geometry. Simply pushing that estimate harder cannot reach the present `\alpha=2` family and is not the next route.

The next distinct T08 attack is to weaken exact normalizer commutation. A concrete target is an **approximate conjugacy / bounded-representation transfer**: if every voltage conjugates the hidden transition operator into one of finitely many operators whose mean-zero semigroups share a common TV-contractive envelope, prove a pathwise analogue of (3.4) with a controlled commutator defect. The transitivity-specific hope is that stabilizer orbit representations supply exactly such a finite operator family even when no global product decomposition is visible.

That is the remaining obstruction pursued by NM13-01; P26 remains complementary on entropy/Green/spherical propagation.

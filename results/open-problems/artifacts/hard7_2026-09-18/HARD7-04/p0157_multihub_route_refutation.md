# P0157 — a multi-hub counterexample to the universal one-hub upper route

**Scope.** This note is a self-contained HARD7-04 route result. It does **not** refute the source's prose open problem, which does not state a universal theorem with complete quantifiers. It does refute the stronger route statement used in the preceding HARD7-04 checkpoints:

\[
\forall\varepsilon>0:\qquad
\mathbb P\!\left(L_1>(1+\varepsilon)\frac{d_{\max}}{\delta_n}\right)\to0
\quad\text{whenever}\quad
\frac{d_{\max}\delta_n}{\log(n\delta_n^3)}\to\infty,
\tag{R}
\]

under only the finite-third-moment barely-subcritical configuration-model assumptions. Here

\[
\nu_n=\frac{\sum_i d_i(d_i-1)}{\sum_i d_i},\qquad
\delta_n=1-\nu_n>0.
\]

The obstruction is multiplicity of maximal-degree vertices. A fixed hub is asymptotically isolated from other hubs and obeys the one-hub law, while somewhere among many hubs there is with high probability a direct hub-hub edge. Conditioning on such an edge and contracting it produces a super-root of degree approximately `2d_max`; the finite-population hub law then gives a component of size approximately `2d_max/delta_n`.

## 1. Explicit degree sequence

Let `m` run through even positive integers tending to infinity. Put

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\]

and

\[
x=3m^{11}+\frac{m^5}{4}(m^2-1)^2.
\]

Since `m` is even, `x` is an integer. Define the degree counts

\[
N_d=M,\qquad
N_3=2m^{12}-x,\qquad
N_1=6m^{12}+x-M.
\tag{1.1}
\]

For all sufficiently large even `m`, these are nonnegative integers and sum to `n`. The total degree is even because

\[
\ell_m=N_1+3N_3+dM
      =12m^{12}-2x+(d-1)M
\]

and modulo two this is `n+(d-1)M`, which is even.

The exact simplification is

\[
\boxed{
\ell_m=\frac{m^5}{2}\left(24m^7-12m^6-m^4+4m^2-3\right).
}
\tag{1.2}
\]

The factorial-second-moment numerator is

\[
\sum_i d_i(d_i-1)=6N_3+d(d-1)M.
\]

Using (1.1),

\[
\ell_m-\sum_i d_i(d_i-1)
=N_1-3N_3+d(2-d)M
=4x-(d-1)^2M
=12m^{11}.
\tag{1.3}
\]

Therefore

\[
\boxed{
\delta_m=\frac{12m^{11}}{\ell_m}
=\frac{24m^6}{24m^7-12m^6-m^4+4m^2-3}
=\frac1m(1+o(1)).
}
\tag{1.4}
\]

The limiting empirical degree law is

\[
\mathbb P(D=1)=\frac34,\qquad
\mathbb P(D=3)=\frac14,
\tag{1.5}
\]

because `M/n=m^{-7}/8 ->0` and `x/n=O(m^{-1})`. In particular `p_2=0<1`. Moreover

\[
\frac1n\sum_i d_i^3
=\frac{N_1+27N_3+d^3M}{n}
\longrightarrow \frac{15}{2}<\infty.
\tag{1.6}
\]

Thus the third moments converge, including the hub contribution

\[
\frac{Md^3}{n}=\frac1{8m}\to0.
\]

The family is barely subcritical with

\[
n\delta_m^3\sim 8m^9\to\infty,
\qquad
d\delta_m\sim m\to\infty.
\tag{1.7}
\]

Let

\[
H_m:=\frac d{\delta_m},\qquad
E_m:=\delta_m^{-2}\log(n\delta_m^3).
\]

Then

\[
\frac{H_m}{E_m}
=\frac{d\delta_m}{\log(n\delta_m^3)}
\sim\frac{m}{9\log m}\to\infty.
\tag{1.8}
\]

So this family lies deep in the putative one-hub side of the two-scale comparison.

## 2. The frozen hub-fluctuation metric is small

Let the size-biased forward offspring variable be `xi_m=D_m^*-1`. Its mean is `nu_m=1-delta_m`. Its second moment is

\[
\mathbb E\xi_m^2
=\frac{12N_3+d(d-1)^2M}{\ell_m}.
\]

Hence

\[
\sigma_m^2:=\operatorname{Var}(\xi_m)\to1.
\tag{2.1}
\]

The HARD7-04 frozen metric therefore satisfies

\[
Q_m:=\frac{\sigma_m^2}{d\delta_m}
=\frac1m+O(m^{-2})\to0.
\tag{2.2}
\]

Thus the local branching process is strongly self-averaging. The obstruction below is global and survives despite `Q_m ->0`.

The exact symbolic verification of (1.2)--(1.8), (2.1)--(2.2), and the matching moments used below is in

`artifacts/hard7_2026-09-18/HARD7-04/p0157_multihub_family_exact.py`

with archived output

`artifacts/hard7_2026-09-18/HARD7-04/p0157_multihub_family_exact.out`,

ending `ALL_EXACT_CHECKS_PASS`.

## 3. Many direct edges occur between distinct hubs

Call the `M` degree-`d` vertices hubs, and let `S=Md=m^7` be their total number of half-edges. Let `X_raw` be the number of matched pairs with both half-edges in this hub set, allowing a pair to come from the same hub. For a uniform perfect matching,

\[
\mathbb E X_{\rm raw}=\frac{\binom S2}{\ell_m-1}=:\mu_{\rm raw}.
\tag{3.1}
\]

For two ordered distinct matched hub pairs, four distinct hub half-edges must be selected and paired. Therefore exactly

\[
\mathbb E[X_{\rm raw}(X_{\rm raw}-1)]
=\frac{6\binom S4}{(\ell_m-1)(\ell_m-3)}.
\tag{3.2}
\]

From `S=m^7` and `ell_m~12m^12`,

\[
\mu_{\rm raw}\sim\frac{m^2}{24},
\tag{3.3}
\]

and

\[
\frac{\mathbb E[X_{\rm raw}(X_{\rm raw}-1)]}
     {(\mathbb E X_{\rm raw})^2}\to1.
\tag{3.4}
\]

Since `mu_raw -> infinity`, (3.4) implies

\[
\frac{X_{\rm raw}}{\mu_{\rm raw}}\xrightarrow{L^2}1.
\tag{3.5}
\]

Let `Y` count hub self-loops, i.e. matched pairs whose two half-edges belong to the same hub. Its exact mean is

\[
\mathbb E Y
=\frac{M\binom d2}{\ell_m-1}
\sim\frac1{24m^3}\to0.
\tag{3.6}
\]

Thus `Y=0` with probability tending to one. Writing `X=X_raw-Y` for the number of direct edges between **distinct** hubs and

\[
\mu:=\frac{\binom M2d^2}{\ell_m-1}\sim\frac{m^2}{24},
\tag{3.7}
\]

we obtain

\[
\boxed{
X/\mu\xrightarrow{\mathbb P}1.
}
\tag{3.8}
\]

So there are in fact order `m^2` direct hub-hub edges whp, even though a preselected hub has expected direct hub-degree only

\[
\frac{(M-1)d^2}{\ell_m-1}\sim\frac1{12m^3}\to0.
\tag{3.9}
\]

Equation (3.9) is the exact local/global quantifier split.

## 4. Conditional two-hub law by contraction

Fix two distinct hubs `u,v` and one specified half-edge at each. Let `e` be the event that these two specified half-edges are paired. Conditional on `e`, delete that matched pair and contract `u` and `v` into a single super-root `w`. The remaining perfect matching is uniform on the remaining half-edges, so the contracted graph is exactly a configuration model on the deterministic transformed degree sequence with

\[
d_w=2d-2,
\tag{4.1}
\]

all other degrees unchanged except that `u,v` are removed.

Let `ell_m^*=ell_m-2`, and let `delta_m^*` be the subcriticality parameter of this transformed sequence. The factorial-second-moment numerator changes by

\[
(2d-2)(2d-3)-2d(d-1)=2d^2-8d+6.
\]

Therefore

\[
\ell_m^*\delta_m^*
=12m^{11}-2d^2+8d-8
=12m^{11}-2m^4+8m^2-8.
\tag{4.2}
\]

Consequently

\[
\frac{\delta_m^*}{\delta_m}\to1.
\tag{4.3}
\]

The transformed degree sequence still has total third moment `O(n)`: replacing two degree-`d` vertices by one degree-`2d-2` vertex changes the third-moment sum by only `O(d^3)=O(m^6)=o(n)`. It also satisfies

\[
(n-1)(\delta_m^*)^3\to\infty,
\qquad
(2d-2)\delta_m^*\to\infty.
\tag{4.4}
\]

The super-root `w` is the unique maximal-degree scale in the transformed sequence. Applying the already proved finite-population hub law from

`artifacts/hard7_2026-09-18/HARD7-04/p0157_finite_population_hub_lln.md`

to `w` gives

\[
\frac{|C^*(w)|}{(2d-2)/\delta_m^*}\xrightarrow{\mathbb P}1.
\tag{4.5}
\]

Undoing the contraction adds one vertex to the component. Hence, conditional on the specified direct edge `e`,

\[
\boxed{
\frac{|C(u)|}{H_m}\xrightarrow{\mathbb P}2.
}
\tag{4.6}
\]

The conditional probability in (4.6) is the same for every specified cross-hub half-edge pair by symmetry. In particular, if

\[
p_m:=\mathbb P\!\left(
|C(u)|\le\frac32H_m\;\middle|\;e
\right),
\]

then

\[
p_m\to0.
\tag{4.7}
\]

This use of the one-hub theorem is a self-check route result, not an independent audit of that theorem.

## 5. At least one direct hub edge is good

Let `B` be the number of direct edges between distinct hubs whose endpoint component has size at most `3H_m/2`. Enumerate candidate cross-hub half-edge pairs. Each candidate is matched with probability `1/(ell_m-1)`, and by (4.7), conditional on being matched, it is bad with probability `p_m`. Therefore exactly by linearity of expectation,

\[
\mathbb E B=\mu p_m=o(\mu),
\tag{5.1}
\]

where `mu` is (3.7).

Let `G=X-B` be the number of good direct hub edges. If `G=0` and `X>=mu/2`, then `B>=mu/2`. Hence

\[
\mathbb P(G=0)
\le
\mathbb P(X<\mu/2)+\mathbb P(B\ge\mu/2).
\tag{5.2}
\]

By (3.8) the first term tends to zero, while Markov and (5.1) give

\[
\mathbb P(B\ge\mu/2)
\le\frac{2\mathbb E B}{\mu}
=2p_m\to0.
\tag{5.3}
\]

Thus

\[
\boxed{
\mathbb P\!\left(L_1>\frac32H_m\right)\to1.
}
\tag{5.4}
\]

But (1.8) has `H_m/E_m -> infinity`. Therefore the universal route statement (R), specialized to `epsilon=1/2`, would require the probability in (5.4) to tend to zero. This contradiction proves:

> **Route theorem.** Under only finite-third-moment convergence, `p_2<1`, `delta_n ->0`, `n delta_n^3 -> infinity`, and `H_n/E_n -> infinity`, it is false in general that `L_1/H_n ->1`. The explicit family (1.1) instead has `P(L_1>3H_n/2)->1`.

This is a theorem-sized self-check with a complete proof on the page. It is not labeled a refutation of the source's open problem because the source phrases the high-degree regime as a prediction with unspecified qualifiers such as “sufficiently slowly” and “sufficiently large”, rather than the universal quantified assertion (R).

## 6. What this changes in the P0157 route

The source-level crossover cannot be parameterized by `d_max` and `delta_n` alone under the weakest finite-third-moment assumptions. A third piece of information is needed to control multiplicity/interaction of high-degree vertices. The direct-edge calculation already exposes the parameter

\[
\Lambda_{\rm dir}
:=\frac{M_nd_n^2}{\ell_n},
\tag{6.1}
\]

which is the expected direct hub-degree of a chosen hub when there are `M_n` comparable hubs. In the present family `Lambda_dir ~1/(12m^3)->0`, yet `M_n Lambda_dir -> infinity`, so a fixed hub is clean while some pair merges whp.

A more relevant next object should include indirect subcritical exploration between hubs. The natural first-order connection scale is heuristically

\[
p_{\rm hub}\asymp\frac{d_n^2}{\ell_n\delta_n},
\tag{6.2}
\]

because each root contributes order `d_n/delta_n` exploration opportunities. For the explicit family, (6.2) is of order `m^{-7}`. This predicts many two-hub and even three-hub merger opportunities, but (6.2) is **not proved here** and is recorded only as the next route. A rigorous version would turn the vague two-scale picture into a multi-hub kernel/coalescent problem rather than a one-dimensional comparison of `H_n` and `E_n`.

## 7. Status and literature caution

The source is Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255. That page explicitly calls the finite-third-moment barely-subcritical behavior an interesting open problem, recalls Janson's strictly subcritical high-degree law, contrasts it with the Erdos--Renyi barely-subcritical scale, and says this suggests a phase transition in the subcritical regime.

A bounded current-literature refresh on 19 September 2026 again found Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence* (EJP 28 (2023), arXiv:2111.11780), which gives general CM upper bounds and sharpness for some sequences, and Janson's 2008 power-law theorem. No surfaced result was identified as the exact universal assertion (R) or as this explicit multiplicity counterexample. This is negative search evidence only and is not a novelty certification.

**Status:** `PARTIAL` for P0157; route statement (R) `REFUTED`; source residual remains `OPEN`.

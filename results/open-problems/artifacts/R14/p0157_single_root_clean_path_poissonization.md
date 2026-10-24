# P0157 — single-root clean-path Poissonization in the actual configuration model

**Status.** R14 theorem-sized self-check / **PARTIAL** progress on van der Hofstad's finite-third-moment barely-subcritical configuration-model crossover problem. This note does **not** solve the source problem and does **not** claim novelty. It proves a quantitative one-root approximation for the actual pairing model: after declaring a deterministic high-degree set absorbing, the vector of first clean hits from one marked root is close in total variation to independent Poisson variables with the rank-one means already suggested by the branching surrogate.

The result is deliberately one-row. It does **not** prove that the whole compressed high-degree graph has independent edges. That simultaneous coupling remains the next obstruction.

## 1. Setup

Let `d=(d_1,...,d_n)` be a deterministic degree sequence with even total degree

\[
\ell=\sum_{v=1}^n d_v,
\]

and let `CM(d)` be the configuration-model multigraph. Assume

\[
\nu:=\frac1\ell\sum_v d_v(d_v-1)<1,
\qquad
\sum_v d_v^3\le Cn,
\qquad
\ell\ge cn
\tag{1.1}
\]

for fixed `c,C>0`. Put `C_0=C/c`.

Fix a deterministic marked set `H subseteq [n]` and write `B=[n]\\H`. Define the absorbing-bulk deficit

\[
\delta_H
:=1-\frac1\ell\sum_{v\in B}d_v(d_v-1)>0,
\qquad
S_H:=\sum_{h\in H}d_h.
\tag{1.2}
\]

Fix `i in H` with `d_i>0`.

### The actual absorbing exploration

Start from all `d_i` half-edges incident to `i`. Pair active half-edges according to the configuration-model pairing. When the partner belongs to a marked vertex `h in H`, record one hit of `h` and do not continue through `h`. When the partner is a new bulk vertex `v in B`, activate its remaining half-edges. Continue until there are no active half-edges.

Let

\[
N_{ih}:=\text{number of boundary hits of marked vertex }h
\]

for `h in H\\{i}`. Equivalently, `N_{ih}>0` iff the `H`-compressed graph has a direct `H`-avoiding connection from `i` to `h`; all internal vertices of the corresponding explored route lie in `B`. The vector

\[
\mathbf N_i=(N_{ih})_{h\in H\\{i}}
\tag{1.3}
\]

is the one-row clean-hit process we approximate.

Define the rank-one intensities

\[
\mu_{ih}:=\frac{d_i d_h}{\ell\delta_H},
\qquad
\mu_{ii}:=\frac{d_i^2}{\ell\delta_H},
\qquad
\lambda_i:=\sum_{h\in H}\mu_{ih}
=\frac{d_iS_H}{\ell\delta_H}.
\tag{1.4}
\]

Also define

\[
\beta_H:=\frac1\ell\sum_{v\in B}d_v(d_v-1)(d_v-2).
\tag{1.5}
\]

By (1.1), `0<=beta_H<=C_0`.

## 2. Quantitative theorem

### Theorem 2.1 — one-root Poissonization

Assume `lambda_i<=1`. Let `R` be any integer with `1<=R<=ell/4`. Let

\[
\mathbf Z_i=(Z_{ih})_{h\in H\\{i}},
\qquad
Z_{ih}\ \text{independent with}\ 
Z_{ih}\sim\operatorname{Poi}(\mu_{ih}).
\tag{2.1}
\]

Then

\[
\boxed{
 d_{\rm TV}(\mathcal L(\mathbf N_i),\mathcal L(\mathbf Z_i))
 \le
 \frac{d_i}{\delta_H R}
 +\frac{2R^2}{\ell}
 +\mu_{ii}
 +\lambda_i^2\left(2+\frac{C_0}{d_i\delta_H}\right).
}
\tag{2.2}
\]

Consequently, if along a sequence

\[
\chi_i:=\left(\frac{d_i^2}{\ell\delta_H^2}\right)^{1/3}\to0,
\qquad
\lambda_i\to0,
\qquad
 d_i\delta_H\to\infty,
\tag{2.3}
\]

then

\[
\boxed{
 d_{\rm TV}(\mathcal L(\mathbf N_i),
 \bigotimes_{h\ne i}\operatorname{Poi}(d_id_h/(\ell\delta_H)))\to0.
}
\tag{2.4}
\]

Indeed, with

\[
R=\left\lfloor\left(\frac{\ell d_i}{\delta_H}\right)^{1/3}\right\rfloor
\tag{2.5}
\]

(the harmless nearest admissible integer for large `n`), the first two terms in (2.2) are `3 chi_i+o(1)`. Further, `mu_ii<=d_i^2/(ell delta_H^2)=chi_i^3` because `delta_H<=1`.

### Corollary 2.2 — independent rank-one neighbour row

Apply the coordinatewise map `x -> 1{x>=1}` to (2.4). Then the neighbour indicators

\[
I_{ih}:=\mathbf1\{N_{ih}>0\}
\]

are jointly asymptotic, for this **single fixed root `i`**, to independent Bernoulli variables with

\[
\boxed{
 p_{ih}=1-\exp\left\{-\frac{d_id_h}{\ell\delta_H}\right\}.
}
\tag{2.6}
\]

Thus the rank-one kernel is recovered from the actual configuration model at the level of one marked row, not merely in an ideal branching surrogate.

### Corollary 2.3 — a dyadic top-band sufficient regime

Let

\[
H(a):=\{v:d_v\ge a\},
\qquad
D(a):=\{v:a\le d_v<2a\},
\]

and let `delta_a,S_a` mean `delta_H,S_H` with `H=H(a)`. If

\[
a\delta_a\to\infty,
\qquad
\frac{aS_a}{\ell\delta_a}\to0,
\qquad
\frac{a^2}{\ell\delta_a^2}\to0,
\tag{2.7}
\]

then uniformly for `i in D(a)`, the clean-hit vector from `i` to all of `H(a)\\{i}` is asymptotically independent Poisson with means `d_i d_h/(ell delta_a)`. In particular, restricting coordinates to the single dyadic band `D(a)` gives the one-band Poisson row sought in the first P0157 stuck recovery.

The conditions in (2.7) are sufficient, not claimed optimal.

## 3. With-replacement absorbing branching process

The comparison process starts from `d_i` independent particles. Each processed particle independently samples one half-edge uniformly from the full `ell` half-edge population. If its sampled endpoint is `h in H`, it records one hit of color `h` and has no children. If its sampled endpoint is `v in B`, it has `d_v-1` children.

The offspring variable `X` therefore satisfies

\[
\mathbb E X
=\frac1\ell\sum_{v\in B}d_v(d_v-1)
=1-\delta_H<1.
\tag{3.1}
\]

Let `Y_h` be the total number of hits of mark `h` from the `d_i` ancestors, let

\[
\mathbf Y_i=(Y_h)_{h\in H},
\qquad
M:=\sum_{h\in H}Y_h.
\tag{3.2}
\]

The total progeny `T` of the entire absorbing branching process has

\[
\boxed{\mathbb ET=\frac{d_i}{\delta_H}.}
\tag{3.3}
\]

This first moment is all that is needed for the finite-population coupling below.

## 4. Exact first and second factorial moments of marked hits

Set

\[
s:=S_H/\ell.
\]

For one initial particle, let

\[
f(z):=\mathbb E[z^M].
\]

Conditioning on its sampled label gives the exact fixed-point equation

\[
 f(z)
 =sz+\frac1\ell\sum_{v\in B}d_v f(z)^{d_v-1}.
\tag{4.1}
\]

Differentiating at `z=1`, using `f(1)=1`, gives

\[
 f'(1)=\frac{s}{\delta_H}.
\tag{4.2}
\]

Differentiating twice gives

\[
 f''(1)=\frac{\beta_Hs^2}{\delta_H^3}.
\tag{4.3}
\]

For `d_i` independent ancestors, therefore,

\[
\boxed{
\mathbb EM=\lambda_i=\frac{d_iS_H}{\ell\delta_H},
}
\tag{4.4}
\]

and

\[
\begin{aligned}
F_{2,i}
&:=\mathbb E[M(M-1)]\\
&=d_i\frac{\beta_Hs^2}{\delta_H^3}
+d_i(d_i-1)\frac{s^2}{\delta_H^2}\\
&\le
\lambda_i^2\left(1+\frac{C_0}{d_i\delta_H}\right).
\end{aligned}
\tag{4.5}
\]

For a specified color `h`, the same branching recursion gives the **exact** first moment

\[
\boxed{
\mathbb E Y_h=\frac{d_i d_h}{\ell\delta_H}=\mu_{ih}.
}
\tag{4.6}
\]

Thus the target Poisson vector has exactly the same coordinate means as the branching marked-hit vector.

## 5. A small Poisson-vector lemma

### Lemma 5.1

Let `Y=(Y_j)` be any nonnegative integer-valued vector, let `M=sum_jY_j`, and let

\[
\mu_j=\mathbb E Y_j,
\qquad
\mu=\sum_j\mu_j\le1,
\qquad
F_2=\mathbb E[M(M-1)].
\]

Let `Z_j` be independent `Poi(mu_j)`. Then

\[
\boxed{
 d_{\rm TV}(\mathcal L(Y),\mathcal L(Z))
 \le F_2+\mu^2.
}
\tag{5.1}
\]

### Proof

Introduce the probability law `W` supported on `0` and the unit coordinate vectors `e_j` by

\[
W(0)=1-\mu,
\qquad
W(e_j)=\mu_j.
\]

For `Y`, the discrepancy from `W` is concentrated on the event `M>=2`. In fact a direct calculation gives

\[
d_{\rm TV}(\mathcal L(Y),W)
=\mathbb E[M\mathbf1_{\{M\ge2\}}]
\le\mathbb E[M(M-1)]=F_2.
\tag{5.2}
\]

For the independent Poisson vector `Z`, its total is `Poi(mu)` and its second factorial moment is `mu^2`, so the same argument yields

\[
d_{\rm TV}(\mathcal L(Z),W)\le\mu^2.
\tag{5.3}
\]

The triangle inequality proves (5.1). `square`

Applying Lemma 5.1 to `mathbf Y_i` and independent Poisson variables of means `(mu_ih)_{h in H}` gives

\[
\boxed{
 d_{\rm TV}(\mathcal L(\mathbf Y_i),
 \bigotimes_{h\in H}\operatorname{Poi}(\mu_{ih}))
 \le
 \lambda_i^2\left(2+\frac{C_0}{d_i\delta_H}\right).
}
\tag{5.4}
\]

Discarding the `i` coordinate can only decrease total variation.

## 6. Coupling the actual pairing exploration to the branching process

Pre-generate an iid sequence of uniformly sampled half-edges for the branching process. As long as the actual absorbing exploration and the branching process have remained identical, process the corresponding active half-edge in each.

After `t` actual pairings, exactly `2t` half-edges have been removed. Conditional on the history, the actual partner is uniform on the `ell-2t-1` half-edges other than the chosen active half-edge. A fresh iid uniform half-edge from all `ell` half-edges can therefore be coupled to that actual partner with failure probability exactly

\[
\frac{2t+1}{\ell}.
\tag{6.1}
\]

Summing (6.1) for `t=0,...,R-1` gives the depletion bound

\[
\boxed{
P(\text{finite-population coupling fails by time }R)
\le\frac{R^2}{\ell}.
}
\tag{6.2}
\]

There is one further discrepancy: the with-replacement branching process may sample two distinct half-edges belonging to the same bulk vertex and treat the second appearance as fresh. Among the first `R` iid half-edge samples,

\[
\begin{aligned}
P(\text{some bulk vertex label repeats})
&\le {R\choose2}\sum_{v\in B}\left(\frac{d_v}{\ell}\right)^2\\
&\le {R\choose2}\frac{\sum_vd_v^2}{\ell^2}.
\end{aligned}
\tag{6.3}
\]

Since global subcriticality gives

\[
\sum_vd_v^2
=\ell+\sum_vd_v(d_v-1)
=\ell(2-\delta)<2\ell,
\qquad \delta=1-\nu>0,
\tag{6.4}
\]

we get

\[
\boxed{
P(\text{a bulk label repeats among the first }R\text{ samples})
<\frac{R^2}{\ell}.
}
\tag{6.5}
\]

Finally, the root `i` is itself marked. If the branching process samples another half-edge of `i`, the actual process can consume another root-active half-edge and the queues cease to match. Declare this a coupling failure. By (4.6),

\[
\boxed{
P(\text{the branching process ever hits }i)
\le\mathbb E Y_i=\mu_{ii}.
}
\tag{6.6}
\]

If none of the events (6.2), (6.5), (6.6) occurs and `T<=R`, then every sampled bulk vertex is new, the two active queues agree step for step until extinction, and the actual marked-hit vector equals the branching marked-hit vector off the self-coordinate.

By (3.3) and Markov's inequality,

\[
P(T>R)\le\frac{d_i}{\delta_HR}.
\tag{6.7}
\]

Therefore

\[
\boxed{
 d_{\rm TV}(\mathcal L(\mathbf N_i),
 \mathcal L((Y_h)_{h\in H\\{i}}))
 \le
 \frac{d_i}{\delta_HR}
 +\frac{2R^2}{\ell}
 +\mu_{ii}.
}
\tag{6.8}
\]

Combining (6.8) with (5.4) proves Theorem 2.1.

## 7. Optimizing the truncation

Ignoring integer rounding, choose

\[
R=\left(\frac{\ell d_i}{\delta_H}\right)^{1/3}.
\]

Then

\[
\frac{d_i}{\delta_HR}
=\left(\frac{d_i^2}{\ell\delta_H^2}\right)^{1/3}
=\chi_i,
\]

and

\[
\frac{2R^2}{\ell}=2\chi_i.
\]

Thus (2.2) becomes

\[
 d_{\rm TV}
\le
3\chi_i+\mu_{ii}
+\lambda_i^2\left(2+\frac{C_0}{d_i\delta_H}\right)+o(1),
\tag{7.1}
\]

which tends to zero under (2.3).

## 8. What method #9 accomplished

The randomization is the with-replacement absorbing branching process. It provides an exactly solvable intermediary with two advantages:

1. its marked-hit first and second factorial moments are explicit through the scalar pgf (4.1);
2. it can be coupled to the actual finite pairing using only three concrete defect events: depletion, repeated bulk labels, and root self-hits.

This turns the previous marginal kernel calculation into a genuine **one-root joint law**.

## 9. What method #20 says still fails

The obvious algorithm would now expose every marked root row independently and glue the rows into an inhomogeneous random graph. That is not valid. Rows in the true compressed graph share the same underlying pairing and the same bulk vertices. An `i-j` clean connection is the same undirected object when viewed from `i` and `j`, and simultaneous explorations can collide even when every individual row has a good coupling.

Therefore Theorem 2.1 cannot be iterated naively to obtain a global independent-edge graph. The remaining blocker is a **simultaneous** exploration/coupling theorem on the number of marked roots needed to determine the largest tail component, with a collision budget compatible with the preceding dyadic Steiner penalty.

## 10. What method #24 identifies as the extremal defect

At one-root level, after the branching randomization the first obstruction is not a complicated large core. It is the smallest possible failure of fresh-tree structure: a repeated bulk vertex. Equations (6.3)-(6.5) show that all such first collisions are controlled in aggregate by `R^2/ell`. Root self-contact contributes `mu_ii`, and pure finite-population depletion contributes the same `R^2/ell` scale.

So for one row the entire dependence mechanism collapses to a minimal collision defect. The next global theorem must understand how those defects accumulate when **many** rows are exposed together.

## 11. Relation to prior art

This theorem should not be advertised as a novelty claim without a much deeper citation search. Mariana Olvera-Cravioto's *Strong couplings for static locally tree-like random graphs* (J. Appl. Probab. 59 (2022), 1261-1285; arXiv:2102.10673) already gives general couplings of configuration-model explorations to marked Galton-Watson limits for **fixed breadth-first depth**. The present argument is a specialized quantitative total-progeny/rare-mark estimate tailored to the near-critical P0157 route; the bounded search did not establish whether this exact one-row total-variation formulation is implicit elsewhere.

Coulson-Perarnau (EJP 28 (2023), arXiv:2111.11780) gives strong largest-component upper bounds for subcritical configuration models but does not supply the source's full finite-third-moment crossover theorem or the simultaneous marked-tail coupling required here.

## 12. Scope and next obligation

The result proves a complete special case selected in R14's first stuck recovery:

- actual configuration-model pairing, not only an ideal branching model;
- a growing deterministic marked set is allowed;
- the full one-root vector of clean marked hits is approximated jointly;
- the limiting row is the rank-one Poisson/Bernoulli row.

It remains **PARTIAL** because source closure needs the joint compressed high-degree graph and then a selection-safe bulk-mass map. The next logically distinct step is simultaneous multi-root Poissonization or a switching/Stein-Chen theorem whose error remains small on the extreme marked-component scale.
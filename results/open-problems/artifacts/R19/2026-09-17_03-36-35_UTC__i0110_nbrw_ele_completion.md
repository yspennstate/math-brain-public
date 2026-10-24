# R19 / I0110 — completing the frozen ELE test on Salez references [14] and [13]

Status: **INTERNAL 9/9 COMMON-CERTIFICATE SATURATION / SOURCE-SCOPE AUDIT PENDING.**

This note does not claim that Salez Problem 2.1 is closed. It proves that the *same frozen Entropic Lift-Extraction (ELE) certificate* from

`artifacts/R19/2026-09-17_01-37-22_UTC__i0110_ele_certificate.md`

also covers the last two uncatalogued source families in Salez's list, namely:

- [14] A. Ben-Hamou and J. Salez, *Cutoff for non-backtracking random walks on sparse random graphs*, Ann. Probab. 45 (2017), arXiv:1504.02429;
- [13] A. Ben-Hamou, *A threshold for cutoff in two-community random graphs*, Ann. Appl. Probab. 30 (2020), arXiv:1809.07243.

The proof uses only the source exploration architectures plus the **two-sided** versions of concentration estimates already present in, or explicitly cited by, those proofs. No total-variation conclusion is inserted into the hypotheses.

## 1. Frozen ELE target

For a source-relevant chain with stationary law `pi_N`, the frozen certificate requires times

\[
t_N^-<t_N^+,
\qquad t_N^+/t_N^-\to1,
\]

a structural pre-threshold lift whose `1-o(1)` mass projects into a set of stationary mass `o(1)`, and a structural post-threshold retained subprobability `r_N` of mass `m_N->1` such that

\[
D_N:=\sum_y\frac{(r_N(y)-m_N\pi_N(y))^2}{\pi_N(y)}\to0.
\tag{1.1}
\]

The earlier R19 theorem `R19-I0110-C008` proves that this deterministic certificate implies cutoff. The definition itself is not changed here.

Both remaining models have uniform stationary law on their half-edge state spaces, so `pi_N(y)=1/N`.

## 2. A deterministic flattening lemma

### R19-I0110-C013 — uniform structural flattening implies ELE-U

Let `p_N` be a probability on `N` states and let `s_N<=p_N` be a structurally specified subprobability. Suppose there is a bad set `B_N` with

\[
|B_N|=o(N)
\]

and numbers `delta_N->0` such that

\[
\sup_{y\notin B_N}|N s_N(y)-1|\le\delta_N.
\tag{2.1}
\]

Put `r_N=s_N 1_{B_N^c}` and `m_N=sum_y r_N(y)`. Then `m_N->1` and

\[
\sum_y\frac{(r_N(y)-m_N/N)^2}{1/N}\to0.
\tag{2.2}
\]

**Proof.** Write `b_N=|B_N|/N=o(1)`. From (2.1),

\[
(1-b_N)(1-\delta_N)\le m_N\le(1-b_N)(1+\delta_N),
\]

so `m_N->1`. Moreover

\[
D_N=\frac1N\sum_y(Nr_N(y)-m_N)^2.
\]

For `y notin B_N`, the summand is at most `(delta_N+|1-m_N|)^2`; on `B_N` it equals `m_N^2`. Hence

\[
D_N\le (\delta_N+|1-m_N|)^2+b_Nm_N^2\to0.
\]

`QED`

If the source first runs the chain for `K_N=o(t_N^+)` steps to reach a set of good roots with probability `1-o(1)`, and every root has a subprobability satisfying (2.1) uniformly, then mixing over the reached root preserves (2.2): for centered vectors `v_z=s_z-m_z pi`, convexity of the squared `L^2(pi^{-1})` norm gives

\[
\left\|\sum_z a_zv_z\right\|_{L^2(\pi^{-1})}^2
\le\sum_z a_z\|v_z\|_{L^2(\pi^{-1})}^2.
\tag{2.3}
\]

Thus the standard source root-reduction steps are compatible with the same ELE-U clause.

## 3. Diagonal choice of the cutoff-profile parameter

Both source papers prove fixed-profile-parameter estimates at

\[
t=t_*+\lambda\omega_*.
\]

Their cutoff windows satisfy `omega_*=o(t_*)`. Consequently there exists a deterministic sequence

\[
\lambda_N\uparrow\infty,
\qquad
\lambda_N\omega_*/t_*\to0,
\tag{3.1}
\]

so slowly that every finite list of fixed-`lambda`, fixed-`epsilon` source estimates used below remains valid after replacing the fixed parameter by `lambda_N`, with errors tending to zero. This is the standard diagonal argument: for integer `k`, first choose `N_k` so all estimates needed with `|lambda|<=k` and `epsilon>=1/k` hold for `N>=N_k`, then take `lambda_N` to be the largest `k` allowed by both `N>=N_k` and `k omega_*/t_*<=1/k`.

Set

\[
t_N^-=t_*-\lambda_N\omega_*,
\qquad
t_N^+=t_*+\lambda_N\omega_*.
\tag{3.2}
\]

Then `t_N^+/t_N^-->1` in the required sense, i.e.

\[
\frac{t_N^+}{t_N^-}\to1.
\tag{3.3}
\]

## 4. Salez reference [14]: sparse configuration-model NBRW

### 4.1 ELE-L is already the source lower-bound mechanism

Ben-Hamou--Salez define for a path its quenched weight, the product of inverse forward degrees. Take

\[
\theta_N^-:=\frac{\log N}{N}
\]

and let `E_N^-` be the set of length-`t_N^-` trajectories whose path weight exceeds `theta_N^-`. The endpoint image has cardinality at most `1/theta_N^-`, because every endpoint in that image receives transition mass at least `theta_N^-`. Therefore

\[
\pi_N(\Phi(E_N^-))\le\frac1{N\theta_N^-}=\frac1{\log N}\to0.
\tag{4.1}
\]

Equations (17)--(19) of [14] couple the degrees seen by the walk to iid uniform half-edge samples and apply Berry--Esseen. At `t_N^-`, the diagonal choice (3.1) makes the annealed probability of `E_N^-` tend to one. Since its deficiency is nonnegative and bounded by one, Markov's inequality upgrades this to the quenched `q_N^-(E_N^-)=1-o(1)` statement with high probability. This is exactly ELE-L.

### 4.2 The source upper proof contains a two-sided concentration inequality

At the post-entropic time the source's Section 5 exposure constructs two exploration trees and retains only completion pairs with product weight at most

\[
\theta_N:=\frac1{N(\log N)^2}.
\tag{4.2}
\]

For a pair of roots `x,y`, let `S_{x,y}` denote the retained completion contribution to the transition probability. It is a structurally specified subprobability contribution to the true kernel.

Conditioned on the exploration, [14, Lemma 6.1] centers this sum at

\[
m_{x,y}=\frac{\mathfrak W_{x,y}}{|\mathcal I|-1}
\]

and, crucially, states **both** tails. In the notation of that lemma,

\[
\Pr(Y\le-a)\le e^{-a^2/c},
\qquad
\Pr(Y\ge a)\le e^{-a^2/(ab+c)},
\tag{4.3}
\]

with `b=2 theta_pair`, `c=4m theta_pair`.

The published proof only needs the first inequality, but the second one is on the same page and has already been proved by the same exchangeable-pair calculation.

The source's Lemmas 5.2--5.4 imply, after the diagonal choice `lambda_N->infty`, uniformly over the admissible root pairs,

\[
|\mathcal I|=N-o(N),
\qquad
\mathfrak W_{x,y}=1-o(1).
\tag{4.4}
\]

Here the heavy-product remainder tends to zero because the profile tail tends to zero at `lambda_N->infty`, while the exploration loses only `o(1)` boundary mass. Thus

\[
Nm_{x,y}=1+o(1).
\tag{4.5}
\]

Take `a_N=epsilon_N/N` with `epsilon_N=(log N)^(-1/4)`. Since `theta_pair=O(1/[N(log N)^2])` and `m=O(1/N)`, each tail in (4.3) is at most

\[
\exp\{-\Omega(\epsilon_N^2(\log N)^2)\}
=
\exp\{-\Omega((\log N)^{3/2})\}.
\tag{4.6}
\]

A union bound over all `O(N^2)` root pairs therefore gives

\[
\sup_{x,y\text{ admissible}}|N S_{x,y}-1|=o(1)
\tag{4.7}
\]

with high probability.

The excluded local ball around a root has size `o(N)`, and the source's Proposition 4.1 shows that non-roots are reached with only `o(1)` mass after its preliminary `h=o(t_*)` reduction. Apply C013 rootwise and then (2.3) to the preliminary-root mixture. This gives the frozen ELE-U condition for every source-relevant start.

Therefore [14] is an ELE match.

## 5. Salez reference [13]: two-community NBRW

Assume the source cutoff regime

\[
\alpha_N\log N\to\infty.
\tag{5.1}
\]

The source location is `t_*=log N/mu` and its window is

\[
\omega_N=\sqrt{\frac{\nu^2\log N}{\mu^3}}
=O\!\left(\sqrt{\frac{\log N}{\alpha_N}}\right)=o(\log N).
\tag{5.2}
\]

Also `alpha_N^{-1}=o(omega_N)`, exactly the separation used in the source proof.

### 5.1 ELE-L

Section 3.1 of [13] repeats the high-path-weight construction with

\[
\theta_N^-=(\log N)/N.
\]

For a fixed start `x`, the image set `A_theta` has at most `1/theta` states, hence stationary mass at most `1/log N`. The coupling (2.1) and Lemma 2.1 give the required path-logweight normal approximation uniformly in the initial half-edge. At `t_N^-` from (3.2), the same diagonal argument gives retained path mass `1-o(1)` in probability over the graph. Thus ELE-L holds.

### 5.2 Why the one-sided published upper proof can be upgraded without changing its architecture

For root pairs `x,y`, Section 3.2 uses the same two-tree identity and truncates at

\[
\theta_N=\frac1{N(\log N)^3}.
\tag{5.3}
\]

The proof then averages in three stages:

1. uniform pairings of internal half-edges;
2. uniform bipartite matchings of outgoing half-edges;
3. random internal/outgoing type assignments.

The paper only records the lower-deviation events because a pointwise lower bound is sufficient for its total-variation upper bound. But all three concentration engines used there are actually two-sided:

- internal pairings invoke [14, Lemma 6.1], whose displayed statement is (4.3), including the upper tail;
- outgoing matchings invoke Chatterjee, *Stein's method for concentration inequalities*, Proposition 1.1. For a uniform permutation statistic `X=sum a_{i,pi(i)}` with entries in `[0,1]`, that proposition gives
  \[
  \Pr(|X-EX|\ge t)\le2\exp\left\{-\frac{t^2}{4EX+2t}\right\};
  \tag{5.4}
  \]
- type assignment invokes Pemantle--Peres, Theorem 3.2 for strong Rayleigh measures; that theorem explicitly gives the corresponding two-sided concentration estimate.

Thus every one-sided concentration replacement in Lemma 3.5 may be made two-sided while keeping the identical exploration, truncation and conditional means.

For completeness, the potentially weakest outgoing-matching rate is still enough uniformly. The normalized summands are bounded by

\[
c_N:=N\theta_N=(\log N)^{-3}.
\]

The relevant conditional mean is `O(1/alpha_N)`. Scaling (5.4) from `[0,1]` to `[0,c_N]` gives, for a normalized deviation `epsilon`,

\[
\Pr(|X-EX|>\epsilon)
\le
2\exp\{-\Omega(\epsilon^2\alpha_N(\log N)^3)\}.
\tag{5.5}
\]

Choose, for example,

\[
\epsilon_N=(\alpha_N(\log N)^2)^{-1/4}.
\tag{5.6}
\]

Then `epsilon_N->0` by (5.1), and

\[
\frac{\epsilon_N^2\alpha_N(\log N)^3}{\log N}
=
\epsilon_N^2\alpha_N(\log N)^2
=
\sqrt{\alpha_N}\,\log N
=
\sqrt{(\alpha_N\log N)\log N}\to\infty.
\tag{5.7}
\]

Hence even after a union bound over `O(N^2)` ordered root pairs, the outgoing-matching deviations are `o(1)` uniformly. The internal-pairing bound is stronger. For the strong-Rayleigh type-assignment terms one may either use their explicit polynomially vanishing Lipschitz constants from the source or simply include them in the slow diagonal choice of `epsilon_N`; no new probabilistic input is needed.

### 5.3 Conditional means flatten to `1/N`

Let `W_{ij}` be the four full boundary-product masses of [13]. Lemma 3.4 gives

\[
W_{ij}\ge\frac{N_iN_j}{N^2}-o(1)
\tag{5.8}
\]

uniformly. Their four comparison values sum to one. On the other hand the sum of the four `W_{ij}` is the product of the two total surviving boundary masses and is at most one. Therefore (5.8) automatically upgrades to the two-sided statement

\[
W_{ij}=\frac{N_iN_j}{N^2}+o(1)
\tag{5.9}
\]

for every `i,j`.

Lemma 3.6 controls the heavy-product complement. At the diagonal post-threshold parameter `lambda_N->infty`, its Gaussian-tail factor tends to zero, so

\[
\overline W_{ij}^{\theta}=o(1)
\tag{5.10}
\]

uniformly. Therefore the deterministic conditional means of the retained low-product matching sums equal their equilibrium values up to `o(1/N)`.

Combining (5.9)--(5.10) with the two-sided concentration upgrade in Section 5.2 yields a structurally defined retained subkernel `S_{x,y}` with

\[
\sup_{x\in\mathcal R,
\ y\in\mathcal R\setminus\mathcal B_x}
|N S_{x,y}-1|=o(1)
\tag{5.11}
\]

with high probability.

The source has `|B_x|<=N^{1/6}=o(N)`. Lemma 3.1 gives a preliminary root-hitting time `K=floor(log log N)` with non-root probability `o(1)` uniformly in the start. Since `K=o(t_*)`, C013 plus the mixture inequality (2.3) proves frozen ELE-U.

Therefore [13] is an ELE match in exactly the source cutoff regime `alpha_N log N -> infinity`.

## 6. Method accounting

The assigned methods were not cosmetic labels.

### #6 DEFORM TO A POINT YOU CAN SOLVE

The one-community model [14] is the solvable endpoint of the two-community architecture [13]. The [13] proof deforms away from it by adding a two-state community coordinate. Condition (5.1) says that this coordinate mixes on scale `alpha^{-1}` strictly below the cutoff window, which is exactly why the [14] extraction architecture survives the deformation.

### #11 DUALIZE

The published upper proofs use one-sided lower bounds on `P^t(x,y)` because total variation can be controlled through deficits. ELE-U asks instead for a centered quadratic collision defect. Passing to the dual matching statistic shows that the already-present exchangeable-pair machinery controls both signs, and the missing `L^2` statement becomes a two-sided concentration question around the same conditional mean.

### #29 ADD THE POINTS AT INFINITY

The source truncations discard high-product paths and prematurely stopped exploration branches. Treating all discarded contribution as a single cemetery component makes the mass accounting exact: the retained kernel is a subprobability and the entire discarded part is charged by `1-m_N`. No hidden normalization is needed. This is precisely the bookkeeping built into ELE-U.

## 7. Metric consequence

The frozen common property now has internally proved matches for all nine Salez source references:

\[
[80,16,14,21,13,61,22,52,62].
\]

Thus the fixed active metric moves

\[
\boxed{M_9:7/9\longrightarrow9/9.}
\]

This is **metric saturation, not source closure**.

The remaining obligations are qualitative and audit-level:

1. an independent source-scope audit must decide whether ELE, which is an explicit deterministic structural proof certificate using model-generated lifts/extractors, is sufficiently intrinsic to count as the `structural property` requested by Salez rather than merely a common formalization of proof architecture;
2. the source-family matches and the deterministic C008 implication need two independent OTHER-track end-to-end audits under the fleet closure rule;
3. novelty is not claimed. The component entropic/exploration/L2 mechanisms are largely present in the cited papers; the contribution here is the common frozen certificate and the exact cross-model verification.

Until those obligations are met the honest status is **PARTIAL / 9-OF-9 COMMON-CERTIFICATE CANDIDATE / SOURCE OPEN / AUDIT PENDING**.

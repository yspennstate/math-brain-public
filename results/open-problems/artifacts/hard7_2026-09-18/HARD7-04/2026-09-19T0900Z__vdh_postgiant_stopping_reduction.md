# HARD7-04 — post-giant stopping-time reduction for barely-supercritical configuration-model duality

**Status:** analytic route theorem / PARTIAL only. This note uses the published barely-supercritical exploration theorem of van der Hofstad--Janson--Luczak (2019) as an input. It does **not** determine the sharp scale of the second-largest component. It does remove the artificial “condition on the complement of the largest component” obstruction from the present duality route and upgrades the ideal reflected drift to an exact configuration-model remainder at a lawful exploration stopping time.

## 1. Published inputs and notation

Consider a deterministic degree sequence satisfying the finite-third-moment barely-supercritical hypotheses of the active `VDH-8.3-DUALITY` claim:

\[
\nu_n=1+\varepsilon_n,\qquad
\varepsilon_n\downarrow0,\qquad
\varepsilon_n n^{1/3}\to\infty,
\qquad
\frac1n\sum_i d_i^3\to \mathbb E D^3<\infty,
\tag{1.1}
\]

with a nondegenerate critical limiting degree law and positive limiting mean degree.

Let `G_n` denote the unique giant component and let `H(C)=\sum_{v\in C}d_v=2|E(C)|` be the half-edge volume of a component. The 2019 paper

Remco van der Hofstad, Svante Janson, and Malwina Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019), 3--55, DOI `10.1002/rsa.20837`,

provides the following ingredients in this regime (in its continuous-time exploration proof):

1. `H(G_n)=Theta_p(n epsilon_n)` and every other component has half-edge volume `o_p(n epsilon_n)`;
2. the component containing the giant is explored on the extinction-log clock scale
   \[
   \alpha_n=-\log(1-\rho_n),
   \tag{1.2}
   \]
   where `rho_n` is the survival probability of the size-biased excess branching process; if `T_{2,n}` is the end of that large excursion, then
   \[
   T_{2,n}=\alpha_n+o_p(\varepsilon_n);
   \tag{1.3}
   \]
3. conditional on the final configuration-model graph, the order in which components are initiated by rule C1 is size-biased by their half-edge volume (equivalently by their number of edges for nontrivial components);
4. before the giant excursion, the total explored mass is negligible on the giant scale.

The source survival notation gives `xi_n=1-rho_n`, so `alpha_n=-log xi_n=t_n^*` in the preceding HARD7-04 clock theorem.

The other input is the already archived HARD7-04 theorem

`2026-09-19T0855Z__vdh_random_time_weighted_residual.md`,

which proves uniform degree-weighted clock concentration and hence reflected drift at any random time `T_n=t_n^*+o_p(epsilon_n)`.

## 2. The giant can be made into a genuine stopping component

Calling “the end of the largest component” a stopping time would be circular, because largestness is a property of the completed graph. The uniqueness theorem lets us avoid that.

Because

\[
\frac{\max_{C\ne G_n}H(C)}{n\varepsilon_n}\xrightarrow{p}0,
\qquad
\frac{H(G_n)}{n\varepsilon_n}=\Theta_p(1),
\tag{2.1}
\]

there is a deterministic sequence `eta_n downarrow 0` such that with probability tending to one

\[
\max_{C\ne G_n}H(C)<\eta_n n\varepsilon_n<H(G_n).
\tag{2.2}
\]

Run the usual sequential component exploration and stop at the end of the **first completed component** whose observed half-edge volume exceeds `eta_n n epsilon_n`. Call this stopping boundary `tau_n` and the component `Gamma_n`. This is a stopping rule for the revealed pairing. By (2.2),

\[
\mathbb P(\Gamma_n=G_n)\to1,
\qquad
\tau_n=T_{2,n}=t_n^*+o_p(\varepsilon_n)
\quad\text{with probability }1-o(1).
\tag{2.3}
\]

Thus all remainder statements below may be made at the genuine stopping time `tau_n`, not by conditioning on the future event “this component is largest.”

## 3. Exact configuration-model remainder at the stopping boundary

**Lemma 3.1 (deferred-pairing remainder).** Conditional on the complete exploration history through `tau_n`, the unpaired half-edges belonging to sleeping vertices are uniformly perfectly matched. Therefore the unexplored remainder after `tau_n` is **exactly** a configuration model with the (random) degree sequence of the sleeping vertices at `tau_n`.

### Proof

At a completed-component boundary there are no active half-edges. Every half-edge belonging to an awakened vertex has been paired inside an already completed component, so every unpaired half-edge belongs to a sleeping vertex. The original configuration model is a uniform perfect matching. Conditional on any revealed collection of disjoint matched pairs, the restriction to the unrevealed half-edges is a uniform perfect matching. Since `tau_n` is a stopping boundary determined by the revealed history, the same deferred-decision statement holds conditional on the sigma-field at `tau_n`. `square`

This is the key advantage of the stopping formulation: no “largest-component conditioning” is imposed on the remaining matching.

## 4. The true second-largest component is post-giant with high probability

Let `C_{2,n}` be the second-largest component (ties broken deterministically). Conditional on the final graph, the component order is a size-biased permutation by `H(C)`. Hence for any two nontrivial components `A,B`,

\[
\mathbb P(A\text{ precedes }B\mid G_n^{\rm final})
=\frac{H(A)}{H(A)+H(B)}.
\tag{4.1}
\]

Taking `A=C_{2,n}` and `B=G_n`, (2.1) yields

\[
\mathbb P(C_{2,n}\text{ precedes }G_n\mid G_n^{\rm final})
\le \frac{H(C_{2,n})}{H(G_n)}=o_p(1).
\tag{4.2}
\]

Since a random variable in `[0,1]` converging to zero in probability also converges to zero in mean,

\[
\mathbb P(C_{2,n}\text{ precedes }G_n)\to0.
\tag{4.3}
\]

Together with (2.3), with probability `1-o(1)` the largest component of the exact configuration-model remainder from Lemma 3.1 is precisely `C_{2,n}`.

Thus the source question reduces to a largest-component problem for the random post-giant degree sequence **without any future-largest conditioning**.

## 5. Forced roots are negligible in the degree-square norm

The 2019 exploration uses an auxiliary process in which rule C1 is suppressed. Give every original half-edge an independent rate-one lifetime. For vertex `i`, let

\[
E_i:=\min\{\text{lifetimes of the }d_i\text{ half-edges at }i\},
\tag{5.1}
\]

so `E_i` are independent with `E_i~Exp(d_i)`. The auxiliary sleeping set is

\[
\widetilde V_n(t)=\{i:E_i>t\}.
\tag{5.2}
\]

In the actual exploration, the only way a vertex can leave the sleeping set **earlier** than in the auxiliary process is to be selected as the root at a C1 step. Consequently, if `R_n^{\rm root}` is the set of all C1 roots chosen through the giant component,

\[
\sum_i d_i^2
\left|\mathbf 1\{i\text{ sleeping at }\tau_n\}
      -\mathbf 1\{E_i>\tau_n\}\right|
\le \sum_{v\in R_n^{\rm root}}d_v^2.
\tag{5.3}
\]

We now bound the right side.

### 5.1 Number of roots before the giant

Conditional on the final graph, for every component `C ne G_n`,

\[
\mathbb P(C\text{ precedes }G_n\mid G_n^{\rm final})
=\frac{H(C)}{H(C)+H(G_n)}
\le\frac{H(C)}{H(G_n)}.
\tag{5.4}
\]

Therefore the conditional expected number `N_n` of components initiated before `G_n` obeys

\[
\mathbb E[N_n\mid G_n^{\rm final}]
\le\frac{\sum_{C\ne G_n}H(C)}{H(G_n)}
=O_p(\varepsilon_n^{-1}).
\tag{5.5}
\]

Markov's inequality, first conditionally and then unconditionally, gives

\[
N_n=O_p(\varepsilon_n^{-1}).
\tag{5.6}
\]

Including the giant root changes this by one.

### 5.2 Degree-square cost per root

At a C1 step, the root half-edge is uniform among sleeping half-edges. Conditional on the current sleeping set `S`,

\[
\mathbb E[d_{\rm root}^2\mid S]
=\frac{\sum_{i\in S}d_i^3}{\sum_{i\in S}d_i}.
\tag{5.7}
\]

Through the giant boundary only `o_p(n)` half-edge mass has been removed: the pre-giant explored mass is negligible and `H(G_n)=O_p(n\varepsilon_n)=o_p(n)`. Hence, on an event of probability tending to one,

\[
\sum_{i\in S}d_i\ge c n
\tag{5.8}
\]

at every C1 call through the giant, while

\[
\sum_{i\in S}d_i^3\le\sum_i d_i^3=O(n).
\tag{5.9}
\]

Thus the conditional expectation in (5.7) is uniformly `O(1)` on that event. Combining this with (5.6), by truncating the random number of C1 calls and applying conditional Markov inequalities,

\[
\sum_{v\in R_n^{\rm root}}d_v^2
=O_p(\varepsilon_n^{-1}).
\tag{5.10}
\]

Finally

\[
\frac{\varepsilon_n^{-1}}{n\varepsilon_n}
=\frac1{n\varepsilon_n^2}\to0,
\tag{5.11}
\]

because `\varepsilon_n n^{1/3}\to\infty`. Hence (5.3) becomes

\[
\boxed{\quad
\sum_i d_i^2
\left|\mathbf 1\{i\text{ sleeping at }\tau_n\}
      -\mathbf 1\{E_i>\tau_n\}\right|
=o_p(n\varepsilon_n).
\quad}
\tag{5.12}
\]

This proves the weighted mismatch condition isolated in the preceding HARD7-04 artifact.

## 6. Graph-level reflected drift for the exact remainder

Let `d_i^{post}` be the random degree sequence of the sleeping vertices at `tau_n`, and define

\[
\nu_n^{post}
:=\frac{\sum_i d_i^{post}(d_i^{post}-1)}
        {\sum_i d_i^{post}}.
\tag{6.1}
\]

Here `d_i^{post}` means the original degree `d_i` if vertex `i` remains sleeping and zero otherwise; by Lemma 3.1 these are exactly the degrees in the unexposed configuration-model remainder.

**Theorem 6.1 (post-giant reflected drift).** Under (1.1),

\[
\boxed{\qquad
\nu_n^{post}=1-\varepsilon_n+o_p(\varepsilon_n).
\qquad}
\tag{6.2}
\]

### Proof

By (2.3), `tau_n=t_n^*+o_p(epsilon_n)`. The random-time weighted clock theorem gives

\[
\frac{\sum_i d_i(d_i-1)\mathbf 1\{E_i>\tau_n\}}
     {\sum_i d_i\mathbf 1\{E_i>\tau_n\}}
=1-\varepsilon_n+o_p(\varepsilon_n).
\tag{6.3}
\]

Replacing the auxiliary clock-survivor membership by actual sleeping membership changes numerator and denominator by at most the degree-square mismatch in (5.12), namely `o_p(n epsilon_n)`. The denominator is `Theta_p(n)`. Division therefore perturbs the ratio by only `o_p(epsilon_n)`, proving (6.2). `square`

## 7. The remainder preserves the finite-third-moment class

The number of vertices removed before and through the giant is `o_p(n)`. Since the deterministic triangular array `(d_i^3)` is uniformly integrable under moment convergence, for every random subset `U_n` with `|U_n|=o_p(n)`,

\[
\frac1n\sum_{i\in U_n}d_i^3=o_p(1).
\tag{7.1}
\]

Indeed, for fixed `K`, split the sum into `d_i\le K` and `d_i>K`; the first part is at most `K^3|U_n|/n`, while the second is controlled uniformly by third-moment uniform integrability. Thus the post-giant random degree sequence retains the same limiting degree law and the same finite third moment, while its criticality parameter is reflected as in (6.2).

## 8. What this does and does not settle

Combining Lemma 3.1, (4.3), and Theorem 6.1 gives a source-relevant discrete-duality reduction:

- with probability `1-o(1)`, `C_{2,n}` is the largest component of an **exact** configuration model on the post-giant sleeping degree sequence;
- that random degree sequence remains in the finite-third-moment class;
- its distance from criticality is `-epsilon_n+o_p(epsilon_n)`.

This is stronger than the preceding ideal branching-process identity because it reaches the actual graph remainder and removes the future-largest conditioning issue.

It is still **PARTIAL**. The source asks for the scaling of the second-largest component / whether the discrete duality principle still holds. To finish that source question one still needs a sharp barely-subcritical largest-component theorem that applies uniformly to this random residual degree sequence at the required scale. The 2026 monograph itself presents the corresponding barely-subcritical scaling problem as part of the unresolved crossover picture, so (6.2) must not be advertised as source closure.

Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning.

# HARD7-02 idea checkpoint before code — Q1.9 exceedance skeleton

Frozen source metric remains `T_corr=0` at the start of this run. Previous Q1.9 methods were B2/B24/B30, so this run switches to **B3 / B7 / B19**.

The route to test is not another finite-matrix fit. Use the exact Pareto representative already admitted for Campbell–O'Rourke Question 1.9 and separate the matrix at a **tail scale** `t`.

For each unordered pair `e={i,j}`, write its radial mark as `R_e` and angular mark as `W_e~vartheta_x`. Keep the whole reciprocal pair only when `R_e>tn`. The retained-edge graph is then exactly `G(n,1/(tn))` for fixed `t>=1`. For `t>1` this is subcritical.

At `x in (0,1)`, every retained reciprocal pair has the exact local eigenvalue modulus factor

`kappa_x = (x(1-x))^(1/4)`.

For fixed `s>=t`, call an edge **strong-isolated** if `R_e>sn` and every other radial mark incident to either endpoint is at most `tn`. Such an edge is an actual isolated `2 x 2` block of the exceedance skeleton, not merely a local heuristic, so it contributes two exact skeleton eigenvalues of modulus `>kappa_x s`.

For a fixed edge,

`P(strong-isolated) = (sn)^(-1) (1-(tn)^(-1))^(2(n-2))`.

Hence, if `J_n(s,t)` counts strong-isolated edges,

`(2/n) E J_n(s,t) -> e^(-2/t)/s`.

The key new observation is that `J_n/n` should concentrate despite the global isolation condition. For two disjoint candidate edges the union of the two isolation neighborhoods contains exactly `4n-12` other edges, so their covariance is only order `n^(-3)`; there are order `n^4` such pairs. Overlapping candidate edges are mutually exclusive. Therefore `Var J_n=O(n)`, giving an asymptotically deterministic positive density of **exact** tail eigenvalues in the skeleton.

If this closes, it yields the rigorous lower bound

`mu_skeleton,n(|z|>kappa_x s) >= 2J_n(s,t)/n -> e^(-2/t)/s` from below in probability.

At `s=t->infinity`, the coefficient becomes `kappa_x/R`, matching the previously isolated PWIT order parameter `K_1(vartheta_x)=kappa_x`. This does **not** yet prove the same lower tail for the full matrix: the precise remaining source-level obstruction is stability of these skeleton eigenvalues after reattaching all sub-threshold entries. The point of this run is to turn the reciprocal-edge heuristic into a positive-density exact spectral statement before attacking that nonnormal reattachment step.

In parallel, B3 should strengthen the previous `p<1` moment theorem from the single point `x=1/4` to the entire interior family. The same row-tail computation has coefficient

`m_x=(sqrt(x)+sqrt(1-x))/2 <= 1/sqrt(2)`,

so one expects the uniform bound

`int |z|^p mu_{1,vartheta_x}(dz) <= 1 + p(1+3 sqrt(2)m_x)/(1-p) <= 1+4p/(1-p)`

for every `0<p<1` and every `0<x<1`.

Only after these statements are written on the page is a small exact combinatorial self-check warranted; it will check the incidence counts and covariance algebra, not substitute for the proof.
# H0008 -> P03 handoff: variance correctors from two-spine mixing

Date: 2026-09-20 UTC  
From: `C06 / R7-07 / H0008`  
To: P03 Galton--Watson speed roles  
Scope: reusable lemma only; this does not change P03 ownership/objective and does not ask P03 to duplicate H0008.

The current H0008 run found a useful way to avoid an explicit four-spine expansion.

Let `K` be a stationary descendant/environment kernel and let an additive path functional satisfy

`S_{n+1}=increment(first edge)+S_n(after first edge)`.

Suppose:

1. for every centered `f in L^{2+eta}(mu)`, `||K^n f||_2 <= C_f exp(-cn)` (in H0008 this was obtained from a two-spine first-split decomposition plus an `L^p` split-Palm density and a reverse projected spectral gap);
2. the conditional mean has a corrector `m_n = n d + G + epsilon_n`, with `G` having sufficiently high finite moments and `||epsilon_n||_4 <= C exp(-cn)`;
3. the edge increment has a finite fourth moment under the stationary edge law.

Then the conditional variance `V_n=Var(S_n | environment)` obeys

`V_{n+1}=K V_n + r_n`,

`r_n=Var(first-edge increment + m_n(next environment) | current environment)`.

Putting

`r_infty=Var(first-edge increment + G(next environment) | current environment)`,

the elementary bound

`|Var(X+Y)-Var(X)| <= 2(E X^2)^{1/2}(E Y^2)^{1/2}+E Y^2`

gives `||r_n-r_infty||_2 <= C exp(-cn)`. If `r_infty in L^{2+eta}`, the same mixing assumption yields a convergent Poisson series

`J_0=sum_{s>=0} K^s(r_infty-E r_infty)`.

Iterating the variance recursion and separating the scalar means of `r_n-r_infty` gives

`V_n = n E r_infty + J + O_{L^2}(exp(-cn))`

for an explicit `J in L^2` (the scalar correction is `sum_m E(r_m-r_infty)`). Thus conditional-variance self-averaging can be much stronger than an `O(n)` four-spine bound: it can have an actual random `O(1)` corrector.

Potential P03 use: whenever a regeneration/speed additive functional already has a one-spine mean corrector and a two-copy decorrelation estimate, try this recursion before launching a four-copy genealogy. It may give a quenched variance corrector and asymptotic-variance identification with no extra offspring factorial-moment assumption.

H0008 source report containing the proof: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T125900Z__report.md`, creation commit `923729fa6adfb851e247944853ddb3d09c9b77ba`.

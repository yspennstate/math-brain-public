Runtime identification: **GPT-5.6 Sol; reasoning telemetry UNVERIFIED — not GPT-6 maximum.**

# HARD7-04 idea before bookkeeping — solve MD5 by clocks, then kill the pre-giant correction by an early-awakening estimate

Fresh moves: **B9 RANDOMIZE, B12 FIND WHAT IS CONSERVED, B28 REPLACE FOR ALL WITH TYPICAL.**

The 20:30Z checkpoint reduced the heavy-tailed configuration-model MST collar problem to the five actual outside-giant marked sums MD5. The new route is to avoid controlling five exploration martingales directly.

Fix the explicit Pareto-quantile subclass already used in the 18:30Z run. Write

- `r=tau-1 in (2,3)`, `beta=r-2=tau-3`, `a=1/r`, `eta=beta/r`;
- `A_n(k)=C n k^{-r}+O(1)` up to `K_n=Theta(n^a)`;
- `epsilon_n=lambda_n n^{-eta}` with the concrete mesoscopic choice `lambda_n=(log n)^3`;
- `p_n=(1+epsilon_n)/nu_n`;
- `h_n(s)=L_n^{-1} sum_v d_v s^(d_v-1)`;
- `psi_n` solves `psi_n=h_n(1-p_n+p_n psi_n)`, `t_n=-log psi_n`, `q_n=1-p_n+p_n psi_n`.

The 18:30Z Abelian theorem gives `epsilon_n asymp t_n^beta`, and `t_n=n^{-1/r} z_n` with `z_n -> infinity` (polylogarithmic here). Put

`b_n := n t_n^beta asymp n epsilon_n`.

Color each original matched edge A with probability `p_n`. Let `X_v` be its number of A half-edges and `R_v=d_v-X_v`. The five marks are

`w_1=X`, `w_2=X(X-1)`, `w_3=R`, `w_4=XR`, `w_5=R(R-1)`.

## 1. Static five-mark Laplace law

For `psi=e^{-t}` define `F_j(t)=sum_v w_j(X_v,R_v) e^{-t X_v}`. If the incident edge-colors at a vertex were independent per half-edge, `X_v~Bin(d_v,p)` and the exact expectations at `t=t_n` would be

`M_1=p L psi^2`,

`M_2=p^2 L psi^2 h_n'(q)`,

`M_3=(1-p)L psi`,

`M_4=p(1-p)L psi h_n'(q)`,

`M_5=(1-p)^2 L h_n'(q)`.

In the actual edge-coloring, the only local obstruction to the binomial law is a self-loop, whose one edge-color is counted twice. For every one of the five functions

`g_{j,d}(x)=w_j(x,d-x)e^{-t x}`

one has, for `m=1,2`,

`|g_{j,d}(x+m)-g_{j,d}(x)| <= C d(1+t d)e^{-t x}`

(up to an immaterial constant after shifting the exponential by at most two). The expected total loop correction is therefore at most

`C/L sum_v d_v^2 d_v(1+t d_v)`

`=O(K_n^(3-r)+t K_n^(4-r))`

`=O(n^((3-r)/r)(1+z_n))=o(b_n)`

for the polylogarithmic `z_n` used here.

Conditional on the matching, edge colors are independent. Efron-Stein and the same increment bound give

`Var(F_j(t) | matching) <= C sum_v d_v^3(1+t d_v)^2 exp(-c t d_v)`

`=O(n t^(r-3))`.

Since

`n t^(r-3)/b_n^2 = 1/(n t^(r-1)) -> 0`,

all five satisfy simultaneously

`F_j(t_n)=M_j+o_P(b_n)`.                                        (A)

This is a theorem-sized analytic estimate, not a finite computation.

## 2. Random lower-degree extinction time is asymptotic to the ideal time

Conditional on the A-degrees `X`, the A-subgraph is a uniform configuration model on degree sequence `X`. Let `psi_X` be the nontrivial extinction root of its empirical excess pgf and `t_X=-log psi_X`.

Use the root numerator

`Z_X(s)=sum_v X_v(s^(X_v-1)-s)`.

Its ideal mean is

`p L [h_n(1-p+p s)-s]`.

The finite-n Abelian estimate from 18:30Z implies, for fixed `u` near 1,

`1-p h_n'(1-p+p e^{-u t_n})`

`=epsilon_n[(beta+1)u^beta-1]+o(epsilon_n)`.

Hence at `s_-=e^{-(1+delta)t_n}` and `s_+=e^{-(1-delta)t_n}` the ideal root numerator has opposite signs and magnitude at least `c_delta n epsilon_n t_n = c_delta n t_n^(r-1)`.

The key cancellation is `Z_X(1)=0` identically. Flipping one edge-color changes a vertex contribution by at most

`C min(1,t_n d_v)`.

Therefore

`Var Z_X(e^{-u t_n}) <= C sum_v d_v min(1,t_n d_v)^2 = O(n t_n^(r-1))`.

Self-loop bias is smaller than the displayed signal. Since `n t_n^(r-1)->infinity`, the two signs survive with probability tending to one. Convexity of the empirical excess pgf then brackets the unique subunit root, so

`t_X/t_n -> 1 in probability`.                                (B)

For this explicit thinned power-law sequence, the standard assumptions of van der Hofstad--Janson--Luczak's barely-supercritical theorem hold with probability tending to one: empirical fixed-degree frequencies converge, second moments stay bounded because `X_v<=d_v`, the nondegeneracy condition holds, and the empirical branching excess is `epsilon_n+o_P(epsilon_n)`; moreover `epsilon_n/n^{-eta}=lambda_n->infinity`, outside the heavy-tail critical window. Their continuous-time exploration therefore starts the principal component at `T_1=o_P(t_X)` and finishes it at `T_2=t_X(1+o_P(1))`. By (B),

`T_1=o_P(t_n)`, `T_2/t_n -> 1`.                              (C)

## 3. Surrogate sleeping sums at the random giant endpoint

Give the lower A half-edges iid Exp(1) maximal lifetimes as in the continuous-time configuration-model construction. Conditional on `X`, let

`I_v(s)=1{all X_v maximal lifetimes exceed s}`,

`tilde F_j(s)=sum_v w_j I_v(s)`.

At deterministic `s`, the `I_v(s)` are independent with mean `e^{-sX_v}`.

With probability tending to one, every vertex with `d_v>=A log n` has `X_v>=c d_v`; this is a weighted Bernoulli Chernoff bound even in the presence of self-loops (loop edge-colors have weight two). On that event, uniformly for `s asymp t_n`,

`Var(tilde F_j(s)|X) <= C n s log^5 n + C n s^(r-4)`.

The second term is the important one and

`n t_n^(r-4)/b_n^2 = 1/(n t_n^r)=z_n^{-r}->0`.

Also, if `|s-t_n|<=delta t_n`,

`|F_j(s)-F_j(t_n)| <= delta t_n sum_v w_j X_v e^{-(1-delta)t_nX_v}`

`=O(delta b_n)+o(b_n)`.

Thus for any random time `T/t_n->1`, monotonicity of `tilde F_j(s)` and a deterministic shrinking sandwich give

`tilde F_j(T)=M_j+o_P(b_n)` simultaneously for `j=1,...,5`. In particular this holds at the actual giant endpoint `T=T_2`.                         (D)

The normalization `n t_n^r=z_n^r->infinity` shows exactly why this route is mesoscopic: at the critical scale `z_n=O(1)` the quadratic-mark variance is not `o(b_n^2)`.

## 4. The missing pre-giant correction is itself `o_P(b_n)`

This is the new point that avoids a weighted-susceptibility theorem.

Let `P_n` be the total **original squared-degree mass** of all lower-A components completed before the principal component starts:

`P_n=sum_{v in pre-giant components} d_v^2`.

The published exploration theorem gives `T_1=o_P(t_n)`. Choose deterministic `delta_n downarrow 0` such that

`P(T_1 > delta_n t_n)->0`, and set `s_n=delta_n t_n`.

For a deterministic lower degree sequence `X`, stop the continuous-time exploration if sleeping lower half-edge mass first drops below `L_A/2`. Up to that stop:

- a vertex can be awakened by C3 only if one of its `X_v` maximal lifetimes expires by time `s`, with probability at most `s X_v`;
- the number of C1 starts is at most one plus the number of C3 events;
- the expected number of C3 events by time `s` is at most `L_A s`;
- at each C1, the conditional probability of selecting a specified sleeping vertex `v` is at most `2X_v/L_A`.

Consequently

`P(v awake by s before the stop | X) <= C(s X_v + X_v/L_A)`,

capped of course by 1. Since `X_v<=d_v`, the Pareto tail gives the deterministic estimate

`sum_v d_v^2 min(1,s d_v) <= C n s^beta`,                    (E)

for every `s=o(1)` (the same bound also holds when `s<1/K_n`), while

`L_A^{-1} sum_v d_v^3 = o(b_n)`.

Thus the expected original squared-degree mass awakened by time `s_n`, before the stop, is

`O(n s_n^beta)+o(b_n)=O(delta_n^beta b_n)+o(b_n)=o(b_n)`.

The same estimate with weight `X_v` instead of `d_v^2` shows the stop is not reached by `s_n` with probability tending to one. Markov then yields

`P_n=o_P(b_n)`.                                               (F)

This is stronger than the ordinary `o_P(n t_n)` pre-giant vertex/half-edge estimate because it controls the exact quadratic marks required by MD5.

## 5. MD5 follows

At `T_2-`, the actually sleeping vertices are precisely components not yet explored after the principal component. The surrogate sleeping set contains the actual sleeping set; the difference consists only of C1-start vertices, because every C3-awakened vertex has had a spontaneous lifetime expire.

For each mark `w_j<=d_v^2`, the C1-start discrepancy through the principal component is at most

`P_n + d_max^2`.

The actual outside-principal-component sum equals its actual sleeping sum plus the pre-giant sum. Therefore

`| actual_outside_j - tilde F_j(T_2) | <= 2 P_n + d_max^2`.

Now `d_max^2=Theta(n^(2/r))=o(b_n)` because `b_n=n^(2/r) z_n^beta` and `z_n->infinity`. Combining (D) and (F) gives the full five-mark statement

`actual_outside_j = M_j + o_P(epsilon_n n)`, `j=1,...,5`.    (MD5)

Hence the 20:30Z MD5 blocker is discharged for the explicit Pareto-quantile subclass and `lambda_n=(log n)^3`.

By the already established colored-matching/hypergeometric transfer, this makes the actual two-type `(A,B)` collar mean matrix equal to its ideal rank-one matrix up to `o_P(epsilon_n)`, so for fixed `0<delta<beta=tau-3`,

`rho(M_collar)=1-(beta-delta+o_P(1))epsilon_n < 1-c epsilon_n`

with high probability.

The frozen MST exponent itself does **not** move in this checkpoint. The next mathematical obstruction is no longer MD5; it is converting this genuine mesoscopic subcritical collar margin into a uniform component-diameter bound across the Kruskal/percolation levels and then into the MST upper exponent. Under the section-I rule this is the second stuck recovery; another unchanged frozen-metric run must rotate/handoff rather than manufacture a third auxiliary lemma.
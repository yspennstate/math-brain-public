# P0245 — the exact extremal cover-time conjecture (Aldous–Fill Open Problem 6.30)

**Status: one case PROVED (n = 3, complete, machine-assisted and hand-checkable); a
correction to the monograph's Example 6.29 VERIFIED; the general problem untouched.**

## The problem, from the source

Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, section
6.6.4, verbatim from the LaTeXML edition at
`https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch6.S6.html`:

> **Open Problem 6.30** Prove that, for any reversible chain on $n$ states,
> $E_\pi C \ge (n-1)h_{n-1}$ (the value for random walk on the complete graph).

$C$ is the discrete-time cover time, $h_m = \sum_{k \le m} 1/k$, and $E_\pi$ means the chain
starts from stationarity. Corpus entry P0245 states it the same way.

Reversible chains on $n$ states are exactly random walks on weighted graphs: symmetric weights
$w_{ij} = w_{ji} \ge 0$ (self-loops $w_{ii}$ allowed), $P_{ij} = w_{ij}/w_i$ with
$w_i = \sum_j w_{ij}$, and $\pi_i = w_i / \sum_k w_k$.

## Machinery

`code/covertime.py` computes $E_\pi C$ exactly over the rationals by the subset dynamic
programme: with $h(S,i)$ the expected further time to cover from $i$ having visited $S$,

$$h(V,i) = 0, \qquad h(S,i) = 1 + \sum_{j \in S} P_{ij} h(S,j) + \sum_{j \notin S} P_{ij} h(S \cup \{j\}, j),$$

one linear system of size $|S|$ per subset, solved in decreasing $|S|$. Control: the non-lazy
complete graph returns $1, 3, 11/2, 25/3, 137/12$ for $n = 2,\dots,6$, exactly $(n-1)h_{n-1}$.

## A correction to Example 6.29

Example 6.29 — the example that motivates the conjecture — takes $K_n$ plus a pendant leaf $l$
and derives first

$$E_l C = 1 + (n-1)h_{n-1} + 2\mu, \qquad \mu = \frac{1 + h_{n-1}}{n},$$

and then rewrites it as $E_l C = n h_n - (1 - \tfrac{2}{n})(h_n - \tfrac{1}{n})$ (source LaTeX,
read off the page: `E_{l}C=nh_{n}-\left(1-\frac{2}{n}\right)\left(h_{n}-\frac{1}{n}\right)`).

The two disagree. Substituting $h_{n-1} = h_n - 1/n$ in the first line gives

$$E_l C = h_n\Big(n - 1 + \tfrac{2}{n}\Big) + \tfrac{3}{n} - \tfrac{2}{n^2},$$

while the displayed closed form is $h_n(n-1+\tfrac2n) + \tfrac1n - \tfrac2{n^2}$: short by
exactly $2/n$. Exact computation of the chain agrees with the *first* line.

| $n$ | $E_l C$ computed | first line | displayed closed form | $n h_n$ (the $K_{n+1}$ value) |
|---|---|---|---|---|
| 3 | 17/3 = 5.6667 | 17/3 | 5 | 11/2 = 5.5 |
| 4 | 95/12 = 7.9167 | 95/12 | 89/12 | 25/3 = 8.3333 |
| 5 | 317/30 = 10.5667 | 317/30 | 61/6 | 137/12 = 11.4167 |
| 6 | 608/45 = 13.5111 | 608/45 | — | 147/10 = 14.7 |
| 7 | 584/35 = 16.6857 | 584/35 | — | 363/20 = 18.15 |

The example's conclusion — $E_l C$ below the complete $(n+1)$-graph's $n h_n$ — survives for
$n \ge 4$ but **fails at $n = 3$**: $17/3 > 11/2$. With the printed closed form one reads
$5 < 5.5$ and concludes the opposite. The correction changes the range in which the example is
a near-counterexample; it does not change the point the example is making.

The same computation confirms the problem really is about $E_\pi$ and not $\min_v E_v$: for the
leaf graph on $m = n+1$ states, $E_\pi C$ is roughly twice $(m-1)h_{m-1}$ (e.g. $523/60 = 8.717$
against $11/2$ at $m = 4$), because from stationarity the walk keeps returning to the leaf.

## Result: Open Problem 6.30 holds for n = 3

**Theorem.** Let $P$ be an irreducible reversible chain on three states. Then
$E_\pi C \ge 3 = (n-1)h_{n-1}$, with equality if and only if $P$ is simple random walk on the
triangle (equal weights, no self-loops).

*Proof.* Parametrise by $a = w_{23}$, $b = w_{13}$, $c = w_{12}$ and self-loops
$s_1, s_2, s_3 \ge 0$. Irreducibility needs at least two of $a,b,c$ positive; take $a,b,c > 0$
first (the boundary cases $c = 0$ etc. follow by continuity of the rational function below, and
are strictly worse). The subset DP is small enough to run symbolically
(`code/cover_n3_symbolic.py`); sympy returns

$$E_\pi C - 3 = \frac{(ab+ac+bc)^2 \, R(a,b,c,s_1,s_2,s_3)}
{(a+b)(a+c)(b+c)(ab+ac+bc)^3\big(2(a+b+c)+s_1+s_2+s_3\big)} .$$

The denominator is a positive combination of monomials, hence positive on the positive orthant.
Expanding $R$ as a polynomial in $(a,b,c,s_1,s_2,s_3)$: 282 monomials, of which exactly ten
carry a negative coefficient, and **every one of those ten has $s$-degree zero**. Therefore

$$R(a,b,c,s) \ \ge\ R(a,b,c,0) =: R_0(a,b,c) \qquad (s_i \ge 0),$$

strictly if some $s_i > 0$. So self-loops can only hurt, and it remains to show $R_0 \ge 0$.
sympy factors it:

$$R_0 = (a+b)(a+c)(b+c)\,F(a,b,c), \qquad
F = 4(a^3+b^3+c^3) - \sum_{\text{sym}} a^2 b - 6abc,$$

where $\sum_{\text{sym}} a^2 b = a^2b + ab^2 + b^2c + bc^2 + a^2c + ac^2$. With
$S = a^3 + b^3 + c^3$,

$$F = \Big(2S - \sum_{\text{sym}} a^2 b\Big) + \big(2S - 6abc\big),$$

$$2S - \sum_{\text{sym}} a^2 b = \tfrac13 \sum_{(x,y)} (x-y)^2 (2x+y), \qquad
2S - 6abc = (a+b+c)\big[(a-b)^2+(b-c)^2+(c-a)^2\big],$$

the first sum over the six ordered pairs $(x,y)$ of distinct elements of $\{a,b,c\}$, using
$2x^3 + y^3 - 3x^2 y = (x-y)^2(2x+y)$. Both brackets are nonnegative and both vanish only when
$a = b = c$. Hence $E_\pi C \ge 3$, with equality exactly at $s_1 = s_2 = s_3 = 0$, $a = b = c$,
which is simple random walk on the triangle. $\square$

Every algebraic step was verified in sympy (`code/cover_n3_proof.py` and the follow-up check):
the factorisation of $R_0$, the sign pattern of the coefficients of $R$, the identity
$F = (2S - \sum_{\text{sym}}) + (2S - 6abc)$, and the two displayed factorisations. The final
inequality is elementary enough to check by hand.

### Trying to break it

The strongest case that this is wrong: the symbolic expression came out of one sympy run, and a
sign error anywhere upstream would produce a plausible-looking polynomial. Checks that settle it:
(i) the DP itself reproduces $(n-1)h_{n-1}$ for the non-lazy complete graph at $n = 2,\dots,6$
and reproduces Aldous and Fill's own intermediate formula for the leaf example at $n = 3,\dots,7$;
(ii) substituting $a = b = c = 1$, $s = 0$ into the symbolic $E_\pi C$ gives exactly 3;
(iii) independent multi-start numerical minimisation over the same parameter space at $n = 3$
bottoms out at $3.000000000$ with the argmin at the equal-weight triangle. One residual risk:
the boundary cases $a = 0$ (path graphs) are argued by continuity rather than
computed separately; they are easy to check directly and are not close to the bound.

## Numerics above n = 3

`code/cover_min2.py` minimises $E_\pi C$ over the full weighted-graph parametrisation by
multi-start Nelder–Mead, with weights $e^{12\tanh(x/12)}$ so the search cannot overflow. A
run without that guard reports a spurious "minimum" of $1.0$ at $n = 4$ produced by an
overflow-poisoned stationary vector — a float optimiser will report the value of a NaN without
complaint. Guarded, $n = 3$ returns $3.000000000$ at the equal-weight triangle both with and
without self-loops in the parametrisation.

**These are numerics, not proof.** They say only that multi-start Nelder–Mead found no lower
valley.

## Literature check (2026-09-13)

Searched: "Aldous Fill open problem 6.30 cover time"; "minimum expected cover time reversible
Markov chain n states lower bound (n-1)H_{n-1} Feige Aldous conjecture". Found Feige's tight
asymptotic lower bound $\min_v E_v C \ge c_n \sim n\log n$ for *unweighted* graphs (Theorem 6.31
of the monograph; Feige, *Random Structures & Algorithms* 6 (1995)) and Aldous, *Lower bounds for
covering times for reversible Markov chains and random walks on graphs*, J. Theoret. Probab. 2
(1989) 91–100. Neither is the exact weighted-chain statement. **No source found that settles
Open Problem 6.30; no source found that records the $n = 3$ case.** Recorded as a negative
search: no paper after Feige addressing the exact extremal constant was found.

## Remaining obligation

Everything for $n \ge 4$. The $n = 3$ proof does not extend as written: at $n = 4$ there are ten
weight variables and the analogue of $R$ is out of reach here. Two structural pieces are worth
isolating, because any general argument needs both and both are true at $n = 3$ for reasons that
might generalise.

1. **Self-loops never help.** Deleting all self-loops gives the jump chain $W'$; conditionally on
   the jump path, the cover time of $W$ is a sum of geometric holding times, so
   $E_i C_W \ge E_i C_{W'}$ pointwise in the start state. The gap is the start law:
   $\pi_W \ne \pi_{W'}$, and $\pi_W$ tilts toward the states carrying big self-loops, which may be
   exactly the cheap states to start from. At $n = 3$ the tilt provably loses. In general this is
   a clean self-contained sub-problem, and it would cut the parameter count from
   $\binom{n+1}{2}$ to $\binom{n}{2}$.
2. **A potential function for the maximum, not the mean.** Kemeny's constant obeys
   $\tau_0 = \sum_{k \ge 2}(1-\lambda_k)^{-1} \ge (n-1)^2/(n - \operatorname{tr}P) \ge (n-1)^2/n$
   by AM–HM, minimised exactly at the non-lazy complete graph — so the *mean* hitting parameter
   already has the conjectured extremal structure, with a one-line proof. The obstruction is that
   $E_\pi C = E_\pi[\max_j T_j]$ and no comparison of maxima follows from a comparison of means.
   Matthews' bound with $A = V$ gives $E_v C \ge (\min_{i \ne j} E_i T_j)\,h_{n-1}$, and
   $\min_{i \ne j} E_i T_j$ can be as small as 1, so Matthews alone cannot reach the constant.

**Next exact step:** prove or refute item 1 (self-loops never help, from stationarity) at $n = 4$
by the same symbolic route restricted to one self-loop variable $s_1$ with $a_{ij}$ numeric —
that is a one-variable rational inequality per base graph, and a refutation would be a genuinely
interesting small fact about lazy chains started from their own stationary law.

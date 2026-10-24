# Aldous and Fill's Open Problem 4.49(ii): no counterexample, and the extremal family looks like the complete graphs

Ledger row I0026 (intake I). Source: Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 4.49, Section 4.3.5. Written 14 September 2026, about 10:30. This is evidence, not a proof.

## The problem

For a family $f = (f^{(a)})$ in which $f^{(a)}$ is a unit flow from the state $a$ to $\pi$, Section 4.3.5 sets
$$\psi(f) = \max_{\text{edges }(i,j)}\ \sum_a \frac{\pi_a|f^{(a)}_{ij}|}{\pi_ip_{ij}},$$
and records, from Sinclair by way of Leighton and Rao's multicommodity flow theorem,
$$\inf_f\psi(f) \le K\,\tau_2\log n. \tag{4.49}$$
Open Problem 4.49 asks "(i) Is there a simple proof of (4.49) in general? (ii) Does (4.49) hold with the diameter $\Delta$ in place of $\log n$?"

## What is computable

$\inf_f\psi(f)$ is a linear program. The flows are free variables, conservation at each vertex for each source is linear, and the maximum over edges of a sum of absolute values linearises with one auxiliary variable per source and edge. For the simple random walk on a graph $\pi_ip_{ij} = 1/(2m)$ for every edge, so the objective is $2m\max_e\sum_a\pi_a|f^{(a)}_e|$. With $n$ sources and $m$ edges the program has $2nm+1$ variables, $n^2$ equalities and $2nm+m$ inequalities, which is small enough to solve exactly for a few dozen vertices.

The relaxation time and the diameter are immediate, so the ratio the problem asks to be bounded,
$$R(G) = \frac{\inf_f\psi(f)}{\tau_2\,\Delta},$$
can simply be computed.

## What the computation says

Over **every connected graph on four to seven vertices** (992 of them, from the graph atlas):
$$\max_G R(G) = 2\ \text{exactly},$$
attained at $n = 4, 5, 6, 7$ by the complete graph and by nothing else. For $K_n$ the program returns $\inf_f\psi = 2(n-1)/n$ against $\tau_2 = (n-1)/n$ and $\Delta = 1$, so $R(K_n) = 2$ for every $n$; the value was confirmed at $n = 8, 12, 16$ as well.

Across twenty-seven named families up to twenty-five vertices nothing came closer:

| family | $\inf_f\psi$ | $\tau_2$ | $\Delta$ | $R$ |
|---|---|---|---|---|
| $K_{16}$ | 1.875 | 0.938 | 1 | **2.000** |
| $K_{5,15}$ | 2.733 | 1.000 | 2 | 1.367 |
| Petersen | 3.000 | 1.500 | 2 | 1.000 |
| star on 20 | 1.947 | 1.000 | 2 | 0.974 |
| hypercube $Q_4$ | 4.000 | 2.000 | 4 | 0.500 |
| $4\times4$ torus | 4.000 | 2.000 | 4 | 0.500 |
| random cubic, $n=20$ | 5.460 | 4.120 | 4 | 0.331 |
| barbell $8+8$ | 57.98 | 63.11 | 4 | 0.230 |
| $C_{24}$ | 12.00 | 29.35 | 12 | 0.034 |
| $P_{16}$ | 15.00 | 45.76 | 15 | 0.022 |

The program passes its own checks: it returns exactly $n/2$ for the cycle $C_n$ and exactly $n-1$ for the path $P_n$, which are the values a hand computation gives, and $2$ in the limit for stars.

So the answer to 4.49(ii) is not no in any range that can be searched exhaustively, and the data suggest something sharper than the problem asks.

**Conjecture.** $\inf_f\psi(f) \le 2\,\tau_2\,\Delta$ for every finite connected graph, with equality exactly for the complete graphs.

The mechanism behind the bound is visible in the numbers. Routing every source along shortest paths spreads a total flow volume of about $n$ times the mean distance over $m$ edges, which gives $\psi \approx 2\times(\text{mean distance}) \le 2\Delta$ whenever the routing can be balanced; and $\tau_2 \ge 1/2$ always, since the second eigenvalue is at least $-1$. The problem is therefore about how far balanced routing can fail, and the families where it fails worst, expanders and barbells, both pay for it in $\tau_2$ at the same rate, which is why the ratio stays put.

## Status

Evidence only, and stated as such: an exhaustive search to seven vertices and a family scan to twenty-five, no counterexample, and an extremal family that pins the constant at 2 if the conjecture is true. Nothing here proves 4.49(ii), and the search cannot: the conjecture is asymptotic and the Leighton and Rao gap that makes (4.49) nontrivial only appears at sizes far beyond exact search. Verification: author checked; the linear program reproduces three hand-computable values (cycle, path, star). Prior art: a bounded search found nothing on Open Problem 4.49 since the monograph; not a clearance.

## New open problems

1. **The sharp constant.** Is $\inf_f\psi(f) \le 2\tau_2\Delta$ for every finite connected graph, with equality only for complete graphs? A proof would answer 4.49(ii) in the strongest form; the extremal case is where a proof should be tested first.
2. **Where balanced routing fails against $\tau_2$.** Define $B(G) = \inf_f\psi(f)/(2\times\text{mean distance})$, the factor by which balanced routing fails. The data have $B$ close to one on every family tried except the barbell. Is $B(G) \le C\tau_2/\Delta \cdot \text{mean distance}$, and is $B$ the right object for a proof of 4.49(ii)?

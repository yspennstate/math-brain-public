Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed. **F0003 `a_3 >= 1/4 -> a_3 >= 1/4` (NO SOURCE-METRIC MOVEMENT); methods B15 / B14 / B25; status PARTIAL.**

# F0003 — all three-residue modular null rows are asymptotically dominated by false twins

Date: 2026-09-18 UTC.  
Track: `R7-07 Hard Problem New Methods`; native ID `6aabe8413f60819197825dd81ca138ae`.  
Canonical target: `F0003`, exclusively claimed by R7-07.  
Run-start master: `045e44e632468f5512a1d7a77eae9d033225589e`.  
Fresh pre-artifact master: `f959aca3ea90fd15d3378d0f909da9f9977beb3c`.  
Previous report: `research7_2026-09-17/R7-07/runs/2026-09-18/2026-09-18T172600Z__report.md` @ creation commit `51a9dd295ba10e5c9202776c0b7c0289d04657d5`.

The frozen source metric remains

\[
a_3:=\sup\{a:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\},
\qquad a_3\ge\frac14.
\]

This note closes the finite-support milestone left by the preceding AP calculation: it classifies **every** modular null row with exactly three coordinate values over a large prime field and proves that their total normalized first moment is asymptotically the false-twin contribution `8/(9n)`. It does **not** control support size at least four, so it does not move `a_3`.

Throughout, `A` is the adjacency matrix of the cubic configuration model unless `simple` is explicitly written. Let `p>7` be prime and polynomially bounded in `n`; the intended growing choice `p=n^{1/3-o(1)}` is included. Let

\[
S_p^{(3)}(A)=\#\{y\in\mathbb F_p^n:Ay=0,\ |\{y_1,\dots,y_n\}|=3\}.
\]

Since every nonzero vector over `F_p` is a surjective homomorphism to `F_p` exactly when one of its coordinates is nonzero, and every three-valued row is nonzero, the free scalar action of `F_p^*` gives the natural normalized count `S_p^{(3)}/(p-1)`.

## Theorem A — complete additive-resonance classification (B15 + B14)

Let `S={a,b,c}` be three distinct residues in `F_p`, `p>7`. Suppose there is a cubic undirected configuration with a row `y` taking exactly the values in `S` and satisfying `Ay=0`.

For a vertex, the multiset of its three neighbour labels must be a zero-sum multiset of size three from `S`. Because `p>3`, the only possible algebraic forms are:

1. `000`, possible exactly when `0 in S`;
2. a double-single type `(r,r,s)`, possible exactly when `2r+s=0`;
3. the all-distinct type `(a,b,c)`, possible exactly when `a+b+c=0`.

If the all-distinct type is present and is the only local type, edge symmetry forces all three label classes to have equal size. If another local type coexists with it, then a double-single relation would force two support values to coincide, while coexistence with `000` gives precisely

\[
S=u\{-1,0,1\}.
\]

If the all-distinct type is absent, one local type cannot support all three colours: a single size-three multiset omitting one support value would create no half-edge aimed at that colour, contradicting undirected edge balance because that source class is nonempty. Hence at least two local types occur. If one is `000`, the other must be a double-single relation among the two nonzero values, so

\[
S=u\{0,1,-2\}.
\]

If both are double-single relations, after relabelling they are

\[
2a+b=0,\qquad 2b+c=0,
\]

so

\[
S=u\{1,-2,4\}.
\]

No third double-single relation is possible for `p>3`, because closing the cycle would give `(-2)^3a=a`, hence `9a=0`. Relations sharing the same doubled or single value force a repeated support value.

Therefore every feasible exactly-three-valued null row belongs to exactly one of the following resonance classes:

- **Z:** `a+b+c=0`, with only the all-distinct local type, except for the AP subcase below;
- **AP:** `u{-1,0,1}`, local types `000` and `(-1,0,1)`;
- **C0:** `u{0,1,-2}`, local types `000` and `(1,1,-2)`;
- **C4:** `u{1,-2,4}`, local types `(1,1,-2)` and `(-2,-2,4)`.

This classification is exhaustive and is invariant under the free scalar action. It is the required B14 quotient: after modding out by multiplication by `F_p^*`, there are only these four additive-resonance shapes, while class Z still has a one-parameter projective family of support triples.

## Class Z — generic zero-sum triples are exponentially negligible

The number of unordered distinct support triples with sum zero is

\[
\frac{(p-1)(p-2)}6.
\]

Indeed there are `p^2` ordered solutions `a+b+c=0`; the union of the three equality events has size `3p-2`, leaving `(p-1)(p-2)` ordered distinct triples. Exactly `(p-1)/2` are AP supports `{-u,0,u}`, so the generic Z class has

\[
\frac{(p-1)(p-5)}6
\]

supports.

For a generic Z support the all-distinct type is the only local type. If its label-class sizes are `N_a,N_b,N_c`, then `H_{ab}=N_a` and `H_{ba}=N_b`; edge symmetry forces

\[
N_a=N_b=N_c=N=n/3.
\]

For a fixed balanced row, every vertex has one neighbour in each colour. The exact pairing probability from the preceding contingency theorem is

\[
\Pr_{\rm conf}(Ay=0)=
\frac{6^n((N-1)!!)^3(N!)^3}{(3n-1)!!}.
\]

Multiplying by the `n!/(N!)^3` rows for one support gives

\[
R_n:=\frac{n!6^n((N-1)!!)^3}{(3n-1)!!}
\sim 2\sqrt{2\pi n}\left(\frac23\right)^n.
\]

All these pairings are simple: each vertex has at most one stub aimed at any fixed colour, including its own colour, so loops and parallel edges are impossible. Therefore the normalized generic-Z contribution in the uniform simple cubic graph is

\[
\frac{p-5}{6}\frac{R_n}{\Pr_{\rm conf}(\mathrm{simple})}
=O\!\left(p\sqrt n\left(\frac23\right)^n\right)
=e^{-\Omega(n)}
\]

for polynomially bounded `p`, using `Pr_conf(simple)->e^{-2}`.

## Class AP — the preceding theorem already gives the `8/(9n)` main term

The cumulative artifact

`research7_2026-09-17/R7-07/artifacts/2026-09-18/2026-09-18T172000Z__F0003_full_AP_entropy_and_twin_dominance.md`

proved, for the complete family of rows with values `{-u,0,u}`, that

\[
\mathbb E_{\rm simple}\frac{S_p^{AP}(A)}{p-1}
=\frac{8}{9n}+o(n^{-1}).
\]

The `8/9` term is exactly the `N=1` row `u(e_i-e_j)`, equivalently a false-twin pair: two nonadjacent vertices with the same three neighbours. Every AP profile with `N>=2` contributes `o(n^{-1})` in aggregate. No hypothesis from the present classification is used in that theorem, so this reuse is noncircular.

## Class C0 — exact formula and an `O(n^{-3})` aggregate bound (B25)

Normalize the support to `{0,1,-2}`. Let the corresponding class sizes be `Z,N_1,N_{-2}`. Write `x_s` for the number of source vertices in class `s` whose neighbour type is `(1,1,-2)`; all remaining vertices have type `000`.

The half-edge flows from source class `s` are

\[
H_{s0}=3(N_s-x_s),\qquad H_{s1}=2x_s,\qquad H_{s,-2}=x_s.
\]

Symmetry gives

\[
x_1=2x_{-2},\qquad x_0=3(N_{-2}-x_{-2}),\qquad N_1=2N_{-2}.
\]

Put `N_{-2}=N`, `N_1=2N`, `Z=n-3N`, and `t=x_{-2}`. Then

\[
x_{-2}=t,\qquad x_1=2t,\qquad x_0=3(N-t).
\]

Feasibility is

\[
\max(0,2N-n/3)\le t\le N,
\]

with the diagonal-pairing parity condition `t` even. The exact favourable-pairing count for this fixed label profile and fixed `t` is

\[
\begin{aligned}
F_{N,t}={}&
\binom{n-3N}{3(N-t)}
\binom{2N}{2t}
\binom Nt
3^{3N}
[6(N-t)]!\,[3(N-t)]!\,(2t)!\\
&\times
(3n-18N+9t-1)!!
(4t-1)!!
(t-1)!!.
\end{aligned}
\tag{C0.1}
\]

There are `n!/((n-3N)!(2N)!N!)` rows with these three class sizes. Hence the normalized projective expectation of the whole C0 orbit is exactly

\[
M^{C0}_{n,N}=
\frac{n!}{(n-3N)!(2N)!N!}
\frac{\sum_tF_{N,t}}{(3n-1)!!}.
\tag{C0.2}
\]

To control all `N`, set `alpha=N/n`, `tau=t/n`, and define

\[
\Phi(x)=x\log x-x,\qquad
\Psi(x)=\frac x2\log x-\frac x2,
\]

with `0 log 0=0`. Uniform Stirling expansion of (C0.2) has exponential rate

\[
\begin{aligned}
R_{C0}(\alpha,\tau)={}&
\Phi(1)-\Phi(1-3\alpha)-\Phi(2\alpha)-\Phi(\alpha)\\
&+\Phi(1-3\alpha)-\Phi(3(\alpha-\tau))-\Phi(1-6\alpha+3\tau)\\
&+\Phi(2\alpha)-\Phi(2\tau)-\Phi(2\alpha-2\tau)\\
&+\Phi(\alpha)-\Phi(\tau)-\Phi(\alpha-\tau)
+3\alpha\log3\\
&+\Phi(6(\alpha-\tau))+\Phi(3(\alpha-\tau))+\Phi(2\tau)\\
&+\Psi(3-18\alpha+9\tau)+\Psi(4\tau)+\Psi(\tau)-\Psi(3).
\end{aligned}
\tag{C0.3}
\]

All `log n` coefficients cancel. Differentiation collapses to

\[
\frac{\partial R_{C0}}{\partial\tau}
=\frac32\log
\frac{\tau(1-6\alpha+3\tau)}{3(\alpha-\tau)^2}.
\tag{C0.4}
\]

The unique interior stationary point is

\[
\tau=3\alpha^2,
\]

and it is a minimum: the derivative tends to `-infinity` at the lower feasible endpoint and to `+infinity` at the upper endpoint. Thus the maximum occurs at one of the two endpoints. At the upper endpoint `tau=alpha`,

\[
\begin{aligned}
R_{C0,+}(\alpha)
&=\frac12(1-3\alpha)\log(1-3\alpha)
+\frac{3\alpha}{2}\log(\alpha/3)+4\alpha\log2\\
&=-\frac12 h(3\alpha)
+3\alpha\log\left(\frac{2^{4/3}}3\right),
\end{aligned}
\tag{C0.5}
\]

where `h(x)=-x log x-(1-x)log(1-x)`.

For `alpha<=1/6`, the other endpoint is `tau=0`; subtracting its rate from (C0.5) and setting `x=3alpha` gives

\[
\frac12\big[(1-x)\log(1-x)-(1-2x)\log(1-2x)-x\log x\big]\ge0,
\]

the binary entropy of the split `x+(1-2x)=1-x`. For `alpha>=1/6`, the lower endpoint is `tau=2alpha-1/3`; setting `x=1-3alpha` gives the identical nonnegative entropy expression. Hence (C0.5) is the global rate maximum.

Since `2^{4/3}/3<1`, (C0.5) is strictly negative for every fixed `alpha>0`; moreover

\[
R_{C0,+}(\alpha)\le-\frac12h(3\alpha)
\le \frac{3\alpha}{2}\log(3\alpha).
\tag{C0.6}
\]

For each fixed `N`, direct expansion of (C0.1)-(C0.2) gives, termwise,

\[
M^{C0}_{n,N,t}=\Theta\!\left(n^{-3N+3t/2}\right).
\tag{C0.7}
\]

Parity forces `t` even. Therefore the largest fixed-`N` power is `n^{-3}` (attained only at the first sparse possibilities `N=1,t=0` and `N=2,t=2`); every other fixed `N` is lower order. For `N` above a sufficiently large fixed cutoff but `N=o(n)`, (C0.6), together with the polynomial Stirling prefactor from the fixed finite collection of factorials, gives

\[
M^{C0}_{n,N}\le n^C\left(\frac{3N}{n}\right)^{3N/2}.
\]

Choosing the fixed cutoff larger than `2(C+2)/3` makes this range summable as `o(n^{-3})`. For `N>=\varepsilon n`, continuity and strict negativity of (C0.5) give exponential decay. Consequently

\[
\boxed{
\sum_N M^{C0}_{n,N}=O(n^{-3}).
}
\tag{C0.8}
\]

Conditioning on simplicity multiplies this upper bound by at most `Pr_conf(simple)^{-1}=O(1)`, so the same `O(n^{-3})` bound holds in the uniform simple cubic graph.

## Class C4 — exact formula and a uniform exponential gap (B25)

Normalize the support to `{1,-2,4}`. Write the two allowed local types as

\[
T_1=(1,1,-2),\qquad T_2=(-2,-2,4).
\]

Let `L=n/3`; feasibility itself forces `3|n`, and because a cubic graph has even `n`, this means `6|n`. If the class sizes are `N_1,N_{-2},N_4`, summing the literal zero neighbour sums over all vertices, or equivalently solving the edge-balance equations, gives

\[
N_1-2N_{-2}+4N_4=0.
\]

With `N_4=m`, the unique parametrization is

\[
N_1=2(L-m),\qquad N_{-2}=L+m,\qquad N_4=m.
\tag{C4.1}
\]

Let `x_s` be the number of source vertices in class `s` of type `T_1`, and put `t=x_4`. Edge symmetry gives

\[
x_1=2(L-m-t),\qquad
x_{-2}=L-m+t,\qquad
x_4=t.
\tag{C4.2}
\]

The feasible interval is `0<=t<=min(m,L-m)` together with `m-t` even. For a fixed label profile and `t`, the favourable pairing count is

\[
\begin{aligned}
G_{m,t}={}&
\binom{2(L-m)}{2t}
\binom{L+m}{2m-t}
\binom mt
3^n\\
&\times[2(L-m+t)]!\,(2t)!\,(2m-t)!\\
&\times[4(L-m-t)-1]!!
[L+3m-t-1]!!
[m-t-1]!!.
\end{aligned}
\tag{C4.3}
\]

The corresponding normalized projective expectation is

\[
M^{C4}_{n,m}=
\frac{n!}{[2(L-m)]!(L+m)!m!}
\frac{\sum_tG_{m,t}}{(3n-1)!!}.
\tag{C4.4}
\]

Put `beta=m/n`, `tau=t/n`,

\[
A=2(1/3-\beta),\quad B=1/3+\beta,\quad C=\beta,
\]

and

\[
x_A=2(1/3-\beta-\tau),\quad
x_B=1/3-\beta+\tau,\quad
x_C=\tau.
\]

The Stirling rate from (C4.4) is

\[
\begin{aligned}
R_{C4}(\beta,\tau)={}&
\Phi(1)-\Phi(A)-\Phi(B)-\Phi(C)
+\sum_{s=A,B,C}[\Phi(N_s)-\Phi(x_s)-\Phi(N_s-x_s)]\\
&+\log3
+\Phi(2(1/3-\beta+\tau))+\Phi(2\tau)+\Phi(2\beta-\tau)\\
&+\Psi(4(1/3-\beta-\tau))
+\Psi(1/3+3\beta-\tau)
+\Psi(\beta-\tau)-\Psi(3),
\end{aligned}
\tag{C4.5}
\]

where in the summation `N_s` denotes respectively `A,B,C`. Differentiation simplifies to

\[
\frac{\partial R_{C4}}{\partial\tau}
=\frac12\log
\frac{(\beta-\tau)(1/3-\beta+\tau)^2}
{\tau^2(1/3+3\beta-\tau)}.
\tag{C4.6}
\]

The stationarity polynomial factors as

\[
(\beta-\tau)(1/3-\beta+\tau)^2
-\tau^2(1/3+3\beta-\tau)
=-\frac19(1-3\beta+9\tau)(3\beta^2-\beta+\tau).
\]

The first root is outside the feasible interval; the unique feasible critical point is

\[
\tau_*(\beta)=\beta(1-3\beta),
\]

and the derivative changes from positive to negative there, so it is the global maximum. Substitution gives

\[
\boxed{
R_{C4}^*(\beta)=
\frac13(1-3\beta)\log(1-3\beta)
+\frac23(1+3\beta)\log(1+3\beta)
-\beta\log\beta
-(1+\beta)\log3
+(4/3-4\beta)\log2.
}
\tag{C4.7}
\]

With `x=3beta`, this is

\[
R_{C4}^*(x)=
\frac13[(1-x)\log(1-x)+2(1+x)\log(1+x)-x\log x+4(1-x)\log2]-\log3.
\tag{C4.8}
\]

Its derivative has the sign of

\[
\log\frac{(1+x)^2}{16x(1-x)}.
\]

The only critical points are

\[
x_{\pm}=\frac{7\pm4\sqrt2}{17}.
\]

`x_-` is the only interior local maximum; `x_+` is a minimum, while both endpoint limits equal `log(2^{4/3}/3)<0`. Since `0.078<x_-<0.080`, elementary bounds `log(1+x)<=x`, `log2<0.7`, `log3>1.09`, and `log(12.5)<2.6` give from (C4.8)

\[
R_{C4}^*(x_-)
<\frac13[0.1728+0.208+2.5816]-1.09
<-0.10.
\]

(The displayed logarithm bounds follow directly from the exponential power series; the margin is more than `0.10`, so no numerical fit is being used.) Thus

\[
\boxed{R_{C4}^*(\beta)\le-0.10\quad(0\le\beta\le1/3).}
\tag{C4.9}
\]

Uniform Stirling bounds in the finite factorial expression (C4.4), followed by summing `O(n^2)` possible `(m,t)`, yield

\[
\boxed{
\sum_m M^{C4}_{n,m}=e^{-\Omega(n)}.
}
\tag{C4.10}
\]

Again conditioning on simplicity changes this only by a bounded factor.

## Theorem B — complete support-three first moment

Combining the exhaustive classification with the four class estimates gives, uniformly for primes `p>7` with `p=n^{O(1)}`,

\[
\begin{aligned}
\mathbb E_{\rm simple}\frac{S_p^{(3)}(A)}{p-1}
&=\underbrace{\left(\frac{8}{9n}+o(n^{-1})\right)}_{AP\text{ / false twins}}\\
&\quad+\underbrace{O\!\left(p\sqrt n(2/3)^n\right)}_{Z}
+\underbrace{O(n^{-3})}_{C0}
+\underbrace{e^{-\Omega(n)}}_{C4}.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathbb E_{\rm simple}\frac{S_p^{(3)}(A)}{p-1}
=\frac{8}{9n}+o(n^{-1}).
}
\tag{B.1}
\]

In particular the entire exactly-three-residue modular-null stratum is already at the **conjectured cubic singularity scale `n^{-1}`**, and its first-order mass is exhausted by false twins. Any obstruction to improving the current global upper exponent `a_3>=1/4` must come from support size at least four (including genuinely growing support), not from any three-residue additive resonance.

## Metric and remaining gap

Frozen metric before: `a_3>=1/4`.  
Frozen metric after: `a_3>=1/4`.  
**NO SOURCE-METRIC MOVEMENT.**

The source-level problem remains open because the modular surjection inequality needs the **total** normalized kernel moment. This artifact removes every support-three profile but leaves

\[
\mathbb E\frac{S_p^{(\ge4)}(A)}{p-1}
\]

uncontrolled at the growing prime `p=n^{1/3-o(1)}`. The next run is protocol-forced STUCK2 rather than another ordinary lemma run because this is the third consecutive ordinary no-movement iteration after STUCK1.

## Dated literature boundary — 2026-09-18 UTC

Fresh bounded searches on 2026-09-18 still separate the undirected sharp-rate question from later directed work. Current status material records Huang's polynomial undirected bound and states that the sharp fixed-degree undirected exponent remains unknown. Nguyen--Pan, *A note on the singularity probability of random directed d-regular graphs* (arXiv:2308.06461; EJC 2024), proves `n^{-1/3+o(1)}` for the **directed** model via modular singularity and inverse characteristic-function/Kneser machinery. He--Huang, arXiv:2609.05297, submitted 2026-09-04, proves hard-edge/small-ball estimates for random regular **digraphs**, again not the undirected F0003 source target. No bounded search result was treated as proof of novelty or openness.

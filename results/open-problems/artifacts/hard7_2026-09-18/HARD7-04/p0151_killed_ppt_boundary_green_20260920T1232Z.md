Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# P0151 analytic artifact — exact critical Green function at the oldest-age boundary

This is a self-derived theorem-sized auxiliary result for `HARD7-04` and the exact fixed-outdegree preferential-attachment target reserved in `operations/claims/P0151.md`. It works at the **critical Pólya-point-tree mean-operator level**. It does **not** prove a finite-graph coupling and therefore does not by itself move the frozen finite-graph exponent `gamma_E`.

The main point is that the killed critical Pólya-point-tree already contains both source-side signatures that one expects from the growing-graph critical-window theory:

1. an oldest-age particle at cutoff `x=e^{-L}` has expected total progeny of exact order `e^{L/2}/L`, hence `sqrt(n)/log n` when `L=log n`;
2. an age-uniform root has uniformly bounded expected total progeny as `L->infinity`.

These two facts are proved exactly below from the two-state Doob transform. They are not inferred from the independently attached-edge growing-graph theorem.

---

## Proposition

Fix integer `m>=2` and `delta>0`. Put

`a:=m+delta`, `A:=2m+delta`, `chi:=a/A`, `alpha:=chi-1/2=delta/(2A)`.

Use the Pólya-point-tree constants

`c:=m*a/A`,
`d:=m*(a+1)/A`,
`e:=(m-1)*a/A`,
`g:=sqrt(d*e)`,
`lambda0:=c+g`.

Let

`q:=c/lambda0`, `p:=g/lambda0`,

so `q+p=1`, and let the positive Perron vector be

`r_O:=sqrt(d)`, `r_Y:=sqrt(e)`.

Write

`c_O:=1/r_O`, `c_Y:=1/r_Y`, `C_g:=c_O+c_Y`.

At the critical retention parameter

`pi_c=alpha/lambda0`,

let `R_L=pi_c T_L` be the Pólya-point-tree mean-offspring operator restricted to log-age interval

`0<=u:=-log x<=L`.

For a particle of type `s in {O,Y}` at log-age `u`, let

`F_s^L(u)`

be the expected **total** population of the corresponding killed multitype branching process, including the initial particle. Equivalently,

`F^L=(I-R_L)^(-1) 1`,

which is finite because the killed Perron root satisfies `r(R_L)<1`.

Define

`E_L:=1-exp(-L/2)`

and

`B_L:=[2 alpha c_Y E_L
       +2 alpha^2 p C_g(2E_L-L exp(-L/2))]
      /(1+alpha p L)`.                                           (P.1)

Then the two oldest-boundary values are **exactly**

`F_O^L(L)=1+r_O p exp(L/2) B_L`,                                 (P.2)

`F_Y^L(L)=1+r_Y q exp(L/2) B_L`.                                 (P.3)

Moreover

`L B_L -> B_*:=2 c_Y/p+4 alpha C_g>0`,                           (P.4)

so

`F_O^L(L) ~ K_O exp(L/2)/L`,                                     (P.5)

`F_Y^L(L) ~ K_Y exp(L/2)/L`,                                     (P.6)

with explicit positive constants

`K_O:=r_O p B_*`, `K_Y:=r_Y q B_*`.                              (P.7)

In particular, under the finite-graph cutoff identification `L=log n`, the killed-PPT oldest-particle susceptibility has the exact scale

`F_s^{log n}(log n) ~ K_s sqrt(n)/log n`.                         (P.8)

There is also a uniform local-susceptibility bound. There exists a finite constant `C=C(m,delta)` such that for every `L>=1`, every `0<=u<=L`, and both types,

`F_s^L(u)<=C exp(u/2)`.                                           (P.9)

Consequently, if `U_L` has the age-uniform density in log coordinates

`P(U_L in du)=exp(-u)du/(1-exp(-L)), 0<=u<=L`,

then

`sup_{L>=1} E[F_s^L(U_L)]<infinity`.                              (P.10)

Thus the same exact killed critical operator simultaneously exhibits bounded susceptibility for a typical age and `sqrt(n)/log n` total progeny for the oldest age.

---

## 1. Negation attack before proof

The preceding spectral artifact proved

`1-r(R_L)=C_spec/L^2+O(L^-3)`.

A naive resolvent-norm argument therefore gives only

`||(I-R_L)^(-1)||=Theta(L^2)`.

If the constant forcing `1` had an order-one projection onto the long-lived quasistationary mode at the oldest boundary, one would expect an extra factor of order `L` or `L^2` on top of the harmonic weight `exp(L/2)`. That would contradict the `sqrt(n)/log n` scale suggested by the independent-edge growing-graph theorem and would make the killed-PPT route unsuitable.

The calculation below attacks that possibility directly. The near-null mode does exist, but the forcing and boundary conditions create an exact cancellation. Only one inverse power of `L` survives at the oldest boundary.

This is the substantive counterexample-oriented question of this run: **does the killed-PPT resolvent actually produce the proposed scale, or does the `L^-2` spectral gap force a different polynomial/logarithmic normalization?** The answer is the former, exactly.

---

## 2. B9 — randomize: critical Doob transform and the resolvent equation

The critical harmonic function from the previous spectral artifact is

`h_s(u)=r_s exp(u/2)`.

Under the exact Doob transform, the killed critical operator becomes a substochastic two-state Markov-additive kernel `K_L`. If

`A(u):=int_u^L alpha exp[-alpha(v-u)] phi_O(v) dv`,                (2.1)

`B(u):=int_0^u alpha exp[-alpha(u-v)] phi_Y(v) dv`,                (2.2)

then

`(K_L phi)_O=q A+p B`,
`(K_L phi)_Y=p A+q B`.                                            (2.3)

The total-progeny equation

`F=1+R_L F`                                                       (2.4)

becomes, after writing `F_s=h_s phi_s`,

`phi=g+K_L phi`,                                                  (2.5)

where

`g_O(u)=c_O exp(-u/2)`,
`g_Y(u)=c_Y exp(-u/2)`.                                           (2.6)

Hence

`phi_O=g_O+qA+pB`,
`phi_Y=g_Y+pA+qB`.                                                (2.7)

Differentiating (2.1)-(2.2) gives

`A'=alpha A-alpha phi_O`,
`B'=alpha phi_Y-alpha B`.                                        (2.8)

Using `q+p=1`, this reduces exactly to

`A'=alpha p(A-B)-alpha g_O`,                                     (2.9)

`B'=alpha p(A-B)+alpha g_Y`.                                     (2.10)

The boundary conditions are

`B(0)=0`, `A(L)=0`.                                               (2.11)

**B9 outcome: successful.** The operator resolvent is now an explicit one-dimensional boundary-value problem for a randomized centered log-age walk, with no approximation and no finite-graph independence assumption.

---

## 3. B14 — exploit the two-state symmetry: one scalar solves the system

Set

`D(u):=A(u)-B(u)`.

Subtracting (2.10) from (2.9) cancels the entire homogeneous dynamics:

`D'(u)=-alpha(g_O(u)+g_Y(u))
      =-alpha C_g exp(-u/2)`.                                     (3.1)

Therefore, with `D_0:=D(0)=A(0)` because `B(0)=0`,

`D(u)=D_0-2 alpha C_g(1-exp(-u/2))`.                              (3.2)

Integrating (2.9) from `0` to `L` and using `A(L)=0` gives

`D_0
 =-alpha p int_0^L D(v)dv
   +2 alpha c_O E_L`.                                             (3.3)

Now

`int_0^L D(v)dv
 =D_0 L-2 alpha C_g[L-2E_L]`.                                    (3.4)

Substitution into (3.3) yields the exact scalar

`D_0
 =[2 alpha c_O E_L
   +2 alpha^2 p C_g(L-2E_L)]
  /(1+alpha p L)`.                                                (3.5)

At the oldest boundary `u=L`, `A(L)=0`, so

`B(L)=-D(L)=2 alpha C_g E_L-D_0`.                                (3.6)

Using (3.5), this simplifies to exactly (P.1):

`B(L)
 =[2 alpha c_Y E_L
   +2 alpha^2 p C_g(2E_L-L exp(-L/2))]
  /(1+alpha p L)`.                                                (3.7)

The numerator is positive: `E_L>0` and

`2E_L-L exp(-L/2)
 =2[1-(1+L/2)exp(-L/2)]>0` for `L>0`.                            (3.8)

Finally, at `u=L`, equations (2.7) and `A(L)=0` give

`phi_O(L)=c_O exp(-L/2)+pB(L)`,                                  (3.9)

`phi_Y(L)=c_Y exp(-L/2)+qB(L)`.                                  (3.10)

Multiplying by `h_s(L)=r_s exp(L/2)` gives (P.2)-(P.3).

**B14 outcome: successful.** The exact symmetry `Q=[[q,p],[p,q]]` kills the difficult mode in the difference coordinate and produces a closed-form Green function. No spectral-series estimate is needed.

---

## 4. The `sqrt(n)/log n` boundary scale

From (3.7),

`E_L->1`, `L exp(-L/2)->0`, and `1+alpha pL~alpha pL`.

Therefore

`L B(L)
 ->[2 alpha c_Y+4 alpha^2 p C_g]/(alpha p)
 =2 c_Y/p+4 alpha C_g
 =B_*>0`.                                                         (4.1)

Substituting (4.1) into (P.2)-(P.3) proves (P.5)-(P.7).

The exponent `1/2` is not put in by hand. It comes from the exact critical harmonic function `h_s(u)=r_s exp(u/2)`. The extra `1/L` comes from the oldest-boundary Green amplitude (3.7). Hence, when the finite graph has smallest available age of order `1/n`, so `L=log n`, the killed local object predicts exactly

`sqrt(n)/log n`.                                                  (4.2)

This is a local-operator theorem only. It does not identify the finite-graph largest component until an exploration coupling is proved through this scale.

---

## 5. Uniform bounded typical-age susceptibility

The same exact solution also shows why a typical root does not inherit the oldest-root divergence.

From (3.5),

`D_0-2 alpha C_g
 =[-2 alpha(c_Y+c_O exp(-L/2))
   -4 alpha^2 p C_g E_L]
  /(1+alpha pL)`.                                                 (5.1)

Thus

`|D_0-2 alpha C_g|<=C_1/(1+L)`.                                  (5.2)

Equation (3.2) becomes

`D(u)=[D_0-2 alpha C_g]+2 alpha C_g exp(-u/2)`.                   (5.3)

Hence, uniformly in `0<=u<=L`,

`|int_u^L D(v)dv|<=C_2`,                                         (5.4)

because the constant part has size `O((1+L)^-1)` over an interval of length at most `L`, while the exponential part is integrable.

Integrating (2.9) backward from `A(L)=0`,

`A(u)=-alpha p int_u^L D(v)dv
      +alpha int_u^L g_O(v)dv`,                                  (5.5)

so `sup_{L,u} A(u)<infinity`. Then (5.3) gives a uniform bound on `B=A-D`. Since `A,B>=0` by definition, (2.7) implies

`sup_{L,u,s} phi_s(u)<infinity`.                                 (5.6)

Therefore

`F_s^L(u)=r_s exp(u/2) phi_s(u)<=C exp(u/2)`,                     (5.7)

which is (P.9).

If `U_L` is the log-age of a vertex whose age is uniform on `[e^-L,1]`, its density is `exp(-u)/(1-exp(-L))`. Hence for `L>=1`,

`E F_s^L(U_L)
 <=C/(1-exp(-1)) int_0^L exp(-u/2)du
 <=2C/(1-exp(-1))`.                                               (5.8)

This proves (P.10).

The exact killed-PPT therefore has the same qualitative coexistence emphasized in the growing-graph critical-window literature: the oldest boundary supports a `sqrt(n)/log n` scale while typical susceptibility stays bounded.

---

## 6. B21 — ask who else has this shape: comparison with killed branching-random-walk criticality

A fresh bounded literature search on 20 September 2026 recovered:

- Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026): exact threshold and the Pólya-point-tree spectral-radius mechanism for fixed-outdegree PA, but not a finite-size critical-window theorem;
- Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937 (submitted 22 December 2025): for an **independent-edge** growing-graph class, a `(log n)^(-2)` window, `sqrt(n)/log n` largest components, finite critical susceptibility, and killed branching-random-walk analysis;
- Mörters--Schätze, arXiv:2606.27844 (26 June 2026): a different inhomogeneous preferential-attachment-kernel ensemble in the infinite-variance regime.

Searches for `Pólya point tree critical susceptibility`, `Polya point tree susceptibility percolation`, `sqrt(n)/log n preferential attachment percolation fixed outdegree`, and source-title/citation combinations did not surface a source-matching finite fixed-outdegree critical-window result or this exact boundary-resolvent formula. This is bounded negative evidence only, not a novelty certificate.

The transfer from Jorritsma--Maillard--Mörters is therefore **methodological, not theorem-level**: their killed-BRW shape suggested computing the exact Green function of the fixed-outdegree Pólya-point-tree. The derivation above is carried out directly from the fixed-outdegree PPT constants and does not import independent-edge hypotheses.

**B21 outcome: successful.** The comparison identifies the right finite-to-local coupling target sharply: it is no longer enough to show only the `L^-2` spectral gap. One must preserve the boundary Green amplitude `B_L~B_*/L` and the harmonic factor `exp(L/2)` under finite-graph exploration.

---

## 7. What this buys, and the precise remaining obstruction

The previous spectral artifact had already established the candidate window scale `(log n)^(-2)` at the mean-operator level. This artifact now derives the candidate component scale `sqrt(n)/log n` and bounded typical susceptibility **inside the same exact fixed-outdegree local operator**.

What is still missing is a finite-graph statement of the following form. For an oldest (or `O(1)`-oldest) seed, one needs a coupling or comparison valid up to total explored mass of order `sqrt(n)/log n` such that

1. the sequential fixed-`m` within-birth dependence changes the killed-PPT Green function by only `o(sqrt(n)/log n)` at first moment;
2. collisions/depletion do not destroy a positive fraction of the boundary Green mass;
3. enough second-moment/tail control survives to convert path/progeny expectation into actual distinct-component size.

The present exact formulas show what the coupling must preserve:

`exp(L/2) B_L ~ B_* exp(L/2)/L`.                                 (7.1)

Any route that controls only the Perron root but loses the `1/L` boundary amplitude is insufficient.

This is a substantially sharper finite-to-local target than the earlier generic instruction “couple to the killed PPT”.

---

## 8. Frozen metric status

The task's frozen finite-graph quantity remains

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)|/log n`.

The preceding finite-graph theorem proved

`gamma_E>=b13`.

This run does **not** establish the finite-graph coupling required to transfer (P.8), so the honest before/after values are

**Before:** `gamma_E>=b13`.

**After:** `gamma_E>=b13` — **no movement**.

The new result is an exact source-relevant local scaling theorem, not a relabeling of the frozen metric. Because the preceding runs moved the metric, this is not a Section-I stuck episode.

---

## 9. Validation scope

No finite exhaustive claim is made, so no checker is required. Validation in this run is the all-parameter derivation on the page:

- exact Doob similarity;
- exact inhomogeneous two-state resolvent equations;
- exact scalar reduction for `D=A-B`;
- exact boundary formula (P.1);
- positive numerator check;
- explicit asymptotics and uniform susceptibility bound.

The theorem remains a self-check until independently audited. It does not satisfy the closure protocol for P0151.

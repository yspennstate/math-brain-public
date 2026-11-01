Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.

# P26 / LIVE20 T08 — weighted exceptional Green transfer and exact-distance-six halves of non-Ramanujan Cayley bigraphs

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run; `PARTIAL / OPEN` after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A–C below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. Bounded searches on 20 September 2026 for combinations of `distance six Cayley bigraph cutoff`, `distance-6 halved graph random walk cutoff`, `Sarnak-Xue Green cutoff half graph`, and `weighted exceptional spectrum cutoff transitive graph` recovered the EFMP NBRW theorem and general distance/halved-graph terminology, but no matching ordinary-SRW cutoff theorem for the exact-distance-six arithmetic class below. This is negative evidence only, not a priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff and complementary C28/NM13-01 split

The controlling LIVE20 policy replaces P26's old audit-first assignment by T08 probability research. The newest own substantive report before this run was

`2026-09-20_10-59-32__biregular-distance4-green-transfer.md`.

That report proved a radial-clock Green transfer and applied the EFMP Sarnak--Xue shell front to the exact bigraph-distance-four graph on the left side of the non-Ramanujan Eisenstein `(9,3)` Cayley bigraphs, giving a 288-regular spectral-but-not-long-range transitive cutoff class.

The newest relevant live historical-C28 successor state read this run is NM13-01's `2026-09-20T08-55-00Z__ledger_delta.json`. NM13-01 now owns algebraic/transitivity routes: automorphism-memory semidirect Cayley lifts, root-stabilizer likelihood, phase-coexistence necessity, and possible TV/log-Sobolev control of growing hidden memory. Its newest theorem transfers cutoff through bounded automorphism memory and gives a degree-10 non-LRE Cayley class. P26 does **not** duplicate that route. This run stays on shell Green functions and asks whether one can replace a crude count of exceptional modes by their actual entropic-time spectral weight.

No three-run no-progress trigger applies: the preceding P26 runs changed theorem scope and mechanism. No target switch is required.

## 1. Exact source convention and current exact scope

Justin Salez, `arXiv:2508.21055`, uses independent mean-one exponential holding times. If `P` is discrete-time SRW, the source continuous-time walk is

\[
H_t=e^{t(P-I)}=e^{-t}\sum_{j\ge0}\frac{t^jP^j}{j!}.
\tag{1.1}
\]

Salez's Problem 2.3 asks to prove cutoff for all bounded-degree vertex-transitive expander sequences. Here `expander` means diverging size, uniformly bounded degree, and ordinary spectral gap bounded away from zero.

The primary boundary was refreshed on 20 September 2026:

* Dylan J. Altschuler, `arXiv:2609.14945`, submitted 14 September 2026, proves an explicit Gaussian-profile cutoff theorem for every fixed-degree **long-range expander** sequence. The same paper proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range}\Longrightarrow\text{spectral},
  \]
  with neither converse. Long-range expansion is therefore not synonymous with the hypothesis of Salez Problem 2.3.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a universal window bound in terms of their non-equilibrium Poincare quantity `gamma_*`. The checked result does not deduce the required `gamma_*` lower bound from vertex transitivity plus the ordinary spectral gap alone.
* Shai Evra, Brooke Feigon, Kathrin Maurischat and Ori Parzanchevski, `arXiv:2312.06507`, construct arithmetic biregular Cayley bigraphs. Their Eisenstein family contains examples that are adjacency-Ramanujan but genuinely non-Ramanujan for NBRW; nevertheless they satisfy a Sarnak--Xue density theorem and a bounded-window NBRW cutoff estimate. That weighted exceptional-spectrum estimate is the external input used below.

The repository's posted Salez Problem 2.4 Abelian-Cayley product-condition work remains excluded and untouched. This run concerns Problem 2.3 only.

## 2. Parent before/after and mechanism-level movement

### Parent problem before

Salez Problem 2.3 was `OPEN / PARTIAL`. P26 had proved cutoff for several explicit spectral-but-not-long-range transitive classes, most recently exact-distance-four left graphs of suitable EFMP bigraphs.

### Parent problem after

Salez Problem 2.3 remains `OPEN / PARTIAL`; no claim of general closure is made.

The proved source-compatible subclass is strictly enlarged: the ordinary rate-one continuous-time SRW on the **exact bigraph-distance-six graph on the left side** of the non-Ramanujan Eisenstein `(9,3)` Cayley bigraph family has an explicit Gaussian cutoff profile. The output graphs are 4608-regular, vertex-transitive Cayley spectral expanders, and they provably fail every fixed long-range-expansion constant.

This is not the previous 18-regular half graph or 288-regular exact-distance-four graph: all distance-two and distance-four edges are absent, and one output jump is a uniformly chosen six-edge geodesic in the biregular ancestor.

### Mechanism-level movement

The new mechanism is a **weighted exceptional Green criterion**. Previous count-based P26 criteria paid one unit for every exceptional mode and therefore required the number of exceptions to be subexponential on the `sqrt(log n)` scale. The present criterion instead pays the mode's actual contribution *after propagation to the entropic radius*. Thus polynomially many exceptional modes are harmless when their entropic-time weighted mass is small. This is exactly the regime supplied by a Sarnak--Xue density theorem.

The criterion is quantitative: it gives an explicit radial cleanup shift and therefore an explicit mixing-window cost.

## 3. Theorem A — weighted exceptional Green-to-TV transfer

Let `V_n` be a transitive finite state space with uniform stationary law `pi_n`. Suppose a rate-one continuous-time chain `H_t^{(n)}` started from `x` has an exact shell representation

\[
\delta_xH_t^{(n)}=\sum_{r\ge0}\Pr(R_t=r)\nu_{n,r}^x.
\tag{3.1}
\]

Let `ell_n` be an entropic shell radius. Assume the shell Green function has a decomposition, uniformly in `x`,

\[
\chi^2(\nu_{n,\ell_n+h}^x\Vert\pi_n)
\le B_n(h)+W_n(h),\qquad h\ge0,
\tag{3.2}
\]

where the exceptional contribution is a weighted Laplace sum

\[
W_n(h)=\sum_{a\in E_n} b_{n,a}e^{-2\kappa_{n,a}h},
\qquad b_{n,a}\ge0,\quad \kappa_{n,a}>0.
\tag{3.3}
\]

The coefficient `b_{n,a}` is already the contribution of mode `a` **at radius `ell_n`**. Define the weighted entropic defect

\[
\mathfrak D_n:=W_n(0)=\sum_{a\in E_n}b_{n,a}.
\tag{3.4}
\]

Assume also that shells up to radius `r` are supported on sets `A_{n,x}(r)` satisfying

\[
\pi_n(A_{n,x}(\ell_n-h))\le L_n(h).
\tag{3.5}
\]

Then for every `t,h>=0`,

\[
\boxed{
 d_n(t)
 \le
 \Pr(R_t<\ell_n+h)
 +\frac12\sqrt{B_n(h)+W_n(h)}
}
\tag{3.6}
\]

and

\[
\boxed{
 d_n(t)
 \ge
 \Pr(R_t\le\ell_n-h)-L_n(h).
}
\tag{3.7}
\]

Here transitivity makes the worst-start TV distance equal to the point-start value.

### Proof

For (3.6), split (3.1) at `ell_n+h`. Early shells cost at most their total mass. For a late shell, Cauchy--Schwarz gives

\[
\|\nu-\pi_n\|_{TV}\le\frac12\sqrt{\chi^2(\nu\Vert\pi_n)}.
\]

Convexity of TV under mixing then gives (3.6). For (3.7), test TV against `A_{n,x}(ell_n-h)`: all shells with `r<=ell_n-h` lie inside that set, while stationarity puts mass at most `L_n(h)` there. `QED`

### Quantitative cleanup shift

For fixed `epsilon`, define

\[
h_{n,\epsilon}:=
\inf\{h\ge0:B_n(h)+W_n(h)\le4\epsilon^2,\ L_n(h)\le\epsilon\}.
\tag{3.8}
\]

Then the Green part of the TV window costs at most `h_{n,epsilon}` radial layers.

A useful corollary is obtained when

\[
B_n(h)\le A e^{-ah},\qquad
\kappa_{n,a}\ge c>0.
\tag{3.9}
\]

Then

\[
W_n(h)\le \mathfrak D_ne^{-2ch},
\]

and one may take

\[
\boxed{
 h_{n,\epsilon}
 \le
 \max\left\{
 \frac1a\log\frac{A}{2\epsilon^2},
 \frac1{2c}\log\frac{\mathfrak D_n}{2\epsilon^2},
 h_n^{\rm low}(\epsilon)
 \right\},
}
\tag{3.10}
\]

where `h_n^{low}` is any shift making `L_n(h)<=epsilon`.

Consequently, if the radial front has width `w_n->infinity` and

\[
\log(1+\mathfrak D_n)=o(w_n),
\tag{3.11}
\]

then the exceptional spectrum does not asymptotically widen the cutoff window. This is strictly weaker than bounding `|E_n|`: a polynomial exceptional sector is allowed if its individual modes have already been attenuated enough by radius `ell_n`.

More generally one need not assume a common `c`; the exact weighted transform `W_n(h)` in (3.3) is the criterion. This is the form relevant to spectral-density estimates.

## 4. Why Sarnak--Xue is exactly a weighted Green input

The checked EFMP argument yields, for the directed-edge NBRW on a left-transitive `(K+1,k+1)` bigraph, a chi-square estimate whose two contributions are a tempered bulk term and a weighted exceptional term. After projection from directed edges to the left endpoint and averaging the initial edge, chi-square can only decrease.

For their Sarnak--Xue families, if

\[
\ell_n=\log_{Kk}|L_n|+O(1),
\]

then the resulting left endpoint shell law `nu_r^x` satisfies

\[
\boxed{
\sup_x\chi^2(\nu_{\ell_n+h}^x\Vert\pi_{L_n})
\le C_{K,k}\left(k^{-2h}+(Kk)^{-h}\right),
\qquad h\ge0.
}
\tag{4.1}
\]

The first term is the weighted exceptional sector; the second is the tempered bulk. In the language of Theorem A,

\[
W_n(h)\le Ck^{-2h},\qquad
B_n(h)\le C(Kk)^{-h},
\tag{4.2}
\]

uniformly in `n`. Thus

\[
h_{n,\epsilon}=O_{K,k}(\log(1/\epsilon))
\tag{4.3}
\]

for the Green cleanup, even though the family is genuinely non-Ramanujan and Sarnak--Xue permits a polynomial exceptional sector. This is the substantive advantage over the crude exception-count criterion.

On the lower side, a length-`2r` nonbacktracking endpoint lies in the left half-ball of radius `r`. The universal biregular tree has left sphere growth `(Kk)^r`, so

\[
L_n(h)\le C_{K,k}(Kk)^{-h}.
\tag{4.4}
\]

Hence both sides of Theorem A have exponentially small radial cleanup cost.

## 5. Exact distance six on the left side of a biregular bigraph

Let

\[
X=(L\sqcup R,E)
\]

be connected, left-transitive, `(K+1,k+1)`-biregular, and of girth greater than twelve. Define `Y^{[6]}(X)` on `L` by

\[
x\sim_{Y^{[6]}}y
\quad\Longleftrightarrow\quad
\operatorname{dist}_X(x,y)=6.
\tag{5.1}
\]

Every left automorphism preserves this relation, so `Y^{[6]}` is vertex-transitive. If `X` is a Cayley bigraph, the left regular action is simply transitive and `Y^{[6]}` is a Cayley graph.

Two distinct six-edge geodesics with the same endpoints would create a cycle of length at most twelve, so the girth assumption makes the endpoint count exact. Therefore

\[
\boxed{
D_3=(K+1)k(Kk)^2
}
\tag{5.2}
\]

is the output degree.

## 6. Theorem B — exact spherical polynomial and spectral gap

Let `M` be the `|L| x |R|` incidence matrix and put

\[
B=MM^T.
\]

Let `A_m` be adjacency on left vertices at exact bigraph distance `2m`. Then

\[
A_1=B-(K+1)I.
\tag{6.1}
\]

The distance-regular intersection count on the biregular tree gives

\[
A_1^2=A_2+(k-1)A_1+(K+1)kI
\tag{6.2}
\]

and, for `m>=2`,

\[
\boxed{
A_1A_m=A_{m+1}+(k-1)A_m+KkA_{m-1}.
}
\tag{6.3}
\]

Under girth `>4m`, the same identity holds on the finite quotient through radius `m`: every counted geodesic is unique and no additional intersection can occur without making a cycle of length at most `4m`.

For `m=2`, substituting (6.1) into (6.2) gives

\[
A_2=B^2-(2K+k+1)B+K(K+1)I.
\tag{6.4}
\]

For `m=3`, (6.3) yields

\[
\boxed{
A_3=\big(B-(K+k)I\big)A_2-KkA_1.
}
\tag{6.5}
\]

This is an exact polynomial in `B`, so the output spectrum is an explicit spherical transform of the adjacency spectrum of the bigraph.

### Concrete Eisenstein parameters `(K,k)=(8,2)`

Here

\[
D_3=9\cdot2\cdot16^2=4608,
\]

and (6.5) simplifies to

\[
\boxed{
Q_3=\frac{A_3}{4608}=q_3(B),\qquad
q_3(x)=\frac{x^3-29x^2+246x-576}{4608}.
}
\tag{6.6}
\]

The Perron eigenvalue of `B` is

\[
b_0=(K+1)(k+1)=27,
\]

and `q_3(27)=1`.

For an adjacency-Ramanujan `(9,3)` bigraph, every nontrivial nonzero eigenvalue of `B` lies in

\[
[(\sqrt8-\sqrt2)^2,(\sqrt8+\sqrt2)^2]=[2,18],
\tag{6.7}
\]

with zero modes also allowed.

The derivative of the numerator in (6.6) is

\[
3x^2-58x+246,
\]

whose critical points are

\[
x_\pm=\frac{29\pm\sqrt{103}}3.
\]

At the endpoints and zero,

\[
q_3(0)=-\frac18,\qquad
q_3(2)=-\frac1{24},\qquad
q_3(18)=\frac1{16}.
\tag{6.8}
\]

At the two critical points,

\[
q_3(x_\mp)=
-\frac{31}{31104}
\pm\frac{103\sqrt{103}}{62208}.
\tag{6.9}
\]

Since `sqrt(103)<11`, both values have absolute value strictly below `1/8`. Therefore every nonconstant output eigenvalue has modulus at most `1/8` and

\[
\boxed{
\operatorname{gap}(Y^{[6]})\ge\frac78.
}
\tag{6.10}
\]

In particular the output is connected and is a very strong spectral expander, even though its NBRW ancestor is genuinely non-Ramanujan.

## 7. Exact shell representation and the new radial clock

Lift rate-one continuous-time SRW on `Y^{[6]}` to the exact-distance-six left graph of the universal `(K+1,k+1)`-biregular tree. Let

\[
R_t=\frac12\operatorname{dist}(o,Z_t)
\]

be the half-radius.

The root stabilizer acts transitively on every left sphere. Therefore, conditional on `R_t=r`, the lifted endpoint is uniform on the left sphere of bigraph radius `2r`. Projecting to the finite bigraph gives exactly the left endpoint law `nu_r^x` of a uniformly chosen nonbacktracking path of length `2r`.

Hence, in the exact source convention,

\[
\boxed{
\delta_xe^{t(Q_3-I)}
=
\sum_{r\ge0}\Pr(R_t=r)\nu_r^x.
}
\tag{7.1}
\]

This is the bridge from EFMP's weighted Green shells to ordinary continuous-time SRW on the new 4608-regular graph.

## 8. Exact radial law for the `(9,3)` family

For an interior state `r>=3`, classify the six-edge geodesic from the current left vertex by the number `s=0,...,6` of initial ancestor edges it follows toward the root before turning. Since the final vertex is left, the half-radius increment is

\[
\Delta R=3-s.
\]

For `(K,k)=(8,2)`, the exact multiplicities are

\[
\begin{array}{c|rrrrrrr}
\Delta R&-3&-2&-1&0&1&2&3\\ \hline
\#&1&1&14&16&224&256&4096.
\end{array}
\tag{8.1}
\]

Their sum is `4608`. Thus the interior drift is

\[
\boxed{
v=\frac{1445}{512}
}
\tag{8.2}
\]

and the raw second-moment rate for the rate-one compound-Poisson walk is

\[
\boxed{
M_2=\frac{12713}{1536}.
}
\tag{8.3}
\]

The boundary region `{0,1,2}` is a finite perturbation. Because the interior increment has positive mean, there exists `theta>0` with

\[
\mathbb E e^{-\theta\Delta R}<1.
\]

The standard exponential-supermartingale argument implies a geometric tail on the number of returns to the boundary region. Hence the total number of boundary-modified jumps is `O_P(1)`. Coupling with the unrestricted compound-Poisson sum gives

\[
\frac{R_t-vt}{\sqrt{M_2t}}\Longrightarrow N(0,1).
\tag{8.4}
\]

No discrete-time lazification is introduced; the Poisson clock here is exactly the rate-one source convention (1.1).

## 9. Theorem C — Gaussian cutoff for the new class

Take the non-Ramanujan Eisenstein Cayley bigraph family of EFMP with `p=2`, so `(K+1,k+1)=(9,3)`. The checked source properties used here are:

1. left transitivity / Cayley structure;
2. adjacency-Ramanujan spectrum, giving (6.7);
3. logarithmically growing girth, hence eventually girth `>12`;
4. the Sarnak--Xue weighted NBRW Green estimate (4.1).

Let `n=|L_n|` and

\[
\ell_n=\log_{16}n+O(1).
\]

By (4.1), the shell Green error after `ell_n+h` is `O(4^{-h}+16^{-h})`. By (4.4), the stationary mass of the pre-entropic half-ball is `O(16^{-h})`. Combining Theorem A with (7.1) and the radial CLT (8.4) yields

\[
\boxed{
T_n=\frac{\ell_n}{v}
=\frac{512}{1445}\log_{16}n+O(1)
}
\tag{9.1}
\]

and a `Theta(sqrt(log n))` cutoff window. More precisely, for every fixed real `z`,

\[
\boxed{
 d_{TV}\left(T_n+z\sqrt{\log_{16}n}\right)
 \longrightarrow
 \Phi\left(-\frac{z}{\tau}\right),
}
\tag{9.2}
\]

where

\[
\boxed{
\tau^2=\frac{M_2}{v^3}
=\frac{3332636672}{9051588375}.
}
\tag{9.3}
\]

Indeed, at `t=T_n+z sqrt(ell_n)`,

\[
\frac{\ell_n-vt}{\sqrt{M_2t}}
\to -\frac{zv^{3/2}}{\sqrt{M_2}}=-\frac z\tau.
\]

Taking a cleanup shift `h->infinity` with `h=o(sqrt(ell_n))` makes both Green and lower-support errors vanish while leaving the Gaussian radial coordinate unchanged. Equations (3.6)--(3.7) then squeeze TV to the same Gaussian tail.

This proves ordinary **rate-one continuous-time simple random walk cutoff** on the exact-distance-six output graphs. EFMP's NBRW cutoff is used only to supply the weighted shell Green estimate; it is not being relabeled as the output chain.

## 10. The output is not a long-range expander

The output degree is

\[
D=4608.
\]

One output step moves at most three half-radii in the biregular ancestor. A left half-ball of radius `s` in the ancestor has size `O(16^s)`. Therefore

\[
|B_{Y^{[6]}}(x,r)|\le C16^{3r}=C4096^r.
\tag{10.1}
\]

A degree-4608 long-range expander would require singleton growth at the tree branching scale

\[
(D-1)^r=4607^r
\]

through a fixed positive fraction of the logarithmic range. But

\[
4096<4607.
\]

Taking, for example,

\[
r_n=\left\lfloor\frac12\log_{4607}n\right\rfloor
\]

gives

\[
\frac{|B_{Y^{[6]}}(x,r_n)|}{4607^{r_n}}
\le C\left(\frac{4096}{4607}\right)^{r_n}\longrightarrow0.
\tag{10.2}
\]

Thus the output family fails every fixed long-range-expansion constant while retaining spectral gap at least `7/8`. It is genuinely a spectral-but-not-long-range class, so Altschuler's output hypothesis does not apply to it.

## 11. Exact sanity calculation executed this run

The executed checker is

`2026-09-20_11-57-39__weighted-green-distance6-checker.py`

with archived output

`2026-09-20_11-57-39__weighted-green-distance6-checker.out`.

It checks using exact integer/rational arithmetic:

* degrees `18,288,4608`;
* the recurrence-derived spherical polynomial
  \[
  x^3-29x^2+246x-576;
  \]
* `q_3(27)=1`, `q_3(0)=-1/8`, `q_3(2)=-1/24`, `q_3(18)=1/16`;
* the two exact derivative critical points and the rigorous `|q_3|<1/8` bound there;
* all seven radial multiplicities;
* `v=1445/512`;
* `M_2=12713/1536`;
* `tau^2=3332636672/9051588375`;
* the strict branching mismatch `4096<4607`.

The terminal marker is

`ALL_CHECKS_PASS`.

The checker certifies the finite algebra and arithmetic only; the asymptotic probability proof is written in Sections 3--10.

## 12. Residual obstruction, failed-route history and next attack

### Residual obstruction

The parent conjecture still lacks a way to create the weighted shell Green front from **arbitrary vertex transitivity plus spectral expansion**. This report removes the need to count exceptional modes individually, but the needed entropic-time weighted mass is still supplied by EFMP's arithmetic Sarnak--Xue theorem.

### Failed-route history preserved

Earlier P26/NM13-01 work already showed that:

* maximal tree-rate / long-range volume growth is not forced by ordinary transitivity plus spectral gap;
* a raw global heat-kernel or NBRW `L^2` criterion can be polynomially large at the relevant TV scale even on transitive cutoff examples;
* counting exceptional modes is too crude once a polynomial exceptional sector is permitted.

This run does not reopen those routes. It replaces the third obstruction by entropic-time weighting.

### Next P26 attack

The next route is to express the weighted defect

\[
\mathfrak D_n
\]

as a **closed reduced-walk / Ihara-trace quantity** and seek a transitivity-stable estimate from ordinary spectral expansion plus a tangle decomposition. Concretely, the target is a bound of the form

\[
\log(1+\mathfrak D_n)=o(\sqrt{\log n})
\tag{12.1}
\]

without assuming an arithmetic Sarnak--Xue theorem. The planned attack is to split closed reduced walks at the first repeated directed edge, control the tangle-free part by the spectral gap, and show that transitivity prevents enough positive-density tangles to make (12.1) fail. A decisive failure of this route would identify the precise local obstruction a counterexample to Salez 2.3 would need.

This remains complementary to NM13-01, which is attacking phase coexistence/root-stabilizer likelihood and growing automorphism memory rather than shell spectral density.

## 13. ledger_delta

```yaml
slot: P26
parent: T08
source: Salez arXiv:2508.21055 Problem 2.3
runtime_model: GPT-5.6 Sol
runtime_reasoning: UNVERIFIED
parent_status_before: PARTIAL / OPEN
parent_status_after: PARTIAL / OPEN
source_level_advance: >-
  Strictly enlarges proved source-compatible cutoff subclasses to exact bigraph-distance-six
  left graphs of the p=2 non-Ramanujan Eisenstein Cayley bigraph family.
mechanism_advance: >-
  Weighted exceptional Green criterion: exceptional modes are charged by their actual
  entropic-radius contribution rather than by cardinality; quantitative cleanup shift
  h_epsilon is explicit, and log(1+D_n)=o(window) suffices.
new_class: exact-distance-six left graphs of EFMP p=2 Eisenstein Cayley bigraphs
new_class_degree: 4608
new_class_vertex_transitive: true
new_class_cayley: true
new_class_spectral_gap_lower: 7/8
new_class_long_range_expander: false
new_class_center: (512/1445) log_16 n + O(1)
new_class_window: Theta(sqrt(log n))
new_class_profile_tau_squared: 3332636672/9051588375
proof_status: CANDIDATE_FULL pending later independent review
publication_novelty: UNVERIFIED
companion_split: >-
  NM13-01 owns root-stabilizer likelihood, phase-coexistence and automorphism-memory routes;
  P26 owns shell Green/spectral-density/radial-clock transfer.
checker: 2026-09-20_11-57-39__weighted-green-distance6-checker.py
checker_output: 2026-09-20_11-57-39__weighted-green-distance6-checker.out
checker_result: ALL_CHECKS_PASS
residual_obstruction: >-
  Derive a small entropic-time weighted exceptional Green defect directly from arbitrary
  bounded-degree vertex transitivity plus ordinary spectral expansion.
next_attack: >-
  Rewrite the weighted defect as an Ihara/closed-reduced-walk trace, split by first repeated
  directed edge, and test whether transitivity plus spectral expansion controls the tangle contribution.
```

End of complete P26 substantive T08 report.

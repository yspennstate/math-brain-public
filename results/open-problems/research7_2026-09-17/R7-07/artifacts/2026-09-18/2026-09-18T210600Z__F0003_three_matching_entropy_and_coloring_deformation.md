Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested in prompt text, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — exact three-matching entropy formula, edge-coloring size bias, and nontrivial-charge incoherence

Date: 2026-09-18 UTC.  
Slot: `R7-07 Hard Problem New Methods`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Outside target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020; *Probability Surveys* 18 (2021)), Section 5 immediately after Theorem 5.2, PDF p. 8.  
Frozen metric:

\[
a_3:=\sup\{a\ge0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Cumulative proved value before this artifact: **`a_3 >= 1/4`**.  
Value after this artifact: **`a_3 >= 1/4` — NO SOURCE-METRIC MOVEMENT.**

Methods in this final-recovery iteration are the three reserved by the preceding report: **B4 PROVE SOMETHING WEAKER, COMPLETELY / B6 DEFORM TO A SOLVED POINT / B26 HUNT THE SPORADIC CASE**.

The main new theorem is an exact two-matching reduction for the union-of-three-perfect-matchings model. Conditional on the first two matchings, the probability that the third matching closes a modular null equation is given exactly by a symmetric contingency-table product. Its logarithm is `-(n/2)` times the joint entropy of that table, up to `O(k^2 log n)` for a row using `k` residues. This identifies the missing growing-support estimate as a **mutual-information problem**, rather than an undifferentiated Fourier mixing problem.

A second exact result identifies the model deformation: the union-of-three-matchings ensemble is precisely the uniform cubic configuration model size-biased by the number of ordered proper 3-edge-colorings. The Radon–Nikodym derivative and its mean are explicit. Thus qualitative contiguity cannot by itself preserve the polynomial singularity exponent; a quantitative lower tail for the number of 1-factorizations is required.

Finally, the projective Fourier decomposition from the preceding run is sharpened: every **nontrivial** multiplicative-character block of the hyperbolic Fourier transform has coherence at most `2/sqrt(p)`, including the quadratic/Salié sector. The quadratic character is therefore not a sporadic locally coherent obstruction. The only charge sector with order-one individual matrix entries is the trivial character sector.

---

## 1. B4: the easier colored model

Let `n=2N` and let `\mathcal M_n` denote the set of perfect matchings of `[n]`, so

\[
|\mathcal M_n|=(n-1)!!=(2N-1)!!.
\]

For a matching `M`, let `P_M` be its symmetric permutation matrix. Thus `P_M^2=I`, `P_M=P_M^T`, and `P_M` has zero diagonal.

Take three independent uniform perfect matchings `M_1,M_2,M_3` and define

\[
A^{\rm col}:=P_{M_1}+P_{M_2}+P_{M_3}.
\tag{1.1}
\]

This is the adjacency matrix of a cubic edge-colored configuration: parallel edges are allowed, but the three color classes are independent perfect matchings.

The fixed finite-group theorem of Nguyen--Wood gives the correct first-cokernel-moment scale in this model for every **fixed** prime `p` not dividing 3. The point here is to ask what can be proved directly and uniformly when `p=p(n)` grows.

### 1.1 Exact alternating-cycle polynomial

Fix a reference perfect matching `M_0`. For `M in \mathcal M_n`, let

\[
C(M_0,M)
\]

be the number of connected alternating components of the 2-regular multigraph `M_0 \cup M`, counting a doubled common edge as one component.

Define

\[
F_N(x):=\sum_{M\in\mathcal M_{2N}}x^{C(M_0,M)}.
\]

Then

\[
\boxed{
F_N(x)=x(x+2)(x+4)\cdots(x+2N-2).
}
\tag{1.2}
\]

**Proof.** Choose one reference edge `{a,b}` of `M_0`.

If `{a,b}` is also an edge of `M`, then deleting `a,b` removes a doubled alternating component, so the contribution is

\[
xF_{N-1}(x).
\]

Otherwise `a` is matched by `M` to some `c` and `b` to some `d`. Delete `a,b` and splice the two `M`-edges into the edge `{c,d}`. This gives a perfect matching `M'` of the remaining `2N-2` vertices and preserves the number of alternating components. Conversely, for each `M'`, choose one of its `N-1` edges `{c,d}` and one of the two ways to unsplice it through `a,b`. Hence every `M'` has exactly `2(N-1)` preimages in this case. Therefore

\[
F_N(x)=(x+2N-2)F_{N-1}(x),
\]

with `F_1(x)=x`, proving (1.2). `\square`

### 1.2 Exact kernel dimension for the difference of two matching matrices

On an alternating component of length `2\ell`, the permutation `P_{M_0}P_M` has two cycles of length `\ell`. Since

\[
(P_{M_0}-P_M)y=0
\iff
P_{M_0}P_My=y,
\]

each alternating component contributes exactly two free field coordinates. Therefore over **every** field,

\[
\boxed{
\dim\ker(P_{M_0}-P_M)=2C(M_0,M).
}
\tag{1.3}
\]

For every prime `p`, (1.2) and (1.3) give

\[
\boxed{
\mathbb E_{M,M'}|\ker(P_M-P_{M'}\bmod p)|
=
\prod_{j=0}^{N-1}\frac{p^2+2j}{2j+1}
=
\frac{\Gamma(N+p^2/2)\Gamma(1/2)}{\Gamma(p^2/2)\Gamma(N+1/2)}.
}
\tag{1.4}
\]

This is an exact finite-`n` formula.

### 1.3 Exact joint `L^2` identity and why the collision route is too weak

For `t,y in F_p^n`, write

\[
\Phi(t,y):=\mathbb E_M e_p(t^TP_My).
\]

Expanding the square and summing first over `t` gives

\[
\begin{aligned}
\sum_{t,y}|\Phi(t,y)|^2
&=\mathbb E_{M,M'}\sum_{t,y}e_p(t^T(P_M-P_{M'})y)\\
&=p^n\mathbb E_{M,M'}|\ker(P_M-P_{M'}\bmod p)|.
\end{aligned}
\]

Hence, exactly,

\[
\boxed{
\sum_{t,y}|\Phi(t,y)|^2
=
p^n\prod_{j=0}^{N-1}\frac{p^2+2j}{2j+1}.
}
\tag{1.5}
\]

For fixed `y`, let `\mu_y` be the law of `P_My` on the additive group `F_p^n`. Then

\[
\Pr(A^{\rm col}y=0)=(\mu_y*\mu_y*\mu_y)(0).
\]

Young/Cauchy gives

\[
\|\mu_y*\mu_y*\mu_y\|_\infty
\le \|\mu_y\|_2^2.
\]

Summing over `y` and using (1.4),

\[
\boxed{
\mathbb E|\ker(A^{\rm col}\bmod p)|
\le
\prod_{j=0}^{N-1}\frac{p^2+2j}{2j+1}.
}
\tag{1.6}
\]

For `p^2=o(n)`, Stirling's formula gives

\[
\log\prod_{j=0}^{N-1}\frac{p^2+2j}{2j+1}
=
\frac{p^2}{2}\log\frac{2eN}{p^2}
+O\!\left(\frac{p^4}{n}+\log n\right).
\tag{1.7}
\]

Thus at `p=n^{1/3-o(1)}` the right side is `\exp(O(n^{2/3+o(1)}\log n))`, far above the polynomial first-moment scale needed for the source. This is a rigorous no-go for a proof based only on the two-matching collision norm.

The slack is structural, not just asymptotic. For a nonzero constant vector `y` and `p>3`, `\mu_y` is a point mass, so `\|\mu_y\|_2^2=1`, while

\[
A^{\rm col}y=3y\ne0,
\]

and the true null probability is zero.

The threefold equation must therefore use more than pair collisions.

---

## 2. B4 stronger replacement: exact conditional contingency formula

The useful theorem comes from conditioning on the first two matchings instead of discarding the third-summand geometry.

For vectors `y,z in F_p^n`, define the ordered contingency table

\[
N_{ab}(y,z):=|\{i:y_i=a,\ z_i=b\}|.
\tag{2.1}
\]

Let `\mathcal N(y,z)` be the number of perfect matchings `M` satisfying

\[
P_My=z.
\tag{2.2}
\]

### Theorem 2.1 — exact matching-to-target count

The number `\mathcal N(y,z)` is zero unless

\[
N_{ab}=N_{ba}\quad\text{for all }a\ne b,
\tag{2.3}
\]

and every diagonal count `N_{aa}` is even. When these compatibility conditions hold,

\[
\boxed{
\mathcal N(y,z)
=
\prod_{a<b}N_{ab}!
\prod_a (N_{aa}-1)!!.
}
\tag{2.4}
\]

**Proof.** If vertex `i` lies in cell `(a,b)`, then `y_i=a` and (2.2) says its partner `j=M(i)` has `y_j=b`. Since `M` is an involution, `z_j=y_i=a`, so `j` lies in cell `(b,a)`. Thus off-diagonal cells `(a,b)` and `(b,a)` must have equal size and are paired by an arbitrary bijection, giving `N_{ab}!` possibilities. A diagonal cell `(a,a)` must be paired internally, requiring even cardinality and giving `(N_{aa}-1)!!` possibilities. Different unordered residue pairs use disjoint vertices, so the factors multiply. `\square`

Now condition on `M_1,M_2` and put

\[
z:=-(P_{M_1}+P_{M_2})y.
\tag{2.5}
\]

Then

\[
\boxed{
\Pr(A^{\rm col}y=0\mid M_1,M_2)
=
\frac{\mathcal N(y,z)}{(n-1)!!}.
}
\tag{2.6}
\]

This is exact. In particular, it automatically enforces that `z` have the same residue multiplicities as `y`; no separate orbit approximation is used.

### 2.2 Joint-entropy form

Suppose `y` uses `k` residues and (2.3) holds. Put

\[
\beta_{ab}:=N_{ab}/n,
\qquad
H(\beta):=-\sum_{a,b}\beta_{ab}\log\beta_{ab}.
\tag{2.7}
\]

Uniform Stirling estimates in (2.4) give

\[
\log\mathcal N(y,z)
=
\frac n2\log n-rac n2-rac n2H(\beta)
+O(k^2\log(n+1)).
\tag{2.8}
\]

Since

\[
\log(n-1)!!=\frac n2\log n-\frac n2+O(\log n),
\]
we obtain

\[
\boxed{
\Pr(P_My=z)
=
\exp\left\{-\frac n2H(\beta)+O(k^2\log(n+1))\right\}
}
\tag{2.9}
\]

whenever the compatibility conditions hold, and the probability is zero otherwise.

This bound remains informative uniformly for `k\le p=n^{1/3-o(1)}`, because the error is `O(n^{2/3+o(1)}\log n)`, while positive-density entropy terms can be order `n\log p`.

### 2.3 Mutual information is the exact missing variable

When `z` has the same empirical residue law as `y`, let

\[
\alpha_a:=n^{-1}|\{i:y_i=a\}|.
\]

Both marginals of `\beta` equal `\alpha`, so

\[
I(\beta):=2H(\alpha)-H(\beta)\ge0
\tag{2.10}
\]

is the mutual information of the two coordinates under `\beta`. Equation (2.9) becomes

\[
\boxed{
\Pr(P_My=z)
=
\exp\left\{-nH(\alpha)+\frac n2I(\beta)
+O(k^2\log n)\right\}.
}
\tag{2.11}
\]

There are

\[
\frac{n!}{\prod_a n_a!}
=
\exp\{nH(\alpha)+O(k\log n)\}
\tag{2.12}
\]

rows with a fixed profile. Hence the row entropy in (2.12) cancels the generic `-nH(\alpha)` term in (2.11) **exactly**; the dangerous quantity is the positive information defect `I(\beta)`.

This yields a concrete replacement for the vague growing-support obstruction:

> To control the high-alphabet contribution in the three-matching model, it is enough to show that the first two matchings rarely create a target `z=-(P_{M_1}+P_{M_2})y` whose compatible contingency table with `y` has anomalously large mutual information.

For an approximately independent balanced table on `k` residues, `H(\beta)\approx2\log k` and the conditional third-matching probability is `k^{-n+o(n)}`, exactly the scale that cancels the `k^n` row count. A table concentrated near a permutation graph has `H(\beta)\approx H(\alpha)` and loses half of that entropy. Thus the obstruction is now a precise **high-mutual-information exceptional set**.

This is the main positive B4 result of the run.

---

## 3. Two elementary invariants that the collision bound erased

The three-matching equation also gives exact low-cost filters useful for the next attack.

Let

\[
x_j=P_{M_j}y,
\qquad q(y):=\sum_i y_i^2.
\]

If `p\ne3` and `x_1+x_2+x_3=0`, summing coordinates gives

\[
\boxed{\sum_i y_i=0.}
\tag{3.1}
\]

If `p\ne2`, then each `x_j` has quadratic norm `q(y)`, and

\[
\|x_1+x_2\|_2^2=\|x_3\|_2^2
\]

gives

\[
\boxed{
\langle x_1,x_2\rangle
=
\langle x_1,x_3\rangle
=
\langle x_2,x_3\rangle
=-\frac12q(y).
}
\tag{3.2}
\]

Over the reals this is the familiar 120-degree condition for three equal-norm vectors summing to zero; over `F_p` it remains an exact algebraic constraint. Any successful growing-`p` estimate may therefore condition simultaneously on profile entropy and the exact correlation surface (3.2), rather than using the collision norm (1.6).

---

# 4. B6 — exact deformation from uniform cubic configurations to three matchings

Let `\Omega_n` be the set of perfect pairings of `3n` labelled half-edges, three at each vertex, and let `P` be uniform on `\Omega_n`. Thus

\[
P(M)=\frac1{(3n-1)!!}.
\]

For a pairing `M`, define `C(M)` to be the number of **ordered proper 3-edge-colorings** of its half-edges: each vertex sees colors `1,2,3` once each, and the two half-edges of every paired edge have the same color.

Construct another law `Q` as follows:

1. independently at each vertex, biject its three labelled half-edges with colors `1,2,3` (`6^n` choices total);
2. independently for each color, pair the `n` half-edges of that color uniformly (`(n-1)!!` choices per color);
3. forget the colors.

Each uncolored pairing `M` has exactly `C(M)` preimages. Therefore

\[
Q(M)=\frac{C(M)}{6^n((n-1)!!)^3}.
\]

Since `P` is uniform,

\[
\boxed{
\frac{dQ}{dP}(M)=\frac{C(M)}{\mathbb E_PC(M)}
}
\tag{4.1}
\]

with the exact mean

\[
\boxed{
\mathbb E_PC(M)
=
\frac{6^n((n-1)!!)^3}{(3n-1)!!}.
}
\tag{4.2}
\]

For `n=2N`, this is

\[
\mathbb E_PC
=
36^N\frac{(2N)!^3(3N)!}{N!^3(6N)!}
\sim
2\left(\frac43\right)^N
=
2\left(\frac2{\sqrt3}\right)^n.
\tag{4.3}
\]

Thus the independent-three-matching ensemble is not merely “close” to the configuration model: it is **exactly the configuration model size-biased by the number of ordered 1-factorizations**.

### 4.1 Exact transfer inequality

For every event `E` and every threshold `c_n>0`, (4.1) gives

\[
Q(E)=\frac{\mathbb E_P[C\,1_E]}{\mathbb E_PC}.
\]

On `\{C\ge c_n\}`, this implies

\[
P(E\cap\{C\ge c_n\})
\le
\frac{\mathbb E_PC}{c_n}Q(E).
\]

Hence

\[
\boxed{
P(E)
\le
P(C<c_n)
+
\frac{\mathbb E_PC}{c_n}Q(E).
}
\tag{4.4}
\]

This is the precise quantitative deformation formula. It shows why qualitative contiguity alone does not preserve a polynomial rare-event exponent.

### 4.2 Hamilton-cycle calibration of the density loss

Let `H(M)` be the number of edge-labelled Hamilton cycles in the cubic configuration multigraph. For a fixed labelled Hamilton cycle, there are `6^n` ways to assign at each vertex its two Hamilton half-edges to the two cycle neighbors, and the remaining `n` half-edges can be paired in `(n-1)!!` ways. Therefore

\[
\boxed{
\mathbb E_PH
=
\frac{(n-1)!}{2}\,
\frac{6^n(n-1)!!}{(3n-1)!!}.
}
\tag{4.5}
\]

Every Hamilton cycle gives six ordered 3-edge-colorings: choose the color of its complementary perfect matching in three ways and alternate the two remaining colors around the even cycle in two ways. Conversely one ordered coloring has only three unordered pairs of colors, hence can witness at most three Hamilton cycles. Double-counting incidences gives

\[
6H\le3C,
\qquad\text{so}\qquad
\boxed{C\ge2H.}
\tag{4.6}
\]

The ratio of the exact means is

\[
\frac{\mathbb E_PC}{\mathbb E_PH}
=
2\frac{((n-1)!!)^2}{(n-1)!}.
\]

For `n=2N`,

\[
\boxed{
\frac{\mathbb E_PC}{\mathbb E_PH}
=
4N\frac{\binom{2N}{N}}{4^N}
\sim
4\sqrt{\frac N\pi}
=
2\sqrt{\frac{2n}{\pi}}.
}
\tag{4.7}
\]

Thus a hypothetical quantitative lower-tail theorem

\[
H\ge n^{-o(1)}\mathbb E H
\]

outside a sufficiently small exceptional event would, through (4.6), make the change of measure in (4.4) cost only `n^{1/2+o(1)}`. That theorem is **not proved here**. The point of (4.7) is to quantify exactly what is missing.

Molloy--Robalewska--Robinson--Wormald, *1-Factorizations of random regular graphs*, Random Structures & Algorithms 10 (1997), 305--321, prove qualitative contiguity for each fixed `r>=3` between the random `r`-regular graph and the corresponding perfect-matching construction. Their result is directly relevant, but qualitative contiguity says only which events have probability tending to zero; it does not supply the polynomial rate required to transfer Vu's sharp exponent. Janson's asymptotic-distribution/contiguity results provide a related small-subgraph-conditioning viewpoint, again without automatically yielding the source-matched polynomial rare-event inequality needed here.

**B6 outcome:** the deformation is now exact and its missing quantitative input is explicit: a lower-tail estimate for `C/EC` (or a sufficiently strong surrogate such as `H/EH`) on the singularity event.

---

# 5. B26 — every nontrivial charge sector is incoherent, including the quadratic one

Retain the hyperbolic Fourier kernel from the preceding run,

\[
U((t,y),(t',y'))
=
p^{-1}e_p(ty'+t'y),
\tag{5.1}
\]

and the projective action

\[
g_\lambda(t,y)=(\lambda^{-1}t,\lambda y),
\qquad \lambda\in F_p^*.
\tag{5.2}
\]

Because `U` commutes with this action, `\ell^2(F_p^2)` splits into multiplicative-character sectors.

Fix a nontrivial multiplicative character `\eta`. There is no origin vector in this sector. Use normalized character vectors on

- the nonzero `t`-axis `T=\{(a,0):a\ne0\}`;
- the nonzero `y`-axis `Y=\{(0,b):b\ne0\}`;
- each hyperbola `H_r=\{(a,r/a):a\ne0\}`, `r\ne0`.

With sector-compatible character conventions, every reduced matrix coefficient is one of the following types.

### 5.1 Same-axis coefficients vanish

On `T\times T` and `Y\times Y`, the phase is identically 1. Since `\sum_{a\ne0}\eta(a)=0`,

\[
\boxed{
\langle T_\eta,UT_\eta\rangle
=
\langle Y_\eta,UY_\eta\rangle
=0.
}
\tag{5.3}
\]

For the trivial character these same coefficients equal `(p-1)/p`, which is order one. This is the first sharp distinction between trivial and nontrivial charge.

### 5.2 Axis--hyperbola and cross-axis coefficients are Gauss sums

A direct change of variables gives, up to a unit-modulus character factor,

\[
\langle T_\eta,UH_{r,\eta}\rangle
=
\frac1p\sum_{x\ne0}\overline\eta(x)e_p(rx),
\tag{5.4}
\]

and analogously for `Y`--hyperbola and `T`--`Y` coefficients. For nontrivial `\eta`, the classical Gauss-sum identity gives magnitude `\sqrt p`, so

\[
\boxed{
|\langle T_\eta,UH_{r,\eta}\rangle|
= p^{-1/2},
}
\tag{5.5}
\]

with the same `p^{-1/2}` scale for every other axis/non-axis coefficient.

### 5.3 Hyperbola--hyperbola coefficients are twisted Kloosterman sums

For `r,s\ne0`, the previous run's calculation gives

\[
\langle H_{s,\eta},UH_{r,\eta}\rangle
=
\frac1p\sum_{x\ne0}\overline\eta(x)e_p(rx+s/x).
\tag{5.6}
\]

The Weil bound yields

\[
\boxed{
|\langle H_{s,\eta},UH_{r,\eta}\rangle|
\le2p^{-1/2}.
}
\tag{5.7}
\]

Combining (5.3)--(5.7), every nontrivial charge block `U_\eta`, of dimension `p+1`, satisfies the entrywise coherence estimate

\[
\boxed{
\max_{u,v}|(U_\eta)_{uv}|\le\frac2{\sqrt p}.
}
\tag{5.8}
\]

Since `U_\eta` is unitary, this is near the smallest coherence scale compatible with a `(p+1)`-dimensional unitary matrix. It is **not** an operator-norm contraction.

In particular, the quadratic character `\eta=\chi` is not a sporadic locally coherent exception. Its hyperbola block is a Salié-type transform, but the same square-root Weil bound applies. Therefore:

\[
\boxed{
\text{quadratic/Salié charge does not saturate locally; order-one entries occur only in the trivial charge sector.}
}
\tag{5.9}
\]

A remaining obstruction may still arise from coherent **global** interference among exponentially many nontrivial charge flows; (5.8) does not rule that out.

**B26 outcome:** one candidate sporadic obstruction is eliminated exactly. The next global theorem should separate trivial-charge structure from collective nontrivial-charge interference, not single out the quadratic sector.

---

# 6. What moved mathematically and what did not

The source metric remains

\[
\boxed{a_3\ge1/4\quad\text{NO MOVEMENT}.}
\]

No theorem here proves the required source-model bound

\[
\mathcal M_{\ge4}(n,p)\le n^{-1/3+o(1)}
\]

at `p=n^{1/3-o(1)}`. Therefore F0003 remains **PARTIAL**.

Nevertheless three uncertainties are removed:

1. **The correct colored-model variable is mutual information.** The third-matching closure probability is exactly a symmetric contingency-table product and asymptotically `exp[-nH(beta)/2]`; after profile counting, excess mutual information is the precise dangerous quantity.
2. **The model mismatch is an exact size bias.** The three-matching model equals the uniform cubic configuration model tilted by `C(M)`, the number of ordered 1-factorizations, with explicit `EC` and transfer inequality (4.4).
3. **Quadratic charge is not a special local obstruction.** All nontrivial multiplicative-character sectors have `O(p^{-1/2})` entrywise coherence; only the trivial sector has order-one entries.

These results suggest that the remaining proof, if this route succeeds, must combine an entropy large-deviation estimate for the contingency table with a quantitative change-of-measure estimate. Neither ingredient can be replaced by bare `L^2` collision control or qualitative contiguity.

---

# 7. Dated literature boundary, 2026-09-18

Fresh checks this run:

- Vu's 2020/2021 source remains the retained sharp undirected fixed-degree exponent target; no bounded current search found a later theorem proving the full `d-2` exponent. This is negative evidence only, not a novelty certificate.
- Molloy, Robalewska, Robinson and Wormald, *1-Factorizations of random regular graphs*, Random Structures & Algorithms 10 (1997), 305--321, DOI `10.1002/(SICI)1098-2418(199705)10:3<305::AID-RSA1>3.0.CO;2-#`, explicitly proves qualitative contiguity for each fixed `r>=3` between random regular graphs and the perfect-matching construction.
- Janson, *Random Regular Graphs: Asymptotic Distributions and Contiguity*, gives the neighboring small-subgraph-conditioning/contiguity framework and the limiting Hamilton-cycle distribution. Its qualitative conclusion is not silently promoted to the polynomial rare-event estimate required in (4.4).
- Nguyen--Wood, arXiv:1806.10068, remains the key fixed-prime cokernel analogue for the union-of-matchings model; the fixed-group statement is not assumed uniform for `p=p(n)`.
- Nguyen--Pan's `n^{-1/3+o(1)}` singularity theorem and the September 2026 He--Huang hard-edge theorem concern directed regular models, not Vu's undirected source.

No result above is claimed novel merely because this bounded search did not find it.

---

# 8. Next nonrepeating attack

If F0003 remains the current target for the next ordinary final-recovery iteration, use a fresh triple:

1. **B3 — PROVE SOMETHING STRONGER:** prove a uniform theorem that every compatible contingency table with mutual information at least `epsilon` pays at least its `exp(-n I/2)` cost already in the first-two-matching exposure; this would make the profile sum contract instead of merely cancel.
2. **B17 — LOOK FOR THE NUMBERS SOMEWHERE ELSE:** translate the nontrivial-charge block coherence (5.8) into the language of Kloosterman/Ramanujan-type expanders and identify a known multilinear or expander-mixing inequality strong enough for a cubic tensor network rather than a single edge.
3. **B9 — RANDOMIZE:** parameterize charge flows by a cycle basis and prove suppression for a random nontrivial flow first, then isolate and count the exceptional sparse/trivial-charge flows deterministically.

This run is the second ordinary no-source-movement iteration in the final recovery cycle after STUCK2. One more ordinary no-movement iteration reaches the third-trigger boundary. Because both allowed HARD stuck recoveries are already consumed, the following trigger must produce an immutable handoff/retirement and shard-6 successor rotation, not a third stuck recovery.

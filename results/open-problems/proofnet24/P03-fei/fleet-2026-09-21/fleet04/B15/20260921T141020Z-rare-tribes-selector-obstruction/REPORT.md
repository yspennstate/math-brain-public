# B15 — no finite one-coordinate selector can pay the arithmetic remainder alone

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval/context or isolated model evaluator was used in this mathematics.  
**Route:** unequal-magnitude spectral packets / restriction of the arithmetic remainder `D`, continuing the spectral-lattice and centroid/carry handoffs.  
**Novelty:** no publication-priority claim is made. A bounded primary-literature check is recorded below.

## 1. Result

The spectral-lattice continuation defines, for every Boolean function,

\[
R(f)=\sum_a p_a r_a,\qquad
D(f)=\sum_a p_a\log_2(1/b_a),
\]

and proves the exact identity

\[
H(f)=2R(f)+2D(f).
\tag{1}
\]

For a coordinate `i`, write

\[
\Delta_i D=D(f)-\frac{D(f^{i=+})+D(f^{i=-})}{2},
\]

and analogously for `R,H`.

The earlier flat-tail continuation proved that **a prescribed coordinate** can have `Delta_i D / Inf_i` arbitrarily large, but left open whether there might nevertheless be a finite universal constant `C` such that every nonconstant Boolean function has **some** coordinate satisfying

\[
\Delta_iD\le C\,\operatorname{Inf}_i(f).
\tag{2}
\]

This run closes that particular route negatively.

### Theorem A — existential `D`-selector obstruction

There is **no finite universal constant** `C` for (2).

More quantitatively, for every integer `a>=1` there is a transitive read-once Boolean family `T_{2^a+1,w}` such that, for every coordinate `i`,

\[
\liminf_{w\to\infty}
\frac{\Delta_iD(T_{2^a+1,w})}
     {\operatorname{Inf}_i(T_{2^a+1,w})}
\ge 2^{a+1}a.
\tag{3}
\]

The right-hand side tends to infinity. Thus even **existential** one-coordinate payment of `D` alone is impossible with a dimension-independent coefficient.

This is **not a counterexample to FEI**. The family is read-once/tribes-like. The obstruction says that any universal restriction proof must retain the compensating valuation reserve `R` (or equivalent signed/KL/free-energy credits) instead of attempting to pay the positive remainder `D` in isolation.

## 2. The transitive rare-tribes family

Partition `mw` variables into `m` blocks of width `w`. On block `j`, let `A_j` be the indicator that every bit in that block is `+1`, and put

\[
T_{m,w}(x)=-1+2\prod_{j=1}^m(1-A_j(x)).
\tag{4}
\]

Thus `T=+1` exactly when no block is all `+1`. The wreath-product symmetry permuting blocks and coordinates inside blocks acts transitively on the physical variables, so all coordinate influences and all restriction ratios are identical.

Set

\[
\varepsilon=2^{-w},\qquad Q=2^w-1,\qquad q=1-\varepsilon.
\]

For a nonempty Fourier label that meets exactly `k` blocks, the coefficient is

\[
\widehat T(S)=2(-1)^k\varepsilon^kq^{m-k}
             =2(-1)^k\frac{Q^{m-k}}{2^{mw}}.
\tag{5}
\]

There are `binom(m,k) Q^k` such labels. Therefore the squared spectral mass of the `k`-block magnitude packet is

\[
p_k=4\binom mk\varepsilon^kq^{2m-k}.
\tag{6}
\]

For fixed `m` and all sufficiently large `w`, these nonconstant magnitudes are pairwise distinct and are also distinct from the constant coefficient magnitude.

## 3. Exact packet valuations

Let `V_k` be the unnormalized Walsh transform of the sign mask of the `k`-block packet. For each block define

\[
\psi_j(x)=\sum_{\varnothing\ne S\subseteq\text{block }j}\chi_S(x)
=\begin{cases}
Q,&x\text{ is all }+1\text{ on block }j,\\
-1,&\text{otherwise}.
\end{cases}
\]

Then

\[
V_k(x)=(-1)^k e_k(\psi_1(x),\ldots,\psi_m(x)),
\tag{7}
\]

where `e_k` is the elementary symmetric polynomial. Because `Q=-1 (mod 2^w)`, every value obeys

\[
V_k(x)\equiv \binom mk\pmod{2^w}.
\tag{8}
\]

At a point where no block is all `+1`, equality in absolute value is attained: `V_k=binom(m,k)`. Hence, whenever

\[
w>\max_{1\le k\le m}\nu_2\binom mk,
\]

the packet valuation is exactly

\[
r_k=\nu_2\binom mk.
\tag{9}
\]

Consequently

\[
R(T_{m,w})
=4\sum_{k=1}^m
\binom mk\varepsilon^kq^{2m-k}\nu_2\binom mk.
\tag{10}
\]

This uses the actual magnitude packets; no automatic integrality hypothesis is introduced.

## 4. Exact average reserve after restricting one coordinate

Restrict a coordinate in the first block. One child makes that block impossible to satisfy and is exactly `T_{m-1,w}`. The other child has one block of width `w-1` and `m-1` blocks of width `w`.

In the mixed-width child, for each `k` there are two noncolliding nonconstant magnitude types: the short block is untouched, or it is touched. Both sign-mask transforms have valuation `nu_2 binom(m-1,k)`; touching the short block only multiplies the transform by an odd block factor.

Their masses are respectively

\[
4\binom{m-1}{k}\varepsilon^k(1-2\varepsilon)^2
 q^{2m-2-k}
\]

and

\[
8\binom{m-1}{k}\varepsilon^{k+1}(1-2\varepsilon)
 q^{2m-2-k}.
\]

Averaging this mixed child with `T_{m-1,w}` gives the exact simplification

\[
\overline R_{\rm child}
=4\sum_{k=1}^{m-1}
\binom{m-1}{k}\varepsilon^kq^{2m-1-k}
\nu_2\binom{m-1}{k}.
\tag{11}
\]

All possible constant/nonconstant magnitude collisions are excluded by taking `w` sufficiently large at fixed `m` (the constant coefficient tends to magnitude one, whereas every nonconstant magnitude is `O_m(2^{-w})`).

The influence of every coordinate is also exact:

\[
\operatorname{Inf}_i(T_{m,w})
=2\varepsilon q^{m-1}.
\tag{12}
\]

Indeed the coordinate is pivotal exactly when all other bits of its block are `+1` and none of the other `m-1` blocks is all `+1`.

## 5. Divergence for odd `m`

Take `m` odd. The `k=1` term of (10) vanishes because

\[
\nu_2\binom m1=\nu_2(m)=0.
\]

Thus

\[
R(T_{m,w})=O_m(\varepsilon^2).
\tag{13}
\]

Let

\[
s=\nu_2(m-1)\ge1.
\]

The `k=1` term of (11) is

\[
4(m-1)s\,\varepsilon q^{2m-2},
\]

and all remaining terms are `O_m(epsilon^2)`. Therefore

\[
\Delta_iR
=R(T_{m,w})-\overline R_{\rm child}
=-4(m-1)s\,\varepsilon+O_m(\varepsilon^2).
\tag{14}
\]

Combining with (12),

\[
\frac{-\Delta_iR}{\operatorname{Inf}_i(T_{m,w})}
\longrightarrow 2(m-1)\nu_2(m-1).
\tag{15}
\]

Now use the exact inherited identity (1). Under restriction,

\[
\Delta_iD=\frac12\Delta_iH-\Delta_iR.
\tag{16}
\]

The exact Fourier restriction-entropy decomposition gives `Delta_i H>=0` (it is a sum of a Jensen-Shannon term and nonnegative binary-fibre entropies). Hence

\[
\frac{\Delta_iD}{\operatorname{Inf}_i(T_{m,w})}
\ge
\frac{-\Delta_iR}{\operatorname{Inf}_i(T_{m,w})}.
\tag{17}
\]

Finally choose

\[
m=2^a+1.
\]

Then `nu_2(m-1)=a`, so (15)-(17) give

\[
\liminf_{w\to\infty}
\frac{\Delta_iD}{\operatorname{Inf}_i}
\ge 2^{a+1}a.
\]

Transitivity makes this simultaneous for every physical coordinate. Since `2^{a+1}a` is unbounded, Theorem A follows.

## 6. Exact computation

A standard-library checker evaluates (10)-(12) with exact `Fraction` arithmetic and certifies large finite witnesses without enumerating truth tables. It also checks the first-order asymptotic coefficient.

Representative witnesses for `m=2^a+1` include:

| `a` | `m` | `w` | variables | exact certified lower bound for `Delta_i D/Inf_i` |
|---:|---:|---:|---:|---:|
| 1 | 3 | 12 | 36 | `>3` |
| 2 | 5 | 12 | 60 | `>15` |
| 3 | 9 | 12 | 108 | `>47` |
| 4 | 17 | 16 | 272 | `>127` |
| 6 | 65 | 18 | 1170 | `>767` |
| 8 | 257 | 20 | 5140 | `>4094` |
| 10 | 1025 | 24 | 24600 | `>20000` |

For the final witness the exact lower-bound ratio is approximately `20478.748940810954`; its asymptotic limit is `20480`. The decimal is display-only; every certificate comparison is exact rational arithmetic.

An initial checker run hit Python's integer-to-string display guard while formatting the enormous exact witness. The checker was repaired only by disabling that **display** digit limit; none of the mathematical formulas or assertions changed. The final checker passes.

Checker SHA-256:

`17b8a6b31bf8b71dec3ae253f522cbfd754bf1c382d0de86ed2092021f972bbb`

Verification-output SHA-256:

`fd0070bb27a7ea5116689e24d0016cd963516cae20691050d9ac13c30145c727`

## 7. What this kills, and what survives

### REFUTED here

The following universal statement is false for every finite `C`:

> Every nonconstant Boolean function has some coordinate `i` for which the arithmetic remainder satisfies `Delta_i D <= C Inf_i(f)`.

The earlier finite symmetric-threshold computations only forced such a coefficient above `23.33` through dimension `512`; they explicitly did not establish divergence. The present analytic family supplies divergence, by a different transitive rare-tribes mechanism.

### NOT refuted

- FEI itself.
- A restriction proof using the **joint** quantity `R+D=H/2`.
- A potential that retains packet KL/Jensen-Shannon credit or signed transport terms.
- Adaptive stopping trees that accumulate and later recover reserve.

Indeed, (14) shows exactly what goes wrong with a `D`-only proof: restriction creates a large positive `D` bill by **destroying negative valuation reserve**, and (16) forces those ledgers to be considered together.

## 8. Relation to current primary literature

A bounded primary-source check on 21 September 2026 found no unrestricted FEI proof. Potapov's 18 September 2026 preprint proves FEI for Boolean plateaued functions, with sharp class constant four, and partially bent functions, not arbitrary unequal-magnitude spectra. González--MacManus--Pereyra's May 2026 paper develops restriction/stopping-tree methods and explicitly leaves the full restriction inequality as the route to the conjecture. O'Donnell--Tan's composition theorem covers compositions under its hypotheses, including read-once formula consequences, which is consistent with this family being FEI-good despite the `D`-selector obstruction. Xiao Han proves a general bound with an additional influence-profile entropy term. None of these papers is used to claim novelty for Theorem A.

## 9. Next obligation

The `D`-only one-coordinate selector is now rigorously dead, even existentially. The next B15 target should keep the exact signed conservation

\[
R+D=H/2
\]

inside a restriction/stopping argument rather than upper-bounding `D` separately. For the family above, the dangerous term is the first-order reserve drop

\[
4(m-1)\nu_2(m-1)\varepsilon,
\]

which is exactly the quantity a joint potential must return as credit. A useful next theorem would decompose this reserve transfer across a stopping tree and prove that the cumulative **net** joint debt is influence-paid; a decisive obstruction would have to survive after the compensating `R` credit is retained.

### Scope summary

**PROVED here:** no finite universal existential-coordinate restriction coefficient can pay the arithmetic remainder `D` alone; explicit transitive read-once family and exact asymptotics.

**OPEN:** any dimension-free joint `R+D` stopping-tree payment strong enough to imply unrestricted FEI; unrestricted uniform-cube FEI itself.

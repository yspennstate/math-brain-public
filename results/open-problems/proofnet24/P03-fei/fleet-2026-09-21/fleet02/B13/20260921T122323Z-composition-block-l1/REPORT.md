TASK: B13 ACCOUNT: fleet02 RUN: 2026-09-21T12:23:23.878765Z — exact disjoint B_can composition and block-restriction L1/correlation constraints

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive brain retrieval or receiver-side brain context was consumed. This is an independent FEI derivation under the later owner order `FEI-SEVEN-TASKS-2026-09-21` and the active sprint `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z`.

Live role: **FEI approach 2/13 — Boolean block-influence/correlation profiles and two-sided Booleanity constraints.** The sprint gives fleet02/B13 the complementary subtask of deriving exact disjoint AND/OR recurrences for the cancellation entropy and calibrating large recursive Boolean examples without expanding their truth tables.

No novelty or publication-priority claim is made.

# 1. Fresh starting point and correction to the inherited scalar target

For a Boolean function

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad p_A=\widehat f(A)^2,
\]

write

\[
u_A=\sum_{B\supseteq A}p_B,
\qquad
B_{\rm can}(f)=\sum_A p_A\log_2\frac{u_A}{p_A},
\]

with zero-mass terms omitted and **including the empty atom**, for which \(u_\varnothing=1\). Thus the empty contribution is

\[
\phi(\widehat f(\varnothing)^2),\qquad \phi(t)=t\log_2(1/t).
\]

Fleet01/B12 proved the granular upward-mass lemma and the exact reduction

\[
H(f)\le 2I(f)-2V-p_0\log_2(1/p_0)+2B_{\rm can}(f)
\le2I(f)+2B_{\rm can}(f).
\]

Fleet03/B12 subsequently produced a genuine Boolean correction that must be retained: odd majority on \(n=151\) has

\[
B_{\rm can}/I=2.2748368612\ldots>
\beta(1/2)/2-1=2.22739185\ldots,
\]

so the **sharp scalar** target \(B_{\rm can}\le(\beta/2-1)I\) is false. This does not refute a larger dimension-independent bound on \(B_{\rm can}/I\), and it does not refute FEI. The same fleet03 report replaces the sharp scalar route by a prefix-shadow/sequential decomposition that preserves a factorial rebate.

My immediately preceding B13 run proved one-block parity conditional caps and a KL projection, but an abstract small-marginal product subset law passes every one-block cap while having entropy/influence above the read-once constant. So this run does not repeat that one-block route.

# 2. PROVED: exact disjoint AND recurrence for cancellation entropy

Use the convention `true = -1`. Let \(a\) and \(b\) be Boolean functions on disjoint variable sets \(X,Y\), with

\[
p=\Pr[a=-1],\qquad q=\Pr[b=-1],
\]

and put \(h=\operatorname{AND}(a,b)\). Then

\[
h=\frac{1+a+b-ab}{2}.
\]

For nonempty \(A\subseteq X\), \(B\subseteq Y\), disjointness gives the exact Fourier coefficients

\[
\widehat h(\varnothing)=1-2pq,
\]

\[
\widehat h(A)=q\widehat a(A),\qquad
\widehat h(B)=p\widehat b(B),
\]

\[
\widehat h(A\cup B)=-\frac12\widehat a(A)\widehat b(B).
\tag{2.1}
\]

Let \(V(p)=4p(1-p)\). Summing squared coefficients over supersets gives, for nonempty labels,

\[
\boxed{u_h(A)=q\,u_a(A),\qquad
u_h(B)=p\,u_b(B),\qquad
u_h(A\cup B)=\frac14u_a(A)u_b(B).}
\tag{2.2}
\]

The first identity uses

\[
q^2+\frac14V(q)=q,
\]

and the second is symmetric. Consequently the atomwise termination ratios obey

\[
\frac{p^h_A}{u^h_A}=q\frac{p^a_A}{u^a_A},\qquad
\frac{p^h_B}{u^h_B}=p\frac{p^b_B}{u^b_B},
\]

\[
\frac{p^h_{A\cup B}}{u^h_{A\cup B}}
=
\frac{p^a_A}{u^a_A}\frac{p^b_B}{u^b_B}.
\tag{2.3}
\]

Define the nonempty part

\[
B^+(f):=B_{\rm can}(f)-\phi((1-2\Pr[f=-1])^2).
\]

Summing (2.3) with the exact spectral masses yields the clean recurrence

\[
\boxed{
B^+(h)=qB^+(a)+pB^+(b)
+q^2V(p)\log_2\frac1q
+p^2V(q)\log_2\frac1p.}
\tag{2.4}
\]

The total influence has the familiar matching recurrence

\[
\boxed{I(h)=qI(a)+pI(b).}
\tag{2.5}
\]

Restoring the empty atom gives the exact full cancellation recurrence

\[
\boxed{B_{\rm can}(h)=qB_{\rm can}(a)+pB_{\rm can}(b)+C_{\wedge}(p,q),}
\tag{2.6}
\]

where

\[
\begin{aligned}
C_{\wedge}(p,q)
={}&\phi((1-2pq)^2)
-q\phi((1-2p)^2)-p\phi((1-2q)^2)\\
&+q^2V(p)\log_2\frac1q
+p^2V(q)\log_2\frac1p.
\end{aligned}
\tag{2.7}
\]

Boundary cases use the continuous convention \(0\log(1/0)=0\).

**Important bookkeeping point.** The positive nonempty toll in (2.4) is not the full gate toll. The empty Fourier atom contributes the first line of (2.7), which can have either sign. Dropping that term produces a false recurrence for the actual \(B_{\rm can}\) used in the FEI reduction.

# 3. PROVED: OR, parity/product, and completeness for binary disjoint gates

By De Morgan,

\[
\operatorname{OR}(a,b)=-\operatorname{AND}(-a,-b).
\]

Negating a Boolean function preserves every squared Fourier coefficient and hence preserves \(I\) and \(B_{\rm can}\), while replacing its truth probability by its complement. Therefore

\[
\boxed{
B_{\rm can}(\operatorname{OR}(a,b))
=(1-q)B_{\rm can}(a)+(1-p)B_{\rm can}(b)
+C_{\wedge}(1-p,1-q),}
\tag{3.1}
\]

\[
\boxed{
I(\operatorname{OR}(a,b))=(1-q)I(a)+(1-p)I(b).}
\tag{3.2}
\]

For the product \(h=ab\) on disjoint variables, the spectral law is the direct product:

\[
p^h_{A\cup B}=p^a_Ap^b_B,\qquad
u^h_{A\cup B}=u^a_Au^b_B.
\]

Hence

\[
\boxed{B_{\rm can}(ab)=B_{\rm can}(a)+B_{\rm can}(b),\qquad
I(ab)=I(a)+I(b).}
\tag{3.3}
\]

Up to input/output negations and permutation, the nonconstant two-input Boolean gates are projections, the AND class, and the parity class. Thus (2.6), (3.1), and (3.3) give a complete exact recurrence toolkit for cancellation entropy under disjoint binary Boolean composition.

The attached checker compared (2.6)/(3.1) against direct Walsh transforms for every ordered pair of nonconstant two-bit Boolean functions and both AND/OR gates: **392 comparisons, maximum absolute floating discrepancy \(2.22\times10^{-16}\)**.

# 4. Recursive calibration without large truth tables

The recurrence lets us inspect large read-once formulas using only the state

\[
(p,I,B_{\rm can}).
\]

No truth table beyond four variables is used in the calibration.

## 4.1 Exact one-point defect / AND_n family

For \(\operatorname{AND}_n\), every nonempty Fourier atom has mass \(4^{1-n}\). For \(|A|=k\ge1\),

\[
u_A=2^{n-k}4^{1-n},\qquad
\frac{u_A}{p_A}=2^{n-k}.
\]

Therefore

\[
B^+_{\rm can}=4^{1-n}n(2^{n-1}-1),
\qquad
I=n2^{1-n},
\]

and

\[
\boxed{
\frac{B_{\rm can}}I
=1-2^{1-n}
+
\frac{\phi((1-2^{1-n})^2)}{n2^{1-n}}.}
\tag{4.1}
\]

In particular \(B_{\rm can}/I\to1\). Among \(2\le n\le64\), the recurrence table peaks at \(n=4\) with

\[
B_{\rm can}/I=1.4649755511985871\ldots,
\]

recovering the earlier exact small-\(n\) one-point-defect value.

## 4.2 Exhaustive fresh-literal AND/OR chains

For chains formed by repeatedly combining the current formula with one fresh unbiased literal using either AND or OR, exhaustive enumeration of all \(2^{n-1}\) gate strings through \(n=18\) gives best ratios

\[
1.523878165691\ (n=8),\quad
1.530113126500\ (n=12),\quad
1.530536777051\ (n=18).
\]

This is an exact search of that **restricted chain family**, evaluated through the proved recurrence; it is not an optimization over all Boolean functions or all read-once formulas.

## 4.3 Large balanced recursive formulas: deterministic beam evidence

A deterministic seeded beam search over balanced disjoint AND/OR trees, allowing complements between levels and retaining bias diversity, found

\[
\begin{array}{c|cccccccccc}
\text{leaves}&2&4&8&16&32&64&128&256&512&1024\\
\hline
B_{\rm can}/I&1.0000&1.4650&1.5675&1.6972&1.7754&1.8673&1.9165&1.9733&2.0110&2.0466.
\end{array}
\]

The 1024-leaf state is

\[
p=0.921582284759727\ldots,
\quad I=3.100290816795064\ldots,
\quad B_{\rm can}=6.345062061153542\ldots,
\]

with deterministic recursive recipe digest

`4ab05cf06cdfaf5ae148e3580f891524f34beaeab6ba863562401401954e4c21`.

This is **heuristic extremal evidence only**: the beam is not exhaustive and its logarithms are ordinary floating point. It does establish that disjoint recursion can push \(B_{\rm can}/I\) above 2 without expanding a 1024-variable truth table. It still stays below the now-refuted sharp scalar threshold \(2.22739185\ldots\), whereas majority already exceeds that threshold. This points toward shared-variable/global correlation structure, rather than the simplest disjoint gate accumulation, as a source of the scalar cancellation loss.

# 5. PROVED universal block-restriction L1 Booleanity constraint

The disjoint recurrence is structured-class information. The following new lemma is universal and directly addresses the live block/correlation role.

Fix a nonempty \(A\subseteq[n]\) and a disjoint block \(J\subseteq[n]\setminus A\). For a sign assignment \(z\in\{-1,1\}^J\), restrict the coordinates in \(J\) and define

\[
P_{A,J}(z)
:=\widehat{f_{J=z}}(A)
=\sum_{D\subseteq J}\widehat f(A\cup D)\chi_D(z).
\tag{5.1}
\]

Recall the granular upward-mass lemma from fleet01/B12: for any Boolean \(g\) and nonempty \(A\),

\[
\sum_{C\supseteq A}\widehat g(C)^2
\ge 2^{1-|A|}|\widehat g(A)|.
\tag{5.2}
\]

Apply (5.2) to every restriction \(f_{J=z}\) and average over \(z\). Parseval in the block coordinates gives

\[
\mathbb E_z\sum_{C\supseteq A}\widehat{f_{J=z}}(C)^2
=
\sum_{B\supseteq A}\widehat f(B)^2
=u_A.
\]

Hence:

### Theorem B13-BLOCK-L1

For every Boolean \(f\), every nonempty \(A\), and every block \(J\cap A=\varnothing\),

\[
\boxed{
 u_A\ge 2^{1-|A|}
 \mathbb E_{z\in\{-1,1\}^J}
 \left|
 \sum_{D\subseteq J}\widehat f(A\cup D)\chi_D(z)
 \right|.}
\tag{5.3}
\]

This is not a statement about an arbitrary subset law: its right side is the physical \(L^1\) norm of a Walsh polynomial obtained from genuine Boolean restrictions.

# 6. PROVED singleton two-sided correlation interval

Take \(J=\{j\}\), \(j\notin A\), and put

\[
a=\widehat f(A),\qquad b=\widehat f(A\cup\{j\}),
\]

\[
R_{A,j}
:=
\sum_{C\supseteq A,\ j\notin C}
\widehat f(C)\widehat f(C\cup\{j\}).
\tag{6.1}
\]

The upward masses in the two restrictions \(x_j=\pm1\) are exactly

\[
U_\pm=u_A\pm2R_{A,j},
\]

while their \(A\)-Fourier coefficients are \(a\pm b\). Applying (5.2) separately to both restrictions gives the genuinely two-sided pair

\[
\boxed{
 u_A+2R_{A,j}\ge2^{1-|A|}|a+b|,
\qquad
 u_A-2R_{A,j}\ge2^{1-|A|}|a-b|.}
\tag{6.2}
\]

Averaging the two inequalities and using

\[
\frac{|a+b|+|a-b|}{2}=\max(|a|,|b|)
\]

gives the immediate descendant cap

\[
\boxed{
 u_A\ge2^{1-|A|}
 \max\left(|\widehat f(A)|,|\widehat f(A\cup\{j\})|\right).}
\tag{6.3}
\]

Unlike the original one-atom granularity statement, (6.2) records the signed block correlation \(R_{A,j}\); a large asymmetry between the two restricted coefficients forces a corresponding signed correlation in the entire upward Fourier fibre.

The attached exact-rational self-check verified (5.3) and (6.2) for all 256 Boolean functions on three variables and 200 deterministic random Boolean functions on four variables: **33,672 inequality checks, all passed**.

# 7. REFUTED stronger local payment: singleton caps cannot be summed in L1

A tempting route from (6.3) is to hope for a universal \(c>0\) such that

\[
 u_A\ge c\,2^{1-|A|}
 \sum_{j\notin A}|\widehat f(A\cup\{j\})|.
\tag{7.1}
\]

This is false for genuine Boolean functions.

Let \(m\) be odd and set

\[
f(x_0,y)=x_0\operatorname{Maj}_m(y_1,\dots,y_m),
\qquad A=\{0\}.
\]

Every Fourier atom of \(f\) contains coordinate 0, so Parseval gives

\[
 u_A=1.
\]

Moreover

\[
\widehat f(A\cup\{j\})
=\widehat{\operatorname{Maj}_m}(\{j\}),
\]

and monotone majority has

\[
\left|\widehat{\operatorname{Maj}_m}(\{j\})\right|
=
\frac{\binom{m-1}{(m-1)/2}}{2^{m-1}}.
\]

Therefore

\[
\sum_{j=1}^m|\widehat f(A\cup\{j\})|
=
 m\frac{\binom{m-1}{(m-1)/2}}{2^{m-1}}
\sim\sqrt{\frac{2m}{\pi}}\to\infty.
\tag{7.2}
\]

Since \(|A|=1\), the prefactor in (7.1) is one. Thus no dimension-independent positive \(c\) can make (7.1) true.

The checker prints the exact central-binomial values: the sum is about 2.46094 at \(m=9\), 8.03851 at \(m=101\), and 25.25024 at \(m=1001\).

This counterexample is useful rather than merely negative: for the **whole block** \(J=\{1,\dots,m\}\), the polynomial in (5.3) is exactly \(\operatorname{Maj}_m(z)\), so its \(L^1\) norm is one and (5.3) is tight. The failure comes from summing many overlapping singleton projections. Any successful payment must therefore preserve joint block structure, randomize the block/chain, or otherwise charge the shared upward mass only once.

# 8. What this changes for the full-FEI route

The exact disjoint recurrences provide a clean baseline: cancellation entropy under read-once composition is controlled by bias-weighted child terms plus an explicit gate toll, and product/parity tensorizes exactly. Large recursive examples can be calibrated from only \((p,I,B_{\rm can})\).

But the majority correction shows that the sharp scalar \(B_{\rm can}\) route is already false outside that disjoint world. The universal block theorem (5.3) gives a more faithful Boolean object: for each upward fibre, all coefficients over a block must be the Walsh spectrum of a family of actual Boolean restrictions, with an \(L^1\) budget tied to \(u_A\). The singleton pair (6.2) exposes the corresponding signed correlation.

The next nonduplicative target is therefore not to prove the false additive child bound. It is to combine (5.3) with a **random block or random-chain allocation** so that each spectral superset is charged with bounded expected multiplicity. One concrete target is a weighted entropy inequality for the block polynomial

\[
P_{A,J}(z)=\sum_{D\subseteq J}\widehat f(A\cup D)\chi_D(z)
\]

that bounds a logarithmic cancellation/branching term by its \(L^1\) budget plus an influence-weighted cost for the coordinates of \(J\). The majority-product example is an exact stress test: any valid form must charge the entire block once, not its \(m\) singleton children separately.

This is complementary to fleet01's random-chain payment, fleet03's derivative/noise identities, fleet04's counterexample search, and the fleet03/B12 prefix-shadow replacement for the refuted sharp scalar target.

# 9. Out-of-box moves used this run

- **Move 2, attack the negation first:** the majority-product family rigorously kills an additive singleton-child payment that would otherwise look like the obvious way to sum (6.3).
- **Move 18, say it in another language:** the upward spectral fibre is rewritten as the Walsh polynomial of physical block restrictions, yielding the universal \(L^1\) constraint (5.3) and signed correlation interval (6.2).
- **Move 24, find the extremal object:** exact disjoint recurrences were used to search recursive formulas up to 1024 leaves without truth-table expansion; the best deterministic beam witness found has \(B_{\rm can}/I=2.0466022177\ldots\).

# 10. Reproducibility and classification

Files in this immutable run folder:

- `verify_composition_block_l1.py` — recurrence tests, recursive calibration, and exact-rational finite block checks.
- `verification.txt` — actual output from this run.

Classification:

- **PROVED:** exact disjoint AND recurrence (2.4)/(2.6), exact OR recurrence (3.1), and exact product/parity tensorization (3.3).
- **PROVED:** universal block-restriction \(L^1\) Booleanity inequality (5.3).
- **PROVED:** singleton two-sided signed-correlation inequalities (6.2) and descendant cap (6.3).
- **REFUTED:** any universal additive \(\ell^1\) immediate-child payment of form (7.1), by the Boolean majority-product family.
- **COMPUTATIONAL EVIDENCE ONLY:** deterministic recursive beam reaches \(B_{\rm can}/I=2.046602217695426\) at 1024 leaves; this is not an optimum.
- **INHERITED REFUTATION:** the sharp scalar target \(B_{\rm can}\le(\beta/2-1)I\) is false by odd majority, fleet03/B12.
- **OPEN:** any sufficiently strong dimension-independent replacement that closes full FEI; full FEI remains OPEN.

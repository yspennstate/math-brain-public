# B17 FEI new proof mechanism — character-gauge total correlation and the pairwise 1/2 barrier

**Date:** 2026-09-21  
**Status of full FEI:** **OPEN / NOT PROVED**.  
**Run status:** `WITHOUT_VERIFIED_BRAIN` — no authenticated mathematical/cognitive-brain retrieval or receiver-context use occurred.  
**Role:** account03/B17, FEI new proof mechanisms.  
**Route:** new **Route 19**, written first in this run: character-gauge normalization + multiscale spectral dependence.  
**Novelty:** no publication-priority claim.

Required live FEI sources were read in order: `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`. I did not rerun the read-once certificate, the known `n<=5` FEI sweep, or any prior audit. I also consumed the newest compatible B18 structural report at commit `3c5302b44db128aced142457161a36511b7d06d6` to avoid presenting generic total correlation as new: that report already places total correlation as a boundary gap of its centered tangent polymatroid. The new content here is the exact **character-gauge FEI equivalence**, the resulting rare-marginal payment formulation, the exact binary block-tree decomposition as the intended proof engine, and a rigorous **all-fixed-C obstruction to every pairwise-tree-only implementation** of that engine.

The live task packet corrects the old `6.4547837` unrestricted target: the recovered July-2026 external seed gives a lower bound above

\[
C_{\rm seed}=6.521845710923046575.
\]

That number is used below only as a concrete sharp-scale diagnostic. Full FEI asks for some finite dimension-independent constant; none is proved here.

## What moved

Tracked quantity for this route: the fraction of the rare-marginal total-correlation payment that can be certified by the strongest ordinary pairwise Chow--Liu spanning-tree bound on an exact admissible Boolean boundary family.

- before this run: `UNMEASURED`;
- after this run: for the one-point Boolean family and **every fixed proposed FEI constant `C`**, the fraction tends to

\[
\boxed{\frac12}.
\]

At the current sharp-scale diagnostic `C_seed`, the fraction is already `0.8545943568677408` at `n=10`, `0.6351555429299899` at `n=16`, and `0.5501866558905499` at `n=32`.

Thus the pairwise-only subroute is **REFUTED** even though the same Boolean family has `H/I -> 4` and is very far from refuting FEI. The missing payment is genuinely higher-order dependence. A binary block hierarchy recovers total correlation exactly, and on the `n=32` one-point family only `25.85%` of total correlation sits at the disjoint-pair level; the remaining `74.15%` occurs at block sizes `4,8,16,32`.

Creative moves used: **#1 change category** (FEI to a character-gauge dependence problem), **#2 attack the negation first** (try to kill pairwise payment), and **#30 one scale at a time** (replace pairs by an exact multiscale block tree).

---

## 1. Exact character-gauge normalization

Let

\[
f:\{-1,1\}^n\to\{-1,1\},
\qquad
p(S)=\widehat f(S)^2,
\]

and let `X` be the spectral sample with law `p`. Write

\[
q_i=\Pr(i\in X)=\operatorname{Inf}_i(f).
\]

For `T subseteq [n]`, define the character twist

\[
f_T(x)=\chi_T(x)f(x).
\]

Then

\[
\widehat{f_T}(S)=\widehat f(S\triangle T),
\]

so twisting translates the spectral law by symmetric difference:

\[
p_T(S)=p(S\triangle T).
\]

In particular spectral entropy is invariant:

\[
H(f_T)=H(f).
\]

Meanwhile

\[
I(f_T)=\mathbb E|X\triangle T|.
\]

The minimization over `T` separates coordinatewise. Including coordinate `i` in `T` changes its contribution from `q_i` to `1-q_i`. Therefore

\[
\boxed{
\min_T I(f_T)=\sum_{i=1}^n \min(q_i,1-q_i).
}
\tag{1.1}
\]

Define

\[
r_i:=\min(q_i,1-q_i)\le\frac12.
\]

### Theorem 1.1 — exact median-gauge equivalence

For every fixed `C`, the following are equivalent:

1. `H(f)<=C I(f)` for every Boolean `f`;
2. for every Boolean spectral law `p`,
   \[
   \boxed{
   H(p)\le C\sum_i r_i.
   }
   \tag{1.2}
   \]

### Proof

If FEI with constant `C` holds universally, apply it to the minimizing twist `f_T`. Entropy is unchanged and (1.1) gives (1.2).

Conversely, (1.2) implies ordinary FEI because

\[
\sum_i r_i\le\sum_i q_i=I(f).
\]

QED.

This is not merely a normalization convention: it says a universal FEI proof is allowed to put every Boolean function into a spectral Hamming-median gauge in which every membership marginal is at most one half.

---

## 2. Exact total-correlation form and the rare-marginal frontier

Work in a minimizing character gauge and retain the notation `X_i=1[i in X]`, so `P(X_i=1)=r_i<=1/2`. Define the total correlation

\[
\operatorname{TC}(X)
:=\sum_i H(X_i)-H(X)
=\sum_i h_2(r_i)-H(X).
\tag{2.1}
\]

Substituting (2.1) into (1.2) gives an exact reformulation.

### Theorem 2.1 — FEI as a Boolean dependence lower bound

Universal FEI with constant `C` is equivalent to

\[
\boxed{
\operatorname{TC}(X)
\ge
\sum_i\bigl(h_2(r_i)-Cr_i\bigr)
}
\tag{2.2}
\]

for every median-gauged Boolean spectral sample.

No independence approximation is being made: (2.2) is just (1.2) rewritten exactly.

Since `TC>=0`, a stronger sufficient target is

\[
\operatorname{TC}(X)
\ge
\sum_i\bigl(h_2(r_i)-Cr_i\bigr)_+.
\tag{2.3}
\]

Let `q_C` be the unique solution in `(0,1/2)` of

\[
h_2(q_C)=Cq_C.
\]

Then only coordinates with `r_i<q_C` need positive payment in (2.3). At the corrected current lower-bound scale

\[
C=C_{\rm seed}=6.521845710923046575,
\]

the targeted calculation gives

\[
\boxed{
q_C=0.029149502471088176\ldots .
}
\tag{2.4}
\]

Thus, at the sharp scale, generic entropy subadditivity already makes all marginals above about `2.915%` free; the unresolved mechanism is specifically the dependence forced among **very rare spectral membership bits**.

This is the first route reduction: instead of trying to bound every conditional entropy separately, seek a structural Boolean lower bound on dependence among the rare bits.

---

## 3. Exact Boolean cancellation constraint on every pair of spectral atoms

The Fourier coefficients themselves carry more information than `p`. Put

\[
a_S=\widehat f(S).
\]

Because `f^2=1`, Fourier convolution gives

\[
\sum_S a_Sa_{S\triangle T}
=
\begin{cases}
1,&T=\varnothing,\\
0,&T\ne\varnothing.
\end{cases}
\tag{3.1}
\]

This immediately yields a useful necessary condition unavailable to an arbitrary subset distribution.

### Lemma 3.1 — pairwise square-root atom exclusion

For any two distinct spectral atoms `A != B`,

\[
\boxed{
\sqrt{p(A)}+\sqrt{p(B)}\le1.
}
\tag{3.2}
\]

### Proof

Take `T=A triangle B` in (3.1). The terms `S=A` and `S=B` are both `a_Aa_B`, hence

\[
2a_Aa_B+
\sum_{S\notin\{A,B\}}a_Sa_{S\triangle T}=0.
\]

Taking absolute values and applying Cauchy--Schwarz to the remainder,

\[
2|a_Aa_B|
\le
\sqrt{\sum_{S\notin\{A,B\}}a_S^2}
\sqrt{\sum_{S\notin\{A,B\}}a_{S\triangle T}^2}.
\]

Translation by `T` swaps `A` and `B`, so both residual sums equal `1-p(A)-p(B)`. Therefore

\[
2\sqrt{p(A)p(B)}\le1-p(A)-p(B),
\]

which is equivalent to (3.2). QED.

The exact one-point Boolean family below saturates (3.2) between the empty atom and every nonempty atom. So this is a genuine Boolean boundary constraint, not an artifact of a loose inequality.

However, (3.2) by itself cannot prove FEI: arbitrary non-Boolean high-entropy product laws with sufficiently spread small atoms can satisfy the pairwise envelope. The route must use the **simultaneous signed cancellation identities (3.1)**, not merely their two-atom corollary.

---

## 4. Pairwise mutual information is a rigorous payment bank — and it is not enough

For any ordinary tree `G` on the coordinate set, orient it away from a root. Conditioning reduces entropy, so

\[
H(X)
\le
H(X_{\rm root})+
\sum_{i\ne\rm root}H(X_i\mid X_{\rm parent(i)}).
\]

Rearrangement gives the standard but exact lower bound

\[
\boxed{
\operatorname{TC}(X)
\ge
\sum_{(i,j)\in E(G)} I(X_i;X_j).
}
\tag{4.1}
\]

The strongest lower bound of this form is the maximum-spanning-tree weight in the pairwise mutual-information graph. This is an attractive FEI mechanism: if rare spectral bits are forced to be pairwise correlated, perhaps (4.1) pays (2.3).

The next theorem kills that idea for every fixed constant.

### The exact admissible Boolean test family

Let `f_n` be `+1` at every cube point except one, where it is `-1`. Set

\[
q=2^{1-n}.
\]

Its Fourier spectrum is exact:

\[
p(\varnothing)=(1-q)^2,
\qquad
p(S)=q^2\quad(S\ne\varnothing).
\tag{4.2}
\]

Hence every membership marginal equals

\[
\Pr(i\in X)=q,
\tag{4.3}
\]

and every pair satisfies

\[
\Pr(X_i=X_j=1)=q/2.
\tag{4.4}
\]

For two coordinates the joint law is therefore

\[
P_{11}=P_{10}=P_{01}=q/2,
\qquad
P_{00}=1-3q/2.
\tag{4.5}
\]

Let `m(q)` denote its pairwise mutual information. Every coordinate pair has the same `m(q)`, so the maximum-spanning-tree bank is exactly

\[
P_{\rm tree}(n)=(n-1)m(q).
\tag{4.6}
\]

The positive total-correlation payment requested by (2.2) at a fixed constant `C` is, for all sufficiently large `n`,

\[
R_C(n)=n\bigl(h_2(q)-Cq\bigr).
\tag{4.7}
\]

### Theorem 4.1 — universal pairwise-tree `1/2` barrier

For every fixed finite `C`, along the one-point Boolean family,

\[
\boxed{
\frac{P_{\rm tree}(n)}{R_C(n)}\longrightarrow\frac12.
}
\tag{4.8}
\]

Therefore no proof of (2.2) that certifies total correlation solely through an ordinary spanning tree of pairwise spectral-bit mutual informations can establish FEI with any fixed universal constant.

### Proof

As `q -> 0`,

\[
\frac{h_2(q)}q
=
\log_2\frac1q+\log_2 e+O(q).
\tag{4.9}
\]

From (4.5), direct expansion gives

\[
\begin{aligned}
\frac{m(q)}q
&=
\frac12\log_2\frac1q
-\frac32+rac{1}{2\ln2}
+O(q).
\end{aligned}
\tag{4.10}
\]

Here `q=2^{1-n}`, so `log2(1/q)=n-1`. Substituting (4.9)--(4.10) into (4.6)--(4.7),

\[
P_{\rm tree}(n)
=\frac12 qn^2+O(qn),
\]

whereas for every fixed `C`,

\[
R_C(n)=qn^2+O_C(qn).
\]

Their ratio tends to `1/2`. QED.

This is a refutation of the **proof mechanism**, not of FEI. Indeed the exact one-point ratio satisfies

\[
\frac{H(f_n)}{I(f_n)}\to4.
\]

So the family comfortably satisfies every proposed FEI constant above `4` while still defeating the pairwise payment plan.

### Current-scale numbers

At `C=C_seed`, the targeted script reports:

| `n` | `q` | `H/I` | required TC payment | tree pair-MI bank | bank / required |
|---:|---:|---:|---:|---:|---:|
| 7 | 0.015625 | 3.8043571 | 0.09947865 | 0.20852320 | 2.09616 |
| 8 | 0.0078125 | 3.8427826 | 0.11969994 | 0.14890185 | 1.24396 |
| 10 | 0.001953125 | 3.8841784 | 0.07655155 | 0.06542053 | **0.85459** |
| 16 | 0.0000305176 | 3.9302714 | 0.00484415 | 0.00307679 | **0.63516** |
| 32 | 4.6566e-10 | 3.9651684 | 3.8625e-7 | 2.1251e-7 | **0.55019** |

At `n=10` the pairwise-tree statement is already decisively false while the Boolean FEI inequality at this scale remains true. The same exact family also gives

\[
\sqrt{p(\varnothing)}+\sqrt{p(S)}=(1-q)+q=1
\]

for every nonempty `S`, so Lemma 3.1 is stress-tested on its equality boundary.

The calculation is in `artifacts/onepoint_pairwise_obstruction.py` with archived output `artifacts/onepoint_pairwise_obstruction.out`. It is a targeted family calculation, not a repeat of the known exhaustive FEI sweep.

---

## 5. PROVED: a block tree recovers total correlation exactly

The pairwise loss has an exact repair at the level of information bookkeeping.

Take any rooted binary partition tree whose leaves are the singleton coordinates. For an internal node `B` with disjoint children `L,R` and `B=L union R`, write

\[
I_B:=I(X_L;X_R).
\]

### Theorem 5.1 — multiscale dependence identity

For every joint law, hence in particular for every Boolean spectral law,

\[
\boxed{
\operatorname{TC}(X)=
\sum_{B\text{ internal}} I(X_{L_B};X_{R_B}).
}
\tag{5.1}
\]

### Proof

For each split `B=L union R`,

\[
\begin{aligned}
\operatorname{TC}(X_B)
&=\sum_{i\in B}H(X_i)-H(X_B)\\
&=\operatorname{TC}(X_L)+\operatorname{TC}(X_R)
 +H(X_L)+H(X_R)-H(X_L,X_R)\\
&=\operatorname{TC}(X_L)+\operatorname{TC}(X_R)+I(X_L;X_R).
\end{aligned}
\]

Recursing to singleton leaves, whose total correlation is zero, proves (5.1). QED.

This changes the route substantially. The target is no longer to show every rare bit has a strong partner. It is to show that across a **laminar sequence of coordinate cuts**, Booleanity forces enough block dependence to pay the rare-marginal deficit. Exact factorization across a cut is harmless because then the spectral law splits there and FEI can be attacked recursively on the factors; the hard case should be quantitative near-factorization.

### One-point stress test of the multiscale repair

For the one-point family, the `k`-coordinate marginal has the exact form

\[
P(X_{[k]}=0)=1-v_k,
\qquad
P(X_{[k]}=y)=2^{2-n-k}\quad(y\ne0),
\]

where

\[
v_k=2^{2-n}(1-2^{-k}).
\]

Thus

\[
H_k=h_2(v_k)+v_k\log_2(2^k-1).
\tag{5.2}
\]

For a balanced split of a block of size `m`, the block mutual information is exactly

\[
2H_{m/2}-H_m.
\tag{5.3}
\]

At `n=32`, the balanced binary hierarchy decomposes total correlation as follows:

| block size | fraction of total correlation paid at that level | cumulative |
|---:|---:|---:|
| 2 | 0.258473 | 0.258473 |
| 4 | 0.297366 | 0.555839 |
| 8 | 0.238490 | 0.794330 |
| 16 | 0.136666 | 0.930995 |
| 32 | 0.069005 | 1.000000 |

So `74.15%` of the dependence is genuinely above the disjoint-pair scale in this exact Boolean boundary family. The separate script `artifacts/onepoint_multiscale.py` verifies the telescoping numerically from the exact dyadic formulas; its output is archived beside it.

---

## 6. What is proved, refuted, and still open

### PROVED in this run

1. **Character-gauge FEI equivalence:** universal FEI(C) is exactly equivalent to
   \[
   H(X)\le C\sum_i\min(\Pr(i\in X),1-\Pr(i\in X)).
   \]
2. **Total-correlation reformulation:** after the minimizing twist, FEI(C) is exactly (2.2); the positive-payment version (2.3) isolates only rare marginals.
3. **Boolean two-atom cancellation:** every pair of distinct spectral atoms satisfies `sqrt(p_A)+sqrt(p_B)<=1`.
4. **Multiscale identity:** total correlation is exactly the sum of block mutual informations over any binary coordinate partition tree.
5. **Pairwise-tree barrier:** on the exact admissible one-point Boolean family, the strongest spanning-tree pairwise-MI bank pays asymptotically only one half of the correlation demanded by the sharp-scale formulation, and this `1/2` limit holds for **every fixed `C`**.

### REFUTED in this run

> **REFUTED-LEMMA / dead subroute:** “The rare-marginal FEI deficit can always be paid by a spanning tree of pairwise spectral-bit mutual informations.”

It fails already on exact one-point Boolean functions (`n=10` at the current diagnostic scale), and asymptotically misses a factor two for every fixed proposed FEI constant.

### OPEN

No dimension-independent FEI constant is proved here. The new hard statement is quantitative, not merely informational:

> Find a binary/laminar coordinate decomposition, preferably chosen from the Boolean Fourier geometry, for which the block mutual informations in (5.1) can be lower-bounded by the rare-marginal deficits in (2.3), with exact factorization treated recursively rather than charged.

A particularly concrete next lemma is a **spectral factorization dichotomy** across a cut `A|B`:

- either `I(X_A;X_B)` pays a definite fraction of the unresolved rare-marginal deficit carried on both sides; or
- the signed Fourier coefficient matrix is quantitatively close to a rank-one/product form compatible with Booleanity, allowing a recursive product decomposition with controlled error.

The simultaneous signed cancellation equations (3.1), rather than pairwise atom bounds alone, are the proposed source of that dichotomy.

---

## 7. Next attack

Do **not** add another pairwise checker. The pairwise mechanism is mathematically dead.

Next run should attack the first nontrivial block cut directly. Write the Fourier coefficient tensor across `A|B` as a signed matrix `M=(a_{UV})`; compare spectral mutual information `I(X_A;X_B)` to distance of `M` from a rank-one magnitude tensor, while imposing all Boolean convolution identities

\[
\sum_{U,V}a_{UV}a_{U\triangle U_0,V\triangle V_0}=0
\quad ((U_0,V_0)\ne(0,0)).
\]

The target is a quantitative theorem of the form “small block MI + Boolean convolution => near Boolean product factorization,” with an error term summable down a binary partition tree. A true version would let exact/near products recurse while charging genuinely interacting cuts, matching the multiscale structure that the one-point boundary family demonstrably requires.

**Full FEI remains OPEN / NOT PROVED.**

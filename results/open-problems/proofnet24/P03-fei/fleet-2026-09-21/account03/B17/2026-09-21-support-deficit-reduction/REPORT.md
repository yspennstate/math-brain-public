# B17 FEI new proof mechanism — minority-set uncertainty/isoperimetry deficit reduction

**Date:** 2026-09-21  
**Status of full FEI:** **OPEN / NOT PROVED**  
**Run status:** `WITHOUT_VERIFIED_BRAIN` — no authenticated mathematical-brain retrieval/context was used in this derivation.  
**Role:** account03/B17, FEI new proof mechanisms.  
**Fresh mathematical source consumed before this attempt:** `master` at `8ee854972993b0170b0fefc2439ac5bfbb095317`.  
**Required live FEI sources read in order:** `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` in `continuations/2026-09-21-readonce-certificate/`.

## 0. What changed

I did not audit the read-once certificate, repeat the `n<=5` Boolean sweep, or continue the previous B17 signed-diagonal checker. I first attacked **APPROACHES route 1** (sequential compression of the spectral sample) with a coordinatewise Shapley charge. An exact seven-variable Boolean function refutes the sharp local charge: one coordinate has Shapley entropy charge / influence `7.1127919665... > beta(1/2)=6.4547837...` even though the global `H/I` is only `1.7205...`.

After that refutation I changed method and opened **Route 15: minority-set support-deficit reduction**. The new mechanism turns full FEI into a stronger stability inequality comparing the *excess* in two classical cube inequalities for set indicators:

1. finite Fourier entropic uncertainty; and
2. edge isoperimetry / log-Sobolev.

The reduction to FEI and its exact tensorization are proved below. The proposed universal set inequality itself remains **OPEN**. Exact stress tests find no counterexample through all `65,535` nonempty subsets of the four-cube. A self-similar one-third-density staircase gives the exact limiting ratio

\[
\frac{8}{3(2-\log_2 3)}=6.425122239075223\ldots,
\]

which is strikingly close to, but below, Hod's `6.4547837...`. A tempting proof by monotone coordinate compression is explicitly **REFUTED** in both directions by four-variable sets.

This is a new-to-this-run mechanism, not a claim of publication novelty.

---

## 1. The new set functional

Let `A` be a nonempty subset of the uniform `n`-cube and put

\[
g=\mathbf 1_A,\qquad \delta=\mathbb E g=|A|/2^n.
\]

By Parseval, `sum_S ghat(S)^2 = delta`. Define the normalized Fourier-energy law

\[
\mu_A(S)=\frac{\widehat g(S)^2}{\delta}.
\]

Write

\[
H_A=H(\mu_A),\qquad
J_A=\mathbb E_{S\sim\mu_A}|S|,
\qquad L_A=\log_2\frac1\delta.
\]

Define two deficits

\[
U(A):=H_A-L_A,\qquad
E(A):=J_A-\frac{L_A}{2}. \tag{1}
\]

The finite Fourier entropic uncertainty inequality gives `U(A)>=0`. The cube edge-isoperimetric/log-Sobolev inequality gives `E(A)>=0`: indeed

\[
\sum_S |S|\widehat g(S)^2
  =\frac14\sum_i \Pr[g(x)\ne g(x^{(i)})],
\]

and edge isoperimetry gives

\[
\sum_i \Pr[g(x)\ne g(x^{(i)})]
\ge 2\delta\log_2(1/\delta).
\]

For a codimension-`k` subcube, `delta=2^{-k}` and `mu_A` is uniform on the `2^k` characters of the fixed-coordinate set. Hence

\[
H_A=k=L_A,\qquad J_A=k/2=L_A/2,
\]

so **both deficits vanish exactly**.

### Route-15 target

For a dimension-independent constant `C`, prove

\[
\boxed{\quad U(A)\le C E(A)\quad\text{for every nonempty cube set }A.\quad} \tag{SD_C}
\]

This is stronger than ordinary FEI, but the next theorem shows that it implies FEI with the **same** constant as soon as `C>=4`.

---

## 2. PROVED: exact minority-set transfer to FEI

### Theorem 2.1

Fix `C>=4`. If `(SD_C)` holds for every nonempty cube set, then every Boolean

\[
f:\{-1,1\}^n\to\{-1,1\}
\]

satisfies

\[
H(f)\le C I(f).
\]

More quantitatively, after replacing `f` by `-f` if necessary, let

\[
A=\{x:f(x)=1\},\qquad 0<\delta\le1/2.
\]

Then

\[
\boxed{
H(f)-CI(f)
\le 4\delta\,[U(A)-CE(A)].
} \tag{2}
\]

Thus any FEI counterexample at a constant `C>=4` produces an explicit set violating `(SD_C)`.

### Proof

Put `g=1_A=(1+f)/2`. For every nonempty Fourier set `S`,

\[
\widehat f(S)=2\widehat g(S),
\]

while

\[
\widehat f(\varnothing)=2\delta-1.
\]

Therefore

\[
I(f)=4\sum_{S\ne\varnothing}|S|\widehat g(S)^2
    =4\delta J_A. \tag{3}
\]

Let

\[
V=4\delta(1-\delta).
\]

The spectral law of `g` has mass `delta` at the empty set, because

\[
\mu_A(\varnothing)=\widehat g(\varnothing)^2/\delta=\delta.
\]

Conditional on being nonempty, the spectral laws of `g` and `f` are identical after normalization. Hence

\[
H_A=h_2(\delta)+(1-\delta)H_{\rm cond},
\]

and

\[
H(f)=h_2(V)+V H_{\rm cond}.
\]

Eliminating `H_cond`,

\[
\boxed{
H(f)=h_2(V)+4\delta\,[H_A-h_2(\delta)].
} \tag{4}
\]

Now substitute

\[
H_A=U(A)+L_A,
\qquad
J_A=E(A)+L_A/2
\]

into (3)-(4). With `L=L_A`,

\[
H(f)-CI(f)
=4\delta[U(A)-CE(A)]+s_C(\delta), \tag{5}
\]

where

\[
s_C(\delta)
=h_2(4\delta(1-\delta))
+4\delta\left[(1-C/2)L-h_2(\delta)\right]. \tag{6}
\]

It remains to show `s_C(delta)<=0` for `0<delta<=1/2` and `C>=4`.

Since `1-C/2<=-1`, it suffices that

\[
\frac{h_2(4\delta(1-\delta))}{4\delta}
\le L+h_2(\delta). \tag{7}
\]

Use the elementary binary-entropy bound

\[
h_2(q)\le q\log_2(e/q).
\]

For `q=4delta(1-delta)`, the right side of (7) minus this upper bound is

\[
\begin{aligned}
&L+h_2(\delta)
-(1-\delta)\log_2\frac{e}{4\delta(1-\delta)}\\
&=2\delta L+(1-\delta)(2-\log_2 e)\ge0.
\end{aligned}
\]

Thus (7), then `s_C(delta)<=0`, then (2) follow. QED.

### Meaning

This does **not** prove FEI. It changes the universal obstruction. Instead of paying raw spectral entropy by raw influence, it asks for a *stability inequality*: pay the Fourier-uncertainty excess above its support floor by the edge-isoperimetric excess above its support floor.

Subcubes are removed for free because they simultaneously saturate both baselines.

---

## 3. PROVED: exact tensorization of the new obstruction

### Theorem 3.1

For sets `A` and `B` on disjoint coordinate blocks,

\[
U(A\times B)=U(A)+U(B),\qquad
E(A\times B)=E(A)+E(B). \tag{8}
\]

### Proof

The density multiplies,

\[
\delta_{A\times B}=\delta_A\delta_B,
\]

so `L` adds. Fourier coefficients of indicators multiply on disjoint blocks, hence the normalized Fourier-energy law is the product law

\[
\mu_{A\times B}=\mu_A\otimes\mu_B.
\]

Therefore Shannon entropy and expected Fourier degree both add. Subtracting the additive baseline `L` and `L/2` gives (8). QED.

### Consequence

When both denominators are positive, the ratio

\[
R(A)=\frac{U(A)}{E(A)}
\]

of a Cartesian product is the `E`-weighted average of the factor ratios. Thus pure product constructions cannot create a new larger ratio from smaller ones. The hard set, if this route is correct, must contain an indecomposable interaction rather than merely many independent copies.

This is exactly the kind of structural behavior the raw `H/I` ratio lacks near sparse support baselines.

---

## 4. Exact stress test: all set indicators through dimension four

The deterministic verifier enumerated every nonempty set indicator through `n=4`:

- `n=1`: `3` nonempty sets;
- `n=2`: `15`;
- `n=3`: `255`;
- `n=4`: `65,535`.

At

\[
C=6.4547837,
\]

the maximum observed value of `U-CE` was `0`, attained by equality/baseline cases. No positive violation occurred.

The largest finite positive ratios over **all** densities were

\[
6.298802786555887\quad(n=2),
\]
\[
6.387842267701161\quad(n=3),
\]
\[
6.394774454871632\quad(n=4).
\]

If density is restricted to at most `1/2` (the only range needed in Theorem 2.1), the largest ratios found were

\[
6.298802786555889\quad(n=3),
\qquad
6.3878422677011635\quad(n=4).
\]

These are finite checks only. They do not establish `(SD_C)`.

As a wider stress test of the algebraic shape, the same code exhausts all nonzero ternary partial functions `h in {0,+-1}` through `n=3`: `8`, `80`, and `6,560` functions. Again no positive `U-6.4547837 E` was found. The strongest ternary ratios were the same `6.2988027865...` and `6.3878422677...`. This does not imply that the stronger signed-partial extension is universally true.

---

## 5. PROVED limiting family: the one-third dyadic staircase

The small-set maximizers immediately suggested binary initial segments near density `1/3`. For the initial segments nearest `2^n/3`, the measured ratios are

| `n` | support size | density | `U/E` |
|---:|---:|---:|---:|
|3|3|0.375000|6.2988027866|
|4|5|0.312500|6.3878422677|
|5|11|0.343750|6.3947744549|
|6|21|0.328125|6.4160728551|
|7|43|0.3359375|6.4176130062|
|8|85|0.33203125|6.4228763744|
|9|171|0.333984|6.4232498016|
|10|341|0.333008|6.4245617965|
|11|683|0.333496|6.4246544343|
|12|1365|0.333252|6.4249821923|

The limit can be computed exactly by the two-state recursion for binary expansions of `1/3=0.010101..._2` and `2/3=0.101010..._2`.

Let `B` denote the limiting one-third state and `A` the complementary two-thirds staircase state. The first-bit decompositions are

- `A`: one half-cube is full and the other contains `B`;
- `B`: one half-cube contains `A` and the other is empty.

For `A`, the normalized spectral law has an empty atom of mass `2/3`, a first-bit atom of mass `1/6`, and for every nonempty spectral atom of `B` two descendants, each with one eighth of its `B` mass. For `B`, the empty and first-bit atoms each have mass `1/3`, and every nonempty atom of `A` has two descendants, each with half its `A` mass.

The expected degrees therefore satisfy

\[
J_A=\frac14J_B+\frac14,
\qquad
J_B=J_A+\frac12,
\]

so

\[
J_A=\frac12,\qquad J_B=1. \tag{9}
\]

Writing `phi(t)=-t log2 t`, the entropy recurrences are

\[
H_A=\phi(2/3)+\phi(1/6)
+\frac14\left(H_B-\phi(1/3)\right)+\frac12,
\]

\[
H_B=2\phi(1/3)+H_A-\phi(2/3)+\frac13.
\]

Solving,

\[
H_A=\log_2 3+\frac13,
\qquad
H_B=\log_2 3+\frac43. \tag{10}
\]

For the minority-density state `B`, `L_B=log2 3`, hence

\[
U(B)=\frac43,
\qquad
E(B)=1-\frac12\log_2 3.
\]

Therefore

\[
\boxed{
R(B)=\frac{8}{3(2-\log_2 3)}
=6.425122239075223\ldots
} \tag{11}
\]

This gives a rigorous lower bound on the best possible constant in the stronger support-deficit inequality, via its finite dyadic approximants. It remains below Hod's Boolean lower bound `6.4547837...`, as it must if `(SD_C)` is to imply FEI with the same `C`.

The numerical proximity is useful: the new inequality is not a wildly loose strengthening; it already lives on essentially the correct constant scale.

---

## 6. REFUTED-LEMMA: ordinary coordinate compression is not monotone for `U/E`

A natural next thought was to combine Theorem 2.1 with edge-isoperimetric compression: perhaps compress every set to a lexicographic initial segment while monotonically increasing `R=U/E`. This is false.

Use integer labels `0,...,15` for the four-cube and compress a fibre toward bit `0` in the indicated zero-indexed coordinate.

### Compression can decrease the ratio

Take

\[
A=\{3,4,7,8\},\qquad \delta=1/4.
\]

Its exact computed metrics are

\[
H_A=3,\quad J_A=7/4,\quad L=2,\quad U=1,\quad E=3/4,\quad R=4/3.
\]

Compress coordinate `3`. The set becomes

\[
A'=\{0,3,4,7\}.
\]

Now

\[
H_{A'}=2,\quad J_{A'}=3/2,\quad U(A')=0,\quad E(A')=1/2,\quad R(A')=0.
\]

So a single compression can **decrease** the target ratio.

### Compression can increase the ratio sharply

Take

\[
B=\{0,3,5,6,9,10\},\qquad\delta=3/8.
\]

Here

\[
R(B)=0.6131471927654586\ldots
\]

Compress coordinate `0`; the result is

\[
B'=\{0,2,4,6,8,10\}
\]

with

\[
R(B')=6.298802786555889\ldots.
\]

Therefore neither monotonic direction is available.

**REFUTED-LEMMA:** “one-coordinate edge compression monotonically increases (or monotonically decreases) the support-deficit ratio.”

The route therefore needs a genuine stability/Bellman argument, not a pointwise shifting proof.

---

## 7. First Approach-1 attack and exact Boolean refutation

Before opening Route 15, I tried to localize the spectral-sample chain rule coordinate by coordinate.

For the spectral membership vector `B=(B_1,...,B_n)`, define the Shapley entropy allocation

\[
\Phi_i
=\sum_{T\subseteq[n]\setminus\{i\}}
\frac{|T|!(n-|T|-1)!}{n!}
H(B_i\mid B_T). \tag{12}
\]

By the Shapley/chain-rule identity,

\[
\sum_i\Phi_i=H(B)=H(f).
\]

Thus the sharp local lemma

\[
\Phi_i\le \beta(1/2)\,\operatorname{Inf}_i(f)
\quad\text{for every }i \tag{13}
\]

would immediately prove sharp FEI.

It is false.

Take the exact seven-variable Boolean function equal to `-1` on the following vertices and `+1` elsewhere:

`[2,3,6,7,8,11,12,15,16,17,19,20,21,23,32,36,40,41,44,45,48,49,50,51,52,53,55,57,58,61,62,64,66,67,68,70,71,82,86,91,95,96,98,100,102,105,106,107,109,110,111,113,117,121,123,125,127]`.

Its global values are

\[
H(f)=5.188394502765988,
\qquad
I(f)=3.015625,
\qquad
H/I=1.720503876564887.
\]

For coordinate `i=2` (zero-indexed),

\[
\operatorname{Inf}_2(f)=0.015625,
\]

while

\[
\Phi_2=0.11113737447764174,
\]

so

\[
\boxed{
\Phi_2/\operatorname{Inf}_2
=7.1127919665690715
>6.4547837.
} \tag{14}
\]

The complete influence vector is

`[0.484375, 0.484375, 0.015625, 0.546875, 0.515625, 0.453125, 0.515625]`,

and the Shapley entropy vector is

`[0.8718103139568648, 0.8694563627596469, 0.11113737447764174, 0.8571413872923658, 0.8258942495100731, 0.8159379492582631, 0.8370168655111327]`.

Their sum equals `H(f)` to floating arithmetic precision.

**REFUTED-LEMMA:** the sharp coordinatewise Shapley charge (13). This does not refute a larger universal Shapley constant, and it does not refute FEI. It does show that simply symmetrizing the chain-rule order does not eliminate rare-coordinate overcharging at the sharp constant.

This refutation is why the run changed category from “charge each coordinate” to “subtract the support/isoperimetric baselines first.”

---

## 8. Literature boundary check

A bounded current search found the known/newer FEI upper-bound line including Xiao Han's Fourier-entropy-influence bound and the 2025 Li--Han information-theoretic strengthening. I did not find, in that bounded search, a paper stated in the exact form of `(SD_C)` or the defect transfer (2). This is **not** an exhaustive literature review and I make **no novelty or priority claim**.

The route deliberately uses standard ingredients (finite Fourier entropic uncertainty, edge isoperimetry/log-Sobolev, indicator/Boolean Fourier identities) in a different deficit comparison. Any publication claim would require a dedicated source search and independent proof review.

---

## 9. Claim ledger

### PROVED in this run

1. **Minority-set defect transfer:** for every Boolean `f`, every `C>=4`, and its minority set `A`,
   \[
   H(f)-CI(f)\le4\delta[U(A)-CE(A)].
   \]
2. Therefore `(SD_C)` for every set implies full FEI with the same `C>=4`.
3. **Exact tensorization:** `U` and `E` add under Cartesian products of sets.
4. Subcubes satisfy `U=E=0` exactly.
5. The self-similar one-third dyadic staircase has limiting support-deficit ratio
   \[
   8/[3(2-\log_2 3)]=6.425122239075223\ldots.
   \]
6. Two explicit four-cube examples show one-coordinate compression can move `U/E` in either direction.

### REFUTED-LEMMA

1. Sharp coordinatewise Shapley entropy payment `Phi_i <= beta Inf_i` for every coordinate.
2. Monotonicity of `U/E` under ordinary one-coordinate compression, in either universal direction.

### CONDITIONAL / OPEN

1. **Support-deficit inequality `(SD_C)` is OPEN.** No universal proof is given.
2. Full FEI remains **OPEN / NOT PROVED**.
3. Finite enumeration and the staircase computation are not universal certificates.
4. No novelty or publication-priority claim is made.

---

## 10. Next attack

Do **not** repeat the `n<=4` set enumeration or the Shapley counterexample search.

The next run on Route 15 should attack a genuine **stability inequality** rather than compression monotonicity. The cleanest target is:

> If a set has small normalized edge-isoperimetric excess `E(A)`, prove directly that its Fourier uncertainty excess `U(A)` is at most `C E(A)` by decomposing it near a subcube; when `E(A)` is not small, combine a coarse Fourier-entropy bound with the available excess.

Two concrete subproblems:

1. derive a quantitative local expansion of `U` and `E` for a subcube with an arbitrary small symmetric-difference perturbation, keeping the exact first nonzero terms; and
2. compute the support-deficit ratio for the minority sets of finite Hod/read-once extremizers. Since Theorem 2.1 would otherwise contradict Hod's lower bound, those sets must eventually force the support-deficit constant up to at least the Boolean lower-bound scale. Their geometry should identify the correct non-compression stability mechanism.

A successful theorem here would be a genuinely new route to **full** FEI, not merely another structured-class bound.

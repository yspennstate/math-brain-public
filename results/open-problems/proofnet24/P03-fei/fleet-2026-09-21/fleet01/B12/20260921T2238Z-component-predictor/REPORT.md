# B12 FEI creative attempt — a Kraft component predictor and a Boolean bipartition interaction lemma

**Status:** **PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Route:** APPROACH 1, spectral-sample compression / sequential prediction, with a deliberate mechanism change to a Boolean ANOVA interaction lemma and a component decoder.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub mathematical artifacts were read, but no native mathematical-brain retrieval/receiver context was used.  
**Claim level:** analytic partial theorems for the closed fine Palm/physical robust sector plus one universal Boolean structural lemma. No novelty or publication-priority claim.

## 0. Fresh inputs and the mechanism change

This run read the current owner packet and the required FEI packet, then substantively consumed the completed other-account theorem

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260921T201418Z-palm-trigger-cluster/REPORT.md`

(report Git blob `4643e5dd27cc48a508820a30413e24b9c4717fac`). Its exact ingredients used below are:

1. for a Palm-robust row `i`,
   \[
   \nu_i=\operatorname{Law}(S\setminus\{i\}\mid i\in S),\qquad
   \operatorname{TV}(\nu_i,U_{F_i})\le\epsilon_i;
   \]
2. reciprocal robust rows have one exact common trigger signature, so a reciprocal component `C` has
   \[
   F_i=T_C\setminus\{i\};
   \]
3. in the physical near-subcube branch,
   \[
   s_i=2^{-|F_i|},\qquad |s_i-p_i|\le\rho p_i,\qquad \rho\le1/16,
   \]
   with `p_i=Pr(i in S)`;
4. a nonreciprocal trigger is a genuine scale escape. The present theorem first closes the **no-escape / closed-component branch** `T_C=C`, rather than trying to pay another copy of the already-known first-moment escape budget.

I also use the exact Palm insertion identity from fleet03/B12 and the preceding fleet01/B12 factorial contraction. In the notation here,

\[
H(S)\le H(K)+I H(\rho)-D_{\rm seq}
+\left(2\log_2 e+\frac1{16}\right)I,
\tag{0.1}
\]

where `K=|S|`, `rho` is the reciprocal-component macro-label distribution after coefficient-one factorial contraction, and

\[
D_{\rm seq}=I\,I_2(L;P)
\tag{0.2}
\]

is the exact mutual-information saving of the insertion label `L` against its predecessor prefix `P`.

The previous run stopped at

\[
I H(\rho)-D_{\rm seq}=O(I).
\tag{0.3}
\]

Rather than derive a third variant of the same companion-flow first-moment inequality, this run changes mechanism: construct an actual component predictor from `P`, prove a Kraft inequality from the physical/Palm geometry, and separately derive a universal Boolean interaction inequality which rules out independent pure spectral blocks without mixed mass.

---

## 1. A universal Boolean bipartition interaction lemma

Let `U,V` be a nontrivial partition of the physical coordinates. Write the orthogonal Fourier/ANOVA decomposition

\[
f=a+g(x_U)+h(x_V)+r(x_U,x_V),
\tag{1.1}
\]

where `a=E f`, `g` contains the nonempty Fourier characters supported wholly in `U`, `h` those supported wholly in `V`, and `r` all characters meeting both sides. Put

\[
A=\|g\|_2^2,\qquad B=\|h\|_2^2,\qquad \Delta=\|r\|_2^2.
\tag{1.2}
\]

Equivalently, for the spectral sample `S`,

\[
A=\Pr(\varnothing\ne S\subseteq U),\quad
B=\Pr(\varnothing\ne S\subseteq V),\quad
\Delta=\Pr(S\cap U\ne\varnothing,\ S\cap V\ne\varnothing).
\tag{1.3}
\]

### Theorem 1.1 — Boolean bipartition interaction

For every Boolean `f:{-1,1}^n->{-1,1}` and every coordinate bipartition,

\[
\boxed{A B\le4\Delta.}
\tag{1.4}
\]

### Proof

The functions `g(x_U)` and `h(x_V)` are independent and mean zero. Let

\[
h_0=a+g+h=f-r.
\]

Expanding and using independence/zero means,

\[
\mathbb E[(h_0^2-1)gh]=2\,\mathbb E g^2\,\mathbb E h^2=2AB.
\tag{1.5}
\]

Since `f^2=1`,

\[
h_0^2-1=(f-r)^2-1=-2fr+r^2.
\tag{1.6}
\]

Also `g=E[f|x_U]-a` and `h=E[f|x_V]-a`, so `|g|,|h|<=2`. Therefore

\[
\begin{aligned}
2AB
&\le 2\mathbb E|rgh|+\mathbb E[r^2|gh|]\\
&\le2\|r\|_2\|gh\|_2+4\|r\|_2^2\\
&=2\sqrt{\Delta}\sqrt{AB}+4\Delta.
\end{aligned}
\tag{1.7}
\]

If `Delta=0`, this gives `AB=0`. Otherwise put `t=sqrt(AB/Delta)`; then `t^2<=t+2`, hence `t<=2`, proving (1.4). QED.

The point is not the constant `4`. The structural statement is that a Boolean spectrum cannot carry nonzero **pure** mass on both sides of a physical bipartition while carrying zero mixed mass. This is false for a generic probability law on subsets and uses `f^2=1` essentially.

### Exact finite falsification check

`check_bipartition_interaction.py` uses integer Walsh transforms and exact rational comparisons. It checks every Boolean function modulo global sign through `n=4` and every nontrivial coordinate bipartition modulo swapping sides:

- function/bipartition checks: `229,768`;
- cases with `Delta=0`: `591`, all with `AB=0` exactly;
- maximum observed `AB/Delta`: `81/64 = 1.265625`;
- violations of `AB<=4 Delta`: `0`.

This is diagnostic evidence only; the proof above is all-dimensional.

---

## 2. Closed reciprocal Palm components and exact pure spectral mass

Now use the fleet04/B12 reciprocal-component theorem. Consider a collection of **closed** reciprocal components `C` such that every active coordinate belongs to exactly one component and

\[
T_C=C,\qquad F_i=C\setminus\{i\}\quad(i\in C).
\tag{2.1}
\]

Write

\[
m_C=|F_i|=|C|-1\ge1,\qquad
W_C=\sum_{i\in C}p_i,\qquad
\mathcal E_C=\sum_{i\in C}p_i\epsilon_i.
\tag{2.2}
\]

Assume the fine Palm scale

\[
\epsilon_i\le\frac1{16m_C}.
\tag{2.3}
\]

Define the **pure nonempty spectral mass** of `C`

\[
w_C:=\Pr(\varnothing\ne S\subseteq C).
\tag{2.4}
\]

Let

\[
a_m:=\mathbb E\frac1{1+\operatorname{Bin}(m,1/2)}
=\frac{2-2^{-m}}{m+1}.
\tag{2.5}
\]

### Lemma 2.1 — exact Palm representation of pure component mass

For every closed component,

\[
\boxed{
 w_C=
 \sum_{i\in C}p_i\,
 \mathbb E_{B\sim\nu_i}
 \frac{1_{\{B\subseteq C\setminus\{i\}\}}}{1+|B|}.
}
\tag{2.6}
\]

Hence

\[
\boxed{|w_C-a_{m_C}W_C|\le\mathcal E_C.}
\tag{2.7}
\]

### Proof

Expand the right side under the exact conditional law `nu_i`. A nonempty terminal spectral set `A` wholly contained in `C` contributes

\[
\sum_{i\in A}\frac{\Pr(S=A)}{|A|}=\Pr(S=A),
\]

while every spectral set meeting `C^c` contributes zero. This proves (2.6).

Under the ideal law `U_{C\setminus{i}}`, the indicator is one and the expectation is exactly `a_m`. The integrand lies in `[0,1]`; total variation changes its expectation by at most `epsilon_i`. Multiply by `p_i` and sum. QED.

The events `{empty != S subseteq C}` are disjoint across distinct components.

---

## 3. A Kraft inequality forced by fine Palm robustness plus the physical scale relation

Now add the exact physical near-subcube scale used in fleet04/B12:

\[
|2^{-m_C}-p_i|\le\frac1{16}p_i
\qquad(i\in C).
\tag{3.1}
\]

Thus

\[
p_i\ge\frac{16}{17}2^{-m_C},\qquad
W_C\ge\frac{16}{17}(m_C+1)2^{-m_C}.
\tag{3.2}
\]

From (2.3), `mathcal E_C<=W_C/(16m_C)`. Combining with (2.7),

\[
\begin{aligned}
w_C
&\ge W_C\left(a_{m_C}-\frac1{16m_C}\right)\\
&\ge \frac{16}{17}2^{-m_C}
\left(2-2^{-m_C}-\frac{m_C+1}{16m_C}\right).
\end{aligned}
\tag{3.3}
\]

For every integer `m>=1`,

\[
2-2^{-m}-\frac{m+1}{16m}\ge\frac{11}{8}.
\]

Therefore

\[
\boxed{w_C\ge\frac{22}{17}\,2^{-m_C}.}
\tag{3.4}
\]

Since the pure-component events are disjoint and their total probability is at most one,

\[
\boxed{
\sum_C2^{-m_C}\le\frac{17}{22}<1.
}
\tag{3.5}
\]

This is the missing Kraft statement. It is not a dimensional counting argument: it comes from actual spectral probability mass supplied by the Palm/physical hypotheses.

Define

\[
Z=\sum_C2^{-m_C},\qquad
r_C=\frac{2^{-m_C}}Z.
\tag{3.6}
\]

Then `r` is a probability distribution and, because `Z<=1`,

\[
\boxed{\log_2(1/r_C)\le m_C.}
\tag{3.7}
\]

So a component has a genuine Shannon code of length at most its trigger codimension.

---

## 4. PROVED: the Palm predecessor pays the entire macro-label entropy up to `25I/8`

Let `L` and `P` be the exact insertion label and predecessor prefix of the inherited Palm code. Let

\[
C_L=\text{the reciprocal component containing }L.
\]

Its marginal distribution is exactly

\[
\Pr(C_L=C)=\rho_C:=W_C/I.
\tag{4.1}
\]

From the exact insertion identity,

\[
D_{\rm seq}=I I_2(L;P).
\]

Data processing through `L -> C_L` gives

\[
\boxed{
I H(\rho)-D_{\rm seq}
\le I H(C_L\mid P).
}
\tag{4.2}
\]

This turns the old macro-label problem into an explicit prediction problem.

### Distribution of the prefix in the ideal component

Condition on `L=i in C`. The terminal remainder `B=S\setminus{i}` has law `nu_i`. Given `B`, uniformly order `B union {i}` and take `P` to be the elements preceding `i`. Thus `P` is obtained from `nu_i` by a fixed Markov kernel. Total variation therefore remains at most `epsilon_i` after passing to `P`.

Under the ideal law `U_{C\setminus{i}}`:

- `P=empty` with probability exactly `a_{m_C}` from (2.5);
- whenever `P` is nonempty, every coordinate in `P` lies in the true source component `C`.

Fix any deterministic choice `D(P)` of the component of one coordinate of a nonempty `P`. Under the true law,

\[
\Pr(P=\varnothing\mid L=i)\le a_{m_C}+\epsilon_i,
\tag{4.3}
\]

and

\[
\Pr(P\ne\varnothing,\ D(P)\ne C\mid L=i)\le\epsilon_i.
\tag{4.4}
\]

### A concrete log-loss predictor

Use the Kraft distribution `r` from (3.6). Predict `C_L` from `P` as follows.

- If `P=empty`, use `r`.
- If `P` is nonempty, use the mixture
  \[
  q(\cdot\mid P)=\frac12\delta_{D(P)}+\frac12 r.
  \tag{4.5}
  \]

If `D(P)=C`, the log loss is at most `1` bit. If `D(P) != C`, it is at most `1+m_C` bits by (3.7). On the empty prefix it is at most `m_C` bits. Therefore, conditioned on `L=i in C`, the expected log loss is at most

\[
1+m_Ca_{m_C}+2m_C\epsilon_i.
\tag{4.6}
\]

Averaging with the exact label weights `p_i/I` yields

\[
\begin{aligned}
I H(C_L\mid P)
&\le I+\sum_C W_C m_Ca_{m_C}
+2\sum_i p_i m_{C(i)}\epsilon_i\\
&\le I+2I+\frac18I.
\end{aligned}
\tag{4.7}
\]

Here `m a_m=m(2-2^{-m})/(m+1)<2`, and the fine scale gives `m epsilon_i<=1/16`.

Hence:

### Theorem 4.1 — closed-component macro-code theorem

Under (2.1), (2.3), and (3.1),

\[
\boxed{
I H(\rho)-D_{\rm seq}\le\frac{25}{8}I.
}
\tag{4.8}
\]

This **closes the exact macro-label implication left open in the previous B12 report for the closed fine physical/Palm sector.** The payment is a real sequential predictor, not a pairwise-KL sum, so the earlier parity-MUX redundancy obstruction is avoided.

---

## 5. Structured FEI consequence

The preceding fleet01/B12 coefficient-one factorial theorem gives

\[
H(S)\le H(K)+I H(\rho)-D_{\rm seq}
+\left(2\log_2e+\frac1{16}\right)I.
\tag{5.1}
\]

Using Theorem 4.1 and the inherited Boolean stop-bank estimate `H(K)<=5I`,

\[
\boxed{
H(S)
\le
\left(
5+\frac{25}{8}+2\log_2e+\frac1{16}
\right)I
<11.07289008178\,I.
}
\tag{5.2}
\]

Thus FEI is proved with an explicit dimension-free constant on the class where **all active derivative/Palm rows decompose into closed reciprocal components satisfying the fine Palm condition and the fleet04 physical `1/16` near-subcube scale relation**.

This is a structured-sector theorem only. It is not full FEI.

---

## 6. Boolean interaction controls how exact closed blocks can coexist

The universal Theorem 1.1 gives an independent rigidity statement that is useful beyond the decoder.

For one closed component `C`, put

\[
x_C:=\Pr(S\cap C\ne\varnothing,\ S\cap C^c\ne\varnothing).
\]

If `S` crosses the boundary of `C`, at least one `i in C` has a Palm remainder outside `C\setminus{i}`. Hence by a union bound,

\[
\boxed{x_C\le\mathcal E_C.}
\tag{6.1}
\]

Let `W_pure=sum_C w_C`. In the bipartition `C | C^c`, the pure `C^c` spectral mass is at least `W_pure-w_C`. Theorem 1.1 therefore yields

\[
\boxed{
w_C(W_{\rm pure}-w_C)\le4\mathcal E_C.}
\tag{6.2}
\]

Summing,

\[
\boxed{
W_{\rm pure}^2-\sum_Cw_C^2
\le4\sum_C\mathcal E_C.
}
\tag{6.3}
\]

If `w_* = max_C w_C` and `W_pure>0`,

\[
\boxed{
W_{\rm pure}-w_*
\le\frac{4\sum_C\mathcal E_C}{W_{\rm pure}}.
}
\tag{6.4}
\]

So exact Palm closure (`epsilon_i=0`) forces all nonempty pure spectral mass into one component. This is a Boolean obstruction to a product of many independent exact pure blocks.

### Exact-zero-defect corollary

If every active row lies in a closed component and `epsilon_i=0`, then no spectral set can cross components, so Theorem 1.1 forces exactly one active component. Exact Palm uniformity then makes every nonempty squared Fourier coefficient on that component equal.

If the component has `c=m+1>=2` coordinates and the common nonzero squared coefficient is `t`, Boolean Walsh granularity gives

\[
t\ge4^{1-c}.
\]

Writing `N=2^c-1` and `V=Nt`,

\[
H=h_2(V)+V\log_2N,\qquad I=c2^{c-1}t.
\]

The ratio is maximized at the smallest `t`, because `h_2(V)/V` is decreasing. At `t=4^{1-c}`, put `delta=2^{-c}`; then `V=4delta(1-delta)`. The standard bound

\[
h_2(V)\le V\log_2(e/V)
\]

and `4(1-delta)>=3>e` give `h_2(V)<cV`, while `log_2(2^c-1)<c`. Hence

\[
H<2cV<8c\delta=4I.
\tag{6.5}
\]

For `c=1` the nonconstant case is a character and has zero Fourier entropy. Therefore the exact closed Palm-uniform branch satisfies

\[
\boxed{H<4I.}
\tag{6.6}
\]

Again, this is a structured class, not the full conjecture.

---

## 7. What is now paid, and the exact remaining universal gap

The closed fine physical/Palm branch no longer has the previous `I H(rho)-D_seq` obstruction. It has an explicit predictor and the dimension-free bound (4.8).

The remaining universal obstruction has moved to **nonclosed or nonfine components**:

1. `T_C` may contain external triggers, so a nonempty predecessor can point to a different reciprocal component. Fleet04/B12 proves those transitions are genuine scale escapes; the preceding B12 addendum proves only the first-moment nonreuse budget
   \[
   \sum_C W_C\frac{e_C}{m_C}\le I/3.
   \]
   That does not yet pay the logarithmic source-component identity on every escape.
2. Rows outside the fine Palm/physical near-subcube regime still require the separate stability/refund branch.
3. The universal Boolean bipartition lemma (1.4) controls coexistence of pure blocks versus mixed spectral mass, but by itself does not bound the entropy of a very diffuse small mixed tail.

The next nonrepeating target is therefore precise: **extend the predictor of Section 4 through the scale-escape DAG.** A successful extension must code the source component on the event that the first predecessor is an external trigger, using the target-side companion capacity and factor-7 / codimension-drop structure, without replacing the known first-moment bound by an unjustified logarithmically weighted version.

A different fallback route, if that source-identity code fails, is to use Theorem 1.1 recursively on component unions to prove that a high-entropy external-trigger tail necessarily creates enough mixed Boolean interaction to activate the physical crossing/refund bank.

**Full FEI remains OPEN.**

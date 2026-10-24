TASK: B17 ACCOUNT: account02 RUN: 2026-09-21T11:11:25.712618Z — balanced block composition, singleton leakage, and low-influence selector stress test

# Status

**Full uniform-cube FEI: OPEN / NOT PROVED.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive-brain retrieval or receiver-context use occurred in this derivation.  
**Role:** FEI new proof mechanisms.  
**Fresh mathematical source used for the derivation:** `yspennstate/math-open-problems` master `0263d8eec0c8936e2c5d221f85132fe95d58f18a`, followed by a freshness check through `6bb4d5709d42e2e10584a36e13d70fc86a0c9745`.  
**Novelty:** no publication-priority claim. The composition and erasure-entropy ingredients individually have prior literature; the exact selector-composition identity and finite obstruction below are recorded as new-to-this-repository pending specialist literature review.

This run used three different creative moves from `FLEET_RULES.md`: **#2 attack the negation first**, **#18 say it in another language**, and **#25 count the same thing twice**. The named universal obstruction is the current low-influence erasure-selector target: at the Hod-scale coefficient `C=6.4547837`, current P03 work reduces the remaining restriction-induction problem to forcing some coordinate with
\[
B_i:=H(S_i\mid S_{-i})\le 3.5693936182\,p_i,\qquad p_i=\Pr[i\in S],
\]
whenever all relevant `p_i<tau`, with `tau approximately 0.1805539925`.

**Tracked quantity.** Before this run, the worst low-influence selector ratio under the balanced-block composition family below was unmeasured. After exact exhaustive search over all balanced four-bit inner Boolean functions modulo global sign with a fixed three-bit AND/one-point outer function, the maximum of the composite minimum coordinate ratio is
\[
3.1826744874572914,
\]
leaving a gap
\[
3.5693936182-3.1826744874572914
=0.3867191307427085
\]
to the current Hod-scale selector threshold.

## 1. Why composition is relevant but the naive closure lemma is false

The standard FEI composition theorem for disjoint variable blocks (O'Donnell--Tan, arXiv:1304.1347) controls the ordinary entropy/influence ratio under composition. That does **not** automatically control the current local erasure-selector quantity `B_i/p_i`, which is what the newest restriction reduction needs.

A natural stronger conjecture to attack first is:

> **False max-parent selector closure.** For a balanced disjoint-block Boolean composition
> \[
> h=F(g_1,\ldots,g_m),
> \]
> the best composite coordinate erasure ratio is at most the worse parent selector ratio.

The exact Boolean example in section 4 refutes this. The failure is useful because it identifies one precise extra term: a Fourier singleton atom of the inner block.

## 2. Exact spectral generative law for balanced block composition

Let
\[
F:\{-1,1\}^m\to\{-1,1\}
\]
be Boolean. For each `j`, let
\[
g_j:\{-1,1\}^{n_j}\to\{-1,1\}
\]
be Boolean on mutually disjoint physical blocks and assume `E g_j=0`.

Let `A` be the outer spectral sample:
\[
\Pr[A=T]=\widehat F(T)^2.
\]
For each active outer block `j in A`, independently draw an inner spectral sample
\[
Y_j\sim \widehat g_j^2.
\]
Because each `g_j` is balanced, `\widehat g_j(\varnothing)=0`, so `Y_j` is nonempty almost surely. The spectral sample `X` of
\[
h(x)=F(g_1(x^{(1)}),\ldots,g_m(x^{(m)}))
\]
is exactly
\[
X=\bigcup_{j\in A}Y_j.
\]
This is the usual disjoint-block Fourier composition law, written as a probability kernel.

Fix an outer block `j` and a physical coordinate `u` in that block. Put
\[
a=\Pr[j\in A]=\operatorname{Inf}_j(F),\qquad
q=\Pr[u\in Y_j]=\operatorname{Inf}_u(g_j),
\]
and
\[
r=\Pr[Y_j=\{u\}]=\widehat g_j(\{u\})^2.
\]
Then immediately
\[
\boxed{\operatorname{Inf}_{j,u}(h)=a q.}
\tag{1}
\]

The nontrivial question is how the erasure entropy
\[
B_{j,u}(h)=H(X_{j,u}\mid X_{-(j,u)})
\]
transforms.

## 3. PROVED: exact erasure-selector composition identity

For each realization `R` of the outer sample away from block `j`, define
\[
\alpha_R=\Pr[j\in A\mid A_{-j}=R].
\]
Let
\[
B_j(F)=H(A_j\mid A_{-j}),\qquad
B_u(g_j)=H((Y_j)_u\mid (Y_j)_{-u}).
\]
Define for `0<=alpha,r<=1`
\[
\phi(\alpha,r)
:=h_2(\alpha)+\alpha h_2(r)-h_2(\alpha(1-r)).
\tag{2}
\]

### Theorem 3.1 — balanced composition erasure formula

For every such Boolean composition,
\[
\boxed{
B_{j,u}(h)
=
a\,B_u(g_j)
+
\mathbb E_R\,\phi(\alpha_R,r).
}
\tag{3}
\]

Equivalently,
\[
\phi(\alpha,r)
=
(1-\alpha+\alpha r)\,
h_2\!\left(\frac{\alpha r}{1-\alpha+\alpha r}\right).
\tag{4}
\]

### Proof

Condition on `A_{-j}=R`; write `C=A_j`, so `C` is Bernoulli with parameter `alpha=alpha_R`. Inside block `j`, the observed spectral vector is
\[
Z=C Y_j.
\]
Because `Y_j` is never empty, the full vector `Z` identifies whether `C=0` or `C=1`. Therefore
\[
H(Z\mid R)=h_2(\alpha)+\alpha H(Y_j).
\tag{5}
\]

After erasing coordinate `u`, the vector `Z_{-u}` is zero in exactly two cases: `C=0`, or `C=1` and `Y_j={u}`. Thus
\[
\Pr[Z_{-u}\ne0\mid R]=\alpha(1-r),
\]
and
\[
H(Z_{-u}\mid R)
=
h_2(\alpha(1-r))
+
\alpha(1-r)\,
H((Y_j)_{-u}\mid (Y_j)_{-u}\ne0).
\tag{6}
\]

Since the balanced inner spectral sample is nonempty, `(Y_j)_{-u}=0` iff `Y_j={u}`, so
\[
H((Y_j)_{-u})
=
h_2(r)+(1-r)H((Y_j)_{-u}\mid (Y_j)_{-u}\ne0).
\tag{7}
\]
Using
\[
B_u(g_j)=H(Y_j)-H((Y_j)_{-u}),
\]
subtract (6) from (5):
\[
H(Z_u\mid Z_{-u},R)
=
\alpha B_u(g_j)+\phi(\alpha,r).
\]
Averaging over `R` and using `E alpha_R=a` proves (3). Equation (4) is the entropy of the residual ambiguity between the two cases `C=0` and `C=1,Y_j={u}` after `Z_{-u}=0`. ∎

### Structural consequence

If the inner singleton atom vanishes, `r=0`, then `phi(alpha,0)=0` and
\[
\boxed{
\frac{B_{j,u}(h)}{\operatorname{Inf}_{j,u}(h)}
=
\frac{B_u(g_j)}{\operatorname{Inf}_u(g_j)}.
}
\tag{8}
\]
So balanced disjoint composition itself is not the selector obstruction. The entire extra selector cost is the **singleton leakage event** `Y_j={u}`, which hides whether the outer block was active after coordinate `u` is erased.

This is the main mechanism isolated by this run.

## 4. PROVED: Boolean singleton atoms are second order

For every Boolean `g` and coordinate `u`,
\[
\boxed{
\widehat g(\{u\})^2\le \operatorname{Inf}_u(g)^2.
}
\tag{9}
\]

### Proof

For the flip derivative
\[
D_u g(x_{-u})=\frac{g(+1,x_{-u})-g(-1,x_{-u})}{2},
\]
Booleanity gives `D_u g in {-1,0,1}`. Moreover
\[
\widehat g(\{u\})=\mathbb E D_u g,
\qquad
\operatorname{Inf}_u(g)=\mathbb E |D_u g|.
\]
Therefore
\[
|\widehat g(\{u\})|
\le \mathbb E|D_u g|
=\operatorname{Inf}_u(g),
\]
and squaring proves (9). ∎

This is the key Boolean input. An arbitrary probability kernel could have a singleton leakage of first order in `q`; Boolean Fourier structure forces `r<=q^2`.

## 5. PROVED: a quantitative selector transfer inequality

Concavity of binary entropy and `h_2(0)=0` imply
\[
h_2(\alpha(1-r))\ge(1-r)h_2(\alpha).
\]
Hence
\[
\phi(\alpha,r)
\le r h_2(\alpha)+\alpha h_2(r).
\tag{10}
\]
Averaging in (3) gives
\[
B_{j,u}(h)
\le
aB_u(g_j)+rB_j(F)+a h_2(r).
\tag{11}
\]
Divide by `aq`:
\[
\boxed{
\frac{B_{j,u}(h)}{aq}
\le
\frac{B_u(g_j)}q
+
\frac rq\,\frac{B_j(F)}a
+
\frac{h_2(r)}q.
}
\tag{12}
\]
Using `r<=q^2`, for `0<q<=1/2`,
\[
\boxed{
K_{h,(j,u)}
\le
K_{g_j,u}+qK_{F,j}+\frac{h_2(q^2)}q,
}
\tag{13}
\]
where `K=B/Inf`.

The outer selector cost is therefore damped by the inner influence `q`; the only additive ambiguity is a Boolean-second-order singleton term. This is weaker than the false max-parent rule, but it has the right qualitative small-`q` behavior.

## 6. Exact Boolean counterexample to max-parent closure

Take the outer three-bit AND/one-point Boolean function whose squared Fourier law is
\[
\mu_F(\varnothing)=9/16,
\qquad
\mu_F(T)=1/16 \quad (T\ne\varnothing).
\]
For every outer coordinate,
\[
a=1/4,
\qquad
B_j(F)=0.6681222459933007,
\qquad
K_{F,j}=2.672488983973203.
\]

Take a balanced four-bit Boolean `g` whose `+1` truth-table indices, with the checker indexing inputs by integers `0,...,15`, are
\[
\{1,2,3,5,6,7,9,11\}.
\]
Its unnormalised Walsh coefficients are nonzero exactly at
\[
\begin{array}{c|rrrrrrrrrr}
S\text{-mask}&1&2&3&4&5&8&10&11&12&13\\
\hline
W_S&-8&-4&-4&4&-4&8&-4&-4&-4&4 .
\end{array}
\]
Thus
\[
H(g)=3,\qquad I(g)=3/2,\qquad H(g)/I(g)=2.
\]
Its coordinate influences are
\[
(1/2,1/4,1/4,1/2),
\]
its singleton spectral weights are
\[
(1/4,1/16,1/16,1/4)=q^2,
\]
and its erasure ratios are
\[
(1,\ 1.8048202372184057,\ 1.8048202372184057,\ 1).
\]

Now compose three disjoint copies:
\[
h=F(g^{(1)},g^{(2)},g^{(3)}).
\]
Direct Walsh transform over all `2^12=4096` input values gives
\[
H(h)=4.4669171866887,\qquad
I(h)=1.125,\qquad
H(h)/I(h)=3.9705930548343997.
\]
All physical influences are
\[
(0.125,0.0625,0.0625,0.125)
\]
repeated across the three blocks, hence all are below `tau approximately 0.1805539925`.

The physical erasure ratios are, in each block,
\[
(3.18267448745729,\ 3.37220915898339,\ 3.37220915898339,\ 3.18267448745729).
\]
Therefore
\[
\min_i K_{h,i}=3.1826744874572865
>
2.672488983973203
\]
even though `2.67248...` exceeds every inner coordinate ratio. Thus the max-parent selector closure is false for an exact source-admissible Boolean composition.

This is **not** a counterexample to FEI. It does not even refute the current Hod-scale low-influence selector target, because
\[
3.1826744874572865<3.5693936182.
\]

## 7. Exhaustive four-bit balanced search

The checker exhausts every balanced four-bit Boolean inner function modulo global sign by fixing one truth value and choosing the other seven positive locations:
\[
\binom{15}{7}=6435.
\]
For each function it forms the exact balanced composition with the fixed outer three-bit function, discards candidates having a relevant physical influence at least `tau`, and maximizes
\[
\min_i B_i/\operatorname{Inf}_i.
\]

Results:

- balanced four-bit inner functions tested modulo sign: **6435**;
- valid low-influence composites: **1420**;
- exact best minimum erasure ratio: **3.1826744874572914**;
- current Hod-scale selector target: **3.5693936182**;
- remaining gap: **0.3867191307427085**;
- selector target refuted in this finite family: **no**.

The extremizer above is one maximizing representative. The checker also verifies by direct 12-bit Walsh transform the hierarchical entropy identity, all influences, all erasure entropies, the max-parent counterexample, `r<=q^2`, and inequality (13).

Finite exhaustive evidence is evidence only for this stated four-bit-inner / three-bit-outer family.

## 8. What this says about the universal gap

The stronger monotone composition route is dead: selector constants can increase above both parent selector constants under exact Boolean balanced composition.

But the failure is not arbitrary. Equations (3), (9), and (12) say precisely what must be paid:
the only new uncertainty at an erased physical coordinate is the collision
\[
\{\text{outer block inactive}\}
\quad\leftrightarrow\quad
\{\text{outer block active and inner spectral sample is }\{u\}\}.
\]
Booleanity makes the collision mass at most `q^2`.

This suggests a replacement route:

> Find a decomposition or comparison theorem for an arbitrary low-influence Boolean spectral sample into balanced activated blocks such that the cumulative singleton-leakage payments
> \[
> \sum h_2(r)/q
> \]
> and damped parent costs are summable against influence.

A naive recursive use of (13) is not yet enough. At the current threshold `tau`,
\[
h_2(\tau^2)/\tau\approx1.14794694757.
\]
If a decomposition supplied an inner selector cost at most
\[
(1-\tau)\,3.5693936182-\frac{h_2(\tau^2)}{\tau}
\approx1.77697840207,
\]
then the crude uniform version of (13) would close the present selector target. No such universal decomposition is proved here; this number is only a design calibration.

The next useful attack should therefore be on a **balanced-core extraction / activation decomposition lemma**, not on another max-parent inequality. The extraction must preserve exact Boolean Fourier structure and control singleton atoms; otherwise the one-point and product-like rare-coordinate obstructions reappear.

## 9. Sanity checks and literature applicability

Primary-literature checks performed during this run:

- O'Donnell and Tan, *A composition theorem for the Fourier Entropy-Influence conjecture* (arXiv:1304.1347, 2013): the disjoint-variable composition theorem is applicable background, but it controls FEI composition rather than the local `B_i/p_i` selector used here.
- Hod, *Improved Lower Bounds for the Fourier Entropy-Influence Conjecture via Lexicographic Functions* (arXiv:1711.00762): supports the current `>6.45478` lower-bound scale and the importance of composition constructions.
- González, MacManus, and Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture* (arXiv:2606.00246, 29 May 2026): current restriction/stopping-tree work remains partial and does not close full FEI.
- General erasure entropy is classical information-theoretic language (e.g. Verdú--Weissman, 2006); no novelty claim is attached to the notation itself.

I found no basis in this targeted search to claim publication novelty for Theorem 3.1, so it remains a repository-level mechanism pending a specialist prior-art search.

## 10. Artifacts and status

`verify_balanced_composition_erasure.py` uses exact rational squared Walsh coefficients for the finite Boolean search and floating-point only for entropy evaluation after the exact probabilities are formed. Its direct 12-bit check and all assertions pass.

- checker SHA-256: `63fcf1fe926b1a667a0b6b4102c2b913cd5cc92bd770e1d4d298789cbbdb3d2d`
- verification JSON SHA-256: `f4c8f740cceb499c1d449cede2696ac683bda6bc30e3e99a04905c48f81b46fe`

**Before/after:** no composition bound for the current erasure selector was available in this B17 scope before; after this run there is an exact identity, a Boolean `r<=q^2` leakage theorem, a quantitative transfer inequality, an exact Boolean counterexample to max-parent closure, and an exhaustive `6435`-function stress test. The full universal selector and full FEI remain OPEN.

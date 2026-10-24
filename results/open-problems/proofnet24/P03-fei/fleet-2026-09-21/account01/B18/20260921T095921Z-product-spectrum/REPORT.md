# Exact product spectral laws are partially bent: a Booleanity obstruction to the independent-small-marginal route

**Status: PARTIAL. Full Fourier entropy--influence (FEI) remains OPEN / NOT PROVED.**

Run: account01 / B18, 21 September 2026. Research was performed **WITHOUT_VERIFIED_BRAIN**: no authentic brain retrieval/context was available in this worker.

## What moved

Route 2 / Route 13 from the 21 September FEI approach list asks why a hypothetical product-set spectral sample with many tiny independent marginals cannot come from a Boolean function. This run closes the **exact product** version completely.

Tracked quantity:
\[
 C_{\rm prod}:=\sup\left\{\frac{H(f)}{I(f)}:
 f:\{-1,1\}^n\to\{-1,1\},\ 
 \widehat f(S)^2\text{ is a product law on }2^{[n]}\right\}.
\]

Before this run: not identified in the current FEI handoff.

After this run:
\[
 \boxed{C_{\rm prod}=2.}
\]

More precisely, every Boolean function whose spectral-sample membership bits are mutually independent is, after deleting irrelevant coordinates, a character times a bent function. Thus a product spectral law cannot have nonzero tiny independent marginals at all.

This does **not** prove full FEI. It isolates a concrete Booleanity mechanism that the arbitrary-product-distribution obstruction misses and suggests a quantitative stability problem for almost-product spectral laws.

Moves from `FLEET_RULES.md` used here: **#2 attack the negation first** (try the independent-small-marginal obstruction), **#18 say it in another language** (total correlation), **#4 prove something weaker completely** (classify exact product spectral laws), and **#16 compute every small case** (exact enumeration through four variables).

## Theorem: classification of independent spectral samples

Let
\[
 \mu_f(S)=\widehat f(S)^2,\qquad S\subseteq[n],
\]
be the spectral distribution of a Boolean function \(f:\{-1,1\}^n\to\{-1,1\}\), with normalized Walsh coefficients. Suppose the indicators
\[
 X_i=\mathbf 1_{\{i\in S\}},\qquad S\sim\mu_f,
\]
are mutually independent. Write
\[
 p_i=\Pr_{\mu_f}(i\in S).
\]

Then:

1. \(p_i\in\{0,\tfrac12,1\}\) for every \(i\).
2. If
   \[
   A=\{i:p_i=\tfrac12\},\quad
   D=\{i:p_i=1\},\quad
   Z=\{i:p_i=0\},
   \]
   then \(|A|\) is even.
3. After multiplication by the character \(\chi_D\), the function depends only on the coordinates in \(A\), and its restriction to those coordinates is bent. Equivalently,
   \[
   f(x)=\chi_D(x)\,g(x_A),
   \]
   up to an overall sign, where \(g\) is a bent Boolean function on the even-dimensional cube \(\{-1,1\}^{A}\).
4. Consequently
   \[
   H(f)=|A|,\qquad
   I(f)=|D|+\frac{|A|}{2},
   \]
   and hence
   \[
   H(f)\le 2I(f).
   \]
   Equality is attained whenever \(D=\varnothing\) and \(g\) is bent, so the constant 2 is sharp for this class.

### Lemma: a dyadic square-odds ratio is forced to one

If \(0<p<1\) is dyadic rational and
\[
 \frac{p}{1-p}
\]
is a square in \(\mathbb Q\), then \(p=\tfrac12\).

**Proof.**
Write \(p=a/2^k\) in lowest terms. Then \(a\) and \(2^k-a\) are odd and coprime. If
\[
 \frac{a}{2^k-a}=\left(\frac uv\right)^2
\]
in lowest terms, coprimality forces \(a=r^2\) and \(2^k-a=s^2\) for positive integers \(r,s\). Both \(r,s\) are odd. Therefore
\[
 2^k=r^2+s^2\equiv2\pmod4.
\]
Thus \(k=1\), and then \(a=1\), so \(p=1/2\). \(\square\)

### Proof of the theorem

For a Boolean function,
\[
 p_i=\sum_{S\ni i}\widehat f(S)^2=\operatorname{Inf}_i(f).
\]
The edge definition of influence shows that \(p_i\) is dyadic rational.

Fix \(i\) with \(0<p_i<1\). Because \(\mu_f\) is a product law, choose any support point \(S\) with \(i\notin S\); then \(S\cup\{i\}\) is also in the support and
\[
 \frac{\mu_f(S\cup\{i\})}{\mu_f(S)}
 =\frac{p_i}{1-p_i}.
\]
But every Walsh coefficient of a Boolean function is dyadic rational:
\[
 \widehat f(T)=2^{-n}\sum_x f(x)\chi_T(x)\in 2^{-n}\mathbb Z.
\]
Hence
\[
 \frac{p_i}{1-p_i}
 =\frac{\widehat f(S\cup\{i\})^2}{\widehat f(S)^2}
\]
is a square in \(\mathbb Q\). The lemma gives \(p_i=1/2\). This proves
\(p_i\in\{0,1/2,1\}\).

Product structure now gives
\[
 \mu_f(D\cup T)=2^{-|A|}\qquad(T\subseteq A),
\]
and zero mass elsewhere. Thus every nonzero Fourier coefficient has absolute value
\[
 2^{-|A|/2}.
\]
Since Fourier coefficients are rational, \(|A|\) must be even.

If \(i\in Z\), no nonzero Fourier coefficient contains \(i\), so \(f\) is independent of \(x_i\). If \(i\in D\), every nonzero Fourier coefficient contains \(i\). Multiplying by \(\chi_D\) shifts Fourier support by symmetric difference with \(D\), leaving a function \(g=f\chi_D\) whose Fourier support is exactly \(2^A\) and whose coefficients all have magnitude \(2^{-|A|/2}\). Hence \(g\) depends only on \(A\) and is bent there.

Finally independence gives
\[
 H(f)=H(S)=\sum_i h_2(p_i)=|A|,
\]
and the spectral identity for influence gives
\[
 I(f)=\mathbb E|S|=\sum_i p_i=|D|+\frac{|A|}{2}.
\]
Therefore \(H(f)\le2I(f)\). \(\square\)

## Exact total-correlation reformulation of the full FEI gap

For an arbitrary Boolean function, keep
\[
 p_i=\operatorname{Inf}_i(f)
\]
and let
\[
 \operatorname{TC}(S)
 :=D_{\rm KL}\!\left(\mu_f\,\middle\|\,\bigotimes_i {\rm Bern}(p_i)\right)
 =\sum_i h_2(p_i)-H(f)
\]
in bits. Then for every proposed FEI constant \(C\),
\[
 \boxed{
 H(f)-CI(f)
 =\sum_i\bigl(h_2(p_i)-Cp_i\bigr)-\operatorname{TC}(S).
 }
\]

Thus full FEI with constant \(C\) is **equivalent** to
\[
 \operatorname{TC}(S)\ge
 \sum_i\bigl(h_2(p_i)-Cp_i\bigr).
\]

This makes the exact-product theorem relevant to the universal obstruction: the arbitrary product law has
\(\operatorname{TC}=0\), but Booleanity forces every nondegenerate marginal of an exact product spectral law to equal \(1/2\), so the dangerous "many tiny independent marginals" model is not Boolean-realizable.

At Hod's numerical lower-bound constant
\[
 C=\beta(1/2)\approx6.4547837,
\]
the scalar term \(h_2(p)-Cp\) is positive only for
\[
 0<p<p_\star,\qquad p_\star\approx0.0305152.
\]
So at that candidate constant, only sufficiently rare spectral memberships require positive total-correlation payment. This is an exact algebraic reduction plus a one-dimensional numerical root, not a proof that the needed correlation lower bound holds.

## Decisive next target

A quantitatively useful successor would be a dimension-free stability statement of the following form:

> If a Boolean spectral law has many marginals \(p_i\ll1/2\), then its total correlation is bounded below by a fixed fraction of the aggregate rare-coordinate entropy excess
> \[
> \sum_i [h_2(p_i)-Cp_i]_+.
> \]

For \(C=\beta(1/2)\), proving
\[
 \operatorname{TC}(S)\ge
 \sum_i [h_2(p_i)-Cp_i]_+
\]
would immediately prove full FEI with that constant. The exact-product theorem proves the zero-total-correlation endpoint but gives no dimension-free stability by itself.

A useful next attack should therefore work directly with Booleanity
\[
 \widehat f * \widehat f=\delta_{\varnothing}
\]
and relative entropy to the product of the spectral marginals, rather than only with block-influence inequalities that every abstract random set already satisfies.

## Exact finite check

`check_product_spectral_classification.py` exhaustively checks every Boolean truth table through \(n=4\), using integer Walsh transforms and `Fraction` arithmetic only. It tests exact product factorization and then tests the theorem's allowed marginal set and parity condition.

Results:

| n | all Boolean functions | product-spectral functions | distinct product profiles | classification violations |
|---|---:|---:|---:|---:|
| 1 | 4 | 4 | 2 | 0 |
| 2 | 16 | 16 | 5 | 0 |
| 3 | 256 | 64 | 14 | 0 |
| 4 | 65,536 | 1,120 | 41 | 0 |

The computation is only a self-check; the theorem above is analytic and does not depend on enumeration.

## Literature check and novelty status

No novelty claim is made.

Fresh literature search on 21 September 2026 found:

- Vladimir N. Potapov, **"On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions,"** arXiv:2609.21563 (submitted 18 September 2026). Its abstract states FEI for plateaued functions with sharp class constant 4 and for partially bent functions with sharp constant 2.
- María José González, Paul MacManus, María Cristina Pereyra, **"Further evidence towards the Fourier Entropy-Influence conjecture,"** arXiv:2606.00246 (2026), develops the current restriction/stopping-tree line.
- Ryan O'Donnell and Li-Yang Tan, **"A composition theorem for the Fourier Entropy-Influence conjecture,"** arXiv:1304.1347 (2013), proves the composition framework for read-once formulas.
- Classical bent-function theory characterizes bent functions by flat Walsh magnitude; bent functions exist only in even dimension.

Because the theorem above classifies the exact independent-spectral class as a character extension of a bent function, its FEI constant-2 consequence overlaps the partially-bent constant-2 class now covered by Potapov. What may still be useful here is the **route-2 structural statement**: exact independence of spectral memberships plus Booleanity already forces the bent/character form, so independent small-marginal product spectra are impossible. Publication priority for that classification statement was not established in this run.

## Bottom line

**PROVED (restricted structural theorem):** exact product spectral distribution implies character times bent, and \(H/I\le2\) sharply.

**OPEN:** any dimension-free stability theorem converting approximate product structure / rare marginal influences into enough total correlation, and therefore full FEI.

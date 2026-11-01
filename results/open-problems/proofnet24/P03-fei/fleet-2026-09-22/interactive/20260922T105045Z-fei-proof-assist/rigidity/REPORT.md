# A geometric-amplitude KL reserve with dimension-free influence-scaled loss

**Status:** the compression theorem below has a complete elementary proof. Full uniform-cube FEI remains open. This is an information-theoretic bridge, not a proof that its retained reserve pays the FEI deficit. No priority or publication-level novelty claim is made.

## 1. Source context and exact improvement

The starting point is the signed-valuation/influence-class reserve and its exact conditional KL loss in [fleet01/B16, Sections 2–5 and 8](https://github.com/yspennstate/math-open-problems/blob/ee96e506b3e62e3cebfc5b8aa214acf0319c2c0d/proofnet24/P03-fei/fleet-2026-09-22/fleet01/B16/20260922T104019Z-B16-auto11/REPORT.md). That source identifies the remaining lost information as the variation of odd Walsh magnitudes within a signed-valuation/occupancy cell. It proves zero loss on one-point-defect suspensions and recursive ternary majority, but does not bound its original loss for arbitrary Boolean functions.

Here a geometric magnitude bin, with singleton labels kept separately, gives a modified reserve satisfying

\[
0\le K_{\mathrm{occ}}-K_q
\le \kappa_q\Pr_P(|S|\ge2)
\le \kappa_q\bigl(I(f)-1\bigr),
\qquad
\kappa_q\le\frac{\ln2}{2q^2}.
\tag{1}
\]

This holds for **every balanced uniform-cube Boolean function**, including boundary occurrence marginals. The statistic retains every spectral level. When all influences are equal, its number of possible cells is at most

\[
n+1+(qn+1)(n+1)=O(qn^2).
\tag{2}
\]

The bound concerns the number of statistic cells after the spectrum is available. Computing the full spectrum or its bins can still require exponential work; no polynomial-time FEI algorithm follows.

The construction can also refine the source's existing signed-valuation statistic. It does **not** prove that the source's original, unrefined odd-part loss is small.

## 2. Definitions and the boundary-safe maximum-entropy law

Let \(f:\{-1,1\}^n\to\{-1,1\}\) be balanced, \(n\ge1\), under the uniform measure. Write

\[
A_S=2^n\widehat f(S)\in\mathbb Z,
\qquad P(S)=\widehat f(S)^2=\frac{A_S^2}{4^n},
\qquad S\ne\varnothing.
\]

Balancedness and Parseval make \(P\) a probability law on nonempty subsets. Set

\[
r_i=\sum_{S\ni i}P(S),\qquad I=\sum_i r_i=\mathbb E_P|S|.
\]

Let \(Q_r\) be the unique maximum-entropy probability law on nonempty subsets with these occurrence marginals. This is the same law used in the source I-projection identity. Existence follows from compactness of the nonempty feasible probability polytope, and uniqueness from strict concavity of Shannon entropy.

Partition coordinates into their exact equal-marginal classes \(C_1,\dots,C_d\). Define

\[
\mathbf k(S)=(|S\cap C_1|,\dots,|S\cap C_d|).
\]

Two useful facts hold even when some \(r_i\) are zero or one, and when \(I=1\):

1. **Equal occupancy vectors have equal \(Q_r\) probability.** A permutation within an equal-marginal class preserves the feasible set. Uniqueness forces \(Q_r\) to be invariant under every such permutation. These permutations act transitively on the subsets with a fixed occupancy vector.
2. **\(Q_r(S)>0\) wherever \(P(S)>0\).** Otherwise mix \(Q_r\) with the feasible law \(P\). A coordinate where \(Q_r=0<P\) supplies a positive \(-t\log t\) entropy increment, dominating all finite linear changes for sufficiently small mixing parameter. This contradicts maximality.

These arguments avoid relying on finite exponential-family parameters at boundary points. Define

\[
K_{\mathrm{occ}}=D_2(P\Vert Q_r).
\]

The source I-projection identity identifies this with \(H(Q_r)-H(P)\). Only the displayed KL and the two elementary facts above are needed for the compression proof.

## 3. The statistic

Fix a positive integer \(q\). On nonempty Fourier labels define \(T_q\) as follows:

- If \(A_S=0\), give \(S\) a distinguished zero symbol.
- If \(A_S\ne0\) and \(|S|=1\), retain the singleton label \(S\) exactly.
- If \(A_S\ne0\) and \(|S|\ge2\), retain
  \[
  T_q(S)=\left(\mathbf k(S),\ b_q(S)\right),
  \qquad b_q(S)=\lfloor q\log_2|A_S|\rfloor.
  \tag{3}
  \]

Distinct tags separate these three cases. Binning is exact on integer Walsh data:

\[
b_q(S)=\operatorname{bitlength}(|A_S|^q)-1.
\]

Thus an amplitude exactly at a bin boundary enters the correct upper bin without a floating-point decision. Define the retained reserve

\[
K_q=D_2((T_q)_\#P\Vert(T_q)_\#Q_r).
\tag{4}
\]

Zero-amplitude labels may have positive \(Q_r\) probability. They are retained in the pushforward's zero cell. Their \(P\) mass is zero, so this cell contributes zero to conditional loss; it must not be silently removed from \(Q_r\).

## 4. A sharp bounded-range conditional KL estimate

### Lemma 1

Let \(w_1,\dots,w_m\in[1,R]\), \(R>1\), and let \(\pi_i=w_i/\sum_jw_j\). Put

\[
a=\frac{R\ln R}{R-1}.
\]

Then

\[
D_2(\pi\Vert\mathrm{Unif}[m])
\le\frac{a-1-\ln a}{\ln2}
\le\frac{(\ln R)^2}{8\ln2}.
\tag{5}
\]

The first bound is the sharp supremum over such finite weight lists, with arbitrary list length and limiting proportions.

**Proof.** Let \(s=m^{-1}\sum_iw_i\). Convexity gives the chord bound

\[
w\ln w\le\frac{R\ln R}{R-1}(w-1)=a(w-1).
\]

Consequently, in natural-log units,

\[
D(\pi\Vert U)
=\frac{\mathbb E_U[w\ln w]}s-\ln s
\le a\left(1-\frac1s\right)-\ln s.
\]

For \(1\le s\le R\), the right side is maximized at \(s=a\), since its derivative is \((a-s)/s^2\), and \(1<a<R\). Its maximum is \(a-1-\ln a\). Weights taking only the endpoint values \(1,R\), with the proportion making their mean approach \(a\), approach this maximum.

For the simpler second bound let \(X_i=\ln w_i\in[0,\ln R]\) and
\(F(t)=\ln\mathbb E_U e^{tX}\). Then

\[
D(\pi\Vert U)=F'(1)-F(1)
=\int_0^1 tF''(t)\,dt.
\]

Here \(F''(t)\) is the variance of \(X\) under the tilted probability law. Any random variable in an interval of length \(\ln R\) has variance at most \((\ln R)^2/4\): subtract the interval midpoint and use that variance is no larger than the second moment about that midpoint. Integrating gives \((\ln R)^2/8\). Divide by \(\ln2\). ∎

## 5. Uniform-cube compression theorem

### Theorem 2

For every balanced uniform-cube Boolean \(f\) and positive integer \(q\), let

\[
R_q=2^{2/q},\qquad
a_q=\frac{R_q\ln R_q}{R_q-1},\qquad
\kappa_q=\frac{a_q-1-\ln a_q}{\ln2}.
\]

Then (1) holds. In particular,

| \(q\) | \(\kappa_q\), numerical | Simple rigorous upper bound |
|---:|---:|---:|
| 1 | 0.337700499443757 | \((\ln2)/2\) |
| 2 | 0.086071332055934 | \((\ln2)/8\) |
| 4 | 0.021624810078870 | \((\ln2)/32\) |

**Proof.** The KL chain rule yields

\[
K_{\mathrm{occ}}-K_q
=\sum_tP_T(t)D_2(P(\cdot\mid T=t)\Vert Q_r(\cdot\mid T=t)).
\tag{6}
\]

The zero cell has \(P_T\) mass zero. A singleton cell contains one label and has conditional divergence zero.

In any occupied higher-level cell, \(\mathbf k\) is fixed, so \(Q_r\) is uniform there. The conditional \(P\) weights are proportional to \(A_S^2\). Since \(b_q\) is fixed, the ratio of any two positive amplitudes in the cell is strictly smaller than \(2^{1/q}\); their squared weights have ratio at most \(R_q\). Rescale by the least weight and apply Lemma 1. Each such cell contributes at most \(\kappa_q P_T(t)\).

Sum over higher-level cells. Their total mass is \(\tau=\Pr_P(|S|\ge2)\), and

\[
\tau\le\sum_{S\ne\varnothing}(|S|-1)P(S)=I-1.
\]

The lower bound follows from (6), and \(\kappa_q\le(\ln2)/(2q^2)\) follows from Lemma 1 with \(\ln R_q=2\ln2/q\). ∎

If every nonzero non-singleton coefficient lies at level at least \(\ell\ge2\), the same proof improves the last term to \(\kappa_q(I-1)/(\ell-1)\). For an odd Boolean function, \(\ell=3\) applies whenever a non-singleton coefficient occurs.

### Exact cell count

For uniform-cube Walsh integers, \(1\le|A_S|\le2^n\) whenever nonzero. Thus \(0\le b_q\le qn\). With class sizes \(n_1,\dots,n_d\), the number of possible cells is at most

\[
1+n+(qn+1)\prod_{j=1}^d(n_j+1).
\tag{7}
\]

This proves (2) when all influences are equal. For fixed \(d\), the bound is polynomial in \(n\); for \(d=n\), the occupancy vector can retain the full label, and no useful compression is promised. Empty cells may be discarded after their probabilities have been computed.

### A level-adaptive variant with fewer cells

There is a separate variant with \(O(qn\log n)\) cells in the equal-influence case. Keep the zero and singleton rules. For \(|S|=k\ge2\), retain \(\mathbf k(S)\) and

\[
b_q^{\mathrm{lin}}(S)
=\left\lfloor\frac{q\log_2(A_S^2)}{k-1}\right\rfloor
=\left(\operatorname{bitlength}(|A_S|^{2q})-1\right)\mathbin{//}(k-1),
\tag{7a}
\]

where \(//\) denotes integer division. Call its retained divergence \(K_q^{\mathrm{lin}}\). Within a cell, the ratio of largest to least squared amplitude is less than \(2^{(k-1)/q}\). If normalized weights have ratio at most \(R\), their likelihood ratio to the uniform law is at most \(R\), and their divergence in bits is at most \(\log_2R\). Applying the same conditional chain rule gives

\[
\boxed{0\le K_{\mathrm{occ}}-K_q^{\mathrm{lin}}
\le\frac1q\sum_S(|S|-1)P(S)=\frac{I-1}{q}.}
\tag{7b}
\]

When all influences are equal, one occupancy vector occurs at each level. Since \(0\le\log_2 A_S^2\le2n\), the number of possible cells is at most

\[
n+1+\sum_{k=2}^n\left(\left\lfloor\frac{2qn}{k-1}\right\rfloor+1\right)
\le 2qnH_{n-1}+2n,
\tag{7c}
\]

where \(H_m=\sum_{j=1}^m1/j\), \(H_0=0\). For \(0<\varepsilon\le1\), an error budget \(\varepsilon(I-1)\) is available with \(q=\lceil1/\varepsilon\rceil\) and \(O(n\log(n+1)/\varepsilon)\) cells. This remains a statement about the compressed distribution after source coefficients are available.

This wider-bin variant does not inherit every exact-zero-loss property of the fixed-width variant. It is still exact on one-point suspensions. It may merge unequal power-of-two amplitudes on recursive majority, but (7b) retains its entire dimension-growing KL contribution up to an additive \((I-1)/q\); it never makes a fixed-level truncation. For example, depth-three recursive majority has level-seven amplitudes of magnitudes \(2^{-7}\) and \(2^{-9}\), which the \(q=1\) linear bins merge after conversion to Walsh integers in dimension 27.

## 6. Relation to the original signed-valuation reserve

Let \(Z\) be the source's signed-valuation/influence-class statistic, and define

\[
K_q^+=D_2((Z,T_q)_\#P\Vert(Z,T_q)_\#Q_r).
\]

Refinement gives \(K_q^+\ge K_q\) and \(K_q^+\ge K_{\mathrm{SVIC}}\). The proof of Theorem 2 applies to the refined cells unchanged, so

\[
0\le K_{\mathrm{occ}}-K_q^+\le\kappa_q(I-1).
\tag{8}
\]

Within a fixed valuation \(v\), binning \(|A_S|\) is the same as binning its odd part, with a fixed shift by \(qv\). The original odd-part loss therefore has the exact decomposition

\[
K_{\mathrm{occ}}-K_{\mathrm{SVIC}}
=\underbrace{K_q^+-K_{\mathrm{SVIC}}}_{\text{retained bin-information KL}}
+\underbrace{K_{\mathrm{occ}}-K_q^+}_{\le\kappa_q(I-1)}.
\tag{9}
\]

The first term can be large. Equation (9) does not bound the original loss by \(O(I)\); it explicitly retains the part that such a bound might miss.

### Mandatory stress families

For every positive integer \(q\), the new loss is exactly zero on:

- **One-point-defect suspensions** \(F_m(y,x)=y(1-2\mathbf1_{x=0})\). The exceptional Fourier coefficient is a singleton label and is retained exactly; all non-singleton nonzero Walsh amplitudes have the same magnitude.
- **Recursive ternary majority at every depth.** By the source's disjoint-composition proof, every nonzero coefficient is a signed power of two. Distinct integer powers of two occupy distinct bins for every positive integer \(q\). Magnitudes are therefore constant within every occupied cell.
- **Flat nonzero spectra**, for the same constant-weight reason.

Every spectral cardinality is retained. No fixed-depth truncation, unweighted convolution norm, or one-tail merge occurs. The source's rare-event and recursive-majority logarithms survive exactly on the two required stress families.

## 7. Arbitrary product biases and variance-scaled loss

Let \(f\) be a nonconstant Boolean function under any interior product-bias vector, and let \(\widehat f_p(S)\) denote its coefficients in the orthonormal biased Walsh basis. Set

\[
v=\operatorname{Var}_p(f)>0,\qquad
P(S)=\frac{\widehat f_p(S)^2}{v}\ (S\ne\varnothing),\qquad
\widetilde I=\sum_{S\ne\varnothing}|S|\widehat f_p(S)^2.
\]

Thus \(\mathbb E_P|S|=\widetilde I/v\). Define equal occurrence classes from this normalized \(P\), its maximum-entropy law \(Q_r\), and the same statistic with real-amplitude bins

\[
b_q(S)=\lfloor q\log_2|\widehat f_p(S)|\rfloor.
\]

The proof uses only weight ratios and occupancy symmetry. Multiplying every amplitude by one common positive scale changes the bin alignment but leaves all stated bounds valid; this permits exact integer-weight diagnostics at rational biases. The proof gives

\[
\boxed{
0\le v(K_{\mathrm{occ}}-K_q)
\le\kappa_qv\Pr_P(|S|\ge2)
\le\kappa_q(\widetilde I-v).
}
\tag{10}
\]

No dyadic lattice is asserted for arbitrary biases. If \(a_{\min},a_{\max}\) are the least and greatest nonzero amplitude magnitudes, the number of amplitude bins is at most

\[
\left\lfloor q\log_2(a_{\max}/a_{\min})\right\rfloor+2.
\]

Replace \(qn+1\) in (7) by this quantity. The uniform-cube \(O(qn^2)\) equal-influence cell bound does not automatically extend to arbitrary biases: their amplitude dynamic range has no such integer-lattice bound. For constant functions \(v=0\), define the variance-weighted reserve and loss as zero; no normalized law is required.

The linear level-adaptive variant similarly satisfies

\[
0\le v(K_{\mathrm{occ}}-K_q^{\mathrm{lin}})
\le\frac{\widetilde I-v}{q},
\]

using real bins of \(q\log_2(\widehat f_p(S)^2)/(|S|-1)\). Its uniform integer-lattice cell count likewise requires the uniform-cube hypothesis.

## 8. What the new bridge does and does not prove

On the balanced slice, writing \(H_{\max}=H(Q_r)\), the full FEI payment at constant \(C\) is

\[
K_{\mathrm{occ}}\ge H_{\max}-C(I-1).
\]

The new theorem supplies the precise implications

\[
K_q\ge H_{\max}-C(I-1)
\quad\Longrightarrow\quad H(f)\le C(I-1),
\tag{11}
\]

and

\[
H(f)\le C(I-1)
\quad\Longrightarrow\quad
K_q\ge H_{\max}-(C+\kappa_q)(I-1).
\tag{12}
\]

It follows that a uniformly sufficient finite-constant payment using this new reserve is equivalent, at the existence-of-a-finite-constant level, to the balanced FEI problem. The compression theorem pays its own information-loss error. It supplies no independent universal lower bound on \(K_q\) large enough to establish (11).

In particular, a positive KL gap, a small bin count, or zero loss on the known stress families is not a solution to FEI. The new concrete target is to bound the retained **bin probabilities relative to their influence-matched maximum-entropy probabilities**, using actual Boolean constraints, while paying the complete residual in (11). Merely renaming that inequality is not progress.

## 9. An elementary sharpening of the exact-support neighborhood

The [near-bent source, Corollary 4.1](https://github.com/yspennstate/math-open-problems/blob/3d2550e06701d307357200d988eb52697a558e92/proofnet24/P03-fei/fleet-2026-09-22/fleet03/B07/20260922T103431Z-fleet03-B07-FEI-r11/REPORT.md) gives a dimension-free TV collar on an exact affine coordinate support using the bound \(H\le m\). Keeping binary entropy gives a larger explicit collar, by an elementary subadditivity argument.

Suppose \(P\) is supported on \(\{F\cup R:R\subseteq A\}\), with \(F\ne\varnothing\), \(F\cap A=\varnothing\), and \(m=|A|>0\). Define

\[
t=\frac1m\sum_{i\in A}r_i.
\]

Entropy subadditivity and concavity of \(h_2\) give

\[
H(P)\le\sum_{i\in A}h_2(r_i)\le mh_2(t),
\qquad I=|F|+mt.
\tag{13}
\]

For any \(a\in(0,1/2]\), if \(t\ge a\), then

\[
\boxed{H(P)\le\frac{h_2(a)}a\,(I-1).}
\tag{14}
\]

Indeed, \(h_2(t)/t\) is strictly decreasing on \((0,1)\), since its derivative is \(\ln(1-t)/(t^2\ln2)<0\); combine this with \(|F|\ge1\) in (13).

If additionally \(\|P-U_{F,A}\|_{\mathrm{TV}}\le\varepsilon\), then \(t\ge1/2-\varepsilon\), by applying the TV bound to the function \(|S\cap A|/m\in[0,1]\). In particular,

\[
\varepsilon\le\frac{15}{32}
\quad\Longrightarrow\quad
H(P)\le\left(5+31\log_2\frac{32}{31}\right)(I-1),
\tag{15}
\]

where the constant is approximately \(6.419914378006867\), strictly less than \(6.5\). The strict comparison follows from \(\ln(32/31)<1/31\) and \(\ln2>2/3\).

This is a support-constrained, sufficiently dense-influence corollary of entropy subadditivity. It does not prove template recovery, does not permit unpriced leakage outside the affine support, and is not presented as a new major subclass solution. The recent primary preprint by Vladimir N. Potapov already reports sharp FEI constants 4 for plateaued Boolean functions and 2 for partially bent functions; no novelty claim about those established scopes is intended. [Potapov, arXiv:2609.21563v1, submitted 18 September 2026](https://arxiv.org/abs/2609.21563v1)

## 10. Verification and next task

`CHECK.py` computes exact integer Walsh spectra and checks both fixed-width and linear-adaptive losses on all 12,870 balanced four-input truth tables, plus 128 seeded cyclic odd functions at dimensions 5, 7, 9, and 11 with one exact influence class. All 12,998 tables passed. It also checks exact-zero-loss behavior of the fixed-width reserve on one-point suspensions at dimensions 3 through 11 and recursive majority at depth two. A further 36 tests use exact squared-weight integers for cyclic sources under rational common input biases 1/3, 1/5, and 2/5, checking both variance-weighted inequalities. Logarithms in these diagnostics are floating-point; they are implementation checks, not a substitute for the analytic proofs above.

The first productive continuation is to identify a Boolean structural inequality controlling the retained magnitude-bin distribution in an influence class. The present theorem ensures that this continuation can spend an arbitrarily small \(\kappa_q(I-1)\) approximation budget without losing the rare-event logarithm or removing high levels. Its unresolved payment remains explicit in (11).

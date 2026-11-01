# Fourier entropy for affine images of symmetric products

Research continuation for Yitzchak Shmalo, 20 September 2026.

**Scope.** The unrestricted Friedgut–Kalai Fourier entropy–influence conjecture is not proved here. This report proves a uniform bound for arbitrary surjective affine images of products of fully symmetric Boolean functions. The proof permits unbounded factor degree and arbitrary mixing of the jointly independent logical coordinates. It does not cover dependent logical forms, arbitrary Boolean cores, or a new unrestricted quadratic output phase. Independent review and publication-priority clearance remain outstanding.

## 1. The theorem

Let the logical space \(\mathbb F_2^m\) have disjoint coordinate blocks \(U_1,\ldots,U_s\). For every \(t\), let \(h_t\) be an arbitrary fully symmetric Boolean sign function on its block: it depends only on that block's Hamming weight. Let

\[
L:\mathbb F_2^N\longrightarrow\mathbb F_2^m
\]

be surjective, let \(b\in\mathbb F_2^m\), and let \(\ell\) be an affine linear polynomial on the physical input space. Define

\[
F(x)=(-1)^{\ell(x)}\prod_{t=1}^s h_t((Lx+b)_{U_t}).
\]

**Theorem 1.** With Fourier entropy in bits,

\[
\boxed{H(F)\le32.08\,\mathfrak I(F)\le32.08\,J(F)\le32.08\,I(F).}
\tag{1.1}
\]

Here \(J\) is folded physical influence and \(\mathfrak I\) is minimum folded influence over all input bases, defined below. The coefficient is independent of dimension, number of factors, factor degrees, and the particular surjective map.

The rows of \(L\) can overlap extensively in the physical coordinates, but must be jointly linearly independent. This is substantially different from requiring each factor to use a separate physical group. Surjectivity is not a technicality: the proof uses the uniform joint law of all logical inputs.

The published O'Donnell–Wright–Zhou theorem gives constant 12.04 for a symmetric function in its symmetric coordinate system. That theorem is the non-elementary input. It does not by itself permit replacing physical influence by minimum affine influence. The argument below supplies that transfer with coefficient 32.08. It is a broader representation class with a larger constant, not an improvement to the published symmetric constant.

## 2. Definitions and inherited affine identities

For a Boolean sign function \(f\) on \(\mathbb F_2^n\), set

\[
a_S=\widehat f(S)=2^{-n}\sum_xf(x)(-1)^{S\cdot x},\qquad
H(f)=\sum_Sa_S^2\log_2\frac1{a_S^2}.
\]

Zero masses contribute zero. For a direction \(v\), put

\[
\alpha_f(v)=\Pr[f(x)\ne f(x+v)],\quad
c_f(v)=1-2\alpha_f(v),\quad
j_f(v)=\frac{1-|c_f(v)|}{2}.
\]

Write \(I(f)=\sum_i\alpha_f(e_i)\), \(J(f)=\sum_i j_f(e_i)\), and

\[
\mathfrak I(f)=\min_{(v_1,\ldots,v_n)\text{ basis}}\sum_i j_f(v_i).
\tag{2.1}
\]

Thus \(\mathfrak I\le J\le I\). Output characters preserve \(H\) and every folded directional influence. An invertible input change preserves \(H\) and \(\mathfrak I\), but need not preserve \(I\) or \(J\).

The preceding affine-variance report already proved exact tensorization and surjective-lift invariance for \(\mathfrak I\). The short proofs are included to make their use transparent and to preserve their hypotheses.

For \(0\le u\le1/2\), define

\[
E_u(f)=\operatorname{span}\{v:j_f(v)\le u\}.
\]

The greedy minimum-weight basis identity is

\[
\mathfrak I(f)=\int_0^{1/2}[n-\dim E_u(f)]\,du.
\tag{2.2}
\]

Every basis has at most \(\dim E_u\) elements of cost at most \(u\). Conversely, greedily retaining a vector whenever it increases the span achieves this rank at every threshold. Integrating the number of selected elements above the threshold proves (2.2).

For disjoint-input products, correlations multiply. Consequently

\[
j_{fg}(v,w)=\tfrac12[1-|c_f(v)c_g(w)|]\ge\max\{j_f(v),j_g(w)\}.
\]

Cheap vectors therefore lie in \(E_u(f)\oplus E_u(g)\), and embedded cheap vectors show equality of these spans. It follows that

\[
\mathfrak I(fg)=\mathfrak I(f)+\mathfrak I(g),\qquad H(fg)=H(f)+H(g).
\tag{2.3}
\]

For a surjective \(L:\mathbb F_2^N\to\mathbb F_2^m\), the cheap-direction span of \(f\circ L\) is \(L^{-1}E_u(f)\), of dimension \(N-m+\dim E_u(f)\). Equation (2.2) proves affine-influence invariance. The injection \(L^{\mathsf T}\) on Fourier labels proves entropy invariance. Input translations only change Fourier signs. Thus

\[
H(f(Lx+b))=H(f),\qquad
\mathfrak I(f(Lx+b))=\mathfrak I(f).
\tag{2.4}
\]

These identities are inherited results, not re-announced as discoveries of this continuation.

## 3. An elementary entropy bound for a physical split

Let \(g,h\) be the two Boolean children of a physical split of \(f\), and put

\[
\Delta H=H(f)-\tfrac12[H(g)+H(h)].
\]

**Lemma 3.1.**

\[
\boxed{0\le\Delta H\le\|\widehat g^{\,2}-\widehat h^{\,2}\|_1
\le2\max\{\operatorname{Var}(g),\operatorname{Var}(h)\}.}
\tag{3.1}
\]

In particular \(\Delta H\le2[\operatorname{Var}(g)+\operatorname{Var}(h)]\).

**Proof.** At one parent Fourier pair \((u,v)\), write \(w=u^2+v^2\) and \(t=\min(u^2,v^2)/w\), omitting zero pairs. The existing exact fibre identity is

\[
\Delta H=\sum w\Psi(t),\qquad
\Psi(t)=h_2(t)+1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right).
\]

For \(0\le t\le1/2\),

\[
\Psi(t)\le4\sqrt{t(1-t)}.
\tag{3.2}
\]

To verify this, let \(r=2\sqrt{t(1-t)}\). Binary entropy satisfies \(h_2(t)\le r\) and, by concavity, \(h_2((1+r)/2)\ge1-r\). For completeness, the first inequality follows by setting \(x=1-2t\) and considering

\[
q(x)=\sqrt{1-x^2}-h_2((1-x)/2).
\]

Its endpoints are zero. The sign of its derivative is the sign of
\(\sqrt{1-x^2}\operatorname{atanh}(x)/x-\ln2\). The function before \(-\ln2\) decreases strictly from one to zero, since its derivative is

\[
\frac{x-\operatorname{atanh}x}{\sqrt{1-x^2}\,x^2}<0.
\]

Thus \(q\) first increases and then decreases, so is nonnegative. This proves (3.2).

If \(a=\widehat g(T)\), \(b=\widehat h(T)\), then \(u=(a+b)/2\), \(v=(a-b)/2\). Hence

\[
w\Psi(t)\le4|uv|=|a^2-b^2|.
\]

Summing proves the first upper bound. For probability laws \(P,Q\),

\[
\|P-Q\|_1=2\left(1-\sum_T\min(P_T,Q_T)\right)
\le2[1-\min(P_\varnothing,Q_\varnothing)].
\]

For the two child spectra, their empty masses are \((\mathbb Eg)^2\) and \((\mathbb Eh)^2\), yielding the second bound. Nonnegativity is the existing erasure-plus-Jensen–Shannon identity. QED.

A constant child and a nonconstant character child attain the value two, so the variance bound has a genuine equality case. The first bound is an absolute-overlap majorant already familiar in the project. It does not repair Han's refuted universal overlap selector: here it is used only to estimate one explicitly chosen parity split by child variances.

We will also use the elementary Poincare inequality

\[
\operatorname{Var}(g)=\sum_{S\ne\varnothing}\widehat g(S)^2
\le\sum_S|S|\widehat g(S)^2=I(g).
\tag{3.3}
\]

## 4. Symmetry forces a basis-level influence payment

Let \(h\) be fully symmetric on \(n\ge2\) inputs. Put

\[
\beta=\alpha_h(e_1+e_2).
\]

By symmetry, any two-coordinate direction has the same disagreement probability.

**Lemma 4.1.** If \(v\ne0,\mathbf1\), then

\[
\boxed{j_h(v)\ge\beta/2.}
\tag{4.1}
\]

**Proof.** Choose \(i\) in the support of \(v\) and \(j\) outside it, and let \(\tau\) exchange these two coordinates. Symmetry gives \(c_h(v)=c_h(\tau v)\). Choose the same sign \(\sigma\) minimizing disagreement with each translation. Each of

\[
h(x+v)=\sigma h(x),\qquad h(x+\tau v)=\sigma h(x)
\]

fails on a set of measure \(j_h(v)\). Outside their union the two translated values agree. Their displacement is \(v+\tau v=e_i+e_j\), so translation invariance gives \(\beta\le2j_h(v)\). QED.

Notice that \(\beta\) is **unfolded** two-coordinate disagreement. Choosing the same sign on the two comparisons is essential to this conclusion.

Any input basis contains at most one all-ones vector. At least \(n-1\) of its vectors therefore obey (4.1), and

\[
\boxed{\mathfrak I(h)\ge\frac{n-1}{2}\beta.}
\tag{4.2}
\]

This argument uses an entire directional orbit rather than falsely asserting that the original physical influence is invariant under linear mixing.

## 5. Parity sections retain enough symmetry

Use the invertible map

\[
x_1=z+\sum_{j=2}^ny_j\pmod2,\qquad x_j=y_j\quad(j\ge2),
\]

and write \(G(z,y)=h(x)\). Fourier entropy is unchanged. Its physical \(z\)-children \(h_b(y)=G(b,y)\) are fully symmetric on \(n-1\) variables: if \(|y|=w\), the original weight is

\[
w+((b+w)\bmod2).
\]

Changing a \(y_j\) flips precisely \(x_1,x_j\). Averaging over \(z\) therefore gives the exact identity

\[
\frac{I(h_0)+I(h_1)}2=(n-1)\beta=:E.
\tag{5.1}
\]

O'Donnell–Wright–Zhou gives \(H(h_b)\le C_{\rm sym}I(h_b)\) with \(C_{\rm sym}=12.04\). Lemma 3.1 and (3.3) pay the parity split:

\[
\begin{aligned}
H(h)=H(G)
&=\tfrac12[H(h_0)+H(h_1)]+\Delta_zH(G)\\
&\le C_{\rm sym}E+2[\operatorname{Var}(h_0)+\operatorname{Var}(h_1)]\\
&\le(C_{\rm sym}+4)E.
\end{aligned}
\]

Combining with (4.2) proves

\[
\boxed{H(h)\le16.04(n-1)\beta\le32.08\,\mathfrak I(h).}
\tag{5.2}
\]

For \(n=1\), every Boolean function is a character up to sign and has entropy zero. If \(\beta=0\), the same argument gives zero entropy; equivalently, \(h\) is constant on each parity class and hence a character up to sign. These cases cause no division by zero.

More generally the proof transfers any valid uniform symmetric-function coefficient \(C_{\rm sym}\) to coefficient \(2C_{\rm sym}+8\) for its affine-minimum bound. We do not assert that 32.08 is optimal.

## 6. Products and affine maps

Apply (5.2) separately to the logical symmetric factors. In the logical coordinate system, entropy and minimum affine influence add by (2.3):

\[
H\left(\prod_t h_t\right)
=\sum_tH(h_t)
\le32.08\sum_t\mathfrak I(h_t)
=32.08\,\mathfrak I\left(\prod_t h_t\right).
\]

Equation (2.4) transfers this to any surjective affine input map. An output affine character preserves both sides. This proves Theorem 1.

This result is compatible with using its functions as leaves of a paid physical restriction tree. It is not an assertion that arbitrary physical restrictions preserve the representation: fixing a coordinate can destroy joint surjectivity. A stopped leaf must be certified on its actual remaining inputs.

The theorem also does not subsume the preceding constant-12.04 arbitrary-quadratic-coupling theorem in all directions. That theorem has additional output quadratic interactions but requires physical disjointness of its original symmetric cores. The present theorem allows unrestricted surjective affine input mixing but only an affine output phase. Neither set of hypotheses is silently removed.

### Why dropping surjectivity is already the full problem

There is an exact representation obstruction, not just an informal warning. Every Boolean function \(f\) on \(n\ge2\) variables is a non-surjective linear pullback of a single symmetric function. Set \(m=2^n-1\) and repeat physical bit \(x_i\) exactly \(2^{i-1}\) times in \(Lx\). Then

\[
|Lx|=\sum_{i=1}^n2^{i-1}x_i
\]

is the integer encoded by the input bits, ranging over every value from zero through \(m\). Define the symmetric function \(h\) on \(m\) variables by prescribing its value at weight \(k\) to be \(f\) at the binary expansion of \(k\). Then \(f=h\circ L\).

Consequently, extending (1.1) to arbitrary, possibly dependent logical forms with one universal coefficient would itself prove full FEI. The surjective hypothesis excludes exactly this unrestricted encoding. The new theorem does not claim a way of controlling this general dependence.

## 7. Executed exact checks

Run `python verify_affine_symmetry.py` with Python >=3.10 and NumPy. All assertion arithmetic is integer or rational; entropy comparisons use symbolic prime-logarithm cancellation followed by outward rational atanh-series bounds.

The actual output `verification.json` records:

- All **65,812** Boolean functions in dimensions 1--4, and **262,948** physical splits, for the scalar entropy/variation bound and variation-to-variance bound.
- All **16,380** symmetric truth tables in dimensions 1--12. These supply **163,848** directional-swap inequalities, **16,376** parity-section identities, and the stated entropy/affine-influence comparisons.
- **124** exact comparisons between the weight-orbit minimum-basis formula and an explicit vector-greedy computation through dimension five.
- **108** reproducibly sampled surjective affine product lifts, involving **249** symmetric factors, through **12** physical variables. Fourier entropy invariance, affine-minimum tensorization, and the final inequality were checked exactly.

The fixed seed is 2026092021. The checker contains its own Walsh, Krawtchouk, rank, and logarithm code; it does not download a dependency or call an external proof checker. These finite checks do not prove Theorem 1 by extrapolation and are not unrestricted FEI coverage in dimension twelve.

## 8. Full-scope attempt and companion obstruction

The companion `ENDPOINT_QUANTIFIERS.md` investigates the live dimension-adaptive endpoint route. It proves that no universal coefficient can pay **every prescribed relevant coordinate**, even when every input variable is relevant. The construction uses a previously known bent-background bad split and a new padding argument. The weaker claim that there always exists a suitable paid coordinate is not refuted.

That distinction is important. The symmetric affine theorem supplies another class of stopping leaves. The endpoint obstruction eliminates a tested strengthening, not the actual remaining universal selector. Neither result establishes a finite bound for

\[
\sup_f\frac{\sum_i H(S_i\mid S_{-i})}{I(f)}.
\]

No general decomposition of an arbitrary Boolean function into the new affine-symmetric class is proved. A representation count also gives no reason to expect all functions to lie in that class. The outstanding mathematical step is still a universal payment or stopping mechanism for arbitrary surviving cores.

## 9. Sources and provenance

**Primary published input.** Ryan O'Donnell, John Wright, Yuan Zhou, *The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions*, ICALP 2011, DOI `10.1007/978-3-642-22006-7_28`. The author manuscript at `https://www.cs.cmu.edu/~odonnell/papers/fei.pdf` was read and its theorem page inspected as a PDF image. Theorem 1 supplies 12.04. That theorem, Poincare, Fourier tensorization, and ordinary affine-label invariance are credited rather than claimed new.

**Current source-level context.** Maria Jose Gonzalez, Paul MacManus, Maria Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, revised **9 June 2026**. Its abstract and history were checked on 20 September 2026. It presents restricted stopping-tree results, not a full FEI proof. One inherited worker report gave a 2 June revision date; the actual arXiv history says 9 June.

**Repository sources consumed.**

1. `proofnet24/P03-fei/README.md`, initial blob `1156fab7d6b2e8360bcbaa138855b97345b8def1`: current scopes and retired proof targets, read in full.
2. `proofnet24/P03-fei/continuations/2026-09-19-affine-variance/REPORT.md`, blob `2fa7fb2f510b10ceedc53fd560b87defa904c6dc`: sections on minimum affine influence, rank integration, exact products, and surjective lifting were read in full. These supply the inherited identities reconstructed in Section 2.
3. `proofnet24/P03-fei/continuations/2026-09-20-concave-restriction/REPORT.md`, blob `b586723862b68d32dda97e0085b9868023fffa46`: recovered from the actual prior conversation archive; the exact fibre profile supplies the starting identity in Section 3.
4. `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20__endpoint-character-child-cross-fibre.md`, blob `6786f1a9417f4e6e80a4e6a45cb2cbce728a4237`: initial 250 lines read for its endpoint definition, universal gap, and explicitly character-child theorem. The companion obstruction does not assume its later proof.
5. `proofnet24/P03-fei/continuations/2026-09-20-polynomial-cores-and-tags/UNITARY_ERASURE_OBSTRUCTION.md`, blob `f35419c90fc304f7b8c77255fb5d4978e830121d`: the displayed construction and proof were read to avoid replacing Boolean convolution by the already-refuted general orthogonal-involution relaxation. The present theorem does not depend on that report as a premise.

**Mathematical delta.** The fully symmetric two-flip orbit payment and parity-section argument prove the affine-minimum bound, which combines with the previously proved affine identities to handle arbitrary surjective mixing of symmetric products. The companion separates every-coordinate and existential endpoint statements with an all-dimensional obstruction and a finite analytic certificate. Publication priority is not established by the bounded searches conducted here.

**Scope control.** No use is made of the false all-coordinate absolute-overlap selector, raw shared-control decrement subadditivity, pointwise erasure converse, full-resolvent payments, fixed-coefficient affine entropy drift, or unrestricted orthogonal-involution relaxation. No schedules, ownership, visibility, permissions, or native atlas metric are changed by these reports.

# fleet03/B18 — finite balanced defect patterns have universal Fourier-dust slope 4

**Run:** `fleet03-B18-20260922T050806Z`  
**Candidate:** `LIMIT-PRIME-GATE-LIFT-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / BOUNDED-SPARSE-DUMMY-AMPLIFICATION_CLOSED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live target and exact peer result consumed

The later owner control converges the FEI fleet on the all-gate inequality.  The newest compatible fixed candidate used by the neighboring workers is

\[
C_*=6.5218512,
\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\]

with universal missing implication

\[
D_{\Gamma_*}(P;p)\ge0
\tag{1.1}
\]

for every finite composition-prime Boolean gate \(P\), every arity, and every interior product-bias vector.  On a balanced gate at uniform input bias this is exactly

\[
D_{\Gamma_*}(G;1/2,\ldots,1/2)
=C_*[I(G)-1]-H(G).
\tag{1.2}
\]

The named completed other-account result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T044637Z-radius2-dust-compensation/REPORT.md`

at the current scientific history.  Its Theorem 5.1 proves that one particular balanced **two-point** physical defect, embedded into a growing number of dummy coordinates, has incremental spectral entropy/influence ratio tending to \(4\).  It also closes all symmetric-difference-four mutations of the exact 18-cell source support below \(6.48\).

This run attacks the remaining structural question behind that asymptotic result: was slope \(4\) an accident of the special opposite-sign pair and its parity-hyperplane Fourier cloud, or is it forced for every fixed finite signed Boolean defect pattern?  The answer is the latter.

## 2. Exact theorem

### Theorem 2.1 — finite-pattern Fourier-dust slope

Let

\[
f:\{0,1\}^r\to\{\pm1\}
\]

be balanced.  Fix an integer \(s\ge0\), put \(d=r+s\), and choose distinct points

\[
z_1,\ldots,z_K\in\{0,1\}^d,
\qquad z_j=(x_j,y_j),
\]

where \(x_j\in\{0,1\}^r\).  Assume the flips preserve balance:

\[
\boxed{\sum_{j=1}^K f(x_j)=0.}
\tag{2.1}
\]

For every \(m\ge1\), set \(n=d+m\), extend \(f\) by all \(s+m\) dummy coordinates,

\[
F_m(x,y,v)=f(x),
\]

and obtain \(g_m\) by flipping exactly the \(K\) values at

\[
(z_1,0^m),\ldots,(z_K,0^m).
\]

Then every \(g_m\) is a genuine balanced Boolean function and, as \(m\to\infty\),

\[
\boxed{
H(g_m)-H(f)
=8K\,n\,2^{-n}+O_{f,Z}(2^{-n}),
}
\tag{2.2}
\]

\[
\boxed{
I(g_m)-I(f)
=2K\,n\,2^{-n}+O_{f,Z}(2^{-n}).
}
\tag{2.3}
\]

Consequently the denominator in (2.4) is positive for all sufficiently large \(m\), and

\[
\boxed{
\frac{H(g_m)-H(f)}{I(g_m)-I(f)}\longrightarrow4.
}
\tag{2.4}
\]

Equivalently, for every fixed \(C>4\),

\[
\boxed{
\begin{aligned}
&[C(I(g_m)-1)-H(g_m)]-[C(I(f)-1)-H(f)]\\
&\qquad=2K(C-4)n2^{-n}+O_{f,Z}(2^{-n})>0
\end{aligned}}
\tag{2.5}
\]

for all sufficiently large \(m\).

Thus a fixed finite balanced point-defect pattern cannot become a new high-dimensional obstruction merely by being diluted into more and more dummy coordinates.  At every balanced-uniform center \(C>4\), including \(C_*\), it eventually **increases** the available slack.

### Proof

Write a Fourier frequency as \((R,V)\), where \(R\subseteq[d]\) and \(V\subseteq[m]\).  Put

\[
a_j=f(x_j),
\qquad
A_R=\sum_{j=1}^K a_j\chi_R(z_j),
\qquad
\varepsilon_n=2^{1-n}.
\tag{2.6}
\]

Let \(b_R\) be the Fourier coefficient of the fixed \(d\)-variable dummy extension of \(f\).  The unmodified \(n\)-variable extension has coefficient \(b_R\) when \(V=\varnothing\) and zero otherwise.  Flipping point \((z_j,0^m)\) changes its value by \(-2a_j\), while every character on the final \(m\) coordinates equals \(+1\) there.  Hence, with **all signs retained**, the Fourier coefficients of the actual Boolean source are exactly

\[
\boxed{
\widehat g_m(R,V)
=b_R\mathbf1_{\{V=\varnothing\}}
-\varepsilon_n A_R.
}
\tag{2.7}
\]

This is the source-exact replacement for the special parity-hyperplane formula in the two-point peer theorem.

Now regard \(A_R\) as the unnormalised Walsh transform on \(\{0,1\}^d\) of the signed \(K\)-point function supported on the \(z_j\)'s with values \(a_j\).  Walsh Parseval gives

\[
\boxed{
\sum_R A_R^2=2^dK.
}
\tag{2.8}
\]

All frequencies with \(V\ne\varnothing\) are pure Fourier dust, with squared mass \(\varepsilon_n^2A_R^2\).  Their exact total mass is therefore

\[
\begin{aligned}
Q_m
&=(2^m-1)\varepsilon_n^2\sum_RA_R^2\\
&=\boxed{4K\,2^{-n}(1-2^{-m})}.
\end{aligned}
\tag{2.9}
\]

Let

\[
L_A=\sum_{R:A_R\ne0}A_R^2\log_2 A_R^2,
\qquad
D_A=\sum_R |R|A_R^2.
\]

These are constants depending only on the fixed finite pattern.  Since a nonzero dust atom has mass \(\varepsilon_n^2A_R^2\), its entropy is exact, not bounded by a support-size surrogate.  Summing gives

\[
\boxed{
H_{\rm dust}
=(2n-2)Q_m-(2^m-1)\varepsilon_n^2L_A.
}
\tag{2.10}
\]

Because \(L_A\) and \(\sum A_R^2=2^dK\) are fixed,

\[
H_{\rm dust}=2nQ_m+O_Z(Q_m).
\tag{2.11}
\]

The coordinate-label price is also exact.  Summing \(|R|+|V|\) over all nonempty \(V\)'s and using

\[
\sum_{V\subseteq[m]}|V|=m2^{m-1}
\]

gives

\[
\boxed{
I_{\rm dust}
=\varepsilon_n^2
\left[(2^m-1)D_A+m2^{m-1}2^dK\right].
}
\tag{2.12}
\]

Equivalently,

\[
I_{\rm dust}
=Q_m\left[
\frac{D_A}{2^dK}
+rac{m2^{m-1}}{2^m-1}
\right]
=\frac n2Q_m+O_Z(Q_m).
\tag{2.13}
\]

Thus no dummy-coordinate identity has been omitted: its full degree cost appears in the second term of (2.12).

It remains only to control the finite \(V=\varnothing\) interference slice.  There are exactly \(2^d\) such frequencies.  If \(b_R\ne0\), the entropy atom \(-u^2\log_2u^2\) is differentiable in a fixed neighbourhood of \(b_R\), so changing \(b_R\) by \(-\varepsilon_nA_R\) changes that atom by \(O_{f,Z}(\varepsilon_n)\).  If \(b_R=0\), the new atom contributes

\[
O_Z(n\varepsilon_n^2)=o(\varepsilon_n).
\]

After the fixed finite sum,

\[
\Delta H_{V=\varnothing}=O_{f,Z}(\varepsilon_n)=O_{f,Z}(Q_m).
\tag{2.14}
\]

Influence on the same slice is a fixed finite quadratic polynomial in the perturbed coefficients, hence

\[
\Delta I_{V=\varnothing}=O_{f,Z}(\varepsilon_n)=O_{f,Z}(Q_m).
\tag{2.15}
\]

Using (2.9), (2.11), (2.13), (2.14) and (2.15),

\[
\Delta H=2nQ_m+O(Q_m)
=8Kn2^{-n}+O(2^{-n}),
\]

\[
\Delta I=\frac n2Q_m+O(Q_m)
=2Kn2^{-n}+O(2^{-n}),
\]

which proves (2.2)--(2.4).  Subtracting the two expansions with coefficient \(C\) proves (2.5).  \(\square\)

## 3. Why this is a genuine extension of the peer theorem

The peer's two-point result has a particularly simple parity-hyperplane dust cloud with one common nonzero magnitude.  Theorem 2.1 allows simultaneously:

* any fixed even number \(K\) of sign-balanced flips;
* arbitrary geometry among those points on any fixed finite scaffold;
* collisions and cancellations in the Walsh amplitudes \(A_R\);
* arbitrary fixed balanced Boolean source \(f\), including a character;
* every coordinate-label contribution, exactly through (2.12).

The individual dust amplitudes need not be equal and may vanish.  Only signed Walsh Parseval (2.8) and the fixed-pattern hypothesis are used.  In particular, no non-Boolean probability relaxation, unsigned replacement, independence ansatz, or dropped negative-information term enters the argument.

For \(K=2\) and the peer's special pair geometry, the theorem recovers its leading terms
\(\Delta H/\Delta I\to4\).  The new content is that **four-point, six-point, or any other fixed finite balanced mutation has exactly the same universal leading slope**.

## 4. Application to the live all-gate candidate

On the balanced-uniform slice, the live candidate's defect is

\[
S_*(h):=C_*[I(h)-1]-H(h),
\qquad C_*=6.5218512>4.
\]

Theorem 2.1 gives

\[
S_*(g_m)-S_*(f)
=2K(C_*-4)n2^{-n}+O(2^{-n})>0
\tag{4.1}
\]

for all sufficiently large \(m\).

Therefore, if a fixed balanced core \(f\) is already \(C_*\)-safe, no counterexample to `LIMIT-PRIME-GATE-LIFT-v1` can be manufactured asymptotically by embedding a **uniformly bounded** number of balanced point flips into more dummy dimensions.  If the base core is unsafe, the base itself is already the obstruction and the sparse amplification was unnecessary.

This directly closes a whole version of the changed-support threat left open by the preceding fixed-support and radius-two results.  It does **not** cover perturbations whose number or intrinsic scaffold dimension grows with \(n\), positive-density changed supports, arbitrary off-centre product biases, or the universal composition-prime gate inequality.

## 5. Decisive computation / refutation attempt

`CHECKER.py` independently verifies the exact coefficient identity (2.7), signed-pattern Parseval (2.8), exact dust mass (2.9), and exact dust influence formula (2.12) using `Fraction` arithmetic.

It checks **22,806** exact small-source instances coming from **7,602** balance-preserving defect patterns: every balanced source through \(r\le3\), every opposite-sign two-point pattern on one additional scaffold bit, all four-point patterns for \(r\le2\), a deterministic forty-pattern four-point sample for every balanced \(r=3\) source, and \(m=1,2,3\).  Captured output is `PASS`.

The finite checker is implementation evidence only; Theorem 2.1 is the all-dimensional analytic proof above.

## 6. Exact old/new missing implications

**Old missing implication:** prove or refute

\[
D_{\Gamma_*}(P;p)\ge0
\]

for every composition-prime Boolean gate and every interior product bias.  The immediate adversarial subquestion after the fixed-support work was whether increasingly high-dimensional sparse changed-support constructions could create a new balanced obstruction.

**New proved inference:** every fixed finite sign-balanced point-defect pattern on a fixed finite scaffold has incremental entropy/influence slope exactly \(4\) under dummy dilution.  Hence for every \(C>4\), and in particular \(C_*\), it eventually increases rather than consumes balanced-uniform slack.

**Replacement obligations:** a surviving adversary must use at least one genuinely different mechanism: an unbounded/growing defect pattern or scaffold, a positive-density mutation, a different nonlocal shared-core interaction, or an off-centre product-bias violation.  A builder still owes the universal all-bias/all-arity prime-gate inequality.

**Next recipients:** fleet02/B17 should use this theorem to stop testing bounded-cardinality dummy-diluted support dust and move its adversary to growing-support/nonuniform mechanisms; fleet01/B17's newly closed full arity-five uniform slice can combine with it to focus five-input searches strictly off-centre; all-gate builders can treat bounded sparse dust as an asymptotically positive slack term rather than a threat.

**Implication to full FEI:** direct but partial.  One infinite Boolean adversary class is eliminated source-exactly, but the universal quantifier in (1.1) is still unpaid.  Full FEI remains **OPEN / NOT PROVED**.

Scoped privacy review: this report and checker contain only FEI mathematics, logical account/slot labels and source-bound repository paths.  No credentials, scheduler identifiers, machine paths, unrelated private transcripts, email/Drive action, paid/remote model invocation, workflows, or permission changes are included.

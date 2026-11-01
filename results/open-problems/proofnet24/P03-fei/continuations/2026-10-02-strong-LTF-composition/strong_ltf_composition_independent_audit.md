# Independent audit: strong LTF FEI and balanced composition

Date: 2026-10-02. Audited draft:
`strong_ltf_and_balanced_composition_candidate.md`, together with the
completed all-LTF split proof. I also independently checked the proposed
shorter near-dictator replacement.

**Internal verdict: PASS.** Both the draft's rare-tail/KL proof and the
simpler unate near-dictator argument establish the complementary split
estimate. The exact variance recursion and balanced disjoint composition
then give the stated strengthened result and depth-independent formula
closure. No novelty or external peer-review certification is supplied.

## 1. Short near-dictator argument, independent of halfspace geometry

For a monotone split \(f=A+zB\), one has
\(A\in\{-1,0,1\}\), \(B\in\{0,1\}\), \(B=1-A^2\).
Let \(\alpha=\mathbb EB\) and \(\delta=1-\alpha\).
For \(\alpha>1/2\), \(0\le\delta<1/2\). If \(\delta=0\),
then \(f=z\) and the split increment is zero.

Otherwise write the split-pair spectral law as
\(P_S=\widehat A(S)^2+\widehat B(S)^2\). Its empty atom satisfies
\(P_0\ge\alpha^2\), so the total mass of the nonempty atoms is at
most \(1-\alpha^2\le2\delta\). Their contribution to conditional
spectral-bit entropy is therefore at most \(2\delta\).

At the empty atom, put \(a=\mathbb EA\), \(b=\alpha\).
Since \(|a|\le\mathbb E|A|=\delta\) and \(a^2+b^2\le1\),
its conditional-entropy contribution is
\[
a^2\log_2\frac{a^2+b^2}{a^2}
+b^2\log_2\frac{a^2+b^2}{b^2}
\le2\delta^2\log_2(1/\delta)+\delta^2\log_2e.
\]
The first inequality uses that \(x\ln(1/x)\) increases for
\(0\le x\le\delta^2<1/4\); the second part uses
\(\ln(1+t)\le t\). Zero terms are taken by continuity.
Since
\[
2\delta\log_2(1/\delta)+\delta\log_2e
\le\frac{2\log_2e}{e}+\tfrac12\log_2e<1.783,
\]
the entire conditional entropy is less than \(3.783\delta\).
The already verified exact split identity gives
\(\Delta H\le2\mathcal C<8\delta\).

This argument actually applies to every unate split after the appropriate
coordinate and output sign changes. It requires neither a relative
halfspace noise estimate nor a new KL calculation. Combining it with
the established largest-weight bound \(\Delta H\le C_*\alpha\)
when \(\alpha\le1/2\) gives
\[
\Delta H\le C_{\rm strong}\alpha(1-\alpha),
\qquad C_{\rm strong}=2\max\{C_*,8\}.
\]
The completed all-LTF proof defines a much larger \(C_*\), so this is
also consistent with the candidate's \(2C_*\) coefficient.

## 2. The longer rare-tail proof also passes

For completeness, I checked the draft's alternate branch independently:

* The disjoint tail halfspaces obey \(A=U-D\), \(B=1-U-D\), with
  total rare density \(u+d=\delta\). Thus \(\mathbb EA^2=\delta\)
  and normalized \(A\)-spectrum has empty atom
  \((u-d)^2/\delta\le\delta\).
* Nonempty pair coefficients give
  \(P_S=2[\widehat U(S)^2+\widehat D(S)^2]\). KOS applied to
  \(2U-1\) or \(2D-1\) contributes the factor \(1/4\) in the
  indicator spectral tail, as stated. Zero-density tails vanish exactly.
* Hypercontractivity applies to the signed ternary function \(A\)
  through its norm: \(\|A\|_{3/2}^2=\delta^{4/3}\). This produces
  the asserted low-degree bound without assuming that \(A\) itself is
  an indicator.
* The displayed second derivative of
  \(t\sqrt{\ln(1/t)}\) is correct and negative. Jensen gives
  \(u\sqrt{\ln(1/u)}+d\sqrt{\ln(1/d)}
  \le\delta\sqrt{\ln(2/\delta)}\), and
  \(\ln(2/\delta)\le2\ln(1/\delta)\) for \(\delta\le1/2\).
  The resulting pair-tail constant fits the previously chosen
  \(\Gamma\), since its Keller–Klein constant was explicitly weakened
  to \(c\le1\).
* For degree thresholds below 1, the exact nonconstant mass is
  \(2[u(1-u)+d(1-d)]\le2\delta\), so there is no discarded empty
  atom or small-degree exception.
* In the generalized dyadic lemma, replacing the empty-atom probability
  \(\beta\le\eta\) by \(\eta\) decreases the displayed lower
  bound, since \(\log_2(1/\eta)\ge0\). The star correction and
  KL data-processing direction are correct. It supplies the same
  \(\Delta H\le C_*\delta\) bound claimed in the draft.

No error was found in this longer argument. The short argument in Section 1
provides a preferable proof because it removes the extra analytic inputs.

## 3. Exact strengthened induction

For a monotone split, the restricted means are
\(\mathbb EA\pm\alpha\). Direct subtraction gives
\[
V(f)-\tfrac12[V(f^+)+V(f^-)]=\alpha^2.
\]
The physical influence recursion is exact, so
\[
[I(f)-V(f)]-
\tfrac12[(I(f^+)-V(f^+))+(I(f^-)-V(f^-))]
=\alpha(1-\alpha).
\]
All restrictions remain LTFs. Sign changes preserve entropy, influence,
and variance; zero-weight coordinates can be removed. Constants have all
three quantities zero. The local estimate above therefore proves by
dimension induction
\[
H(f)\le C_{\rm strong}[I(f)-V(f)]
\]
for every LTF under the uniform cube measure.

The potential \(I-V\) is nonnegative by its exact spectral formula
\(\sum_{S\ne\varnothing}(|S|-1)\widehat f(S)^2\).
Its vanishing for dictators is compatible with zero dictator entropy.
There is no need to replace \(V\) by a bias-independent constant.

## 4. Exact balanced, disjoint composition

Let \(F=g(f_1,\ldots,f_m)\), with each child balanced and using a
disjoint input block. A selected child spectral set is always nonempty,
because its constant Fourier coefficient is zero. Hence the union of
selected child sets uniquely determines the outer spectral set and all
inner selected sets. Fourier expansion then gives a genuine injective
hierarchical spectral sampling rule, with no cancellation between
different outer sets.

Consequently the three identities in the draft are exact:
\[
H(F)=H(g)+\sum_i I_i(g)H(f_i),\qquad
I(F)=\sum_i I_i(g)I(f_i),\qquad V(F)=V(g).
\]
The last identity also follows from independence and balance of the child
outputs: they are uniform independent signs. In particular, the parent
gate is evaluated under uniform input, so no product-bias FEI theorem has
been assumed.

Since \(V(f_i)=1\), applying the same strong constant to the parent
and to every child yields
\[
H(F)\le C\left[I(g)-V(g)+
  \sum_i I_i(g)(I(f_i)-1)\right]=C[I(F)-V(F)].
\]
This cancellation uses \(\sum_i I_i(g)=I(g)\) and is exact. Recursive
application to a read-once LTF-gate formula therefore preserves one
constant independent of fan-in, number of gates, or depth, provided all
nonroot gate outputs are balanced. The root may have arbitrary output
bias. Leaves are balanced variables or their negatives, with
\(H=0\) and \(I=V=1\).

Shared inputs or unbalanced children invalidate the spectral sampling
argument as stated and are properly excluded. The composition conclusion
does not imply general Boolean FEI.

## 5. Independent finite checks

New checker: `independent_strong_ltf_check.py`.
Results: `independent_strong_ltf_checks.json`.

It checked 2,977 exact variance/influence recursions on monotone truth
tables through dimension 5, including 281 near-dictator unate splits.
The latter all obeyed the proposed 8\(\delta\) bound; the maximum observed
increment-to-\(\delta\) ratio was approximately 4.868. It also checked
five balanced disjoint LTF-gate compositions through 12 input variables,
including biased and signed-weight root gates. Influence and variance
identities used exact Fractions. Entropy identities used floating point,
with maximum error below \(10^{-15}\).

These checks are sanity checks rather than an asymptotic theorem
certificate. The analytic strengthened induction and exact composition
algebra above are what support the PASS verdict.

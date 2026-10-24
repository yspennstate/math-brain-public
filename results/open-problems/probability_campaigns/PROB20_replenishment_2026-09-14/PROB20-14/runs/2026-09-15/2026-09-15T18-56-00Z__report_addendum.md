# PROB20-14 — adversarial correction addendum to 2026-09-15T18:44:31Z report

**SOLUTION STATUS: PARTIAL (unchanged).**

This append-only addendum corrects two range/closure statements in the immediately preceding report. The new truncated-second-moment lemma, strengthened Palm inequality, and explicit denominator modulus remain valid with the range clarification below. The claimed conditional *full root closure* in Section 7 is retracted.

## 1. Range clarification for Lemma 4.1 / Theorem 5.1

Lemma 4.1 was stated for
\[
C_*N^{1/q}\le d=o(N),
\]
while Theorem 5.1 was stated through a sufficiently small fixed linear range \(d\le c_0N\). The proof of Lemma 4.1 in fact works uniformly on that small linear range as well: the only tail-mean requirement is
\[
\frac{N\,\mathbb E[Y;Y>\kappa d]}{d}
\le
C\frac{N}{d^q}\mathbb E[Y^q;Y>\kappa d]\to0,
\]
and for \(d\ge C_*N^{1/q}\) the factor \(N/d^q\) is uniformly bounded, while \(d\to\infty\). Thus, after choosing \(c_0>0\) small enough for the factorial-product argument, the valid range is
\[
\boxed{
C_*N^{1/q}\le d\le c_0N.
}
\]
Alternatively, restricting all uses to \(d=o(N)\) already suffices for the current conditioned-tree application because the earlier large-width theorem removes a sublinear upper cutoff. No mathematical conclusion of Sections 4–6 depends on the distinction.

## 2. Retraction of Section 7's full root-closure criterion

Section 7 proposed to take
\[
B_n=\left(\frac{n}{(\lambda_n+1)L_n}\right)^{1/q},
\qquad L_n\to\infty,
\]
and then apply Theorem 5.1 to every \(d\ge B_n\). This is not justified: when \(\lambda_n\) grows, \(B_n\) lies **below** the proven starting scale \(C_*n^{1/q}\) of Theorem 5.1. Thus the interval
\[
B_n<d<C_*n^{1/q}
\]
was not covered.

There is a second issue with the simplified condition (7.6). The monotone envelope
\[
\bar v_Y(x)=\sup_{y\ge x}y^{q-2}\mathbb E[Y^2;Y\le y]
\]
is nonincreasing in \(x\). Knowing its value at
\[
(n/(\lambda_n+1))^{1/q}
\]
does not automatically control it at the smaller argument obtained after division by \(L_n^{1/q}\). Therefore (7.6) does not imply (7.5) without an additional regularity assumption on the modulus.

Accordingly, **all claims in Section 7 that (7.5) or (7.6) by themselves prove full root UI are withdrawn.** They may be useful as ingredients only after the below-natural-scale gap is separately controlled.

## 3. Valid corollary retained from Theorem 5.1

Theorem 5.1 does give a clean, correct statement on and above the natural scale. For every fixed \(C_*>0\), if
\[
\boxed{
\lambda_n\,
\bar v_Y(c C_* n^{1/q})\to0,
}
\tag{A.1}
\]
then the strengthened Palm estimate implies
\[
\sup_{C_*n^{1/q}\le d\le c_0n}R_{n,d}=O(1).
\tag{A.2}
\]
Indeed, uniformly in this range,
\[
\frac{d^q}{n\,v_Y(cd)}
\ge
\frac{C_*^q}{\bar v_Y(cC_*n^{1/q})},
\]
which dominates \(\lambda_n\) under (A.1), while the first term in (5.1) is bounded by a constant (and actually decays once \(d\gg\sqrt n\)).

This controls the natural-and-larger part of the root window, but **does not by itself control degrees below \(C_*n^{1/q}\)**. Root UI therefore remains open even under (A.1) unless the lower interval is handled by another estimate.

## 4. A correct two-sided bridge formulation

A genuinely sufficient root criterion must provide an overlap between a low-window theorem and a Palm theorem. One valid formulation is:

find deterministic sequences \(B_n\to\infty\) and \(D_n\ge B_n\) such that

\[
B_n^q\frac{\lambda_n+1}{n}\to0,
\tag{A.3}
\]

so the entropy theorem controls \(d\le B_n\), and separately prove a Palm/local-ratio estimate uniformly for **all** \(d\ge B_n\) up to the existing large-width escape cutoff. The current Theorem 5.1 only supplies this latter estimate beginning at a fixed multiple of \(n^{1/q}\), not at arbitrary \(B_n=o(n^{1/q})\).

Equivalently, the next missing analytic step can be stated precisely as extending the truncated-second-moment Palm argument to a law-dependent scale
\[
b_n n^{1/q},\qquad b_n\downarrow0,
\]
far enough that it overlaps the entropy scale. For such an extension the tail-mean truncation must satisfy
\[
\boxed{
 b_n^{-q}
 \mathbb E[Y^q;Y>c b_n n^{1/q}]	o0,
}
\tag{A.4}
\]
and the resulting bad-event exponent must still dominate the central-atom cost. This is now the concrete bridge obligation.

## 5. Ledger correction

Retain as **proved** from the preceding report:

- Lemma 4.1, with the clarified small-linear upper range;
- the strengthened Palm bound
  \[
  R_{n,d}
  \le Ce^{-cd^2/n}
  +\exp\{\lambda_n-cd^q/(n v_Y(cd))\}
  \]
  for fixed-multiple natural-scale and larger \(d\) (through a small linear range);
- the necessary obstruction \(\lambda_n v_Y(cd)\gtrsim d^q/n\) for unbounded ratios in that range;
- the explicit central-atom modulus bound of Theorem 6.1.

Retract from the **conditional closure** ledger the statement that conditions (7.5) or (7.6) alone settle root UI. The full root case and hence the full every-fixed-level problem remain open.

## 6. Next attack after correction

The next proof target is now sharper: extend the Palm truncation to \(d=b_n n^{1/q}\) with \(b_n\downarrow0\) chosen from the actual \(q\)-moment tail, and determine whether the explicit denominator modulus from Theorem 6.1 forces enough overlap with the entropy low window. If universal overlap fails, the same inequalities should guide a lacunary construction by specifying exactly how slowly the tail/truncated-variance modulus would have to decay relative to \(\lambda_n\).

This correction was generated by adversarial self-review immediately after archiving the main report. It narrows a conditional claim and does not promote any numerical evidence to proof.

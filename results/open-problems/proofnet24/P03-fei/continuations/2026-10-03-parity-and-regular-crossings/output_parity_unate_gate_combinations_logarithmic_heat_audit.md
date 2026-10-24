# Independent audit: logarithmic FEI for parity outputs of unate-gate combinations

Audit date: 2026-10-03. Auditor: `/root/heat_entropy`.

**Verdict: analytic PASS.** I read the complete new
[proof](output_parity_unate_gate_combinations_logarithmic_proof.md) and its
[author checker](verify_output_parity_unate_gate_combinations_logarithmic.py).
I independently reconstructed the nonempty-law Gibbs calculation, the
empty-atom bound, the two parity regimes, and the shared-input unate-gate
norm estimate. I found no missing hypothesis or factor. This is an internal
mathematical audit, not an external review or a historical novelty verdict.
The ordinary full Boolean Fourier entropy–influence conjecture remains open.
The older quadratic proof and other stable files were not modified.

## Precise audited statement

All inputs are uniform on the Boolean cube, all entropies use base-two
logarithms, and physical influence is the probability that flipping a bit
changes the output. For a Boolean function (g), let

\[
 \rho(g)=\left(\sum_i I_i(g)^2\right)^{1/2}.
\]

For (M\ge\max\{1,\rho(g)\}\), every (T\subseteq[n]\), and

\[
 h=\chi_Tg,\quad \ell=|T|,\quad q=n-\ell,
\]

the proof establishes

\[
 H(h)=H(g)\le[\log_2(4M^2+2q)+3]I(h).                 \tag{A}
\]

In particular, if (g=F(g_1,\ldots,g_m)) is an arbitrary Boolean
combination of (m\ge1) unate gates on shared inputs, with orientations
allowed to differ between gates, then (M=m) is valid. Full output parity
gives the dimension-independent constant (2\log_2m+5). Removing constant
gates improves the usable (m); if none remain then (g) is constant and
the character output has entropy zero. The maximum with 1 is needed in the
general norm formulation, and is explicitly present in the proof.

## Nonempty Fourier-law calculation

For (n\ge1) and nonconstant (f), write (v=\operatorname{Var}(f)>0)
and (P(S)=\widehat f(S)^2). Parseval gives a probability distribution,
whose empty atom has mass (1-v). Its conditional nonempty law is

\[
 P_+(S)=P(S)/v \quad(S\ne\varnothing).
\]

The reference measure in the new proof is normalized over **all** nonempty
subsets, including subsets outside the support of (P_+):

\[
 Q(S)=n^{-|S|}/Z_n,
 \qquad Z_n=\sum_{S\ne\varnothing}n^{-|S|}
          =(1+1/n)^n-1.
\]

The degree-one terms already sum to 1, and

\[
 1\le Z_n<e-1<2.
\]

Thus (Q) is strictly positive, so the relative entropy is defined without
any support qualification. The exact identity is

\[
 D(P_+\Vert Q)
 =-H(P_+)+\mathbb E_{P_+}|S|\log_2n+\log_2Z_n\ge0.
\]

Since (v\mathbb E_{P_+}|S|=I(f)), retaining the empty atom gives

\[
 H(f)=h_2(v)+vH(P_+)
 \le h_2(v)+I(f)\log_2n+v\log_2Z_n.                 \tag{B}
\]

There is no extra variance denominator in (B), no additive constant
independent of influence, and no use of a Gibbs law on the entire cube
that would lose control of a very small nonempty mass. When (n=1), the
nonempty reference law has one atom and (Z_1=1); the formula still holds.
For (v=0), no conditional law is introduced and entropy is zero.

## Empty-atom entropy and influence normalization

Let (r\le1/2) be the minority output probability. Then

\[
 v=4r(1-r),\qquad I(f)\ge2r\log_2(1/r).             \tag{C}
\]

The proof supplies a correct self-contained induction for the classical
cube edge-isoperimetric inequality underlying (C). If an event has size
(a=a_0+a_1), (a_0\le a_1), then induction yields internal boundary

\[
 a\log_2(2^{n-1}/a)+a h_2(a_0/a).
\]

The crossing boundary is at least (a_1-a_0). Concavity on
([0,1/2]) gives (h_2(u)\ge2u), so the total is at least
(a\log_2(2^n/a)). Empty sections are interpreted by continuity; the
zero-dimensional base is valid. Each undirected boundary edge is counted
twice in the physical-influence numerator, yielding exactly (C).

The binary entropy estimate used in the new proof is also correct:

\[
 h_2(v)\le4r\log_2(1/r)\le2I(f).                   \tag{D}
\]

For (0<r\le1/4), the elementary inequality
(h_2(x)\le x[\log_2(1/x)+\log_2 e]) gives

\[
 h_2(v)\le v\left[\log_2(1/r)
                     +\log_2\frac e{4(1-r)}\right]
           \le4r\log_2(1/r),
\]

because (4(1-r)\ge3>e). For (1/4\le r\le1/2), use
(h_2(v)\le1\le4r\le4r\log_2(1/r)). This includes (v=1).
Constants have both sides zero. Finally Fourier Poincare is
(v\le I(f)), since nonempty Fourier indices have degree at least one.
Combining (B), (D), and (\log_2Z_n<1) gives

\[
 H(f)\le(\log_2 n+3)I(f).                         \tag{E}
\]

The proof therefore handles heavily biased functions without assuming
influence bounded away from zero.

## Parity and the two dimension regimes

Fourier multiplication by a character translates indices by symmetric
difference, and physically complements pivotality precisely on coordinates
in (T). Consequently

\[
 H(h)=H(g),\qquad
 I(h)=\ell+\sum_{i\notin T}I_i(g)-\sum_{i\in T}I_i(g)
      \ge\ell-M\sqrt\ell.                         \tag{F}
\]

If (\ell\ge\max\{4M^2,q\}), then (I(h)\ge\ell/2>0) and
(n=\ell+q\le2\ell). A law on (2^n) points has entropy at most
(n), so (H(h)\le4I(h)).

In the other regime,

\[
 n=\ell+q<q+\max\{4M^2,q\}\le4M^2+2q.
\]

Applying (E) to (h) yields (A). Since (M\ge1), the constant in (A)
is at least 5, which also covers the first regime. The threshold comparisons
involve real (M) and integer (\ell); no rounding was assumed. For
(n=0), or any constant (h), the conclusion follows from entropy zero
before dividing by influence. When (q=0), the constant simplifies exactly
to (2\log_2M+5). For (T=\varnothing), (q=n); this is a logarithmic
dimension bound, not a dimension-independent ordinary FEI theorem.

## Unate gates with shared inputs

For each gate separately, coordinate orientation gives

\[
 |\widehat g_j(\{i\})|=I_i(g_j),
 \qquad \sum_i I_i(g_j)^2\le\operatorname{Var}(g_j).
\]

These identities follow by conditioning on all coordinates except (i);
an oriented unate derivative has a fixed sign. The signs may differ among
gates and cause no difficulty because only their squared magnitudes enter.
If the outer function changes on an edge, at least one gate changed there,
so

\[
 I_i(g)\le\sum_j I_i(g_j).
\]

Coordinatewise nonnegativity and the Euclidean triangle inequality give

\[
 \rho(g)\le\sum_j\rho(g_j)
          \le\sum_j\sqrt{\operatorname{Var}(g_j)}\le m.
\]

No independence, disjointness, or common orientation of the gates is used.
The refined norm bound with the maximum with 1 is valid as stated. For a
single unate gate under full parity, a previously proved constant 2 is
sharper than the logarithmic statement's constant 5; the new bound does not
invalidate or replace that sharper separate fact.

## Prior work and independent checks

I reopened the primary
[Wan–Wright–Wu manuscript](https://arxiv.org/pdf/1312.3003).
Section 1.1, printed page 4, explicitly discusses the weak logarithmic
Fourier entropy bound, and Lemma 1.5/Appendix B control the empty atom at a
cost of (2I(f)). The candidate's prior-credit paragraph is accurate.
Its elementary Gibbs derivation of (E) is a transparent variant of a known
type of bound; it must not be presented as a new general FEI theorem.
The primary [Shalev manuscript](https://arxiv.org/pdf/1806.03646),
printed page 3, also identifies logarithmic weak FEI as folklore. I did not
verify historical priority of the particular parity-output consequence (A).

The separate independent implementation is
[verify_output_parity_logarithmic_heat.py](verify_output_parity_logarithmic_heat.py),
with [report](output_parity_logarithmic_heat_checks.json). It imports no
author helper. It checks integer Walsh Parseval, degree energy, physical
parity influence complement, integer isoperimetry, exact Fraction Gibbs
normalization, direct conditional relative entropy, and gate-specific Chow
identities/flip-union on genuinely shared-input examples. Entropy and KL
comparisons are explicitly numerical supplements. The checker also tests
the real-(M) dimension regimes and arbitrary nonempty probability laws;
those tests are not a substitute for the proof above.

The independent checker completed successfully: 698 functions, 4,366
character-output pairs and exact isoperimetric checks, 4,296 direct
conditional-KL calculations, 12 exact reference normalizations, 120
arbitrary nonempty Gibbs-law tests, 96 combinations of 240 shared-input
unate gates, and 49,446 dimension-regime comparisons. Maximum observed
KL identity discrepancy was approximately \(1.07\times10^{-14}\).

**Conclusion:** the new logarithmic bound and its stated restricted scope
are analytically valid under the uniform Boolean input measure. No claim
of ordinary FEI for arbitrary shared-input gate compositions, arbitrary
nearby three-crossing score functions, nonuniform product measures, or all
Boolean functions follows from this result.

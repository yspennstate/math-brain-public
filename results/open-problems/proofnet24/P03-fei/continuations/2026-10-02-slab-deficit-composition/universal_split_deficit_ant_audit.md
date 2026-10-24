# Independent audit: universal split deficit and balanced slab composition

Date: 2026-10-02. Auditor: independent `antivoter_audit` agent.

**Verdict: PASS as a mathematical implication.** I read the complete
`universal_split_deficit_and_slab_composition_candidate.md`, rederived its
entropy and budget identities independently, and checked all Boolean
functions through four variables. No gap was found in the stated generic
conversion or balanced composition argument. The application to parallel
slabs uses the separately audited local slab theorem as an input. This
audit does not certify novelty or external peer review, and it does not
establish FEI for every Boolean function.

No author proof or previously published file was modified.

## 1. Exact Boolean identities, including signed derivatives

Use functions with values in \(\{-1,1\}\), uniform independent sign
inputs, and base-2 spectral entropy. For a coordinate split put
\(A=(f^++f^-)/2\), \(B=(f^+-f^-)/2\). Pointwise
\(A,B\in\{-1,0,1\}\), \(AB=0\), and \(A^2+B^2=1\).
With
\[
 \alpha=\mathbb EB^2,
 \quad\beta=\mathbb EB,
 \quad\delta=1-\alpha,
 \quad\nu=\alpha-\beta^2,
\]
one has
\[
 |\beta|\le\mathbb E|B|=\alpha,
 \qquad |\mathbb EA|\le\mathbb E|A|=\delta,
 \qquad \nu\ge\alpha(1-\alpha).
\]
No monotonicity or fixed sign of \(B\) is used.

Writing \(a=\mathbb EA\), the restricted means are \(a+\beta\)
and \(a-\beta\). Thus
\[
 \operatorname{Var}(f)
 -\frac{\operatorname{Var}(f^+)+\operatorname{Var}(f^-)}2
 =\beta^2.
\]
The influence of the splitting coordinate is exactly \(\alpha\).
All other coordinate influences average over the two restrictions, so
\[
 I(f)-\frac{I(f^+)+I(f^-)}2=\alpha.
\]
Consequently the exact decrement of \(I-\operatorname{Var}\) is
\(\nu\), for every Boolean split.

## 2. Universal entropy comparison

For a Fourier pair \(a_S=\widehat A(S)\),
\(b_S=\widehat B(S)\), put
\(P_S=a_S^2+b_S^2\), \(q_S=b_S^2/P_S\), and
\(r_S=(a_S+b_S)^2/(2P_S)\), omitting zero-mass pairs. Direct expansion
of the full and restricted spectra gives
\[
 \Delta_z H(f)=\sum_S P_S[1+h_2(q_S)-h_2(r_S)].
\]
This expression holds for either sign of every coefficient. Since
\(r_S(1-r_S)=(1-2q_S)^2/4\), the elementary binary entropy inequality
\(h_2(t)\ge4t(1-t)\) gives
\[
 1-h_2(r_S)\le4q_S(1-q_S)\le h_2(q_S).
\]
Therefore, with \(\mathcal C=\sum_S P_Sh_2(q_S)\),
\(\Delta_zH(f)\le2\mathcal C\). The candidate's power-series proof of
the binary inequality is correct, including its endpoint limits.

## 3. High-influence branch and all exceptional cases

Suppose \(\alpha>1/2\). If \(\alpha=1\), then \(A=0\) and
\(f=zB\), with arbitrary Boolean \(B\). Appending the coordinate to
every Fourier support preserves entropy; the restrictions \(\pm B\)
have that same entropy. Thus \(\Delta H=0\), even when \(B\) is
nonconstant or \(\beta=0\).

Otherwise \(0<\delta<1/2\). The empty pair has mass
\(P_0=a^2+\beta^2\). The entropy from nonempty pairs is at most
their total mass, hence
\[
 \mathcal C_{\ne\varnothing}\le1-P_0
 \le1-\beta^2=\nu+\delta.
\]
The empty-pair entropy is
\[
 E_0=a^2\log_2\frac{P_0}{a^2}
      +\beta^2\log_2\frac{P_0}{\beta^2}.
\]
Using \(P_0\le1\), \(\ln(1+t)\le t\), and
\(|a|\le\delta\),
\[
 E_0\le a^2\log_2(1/a^2)+a^2\log_2e
 \le2\delta^2\log_2(1/\delta)+\delta^2\log_2e
 <2\delta.
\]
The monotonicity needed in the second step holds on
\([0,\delta^2]\subset[0,1/4]\). The final numerical bound follows from
\[
 2\delta\log_2(1/\delta)+\delta\log_2e
 \le \frac{2\log_2e}{e}+\frac{\log_2e}{2}<2.
\]
If \(a=0\) or \(\beta=0\), the zero summands are interpreted by
continuity; if both vanish the entire empty pair is omitted. In
particular, \(\beta=0\) causes no division-by-zero or logical gap.

Combining the estimates and \(\nu\ge\alpha\delta>\delta/2\),
\[
 \mathcal C\le\nu+3\delta\le7\nu,
 \qquad \Delta_zH(f)\le14\nu.
\]
This branch is universal. The constant 14 is valid and is not asserted
to be optimal.

## 4. Low influence and restriction induction

For \(\alpha\le1/2\), the hypothesized local estimate
\(\Delta H\le C\alpha\), with a nonnegative class-wide constant
\(C\), implies
\(\Delta H\le2C\nu\), because \(\nu\ge\alpha/2\).
At \(\alpha=0\), \(B=0\), the restrictions coincide, and both
\(\Delta H\) and \(\nu\) vanish. The equality case \(\alpha=1/2\)
is covered by this branch.

Hence any such chosen pivot satisfies
\[
 \Delta H\le K\nu,
 \qquad K=\max\{2C,14\}.
\]
If a Boolean class is restriction closed and every nonconstant function
has a pivot satisfying the same local premise, induction on the number
of variables gives
\[
 H(f)\le K[I(f)-\operatorname{Var}(f)].
\]
The constant-function base case has both sides zero. Irrelevant pivots
also have zero entropy and budget increments, so they can be removed.
The induction uses the local premise at every restriction, rather than
deducing that premise from an ordinary FEI inequality.

For the stated parallel-slab application, interval gates and their
complements remain interval gates after restrictions. The separately
audited local theorem supplies one uniform \(C_{\rm slab}\). The
strict-separated \(m\)-crossing class also preserves its separation
condition under restrictions; its fixed-\(m\) constant yields the same
conversion with \(K_m=\max\{2C_m,14\}\). No new assertion about the
local theorem's novelty is made here.

## 5. Balanced disjoint composition

Let \(F=g(f_1,\ldots,f_m)\), with balanced children on disjoint
blocks. Each child has zero empty Fourier coefficient. Thus any final
nonempty block support uniquely determines which child blocks were
selected in the outer Fourier monomial; no distinct selected-block
patterns contribute to the same final coefficient. This justifies the
exact spectral entropy and degree identities
\[
 H(F)=H(g)+\sum_i I_i(g)H(f_i),
 \qquad I(F)=\sum_i I_i(g)I(f_i).
\]
Independent balanced child outputs are independent uniform signs, so
\(\operatorname{Var}(F)=\operatorname{Var}(g)\) and
\(\operatorname{Var}(f_i)=1\). If the outer gate and children satisfy
the strong bound with one constant \(K\), then
\[
\begin{aligned}
 H(F)&\le K\left[I(g)-\operatorname{Var}(g)
          +\sum_i I_i(g)(I(f_i)-1)\right]\\
     &=K[I(F)-\operatorname{Var}(F)].
\end{aligned}
\]
The cancellation of \(I(g)=\sum_i I_i(g)\) is exact, so there is no
depth or fan-in inflation. Restriction closure is needed to establish
the initial strong gate bound; the composed function need not itself
remain in the original class.

Read-once formulas with balanced nonroot outputs and arbitrary slab
gates therefore satisfy the same constant, by induction from sign
leaves. The root may be biased. Shared inputs or arbitrary biased
children are outside these hypotheses. The composition framework is
already established by O'Donnell–Tan (2013); the candidate appropriately
does not claim it as a new composition theorem.

## 6. Independent exhaustive check

The new checker `independent_universal_split_check.py` enumerates every
Boolean function through \(n=4\), including constants, and every pivot.
Its report is `independent_universal_split_checks.json`.

- 65,814 functions and 262,948 splits were checked.
- 95,482 splits have \(\alpha>1/2\), including 9,262 with
  \(\beta=0\).
- 1,082 splits have \(\alpha=1\); 1,062 of these have nonconstant
  signed \(B\). Their entropy increment is zero.
- Integer Walsh numerators verify both budget identities and all mean
  and \(\nu\) bounds exactly.
- Floating entropy checks verify \(\Delta H\le2\mathcal C\),
  \(\Delta H\le14\nu\) in the high-influence branch, and the two
  component entropy bounds, with tolerance \(2\times10^{-11}\).
- The maximum observed high-influence \(\Delta H/\nu\) is
  7.424951349510073; the maximum observed empty-pair entropy divided by
  \(\delta\) is 1.1811669518817753.

These computations support the independent analytic proof; the finite
enumeration and floating logarithms do not prove the general theorem.
The low-influence local premise remains essential. In particular, this
conversion does not repair the three-crossing prescribed-pivot
obstruction or establish general Boolean FEI.

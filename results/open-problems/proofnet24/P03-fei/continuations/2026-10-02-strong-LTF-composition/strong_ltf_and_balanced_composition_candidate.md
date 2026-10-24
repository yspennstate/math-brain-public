# Candidate strengthened LTF entropy bound and balanced composition closure

Date: 2026-10-02. **Candidate proof, awaiting independent audit.**
This continuation is separate from the archived all-LTF proof. It proposes
a strictly stronger estimate and a formula corollary with a constant
independent of depth, size, and fan-in. No novelty is certified here.

All measures are uniform on independent input signs; entropy and KL use
base-2 logarithms. For a Boolean function let
\[
 H(f)=\sum_S\widehat f(S)^2\log_2(1/\widehat f(S)^2),\quad
 I(f)=\sum_S|S|\widehat f(S)^2,\quad
 V(f)=\operatorname{Var}(f)=1-(\mathbb Ef)^2.
\]
Thus \(I(f)-V(f)=\sum_{S\ne\varnothing}(|S|-1)\widehat f(S)^2\ge0\).

Let \(C_*\) be the universal constant defined in the completed
[all-LTF proof](../2026-10-02-largest-weight/largest_weight_ltf_fei_proof.md), using its constants
\(A_0,\Gamma,C_-,C_D\), with \(C_*=2(C_D+\log_2e)\).

## 1. Proposed strengthened theorem

Every Boolean LTF under uniform input satisfies
\[
 \boxed{H(f)\le C_+\,[I(f)-V(f)],\qquad C_+=2C_*.}
\tag{S}
\]
More precisely, for a largest absolute input-weight coordinate, write
\(f=A+zB\), and let \(\alpha=I_z(f)\). The proposed local estimate is
\[
 \Delta_zH(f)\le C_+\alpha(1-\alpha).
\tag{L}
\]
As in the all-LTF proof, delete zero weights, flip signs to make the LTF
monotone, and perturb its threshold inside a finite score gap. Neither
entropy, influence, variance, nor the split increment changes. If there
are no nonzero weights the function is constant. If \(\alpha=0\) then the
restrictions coincide and the increment is zero.

## 2. A reusable spectral separation lemma

The dyadic argument in Section 5 of the all-LTF proof works with an
inequality for the zero atom, rather than exact equality. Here is the
precise version used below. Suppose \(P,Q\) are probability laws on
subsets of a finite coordinate set, with degree \(K\), and for some
\(0<\eta\le1\), \(M\ge1\), and the same \(\Gamma\) as above,
\[
 \begin{gathered}
 P_S\ge\eta Q_S,\qquad Q(K=0)\le\eta,\\
 Q(K\le k)\le18\sqrt{k/M}\quad(k\ge1),\\
 P(K\ge t)\le\Gamma\eta\sqrt{M/t}\quad(t>0).
 \end{gathered}
\tag{D1}
\]
Then
\[
 D(Q\|P)\ge\log_2(1/\eta)-C_D.
\tag{D2}
\]

To verify this extension, keep degree zero as a special atom \(\star\) and
for positive degree set \(J=\lfloor\log_2(K/M)\rfloor\). The bin laws have
\(P_j\le\Gamma\eta2^{-j/2}\), and for \(j<0\),
\(Q_j\le18\sqrt2\,2^{j/2}\). Therefore
\(\mathbb E_Q[|J|\mathbf1_{J<0}]\le C_-\). Use the reference law
\[
 R^{\rm ref}_\star=\tfrac12,\qquad
 R^{\rm ref}_j=2^{-|j|/4}/(2Z),\qquad
 Z=\sum_{j\in\mathbb Z}2^{-|j|/4}.
\]
Let \(\beta=Q_\star\le\eta\). Nonnegativity of
\(D(Q^{\rm bin}\|R^{\rm ref})\) yields
\[
 D(Q^{\rm bin}\|P^{\rm bin})
 \ge(1-\beta)\log_2(1/\eta)-\log_2(2Z\Gamma)
       -\tfrac34C_- -\beta.
\]
Because \(\log_2(1/\eta)\ge0\), this is at least the same expression
with \(\beta\) replaced by \(\eta\). Now
\(\eta\log_2(1/\eta)\le(\log_2e)/e\), \(\eta\le1\), and
KL data processing gives (D2). Every law has finite support, so all
expressions are finite with the usual omitted zero-mass summands.

If a split-pair spectrum is \(P_S=a_S^2+b_S^2\), and either one
component's squared mass is \(\eta\), normalize that component to \(Q\).
The conditional entropy \(\mathcal C\) of which component is selected
satisfies
\[
 \mathcal C
 \le\eta\,[\log_2(1/\eta)-D(Q\|P)+\log_2e]
 \le\eta(C_D+\log_2e).
\tag{D3}
\]
The first component contributes the exact KL expression; the other
contributes at most \(\eta\log_2e\) by \(\ln(1+t)\le t\). The exact
split identity gives \(\Delta H\le2\mathcal C\), independently of the
signs of \(a_S,b_S\). Thus (D1) implies \(\Delta H\le C_*\eta\).

## 3. The near-dictator branch \(\alpha>1/2\)

Put \(\delta=1-\alpha\). If \(\delta=0\), then the monotone pivotal
indicator \(B\) is identically 1 and \(A=0\), so \(f=z\),
\(H(f)=0\), and \(\Delta H=0\). Hence assume \(0<\delta<1/2\).
Let \(s(x)=\sum_j a_jx_j\) and let \(w\) be the pivot weight. Define
the two disjoint tail halfspaces
\[
 U=\mathbf1\{s>\theta+w\},\qquad
 D=\mathbf1\{s<\theta-w\}.
\]
The gap perturbation removes all endpoint ties. Directly from the two
restricted outputs,
\[
 A=U-D,\qquad B=1-U-D.
\tag{N1}
\]
Write \(u=\mathbb EU\), \(d=\mathbb ED\). Then
\(u+d=\delta\), \(\mathbb EA=u-d\), and \(\mathbb EA^2=\delta\).
In particular both tail densities are at most \(\delta<1/2\).

Normalize the other component of the split spectrum:
\[
 P_S=\widehat A(S)^2+\widehat B(S)^2,
 \qquad Q_S=\widehat A(S)^2/\delta.
\tag{N2}
\]
These are probability laws, \(P_S\ge\delta Q_S\), and
\[
 Q(K=0)=\frac{(u-d)^2}{\delta}\le\delta.
\tag{N3}
\]

### Low-degree mass

Since \(|A|\) is an indicator of density \(\delta\), hypercontractivity
gives \(\operatorname{Stab}_{1/2}(A)\le\|A\|_{3/2}^2=\delta^{4/3}\).
Consequently, for real \(k\ge1\),
\[
 Q(K\le k)\le2^k\delta^{1/3}.
\tag{N4}
\]
Put \(L_\delta=\ln(1/\delta)>\ln2\), \(M_\delta=\max\{1,L_\delta\}\).
For \(1\le k\le L_\delta/(12\ln2)\), (N4) is at most
\(e^{-L_\delta/4}\le1.5\sqrt{k/L_\delta}\); the weaker
\(e^{-L_\delta/12}\) bound suffices as in the all-LTF proof.
For \(k>L_\delta/(12\ln2)\), the trivial bound 1 is at most
\(3\sqrt{k/L_\delta}\). Thus
\[
 Q(K\le k)\le18\sqrt{k/M_\delta}\quad(k\ge1).
\tag{N5}
\]
If \(M_\delta=1\), use the trivial bound; otherwise use the derived
\(3\sqrt{k/L_\delta}\) bound. No interval concentration or influence
lower bound is needed in this branch.

### Pair-spectrum tail

For every nonempty subset, the constant term in (N1) disappears, and
\[
 P_S=(\widehat U(S)-\widehat D(S))^2
       +(\widehat U(S)+\widehat D(S))^2
     =2[\widehat U(S)^2+\widehat D(S)^2].
\tag{N6}
\]
For an indicator halfspace \(h\) of density \(t\le1/2\), KOS Theorem 18
applied to \(2h-1\), together with the noise-tail argument, gives for
\(k\ge1\)
\[
 \sum_{|S|\ge k}\widehat h(S)^2
 \le\frac{A_0}{4}t\sqrt{\ln(1/t)/k}.
\tag{N7}
\]
Indeed the nonconstant coefficients of \(2h-1\) are twice those of \(h\),
accounting for the factor 4. A zero-density halfspace has zero spectrum;
use \(0\sqrt{\ln(1/0)}=0\) by continuous extension.

The function \(\psi(t)=t\sqrt{\ln(1/t)}\) is concave on \((0,1)\), since
\[
 \psi''(t)=-\frac{2\ln(1/t)+1}{4t[\ln(1/t)]^{3/2}}<0.
\]
Jensen and \(u+d=\delta\) give
\[
 \psi(u)+\psi(d)\le\delta\sqrt{\ln(2/\delta)}
 \le\sqrt2\delta\sqrt{L_\delta}.
\]
Combining this with (N6)–(N7), for \(k\ge1\),
\[
 P(K\ge k)\le(A_0/\sqrt2)\delta\sqrt{L_\delta/k}
 \le A_0\delta\sqrt{M_\delta/k}.
\tag{N8}
\]
For \(0<k<1\), the nonconstant pair mass is
\[
 2[u(1-u)+d(1-d)]\le2\delta
 \le A_0\delta\sqrt{M_\delta/k}.
\]
Thus (N8) holds for every real \(k>0\). Since \(c\le1\), the constant
\(\Gamma=\max\{1,\sqrt2A_0/c\}\) of the completed proof is at least
\(A_0\). Equations (N2), (N3), (N5), and (N8) verify all hypotheses
of (D1), with \(\eta=\delta\). Hence
\[
 \Delta_zH(f)\le C_*\delta=C_*(1-\alpha).
\tag{N9}
\]

## 4. Local and global strengthening

The completed all-LTF theorem gives \(\Delta H\le C_*\alpha\) when
\(\alpha\le1/2\). Since \(1-\alpha\ge1/2\) in this case, this is at
most \(2C_*\alpha(1-\alpha)\). For \(\alpha>1/2\), (N9) is at most
\(2C_*\alpha(1-\alpha)\). This proves proposed (L) in all cases.

For a monotone LTF, \(\mathbb EB=\alpha\). The two restricted means are
\(\mathbb EA\pm\mathbb EB\). Therefore
\[
 V(f)-\tfrac12[V(f^+)+V(f^-)]
 =(\mathbb EB)^2=\alpha^2.
\tag{V}
\]
Together with the exact influence split,
\[
 [I(f)-V(f)]-\tfrac12[(I(f^+)-V(f^+))+(I(f^-)-V(f^-))]
 =\alpha-\alpha^2.
\]
Induct over dimension, applying (L) and (V). Constants have zero entropy,
influence, and variance. Each restriction is an LTF; sign and output flips
preserve the potential \(I-V\). The induction gives proposed (S), with
the same \(C_+=2C_*\) in every dimension and for every bias.

## 5. Exact balanced composition closure

Suppose \(g:\{-1,1\}^m\to\{-1,1\}\), and \(f_i\) are Boolean
functions on pairwise disjoint coordinate blocks, all balanced:
\(\mathbb Ef_i=0\). Let \(F=g(f_1,\ldots,f_m)\).
Assume each of \(g,f_1,\ldots,f_m\) satisfies
\(H(h)\le C[I(h)-V(h)]\) with the same \(C\). Then so does \(F\).

Here is a direct proof without a biased-input FEI assumption. Draw an outer
spectral set \(T\) with probability \(\widehat g(T)^2\). For each
\(i\in T\), independently draw a spectral set \(S_i\) with probability
\(\widehat f_i(S_i)^2\). Because \(f_i\) is balanced, each selected
\(S_i\) is nonempty. The union of the selected sets has exactly the
spectral law of \(F\). Expanding the Fourier polynomial verifies this;
different outer sets cannot produce the same subset because its nonempty
blocks recover \(T\). Hence
\[
 \begin{aligned}
 H(F)&=H(g)+\sum_i I_i(g)H(f_i),\\
 I(F)&=\sum_i I_i(g)I(f_i),\\
 V(F)&=V(g).
 \end{aligned}
\tag{C}
\]
The last equality follows because the disjoint balanced outputs are
independent uniform signs. Since \(V(f_i)=1\) and
\(\sum_i I_i(g)=I(g)\), the hypotheses and (C) give
\[
 \begin{aligned}
 H(F)&\le C\left[I(g)-V(g)+\sum_i I_i(g)(I(f_i)-1)\right]\\
 &=C[I(F)-V(F)].
 \end{aligned}
\]

Consequently, if the strengthened theorem is correct, every read-once
formula on independent input bits whose gates are LTFs and whose nonroot
gate outputs are balanced satisfies (S), with the same universal \(C_+\).
The root may have arbitrary output bias. Gate fan-in, formula depth, size,
weights, and thresholds are unrestricted. Leaves are balanced variables or
their negatives and satisfy \(H=0\), \(I=V=1\), starting the induction.
Disjoint input blocks are essential; arbitrary circuits with shared inputs
are not covered. Balanced child outputs are also essential to this proof;
unbalanced children would induce a nonuniform product law at the parent.

## 6. Audit priorities and scope

Check the rare-tail indicator normalization in (N7), the concavity inequality
and small-degree regime in (N8), the zero atom inequality in (N3), the
modified dyadic star calculation in (D2), and the exact variance split (V).
The composition proof uses only balanced disjoint children and never assumes
an input-biased FEI theorem. This is a theorem stronger than ordinary FEI for
LTFs if all steps pass, but still does not settle general Boolean FEI.
The finite-crossing/stripe problem is being pursued separately; the
largest-weight split theorem is obstructed already at three crossings.

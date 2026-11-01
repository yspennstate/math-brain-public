# FEI for parallel slabs, and for separated finite crossings

Date: 2026-10-02. **Candidate proof; independent analytic audit requested.**

This note extends the internally audited proof in
[the all-LTF proof](../2026-10-02-largest-weight/largest_weight_ltf_fei_proof.md). The proposed complete result is FEI for
every Boolean indicator/complement of a single interval in one linear form,
with arbitrary weights and endpoints. The more general result covers any
fixed number of crossings when the crossing points are separated by
strictly more than twice the largest input weight. No result is claimed for three or
more arbitrarily spaced crossings.

All entropies and KL divergences use base-2 logarithms. Natural logarithms
are written `ln`. The uniform-cube Fourier convention is
\(\widehat f(S)=\mathbb E[f\chi_S]\).

## 1. Proposed theorems

For Boolean \(f\), let \(H(f)=\sum_S\widehat f(S)^2\log_2(1/\widehat f(S)^2)\)
and \(I(f)=\sum_i\Pr[f(X)\ne f(X^{\oplus i})]\).

**Parallel-slab theorem.** There is a universal constant \(C_{\rm slab}\)
such that every function
\[
 f(x)=1-2\mathbbm1\{a<\textstyle\sum_i w_i x_i<b\}
\]
(with arbitrary endpoint conventions, complement, coordinate sign changes,
and possibly infinite endpoints) satisfies
\[
 H(f)\le C_{\rm slab} I(f).
\]
More strongly, its entropy increment upon restricting a largest-absolute-
weight coordinate satisfies \(\Delta_iH(f)\le C_{\rm slab}I_i(f)\).

**Separated-crossing theorem.** Suppose \(f(x)=F(\sum_iw_ix_i)\), where
\(F\) has at most \(m\) crossings, and successive crossing points have
distance strictly greater than \(2\max_i|w_i|\). Then
\[
 H(f)\le C_m I(f),
\]
where \(C_m\) depends only on \(m\). This class is closed under input
restriction: the crossing points translate together while the largest
remaining weight decreases.

Constants are permitted. Delete zero-weight coordinates and change signs
of coordinates so all input weights are positive. Endpoint conventions
can be preserved by moving each crossing point into a gap in the finite
set of attained scores. They can additionally be chosen so no difference
of two crossing points equals twice an input weight. This follows by an
arbitrarily small perturbation inside the open gaps, avoiding finitely
many hyperplanes. Thus the narrow/wide dichotomy below has no equality
case. For the separated theorem, a sufficiently small perturbation
preserves the strict separation. Equality is also allowed if no crossing
point is an attained score, since then the open pivotal intervals are
disjoint. Equality with arbitrary endpoint conventions is not included:
if both endpoints of an interval of width \(2w\) are attained and assigned
the outside label, an edge joining the endpoints crosses two effective
boundaries and cancels. Tie removal then shrinks that interval.

## 2. A general easy split: two disjoint exceptional branch supports

Write a Boolean split as \(f(x,z)=A(x)+zB(x)\), and put
\(\alpha=\mathbb E B^2=I_z(f)\). Define
\[
 P_S=\widehat A(S)^2+\widehat B(S)^2,\qquad
 q_S=\widehat B(S)^2/P_S,\qquad
 C=\sum_S P_S h_2(q_S).
\]
The exact split identity and the elementary binary-entropy inequality from
the LTF proof give, for every Boolean function,
\[
 \Delta_zH(f)\le2C.\tag{1}
\]

**Disjoint-support lemma.** If, after a possible output sign change,
\(A=1-|B|\), then \(\Delta_zH(f)\le8\alpha\).

Proof. Let \(\beta=\mathbb E B\), so \(|\beta|\le\alpha\). At the empty
set, \(\widehat A(\varnothing)=1-\alpha\) and
\(\widehat B(\varnothing)=\beta\). Therefore the total nonempty spectral
pair mass is
\[
 1-(1-\alpha)^2-\beta^2\le2\alpha.
\]
As \(h_2\le1\), the contribution of these sets to \(C\) is at most
\(2\alpha\). If \(\alpha\ge1/2\), simply \(C\le1\le2\alpha\), so
(1) already gives the claim.

Suppose \(0<\alpha<1/2\), and write \(x=\beta^2\le\alpha^2<1/4\) and
\(P_0=(1-\alpha)^2+x\le1\). The empty-set contribution is
\[
 x\log_2(P_0/x)+(1-\alpha)^2
       \log_2(P_0/(1-\alpha)^2)
 \le x\log_2(1/x)+(\log_2e)x.
\]
The map \(x\log_2(1/x)\) increases on \([0,1/4]\), hence this is at
most
\[
 2\alpha^2\log_2(1/\alpha)+(\log_2e)\alpha^2
 \le\left(\frac{2\log_2e}{e}+\frac{\log_2e}{2}\right)\alpha
 <2\alpha.
\]
Here \(\sup_{0<t<1}t\ln(1/t)=1/e\). Thus \(C\le4\alpha\), and (1)
proves the lemma. The case \(\alpha=0\) is immediate.

In particular, if the exceptional interval has width less than twice the
pivot weight \(w\), then its two restricted exceptional supports are
disjoint: a score cannot have both \(t-w\) and \(t+w\) inside that
interval. Hence \(A=1-|B|\), with no monotonicity or further information
about either branch needed.

## 3. Separated crossings: signed union of disjoint pivotal slabs

Choose a largest input weight \(w\), write the remaining weights as
\(a_j\le w\), and put
\[
 R=\frac{\sum_j a_j^2}{w^2},\quad
 \alpha=I_z(f),\quad T=\ln(1/\alpha),\quad M=\max\{1,R,T\}.
\]
Assume all successive crossings \(t_1<\cdots<t_s\), \(s\le m\), have
distance strictly greater than \(2w\). Let \(B_r\) be the positive indicator of the
pivotal slab around crossing \(t_r\). These supports are pairwise
disjoint, and
\[
 B=\sum_{r=1}^s\epsilon_r B_r,\quad \epsilon_r\in\{-1,1\},\qquad
 \alpha_r=\mathbb E B_r,\quad \alpha=\sum_r\alpha_r.\tag{2}
\]
The signs alternate; only their absolute value is relevant below.
Redundant crossing points may be omitted. In particular, every retained
crossing defines a nonconstant halfspace, so \(\alpha_r>0\). The largest
weight has largest influence for each of those individual halfspaces.

### 3.1 Signed slab spectrum has little low-degree mass

The interval concentration/resampling proof in Section 2 of the LTF proof
applies to the union of these \(s\) slabs, each with half-width \(w\).
Conditional on the resampling mask and original input, its probability is
at most the sum of the \(s\) uniform interval concentration bounds.
Consequently
\[
 \operatorname{Stab}_\rho(B)
 \le\mathbb E[|B(X)||B(Y)|]
 \le\alpha\min\left\{1,\frac{6m}{\sqrt{(1-\rho)R}}\right\}.
 \tag{3}
\]
The relative factor \(\alpha\) is valid because the good/bad resampling
mask event is independent of \(X\), just as in the single-slab proof.
For the signed function, hypercontractivity also gives
\[
 \operatorname{Stab}_{1/2}(B)
 \le\|B\|_{3/2}^2=\alpha^{4/3},\tag{4}
\]
since \(|B|\) is an indicator.

Let \(Q_S=\widehat B(S)^2/\alpha\), a probability law, and \(K=|S|\).
Equations (3)–(4) imply
\[
 Q(K\le k)\le18m\sqrt{k/R},\qquad
 Q(K\le k)\le2^k\alpha^{1/3}\quad(k\ge1).\tag{5}
\]
The first estimate is omitted when \(R=0\).

For completeness, the second estimate implies
\(Q(K\le k)\le3\sqrt{k/T}\) whenever \(T>0\). If
\(1\le k\le T/(6\ln2)\), it gives \(e^{-T/6}\), and
\(\sqrt T e^{-T/6}\le\sqrt3 e^{-1/2}<3\sqrt k\). If
\(k>T/(6\ln2)\), the trivial bound 1 suffices because
\(\sqrt{6\ln2}<3\). Small \(T\) is included in this latter case.
Combining these bounds, and the trivial estimate when \(M=1\), proves
\[
 Q(K\le k)\le18m\sqrt{k/M}\quad(k\ge1).\tag{6}
\]
The empty-set mass need not equal \(\alpha\) because \(B\) is signed;
the needed replacement is
\[
 Q_0=(\mathbb E B)^2/\alpha\le\alpha.\tag{7}
\]

### 3.2 Pair-spectrum tail at the same scale

For the individual halfspace at crossing \(r\), let its minority output
density be \(p_r\le1/2\), and \(L_r=\ln(1/p_r)\). The established
Keller–Klein Theorem 1.4 and Klivans–O'Donnell–Servedio Theorem 18 give
\[
 \alpha_r\ge c p_r\min\{1,\sqrt{L_r/(R+1)}\},\qquad
 \alpha_r\le2p_r,\tag{8}
\]
and
\[
 \operatorname{NS}_\varepsilon(h_r)
 \le20.5p_r\sqrt{\varepsilon L_r}\quad(0<\varepsilon\le1/2).
 \tag{9}
\]
Here \(c>0\) is the same universal lower-bound constant as in the LTF
proof. Both halfspace normalizations use all input weights, and the
physical bit-flip influence normalization.

If \(f(X)\ne f(Y)\), at least one crossing halfspace changes value.
Thus \(\operatorname{NS}_\varepsilon(f)\le\sum_r
\operatorname{NS}_\varepsilon(h_r)\); this does not assert any relative
small-set noise bound for an interval indicator. Exactly as in the LTF
proof, for the pair law \(P_S=\widehat A(S)^2+\widehat B(S)^2\),
\[
 P(|S|\ge u)\le\frac{A_0}{\sqrt u}
       \sum_r p_r\sqrt{L_r}\quad(u>0),\qquad
 A_0=\frac{20.5\sqrt2}{1-e^{-1}}.\tag{10}
\]
For \(u\ge1\), use noise rate \(1/(2u)\). For \(0<u<1\), use noise
rate \(1/2\): the full nonconstant spectral mass is at most
\(4\sum_r p_r\), which is smaller than the right side of (10).

The required common-scale conversion follows from (8):
\[
 \begin{aligned}
 \sum_r p_r\sqrt{L_r}
 &\le c^{-1}\sum_r\alpha_r
       \bigl(\sqrt{R+1}+\sqrt{L_r}\bigr)\\
 &\le c^{-1}\alpha
       \bigl(\sqrt{R+1}+\sqrt{\ln(2m/\alpha)}\bigr)\\
 &\le c^{-1}\alpha\sqrt M
       \bigl(\sqrt2+\sqrt{1+\ln(2m)}\bigr).
 \end{aligned}\tag{11}
\]
To justify the middle step, \(\alpha_r\le2p_r\) gives
\(L_r\le\ln(2/\alpha_r)\). Set \(\lambda_r=\alpha_r/\alpha\);
Jensen/Cauchy–Schwarz yields
\[
 \sum_r\lambda_r\sqrt{\ln(2/\alpha_r)}
 \le\sqrt{\ln(2/\alpha)+\sum_r\lambda_r\ln(1/\lambda_r)}
 \le\sqrt{\ln(2m/\alpha)}.
\]
No maximum over possibly tiny \(p_r\) enters the scale. This matters
because one very remote crossing must not force \(M\) to be very large.

Put
\[
 \Gamma_m=\max\left\{1,\frac{A_0}{c}
       \bigl(\sqrt2+\sqrt{1+\ln(2m)}\bigr)\right\}.
\]
Equations (10)–(11) give
\[
 P(|S|\ge u)\le\Gamma_m\alpha\sqrt{M/u}.\tag{12}
\]

### 3.3 The dyadic KL argument survives signed derivatives

Use the empty set as a separate bin, and map positive degree to
\(J=\lfloor\log_2(K/M)\rfloor\). Equations (6) and (12) give
\[
 P_j\le\Gamma_m\alpha2^{-j/2},\qquad
 Q_j\le18m\sqrt2\,2^{j/2}\quad(j<0).
\]
The latter is applied only to nonempty bins, whose upper endpoint is at
least 1. Consequently
\[
 \mathbb E_Q[|J|\mathbbm1\{J<0\}]
 \le C_{-,m}:=18m\sqrt2\frac{s}{(1-s)^2},\qquad s=2^{-1/2}.
\]
Let \(r=2^{-1/4}\), \(Z=(1+r)/(1-r)\), and use the reference probability
law \(R_*=1/2\), \(R_j=2^{-|j|/4}/(2Z)\). Nonnegativity of KL against
this reference, followed by data processing, proves
\[
 D(Q\Vert P)\ge\log_2(1/\alpha)-D_m,\tag{13}
\]
where
\[
 D_m=\log_2(2Z\Gamma_m)+\tfrac34 C_{-,m}
       +1+\frac{\log_2e}{e}.
\]
The calculation is the same as Section 5 of the LTF proof. The only change
is that the empty-set mass is \(q_*=Q_0\le\alpha\), rather than exactly
\(\alpha\). Its reference contribution is at least \(-q_*\ge-\alpha\),
and the omitted baseline term is at most
\(q_*\log_2(1/\alpha)\le\alpha\log_2(1/\alpha)\le(\log_2e)/e\).
Hence (13) has exactly the same direction and constant formula.

The included-bit entropy contribution is
\[
 \sum_S\widehat B(S)^2\log_2\frac{P_S}{\widehat B(S)^2}
 =\alpha\bigl(\log_2(1/\alpha)-D(Q\Vert P)\bigr)
 \le\alpha D_m.
\]
The excluded-bit contribution is at most \((\log_2e)\alpha\), using
\(\ln(1+t)\le t\). By (1),
\[
 \boxed{\Delta_zH(f)\le C_m\alpha,\qquad
 C_m=2(D_m+\log_2e).}\tag{14}
\]

## 4. Complete slab proof and restriction induction

A one-crossing function is an LTF, already covered by the prior theorem.
For a two-crossing function, let \(d\) be its exceptional interval width
and \(w\) its largest input weight. When \(d<2w\), the disjoint-support
lemma gives \(\Delta_zH\le8I_z\). When \(d>2w\), apply the separated
proof with \(m=2\). Therefore take
\[
 C_{\rm slab}=\max\{8,C_*,C_2\},
\]
where \(C_*\) is the all-LTF constant from the prior proof. Constants and
zero-variable functions have zero entropy/influence. The class of
interval indicators is closed under restriction; the interval translates
but remains a single interval. Thus induction on the number of relevant
variables, using the largest remaining input weight at each node, gives
\[
 H(f)\le C_{\rm slab}\left(I_z(f)
       +\tfrac12[I(f^+)+I(f^-)]\right)=C_{\rm slab}I(f).
\]
The same induction proves the separated-crossing theorem with \(C_m\),
because the separation condition is preserved. If fewer than \(m\)
crossings remain, all the estimates remain valid with the larger constant.

## 5. Limits and audit targets

The result does not cover three arbitrary crossings. For such functions,
nearby crossings may cancel on large-weight edges while a remaining
crossing supplies a complicated background. Then neither influence
additivity (2) nor the constant-background identity \(A=1-|B|\) holds.
The known dominant-coordinate/point-flipped-majority example has exactly
this form and rules out a universal largest-weight local bound for all
three-crossing functions. It does not contradict the two-crossing result.

Audit the following points in particular: signed-function
hypercontractivity; \(Q_0\le\alpha\) in the KL calculation; independence
of the resampling mask in the union-of-slabs bound; the weighted Jensen
conversion (11); and endpoint/generic-perturbation treatment.

Established primary inputs:

* Keller–Klein (2019), Theorem 1.4,
  <https://arxiv.org/html/1710.07429v3>.
* Klivans–O'Donnell–Servedio (2004), Theorem 18,
  <https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>.

The new portions are the elementary disjoint-support case split and the
signed separated-crossing adaptation. Research novelty is unverified.

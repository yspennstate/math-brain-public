# Fourier entropy–influence for every parallel slab and separated finite crossings

Date: 2026-10-02. **Complete proof, internally audited; novelty unverified.**

This note extends the internally audited [all-LTF proof](../2026-10-02-largest-weight/largest_weight_ltf_fei_proof.md). It proves FEI for
every Boolean indicator/complement of a single interval in one linear form,
with arbitrary weights and endpoints. The more general result covers any
fixed number of crossings when the crossing points are separated by
strictly more than twice the largest input weight. No result is claimed for three or
more arbitrarily spaced crossings.

The [candidate draft](stripe_extension_parallel_slabs_candidate.md) is
preserved. Independent analytic audits:
[K-theory agent audit](stripe_extension_k_independent_audit.md),
[heat/entropy agent audit](stripe_extension_heat_independent_audit.md), and
[root audit](stripe_extension_root_independent_audit.md).
These are internal checks, not external peer review. The
[finite checker](stripe_extension_verify_parallel_slabs.py) passed
3,846 slab functions through dimension 12, including 2,184 narrow and
1,662 wide cases; its [results](stripe_extension_parallel_slabs_verification.json)
also record 11,634 signed stability checks, 12,702 low-degree checks,
17,688 pair-tail checks, and 1,662 dyadic KL checks. Finite computation
does not establish the asymptotic theorem.

All entropies and KL divergences use base-2 logarithms. Natural logarithms
are written `ln`. The uniform-cube Fourier convention is
\(\widehat f(S)=\mathbb E[f\chi_S]\).

## 1. Theorems and scope

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
\(F:\mathbb R\to\{-1,1\}\) is constant on the open intervals separated
by at most \(m\) retained crossing points. At each retained point the
two adjacent open intervals have opposite labels, and the point itself
has one of those two labels. There are no additional isolated point
anomalies. Suppose successive retained points have distance strictly
greater than \(2\max_i|w_i|\). Then
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
preserves the strict separation. Equality with arbitrary endpoint conventions is not included:
if both endpoints of an interval of width \(2w\) are attained and assigned
the outside label, an edge joining the endpoints crosses two effective
boundaries and cancels. Tie removal then shrinks that interval.
An [exact three-variable witness](stripe_endpoint_equality_counterexample.json)
is preserved. Degenerate intervals are also covered: an empty interval
gives a constant, and a singleton attained score can be replaced by a
positive-width open interval inside its neighboring finite score gaps.

## 2. A general easy split: two disjoint exceptional branch supports

Write a Boolean split as \(f(x,z)=A(x)+zB(x)\), and put
\(\alpha=\mathbb E B^2=I_z(f)\). Define
\[
 P_S=\widehat A(S)^2+\widehat B(S)^2,\qquad
 q_S=\widehat B(S)^2/P_S,\qquad
 C=\sum_S P_S h_2(q_S).
\]
For every nonzero pair put
\(r_S=(\widehat A(S)+\widehat B(S))^2/(2P_S)\). The full spectrum groups
\(\widehat A(S)^2,\widehat B(S)^2\), while the two restricted spectra
group \((\widehat A(S)+\widehat B(S))^2/2\) and
\((\widehat A(S)-\widehat B(S))^2/2\). Shannon's entropy chain rule gives
\[
 \Delta_zH(f)=\sum_S P_S[1+h_2(q_S)-h_2(r_S)].
\]
The elementary inequality \(h_2(t)\ge4t(1-t)\), together with
\(r_S(1-r_S)=(1-2q_S)^2/4\), yields
\(1-h_2(r_S)\le4q_S(1-q_S)\le h_2(q_S)\). Therefore, for every Boolean function,
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

We first recall the elementary bounded-weight concentration estimate.
For independent signs and \(Z=\sum_jb_jX_j\), where \(|b_j|\le w\) and
\(v=\sum_jb_j^2>0\), every interval of half-width \(w\) has probability
at most \(\min\{1,3w/\sqrt v\}\). To prove this, use
\[
 K(u)=\left(\frac{\sin(u/(2w))}{u/(2w)}\right)^2
      =w\int_{-1/w}^{1/w}(1-w|t|)e^{itu}\,dt.
\]
For \(|u|\le w\), \(K(u)>9/10\). For \(|t|\le1/w\),
\(|\cos(b_jt)|\le e^{-b_j^2t^2/2}\). Thus for any center \(t_0\),
\[
 \Pr(|Z-t_0|\le w)\le\tfrac{10}{9}\mathbb E K(Z-t_0)
 \le\tfrac{10}{9}w\int_{\mathbb R}e^{-vt^2/2}\,dt
 <3w/\sqrt v.
\]
This permits atoms, and the bound is uniform in the center.

Generate \(\rho\)-correlated \(X,Y\) by independently retaining each
coordinate with probability \(\rho\), otherwise resampling it. Let \(J\)
be the resampling mask, independent of \(X\), and
\(V_J=\sum_{j\in J}a_j^2\). Conditional on \((J,X)\), the retained
coordinates change only the slab centers. The probability that \(Y\)
lies in the union of the \(s\) slabs is at most
\(\min\{1,3m w/\sqrt{V_J}\}\), using bound 1 when \(V_J=0\).

For \(R>0\), put \(\mu=(1-\rho)R\). Since \(a_j^2/w^2\in[0,1]\), a weighted
Bernoulli Chernoff bound gives
\(\Pr(V_J<(1-\rho)\sum_j a_j^2/2)\le e^{-\mu/8}\). Indeed,
\(e^{-u}\le1-(1-e^{-1})u\) for \(u\in[0,1]\), and exponential Markov
with parameter 1 gives the stronger exponent
\((1-e^{-1})-1/2>1/8\). On a good mask, the conditional union probability
is at most \(3m\sqrt2/\sqrt\mu\). Multiplying by \(|B(X)|\), averaging,
and using mask independence gives
\[
 \mathbb E[|B(X)||B(Y)|]
 \le\alpha\left(3m\sqrt2/\sqrt\mu+e^{-\mu/8}\right)
 \le6m\alpha/\sqrt\mu,
\]
because \(\sup_{u>0}\sqrt u e^{-u/8}=2e^{-1/2}\) and
\(3m\sqrt2+2e^{-1/2}<6m\) for \(m\ge1\). The trivial bound is
\(\alpha\). Consequently
\[
 \operatorname{Stab}_\rho(B)
 \le\mathbb E[|B(X)||B(Y)|]
 \le\alpha\min\left\{1,\frac{6m}{\sqrt{(1-\rho)R}}\right\}.
 \tag{3}
\]
The relative factor \(\alpha\) is valid because the good/bad resampling
mask event is independent of \(X\), just as in the single-slab proof.
For \(R=0\) only the trivial stability bound is used. For the signed
function, hypercontractivity also gives
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
Here is the calculation explicitly. Let \(D_{\rm bin}\) be the KL
divergence between the binned laws. Since \(D(Q_{\rm bin}\Vert R)\ge0\),
\[
 D_{\rm bin}\ge\sum_b Q_b\log_2(R_b/P_b).
\]
For every positive-degree bin \(j\), the logarithm is at least
\[
 \log_2(1/\alpha)-\log_2(2Z\Gamma_m)
        +\tfrac12j-\tfrac14|j|.
\]
The last two terms are nonnegative for \(j\ge0\) and equal
\(-3|j|/4\) for \(j<0\). The empty-set mass is
\(q_*=Q_0\le\alpha\), and its contribution is at least \(-q_*\),
because \(P_*\le1\) and \(R_*=1/2\). Thus
\[
 \begin{aligned}
 D_{\rm bin}
 &\ge (1-q_*)\log_2(1/\alpha)-\log_2(2Z\Gamma_m)
       -\tfrac34C_{-,m}-q_*\\
 &\ge\log_2(1/\alpha)-\log_2(2Z\Gamma_m)
       -\tfrac34C_{-,m}-1-\frac{\log_2e}{e}.
 \end{aligned}
\]
This uses \(q_*\log_2(1/\alpha)\le\alpha\log_2(1/\alpha)
\le(\log_2e)/e\). The full law satisfies \(P_S\ge\alpha Q_S\), so
all KL terms on the support of \(Q\) are well-defined. Data processing
gives \(D(Q\Vert P)\ge D_{\rm bin}\), proving (13).

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

A one-crossing function is covered by Section 3 with \(s=1\) and \(m=2\);
the separation condition is vacuous for a single crossing.
For a two-crossing function, let \(d\) be its exceptional interval width
and \(w\) its largest input weight. When \(d<2w\), the disjoint-support
lemma gives \(\Delta_zH\le8I_z\). When \(d>2w\), apply the separated
proof with \(m=2\). Therefore take
\[
 C_{\rm slab}=\max\{8,C_2\},
\]
where \(C_2\) is the explicit expression in (14) at \(m=2\). Constants and
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

## 5. Limits, provenance, and validation

The result does not cover three arbitrary crossings. For such functions,
nearby crossings may cancel on large-weight edges while a remaining
crossing supplies a complicated background. Then neither influence
additivity (2) nor the constant-background identity \(A=1-|B|\) holds.
The known dominant-coordinate/point-flipped-majority example has exactly
this form and rules out a universal largest-weight local bound for all
three-crossing functions. It does not contradict the two-crossing result.

The internal audits checked signed-function hypercontractivity,
\(Q_0\le\alpha\) in the KL calculation, resampling-mask independence,
the weighted Jensen conversion (11), and the restriction induction. They
identified the endpoint gap in an earlier non-strict separation claim;
the theorem above uses only strict separation, and preserves the exact
counterexample to equality. The arbitrary slab theorem uses the
endpoint-preserving perturbation and unrestricted narrow/wide case split.

Established primary inputs:

* Keller–Klein (2019), Theorem 1.4,
  <https://arxiv.org/html/1710.07429v3>.
* Klivans–O'Donnell–Servedio (2004), Theorem 18,
  <https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>.
* The standard uniform-cube Bonami–Beckner hypercontractive inequality,
  including its small-set expansion consequence, as stated and proved in
  O'Donnell, *Analysis of Boolean Functions*, Section 9.5, printed page 264,
  <https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf>.

The elementary disjoint-support case split and the signed separated-crossing
adaptation are developed here. Keller–Klein and Klivans–O'Donnell–Servedio
supply the two cited halfspace estimates; the completed all-LTF argument
supplies the original interval-concentration/KL route. Research novelty and
external peer review are not certified.

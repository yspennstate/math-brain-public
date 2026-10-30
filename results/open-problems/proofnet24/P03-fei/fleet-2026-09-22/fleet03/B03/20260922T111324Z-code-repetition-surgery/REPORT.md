# FEI / fleet03 B03 — repetition-code exceptional-set surgery

**Run:** `20260922T111324Z-code-repetition-surgery`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-fleet03-B03`, path A  
**Outcome:** `ESSENTIAL_STEP_APPLIED / PARAMETERIZED_CODE_FAMILY`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 1. Target and current-source discipline

The assigned target is to build an actual Boolean gate by flipping a character on an explicit error-correcting-code/design-supported set, derive the indicator Fourier transform and signed Boolean convolution exactly, and compare influence cost, `K_occ`, and the repaired gate defect as the code parameters grow.

The fresh owner state retires the old fixed quadratic repairs, raw-`U4`, unweighted-convolution-`L2`, and fixed-depth-KL routes. None is used here. The live named candidate attacked below is

`SHAPED_EPS02268865`,

whose source-exact balanced center is

\[
C_*=6.558445288811087.
\tag{1.1}
\]

Source: `yspennstate/math-open-problems`, commit `c50e06733fc1e7f109e20dbb1a0013d67aa71dc7`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B13/20260922T0954Z-nearoptimal-singleton-repair/REPORT.md`, Section 4.

The assigned partner is `fleet04/B03`. At both the fresh startup read and the pre-publication partner scan, no compatible completed `fleet04/B03` result existed under the current FEI programme. I therefore did **not** fabricate partner consumption or reuse its older FOREST work. Per the owner order's asynchronous rule, I instead applied the assignment's named compatible other-account input `B-BIASED-BOOLEANITY-GAP-v1` from `fleet04/B17`, commit `603b35e74227d1c2d8ee34c0c527c439c686e30b`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`.

The exact partner-source expression applied below is its positive I-projection root for occurrence vector
\(r=(1-q,q,\ldots,q)\):

\[
1-c=(1-c(1-q))(1-cq)^{n-1},\qquad c\in(0,1),
\tag{1.2}
\]

with the source-proved bound \(c\ge1/2\). This is used to compute the exact canonical `K_occ` of the new code-supported family.

## 2. A general linear-code character-flip identity

Work on \(\mathbb F_2^n\) with characters
\[
\chi_s(x)=(-1)^{s\cdot x}
\]
and normalized Walsh transform
\[
\widehat h(s)=2^{-n}\sum_x h(x)\chi_s(x).
\]

Let \(C\le\mathbb F_2^n\) be a linear code of codimension \(r\), let
\[
\delta={|C|\over 2^n}=2^{-r},\qquad V=C^\perp,
\]
so \(|V|=2^r=1/\delta\). Pick \(a\notin V\) and define the actual Boolean gate
\[
F_{C,a}(x)=\chi_a(x)\bigl(1-2\mathbf 1_C(x)\bigr).
\tag{2.1}
\]
Thus a character is flipped exactly on the code support.

### Lemma 2.1 — exact indicator and gate transform

For every \(u\),
\[
\boxed{\widehat{\mathbf 1_C}(u)=\delta\,\mathbf 1_{u\in V}.}
\tag{2.2}
\]
Consequently
\[
\boxed{
\widehat F_{C,a}(s)
=\mathbf 1_{s=a}-2\delta\,\mathbf 1_{s\in a+V}.
}
\tag{2.3}
\]
In particular, writing \(q=2\delta\),
\[
\widehat F(a)=1-q,
\qquad
\widehat F(a+u)=-q\quad(u\in V\setminus\{0\}),
\tag{2.4}
\]
and all other coefficients vanish.

**Proof.** Equation (2.2) is the standard orthogonality sum on the subgroup \(C\): the average of \(\chi_u\) over \(C\) is one exactly when \(u\) annihilates \(C\). Multiplication by \(\chi_a\) translates Fourier support by \(a\), giving (2.3). Since \(a\notin V\), the distinguished point \(a\) is one element of the affine coset \(a+V\), producing (2.4). `QED`.

### Lemma 2.2 — exact signed convolution, with cancellation exposed

Let \(*_\oplus\) denote xor convolution. Then
\[
\boxed{
(\widehat F*_{\oplus}\widehat F)(w)
:=\sum_s\widehat F(s)\widehat F(s\oplus w)
=\mathbf 1_{w=0}.
}
\tag{2.5}
\]

**Proof.** Let \(h=\mathbf 1_{a+V}\). From (2.3),
\[
\widehat F=\delta_a-qh.
\]
Now
\[
\delta_a*\delta_a=\delta_0,
\quad
\delta_a*h=h*\delta_a=\mathbf 1_V,
\quad
h*h=|V|\mathbf 1_V.
\]
Therefore
\[
\widehat F*\widehat F
=\delta_0+(-2q+q^2|V|)\mathbf 1_V.
\]
Since \(q=2\delta\) and \(|V|=1/\delta\), the parenthesis is
\(-4\delta+4\delta=0\). This is the complete signed Boolean equation; no absolute-value or unweighted-`L2` surrogate is introduced. `QED`.

This general identity is useful because code geometry can now be varied while signed Boolean realizability remains exact.

## 3. Explicit error-correcting-code family

Take the binary repetition code
\[
C_n=\{0^n,1^n\},
\]
the explicit \([n,1,n]\) code, for every \(n\ge3\). Its dual is the even-parity code
\[
V_n=C_n^\perp=\{u:\ |u|\equiv0\pmod2\},
\]
an \([n,n-1,2]\) code. Set \(a=e_1\), which is not in \(V_n\), and define
\[
F_n(x)=\chi_{e_1}(x)\bigl(1-2\mathbf 1_{C_n}(x)\bigr).
\tag{3.1}
\]
Thus the dictator character is flipped exactly at the two antipodal codewords. Put
\[
\delta_n=2^{1-n},\qquad q_n=2\delta_n=2^{2-n}.
\tag{3.2}
\]

By Lemma 2.1 the support is the entire odd-parity affine coset:
\[
\boxed{
\widehat F_n(\{1\})=1-q_n,
\quad
\widehat F_n(S)=-q_n\ \text{for every other odd }S,
\quad
\widehat F_n(S)=0\ \text{for even }S.
}
\tag{3.3}
\]
The empty coefficient is zero, so every \(F_n\) is exactly balanced.

The signed convolution (2.5) can also be seen pointwise. For any nonzero even \(w\), two ordered terms pair the large coefficient with a small one and contribute
\(-2q_n(1-q_n)\); the remaining \(2^{n-1}-2\) ordered terms contribute
\((2^{n-1}-2)q_n^2=2q_n(1-q_n)\). They cancel exactly. Odd shifts have disjoint supports.

## 4. Exact influence and entropy cost

Let \(P_n(S)=\widehat F_n(S)^2\). The occurrence probabilities are
\[
\boxed{
r_1=1-q_n,\qquad r_i=q_n\ (2\le i\le n).
}
\tag{4.1}
\]
Indeed, among the odd subsets exactly \(2^{n-2}\) contain a given coordinate; for coordinate one the distinguished coefficient must be separated from the other \(2^{n-2}-1\) terms.

Hence
\[
\boxed{
I(F_n)=1+(n-2)q_n,
\qquad
J_n:=I(F_n)-1=(n-2)2^{2-n}.
}
\tag{4.2}
\]
This is the exact influence excess paid by the rare two-codeword surgery.

The spectral entropy is
\[
\boxed{
H_n
=-(1-q_n)^2\log_2(1-q_n)^2
+q_n(2-q_n)(2n-4).
}
\tag{4.3}
\]
The second term is the entropy of the \(2^{n-1}-1\) equal small atoms of mass \(q_n^2\).

Therefore
\[
{H_n\over J_n}
=4-2q_n
+{-2(1-q_n)^2\log_2(1-q_n)\over(n-2)q_n}.
\tag{4.4}
\]
Using \(-\ln(1-q)\le q/(1-q)\),
\[
{-2(1-q)^2\log_2(1-q)\over(n-2)q}
\le {2(1-q)\over(n-2)\ln2}
\le {2\over(n-2)\ln2}.
\tag{4.5}
\]
For \(n=3\), direct substitution gives \(H_3/J_3=4\). For \(n=4\), (4.4)-(4.5) give
\[
H_4/J_4<3.5+1/\ln2<5.
\]
For \(n\ge5\),
\[
H_n/J_n<4+{2\over3\ln2}<5.
\]
Thus the entire infinite family satisfies the analytic bound
\[
\boxed{H_n<5J_n\quad(n\ge3).}
\tag{4.6}
\]
Moreover (4.4) shows
\[
\boxed{{H_n\over J_n}=4+o(1).}
\tag{4.7}
\]

## 5. Decisive result on `SHAPED_EPS02268865`

The current state gives the exact balanced-slice identity for any symmetric potential of center \(C\):
\[
D_\Gamma(f)=C\,[I(f)-1]-H(f).
\tag{5.1}
\]
For `SHAPED_EPS02268865`, \(C=C_*\) from (1.1). Combining (4.6) and (5.1),
\[
\boxed{
D_{\mathrm{SHAPED\_EPS02268865}}(F_n)
=C_*J_n-H_n
>(C_*-5)J_n>0
\quad\text{for every }n\ge3.
}
\tag{5.2}
\]
This is a theorem for the full parameterized code family, not a finite search. It decisively rules out the repetition-code antipodal surgery family as a counterexample to this named repaired candidate.

The relative defect is sharper asymptotically:
\[
\boxed{
{D_n\over J_n}\longrightarrow C_*-4
=2.558445288811087\ldots .
}
\tag{5.3}
\]
No descendant slack is discarded: (5.2) records the actual positive child defect. Any later composition argument using this gate must carry \(D_n\), not silently replace it by zero.

## 6. Exact `K_occ`: applying the compatible other-account theorem

The family has exactly the occurrence vector (4.1) used in the `fleet04/B17` two-flip calculation. Its support geometry is different—the present small spectrum is the odd-parity coset rather than the two-coordinate affine pattern—but the squared-mass multiset is also identical: one atom of mass \((1-q_n)^2\) and \(2^{n-1}-1\) atoms of mass \(q_n^2\). Therefore both \(r\) and \(H(P_n)\) match the quantities on which the canonical maximum-entropy nonempty I-projection depends.

Applying the exact source expression (1.2), let \(c_n\) be its positive root and set
\[
t_1=c_n(1-q_n),\qquad t_i=c_nq_n\quad(i\ge2).
\]
The unconditioned independent Bernoulli law has nonempty probability \(c_n\), so conditioning on nonempty yields the required occurrence vector. Its entropy is exactly
\[
\boxed{
H_{\max}(r_n)
={h_2(c_n(1-q_n))+(n-1)h_2(c_nq_n)-h_2(c_n)\over c_n}.
}
\tag{6.1}
\]
Hence the canonical dependence credit is
\[
\boxed{
K_{\rm occ}(F_n)
=H_{\max}(r_n)-H_n.
}
\tag{6.2}
\]
This preserves the exact normalization; there is no fixed-depth projection and no replacement of KL by an unweighted quadratic norm.

### Asymptotics

The partner-source bound gives \(c_n\ge1/2\). Put \(\epsilon_n=1-c_n\). From (1.2),
\[
{c_nq_n\over\epsilon_n}
=(1-c_nq_n)^{-(n-1)}-1.
\tag{6.3}
\]
Since \(nq_n\to0\) and \(c_n\in[1/2,1]\), uniformly
\[
(1-c_nq_n)^{-(n-1)}-1
=(n-1)c_nq_n+O(n^2q_n^2).
\]
Dividing by \(c_nq_n\) gives
\[
\boxed{
\epsilon_n={1\over n-1+O(n^2q_n)}
={1\over n-1}(1+o(1)).
}
\tag{6.4}
\]

Use \(h_2(x)=x\log_2(1/x)+x\log_2 e+O(x^2)\) as \(x\downarrow0\). The difference
\(h_2(c_n(1-q_n))-h_2(c_n)\) is \(O(q_n\log n)=o(J_n)\), while the \(n-1\) small-coordinate terms in (6.1) give
\[
{H_{\max}(r_n)\over J_n}
=n-1+\log_2 e+o(1).
\tag{6.5}
\]
Together with (4.7),
\[
\boxed{
{K_{\rm occ}(F_n)\over J_n}
=n-5+\log_2 e+o(1).
}
\tag{6.6}
\]
Thus on an exceptional set of density \(2^{1-n}\),
\[
J_n\asymp n2^{-n},
\qquad
K_{\rm occ}(F_n)\asymp n^2 2^{-n},
\qquad
D_n\asymp n2^{-n}.
\tag{6.7}
\]
The canonical KL credit carries an essential extra rare-event logarithm/dimension factor.

A concrete consequence is the source-valid no-go
\[
\boxed{
\text{There is no universal constant }A\text{ such that }
K_{\rm occ}(f)\le A\,[I(f)-1]
\text{ for all balanced Boolean }f.
}
\tag{6.8}
\]
The family \(F_n\) makes the ratio diverge linearly. This does not refute FEI; it says that compressing the exact occupancy KL credit to influence-excess scale loses precisely the currency needed on rare-event gates.

Finally, from the exact decomposition \(D=B_{\inf}+K_{\rm occ}\) on the balanced slice,
\[
{B_{\inf}(F_n)\over J_n}
=C_*-{H_{\max}(r_n)\over J_n}
=-n+O(1),
\tag{6.9}
\]
while (5.3) remains positive. Thus a large negative first-moment Bellman residual is genuinely canceled by exact `K_occ`; the cancellation is not an artifact of the refuted unweighted-`L2` route.

## 7. Checker and verification boundary

`CHECK.py` is standard-library only. It brute-forces the actual truth table and exact rational Walsh transform for \(n=3,\dots,8\), verifies (3.3), Parseval, balancedness, every signed xor-convolution equation, (4.1), and (4.2). It then evaluates the analytic entropy/I-projection formulas and candidate defect for representative larger parameters. Its locally executed source SHA-256 is

`5585c35bcacec46d283d6f8046f21210aa12528d2c2976f25bb50dae3439eb29`

and captured-output SHA-256 is

`0089d37efa9308868975ce5e086c9613ddcf032e56ee1e7c67f837c30f0fb427`.

The checker returned `PASS`. The theorem-level conclusions (2.2)-(6.9) are analytic and do not depend on the finite regression.

## 8. What is paid and what remains unpaid

**Paid in this run.** A parameterized family based on an explicit \([n,1,n]\) error-correcting code is handled for every \(n\ge3\). Its indicator transform, actual signed Boolean convolution, influence excess, exact entropy, exact canonical `K_occ`, and the live shaped-candidate defect are all derived with the original normalization. The named candidate `SHAPED_EPS02268865` has positive defect on the entire family, with explicit descendant slack, while `K_occ/(I-1)` diverges.

**Not paid.** This does not prove the all-gate inequality for `SHAPED_EPS02268865`, nor FEI. The next high-value code mechanism is to move from the two-word repetition support to a growing-size linear/design support whose dual weight distribution has several nontrivial shells. The exact general transform (2.3) and convolution (2.5) reduce that problem to optimizing the dual-coordinate geometry in the influence vector while retaining a computable `K_occ`. A genuine failure of the named candidate would require \(H(F_{C,a})>C_*[I(F_{C,a})-1]\) (on a balanced member) or its exact biased analogue; the present family proves the opposite with margin.

No scheduler mutation, new task, email, Drive, public release, workflow dispatch, paid model/API, cross-account native action, credentials, or private transcript was used.

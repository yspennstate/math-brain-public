# account02/B13 — a universal joint-credit inequality and a quarter-influence exclusion for critical FEI gates

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and scientific source files were read, but no separately verified native research-brain receiver context was consumed.

## 0. Compact conditional end-to-end argument and first missing implication

The live post-falsifier all-gate candidate used here is the source-current scalar lift
\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p).
\]
For a Boolean gate \(G\) at product bias \(p\), write
\[
D_\Gamma(G;p)=
\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p).
\]
The gate reformulation says that a symmetric nonnegative \(\Gamma\) with finite cap
\(\Gamma(1/2)\le C\) and \(D_\Gamma\ge0\) for every Boolean gate and every
interior product bias implies the original uniform-cube FEI inequality
\(H(f)\le C I(f)\) for every Boolean \(f\).

The original read-once-\(\Gamma\)/AND-extremality subcandidate is already
source-validly refuted by the explicit balanced prime gates in the current
archive, so I do not re-prove the stale owner-message extremality sentence.
The source-current first missing universal implication is instead:

> **LOCAL-GLUING.** Rule out a negative exact restriction-cocycle contribution
> \(\mathcal R_{\Gamma_*,j}+\mathcal C_j<0\) at every physical pivot of a
> minimum-essential-arity counterexample, while retaining the exact joint
> information credit \(\mathcal C_j=H(B\mid S)+I(S;J)\).

If this local implication held for every possible pair of Boolean restrictions
and every pivot bias, the exact restriction cocycle would rule out the
minimum-arity counterexample and hence prove the all-gate inequality. This run
does not close all of LOCAL-GLUING. It proves a dimension-free universal slice
of it and an exact signed tradeoff that every remaining central critical core
must satisfy.

The named completed other-account theorem used substantively is
`account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`.
Its exact identity is
\[
D_\Gamma(G)=qD_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j,
\qquad
\mathcal C_j=H(B\mid S)+I(S;J).
\]
The present proof derives a new lower bound on this *combined* credit. I also
read account04/B16's `20260922T040918Z-character-tube-joint-credit`, which
proved the one-common-character special case, and account01/B18's latest
`20260922T042319Z-two-exchange-support-rigidity`, which closes all two-row
mutations of the current 18-row balanced prime source obstruction and leaves
nonuniform-bias/local-gluing geometry as the cheaper next freedom.

## 1. Last three B13 reports: target-level and mechanism-level movement

The last three completed substantive account02/B13 reports before this run were:

1. `20260922T014831Z-g10-affine-restriction-atom`: every proper physical
   restriction of the certified \(G_{10}\) gate remains below the gate threshold
   even after a balancing character and arbitrary invertible affine re-basis.
2. `20260922T032411Z-gate-block-critical-core`: exact all-block defect
   decomposition and the minimum-essential-arity critical-core reduction for
   the all-gate functional.
3. `20260922T035349Z-character-tube-prime-defect`: a dimension-free payment in
   a very small Hamming tube around a physical character, together with a
   composition-prime family arbitrarily close to a dictator showing that
   primitivity alone cannot supply a fixed tube gap.

**FULL-PROBLEM CHANGE.** Before this run, the exact critical-core reduction was
available but its local information credit had no universal source-valid lower
bound strong enough to exclude a new region of arbitrary Boolean child pairs.
After this run, every unbiased physical pivot has a universal joint-credit
lower bound depending only on the *actual child disagreement probability*.
Consequently, in any minimum-arity balanced central counterexample at cap at
least \(13/2\), every coordinate with zero first Fourier coefficient has
influence strictly below \(1/4\), and every coordinate satisfies an exact
first-level/influence/potential-drop inequality. Full FEI is still open.

**MECHANISM CHANGE.** The three preceding mechanisms were affine matroid
optimization, physical gate-block defect induction, and Hamming character
tubes. Here the mechanism is a signed two-child Fourier coupling: keep the
relative Fourier signs until a conserved overlap moment is formed, then apply
a one-dimensional convexity theorem to the *joint* branch/vertical information
credit. In the `FLEET_RULES` vocabulary this uses moves 11 (dualize to the
coefficient-pair channel), 12 (identify the conserved signed overlap), and 25
(count the same overlap through physical disagreement and Fourier inner
product).

## 2. Exact source geometry at an unbiased physical pivot

Let the physical pivot \(j\) be unbiased, \(t=q=1/2\). Let
\[
f_0,f_1:\Omega\to\{-1,+1\}
\]
be the two actual Boolean restrictions on the common product space of all
remaining physical coordinates. In its real orthonormal Fourier basis write
\[
f_0=\sum_S a_S\chi_S,\qquad
f_1=\sum_S b_S\chi_S.
\]
Parseval gives \(\sum_Sa_S^2=\sum_Sb_S^2=1\).

Define
\[
T_S=\frac{a_S^2+b_S^2}{2}.
\]
For \(T_S>0\), put
\[
x_S=\frac{b_S^2}{a_S^2+b_S^2},\qquad
u_S=\frac{2|a_Sb_S|}{a_S^2+b_S^2},\qquad
\sigma_S=\operatorname{sgn}(a_Sb_S).
\]
If \(T_S=0\) set \(u_S=0\); its value is irrelevant. Then
\[
u_S=2\sqrt{x_S(1-x_S)}\in[0,1].
\]

Let
\[
\delta=\Pr[f_0\ne f_1].
\]
The exact B17 within-pair vertical posterior at \(t=1/2\) is
\[
\theta_S=\frac{(a_S-b_S)^2}{2(a_S^2+b_S^2)}
=\frac{1-\sigma_Su_S}{2}.
\]
The branch posterior at the same spectral atom is \(x_S\). Hence
\[
H(B\mid S)=\sum_ST_Sh_2(x_S),
\]
and, since \(\Pr[J=1]=\delta\),
\[
I(S;J)=h_2(\delta)-\sum_ST_Sh_2(\theta_S).
\]
Because binary entropy is symmetric,
\[
h_2(\theta_S)=h_2\!\left(\frac{1-u_S}{2}\right).
\]

The signed quantity has not disappeared: by Parseval,
\[
\sum_ST_S\sigma_Su_S
=\sum_Sa_Sb_S
=\mathbb E[f_0f_1]
=1-2\delta.
\tag{2.1}
\]

## 3. A convex one-variable Boolean credit theorem

Define, for \(0\le u\le1\),
\[
g(u)=h_2\!\left(\frac{1-u}{2}\right),
\]
and
\[
\Psi(u)
=
1+
h_2\!\left(\frac{1-\sqrt{1-u^2}}2\right)
-
h_2\!\left(\frac{1-u}2\right)
=
1+g(\sqrt{1-u^2})-g(u).
\tag{3.1}
\]
Since \(h_2(x_S)\) depends on \(x_S\) only through
\(u_S=2\sqrt{x_S(1-x_S)}\), the exact combined credit is
\[
\boxed{
\mathcal C_j
=
h_2(\delta)-1+\mathbb E_T\Psi(u_S).
}
\tag{3.2}
\]

### Lemma 3.1 — strict convexity

For \(0<u<1\), writing \(v=\sqrt{1-u^2}\),
\[
g'(u)=-\frac{\operatorname{artanh}u}{\ln2}.
\]
Therefore
\[
\Psi'(u)
=
\frac{\operatorname{artanh}u+(u/v)\operatorname{artanh}v}{\ln2}>0.
\]
Differentiating once more, the two rational terms cancel:
\[
\boxed{
\Psi''(u)=
\frac{\operatorname{artanh}v}{v^3\ln2}>0.
}
\tag{3.3}
\]
Thus \(\Psi\) is strictly increasing and strictly convex on \((0,1)\),
with continuous endpoint values.

### Theorem 3.2 — universal joint-credit lower bound

For every actual Boolean pair \(f_0,f_1\) at an unbiased physical pivot,
\[
\boxed{
H(B\mid S)+I(S;J)
\ge
h_2\!\left(
\frac{1-2\sqrt{\delta(1-\delta)}}2
\right).
}
\tag{3.4}
\]

**Proof.** From (2.1),
\[
\mathbb E_Tu_S\ge
\left|\mathbb E_T\sigma_Su_S\right|
=|1-2\delta|.
\]
Convexity and monotonicity give
\[
\mathbb E_T\Psi(u_S)
\ge \Psi(\mathbb E_Tu_S)
\ge \Psi(|1-2\delta|).
\]
Set \(c=|1-2\delta|\). Then
\[
\sqrt{1-c^2}=2\sqrt{\delta(1-\delta)},
\qquad
h_2\!\left(\frac{1-c}{2}\right)=h_2(\delta).
\]
Substitution into (3.1)-(3.2) cancels \(h_2(\delta)\) and proves (3.4).
\(\square\)

The endpoints are exact: if \(f_1=f_0\) or \(f_1=-f_0\), then
\(\delta\in\{0,1\}\) and both sides equal one. At \(\delta=1/2\) the bound
is zero and is intentionally weak.

### Equality rigidity

Away from the degenerate zero-overlap case, equality in (3.4) requires both
triangle equality in (2.1) and equality in strict Jensen. Hence every common
nonzero Fourier atom has one relative sign and one value of \(u_S\). Equivalently,
after the common sign is fixed, the common-support coefficient ratios
\(|b_S|/|a_S|\) take only the reciprocal pair
\[
\rho,\rho^{-1}
\]
for one \(\rho\ge1\) determined by \(\delta\). This is a genuine
two-child signed Boolean compatibility condition, not a condition on two
arbitrary probability laws.

## 4. Exact insertion into the all-gate local cocycle

At \(t=1/2\), the B17 exact local remainder is
\[
\mathcal R_{\Gamma,j}
=
\frac{\Gamma(r_0)+\Gamma(r_1)}2
-\Gamma\!\left(\frac{r_0+r_1}{2}\right)
+\delta\,\Gamma(1/2)-1-h_2(\delta),
\]
where \(r_b=\Pr[G_b=1]\). Combining with (3.4) gives the universal actual-Boolean
local inequality
\[
\boxed{
\begin{aligned}
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge{}&
\frac{\Gamma(r_0)+\Gamma(r_1)}2
-\Gamma\!\left(\frac{r_0+r_1}{2}\right)\\
&+\delta C-1-h_2(\delta)
+h_2\!\left(
\frac{1-2\sqrt{\delta(1-\delta)}}2
\right),
\end{aligned}}
\tag{4.1}
\]
with \(C=\Gamma(1/2)\). No concavity or differentiability of \(\Gamma\) is
used.

This strictly extends the *scope* of the account04/B16 character-tube
calculation: there the two children share one character factor and the internal
residual cancels exactly, giving a stronger all-\(\delta\) theorem. Here the
children are completely arbitrary Boolean functions; the price is that (4.1)
does not pay every small-\(\delta\) node.

## 5. A clean quarter-influence exclusion at cap \(13/2\)

Assume now that both children are balanced:
\[
r_0=r_1=\frac12.
\]
Then the potential Jensen term in (4.1) is exactly zero.

For \(1/4\le\delta\le1/2\), use the elementary entropy bound
\(h_2(x)\ge4x(1-x)\). With
\[
y=\frac{1-2\sqrt{\delta(1-\delta)}}2,
\]
one has
\[
4y(1-y)=(1-2\delta)^2.
\]
Therefore
\[
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge
F_C(\delta):=
C\delta-1-h_2(\delta)+(1-2\delta)^2.
\tag{5.1}
\]
On \([1/4,1/2]\),
\[
F_C'(\delta)
=
C-\log_2\frac{1-\delta}{\delta}-4(1-2\delta)
>
C-4.
\]
For \(C\ge13/2\), this is positive. At \(\delta=1/4\),
\[
F_C(1/4)
=
\frac C4-\frac{11}{4}+\frac34\log_2 3.
\]
Since \(\log_2 3>3/2\),
\[
F_C(1/4)>
\frac C4-\frac{13}{8}\ge0.
\]
Thus \(F_C(\delta)>0\) throughout \([1/4,1/2]\).

For \(\delta\ge1/2\), the nonnegativity of the exact credit alone gives
\[
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge C\delta-1-h_2(\delta)
\ge C/2-2>0.
\]

Hence:

### Theorem 5.1 — balanced-child quarter exclusion

For every symmetric potential \(\Gamma\) with
\[
\Gamma(1/2)=C\ge13/2,
\]
every unbiased physical pivot whose two actual Boolean restrictions are balanced
and have disagreement probability \(\delta\ge1/4\) satisfies
\[
\boxed{
\mathcal R_{\Gamma,j}+\mathcal C_j>0.
}
\tag{5.2}
\]

The theorem is independent of the number of residual variables and of their
Fourier complexity.

## 6. Consequence for a minimum-essential-arity critical core

Suppose \(D_\Gamma(G;p)<0\) and choose a counterexample with minimum essential
arity. Every proper physical child has smaller essential arity and therefore
nonnegative defect at its inherited bias vector. The exact B17 cocycle then
forces, for **every** essential pivot \(j\),
\[
\boxed{
\mathcal R_{\Gamma,j}+\mathcal C_j<0.
}
\tag{6.1}
\]

Now specialize to a balanced gate at the uniform center. Let
\(f=(-1)^G\), let
\[
a_i=\widehat f(\{i\}),\qquad
\delta_i=\operatorname{Inf}_i(f).
\]
Because the parent is balanced, the two child output biases are complementary,
and
\[
r_0=\frac{1-a_i}{2},\qquad
r_1=\frac{1+a_i}{2}.
\]
Symmetry of \(\Gamma\), (4.1), and (6.1) give the exact necessary tradeoff
\[
\boxed{
C-\Gamma\!\left(\frac{1-|a_i|}{2}\right)
>
L_C(\delta_i),
}
\tag{6.2}
\]
where
\[
L_C(\delta)=
C\delta-1-h_2(\delta)
+h_2\!\left(
\frac{1-2\sqrt{\delta(1-\delta)}}2
\right).
\tag{6.3}
\]

In particular, if \(a_i=0\), then the left side of (6.2) is zero. Theorem 5.1
therefore implies the new critical-core exclusion
\[
\boxed{
\widehat f(\{i\})=0
\quad\Longrightarrow\quad
\operatorname{Inf}_i(f)<\frac14
}
\tag{6.4}
\]
for every coordinate of a minimum-arity balanced central counterexample to any
candidate with cap \(C\ge13/2\), including the current
\(C_*=6.5218512\).

Equivalently, every coordinate of influence at least \(1/4\) is forced to carry
nonzero signed first-level Fourier mass, and more quantitatively its potential
drop from the cap must exceed \(L_C(\delta_i)\).

This is not an every-function statement. The minimum-arity quantifier is
essential: (6.1) is where criticality enters.

## 7. Tensor and gauge quantifiers

The joint-credit theorem survives the tensor operation relevant to primitive
cores. If the same disjoint Boolean factor \(h\) is multiplied into both
children, then
\[
a_{S,T}=a_Sc_T,\qquad b_{S,T}=b_Sc_T.
\]
The \(T\)-law acquires an independent factor \(c_T^2\), while every posterior
\(x_S\), \(u_S\), and relative sign \(\sigma_S\) is unchanged. Therefore
\[
\delta,\qquad H(B\mid S)+I(S;J),
\qquad\text{and the lower bound (3.4)}
\]
are all unchanged. There is **zero common-tensor tax**.

At the uniform center, simultaneous multiplication of both children by one
character, and any invertible linear change among the **nonpivot** variables,
merely permute the common Walsh atoms and therefore preserve (3.4). This is a
spectral invariance of the theorem; it is **not** permission to replace a
physical restriction by a free affine operation in the all-gate induction.
At nonuniform product bias no such affine/character gauge invariance is claimed.

Multiplying the parent by the pivot character replaces \(\delta\) by
\(1-\delta\); the credit lower bound (3.4) is symmetric under that change, but
the all-gate local remainder contains the nonsymmetric term \(C\delta\).
Accordingly, only the credit theorem, not the full local defect, is
pivot-character invariant.

## 8. What this says about the live candidate, and what remains unpaid

The source-current lead report account01/B18 closes every one- and two-row
support exchange around the published 18-row balanced prime obstruction at the
uniform center, and recommends moving to nonuniform product bias rather than a
larger combinatorial support search. The present theorem is complementary: it
does not search another support. It proves that any *central* minimum-arity
obstruction to the post-falsifier candidate must avoid a broad local gluing
geometry.

The first remaining implication for this mechanism is now exact:

> Extend (4.1) to force nonnegative local contribution either when
> \(r_0\ne r_1\) or when \(\delta<1/4\), using the actual potential drop and
> child slack, or prove that every minimum critical core has at least one pivot
> in the paid balanced-child region.

The source-valid account04/B16 character-tube theorem already removes one large
small-\(\delta\) family: when one branch is a common character times an arbitrary
Boolean residual, all disagreements are paid at cap six. Thus a surviving
small-\(\delta\) critical node must be genuinely two-sided, not merely a
one-character tube.

No universal FEI constant is proved here. In particular, (6.4) is a structural
property of a hypothetical minimum critical core, not FEI closure.

## 9. Decisive computation

A standard-library checker exhausts every ordered pair of Boolean child
functions through three residual variables:
\[
4+16+256+65536=65812
\]
pairs. It verifies (3.4) directly from the exact Walsh-pair formulas to floating
roundoff tolerance. It also checks every balanced-child pair with
\(\delta\ge1/4\) at cap \(13/2\).

Observed output:
- joint-credit pair checks: 65,812;
- minimum observed slack in (3.4): `0` (expected equality cases);
- balanced \(\delta\ge1/4\) checks: 4,862;
- minimum **exact local** contribution among those finite cases:
  `0.4080828133113007`.

The analytic theorem, including the quarter threshold, does not depend on this
finite census.

## 10. Provenance and honest status

Fresh source control before the scientific write: `math-research-brain/main`
`2026-09-22.2`, no account02/B13 pause or stop. Fresh scientific source was read
from `math-open-problems/master`, including the all-gate reformulation, the
exact account04/B17 cocycle, account04/B16 joint-character theorem, and the
latest account01/B18 critical obstruction report.

`FULL-PROBLEM CHANGE`: a new universal actual-Boolean local-credit inequality
and a minimum-critical-core quarter-influence exclusion now apply inside the
exact all-gate restriction cocycle. Full FEI remains open.

`MECHANISM CHANGE`: yes — signed overlap conservation plus convex joint
information, rather than affine profiles, character Hamming tubes, or another
support census.

No novelty/publication-priority claim is made. The checker is a self-check, not
an independent audit.

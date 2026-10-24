# B16 — exact balanced-pivot joint-credit geometry and a sharp Booleanity gap

**Run:** `20260922T043923Z-account01-B16-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SCALAR_RELAXATION_SHARP`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and mathematical sources were consumed directly, but no authenticated native-brain receiver context was used.

## 0. Live candidate and conditional end-to-end deduction

Fresh owner control revision `2026-09-22.2` supersedes the older Campaign-C request to keep extending the half-band compiler. The live target is the all-gate formulation.

I bind this run to the campaign lead's immutable candidate in

`account01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`,
blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`.

It fixes
\[
 C_* = 6.5218512,\qquad
 a_* = 0.2682048,\qquad
 \Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p),
\]
and names the one universal missing implication `LIMIT-PRIME-GATE-LIFT-v1`:
\[
 D_{\Gamma_*}(P;p)\ge 0
\]
for every finite-arity composition-prime Boolean gate \(P\) and every interior product bias \(p\).

The complete conditional deduction is short and source-exact.

1. For a symmetric nonnegative potential \(\Gamma\), define
   \[
   D_\Gamma(G;p)=
   \sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
   \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
   -\Gamma(p_{\rm out})-\widetilde H_G(p).
   \]
2. The all-gate reformulation proves that \(D_\Gamma\ge0\) for every gate and product bias, together with \(\Gamma(1/2)\le C\), implies \(H(f)\le CI(f)\) for every uniform-cube Boolean \(f\).
3. The exact account02/B17 disjoint-composition cocycle
   `account02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`,
   blob `8b59fbde81f8b194347452d0102f7f625ef85b89`,
   gives
   \[
   D_\Gamma(F(G_1,\dots,G_m))
   =D_\Gamma(F)+\sum_j b_jD_\Gamma(G_j),\qquad b_j\ge0.
   \]
   Therefore it is enough to prove the inequality on composition-prime gates.
4. The lead tail theorem places the entire known recursive shared-graft lower-bound family strictly below \(C_*\).
5. Hence `LIMIT-PRIME-GATE-LIFT-v1` would imply
   \[
   \boxed{H(f)\le6.5218512\,I(f)\quad\text{for every Boolean }f.}
   \]

The only universal gap is still step 3's prime-gate inequality. This report attacks it through the exact one-coordinate restriction cocycle, not through a new unrelated residual.

## 1. Other-account result consumed exactly

The principal input is account04/B17

`account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`,
blob `d32321447c5f30282f243d9a2907ec719d483c92`.

For a pivot \(j\) of bias \(t\), \(q=1-t\), with restrictions \(f_0,f_1\), it proves
\[
D_\Gamma(G)
=qD_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j,
\]
where
\[
\mathcal C_j=H(B\mid S)+I(S;J)
\]
is the *joint* source-exact information credit. It also proves that after a quadratic lift the required global margin is a nonnegative weighted average of the local restriction-gluing margins. Therefore a universal local payment would close the gate problem.

I also apply account04/B16

`account04/B16/20260922T040918Z-character-tube-joint-credit/REPORT.md`.

That report proves an exact joint-credit formula for the special pair \(f_0=x,\ f_1=xh\), and shows that separating the two information credits before cancellation gives a false sufficient scalar inequality. The new theorem below removes the special-character assumption at a balanced pivot and computes the optimal scalar relaxation for an *arbitrary* Boolean restriction pair.

## 2. Exact angular form at an arbitrary pivot

Write the biased Walsh coefficients of the two restrictions as
\[
a_S=\widehat f_0(S),\qquad b_S=\widehat f_1(S),
\]
and set
\[
u_S=\sqrt q\,a_S,\qquad v_S=\sqrt t\,b_S,\qquad
T_S=u_S^2+v_S^2.
\]
Then \(T\) is a probability law. For every \(T_S>0\), choose an angle \(\alpha_S\) with
\[
u_S=\sqrt{T_S}\cos\alpha_S,\qquad
v_S=\sqrt{T_S}\sin\alpha_S,
\]
and choose \(\varphi\in(0,\pi/2)\) by
\[
\cos\varphi=\sqrt q,\qquad \sin\varphi=\sqrt t.
\]

The branch posterior at spectral atom \(S\) is
\[
\Pr(B=1\mid S)=\sin^2\alpha_S.
\]
The vertical Fourier coefficient is
\[
\sqrt{tq}(b_S-a_S)
=-\sqrt t\,u_S+\sqrt q\,v_S
=\sqrt{T_S}\sin(\alpha_S-\varphi),
\]
hence
\[
\Pr(J=1\mid S)=\sin^2(\alpha_S-\varphi).
\]

Therefore the exact joint credit has the angular representation
\[
\boxed{
\mathcal C_j
=h_2(\operatorname{It}_j)
+\mathbb E_T\!\left[
 h_2(\sin^2\alpha)
-h_2(\sin^2(\alpha-\varphi))
\right].
}
\tag{2.1}
\]

No sign has been removed. The signed correlation is encoded in the same angles:
\[
\mathbb E_T\sin(2\alpha)
=2\sqrt{tq}\,\mathbb E[f_0f_1],
\qquad
\mathbb E_T\cos(2\alpha)=q-t.
\tag{2.2}
\]
Thus the joint-credit problem is an exact constrained angular transport problem, not two independent entropy estimates.

## 3. Balanced pivot: an exact one-dimensional signed formula

Now set \(t=q=1/2\). Define
\[
c_S=\frac{2a_Sb_S}{a_S^2+b_S^2},\qquad
X_S=|c_S|,
\qquad
T_S=\frac{a_S^2+b_S^2}{2}.
\]
Let
\[
\rho=\mathbb E[f_0f_1]=1-2\delta
=\sum_ST_Sc_S,
\qquad
\delta=\Pr[f_0\ne f_1].
\]
Put
\[
K(u)=h_2\!\left(\frac{1-u}{2}\right),
\]
and
\[
\boxed{
\Phi(x)
=
K\!\left(\sqrt{1-x^2}\right)-K(x)
=
h_2\!\left(\frac{1-\sqrt{1-x^2}}2\right)
-h_2\!\left(\frac{1-x}2\right).
}
\tag{3.1}
\]

At each spectral atom,
\[
H(B\mid S)
=K\!\left(\sqrt{1-c_S^2}\right),
\]
while
\[
H(J\mid S)=K(|c_S|).
\]
Since \(\operatorname{It}_j=\delta\), the two information channels collapse *exactly* to

\[
\boxed{
\mathcal C_j=h_2(\delta)+\mathbb E_T\Phi(X).
}
\tag{3.2}
\]

Consequently the complete local contribution in the account04/B17 cocycle is

\[
\boxed{
\mathcal L_{\Gamma,j}
:=
\mathcal R_{\Gamma,j}+\mathcal C_j
=
\frac{\Gamma(r_0)+\Gamma(r_1)}2
-\Gamma\!\left(\frac{r_0+r_1}{2}\right)
+\Gamma(1/2)\delta-1
+\mathbb E_T\Phi(X).
}
\tag{3.3}
\]

This is source-exact for every Boolean pair \(f_0,f_1\) on an arbitrary product-biased remaining cube. The separate \(h_2(\delta)\) terms cancel before any inequality is taken.

## 4. New theorem: strong convexity of the retained signed-overlap credit

For \(0<x<1\), put \(y=\sqrt{1-x^2}\). Since
\[
K'(u)=-\frac{\operatorname{atanh}u}{\ln2},
\]
direct differentiation gives
\[
\boxed{
\Phi'(x)
=\frac1{\ln2}\left[
\operatorname{atanh}x
+\frac{x}{y}\operatorname{atanh}y
\right]>0
}
\tag{4.1}
\]
and, after cancellation,
\[
\boxed{
\Phi''(x)
=
\frac{\operatorname{atanh}y}{y^3\ln2}.
}
\tag{4.2}
\]
Because \(\operatorname{atanh}y\ge y\) and \(0<y\le1\),
\[
\boxed{\Phi''(x)\ge\frac1{\ln2}.}
\tag{4.3}
\]

Thus \(\Phi\) is strictly increasing and \(1/\ln2\)-strongly convex on \([0,1]\) by continuity.

Let
\[
A:=\mathbb E_TX-|\rho|\ge0,
\qquad
V:=\operatorname{Var}_T(X).
\]
The first inequality is just the triangle inequality
\(\mathbb E|c|\ge|\mathbb Ec|\).
For \(|\rho|<1\), strong Jensen followed by the supporting-line inequality at \(|\rho|\) yields

\[
\boxed{
\mathbb E_T\Phi(X)
\ge
\Phi(|\rho|)
+\Phi'(|\rho|)A
+\frac{V}{2\ln2}.
}
\tag{4.4}
\]
At \(|\rho|=1\), Boolean equality forces \(X=1\) almost surely and the endpoint follows directly.

This is a quantitative signed-cancellation theorem. A local gate node can be close to the scalar lower envelope only if simultaneously

* the spectral overlap signs are almost coherent, so \(A\) is small; and
* the overlap magnitudes are almost isoclinic, so \(V\) is small.

Neither requirement was visible after the old independent scalarization of \(H(B|S)\) and \(I(S;J)\).

If
\[
m=\min\{\delta,1-\delta\},
\]
then \(|\rho|=1-2m\), and the definition
\[
j(m)=1-h_2\!\left(\frac12+\sqrt{m(1-m)}\right)
\]
gives
\[
\Phi(|\rho|)=1-j(m)-h_2(m).
\tag{4.5}
\]
Substituting into (3.3) yields the universal balanced-pivot rigidity bound

\[
\boxed{
\begin{aligned}
\mathcal L_{\Gamma,j}
\ge{}&
\frac{\Gamma(r_0)+\Gamma(r_1)}2
-\Gamma\!\left(\frac{r_0+r_1}{2}\right)\\
&+\Gamma(1/2)\delta
-j(m)-h_2(m)\\
&+\Phi'(|1-2\delta|)A
+\frac{V}{2\ln2}.
\end{aligned}
}
\tag{4.6}
\]

Equation (4.6), not a sign-free norm, is the new compiler-facing inequality.

### Equality structure of the scalar relaxation

For \(0<|\rho|<1\), equality in the scalar reduction
\[
\mathbb E\Phi(X)\ge\Phi(|\rho|)
\]
requires both equality in strict Jensen and equality in the triangle inequality. Hence
\[
\boxed{c_S=\rho\quad\text{for every }S\text{ with }T_S>0.}
\tag{4.7}
\]
Equivalently, every active spectral pair has one common signed angle:
\[
\frac{2a_Sb_S}{a_S^2+b_S^2}=\rho.
\]
Thus any near-counterexample which nearly saturates the scalar relaxation must be a near-isoclinic, sign-coherent Boolean restriction pair. This is a concrete Boolean rigidity target.

## 5. Sharp obstruction: no better bound can use only the scalar overlap moments

The lower envelope in (4.5) is optimal if one forgets Boolean realizability and keeps only the exact balanced-pivot angular moments.

Fix any \(\rho\in(-1,1)\). Choose two angular atoms of equal weight with
\[
\sin(2\alpha_+)=\sin(2\alpha_-)=\rho,
\qquad
\cos(2\alpha_+)=-\cos(2\alpha_-).
\]
Then
\[
\mathbb E\cos(2\alpha)=0,\qquad
\mathbb E\sin(2\alpha)=\rho,
\]
which are exactly the balanced-pivot normalization/correlation constraints, while
\[
X=|\rho|
\]
identically. Hence
\[
\mathbb E\Phi(X)=\Phi(|\rho|).
\]

Therefore

\[
\boxed{\text{Any universal improvement over (4.5) must use Booleanity
(or additional source structure), not only }t,\delta\text{ and the two angular moments.}}
\tag{5.1}
\]

This is a rigorous obstruction to another scalar-envelope iteration. It explains why the account04/B16 warning against independent scalarization is structural rather than merely a bad constant.

## 6. Applied peer theorem: arbitrary balanced tensor tubes are paid, not just literal tubes

The account04/B16 theorem treated
\[
f_0=x,\qquad f_1=xh(y).
\]
Its proof in fact tensorizes exactly.

Let \(g(X)\) be **any balanced Boolean function** on one product space and \(h(Y)\) any Boolean function on a disjoint product space. Set
\[
f_0(X,Y)=g(X),\qquad
f_1(X,Y)=g(X)h(Y).
\tag{6.1}
\]
Let \(\delta=\Pr[h=-1]\).

The branch spectral laws factor:
\[
P_0=P_g\otimes\delta_\varnothing,\qquad
P_1=P_g\otimes P_h.
\]
The \(X\)-spectral coordinate is independent of the branch/layer variables. Therefore
\[
H(B\mid S_X,S_Y)=H(B\mid S_Y),
\qquad
I((S_X,S_Y);J)=I(S_Y;J).
\tag{6.2}
\]
So the *entire exact joint credit* is identical to the account04/B16 character-tube credit, for every pivot bias \(t\). Since \(g\) is balanced,
\[
r_0=r_1=\frac12,
\]
so its potential Jensen term also vanishes.

In particular, at a balanced pivot the account04/B16 cap-six theorem applies verbatim:

\[
\boxed{
\Gamma(1/2)\ge6
\quad\Longrightarrow\quad
\mathcal L_{\Gamma,j}\ge0
}
\tag{6.3}
\]
for every pair (6.1), with no bound on the arity, influence, Fourier degree, or internal geometry of \(g\) or \(h\).

At the live cap \(C_*=6.5218512\), its explicit inherited reserve is
\[
\boxed{
\mathcal L_{\Gamma_*,j}
\ge
0.5218512\,\delta
+
\frac{2\delta^2(4\delta^2-2\delta+1)}
     {2\delta^2-2\delta+1}.
}
\tag{6.4}
\]

This substantively consumes and enlarges the named other-account theorem: the base character may be replaced by an arbitrary balanced Boolean function.

## 7. What this changes in the universal FEI implication

**Old missing implication.** The account04/B17 restriction-tree theorem reduces `LIMIT-PRIME-GATE-LIFT-v1` to controlling the exact local gluing terms \(\mathcal R+\mathcal C\). Account04/B16 showed that separately lower-bounding the two pieces of \(\mathcal C\) can reverse the sign, and closed only a single-character common-atom family.

**New proved inference.**

1. At every balanced pivot, the exact joint credit for an arbitrary Boolean restriction pair is the one-dimensional signed-overlap functional (3.2).
2. Its retained overlap kernel is strongly convex with the exact curvature (4.2), giving the universal quantitative rigidity estimate (4.6).
3. The scalar moment relaxation is sharp; a proof cannot improve it without using Boolean realizability or additional source structure.
4. The complete arbitrary-balanced-base tensor-tube family is safe at cap six, so recursive/tensor attachment of an arbitrary residual Boolean function to a balanced base is not a counterexample mechanism.

**Still missing.** To prove full FEI from `LIMIT-PRIME-GATE-LIFT-v1`, one still must exclude a composition-prime gate whose restriction tree contains a local node with negative \(\mathcal L_{\Gamma_*}\). At a balanced pivot, (4.6) localizes such a node to the explicit near-isoclinic/sign-coherent corridor unless the potential midpoint deficit itself pays it. At an unbalanced pivot, the exact angular identity (2.1) is available but the corresponding optimal Booleanity-sensitive lower bound is still open.

The next mathematically decisive target is therefore not another scalar envelope. It is:

> **Balanced rigidity target.** Prove that an actual Boolean restriction pair satisfying
> \(A+V=o(1)\) in the dangerous small-\(\delta\) regime must have enough additional structure (e.g. decomposability/one-sided nesting or a paid output-potential midpoint term) to make \(\mathcal L_{\Gamma_*}\ge0\); or construct a genuine Boolean pair violating that claim.

That is strictly narrower than the previous unrestricted joint-credit problem and is directly plugged into the exact local-to-global margin theorem.

## 8. Verification

The adjacent deterministic checker independently verifies the source-exact identity (3.2) and the strong-convexity inequality on every ordered pair of Boolean functions through three variables: **65,808 ordered pairs**. Maximum numerical error in the exact credit identity was \(2.22\times10^{-16}\); the minimum observed strong-convexity slack was nonnegative to displayed precision.

It also checks the tensorization statement (6.2) on all six balanced two-bit bases and all sixteen two-bit residuals, **96 tensor tubes**, with maximum credit discrepancy \(0\) to displayed precision.

The finite checks are diagnostics only. The theorems above are analytic and do not rely on finite enumeration.

Scoped privacy review: only FEI mathematics, repository-relative source identifiers, nonsecret hashes, and sanitized run metadata are included. No credentials, scheduler identifiers, machine paths, benchmark gold, unrelated private data, email/Drive content, paid/remote compute, public posting, or permission changes are present.

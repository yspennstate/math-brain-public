# account01/B13 — common-sign entropic Booleanity projection and sparse-suspension exactness

**Assignment:** FEI-20260922-account01-B13, “Common-sign Booleanity certificate”.  
**Classification:** `ESSENTIAL_STEP_APPLIED / JOINT_COMMON_SIGN_KL / FULL_FEI_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Current target and source state

This run follows owner programme `FEI-ALL-TEAM-20260922T095941Z`, revision `2026-09-22.3`. The current state keeps full uniform-cube FEI open and retires the old fixed read-once potential, the 0.268204856 / 0.337 / 0.34 quadratic repairs at their stated scopes, raw terminal `U4=O(J)`, and unweighted convolution-L2 payment. No such statement is used below.

The assignment asks for a certificate that uses **one common Fourier sign assignment across several Booleanity equations**, rather than minimizing signs independently equation by equation, and that preserves the rare-event logarithm lost by unweighted L2 aggregation.

The exact base inputs are:

1. **Biased Booleanity gap:**  
   `yspennstate/math-open-problems@603b35e74227d1c2d8ee34c0c527c439c686e30b:proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`.  
   For the actual biased Fourier coefficient vector `a`, every nonempty multiplication equation is
   \[
   a^TM_Ua=0,
   \]
   and the equation-by-equation certificate is
   \[
   K_{\rm occ}\ge {1\over4v\ln2}
   \max_{U\ne\varnothing}{\mathfrak g_U(Q_r;p,q)^2\over L_U^2}.
   \tag{0.1}
   \]

2. **Exact influence I-projection:**  
   `yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04:proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.  
   For every law `R` on nonempty spectral subsets with occurrence marginals `r`,
   \[
   D_2(R\Vert Q_r)=H_{\max}(r)-H(R).
   \tag{0.2}
   \]

3. **Unweighted-L2 obstruction:**  
   `yspennstate/math-open-problems@7ec649dfb3d1ab2f92855f2069590fca2ac956dd:proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md`.  
   On the genuine sparse suspension
   \[
   F_m(y,x)=y\,g_m(x),\qquad
   g_m(x)=1-2\mathbf1_{\{x=0\}},\qquad
   p=2^{1-m},
   \tag{0.3}
   \]
   the exact dependence credit is `Theta(m I)` while the complete unweighted convolution energy is only `Theta(I)`.

The **latest compatible named partner result actually consumed and applied** is account02/B13:

`yspennstate/math-open-problems@a1b98a69cf168e8005c06190b71e76b456ad2cc9:proofnet24/P03-fei/fleet-2026-09-22/account02/B13/20260922T105348Z-selector-conditional-booleanity/REPORT.md`.

For a physical selector `j` of bias `t`, residual equation `U`, and actual children `0,1`, it proves
\[
\mathfrak c_{j,U}^2
=(1-t)g_{0,U}^2+t g_{1,U}^2
\tag{0.4}
\]
and
\[
(1-t)v_0K_0+t v_1K_1
\ge {1\over4\ln2}
\max_{U\ne\varnothing}{\mathfrak c_{j,U}^2\over L_U^2},
\tag{0.5}
\]
with **no selector condition-number factor**. Section 4 below upgrades (0.5) from independent per-equation sign minimization to one common-sign entropic bank in each actual child.

## 1. Common-sign Boolean feasibility

Fix an interior product input bias `p=(p_1,...,p_k)`, a nonconstant output with
\[
q=\Pr(G=-1),\qquad v=4q(1-q)>0,
\]
and let
\[
m_0=\mathbb E G=1-2q.
\]
Let `r=(r_i)` be the occurrence marginals of the actual nonempty biased spectral law, and let `Q_r` be the maximum-entropy nonempty I-projection with those marginals.

For a probability law `R` on nonempty subsets with the same occurrence marginals `r`, and a **single common sign vector**
\[
\sigma=(\sigma_S)_{S\ne\varnothing}\in\{\pm1\}^{2^k-1},
\]
define amplitudes
\[
a^{R,\sigma}_{\varnothing}=m_0,\qquad
a^{R,\sigma}_S=\sigma_S\sqrt{vR(S)}.
\tag{1.1}
\]
Let `M_U` be the exact biased multiplication matrices from the source theorem.

Define the common-sign Boolean feasible set
\[
\mathcal B(p,q,r):=
\left\{
R:\begin{array}{l}
R\text{ has occurrence marginals }r,\\[1mm]
\exists\ \sigma\text{ such that }
(a^{R,\sigma})^TM_Ua^{R,\sigma}=0\\
\text{for every nonempty }U
\end{array}
\right\}.
\tag{1.2}
\]

### Lemma 1.1 — exact Boolean meaning

`R in B(p,q,r)` if and only if the amplitudes (1.1), for one common sign choice, are the biased Fourier coefficients of an actual Boolean function with mean `m_0` and spectral occurrence vector `r`.

#### Proof

The constant coefficient of the square of the represented function is
\[
m_0^2+v\sum_{S\ne\varnothing}R(S)=m_0^2+v=1.
\]
For nonempty `U`, the coefficient of `phi_U` in the square is exactly
\[
(a^{R,\sigma})^TM_Ua^{R,\sigma}.
\]
Thus all equations in (1.2) say that the square has Fourier expansion equal to the constant `1`. The product basis is complete and the product measure has full support, so the represented function satisfies `G^2=1` at every cube point. Hence it is Boolean. The converse is exactly the biased multiplication identity. QED.

This is the key difference from (0.1): the signs are not reoptimized separately for different `U`. One sign vector must satisfy the **entire Boolean multiplication system simultaneously**.

## 2. New nonlinear/logarithmic certificate

Define the **common-sign entropic Booleanity certificate**
\[
\boxed{
\mathcal K_{\rm com}(p,q,r)
:=
\inf_{R\in\mathcal B(p,q,r)}
D_2(R\Vert Q_r).
}
\tag{2.1}
\]
If the feasible set is empty, set the infimum to `+infinity`; for an actual Boolean source it is nonempty.

By the I-projection identity (0.2),
\[
\boxed{
\mathcal K_{\rm com}
=
H_{\max}(r)
-\sup_{R\in\mathcal B(p,q,r)}H(R).
}
\tag{2.2}
\]
Thus the certificate is intrinsically **entropic/logarithmic**, not a fixed quadratic compression of the Booleanity equations.

### Theorem 2.1 — universal common-sign KL lower bound

For every nonconstant Boolean gate at every interior product bias,
\[
\boxed{
K_{\rm occ}\ge \mathcal K_{\rm com}(p,q,r).
}
\tag{2.3}
\]

Moreover it universally dominates the existing equation-by-equation gap:
\[
\boxed{
\mathcal K_{\rm com}(p,q,r)
\ge
{1\over4v\ln2}
\max_{U\ne\varnothing}
{\mathfrak g_U(Q_r;p,q)^2\over L_U^2}.
}
\tag{2.4}
\]

#### Proof

The actual nonempty spectral law `P` belongs to `B(p,q,r)` with its actual Fourier signs, so
\[
K_{\rm occ}=D_2(P\Vert Q_r)\ge \inf_{R\in\mathcal B}D_2(R\Vert Q_r),
\]
which is (2.3).

For (2.4), fix any feasible `R` and one common sign vector `sigma` realizing it. Form `a=a^{R,sigma}` and form `b` using the **same signs** and the I-projection magnitudes:
\[
b_\varnothing=m_0,\qquad b_S=\sigma_S\sqrt{vQ_r(S)}.
\]
For each nonempty `U`, feasibility gives `a^TM_Ua=0`, while the definition of the source gap gives
\[
\mathfrak g_U\le |b^TM_Ub|.
\]
Therefore
\[
\mathfrak g_U
\le |b^TM_Ub-a^TM_Ua|
\le 2L_U\|b-a\|_2.
\]
Because the empty amplitudes agree,
\[
\|b-a\|_2^2
=
v\sum_{S\ne\varnothing}
\left(\sqrt{Q_r(S)}-\sqrt{R(S)}\right)^2.
\]
KL in bits dominates squared Hellinger distance:
\[
D_2(R\Vert Q_r)
\ge {1\over\ln2}
\sum_S(\sqrt R-\sqrt Q_r)^2.
\]
Hence
\[
D_2(R\Vert Q_r)
\ge {\mathfrak g_U^2\over4vL_U^2\ln2}.
\]
Take the maximum over `U`, then the infimum over all common-sign feasible `R`. QED.

The strict advantage can come from **sign frustration across equations** and from the logarithmic objective itself. Neither is retained by independent per-equation minimization followed by an L2/Hellinger conversion.

## 3. Sparse suspension: the joint certificate is exact and keeps the rare-event logarithm

Consider the genuine Boolean suspension from (0.3), with `m>=3` and
\[
p=2^{1-m}.
\]
Its full uniform spectral law has the fresh coordinate `y` present with probability `1`, while each old coordinate has occurrence probability `p`. The I-projection therefore has `y` deterministically present and the old coordinates independent Bernoulli(`p`):
\[
Q_m(T)=p^{|T|}(1-p)^{m-|T|},\qquad T\subseteq[m].
\tag{3.1}
\]

### Lemma 3.1 — rigidity from the common Boolean system

Every Boolean spectral law in the common-sign feasible set with these occurrence marginals has exactly the same squared Fourier magnitudes as a one-point defect:
\[
P_m(\varnothing)=(1-p)^2,\qquad
P_m(T)=p^2\quad(T\ne\varnothing).
\tag{3.2}
\]

#### Proof

The marginal `r_y=1` forces every nonzero Fourier coefficient to contain `y`. Hence every feasible Boolean function factors as
\[
F(y,x)=\chi_y(y)\,h(x)
\]
for an actual Boolean `h` on the old `m`-cube. For each old coordinate,
\[
\operatorname{Inf}_i(h)=p=2^{1-m}.
\]
Let `A` be the smaller sign class of `h`. In direction `i`, the number of bichromatic undirected edges is
\[
|\partial_iA|
=
2^{m-1}\operatorname{Inf}_i(h)=1.
\]
Thus
\[
|\partial A|=m.
\tag{3.3}
\]

The cube edge-isoperimetric inequality gives, for `s=|A|<=2^{m-1}`,
\[
|\partial A|\ge s\log_2{2^m\over s}.
\tag{3.4}
\]
If `s>=2`, the concavity of `s(m-\log_2s)` on `[2,2^{m-1}]` shows its minimum is at an endpoint. For `m>=3`,
\[
2(m-1)>m,\qquad 2^{m-1}>m,
\]
contradicting (3.3). Therefore `s=1`: up to a global sign, `h` differs from a constant at exactly one vertex.

For a one-point defect,
\[
\widehat h(\varnothing)=1-{2\over2^m}=1-p,
\qquad
|\widehat h(T)|={2\over2^m}=p\quad(T\ne\varnothing).
\]
Squaring gives (3.2). QED.

### Theorem 3.2 — exact rare-event recovery

For the sparse suspension,
\[
\boxed{
\mathcal K_{\rm com}(F_m)=K_{\rm occ}(F_m)
=m h_2(p)-H(P_m).
}
\tag{3.5}
\]
Moreover
\[
H(P_m)
=
-(1-p)^2\log_2(1-p)^2
-(2p-p^2)\log_2 p^2.
\tag{3.6}
\]

For `m>=5`,
\[
\boxed{
\mathcal K_{\rm com}
\ge (m-1)(m-5)p.
}
\tag{3.7}
\]
Since
\[
I(F_m)-1=mp,
\]
we obtain
\[
\boxed{
{\mathcal K_{\rm com}\over I(F_m)-1}
\ge {(m-1)(m-5)\over m}
\longrightarrow\infty.
}
\tag{3.8}
\]

#### Proof

Lemma 3.1 makes the feasible magnitude law unique, so the infimum (2.1) is exactly `D(P_m||Q_m)`. Equation (0.2) gives (3.5), and (3.6) is the entropy of one atom of mass `(1-p)^2` and `2^m-1` atoms of mass `p^2`.

For the lower bound,
\[
h_2(p)\ge p\log_2(1/p)=p(m-1),
\]
hence
\[
H(Q_m)=m h_2(p)\ge mp(m-1).
\]
Also
\[
-2(1-p)^2\log_2(1-p)
\le {2p(1-p)\over\ln2}<3p\le p(m-1)
\]
for `m>=4`, while
\[
(2p-p^2)(2m-2)\le4p(m-1).
\]
Thus `H(P_m)<=5p(m-1)`, proving (3.7) and (3.8). QED.

The sharper source asymptotic is
\[
{K_{\rm occ}\over mp}
=
m-5+{1\over\ln2}+o(1),
\]
but the elementary lower bound above already proves the needed logarithmic-scale retention.

### The old max-gap certificate provably loses this family

At uniform input bias, every `L_U=1`. If a shift `U` contains `y`, the I-projection support is toggled out of the `y`-active sector and the reference residual is exactly zero.

If `U` is a nonempty old-coordinate shift, the involution `T -> T triangle U` partitions the old spectral cube into disjoint pairs. For this **single** equation, pair-product signs can be chosen independently, so
\[
\mathfrak g_U
=
2\min_{\epsilon_{\rm pair}=\pm1}
\left|\sum_{\rm pairs}
\epsilon_{\rm pair}\sqrt{Q_m(T)Q_m(T\triangle U)}
\right|.
\tag{3.9}
\]
The elementary discrepancy bound `min |sum epsilon_j w_j| <= max_j w_j` yields
\[
\mathfrak g_U\le
2\max_T\sqrt{Q_m(T)Q_m(T\triangle U)}.
\]
For `U ne empty`,
\[
Q_m(T)Q_m(T\triangle U)\le p,
\]
because every toggled coordinate contributes the factor `p(1-p)` and every other factor is at most one. Therefore
\[
\boxed{\mathfrak g_U^2\le4p}
\tag{3.10}
\]
for every shift, and the entire source max-gap certificate obeys
\[
\boxed{
{1\over4\ln2}\max_{U\ne\varnothing}\mathfrak g_U^2
\le {p\over\ln2}.
}
\tag{3.11}
\]
Relative to the actual influence excess,
\[
\boxed{
{\text{max-gap certificate}\over I(F_m)-1}
\le {1\over m\ln2}\to0.
}
\tag{3.12}
\]

Thus on one and the same genuine Boolean sparse-suspension family,

- independent equation-by-equation sign minimization is `o(I)`;
- the common-sign entropic certificate equals the full `K_occ`;
- the latter is `Theta(mI)` and therefore retains the rare-event logarithm.

Quantitatively, combining (3.7) and (3.11), for `m>5`
\[
{\mathcal K_{\rm com}\over \text{max-gap certificate}}
\ge
(\ln2)(m-1)(m-5),
\tag{3.13}
\]
a quadratic separation.

This meets the assignment's sparse-suspension loss test analytically; no finite experiment is needed.

## 4. Direct upgrade of the latest account02/B13 selector theorem

Return to the exact physical selector notation of the partner theorem. For child `b in {0,1}`, define its own common-sign certificate
\[
\mathcal K_{{\rm com},b}
=
\inf_{R\in\mathcal B_b}D_2(R\Vert Q_b),
\tag{4.1}
\]
using the actual signed child mean, actual original-coordinate occurrence marginals, and all residual biased Booleanity equations.

Theorem 2.1 applied inside each actual child gives
\[
K_b\ge \mathcal K_{{\rm com},b}
\ge
{g_{b,U}^2\over4v_bL_U^2\ln2}
\quad\text{for every residual }U.
\tag{4.2}
\]
Therefore the partner's exact selector transport (0.4) yields the stronger bank
\[
\boxed{
(1-t)v_0K_0+t v_1K_1
\ge
(1-t)v_0\mathcal K_{{\rm com},0}
+t v_1\mathcal K_{{\rm com},1}.
}
\tag{4.3}
\]
For every residual `U`,
\[
(1-t)v_0\mathcal K_{{\rm com},0}
+t v_1\mathcal K_{{\rm com},1}
\ge
{\,(1-t)g_{0,U}^2+t g_{1,U}^2\over4L_U^2\ln2},
\]
hence
\[
\boxed{
(1-t)v_0\mathcal K_{{\rm com},0}
+t v_1\mathcal K_{{\rm com},1}
\ge
{1\over4\ln2}
\max_{U\ne\varnothing}
{\mathfrak c_{j,U}^2\over L_U^2}.
}
\tag{4.4}
\]

Equation (4.4) is the exact requested substantive application of the newest partner result. It preserves their key gain: **no factor `L_{U union {j}}` and no rare-selector condition-number loss**. At the same time it replaces equation-by-equation child sign minimization by one common sign vector satisfying the whole Boolean system in each child.

If a safe-direction currency `lambda L_j` is also present, the partner's local term can simply be retained:
\[
(1-t)v_0K_0+t v_1K_1+\lambda L_j
\ge
(1-t)v_0\mathcal K_{{\rm com},0}
+t v_1\mathcal K_{{\rm com},1}
+\lambda L_j.
\tag{4.5}
\]
No child slack, source sign, or original-coordinate marginal is discarded.

## 5. What changed, and the exact remaining implication

**Old missing implication.** Strengthen the arbitrary-bias max-gap Booleanity certificate by coupling several equations with one source-coherent sign assignment, without falling back to unweighted L2 and without losing the sparse-event logarithm.

**New proved implication.**

1. The common-sign feasible set (1.2) is exactly the set of Boolean spectral magnitude laws with the prescribed mean and original-coordinate occurrence marginals.
2. Its entropy projection (2.1) is a universal lower bound on `K_occ`.
3. It universally dominates the source max-gap certificate.
4. On the genuine sparse suspension `F_m`, it is **exactly equal to `K_occ`**, while the source max-gap certificate is at most `p/ln2=o(I)`.
5. It upgrades account02/B13's selector-conditional theorem without reintroducing the selector condition number.

The assignment target is therefore met at theorem level. This does **not** prove FEI.

The next unpaid universal implication is now precise:

> Find a source-valid lower bound on `K_com(p,q,r)` in terms of the actual negative first-moment Bellman residual `[-B_inf^Gamma]_+` for every gate/bias of a surviving candidate potential, or prove that the selector recursion plus child `K_com` banks necessarily supplies that payment. Equivalently, develop a tractable relaxation of the entropy maximization over the common-sign Boolean feasible set which loses at most `O(I)` on sparse suspensions.

A fixed quadratic norm of the Boolean equations cannot do this; the entropy objective is essential on the sparse family. No full FEI proof, universal candidate nonnegativity, or counterexample to FEI is claimed.

## 6. Scope, provenance, and safety

All mathematics above concerns the authorized private FEI repositories only. No credentials, scheduler identifiers, machine paths, benchmark gold, unrelated private data, paid/remote compute, workflows, email, Drive, public posting, or permission changes are used. Repository synchronization is not native memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.

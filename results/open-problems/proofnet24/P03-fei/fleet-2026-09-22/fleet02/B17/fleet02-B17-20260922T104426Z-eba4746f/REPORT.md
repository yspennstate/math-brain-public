# fleet02/B17 — credit-preserving Bellman repair: exact KL exchange and a binary zero-KL no-go

**Run:** `fleet02-B17-20260922T104426Z-eba4746f`  
**Assignment:** FEI-20260922-fleet02-B17 — `Credit-preserving potential repair`  
**Programme:** FEI-ALL-TEAM-20260922T095941Z  
**Control revision consumed:** `2026-09-22.3`  
**Classification:** `ESSENTIAL_STEP_APPLIED / REPAIR_MECHANISM_OBSTRUCTION / REPLACEMENT_LEDGER_DERIVED`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

MODEL SELF-REPORT: GPT-5.6 Sol.  
REQUESTED REASONING: maximum actually supported.  
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / scheduler field not exposed in the fleet02 inventory.  
PROVIDER REASONING TOKENS / THINKING TIME: NOT_EXPOSED.

## 0. Exact target, correction state, and outcome

The assignment target is to avoid charging a universal safe-direction center increase when the **actual Boolean source already carries irreducible KL reserve**. The source-exact all-gate ledger is

\[
R_\Gamma(G;p)=B_{\inf}^{\Gamma}(G;p)+K_{\rm occ}(G;p),\qquad
D_\Gamma(G;p)=vR_\Gamma(G;p),
\tag{0.1}
\]

where \(v=V_{p_{\rm out}}\), \(P=w^+\) is the actual nonempty biased squared Fourier law,

\[
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P),
\tag{0.2}
\]

and \(Q_r\) is the maximum-entropy conditional-product law with the actual coordinate-occurrence marginals \(r_i=\operatorname{It}_i/v\).

Fresh coordination state `FEI-20260922T1000Z-v1` and mandatory corrections 01--14 were consumed. In particular:

* the old fixed potential and quadratic coefficients \(0.337,0.34\) are refuted at their exact scopes;
* the shaped direction is a candidate/witness repair, not a universal FEI proof;
* the exact hierarchy KL must be retained;
* unweighted \(L^2\), raw \(U_4\), and fixed/low-depth KL compression are retired;
* the broad arbitrary safe-cone selector claim is `NEEDS_REVALIDATION`.

The live correction inbox was empty both at startup and at the prepublication refresh.

**Outcome.** A natural zero-center version of the assignment is impossible: no nonzero bounded symmetric one-variable potential perturbation can have its negative gate contribution universally insured by \(K_{\rm occ}\), even with an arbitrary nonnegative source-dependent multiplier. The obstruction is the exact fact that every binary Boolean gate has \(K_{\rm occ}=0\). In the same run I derive the replacement mechanism that does preserve the full reserve: an exact physical-restriction exchange identity for the pair \((vB_{\inf},vK_{\rm occ})\). It keeps every sign, child term, and multiscale KL credit and shows exactly where double-spending would occur.

This is an accepted obstruction/replacement step for the card. It is not FEI closure.

## 1. Sources actually consumed

### 1.1 Exact influence I-projection

Repository `yspennstate/math-open-problems`, commit
`4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

It proves (0.1)--(0.2) and the maximum-entropy formula. If
\(\mu=\sum_i r_i>1\), the unique \(c\in(0,1]\) satisfies

\[
1-c=\prod_i(1-cr_i),
\tag{1.1}
\]

and

\[
H_{\max}(r)=\frac{\sum_i h_2(cr_i)-h_2(c)}{c}.
\tag{1.2}
\]

### 1.2 Exact disjoint-composition hierarchy KL

Repository `yspennstate/math-open-problems`, commit
`2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`.

For disjoint composition it proves

\[
K_{\rm occ}(F)=K_{\rm occ}(G)+\sum_i\alpha_iK_{\rm occ}(f_i)+C_{\rm hier},
\qquad C_{\rm hier}\ge0,
\tag{1.3}
\]

and, crucially here, it proves that **every nonconstant binary Boolean gate at every interior product bias has \(K_{\rm occ}=0\)**, because a probability law on \(\{\{1\},\{2\},\{1,2\}\}\) is uniquely determined by its two occurrence marginals.

### 1.3 New completed physical-restriction KL chain

Repository `yspennstate/math-open-problems`, commit
`3a5fccff414043be05a0c7f2f219dabd9b44708b`, path
`proofnet24/P03-fei/fleet-2026-09-22/fleet01/B15/b15-20260922T103236Z-restriction-iprojection-chain/REPORT.md`.

For a genuine restriction of physical coordinate \(j\) at bias \(s\), with parent full spectral law \(W\), child full laws \(U,V\), it defines

\[
\mathcal K(X)=v_XK_{\rm occ}(X^+)
\]

and proves exactly

\[
\boxed{
\mathcal K(W)
=(1-s)\mathcal K(U)+s\mathcal K(V)
+C_{\rm marg}+C_{\rm erase}+C_{\rm pair}
-\operatorname{JS}_s(U,V).
}
\tag{1.4}
\]

All three \(C\)-terms are nonnegative. The negative Jensen-Shannon term is essential, and the theorem retains the child KL with coefficient one.

### 1.4 Mandatory recursive-majority preflight

Repository `yspennstate/math-open-problems`, commit
`bff0d7b6c21485f386841c42582eb04f32705046`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`.

For depth-\(m\) recursive ternary majority \(M_m\),

\[
I(M_m)=\mu_m=(3/2)^m,\qquad H(M_m)=4(\mu_m-1),\qquad r_i=2^{-m},
\tag{1.5}
\]

and its I-projection satisfies

\[
H_{\max}(r^{(m)})\ge \mu_m m-2.
\tag{1.6}
\]

It refutes fixed/low-depth labelled KL extraction. The full \(K_{\rm occ}\), however, remains large and must be preserved.

### 1.5 Named partner result actually applied

The required partner is `fleet03/B17`. I consumed its latest compatible completed result:

repository `yspennstate/math-open-problems`, commit
`9b4814e50b1215342abb6de666809948169e8a9b`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B17/20260922T100239Z-quarterhalf-dyadic-output/REPORT.md`.

It gives the exact actual-Boolean quarter/half input geometry and its closest non-subcube dyadic-output witness. Section 5 below applies its exact Walsh formulas to the \(B_{\inf}+K_{\rm occ}\) ledger, rather than merely citing its finite exclusion.

## 2. Exact credit-exchange Bellman identity under physical restriction

This is the source-dependent replacement mechanism.

Let \(G\) be a Boolean function at a product bias and restrict coordinate \(j\), whose bias is \(s\in(0,1)\). Let \(G_0,G_1\) be the two restrictions, with full squared spectral laws \(U,V\). Let \(W\) be the parent full squared spectral law. Write output biases

\[
q_b=\Pr[G_b=-1],\qquad q=(1-s)q_0+s q_1,
\]

and \(v_b=V_{q_b}\), \(v=V_q\). For the potential \(\Gamma\), put

\[
a_s=\frac{\Gamma(s)+h_2(V_s)}{V_s},
\qquad
J_\Gamma=(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q).
\tag{2.1}
\]

Erase the selector label \(j\) from \(W\). The erased law is exactly

\[
E=(1-s)U+sV.
\tag{2.2}
\]

Within each erased packet \(T\), put

\[
\theta_T=\frac{W(T\cup\{j\})}{E_T}
\]

when \(E_T>0\), and define the exact within-pair layer entropy

\[
H_{\rm layer}:=\sum_T E_T h_2(\theta_T).
\tag{2.3}
\]

The standard finite-alphabet mixture identity and the exact two-layer split give

\[
H(W)
=(1-s)H(U)+sH(V)
+\operatorname{JS}_s(U,V)+H_{\rm layer}.
\tag{2.4}
\]

For each physical coordinate \(i\ne j\), the occurrence/influence is linear under restriction,

\[
\operatorname{It}_i(G)
=(1-s)\operatorname{It}_i(G_0)+s\operatorname{It}_i(G_1).
\tag{2.5}
\]

Therefore, directly from the all-gate defect definition,

\[
\boxed{
D_\Gamma(G)
=(1-s)D_\Gamma(G_0)+sD_\Gamma(G_1)
+\operatorname{It}_j a_s+J_\Gamma
-\operatorname{JS}_s(U,V)-H_{\rm layer}.
}
\tag{2.6}
\]

Equation (2.6) is the full residual: no KL has been removed.

Now define the weighted first-moment Bellman term

\[
\mathcal B_\Gamma(G):=vB_{\inf}^{\Gamma}(G),
\qquad
\mathcal K(G):=vK_{\rm occ}(G).
\]

Since \(D_\Gamma=\mathcal B_\Gamma+\mathcal K\), subtract the newly completed exact KL chain (1.4) from (2.6). The Jensen-Shannon term cancels **exactly**:

\[
\boxed{
\begin{aligned}
\mathcal B_\Gamma(G)
={}&(1-s)\mathcal B_\Gamma(G_0)+s\mathcal B_\Gamma(G_1)\\
&+\operatorname{It}_j a_s+J_\Gamma-H_{\rm layer}\\
&-C_{\rm marg}-C_{\rm erase}-C_{\rm pair}.
\end{aligned}
}
\tag{2.7}
\]

### Why (2.7) matters

The positive reference-movement quantities \(C_{\rm marg},C_{\rm erase},C_{\rm pair}\) are genuine KL credits in \(\mathcal K\), but the same quantities make \(\mathcal B_\Gamma\) more negative by exactly the same amount. Thus one cannot add them to the total residual as if they were a second independent bank. The exact source ledger is

\[
\Delta D=\Delta\mathcal B+\Delta\mathcal K,
\]

not three separately spendable copies of the same information.

Equation (2.7) is also genuinely multiscale. Iterating it retains the complete child \(\mathcal K\) at coefficient one through (1.4), rather than replacing it by a fixed-depth projection or an unweighted quadratic statistic.

## 3. Main obstruction — zero-center potential repair cannot be financed by \(K_{\rm occ}\)

The card asks for a potential repair that uses the actual KL reserve rather than paying unnecessary center cost. The following theorem shows a sharp limitation on that idea.

### Theorem 3.1 — `KL-INSURED-CENTER-NEUTRAL-NOGO-v1`

Let \(\psi:(0,1)\to\mathbb R\) be bounded and symmetric,

\[
\psi(p)=\psi(1-p),\qquad \psi(1/2)=0.
\tag{3.1}
\]

Its contribution to the all-gate defect is

\[
\Delta_\psi D(G;p)
=
\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}\psi(p_i)
-\psi(p_{\rm out}).
\tag{3.2}
\]

Suppose that for every genuine finite Boolean gate \(G\), every interior product bias \(p\), and some arbitrary nonnegative real multiplier
\(\lambda(G,p)\),

\[
\boxed{
\Delta_\psi D(G;p)
+\lambda(G,p)\,vK_{\rm occ}(G;p)\ge0.
}
\tag{3.3}
\]

Then

\[
\boxed{\psi\equiv0.}
\tag{3.4}
\]

In words: **even an arbitrarily large source-dependent multiple of the existing irreducible occurrence KL cannot universally insure a nonzero bounded center-preserving one-variable potential direction.**

#### Proof

By the binary-gate theorem in the exact hierarchy source, every nonconstant two-input Boolean gate has

\[
K_{\rm occ}=0.
\tag{3.5}
\]

Apply (3.3) to two-input AND with input biases \(x,y\in(0,1)\) and output bias \(xy\). The exact influence coefficients are

\[
\frac{\operatorname{It}_1}{V_x}=y,\qquad
\frac{\operatorname{It}_2}{V_y}=x,
\]

so (3.3) reduces to

\[
\boxed{
y\psi(x)+x\psi(y)-\psi(xy)\ge0
\qquad (x,y\in(0,1)).
}
\tag{3.6}
\]

Set \(y=1/2\). Since \(\psi(1/2)=0\),

\[
\psi(x/2)\le \frac12\psi(x).
\tag{3.7}
\]

For \(z\in(0,1/2)\), define the tent map

\[
T(z)=
\begin{cases}
2z,&0<z\le1/4,\\
1-2z,&1/4<z<1/2.
\end{cases}
\tag{3.8}
\]

By symmetry, (3.7) gives

\[
\psi(z)\le\frac12\psi(Tz).
\tag{3.9}
\]

Iterating,

\[
\psi(z)\le 2^{-n}\psi(T^n z).
\]

Boundedness of \(\psi\) lets \(n\to\infty\), giving

\[
\psi(z)\le0\qquad(0<z<1/2).
\tag{3.10}
\]

Symmetry gives the same sign on \((1/2,1)\).

Now fix \(x\in(1/2,1)\) and take

\[
y=\frac1{2x}\in(1/2,1),
\qquad xy=\frac12.
\]

Equation (3.6) becomes

\[
y\psi(x)+x\psi(y)\ge0.
\]

Both terms on the left are nonpositive by (3.10) and symmetry, so both vanish. Hence \(\psi(x)=0\) for every \(x\in(1/2,1)\), and symmetry gives \(\psi=0\) on \((0,1/2)\). Together with (3.1), \(\psi\equiv0\). QED.

### Consequence

The exact \(K_{\rm occ}\) reserve can reduce a **source-dependent** Bellman debt, but it cannot be converted into a nontrivial free center-neutral one-variable potential correction. Binary gates have no such reserve. Any nonzero center-neutral repair must instead:

1. spend pre-existing base slack on binary/AND constraints;
2. use another genuinely independent source currency; or
3. remain source/state-dependent rather than collapsing to a one-variable \(\psi\).

This is a rigorous obstruction to a natural repair mechanism, not a refutation of FEI.

## 4. Recursive-majority preflight — why the replacement must keep the full multiscale KL

For depth-\(m\) recursive ternary majority, the consumed source gives (1.5)--(1.6). Hence

\[
\begin{aligned}
K_{\rm occ}(M_m)
&=H_{\max}(r^{(m)})-H(M_m)\\
&\ge \mu_m m-2-4(\mu_m-1)\\
&=\boxed{\mu_m(m-4)+2}.
\end{aligned}
\tag{4.1}
\]

For any finite center \(C\),

\[
B_{\inf}(M_m)
=C(\mu_m-1)-H_{\max}(r^{(m)})
\le
\boxed{\mu_m(C-m)-C+2}.
\tag{4.2}
\]

At the same time the **full** residual is exactly

\[
R_C(M_m)=(C-4)(\mu_m-1).
\tag{4.3}
\]

Thus \(B_{\inf}\) is negative on the scale \(-m\mu_m\), while \(K_{\rm occ}\) is positive on the scale \(+m\mu_m\), and their cancellation leaves the correct \(O(\mu_m)\) FEI residual. This is the mandatory preflight in the strongest possible form for the present mechanism:

* a fixed-depth/merged-tail compression cannot replace \(K_{\rm occ}\);
* a fixed multiplicative discard of the dependence reserve is structurally dangerous;
* the exact restriction chain (1.4) and exchange identity (2.7) retain the required high-cardinality/multiscale information.

At the current shaped benchmark center \(C=6.5584452830718245\), the checker records, for example, the rigorous source lower/upper bounds

\[
\begin{array}{c|r|r}
m&K_{\rm occ}\ \text{lower bound}&B_{\inf}\ \text{upper bound}\\ \hline
8&104.515625&-41.503915977\ldots\\
12&1039.970703125&-710.580242236\ldots\\
20&53206.107681274\ldots&-44701.178730482\ldots
\end{array}
\]

These are diagnostics of the analytic inequalities (4.1)--(4.2), not a finite substitute for them.

## 5. Application of the named partner result to the exact \(B_{\inf}+K_{\rm occ}\) ledger

Fleet03/B17's completed quarter/half result gives the actual Boolean non-subcube witness with branch-positive masks

\[
G_0^+=\{0,1,2\},
\qquad
G_1^+=\{0,1,2,4,5,6,7\},
\tag{5.1}
\]

at input biases \((1/4,1/2,1/2,1/2,1/2)\) and output bias \(1/4\).

If \(a_T,b_T\) are the raw four-bit Walsh sums of the two restrictions, the source-exact biased squared spectral numerators are

\[
P(T):\ (3a_T+b_T)^2,\qquad
P(T\cup\{y\}):\ 3(b_T-a_T)^2
\]

over denominator \(4096\). Reconstructing (5.1) gives the exact histograms from the partner report and, after conditioning on the nonempty spectral branch \(v=3/4\), the occurrence marginals

\[
\boxed{
r=\left(\frac14,\frac16,\frac16,\frac5{12},\frac23\right),
\qquad
\mu=\frac53.
}
\tag{5.2}
\]

The conditioned nonempty spectral masses have histogram

\[
(1/48)^{\times12},\quad
(1/16)^{\times4},\quad
(1/12)^{\times2},\quad
(1/3)^{\times1},
\]

hence

\[
\boxed{
H(P)=\frac73+\frac34\log_2 3
=3.522055208874200\ldots .
}
\tag{5.3}
\]

The I-projection parameter is the nonzero root in \((0,1)\) of

\[
\boxed{
10c^4-199c^3+1500c^2-5292c+3456=0,
}
\tag{5.4}
\]

namely

\[
c=0.82622778226935999\ldots .
\]

Equation (1.2) then gives

\[
H_{\max}(r)=3.80809453260468166\ldots,
\qquad
\boxed{
K_{\rm occ}=0.28603932373048119\ldots .
}
\tag{5.5}
\]

For the partner's source-exact read-once base value \(C_0=6.4548\), its exact defect is

\[
D_{\Gamma_0}=\frac5{16}C_0-\frac74=0.267125,
\]

so

\[
R_{\Gamma_0}=\frac{D}{v}=0.356166666666666\ldots
\]

and therefore

\[
\boxed{
B_{\inf}^{\Gamma_0}
=R_{\Gamma_0}-K_{\rm occ}
=0.07012734293618547\ldots>0.
}
\tag{5.6}
\]

This is the exact expression from the named completed partner applied to this assignment: the nearest non-subcube dyadic gate on that face does **not** need its KL reserve to rescue a negative first-moment Bellman term. It is already \(B_{\inf}>0\). Therefore the useful adversarial search for the present repair problem is correctly concentrated on genuine \(B_{\inf}<0\) sources, not on repeating that dyadic face.

This finite partner application does not prove a universal class beyond its stated geometry.

## 6. Prime constraint and why the KL cannot be “spent twice”

The source-bound 18-input composition-prime witness at

\[
p_1=223/456,\qquad p_2=\cdots=p_{18}=1/2,\qquad
p_{\rm out}=1019/2048
\]

has, for the refuted historical \(\Gamma^\dagger\),

\[
D_{\Gamma^\dagger}
=-0.03802373436527919\ldots<0.
\tag{6.1}
\]

The key point for this assignment is not the obsolete candidate. It is the normalization:

\[
D_{\Gamma^\dagger}=v(B_{\inf}^{\Gamma^\dagger}+K_{\rm occ}).
\]

Thus the negative quantity (6.1) is negative **after the full \(K_{\rm occ}\) has already been credited**. Adding \(K_{\rm occ}\) a second time as a repair bank would be double-spending. The current shaped direction changes the potential and repairs this known witness, but its all-gate universality remains open.

For a composition-prime source there is also no disjoint-composition hierarchy credit \(C_{\rm hier}\) available from factoring the gate. Hierarchy KL remains essential for decomposable transport but cannot be invoked as a free prime-gate reserve.

## 7. Mechanism change and exact remaining implication

### Failed mechanism

The natural proposal

> choose a nonzero center-preserving bias-only \(\psi\), permit \(\psi\) to hurt some gates, and insure those losses using the already available \(K_{\rm occ}\)

is refuted by Theorem 3.1. Binary gates have \(K_{\rm occ}=0\), and their AND constraints force every bounded symmetric zero-center insured direction to vanish.

### Replacement mechanism

Keep the exact **two-ledger source state**

\[
\boxed{(\mathcal B_\Gamma,\mathcal K)
=(vB_{\inf}^{\Gamma},vK_{\rm occ})}
\]

through physical restriction. Use (1.4) and (2.7) together. This preserves:

* all child dependence KL with coefficient one;
* the negative Jensen-Shannon term with its correct sign;
* \(C_{\rm marg},C_{\rm erase},C_{\rm pair}\) without double counting;
* the full high-cardinality dependence required by recursive majority;
* exact Boolean physical restrictions rather than arbitrary real-row relaxations.

The next unpaid implication is now precise. Along an adaptive genuine physical restriction tree, prove a dimension-independent amortized inequality for the exact local total-residual increment

\[
\boxed{
L_{\Gamma,j}
=
\operatorname{It}_j a_s+J_\Gamma
-\operatorname{JS}_s(U,V)-H_{\rm layer},
}
\tag{7.1}
\]

while carrying the child residuals and the exact \((\mathcal B,\mathcal K)\) exchange. Equivalently, find a source/state-dependent Bellman augmentation whose node inequality telescopes without replacing \(K_{\rm occ}\) by a fixed fraction or charging the same \(C\)-credit twice.

A proof of such a universal joint node/amortization statement for a finite-center \(\Gamma\), together with terminal control, would advance the all-gate route. A witness repair by itself does not.

**FULL-PROBLEM CHANGE:** none; FEI remains open.  
**MECHANISM CHANGE:** yes; `KL-insured zero-center one-variable potential -> exact multiscale two-ledger restriction Bellman state`.

## 8. Verification and scope

`CHECK.py` is standard-library only. It:

1. reconstructs the exact partner masks (5.1), their integer Walsh spectra, the partner's numerator histograms, the exact occurrence vector (5.2), and the nonempty spectral histogram;
2. recomputes the I-projection root, \(H(P)\), \(H_{\max}\), \(K_{\rm occ}\), \(R\), and \(B_{\inf}\);
3. checks the recursive-majority analytic lower/upper formulas at representative depths;
4. checks the elementary binary-law uniqueness identities underlying \(K_{\rm occ}=0\).

The checker returned `PASS`. Its finite numerical checks validate implementation only. Theorems 2.7 and 3.1 are analytic proofs above. No novelty or publication-priority claim is made.

Checker SHA-256:
`3c6b75bfd3c6c9c2f5c31c9608b1dc7fe2de3776f815a58109b8b1ff8a3a877d`

Captured output SHA-256:
`e690c80a42c95db6bcb200faa2457d88fc37857b901279d8a8f490ab771c1ae7`

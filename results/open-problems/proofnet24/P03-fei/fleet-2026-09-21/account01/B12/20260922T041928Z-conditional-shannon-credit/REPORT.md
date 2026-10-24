# B12 — quantitative conditional Shannon credit for the live prime-gate candidate

**Run:** `20260922T041928Z-b12-fei-gate-increment-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` to the assigned conditional-Shannon subproblem; `LIMIT-PRIME-GATE-LIFT-v1` remains **OPEN**.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Live candidate and exact peer inputs

The live common candidate is the account03/B18 campaign state
`account03/B18/20260922T032411Z-n18-host-repairing-barrier/REPORT.md`,
report blob `3acc87960b7179fa094c8a27d43f1f9beae5fb34`:

\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p).
\]

The exact remaining universal implication is

\[
D_{\Gamma_*}(P;p)\ge0
\tag{0.1}
\]

for every finite composition-prime Boolean gate \(P\) and every interior product
bias vector \(p\). By the already-proved gate composition cocycle, (0.1)
would imply the all-gate inequality and hence full FEI with constant \(C_*\).
This report does not prove (0.1).

The named compatible other-account theorem used substantively is
`account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`.
For a physical pivot \(j\), bias \(t\), \(q=1-t\), and Boolean restrictions
\(f_0,f_1\), write their biased Fourier coefficients as

\[
a_S=\widehat f_0(S),\qquad b_S=\widehat f_1(S).
\]

That report proves the exact conditional spectral-entropy identity

\[
\widetilde H_G
=q\widetilde H_{G_0}+t\widetilde H_{G_1}
+h_2(t)+h_2(u)-\mathcal C_j,
\tag{0.2}
\]

where \(u=\operatorname{It}_j(G;p)\) and

\[
\mathcal C_j=H(B\mid S)+I(S;J)\ge0.
\tag{0.3}
\]

It also proves the exact defect cocycle

\[
D_\Gamma(G)
=qD_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j,
\tag{0.4}
\]

with

\[
\begin{aligned}
\mathcal R_{\Gamma,j}
={}&q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(r)\\
&+\delta_j\bigl(\Gamma(t)+h_2(V_t)\bigr)
-h_2(t)-h_2(u),
\end{aligned}
\tag{0.5}
\]

\(r_b=\Pr(G_b=1)\), \(r=qr_0+tr_1\),
\(\delta_j=\Pr(G_0\ne G_1)\), \(u=V_t\delta_j\), and
\(V_t=4tq\).

The missing term in the assigned B12 Shannon step is therefore not an
unspecified remainder: it is the exact positive information credit
\(\mathcal C_j\). The purpose of this run is to lower-bound it in source
variables strongly enough to be usable in (0.4).

## 1. A modewise representation of the missing credit

Define

\[
m_S=q a_S^2+t b_S^2,\qquad
z_S=tq(b_S-a_S)^2.
\tag{1.1}
\]

Parseval gives \(\sum_Sm_S=1\), while the peer splitting identity gives

\[
u=\sum_Sz_S=\operatorname{It}_j(G;p).
\tag{1.2}
\]

On \(m_S>0\), put

\[
\eta_S=\frac{t b_S^2}{m_S},
\qquad
\theta_S=\frac{z_S}{m_S},
\tag{1.3}
\]

and use value zero when \(m_S=0\). Then the two exact information terms in
(0.3) are

\[
H(B\mid S)=\sum_Sm_Sh_2(\eta_S),
\tag{1.4}
\]

\[
I(S;J)
=h_2(u)-\sum_Sm_Sh_2(\theta_S).
\tag{1.5}
\]

Thus every quantity below is computed from the actual two Boolean restriction
spectra; no arbitrary spectral law or unsigned replacement is introduced.

## 2. Main theorem: an explicit two-credit lower bound

Define

\[
K_{\rm br}
:=4tq\sum_{S:m_S>0}\frac{a_S^2b_S^2}{m_S},
\tag{2.1}
\]

and

\[
K_{\rm vert}
:=\frac{2}{\ln2}
\left(
\sum_{S:m_S>0}\frac{z_S^2}{m_S}-u^2
\right).
\tag{2.2}
\]

### Theorem 2.1 — quantitative conditional Shannon credit

For every Boolean gate, every physical pivot, and every interior product bias,

\[
\boxed{\mathcal C_j\ge K_{\rm br}+K_{\rm vert}.}
\tag{2.3}
\]

Consequently,

\[
\boxed{
\widetilde H_G-q\widetilde H_{G_0}-t\widetilde H_{G_1}
\le
h_2(t)+h_2(u)-K_{\rm br}-K_{\rm vert}.
}
\tag{2.4}
\]

Moreover \(K_{\rm br},K_{\rm vert}\ge0\).

### Proof

The sharp elementary scalar inequality

\[
h_2(x)\ge4x(1-x),\qquad 0\le x\le1,
\tag{2.5}
\]

gives, using
\(
\eta_S(1-\eta_S)=tq\,a_S^2b_S^2/m_S^2
\),

\[
H(B\mid S)
=\sum_Sm_Sh_2(\eta_S)
\ge
4tq\sum_{S:m_S>0}\frac{a_S^2b_S^2}{m_S}
=K_{\rm br}.
\tag{2.6}
\]

For completeness, (2.5) follows by setting
\(g(x)=h_2(x)-4x(1-x)\). It is symmetric about \(1/2\),
\(g(0)=g(1/2)=0\), and on \(0<x<1/2\),

\[
g''(x)=8-\frac{1}{(\ln2)x(1-x)}.
\]

This second derivative increases from \(-\infty\) to
\(8-4/\ln2>0\), so \(g'\) decreases and then increases.
Since \(g'(0+)=+\infty\), \(g'(1/2)=0\), and
\(\int_0^{1/2}g'=0\), \(g\) first rises and then returns
monotonically to zero. Hence \(g\ge0\) on \([0,1/2]\), and symmetry
finishes the proof.

For the second credit,

\[
h_2''(x)
=-\frac{1}{(\ln2)x(1-x)}
\le-\frac4{\ln2}.
\tag{2.7}
\]

Thus binary entropy is \(4/\ln2\)-strongly concave. Applied to the
probability law \(m\) and the random variable \(\theta_S\), whose mean is
\(u\), this gives

\[
\begin{aligned}
I(S;J)
&=h_2(u)-\sum_Sm_Sh_2(\theta_S)\\
&\ge
\frac{2}{\ln2}\sum_Sm_S(\theta_S-u)^2\\
&=
\frac{2}{\ln2}
\left(\sum_{S:m_S>0}\frac{z_S^2}{m_S}-u^2\right)
=K_{\rm vert}.
\end{aligned}
\tag{2.8}
\]

Adding (2.6) and (2.8) proves (2.3), and substitution into (0.2)
gives (2.4). \(\square\)

## 3. Direct insertion into the live all-gate candidate

Combining Theorem 2.1 with (0.4)-(0.5) gives a completely explicit lower
certificate for any candidate potential:

\[
\boxed{
\begin{aligned}
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge{}&
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(r)\\
&+\delta_j\bigl(\Gamma(t)+h_2(V_t)\bigr)
-h_2(t)-h_2(u)\\
&+K_{\rm br}+K_{\rm vert}.
\end{aligned}}
\tag{3.1}
\]

Therefore, if both child defects are nonnegative and the right side of (3.1)
is nonnegative for one physical split, then the parent satisfies the same
all-gate candidate. This is the exact application to
`LIMIT-PRIME-GATE-LIFT-v1`; no coordinate label, terminal term, or information
credit is omitted.

This does not yet show that every composition-prime gate has such a split.
That remains the universal step.

## 4. Exact zero-credit rigidity and a dead stronger route

The same representation gives a sharp structural statement.

### Proposition 4.1 — zero-credit characterization

For an interior pivot \(0<t<1\),

\[
\boxed{
\mathcal C_j=0
\iff
t=\frac12
\quad\text{and}\quad
\operatorname{supp}\widehat f_0
\cap
\operatorname{supp}\widehat f_1
=\varnothing.
}
\tag{4.1}
\]

### Proof

Since both terms in (0.3) are nonnegative,
\(\mathcal C_j=0\) forces \(H(B\mid S)=0\).
For interior \(t\), (1.4) then gives
\(\eta_S\in\{0,1\}\) at every positive-mass mode, equivalently
\(a_Sb_S=0\) for every \(S\). Thus the two Fourier supports are disjoint.

Under disjoint support, \(\theta_S=t\) on the \(f_0\)-support and
\(\theta_S=q\) on the \(f_1\)-support. These two support sectors have
\(m\)-masses \(q\) and \(t\), respectively, by Parseval. Hence
\(I(S;J)=0\), i.e. \(\theta_S\) is constant \(m\)-almost surely, exactly
when \(t=q=1/2\). The converse is immediate. \(\square\)

In fact, for disjoint child spectra at arbitrary interior \(t\),

\[
\boxed{
\mathcal C_j=h_2(2tq)-h_2(t).
}
\tag{4.2}
\]

This exposes a dead stronger route that should not be retried:
there is **no** universal \(\kappa>0\) such that
\(\mathcal C_j\ge\kappa\mathcal W_j\), where

\[
\mathcal W_j=tq\bigl(\delta_j-(r_1-r_0)^2\bigr)
\tag{4.3}
\]

is the exact quadratic Poincare currency.

Indeed take the genuine Boolean children
\(f_0\equiv1\) and \(f_1=\chi_1\), and take \(t=1/2\).
Their Fourier supports are \(\{\varnothing\}\) and \(\{\{1\}\}\), so
\(\mathcal C_j=0\) by (4.1), whereas
\(\delta_j=1/2\), \(r_0=0\), \(r_1=1/2\), and

\[
\boxed{\mathcal W_j=\frac1{16}>0.}
\tag{4.4}
\]

Thus the new credit bound must be combined with the potential/child slack,
not substituted for it by a constant-factor currency estimate.

## 5. Nontrivial application: the four-bit prime gate B0 at its uniform anchor

I also apply the theorem to the exact other-account prime gate from
`account03/B14/20260922T033806Z-b0-middle-selector/REPORT.md`,

\[
B_0^{-1}(1)=\{0,1,2,3,4,5,8,10\}.
\]

For either middle pivot at uniform bias, that report gives two binary
AND/OR-type children. In one middle-pivot convention their Fourier coefficient
vectors on the six nonzero union-support modes can be taken as

\[
a=(-1/2,-1/2,-1/2,1/2,0,0),
\]

\[
b=(1/2,-1/2,0,0,-1/2,-1/2).
\tag{5.1}
\]

Therefore

\[
H(B\mid S)=\frac12,\qquad I(S;J)=\frac12,
\tag{5.2}
\]

while the new lower bounds give exactly

\[
K_{\rm br}=\frac12,\qquad
K_{\rm vert}=\frac{1}{4\ln2}.
\tag{5.3}
\]

Hence

\[
\boxed{
\Delta_j\widetilde H
\le
\frac32-\frac{1}{4\ln2}
=
1.139326239777759\ldots .
}
\tag{5.4}
\]

This is already strictly below the credit-free bound \(2\).

For the live stable candidate, the read-once certificate gives
\(\Gamma_{\rm RO}(1/4)=6.4548-2\), so

\[
\Gamma_*(1/4)
=4.4548+0.2682048\frac{3}{16}
=4.5050884.
\tag{5.5}
\]

At the uniform middle split,
\(r_0=3/4\), \(r_1=1/4\), \(r=t=1/2\), and
\(\delta_j=u=1/2\). Thus (3.1) yields the strictly positive local estimate

\[
\boxed{
\mathcal R_{\Gamma_*,j}+\mathcal C_j
\ge
-0.2558372+\frac{1}{4\ln2}
=
0.1048365602222406\ldots>0.
}
\tag{5.6}
\]

The exact peer value is \(0.2441628\); (5.6) intentionally uses only the new
universal lower bound, not the exact credit. The binary children are already
safe under the read-once certificate (indeed their stable-candidate defects
are \(0.0167628\) each), so this supplies an independent quantitative
Shannon-credit closure of the uniform \(B_0\) split.

This application is not claimed as new coverage of the full gate problem:
the all-bias \(B_0\) case and the universal prime-gate statement remain open.

## 6. A closed-form all-bias certificate for the B0 middle split

The same theorem turns the outstanding all-bias \(B_0\) middle split into an
explicit scalar expression suitable for interval analysis.

Write

\[
a=\Pr(x_0=1),\quad b=\Pr(x_1=1),\quad
t=\Pr(x_2=1),\quad d=\Pr(x_3=1),\quad q=1-t,
\]

and use pivot \(x_2\). The child output probabilities and disagreement are

\[
r_0=1-ad,\qquad r_1=(1-b)(1-d),
\]

\[
\delta=d(1-a)+(1-d)b,\qquad r=qr_0+tr_1,
\qquad u=4tq\delta.
\tag{6.1}
\]

Let \(s=\sqrt{d(1-d)}\). The only two overlapping biased-Fourier modes have
coefficients

\[
A_0=2ad-1,\qquad
B_0=1-2(1-b)(1-d),
\]

\[
A_3=2as,\qquad B_3=2(1-b)s.
\tag{6.2}
\]

The exclusive child-square masses are

\[
E_A=4a(1-a)d,\qquad
E_B=4b(1-b)(1-d).
\tag{6.3}
\]

For \(\ell\in\{0,3\}\), set

\[
M_\ell=qA_\ell^2+tB_\ell^2,\qquad
Z_\ell=tq(B_\ell-A_\ell)^2.
\tag{6.4}
\]

Then Theorem 2.1 specializes to

\[
\boxed{
K_{\rm br}^{B_0}
=
4tq\sum_{\ell\in\{0,3\}:M_\ell>0}
\frac{A_\ell^2B_\ell^2}{M_\ell},
}
\tag{6.5}
\]

\[
\boxed{
K_{\rm vert}^{B_0}
=
\frac{2}{\ln2}
\left[
\sum_{\ell\in\{0,3\}:M_\ell>0}\frac{Z_\ell^2}{M_\ell}
+t^2qE_A+tq^2E_B-u^2
\right].
}
\tag{6.6}
\]

Thus a sufficient, entirely explicit inequality for this physical split is

\[
\boxed{
\begin{aligned}
0\le L_2(a,b,t,d):={}&
q\Gamma_*(r_0)+t\Gamma_*(r_1)-\Gamma_*(r)\\
&+\delta[\Gamma_*(t)+h_2(4tq)]
-h_2(t)-h_2(u)\\
&+K_{\rm br}^{B_0}+K_{\rm vert}^{B_0}.
\end{aligned}}
\tag{6.7}
\]

Every term except the one-dimensional evaluations of the already-fixed
\(\Gamma_*\) is now elementary. If (6.7) holds, the pivot-\(x_2\) local
contribution is nonnegative. The analogous formula for pivot \(x_3\), combined
with the proved middle-selector theorem
\(\max(\omega_2,\omega_3)\ge W/2\), gives a concrete next interval/analytic
target without dropping either Shannon information credit.

A simple useful sub-bound follows from the shared \(x_3\) Fourier mode:

\[
\boxed{
K_{\rm br}^{B_0}
\ge
16tq\,d(1-d)
\frac{a^2(1-b)^2}{q a^2+t(1-b)^2}.
}
\tag{6.8}
\]

In particular the middle-split credit is strictly positive throughout the
interior \(a,b,t,d\in(0,1)\), because the two child spectra always overlap on
the \(x_3\) mode.

## 7. Status change and exact remaining implication

**Old missing inference:** in the exact Shannon restriction cocycle, the
positive information term \(\mathcal C_j\) was retained symbolically but had
no generally applicable lower bound in the child Fourier coefficients strong
enough to insert directly into the live candidate.

**New proved inference:** Theorem 2.1 supplies the universal source-exact
lower bound \(K_{\rm br}+K_{\rm vert}\), Proposition 4.1 identifies its
zero-credit obstruction exactly, and equations (6.5)-(6.7) specialize the
bound to an explicit all-bias certificate for the current four-bit prime
handoff.

**Refuted stronger shortcut:** no positive constant can lower-bound
\(\mathcal C_j\) by the local quadratic currency \(\mathcal W_j\) on all
Boolean splits.

**New missing implication:** prove that every composition-prime gate/product
bias has a physical split (or a realizable stopped restriction tree) for which
the candidate lower certificate, together with already-paid child slack,
closes (0.1); or exhibit a genuine Boolean gate/bias vector violating the
fixed \(\Gamma_*\). This is still the same `LIMIT-PRIME-GATE-LIFT-v1` target.

Therefore the result is `ESSENTIAL_STEP_APPLIED` to B12's assigned conditional
Shannon increment, **not** a full FEI proof candidate.

## 8. Reproducibility and scope

`CHECKER.py` performs deterministic regression checks of:

- \(h_2(x)\ge4x(1-x)\) on a dense scalar grid;
- the two lower bounds on 10,000 deterministic random normalized coefficient
  pairs (diagnostic only; the proof is analytic);
- the exact Boolean zero-credit / positive-currency obstruction;
- the \(B_0\) uniform values in (5.2)-(5.6).

The random normalized-vector checks are algebraic regression only and are not
used as evidence of Boolean realizability or of the universal FEI claim.

Scoped privacy/secret review: the report and checker contain only mathematical
formulas, logical account/slot labels, repository-relative scientific
provenance, and nonsecret hashes. They contain no credentials, scheduler IDs,
machine paths, raw private transcripts, benchmark keys, email/Drive content,
paid-compute instructions, remote-workflow instructions, or permission
changes.

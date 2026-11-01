# fleet03/B16 — exact B0 selector credit and a certified dyadic spine

**Classification:** `ESSENTIAL_STEP_APPLIED / SOURCE-VALID SUBCLASS CLOSED`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Live all-gate candidate:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Effective target and peer artifact consumed

Fresh owner control revision `2026-09-22.2` supersedes the older Campaign-C packet assignment and directs all FEI workers to the same all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
      [\Gamma(p_i)+h_2(V_{p_i})],\qquad V_u=4u(1-u).
\tag{G}
\]

The current stable successor candidate is

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(z)=\Gamma_{\rm RO}(z)+a^\dagger z(1-z),
\quad a^\dagger=0.268204856,
\tag{0.1}
\]

with \(\Gamma_{\rm RO}(1/2)=C_0=6.4548\).  The universal prime/all-bias implication remains open.

The named compatible cross-account input consumed substantively is

`fleet01/B12/20260922T041928Z-conditional-shannon-credit/REPORT.md`.

It proves the exact physical restriction cocycle, including the full information credit
\(\mathcal C_j=H(B\mid S)+I(S;J)\), and gives the explicit two-overlap biased spectra for the four-input composition-prime gate

\[
B_0^{-1}(1)=\{0,1,2,3,4,5,8,10\}\subset Q_4.
\tag{0.2}
\]

I apply that theorem to the selector-varying line suggested by the concurrent B0 work rather than dropping the Shannon/KL credit.

## 1. Exact selector line

Use the peer convention in which the pivot has bias \(t\), and set the other three physical biases to \(1/2\).  The two restrictions have

\[
r_0={3\over4},\qquad r_1={1\over4},\qquad
\delta={1\over2},\qquad
r={3\over4}-{t\over2}.
\tag{1.1}
\]

Write \(q=1-t\), \(V=4tq\), and \(u=\operatorname{It}_j=V/2=2tq\).  The exact six-mode child spectra from the peer report can be arranged as

\[
a=(-1/2,-1/2,-1/2,1/2,0,0),
\qquad
b=(1/2,-1/2,0,0,-1/2,-1/2).
\tag{1.2}
\]

For \(m_S=qa_S^2+tb_S^2\), \(z_S=tq(b_S-a_S)^2\),
\(\eta_S=tb_S^2/m_S\), and \(\theta_S=z_S/m_S\), the six modes split exactly into

- one mode with \(m=1/4,z=tq,\eta=t\);
- one mode with \(m=1/4,z=0,\eta=t\);
- two modes with \(m=q/4,z=tq/4,\eta=0\);
- two modes with \(m=t/4,z=tq/4,\eta=1\).

Therefore the full information credit is not merely lower-bounded; it is exactly

\[
\boxed{
\mathcal C(t)=h_2(2tq)-{1\over4}h_2(4tq).
}
\tag{1.3}
\]

The exact quadratic currency is

\[
\boxed{
\mathcal W(t)=tq\left(\delta-(r_1-r_0)^2\right)={tq\over4}.
}
\tag{1.4}
\]

Substitution into the peer restriction cocycle gives, for every symmetric potential \(\Gamma\), the exact local remainder

\[
\boxed{
L_\Gamma(t)
=\Gamma(1/4)-\Gamma(1/4+t/2)
 +{1\over2}\Gamma(t)
 +{1\over4}h_2(4tq)-h_2(t).
}
\tag{1.5}
\]

In particular a quadratic lift \(\Gamma_c=\Gamma+c z(1-z)\) changes (1.5) by exactly

\[
L_{\Gamma_c}(t)-L_\Gamma(t)=c\,{tq\over4}=c\mathcal W(t).
\tag{1.6}
\]

No negative information credit, terminal term, or quadratic currency is discarded here.

## 2. A two-AND bridge and its exact kernel

For the source read-once fixed-point potential define the half-factor AND map

\[
T(q,g)=qC_0+{g\over2}-{q\over2}E(1/2,q),
\tag{2.1}
\]

with exactly the source kernel

\[
E(p,q)=8p(1-q)L(p)+8q(1-p)L(q)+8(1-p)(1-q)
+\Psi(pq)-\Psi(p)-\Psi(q).
\tag{2.2}
\]

For a dyadic selector \(t=2^{-m}\), \(m\ge2\), use the exact dyadic AND-chain equality for \(\Gamma_{\rm RO}(t)\).  To reach the off-dyadic argument in (1.5), factor

\[
{1\over2}-t={1\over2}(1-2t),
\qquad
{1\over4}+{t\over2}={1\over2}\left({1\over2}+t\right).
\tag{2.3}
\]

Two source AND inequalities then give a lower bound for (1.5).  After the dyadic value cancels, the remaining scalar kernel is

\[
L_{\Gamma_{\rm RO}}(t)\ge B(t):={F(t)\over\ln2},
\tag{2.4}
\]

where

\[
\begin{aligned}
F(t)={}&-(1-2t)^2\ln(1-2t)+(1-t)^2\ln(1-t)+5t^2\ln t\\
&-(2t^2+2t+1/2)\ln(1+2t)
+t(6t+C_0-2)\ln2.
\end{aligned}
\tag{2.5}
\]

This identity is useful independently of the numerical fixed-point array: all intermediate \(\Psi\)-terms cancel.

### Concavity theorem

Direct differentiation gives

\[
F''(t)=-2\left[-5\ln t+4\ln(1-2t)-\ln(1-t)
+2\ln(1+2t)-6\ln2\right].
\tag{2.6}
\]

The bracket is nonnegative exactly when

\[
(1-2t)^4(1+2t)^2\ge64t^5(1-t).
\tag{2.7}
\]

For \(0<t\le1/4\),
\(1-2t\ge2t\) and \((1+2t)^2\ge1\ge4t(1-t)\), so (2.7) follows immediately.  Hence \(F\) is concave on \([0,1/4]\), with \(F(0)=0\).  At the other endpoint,

\[
B(1/4)= {11137\over10000}-{9\over16}\log_2 3
=0.22215859334434965\ldots>0.
\tag{2.8}
\]

For a completely elementary sign check, \(\log_2 3<8/5\) because \(3^5<2^8\), so the right side of (2.8) is greater than \(0.2137\).  Concavity therefore yields

\[
B(t)\ge4tB(1/4)>0,
\qquad 0<t\le1/4.
\tag{2.9}
\]

The unlifted application (2.4) should be read at the scope of the source AND-subsolution.  The next section removes that scope issue for a finite but nontrivial dyadic spine by using the fully certified binary potential.

## 3. PROVED: eleven nonuniform dyadic selector points are safe under the proved binary certificate and under the stable candidate

The source certificate proves the binary AND/OR inequality for

\[
\Gamma_{\rm cert}(z)=\Gamma_{\rm RO}(z)+0.01z(1-z),
\qquad \Gamma_{\rm cert}(1/2)=6.4573.
\tag{3.1}
\]

The source certificate summary records all regions verified.  Repeating the two-factor bridge with \(\Gamma_{\rm cert}\), while using the exact dyadic AND-chain values of \(\Gamma_{\rm RO}\), changes (2.4) by the explicit amount

\[
\boxed{
L_{\Gamma_{\rm cert}}(2^{-m})
\ge B(2^{-m})+0.01\left({2^{-2m}\over2}-{1\over16}\right).
}
\tag{3.2}
\]

A standard-library checker below evaluates every logarithm by the exact rational atanh series with a rigorous geometric tail enclosure.  It proves (3.2) is strictly positive for every

\[
\boxed{m=2,3,\ldots,12.}
\tag{3.3}
\]

The smallest certified local margin is at \(m=12\):

\[
L_{\Gamma_{\rm cert}}(2^{-12})
>0.00045873438951841766.
\tag{3.4}
\]

The current stable lift satisfies

\[
\Gamma^\dagger=\Gamma_{\rm cert}+(0.268204856-0.01)z(1-z).
\]

By (1.6), its local remainder is larger by

\[
(0.258204856){t(1-t)\over4}.
\tag{3.5}
\]

Thus all eleven points (3.3) are also strictly safe for \(\Gamma^\dagger\); at \(m=12\) the lower margin is

\[
L_{\Gamma^\dagger}(2^{-12})
>0.0004744901156967061.
\tag{3.6}
\]

Both restrictions on this line are binary AND/NAND-type gates, already paid by the proved binary certificate.  A further positive quadratic lift cannot destroy their defects because the quadratic gate currency is nonnegative.  Therefore these are genuine four-input B0 gate inequalities, not merely positive local remainders.

## 4. Attempted refutation / precise dead route

The natural hope was that the same two-AND certified bridge would close the entire infinite dyadic tail.  It does not.  The certified lift introduces a fixed bridge loss

\[
0.01\left({t^2\over2}-{1\over16}\right),
\tag{4.1}
\]

which tends to \(-0.000625\) as \(t\downarrow0\).  At \(m=13\) the resulting lower certificate is already negative:

\[
B(2^{-13})+0.01\left({2^{-26}\over2}-{1\over16}\right)
<-8.2241\times10^{-5}.
\tag{4.2}
\]

Even after adding the stable-candidate quadratic increment, this particular lower bound is still negative (about \(-7.4363\times10^{-5}\)).  This is **not** a counterexample to \(B_0\), to \(\Gamma^\dagger\), or to FEI.  It refutes only the stronger claim that two black-box applications of the certified binary inequality close the whole dyadic selector tail without retaining their local quadratic slack.

This identifies the exact replacement obligation: remove the artificial \(0.01/16\) loss by a local/tangent interpolation around the known quarter-bias endpoint, or combine the exact selector identity (1.5) with the already-proved boundary-repulsion theorem to obtain an explicit boundary cutoff.  The latter theorem says the genuine two-sided local margin is driven favorable as \(t\to0\), so the negative value in (4.2) is known to be a bridge artifact.

## 5. Status and handoff

**Old missing implication:** the universal composition-prime/all-bias inequality for the stable all-gate candidate.

**New proved implication:** for the isolated four-input prime gate \(B_0\), the full information credit along the selector line is exactly (1.3), the local defect is exactly (1.5), and the eleven dyadic nonuniform points \((1/2,1/2,2^{-m},1/2)\), \(2\le m\le12\), are rigorously safe under the proved binary certificate and hence under \(\Gamma^\dagger\).

**Refuted stronger route:** a two-black-box-AND certificate with the `0.01` lift does not close the entire dyadic tail; it loses a fixed `0.000625` asymptotically.

**Replacement obligation:** combine (1.5) with an explicit quantitative form of the boundary-repulsion theorem, or prove a no-loss quarter-endpoint interpolation, to close \(m\ge13\) and then the continuous selector interval.  This is still only one prime-gate family; the universal prime-gate theorem remains open afterward.

**Consumed peer artifact:** `fleet01/B12/20260922T041928Z-conditional-shannon-credit/REPORT.md` (exact restriction/credit cocycle and B0 two-overlap spectra).

**Next recipient:** `fleet01/B13` for an explicit boundary cutoff, with `fleet04/B15` as the B0 interior-slice companion.

**Full-FEI implication:** no universal finite constant is proved here.  Full FEI remains **OPEN**.

# ProofNet24 P22 — Kernel Benign Audit / Hard-Edge Assistance

**Run timestamp:** 2026-09-14 23:23:56 Asia/Jerusalem  
**Scope:** P04 Target 2 re-audit, then post-certification assistance on P04/P20 Target 4. **NO number theory.**

## Verdict on Target 2

P04 Target 2 remains **PROVED / ProofNet24-certified**.

For fixed \(h>0\), fixed \(q_0<\infty\), any signal sequence
\[
f_d\in\bigoplus_{s=0}^{q_0}\mathcal H_{d,s},
\qquad
\sup_d\|f_d\|_{L^2}\le B,
\]
with
\[
d_\ell=2^{2^\ell},
\qquad
n_\ell=2^{2^{2\ell}},
\]
iid \(X_i\sim{\rm Unif}(S^{d_\ell-1})\), Gaussian label noise of variance \(\sigma^2\), and the actual minimum-RKHS-norm interpolant for
\[
K_h(x,y)=\exp\!\left(-\frac{\|x-y\|^2}{2h^2}\right),
\]
the realized conditional clean-test excess risk satisfies
\[
\boxed{
E_{X_0}\!\left[
(\widehat f_\ell(X_0)-f_{d_\ell}(X_0))^2
\mid X_{1:n_\ell},\varepsilon_{1:n_\ell}
\right]\xrightarrow{\mathbb P}0.
}
\]
The proof gives almost-sure convergence along the prescribed level sequence under any coupling with the correct levelwise marginals.

The fragile chain was rechecked: with
\[
R=2^\ell,\quad d=2^R,\quad n=d^R,\quad k=R+\ell-1,
\]
\[
N_{d,k}/n=d^{\delta_*+o(1)},\qquad
D_{<k}/n=d^{-(1-\delta_*)+o(1)},
\quad
\delta_*=1/\log2-1.
\]
The exact Mercer series is
\[
\lambda_{d,s}
=
e^{-\gamma}
\sum_{r\ge0}
\frac{\gamma^{s+2r}}
{2^r r!\,d(d+2)\cdots(d+2(s+r)-2)},
\qquad
\gamma=h^{-2},
\]
and gives
\[
\lambda_{d,s+1}\le\frac{\gamma}{d+2s}\lambda_{d,s}.
\]
The growing-degree spherical estimate is dimension-free:
\[
\|Y_s\|_p\le(p-1)^{s/2}\|Y_s\|_2.
\]
At moment order \(q=R\), the conservative Rosenthal errors are
\[
dR\,3^k/\sqrt n=d^{-R/2+O(1)}\to0,
\]
and
\[
Rd^2(2R)^k/n=d^{-R+\ell+O(1)}\to0.
\]
The infinite tail is summed factorially. The KRM step uses its proof-level row-square/correlation-kernel statistic, not max-entry control. The high block obeys
\[
K_T=\tau(I+o_{\rm op}(1)),
\]
the low harmonic matrix obeys
\[
\Psi^\top\Psi=n(I+o_{\rm op}(1)),
\]
and exact low/high RKHS elimination gives
\[
G_0=\tau\Lambda^{-1}+\Psi^\top W\Psi\succeq cnI.
\]
Hence
\[
E_\varepsilon[\mathcal R_\ell\mid X]
\le
C\left[
\sigma^2\left(D_{<k}/n+n/N_k\right)
+
B^2\left(d^{2q_0}/n^2+d^{2q_0}/(nN_k)\right)
\right]\to0.
\]
No microscopic full-Gram hard-edge theorem enters.

Target 2 already has two complete OTHER-worker audits, so this run proceeds to Target 4.

## Source state for Target 4

Latest P04 source: Gmail message `1a0a17dd4c71a913`, claim set including `P04-T4-CHAOSCONTR-13`, `P04-T4-TRACERED-14`, and `P04-T4-VOLDPP-15`.

Latest P20 reduction uses the square pure degree-two harmonic block \(H\), independent radial column \(b\), and Frobenius isometry
\[
T:\mathbb R^m\to\operatorname{Sym}_d^0,
\qquad
m=\frac{(d-1)(d+2)}2.
\]
It reduces adaptive-normal delocalization to
\[
\operatorname{Tr}(N^4)
=
\operatorname{Tr}\!\left[
T\!\left(
\frac{H^{-1}b}{\|H^{-1}b\|}
\right)^4
\right]
+O_P(d^{-1}).
\]
Prior P22 work gives, for a bottom right-singular subspace \(E_k\),
\[
\operatorname{Tr}\!\left[
T\!\left(
\frac{H^{-1}b}{\|H^{-1}b\|}
\right)^4
\right]
\le
\left(\Theta_4(E_k)^{1/4}+\eta_k\right)^4,
\]
where
\[
\Theta_4(E_k)
=
\sup_{0\ne v\in E_k}
\frac{\operatorname{Tr}(T(v)^4)}{\|v\|^4},
\]
and
\[
\eta_k^2
=
\frac{\sum_{j>k}(u_j^\top b)^2/s_j^2}
{\sum_{j\ge1}(u_j^\top b)^2/s_j^2}.
\]
Thus a sufficient package is
\[
\Theta_4(E_k)=O_P(d^{-1}),
\qquad
\eta_k=O_P(d^{-1/4}).
\]

## New theorem `P22-T4-ORBIT-INCOHERENCE-12`

For \(u\in S^{d-1}\), define
\[
B_u
=
\sqrt{\frac d{d-1}}
\left(uu^\top-\frac1dI\right)
\in\operatorname{Sym}_d^0.
\]
For \(E\subset\mathbb R^m\), let \(\mathcal E=T(E)\) and
\[
\mu(E)
=
\sup_{\substack{v\in E\\\|v\|=1}}
\|T(v)\|_{\rm op}^2.
\]
Since \(A\in\operatorname{Sym}_d^0\) is traceless,
\[
u^\top Au
=
\sqrt{\frac{d-1}{d}}\langle A,B_u\rangle_F.
\]
Therefore
\[
\boxed{
\mu(E)
=
\frac{d-1}{d}
\sup_{u\in S^{d-1}}
\|P_{\mathcal E}B_u\|_F^2.
}
\]
For every Frobenius-unit symmetric \(A\),
\[
\|A\|_{\rm op}^4
\le
\operatorname{Tr}(A^4)
\le
\|A\|_{\rm op}^2,
\]
so
\[
\boxed{
\mu(E)^2\le\Theta_4(E)\le\mu(E).
}
\]
Hence it suffices to prove
\[
\boxed{
\sup_u\|P_{T(E_k)}B_u\|_F^2=O_P(d^{-1}).
}
\]
This replaces a full coefficient-space subspace-universality problem by incoherence with one \(d-1\) dimensional physical Veronese orbit.

## New theorem `P22-T4-HAAR-BOTTOMSUBSPACE-12`

If \(E\) is a Haar \(k\)-plane in \(\mathbb R^m\), \(1\le k\le d\), then for sufficiently large \(d\),
\[
\boxed{
P\left\{
\sup_{u\in S^{d-1}}
\|P_{T(E)}B_u\|_F^2>\frac{128}{d}
\right\}\le2e^{-d},
}
\]
and consequently
\[
\boxed{
P\left\{\Theta_4(E)>\frac{512}{d}\right\}\le2e^{-d}.
}
\]
Proof: for a fixed unit \(b\),
\[
\|P_Eb\|^2\stackrel d=\frac{S}{S+T},
\quad
S\sim\chi_k^2,\quad
T\sim\chi_{m-k}^2.
\]
At threshold \(128/d\), on \(T\ge(m-k)/2\) one needs \(S\ge16d\). Exact exponential moments give
\[
P\{\|P_Eb\|^2>128/d\}
\le e^{-3.65d}+e^{-cd^2}.
\]
A \(1/4\)-net of \(S^{d-1}\) has at most \(9^d\) points, and
\[
\|A\|_{\rm op}\le2\max_{u\in\mathcal N}|u^\top Au|.
\]
The union bound then gives the stated exponential estimate.

Thus the desired whole-bottom-subspace geometry is automatic in the fully rotational benchmark for windows as large as \(k=d\), including the natural tentative scale \(k\asymp\sqrt d\).

## New theorem `P22-T4-ACTUAL-ORBIT-MEAN-12`

For the actual harmonic matrix \(H\), let \(P_J(H^\top H)\) be any deterministic Borel spectral projector.

Physical \(O(d)\) invariance gives
\[
H\rho(Q)^\top\stackrel d=H
\]
for the irreducible degree-two traceless-symmetric representation \(\rho\). Hence \(E P_J\) commutes with every \(\rho(Q)\), so by irreducibility
\[
\boxed{
E\,P_J(H^\top H)
=
\frac{E\,\operatorname{rank}P_J}{m}I_m.
}
\]
Therefore, for every fixed physical direction,
\[
\boxed{
E\|P_JT^{-1}(B_u)\|^2
=
\frac{E\,\operatorname{rank}P_J}{m}.
}
\]
If the window rank is deterministically \(k\),
\[
E\|P_{E_k}T^{-1}(B_u)\|^2=k/m.
\]
Thus the actual structured model already has the exact Haar first moment on every physical orbit direction. The missing theorem is concentration, not mean isotropy.

For \(k\asymp\sqrt d\),
\[
k/m\asymp d^{-3/2},
\]
while the required threshold is only \(O(d^{-1})\), allowing a factor \(\asymp\sqrt d\) above the mean.

## New theorem `P22-T4-ORBIT-HYPERCONTR-BARRIER-12`

For every deterministic rank-\(k\) subspace \(E\) and every \(p\ge2\),
\[
\boxed{
\left(
E_{u\sim{\rm Unif}(S^{d-1})}
\|P_{T(E)}B_u\|_F^p
\right)^{1/p}
\le
(p-1)\sqrt{\frac{k}{m}}.
}
\]
This is the Hilbert-valued degree-two spherical hypercontractive estimate obtained by the Gaussian polar lift and Ornstein-Uhlenbeck hypercontractivity.

For a physically invariant actual rank-\(k\) spectral window the same fixed-\(u_0\) moment estimate holds after averaging over the random window.

However, at the desired norm scale \(a/\sqrt d\), Markov gives at best
\[
P\left\{
\|P_{E_k}B_{u_0}\|\ge a/\sqrt d
\right\}
\lesssim
\exp\!\left[-c_a\sqrt{\frac d k}\right].
\]
For \(k\asymp\sqrt d\), this is only \(e^{-c d^{1/4}}\), far too weak to pay an \(e^{O(d)}\) physical sphere net.

Therefore physical invariance plus degree-two hypercontractivity alone cannot prove the uniform orbit theorem. The actual adaptive spectral randomness must be used.

## Independent peer audit

### `P22-AUDIT-P04-CHAOSCONTR-12`

**Source:** Gmail `1a0a17dd4c71a913`  
**Claim:** `P04-T4-CHAOSCONTR-13`  
**Verdict:** **PASS.**

For
\[
\phi_a(g)=\frac{g^\top E_ag-\operatorname{Tr}E_a}{\sqrt2},
\]
and self-adjoint \(B=(B_{ab})\), P04 defines
\[
C(B)=\sum_{a,b}B_{ab}\frac{E_aE_b+E_bE_a}{2},
\]
\[
K(B)=\sum_{a,b}B_{ab}\operatorname{Sym}(E_a\otimes E_b).
\]
The Wiener product formula gives exactly
\[
\boxed{
\langle\phi,B\phi\rangle-\operatorname{Tr}B
=
2I_2(C(B))+\frac12I_4(K(B)).
}
\]
Since
\[
E I_2(A)^2=2\|A\|_F^2,
\qquad
E I_4(K)^2=24\|K\|^2,
\]
and different chaoses are orthogonal,
\[
\boxed{
\operatorname{Var}\langle\phi,B\phi\rangle
=
8\|C(B)\|_F^2+6\|K(B)\|^2.
}
\]
Symmetrization is contractive, so \(\|K(B)\|\le\|B\|_{\rm HS}\).

For rank-one \(B_N=n\otimes n\),
\[
C(B_N)=N^2,
\qquad
\|C(B_N)\|_F^2=\operatorname{Tr}(N^4).
\]
Using
\[
Eq_N^4=3+12\operatorname{Tr}(N^4)
\]
gives
\[
\boxed{
6\|K(B_N)\|^2
=
2+4\operatorname{Tr}(N^4).
}
\]
All constants check. No iid-coordinate substitution is hidden.

## Ledger

**PROVED / certified Target 2:** exact Mercer spectrum and tail ratio; harmonic multiplicities and critical cutoff; growing-degree hypercontractivity; factorial infinite-tail moment control; conservative Rosenthal; KRM row-square/correlation-kernel closure; low harmonic Chernoff; exact low/high RKHS elimination; inverse control; vanishing noise risk; fixed-degree signal bias and tail leakage; conditional excess risk convergence in probability; almost-sure level-sequence strengthening; two complete OTHER audits.

**PROVED post-closure:** traceless Haar fourth moment; right-invariant inverse-direction Haar benchmark; S4 bottom-window split; orbit incoherence identity; Haar whole-bottom-subspace theorem; actual fixed-orbit mean isotropy; hypercontractive barrier; P04 chaos-contraction audit.

**OPEN:** fixed-orbit exponential tail for the actual bottom window; \(\Theta_4(E_k)=O_P(d^{-1})\); inverse-tail mass \(\eta_k=O_P(d^{-1/4})\); inverse-harmonic fourth-Schatten delocalization; finitely many tangent modes; growing bottom spectral tail; annealed graph-factor \(L^1\); early/middle reciprocal resistance; full fixed-\(t\) hard-edge law.

**REJECTED shortcuts:** full-Gram hard edge is needed for Target 2; fixed-degree constants may be extrapolated to growing degree; KRM can be replaced by max-entry control; physical \(O(d)\) invariance implies coefficient-space Haar behavior; mean isotropy implies uniform fourth-Schatten delocalization; generic degree-two hypercontractivity closes the orbit supremum; bulk MP implies Target 4.

## Highest-value next attack

### `P22/P20-T4-FIXED-ORBIT-TAIL-13`

Initially take
\[
k=\lfloor\sqrt d\rfloor.
\]
For one fixed \(u\in S^{d-1}\), prove
\[
\boxed{
P\left\{
\|P_{E_k}T^{-1}(B_u)\|^2>\frac{C}{d}
\right\}
\le e^{-cd}.
}
\]
Physical invariance then makes the bound uniform over deterministic \(u\), and a constant physical net plus `P22-T4-ORBIT-INCOHERENCE-12` yields
\[
\Theta_4(E_k)=O_P(d^{-1}).
\]

Promising routes:

1. anisotropic bottom resolvent control for the deterministic coefficient vector \(T^{-1}(B_u)\);
2. P04's projection-volume ensemble plus a fractional negative-determinant change of measure;
3. leave-one-row/cofactor expansion preserving the exact harmonic row law;
4. direct control of the fixed-vector right spectral measure.

This is weaker than full bottom-eigenvector or full subspace Haar universality.

The independent branch remains
\[
\eta_k=O_P(d^{-1/4}),
\]
and both branches are required by the deterministic S4 split.

## Bottom line

Target 2 remains completely solved and certified.

The new hard-edge reduction is
\[
\boxed{
\Theta_4(E)
\le
\frac{d-1}{d}
\sup_{u\in S^{d-1}}
\|P_{T(E)}B_u\|^2.
}
\]
For Haar \(k\)-planes with \(k\le d\), the right-hand side is \(O(d^{-1})\) with probability \(1-e^{-\Omega(d)}\). For the actual harmonic bottom spectral window, the fixed-direction mean is already exactly \(k/m\).

The live gap is therefore:
\[
\boxed{
\text{upgrade exact fixed-orbit mean isotropy to an }e^{-cd}\text{ tail at the }1/d\text{ scale.}
\]
Combined with the separate inverse-tail mass estimate, that would close the adaptive-normal fourth-Schatten bottleneck blocking P04/P20 Target 4.

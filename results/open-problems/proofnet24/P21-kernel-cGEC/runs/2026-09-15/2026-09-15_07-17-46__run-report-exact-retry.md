# ProofNet24 P21 — Restricted correlated Gaussian equivalence (cGEC)

**Run timestamp:** 2026-09-15 07:17:46 Asia/Jerusalem  
**Scope:** P04 Target 1 only; two augmentations per original sample; fixed \(\Delta>0\), fixed ridge \(\lambda>0\); smooth bounded odd activation such as \(\tanh\); \(F_{ab}\sim N(0,1/d)\); \(n/d\to\alpha>0\), \(m/d\to\beta>0\); unit-norm linear teacher; **NO number theory**.

## Exact target and status

Put \(N=2n\). For original sample \(i\),
\[
a_i,z_{i1},z_{i2}\stackrel{\rm iid}{\sim}N(0,I_d),\qquad
t_i=\xi^\top a_i,\qquad \|\xi\|=1,
\]
and
\[
x_{ij}^A=\sigma(F^\top(a_i+\Delta z_{ij})),\qquad j=1,2.
\]
The exact ridge objective is
\[
\boxed{
L_A(w)=
\frac1{4n}\sum_{i=1}^n\sum_{j=1}^2
\left(t_i-(x_{ij}^A)^\top w\right)^2
+\frac\lambda2\|w\|^2
=
\frac1{2N}\|y-X_Aw\|^2+\frac\lambda2\|w\|^2.
}
\tag{1}
\]

The matched correlated-Gaussian surrogate is
\[
\boxed{
x_{ij}^G=
\mu_eF^\top a_i+
\mu_bF^\top z_{ij}+
\mu_2b_i+
\mu_3p_{ij},
}
\tag{2}
\]
with the same \(a_i\) and the same Gaussian residual \(b_i\) shared by the two views, while \(z_{ij},p_{ij}\) are view-private. The teacher scalar \(t_i=\xi^\top a_i\) stays in the same block. Therefore the Lindeberg replacement unit is
\[
\boxed{(t_i,x_{i1},x_{i2})}
\tag{3}
\]
and never one augmentation alone.

For clean testing,
\[
x^{0,A}=\sigma(F^\top a^0),\qquad t^0=\xi^\top a^0,
\]
while the separately matched clean Gaussian row is
\[
\boxed{x^{0,G}=\nu_1F^\top a^0+\nu_2g^0.}
\tag{4}
\]

**Verdict:** the exact restricted Target 1 remains
\[
\boxed{\text{MATHEMATICALLY PROVED / CANDIDATE COMPLETE}.}
\]
The only Target-1 closure debt remains one complete **OTHER-worker end-to-end audit**.

## Sources read in full

1. Latest P21: `2026-09-15_06-16-59__run-report.md`.
2. Latest full P04: Gmail message `1a0a32dd6ff76d4c`, subject `[ProofNet24] P04 | Kernel conjectures | 2026-09-15 06:42 Asia/Jerusalem`.
3. OTHER report: `P13_fourth_moment_RMT_2026-09-15_07-06-28.md`, Library file id `file_00000000dfd081f8ba56fa1f2118aa40`.

The latest P04 still says T1 is proved/candidate complete and still asks for one complete OTHER audit. The latest P13 proves a real \(q\)-basis \(L^2\)-density hierarchy, identifies the real inverse-moment threshold \(1/2\), and shows that \(q=3\) moves the determinant exponent from the critical \(1/2\) to \(1/3\). Its methodological lesson for P21 is the same: condition on the correct adaptive sigma field and preserve the exact dependence/geometry used by the target.

## Training-value block theorem — retained

Delete both views of one original sample. Let
\[
H_-=\lambda I+\frac1N X_-^\top X_-,\qquad B=H_-^{-1},
\]
and let \(w_-\) be the leave-block optimizer. Put
\[
X_i=
\begin{pmatrix}
x_{i1}^\top\\
x_{i2}^\top
\end{pmatrix},
\qquad
e_i=t_i{\bf1}_2-X_iw_-,
\qquad
Q_i=\frac1N X_iBX_i^\top.
\]
Then exactly
\[
\boxed{
L_i^\star-L_-^\star
=
\frac1{2N}e_i^\top(I_2+Q_i)^{-1}e_i.
}
\tag{5}
\]
At the real training problem, \(Q_i\succeq0\), hence
\[
\|(I_2+Q_i)^{-1}\|\le1.
\]

Conditional Gaussian Poincaré gives entrywise leverage fluctuation variance \(O(d^{-1})\). After leverage freezing, the local statistic is quadratic in
\[
(t,u_1,u_2),\qquad u_j=x_{ij}^\top w_-,
\]
so only \(Et^2\), \(Etu_a\), and \(Eu_au_b\) enter. The teacher cross moment is exact Gaussian Stein:
\[
\boxed{
E[t\,\sigma(Z)]
=
\operatorname{Cov}(t,Z)E[\sigma'(Z)].
}
\tag{6}
\]
Oddness of \(\sigma\) eliminates all even Hermite coefficients, so the quadratic Price/Hermite coefficient vanishes exactly. The inherited sharpened scalar covariance comparison gives unscaled block discrepancy \(O(d^{-1/2})\). Thus one optimized-value replacement costs
\[
O((N\sqrt d)^{-1}),
\]
and since \(n=N/2\),
\[
\boxed{
n\,O((N\sqrt d)^{-1})=O(d^{-1/2}).
}
\tag{7}
\]
No hidden \(n\), \(m\), or \(\sqrt m\) factor survives.

# New theorem: exact fully real clean-risk block identity

Generate an independent matched clean-Gaussian ghost block of size \(M\asymp d\) and write its empirical risk as
\[
\widehat R_0(w)
=
\frac1M\sum_{a=1}^M
\left(t_a^0-(x_a^{0,G})^\top w\right)^2
=
c_0-2r_0^\top w+w^\top S_0w,
\tag{8}
\]
where
\[
S_0=M^{-1}(X_0^G)^\top X_0^G,\qquad
r_0=M^{-1}(X_0^G)^\top t_0.
\]

Let \(w_i\) be the full optimizer after restoring the current two-view training block. Put
\[
A_i=(I_2+Q_i)^{-1}.
\]
The full Hessian is
\[
H_i=H_-+\frac1N X_i^\top X_i.
\]
Because the restored block gradient at \(w_-\) is \(-N^{-1}X_i^\top e_i\),
\[
H_i(w_i-w_-)=\frac1N X_i^\top e_i.
\]
Woodbury gives
\[
H_i^{-1}X_i^\top
=
BX_i^\top A_i,
\]
so
\[
\boxed{
w_i-w_-=
\frac1N BX_i^\top A_ie_i.
}
\tag{9}
\]

Now put
\[
g_-=S_0w_--r_0,\qquad
v_-=Bg_-,
\]
and
\[
R_i=\frac1N X_iBS_0BX_i^\top.
\]
Since
\[
\widehat R_0(w_-+\delta)-\widehat R_0(w_-)
=
2g_-^\top\delta+\delta^\top S_0\delta,
\]
substitution of \(\delta=w_i-w_-\) from (9) gives the exact pathwise identity
\[
\boxed{
\Gamma_i
:=
\widehat R_0(w_i)-\widehat R_0(w_-)
=
\frac1N
\left[
2e_i^\top A_iX_iv_-+
e_i^\top A_iR_iA_ie_i
\right].
}
\tag{10}
\]

This is `P21-REAL-GHOST-BLOCK-19`.

The key point is structural: although clean population risk itself has no visible training normalization, its **one-original-sample training-block increment has an exact outer \(1/N\)** after ridge updating.

## Symbolic check

For the rational test data
\[
H=\begin{pmatrix}3&1\\1&2\end{pmatrix},\quad
N=6,\quad
w=(1/3,-2/5)^\top,\quad
X=\begin{pmatrix}1&2\\-1&1\end{pmatrix},
\]
\[
t=4/7,\quad
S_0=\begin{pmatrix}2&1/2\\1/2&1\end{pmatrix},\quad
r_0=(1/4,-1/3)^\top,
\]
the direct ghost-risk change and the right side of (10) both reduce exactly to
\[
\boxed{\frac{484835}{8298738}}.
\]
Ten random floating-point checks had absolute discrepancy below \(1.4\times10^{-15}\).

# One-block moments for the real clean-risk Lindeberg proof

Because \(\|A_i\|\le1\),
\[
|\Psi_i|
\le
2\|e_i\|\|X_iv_-\|+\|e_i\|^2\|R_i\|,
\]
where \(\Gamma_i=N^{-1}\Psi_i\).

Fixed ridge gives uniformly bounded moments of \(w_-\). The ghost block has bounded fixed moments of \(\|S_0\|\) and \(\|r_0\|\). Hence
\[
\|v_-\|
\le
\lambda^{-1}(\|S_0\|\|w_-\|+\|r_0\|)
\]
has uniformly bounded fourth moment. Conditional current-row moment bounds give
\[
E[\|X_iv_-\|^4\mid\mathcal F_-^0]\le C\|v_-\|^4.
\]
Also
\[
R_i=N^{-1}X_iBS_0BX_i^\top
\]
has bounded fixed moments because \(\|B\|\le\lambda^{-1}\), \(m/N=O(1)\), and the ghost covariance has bounded operator moments. Together with bounded residual eighth moments,
\[
\boxed{E|\Psi_i|^2\le C}
\tag{11}
\]
and therefore
\[
\boxed{E|\Gamma_i|^2\le C/N^2.}
\tag{12}
\]

# Conditional actual/Gaussian comparison of the real clean-risk block

Let \(\mathcal F_-^0\) contain \(F\), the common leave-block training hybrid, and the independent ghost block. Conditional on \(\mathcal F_-^0\),
\[
w_-,B,S_0,r_0,v_-
\]
are fixed and only the current original-sample block is actual-versus-Gaussian.

Let
\[
\varepsilon_d^{\rm op}
=
C_\sigma\sqrt{\frac{\log d}{d}}
\tag{13}
\]
be the inherited operator covariance discrepancy.

Freeze both \(2\times2\) matrices
\[
Q_i=N^{-1}X_iBX_i^\top,
\qquad
R_i=N^{-1}X_iBS_0BX_i^\top.
\]
Conditional Poincaré/quadratic-form variance gives
\[
E\|Q_i-EQ_i\|_F^2\le C/d,
\tag{14}
\]
and
\[
E\|R_i-ER_i\|_F^2
\le
C(1+\|S_0\|^2)/d.
\tag{15}
\]
Since \(A(Q)=(I_2+Q)^{-1}\) is 1-Lipschitz on the PSD cone in operator norm, the total freezing error in the unscaled bracket is \(O(d^{-1/2})\).

For the conditional means,
\[
(\bar Q_i^M)_{ab}
=
N^{-1}\operatorname{Tr}(BC_{ab}^M),
\tag{16}
\]
so
\[
\|\bar Q_i^A-\bar Q_i^G\|
\le
C\varepsilon_d^{\rm op}.
\tag{17}
\]
Similarly,
\[
(\bar R_i^M)_{ab}
=
N^{-1}\operatorname{Tr}(BS_0BC_{ab}^M),
\tag{18}
\]
and since \(BS_0B\succeq0\),
\[
E\|\bar R_i^A-\bar R_i^G\|
\le
C\varepsilon_d^{\rm op}.
\tag{19}
\]

After \(Q_i,R_i\) are frozen, the first term in (10) involves
\[
u=X_iw_-,\qquad h=X_iv_-,
\]
and
\[
2e^\top \bar A h
=
2t{\bf1}^\top\bar Ah-2u^\top\bar Ah.
\]
Its expectation uses only
\[
E[t h_a],\qquad E[u_a h_b],
\]
with
\[
E[t h_a]=(c_a^M)^\top v_-,
\qquad
E[u_a h_b]=w_-^\top C_{ab}^Mv_-.
\]
Thus
\[
|E_A[t h_a]-E_G[t h_a]|
\le
\varepsilon_d^{\rm op}\|v_-\|,
\tag{20}
\]
and
\[
|E_A[u_a h_b]-E_G[u_a h_b]|
\le
\varepsilon_d^{\rm op}\|w_-\|\|v_-\|.
\tag{21}
\]

The second term in (10), after freezing, is a fixed quadratic form in
\[
e=t{\bf1}_2-u
\]
and uses only
\[
Et^2,\quad E[t u_a],\quad E[u_au_b],
\]
exactly the same second moments already controlled in the training block theorem.

Combining (14)–(21) and bounded leave/ghost moments gives
\[
\boxed{
E\left|
E_A[\Psi_i^A\mid\mathcal F_-^0]
-
E_G[\Psi_i^G\mid\mathcal F_-^0]
\right|
\le
C\varepsilon_d^{\rm op}.
}
\tag{22}
\]
Since \(\Gamma_i=\Psi_i/N\),
\[
\boxed{
E\left|
E_A[\Gamma_i^A\mid\mathcal F_-^0]
-
E_G[\Gamma_i^G\mid\mathcal F_-^0]
\right|
\le
C\varepsilon_d^{\rm op}/N.
}
\tag{23}
\]

# Whole-block Lindeberg for the independent ghost risk

Let
\[
Y_-=\widehat R_0(w_-).
\]
Then
\[
Y_i^M=Y_-+\Gamma_i^M.
\]
For \(\varphi\in C_b^2(\mathbb R)\),
\[
\varphi(Y_-+\Gamma)
=
\varphi(Y_-)+\varphi'(Y_-)\Gamma+R,
\]
with
\[
|R|
\le
\frac12\|\varphi''\|_\infty|\Gamma|^2.
\]
The one-block replacement cost is therefore
\[
\boxed{
C\|\varphi'\|_\infty\frac{\varepsilon_d^{\rm op}}N
+
C\|\varphi''\|_\infty N^{-2}.
}
\tag{24}
\]
There are \(n=N/2\) whole-original-sample blocks, hence
\[
\boxed{
\left|
E\varphi(\widehat R_0(w_A^\star))
-
E\varphi(\widehat R_0(w_G^\star))
\right|
\le
C\|\varphi'\|_\infty\varepsilon_d^{\rm op}
+
C\|\varphi''\|_\infty N^{-1}
+
o(1).
}
\tag{25}
\]
This is `P21-REAL-GHOST-LAW-19`.

Since \(\varepsilon_d^{\rm op}=O(\sqrt{\log d/d})\), the ghost empirical clean-risk laws are asymptotically equivalent.

For either trained model, the optimizer is independent of the ghost block, so
\[
E|
\widehat R_0(w^\star)-R_G(w^\star\mid F)
|
=
O(M^{-1/2})
=
O(d^{-1/2}).
\tag{26}
\]
Separately, the actual-clean versus Gaussian-clean covariance transfer gives
\[
E|
R_A(w_A^\star\mid F)-R_G(w_A^\star\mid F)
|
\le
C\varepsilon_d^{\rm op}+o(1).
\tag{27}
\]
Therefore
\[
\boxed{
|E\varphi(\mathcal R_A)-E\varphi(\mathcal R_G)|
\le
C_\varphi\sqrt{\frac{\log d}{d}}+o(1).
}
\tag{28}
\]
This is `P21-REAL-CLEAN-LAW-19`.

The later localized complex-contour theorem remains stronger quantitatively:
\[
W_1(
\mathcal L(\mathcal R_A),
\mathcal L(\mathcal R_G)
)
\le
Cd^{-1/2}.
\tag{29}
\]
But (28) is an independent, fully real source-level clean-test proof.

# Independent audit of the latest P04 block-Stein/Lindeberg claim

## `P21-AUDIT-P04-T1-0642-19`

**Source:** Gmail message `1a0a32dd6ff76d4c`  
**Subject:** `[ProofNet24] P04 | Kernel conjectures | 2026-09-15 06:42 Asia/Jerusalem`  
**Source section:** `TARGET 1 PRESERVED`.

Audit:

1. **Normalization:** \(1/(4n)=1/(2N)\) with \(N=2n\). **PASS.**
2. **Dependence block:** both actual views share \(a_i,t_i\); both surrogate views share \(a_i,b_i\). Whole-original-sample replacement is necessary. **PASS.**
3. **Rank-two update:** (5) follows exactly by Woodbury/completing squares. **PASS.**
4. **Leverage stability:** fixed \(2\times2\) leverage has conditional entry variance \(O(d^{-1})\); freezing costs \(O(d^{-1/2})\) unscaled. **PASS.**
5. **Correlated Stein/Hermite:** after freezing only second moments of \((t,u_1,u_2)\) are needed; teacher cross moments are exact Gaussian-Stein quantities; odd activation kills the quadratic Hermite/Price coefficient. **PASS.**
6. **Total training error:** one block \(O((N\sqrt d)^{-1})\), \(n=N/2\) blocks \(O(d^{-1/2})\). **PASS.**
7. **Separate clean testing:** P04 is correct that clean testing needs its own matched independent clean block. **PASS.**
8. **“Centered-difference” wording:** literal real minimization at negative ghost coefficient is not globally valid because \(H-hS_0\) can lose positive definiteness. This is a wording issue, not a theorem gap. Three rigorous routes exist: positive one-sided Richardson, localized complex contour differentiation, and the new fully real block identity (10).

**Verdict:**
\[
\boxed{
\texttt{P21-AUDIT-P04-T1-0642-19:
CORE PASS / CLEAN-WORDING REPAIR.}
}
\tag{30}
\]

This is a P21 self-track audit and does not count as the missing complete OTHER-worker certification audit.

# Route comparison

- **Whole-original-sample block Lindeberg:** PRIMARY / COMPLETE. Preserves the exact shared-latent block and \(1/N\) scale.
- **Correlated Stein/Hermite:** moment-level sufficient for squared ridge; strong vector CLT unnecessary.
- **Direct real ghost-risk block identity:** NEW / PROMOTED for source-level clean testing. Exact \(1/N\) clean-risk block scale, real algebra only.
- **Positive one-sided Richardson:** VALID / GLOBAL; independent real fallback.
- **Localized complex contour:** SHARPEST RATE; needed for the inherited \(d^{-1/2}\) Wasserstein refinement, not for source-level equivalence.
- **Global Gram/resolvent universality:** TOO STRONG.
- **Source-natural same-coupling theorem:** OPEN / STRICTLY STRONGER.

# Ledger

## PROVED

- exact \(N=2n\) normalization;
- matched shared-latent two-view Gaussian surrogate;
- whole-original-sample replacement;
- exact rank-two training optimized-value identity;
- leave-block ridge stability;
- leverage Poincaré/freezing;
- teacher Stein identity;
- odd-Hermite/Price covariance matching;
- cubic covariance remainder;
- real feature-coordinate averaging;
- positive one-sided clean-test equivalence;
- localized complex feature-coordinate theorem;
- localized complex contour theorem;
- \(O(d^{-1/2})\) optimized-value smooth-law comparison;
- \(O(d^{-1/2})\) clean-risk smooth-law comparison;
- \(W_1\) and fixed-\(W_p\) law comparisons;
- deterministic clean-risk transfer in fixed \(L^p\);
- `P21-REAL-GHOST-BLOCK-19`;
- `P21-REAL-GHOST-LAW-19`;
- `P21-REAL-CLEAN-LAW-19`;
- `P21-AUDIT-P04-T1-0642-19` core PASS.

## CONDITIONAL / PROTOCOL-OPEN

- one complete OTHER-worker end-to-end audit of the full Target-1 chain;
- explicit deterministic scalar formulas for the matched Gaussian surrogate remain imported under their stated proportional-limit assumptions;
- regime remains fixed at \(\ell=2\), fixed \(\Delta>0\), fixed \(\lambda>0\), smooth bounded odd activation;
- no source-natural same-probability-space clean-risk coupling is claimed.

## DISPROVED / REJECTED

- separate-view replacement;
- raw \(n\varepsilon_d\) accumulation;
- strong full-logit Gaussianity as necessary;
- automatic objective-to-test implication;
- noisy-training coefficients at clean test;
- complex PSD Schur reasoning;
- globally convex negative-real centered difference;
- invalid good-event conditioning shortcuts;
- claim that clean population risk has no exact \(1/N\)-scale one-block increment.

## OPEN

1. One complete OTHER-worker certification audit of the entire Target-1 chain.
2. Source-natural same-coupling theorem
   \[
   \mathcal R_A-\mathcal R_G\to_{\mathbb P}0.
   \]
3. Optional direct-real sharp \(d^{-1/2}\) clean-law proof by feature averaging for
   \[
   v_-=H_-^{-1}(S_0w_--r_0).
   \]
4. Growing augmentation count \(\ell_d\to\infty\).
5. Smooth strongly convex nonquadratic losses.
6. ReLU / nonsmooth activations.
7. Nonlinear teachers.
8. Vanishing ridge \(\lambda_d\downarrow0\).
9. Genuine correlated Stein comparison for nonquadratic local statistics.

# Exact remaining obligation / next attack

There is no remaining theorem-sized mathematical gap for the exact restricted Target 1.

The sole closure obligation is
\[
\boxed{\text{one complete independent OTHER-worker end-to-end audit}.}
\tag{31}
\]

For certification, the shortest audit path is now fully real:

1. exact \(N=2n\) normalization;
2. whole-original-sample replacement;
3. rank-two training optimized-value identity;
4. leverage freezing;
5. teacher Stein / odd-Hermite second-moment comparison;
6. total \(n\)-block training error;
7. exact real ghost-risk block identity (10);
8. \(Q_i,R_i\) freezing;
9. second-moment comparison for \((t,u,h)\);
10. total \(n\)-block clean-risk error;
11. ghost empirical-to-population transfer;
12. separately matched actual-clean/Gaussian-clean transfer.

If an OTHER worker completes this chain successfully, Target 1 should be marked ProofNet24-certified.

After certification, the closest stronger extension is a source-natural coupling theorem:
\[
\boxed{\mathcal R_A-\mathcal R_G\to_{\mathbb P}0}
\]
under an explicit coupling that preserves the two-view shared latent.

# Bottom line

The restricted cGEC theorem remains mathematically solved and outside-audit-open.

The main new contribution is the exact real identity
\[
\boxed{
\widehat R_0(w_i)-\widehat R_0(w_-)
=
\frac1N
\left[
2e_i^\top A_iX_iH_-^{-1}(S_0w_--r_0)
+
e_i^\top A_i
\left(
\frac1N
X_iH_-^{-1}S_0H_-^{-1}X_i^\top
\right)
A_ie_i
\right].
}
\tag{32}
\]
It proves that the clean-risk change induced by one training block has an exact \(1/N\) scale, even though clean prediction risk itself has no visible training-loss prefactor.

This gives a direct real whole-original-sample Lindeberg proof of clean-test law equivalence and makes the source theorem independent of negative ghost perturbations and complex contour arguments.

Shared latent randomness between the two augmentations is preserved at every actual replacement step. No strong full-logit CLT, no global nonlinear Gram universality, no projected-coordinate independence, and no hidden dimension factor is used.

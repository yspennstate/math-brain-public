# ProofNet24 P19 — Kernel Spectral Pruning

**Run timestamp:** 2026-09-16 10:06:19 Asia/Jerusalem  
**Repository / branch:** `yspennstate/math-open-problems` / `master`  
**Track:** `proofnet24/P19-kernel-spectral-pruning`  
**Scope:** singular values/vectors, structured spectral pruning, Marchenko–Pastur nulls, neural-feature/kernel/operator-learning stability; **NO number theory**.  
**Delivery:** GitHub only; no email/Gmail action.  
**Runtime honesty:** exposed runtime is GPT-5.6 Sol. No GPT-6 selector, separate effort control, or hidden-agent fan-out is exposed; none is claimed.

**Correction note.** The immutable same-run first draft `2026-09-16_10-06-19__run-report.md` contains one notation typo in its Bernoulli counterexample: it writes `nu_0,nu_1` where the defining symbols must be `u_0,u_1`. The first draft is intentionally not overwritten. This file is the complete corrected canonical report; no theorem statement or numerical constant changes.

---

# 0. Executive result

P19 remains **OPEN**, but the previous polynomial-confidence ghost-frame bottleneck is closed at the abstract theorem level.

The entering theorem compared the actual trained/pruned signal `P=A(S,Theta)` with an independent-data, synchronized-procedure ghost `P0=A(S',Theta)` only in mean square. The present target was:

> `P19-CROSSFIT-GHOST-HIGHPROB-42`: obtain exponential-confidence control of `||P-P0||op`, normalized by the ghost retained singular floor, while keeping trained support selection adaptive rather than replacing it by an iid mask.

This run proves:

\[
\boxed{
\|P-P_0\|_{\rm op}\le \|P-P_0\|_F
\le 2\sqrt{QL}+\frac{\sqrt2}{3}cL,
\qquad
L=\log(1/\delta)+\frac12,
}
\tag{0.1}
\]

with probability at least `1-delta` when the full matrix-valued coordinate-replacement martingale has predictable covariance trace at most `Q` and pathwise coordinate-replacement Frobenius jumps at most `c`. A predictable high-probability UCB for `Q` is allowed by stopping and contributes its own failure probability.

Under the stronger common-operator conditional sub-Gaussian replacement MGF, the scale term vanishes:

\[
\boxed{
\|P-P_0\|_{\rm op}\le \|P-P_0\|_F
\le 2\sqrt{Q\left(\log(1/\delta)+\frac12\right)}.
}
\tag{0.2}
\]

The proof is an exact replacement-to-Doob reduction plus David Janz's primary-source Hilbert-valued self-normalised Bernstein/Gaussian-mixture supermartingale, arXiv:2608.15874v1 (16 Aug 2026).

If a source-legal ghost proxy satisfies `sigma_r(P0)>=g`, then outside the concentration/variance-UCB/singular-floor failures,

\[
\boxed{
\frac{\|P-P_0\|_{\rm op}}{\sigma_r(P_0)}
\le
\frac{2\sqrt{QL}+(\sqrt2/3)cL}{g}.
}
\tag{0.3}
\]

The inherited relative-signal projector/Procrustes theorem then transfers the August holomorphic subspace local law (SLL) and hence the compressed left/right/cross-projector theorem to the actual adaptive trained/pruned frame whenever the right side tends to zero.

For structured rowwise top-`k` pruning, a simultaneous `2k` restricted Gram floor converts prediction-scale replacement energy into matrix Frobenius energy **after adaptive support selection**; exact support lock reduces `2k` to `k`. No iid pruning-mask hypothesis is introduced.

A new rank-one Bernoulli counterexample has retained singular value exactly one and mean-square ghost displacement tending to zero, but only polynomially small order-one jump probability. Thus mean-square ghost closeness alone cannot imply exponential confidence; a bounded jump, a full-vector conditional MGF, or another explicit tail mechanism is necessary.

New claims:

- `P19-REPLACEMENT-DOOB-HILBERT-42` — **PROVED**;
- `P19-GHOST-HILBERT-BERNSTEIN-42` — **PROVED**;
- `P19-GHOST-HILBERT-SUBGAUSS-42` — **PROVED under explicit full-vector conditional MGF**;
- `P19-STRUCTURED-PREDICTABLE-ENERGY-42` — **PROVED**;
- `P19-BERNSTEIN-GHOST-RELATIVE-SLL-42` — **PROVED under explicit source-legal proxy / singular-floor assumptions**;
- `P19-MEAN-SQUARE-NOT-EXPONENTIAL-CE-42` — **PROVED counterexample**;
- `P19-AUDIT-P15-SPECTRAL-SAMEOBS-42` — **PASS**.

---

# 1. Mandatory continuity and peer snapshots

Read from `master` before proof work:

- root `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`;
- latest complete entering P19 report `proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_08-57-03__run-report.md`, creation commit `97e37867bbd937707096d4bf2e70eb01515fad9e`, verified blob `9a9dcfe921931c479b8e1613e2cd4badbfdd79b7`.

The entering strongest target was `P19-CROSSFIT-GHOST-HIGHPROB-42`.

Two current completed peers were consumed:

- P15: `proofnet24/P15-kernel-mean-correction/runs/2026-09-16/2026-09-16_09-26-55__run-report.md`, creation commit `52149c953f7623bf013e2b5bf3ccf7bc74797347`, blob `332e6ac1388c93b73ba1c4ef19a25d63391b744a`;
- P16: `proofnet24/P16-relu-contraction/runs/2026-09-16/2026-09-16_09-37-29__run-report.md`, creation commit `abf139512619891ac0eb9441321239eaa8aca4d9`, blob `423ba3e5cc0a9d48000b54d3128078e46b7b37e9`.

The first draft path and this corrected path were checked before their respective creations; each returned `404 Not Found`.

A pre-write `master` head observed during this run was `1d2e7b2a854e78f67fa557df108930c6213be34f`. Other workers are active, so head identity is informational only; verification uses the returned creation commit for this immutable file.

---

# 2. Exact July–August source boundary

## 2.1 July 7 source — exact archived statements, standalone PDF inaccessible this run

Fresh Library searches for the manuscript attachment name and title did not surface the standalone original PDF; they surfaced prior source-certified P19 reports, including reports that had directly read it. No unseen source assumption is reconstructed.

The recovered July manuscript is **Growing-rank spiked singular vectors and singular values, with applications to pruning deep neural networks**, dated 7 July 2026. Its model is

\[
\boxed{
W_n=X_n+P_n,
\qquad
P_n=U_n\Theta_nV_n^*,
}
\tag{2.1}
\]

with

\[
X_n\in\mathbb R^{n\times m},
\qquad
n/m\to c\in(0,1],
\tag{2.2}
\]

\[
r_n:=\operatorname{rank}(P_n)\to\infty,
\qquad
r_n=o(n),
\tag{2.3}
\]

uniformly bounded spikes, and, when `P_n` is random,

\[
\boxed{P_n\ \text{is independent of}\ X_n.}
\tag{2.4}
\]

For a separated supercritical cluster `C_n`, the stable vector objects are

\[
\widehat\Pi^L_{C_n},
\qquad
\widehat\Pi^R_{C_n},
\qquad
\widehat F_{C_n}=\sum_{j\in C_n}\widehat u_j\widehat v_j^*.
\tag{2.5}
\]

The source-certified cluster formulas are

\[
U_n^*\widehat\Pi^L_{C_n}U_n
=
\operatorname{diag}(\alpha_L(\theta_{n,i})1_{\{i\in C_n\}})
+O_{\rm op}(\eta_{n,C}),
\tag{2.6}
\]

\[
V_n^*\widehat\Pi^R_{C_n}V_n
=
\operatorname{diag}(\alpha_R(\theta_{n,i})1_{\{i\in C_n\}})
+O_{\rm op}(\eta_{n,C}),
\tag{2.7}
\]

\[
U_n^*\widehat F_{C_n}V_n
=
\operatorname{diag}\!\left(\sqrt{\alpha_L(\theta_{n,i})\alpha_R(\theta_{n,i})}\,1_{\{i\in C_n\}}\right)
+O_{\rm op}(\eta_{n,C}),
\tag{2.8}
\]

with

\[
\boxed{
\eta_{n,C}=\frac{\beta_n^{cc}+\zeta_n}{\Delta_n(C_n)}.
}
\tag{2.9}
\]

For the MP null,

\[
\theta_c=c^{1/4},
\qquad
\rho(\theta)^2=\theta^2+(1+c)+\frac c{\theta^2},
\tag{2.10}
\]

\[
1-\alpha_L(\theta)=\frac{c(\theta^2+1)}{\theta^2(\theta^2+c)},
\qquad
1-\alpha_R(\theta)=\frac{\theta^2+c}{\theta^2(\theta^2+1)}.
\tag{2.11}
\]

The recovered Frobenius-optimal kept value and realized-activation identity are

\[
\eta^*(\rho(\theta))=\theta\sqrt{\alpha_L(\theta)\alpha_R(\theta)},
\tag{2.12}
\]

\[
\boxed{
\|Ea\|_2^2=\sum_j(\sigma_j-\eta_j)^2|\langle\widehat v_j,a\rangle|^2.
}
\tag{2.13}
\]

The last identity is a realized perturbation certificate, not by itself a population prediction-risk theorem.

## 2.2 August 19 referee report — standalone PDF inaccessible this run

Fresh Library title search did not surface `RMTA_26_report.pdf`. The preserved source-certified state is that compressed-resolvent control contained the principal RMT difficulty, concrete verification was mainly Haar/Gaussian and needed a stronger local-law connection, and singular-vector theory was explicitly identified as a publication-level issue. No unseen wording or hypothesis is guessed.

## 2.3 August 20 public primary source — freshly verified

Current public primary record:

**Yitzchak Shmalo, “Mesoscopic Rectangular Spikes under Subspace Local Laws: Outlier Values and Singular Subspaces,” arXiv:2608.19594v1, 20 Aug 2026**, `https://arxiv.org/html/2608.19594`.

Fresh theorem-level verification this run:

- Theorem 3.7 controls the compressed left projector, right projector, and phase-invariant left/right cross projector on stable outlier windows in operator norm;
- Remark 3.8 explains why projectors, not individual labels, are invariant under repeated or tighter-than-error clusters;
- the paper explicitly states that value/projector transfer does **not** require `r_n=o(n)`; sublinear rank is used for preservation of the global law and concrete probabilistic SLL verification;
- Theorem 7.4 gives, under independent-entry LSI assumptions and `r_n=o(n)`,
  \[
  \varepsilon_n(K)\le C_K\left(a_n(K)+\sqrt{r_n/n}+\sqrt{\log n/n}\right),
  \tag{2.14}
  \]
  for the MP deterministic equivalent;
- Example 8.12 allows random strengths/directions only when the entire signal is independent of the noise and satisfies rank/compatibility conditions with high probability.

Therefore the actual same-data trained/pruned `P_n` cannot simply be inserted into Theorem 7.4. The legal strategy remains: construct a noise-independent source-legal proxy and prove relative frame alignment.

---

# 3. Primary concentration input

Freshly read:

**David Janz, “Self-normalised Bennett inequalities for Hilbert-valued martingales,” arXiv:2608.15874v1, 16 Aug 2026**, `https://arxiv.org/html/2608.15874`.

For a separable real Hilbert-space martingale with increments `X_j`, `||X_j||<=1`, and predictable covariance

\[
V_n=\sum_{j\le n}E[X_j\otimes X_j\mid\mathcal F_{j-1}],
\tag{3.1}
\]

its Theorem 3.3 gives, for every `rho>0` and `y>=0`, the time-uniform Bernstein boundary

\[
\left\|(V_n+\rho I)^{-1/2}M_n\right\|
\le
\sqrt{2(y+\ell_\rho(V_n))}
+
\frac{y+\ell_\rho(V_n)}{3\sqrt\rho}
\tag{3.2}
\]

outside probability `e^{-y}`, where

\[
\ell_\rho(V)=\frac12\log\det(I+\rho^{-1}V).
\tag{3.3}
\]

The same source records a Gaussian-mixture supermartingale when, for a predictable positive trace-class `W_j`,

\[
E[e^{\langle H,X_j\rangle}\mid\mathcal F_{j-1}]
\le
\exp\left\{\frac12\langle H,W_jH\rangle\right\}
\quad\forall H.
\tag{3.4}
\]

The paper also explicitly warns that separate scalar directional sub-Bennett/sub-gamma inequalities do not automatically give the Hilbert Bennett potential. P19 therefore keeps bounded increments and the strong common-operator sub-Gaussian route distinct.

---

# 4. `P19-REPLACEMENT-DOOB-HILBERT-42` — PROVED

Let `Z=(Z_1,...,Z_m)` have independent coordinates and let `F(Z)` be centered in a separable Hilbert space `H`. Define

\[
\mathcal F_j=\sigma(Z_1,\ldots,Z_j),
\qquad
M_j=E[F\mid\mathcal F_j],
\qquad
D_j=M_j-M_{j-1}.
\tag{4.1}
\]

Let `Z_j'` be an independent copy of coordinate `j`, `Z^(j)` the corresponding replacement vector, and

\[
R_j=F(Z)-F(Z^{(j)}).
\tag{4.2}
\]

Then

\[
\boxed{D_j=E[R_j\mid\mathcal F_j].}
\tag{4.3}
\]

**Proof.** Conditional on the prefix through `j-1`, write the future coordinates as `U` and define `g(z)=E_UF(Z_{<j},z,U)`. Then `M_j=g(Z_j)`, `M_{j-1}=E_{Z_j'}g(Z_j')`, and conditioning the same-future replacement difference on `F_j` gives exactly their difference.

Put

\[
q_j=E[\|R_j\|^2\mid\mathcal F_{j-1}].
\tag{4.4}
\]

The conditional Hilbert variance identity and Jensen over the common future give

\[
\boxed{
E[\|D_j\|^2\mid\mathcal F_{j-1}]
\le\frac12q_j.
}
\tag{4.5}
\]

Indeed, conditionally,

\[
E\|g(Z_j)-Eg(Z_j)\|^2
=\frac12E\|g(Z_j)-g(Z_j')\|^2
\le\frac12E\|R_j\|^2.
\]

If `||R_j||<=c_j` pathwise, `(4.3)` and Jensen give `||D_j||<=c_j`.

If instead the replacement difference obeys the full-vector conditional MGF

\[
E[e^{\langle H,R_j\rangle}\mid\mathcal F_{j-1}]
\le
\exp\{\tfrac12\langle H,W_jH\rangle\}
\quad\forall H,
\tag{4.6}
\]

then conditional Jensen applied to `(4.3)` gives the same MGF bound for `D_j`. Thus both legal concentration inputs transfer from replacements to the Doob martingale without pretending replacement effects are independent.

---

# 5. `P19-GHOST-HILBERT-BERNSTEIN-42` — PROVED

Let

\[
P=A(S,\Theta),
\qquad
P_0=A(S',\Theta),
\tag{5.1}
\]

where `S=(Z_1,...,Z_N)` has iid coordinates, `S'` is an independent copy, and the same exogenous procedure randomness `Theta` is used in both runs. Conditional on `Theta`, `P` and `P0` are iid, so

\[
F=P-P_0,
\qquad E[F\mid\Theta]=0.
\tag{5.2}
\]

Regard matrices as a real Frobenius Hilbert space and reveal the `2N` data coordinates. Let `D_j` be the resulting Doob increments and

\[
V=\sum_{j=1}^{2N}E[D_j\otimes D_j\mid\mathcal F_{j-1}].
\tag{5.3}
\]

Suppose `||R_j||_F<=c` for every coordinate replacement and

\[
\frac12\sum_{j=1}^{2N}q_j\le Q
\tag{5.4}
\]

almost surely, with `Q>0`. By `(4.5)`,

\[
\operatorname{tr}V\le Q,
\qquad
\|V\|_{\rm op}\le Q.
\tag{5.5}
\]

Normalize the martingale increments by `c` and choose Janz regularisation

\[
\rho=Q/c^2.
\tag{5.6}
\]

For `V'=V/c^2`,

\[
\ell_\rho(V')
=\frac12\sum_k\log(1+\lambda_k(V')/\rho)
\le\frac{\operatorname{tr}V'}{2\rho}
\le\frac12,
\tag{5.7}
\]

using `log(1+x)<=x`. Also `||V+QI||op<=2Q`. Set

\[
L=\log(1/\delta)+\frac12.
\tag{5.8}
\]

Janz's Bernstein boundary therefore implies

\[
\boxed{
\|P-P_0\|_F
\le
2\sqrt{QL}+\frac{\sqrt2}{3}cL
}
\tag{5.9}
\]

with probability at least `1-delta`; operator norm is smaller than Frobenius norm, proving `(0.1)`.

If the predictable trace bound is only certified with

\[
P\{\tfrac12\sum_jq_j>Q\}\le\delta_Q,
\tag{5.10}
\]

stop before the first predictable covariance increment that would push the cumulative trace above `Q`. The Janz theorem is time-uniform, and on the event of terminal trace at most `Q` the stopped terminal martingale equals the original one. Hence `(5.9)` holds with probability at least `1-delta-delta_Q`. No illicit conditioning on a future-dependent good event is used.

If `Q=0`, all Doob increments vanish a.s.; the ghost displacement is exactly zero, so the theorem is interpreted separately from the division in `(5.6)`.

---

# 6. `P19-GHOST-HILBERT-SUBGAUSS-42` — PROVED under explicit MGF

Assume `(4.6)` with predictable positive trace-class `W_j`, and let

\[
G=\sum_{j=1}^{2N}W_j,
\qquad
\operatorname{tr}G\le Q.
\tag{6.1}
\]

The replacement-to-Doob MGF transfer from Section 4 permits the Gaussian-mixture supermartingale. Choose regularisation `rho=Q`. Then

\[
\ell_Q(G)\le\frac12,
\qquad
\|G+QI\|_{\rm op}\le2Q.
\tag{6.2}
\]

Ville's inequality gives, with probability at least `1-delta`,

\[
\boxed{
\|P-P_0\|_{\rm op}
\le\|P-P_0\|_F
\le
2\sqrt{Q\left(\log(1/\delta)+\frac12\right)}.
}
\tag{6.3}
\]

A predictable stopping argument again permits a high-probability UCB on `tr G`, with its failure probability carried explicitly.

This theorem is **not** inferred from RMS influence and is **not** inferred from arbitrary separate directional sub-gamma bounds. It requires the common-operator all-directions conditional MGF `(4.6)`.

---

# 7. `P19-STRUCTURED-PREDICTABLE-ENERGY-42` — PROVED

Let `psi` be a fresh probe with Gram

\[
G_\psi=E[\psi\psi^*].
\tag{7.1}
\]

Suppose every row of each replacement matrix `R_j` belongs to a structured difference support family `D`, and there is a simultaneous restricted floor

\[
\boxed{
a=\inf_{J\in\mathfrak D}\lambda_{\min}((G_\psi)_{JJ})>0.}
\tag{7.2}
\]

Then, row by row,

\[
E_\psi\|R_j\psi\|^2
=\operatorname{tr}(R_jG_\psi R_j^*)
\ge a\|R_j\|_F^2.
\tag{7.3}
\]

Define predictable fresh-probe influence

\[
\beta_j^2
=E[E_\psi\|R_j\psi\|^2\mid\mathcal F_{j-1}].
\tag{7.4}
\]

Then

\[
q_j\le\beta_j^2/a,
\qquad
\boxed{
\operatorname{tr}V
\le\frac1{2a}\sum_{j=1}^{2N}\beta_j^2.
}
\tag{7.5}
\]

If the same predictable envelope `l_i^2` applies to coordinate `i` in the original and ghost samples, the two-copy sum cancels the Efron–Stein factor:

\[
\frac12\sum_{j=1}^{2N}\beta_j^2\le\sum_{i=1}^Nl_i^2,
\quad\Rightarrow\quad
\boxed{Q\le a^{-1}\sum_i l_i^2.}
\tag{7.6}
\]

For rowwise top-`k` outputs, the difference of two adaptively support-selected matrices is rowwise `2k`-sparse. Therefore a simultaneous `2k` restricted Gram event validates `(7.3)` regardless of which supports the same trained matrix selected. Exact support lock reduces the order from `2k` to `k`. This is the legal adaptive-pruning replacement for an iid-mask argument.

---

# 8. `P19-BERNSTEIN-GHOST-RELATIVE-SLL-42` — PROVED under source hypotheses

Assume the ghost proxy has equal target rank `r_n` and

\[
P\{\sigma_{r_n}(P_0)<g_n\}\le\delta_{g,n}.
\tag{8.1}
\]

Let the Hilbert Bernstein theorem hold with predictable variance bound `Q_n`, jump scale `c_n`, concentration failure `delta_n`, and variance-UCB failure `delta_{Q,n}`. Set

\[
L_n=\log(1/\delta_n)+\frac12.
\tag{8.2}
\]

Then, outside probability at most `delta_n+delta_{Q,n}+delta_{g,n}`,

\[
\boxed{
\frac{\|P-P_0\|_{\rm op}}{\sigma_{r_n}(P_0)}
\le
q_n^{hp}
:=
\frac{2\sqrt{Q_nL_n}+(\sqrt2/3)c_nL_n}{g_n}.
}
\tag{8.3}
\]

If `q_n^{hp}<1`, the retained rank-`r` projector theorem gives

\[
\|\Pi_U-\Pi_{U_0}\|_{\rm op},
\quad
\|\Pi_V-\Pi_{V_0}\|_{\rm op}
\le q_n^{hp}.
\tag{8.4}
\]

The basis-free Procrustes debt satisfies

\[
\delta_{frame,n}
\le
h(q_n^{hp}),
\qquad
h(s)=\sqrt{2-2\sqrt{1-s^2}}\le\sqrt2s.
\tag{8.5}
\]

If the source-legal ghost frame has holomorphic SLL error `epsilon_{0,n}(K)` on compact contour set `K`, and `R_K` bounds the resolvent there, the inherited aligned-SLL theorem gives

\[
\boxed{
\epsilon_{actual,n}(K)
\le
\epsilon_{0,n}(K)+2R_Kh(q_n^{hp}).
}
\tag{8.6}
\]

Thus `q_n^{hp}->0` plus `epsilon_{0,n}(K)->0`, weighted compatibility, and a stable outlier contour transfer August Theorem 3.7 to the actual same-data trained/pruned frame.

For the independent-entry MP/LSI source proxy one may insert

\[
\epsilon_{0,n}(K)
\le C_K\left(a_n(K)+\sqrt{r_n/n}+\sqrt{\log n/n}\right),
\tag{8.7}
\]

provided the **proxy**, not the actual adaptive signal, satisfies the source independence/rank/compatibility assumptions.

Under the full-vector sub-Gaussian route the relative debt is simply

\[
\boxed{
q_{n,sg}^{hp}
=
\frac{2\sqrt{Q_nL_n}}{g_n}.
}
\tag{8.8}
\]

This closes the abstract target `P19-CROSSFIT-GHOST-HIGHPROB-42`. The source application remains conditional on source-specific values of `Q_n`, `c_n` or an MGF proxy, `a_{2k,n}`, and `g_n`.

---

# 9. `P19-MEAN-SQUARE-NOT-EXPONENTIAL-CE-42` — PROVED

Let

\[
B\sim\operatorname{Bernoulli}(p),
\qquad
B'\ \text{iid},
\tag{9.1}
\]

and define rank-one `2 x 2` signals

\[
P(B)=u_Be_1^*,
\qquad
u_0:=u_0=e_1,
\qquad
u_1:=u_1=e_2.
\tag{9.2}
\]

The auxiliary `nu` aliases in `(9.2)` are only to make the first-draft typo unambiguous; the actual defining vectors are `u_0,u_1`.

Every realization has

\[
\sigma_1(P(B))=1.
\tag{9.3}
\]

If `B!=B'`,

\[
\|P(B)-P(B')\|_{\rm op}
=\|P(B)-P(B')\|_F
=\sqrt2.
\tag{9.4}
\]

Therefore

\[
P\{\|P-P_0\|_{\rm op}=\sqrt2\}=2p(1-p),
\tag{9.5}
\]

but

\[
\boxed{
E\|P-P_0\|_F^2=4p(1-p)\to0.
}
\tag{9.6}
\]

Any universal constant-threshold tail of the form

\[
P\{\|P-P_0\|_{\rm op}\ge1\}
\le\exp\{-c/Q_p\},
\qquad Q_p\asymp p,
\tag{9.7}
\]

fails as `p->0`, because the left side is asymptotic to `2p` while the right side is `exp[-Theta(1/p)]`.

Sanity check only, not proof: at `p=0.005`, the exact tail is `0.00995` and `Q=4p(1-p)=0.0199`, while the illustrative `exp[-1/(8Q)]` is about `0.00187`; at `p=0.002`, the exact tail is `0.003992` while that illustrative exponential is about `1.59e-7`.

The obstruction is tail behavior, not rank collapse: the retained singular floor is identically one.

---

# 10. Required separation of layers and method comparison

**Eigenvalue distributions.** Global MP ESD and any zero atom concern the empirical singular-value distribution. They neither give sparse restricted identifiability nor imply singular-vector isotropy after adaptive training.

**Extreme/restricted singular values.** Simultaneous sparse-RIP/restricted-Gram control is an extreme-singular-value statement on the pruning difference class. It is what converts prediction influence to matrix influence. A global zero hard edge can coexist with a strong sparse lower edge.

**Singular-vector overlap.** August overlap/projector constants are compressed-resolvent/SLL contour-residue quantities. They are not Davis–Kahan/Wedin outputs.

**Prediction risk/operator learning.** Fresh-probe replacement energy `beta_j^2` is a prediction/operator stability object. It becomes matrix control only through the restricted floor `(7.2)`.

**Finite-width confidence.** `Q_n`, `c_n` or MGF proxy, restricted-floor failure, ghost singular-floor failure, representation movement, score margin, and raw-risk tails are finite-sample debts. They are not folded into the MP overlap constants.

**Resolvent versus Wedin.** The legal chain is `source proxy SLL -> relative frame alignment -> actual-frame SLL -> source projectors`. Wedin/Hermitian dilation is reserved for a separate finite perturbation step after a genuine protected singular gap is already known; it is never used to manufacture BBP overlap.

**Leave-one-out/ghost methods.** The replacement identity `(4.3)` is the dependence-preserving step. It permits concentration without treating retraining effects as independent summands.

**Free probability/deterministic equivalents.** Global MP/free-probability formulas can describe spectra or fixed-feature risk integrals, but they do not remove same-noise adaptive-frame bias. The inherited rank-one adaptive-BBP counterexample remains decisive.

**Sparsification concentration.** A fixed-support theorem cannot be conditioned through same-data support selection for free. A simultaneous support-class event or an independent support-lock theorem is required. This run uses the simultaneous route.

---

# 11. Independent peer audit — P15

Audit ID: `P19-AUDIT-P15-SPECTRAL-SAMEOBS-42`.

Peer path:

`proofnet24/P15-kernel-mean-correction/runs/2026-09-16/2026-09-16_09-26-55__run-report.md`

Creation commit `52149c953f7623bf013e2b5bf3ccf7bc74797347`; blob `332e6ac1388c93b73ba1c4ef19a25d63391b744a`.

Audited claim: `P15-SPECTRAL-SAMEOBS-FINITEN-42`.

P15 fixes feature matrix `X`, Gram matrix `K=XX^T`, ridge mass `rho`, and spectral mean

\[
m_b(u)=k_u^Tb(K)Y.
\tag{11.1}
\]

Residual KRR is fit to the **same** `Y`:

\[
f_b(u)=m_b(u)+k_u^T(K+\rho I)^{-1}[Y-Kb(K)Y].
\tag{11.2}
\]

Because `b(K)` commutes with `K`, independent algebra gives

\[
a_b(K)
=b(K)+(K+\rho I)^{-1}[I-Kb(K)]
=(K+\rho I)^{-1}[I+\rho b(K)].
\tag{11.3}
\]

For a nonzero Gram eigenvalue `kappa`, let `s=kappa b(kappa)` and `h=kappa/(kappa+rho)`. The induced primal transfer is

\[
\boxed{
t_b(\kappa)=\frac{\kappa[1+\rho b(\kappa)]}{\kappa+\rho}=h+(1-h)s.
}
\tag{11.4}
\]

Under the peer's model `Y=XTheta+E`, with centered independent perturbation rows of covariance `Omega` and fresh isotropic query covariance `I/d`, the signal error is

\[
\frac1d\|P_{\ker X}\Theta\|_F^2
+
\frac1d\sum_j(1-t_j)^2\theta_j^2,
\tag{11.5}
\]

while row independence gives the perturbation term

\[
\frac{\operatorname{tr}\Omega}{d}
\operatorname{tr}[a_b(K)Ka_b(K)]
=
\frac{\operatorname{tr}\Omega}{d}
\sum_j\frac{t_j^2}{\kappa_j}.
\tag{11.6}
\]

Thus the peer's exact finite-design risk formula is reproduced. For the baseline `h_j`,

\[
1-t_j=(1-h_j)(1-s_j)
\]

gives signal gain

\[
\frac{\rho^2(2s_j-s_j^2)\theta_j^2}{(\kappa_j+\rho)^2},
\tag{11.7}
\]

and direct expansion gives

\[
\frac{t_j^2-h_j^2}{\kappa_j}
=
\frac{2\rho s_j+\rho^2s_j^2/\kappa_j}{(\kappa_j+\rho)^2},
\tag{11.8}
\]

exactly matching the peer's same-response perturbation penalty.

**Verdict:** `PASS` under the explicit fixed-representation, spectral-linear-mean, linear-teacher plus centered independent-row perturbation hypotheses. This audit does not extend the claim to response-trained neural representations and is not one of the two complete OTHER-worker end-to-end P19 closure audits.

---

# 12. Tests, failures and counterexamples preserved

1. On `tr V<=Q`, choosing `rho=Q/c^2` gives `ell<=1/2` and `||V+QI||op<=2Q`; this reproduces the constants in `(5.9)` with no ambient-dimension union bound.
2. The `1/2` conditional Efron–Stein factor in `(4.5)` is exactly canceled by the two iid sample copies when symmetric per-coordinate prediction envelopes are summed, producing `(7.6)` rather than an erroneous factor two.
3. The Bernoulli rare-jump example keeps `sigma_1=1`, so it falsifies exponential-from-variance without confounding rank loss.
4. The simultaneous `2k` Gram event is quantified over the support class before the realized support is selected, so same-trained-matrix pruning does not invalidate the restricted-floor step.
5. The actual adaptive `P` is never declared independent of the RMT noise. Only a separately source-legal ghost `P0` is eligible for source Theorem 7.4.
6. Preserved failed routes include iid-mask substitution, fixed-support concentration after adaptive selection, global-MP-bulk-to-vector inference, prediction-to-vector inference without a restricted floor, absolute signal closeness without a retained singular floor, per-coordinate RMS without a summed influence budget, procedure-seed omission, naive ghost variance plug-in, frozen pruning-mask calibration, and Wedin-as-BBP substitution.

---

# 13. Cumulative ledger

## PROVED

Retained: July source formulas; deterministic covariance-weighted pruning; hard top-`k` boundary identities; restricted-Gram prediction-to-operator conversion; Gaussian sparse-RIP and MP-global-hard-edge/sparse-floor separation; finite-gap Wedin/Hermitian-dilation projector stability; LOO clipped/raw-risk and memorization counterexample; conditional Bernstein/`psi_1` LOO confidence; predictable Efron–Stein/self-normalized scalar-risk machinery; exact ghost variance UCB; score-gap/rare-boundary support-lock theorems; corrected Warnke route and disconnected-good-set counterexample; aligned-SLL transfer; adaptive same-noise BBP/SLL-collapse counterexample; relative-signal projector/Procrustes/SLL transfer; prediction-to-relative-SLL with restricted identifiability; synchronized/hierarchical ghost mean-square theorems; procedure-randomness debt; summed-influence counterexamples.

New: `P19-REPLACEMENT-DOOB-HILBERT-42`, `P19-GHOST-HILBERT-BERNSTEIN-42`, `P19-GHOST-HILBERT-SUBGAUSS-42` under its explicit MGF hypothesis, `P19-STRUCTURED-PREDICTABLE-ENERGY-42`, `P19-BERNSTEIN-GHOST-RELATIVE-SLL-42` under source hypotheses, `P19-MEAN-SQUARE-NOT-EXPONENTIAL-CE-42`, and P15 peer audit PASS.

## CONDITIONAL

- exact source map `P=A(S,Theta)` in the RMT signal coordinates;
- source legality of the chosen ghost relative to the exact noise object `X_n`;
- useful predictable full-retrain-and-prune influence `Q_n`;
- bounded matrix jump `c_n` **or** a legal full-vector conditional MGF;
- simultaneous source-relevant `a_{2k,n}` (or `a_{k,n}` after support lock);
- retained ghost singular floor `g_n` and equal-rank matching;
- learned-feature representation alignment debt;
- weighted compatibility for any unbounded spikes;
- raw deployment-risk tails if a population-risk statement is requested;
- stable deployed outlier contour / protected singular gap;
- source checkpoint values of the above quantities.

## DISPROVED / REJECTED

- MP ESD implies same-noise singular-vector isotropy;
- trained pruning can be replaced by an iid mask for free;
- fixed-support concentration survives adaptive selection without a cost;
- global MP zero atom implies sparse restricted-floor failure;
- prediction equality implies vector/operator equality without identifiability;
- absolute `o(1)` signal perturbation implies frame stability without a singular floor;
- vanishing individual replacement RMS implies ghost-frame closeness;
- procedure randomness can be omitted from an independently reseeded ghost;
- mean-square ghost closeness implies exponential confidence — newly disproved;
- separate directional sub-gamma bounds automatically yield the Hilbert Bennett potential;
- Davis–Kahan/Wedin produces BBP overlap constants;
- global deterministic equivalents/free probability remove adaptive-frame dependence.

## OPEN

- `P19-SOURCE-PREDICTABLE-INFLUENCE-43`: derive or measure the source tuple `(Q_n, c_n or MGF proxy, a_{2k,n}, g_n, score margin, stable outlier gap)` for the actual retrain-and-prune pipeline;
- `P19-PREDICTABLE-MARGIN-MGF-38`: convert random score-margin geometry into a predictable MGF/jump certificate;
- non-Haar learned-frame SLL without a proxy-alignment reduction;
- critical `n^{-1/3}` BBP coupling;
- two OTHER independent complete end-to-end P19 audits before closure.

---

# 14. Next attack

Highest-value next target:

\[
\boxed{\texttt{P19-SOURCE-PREDICTABLE-INFLUENCE-43}}.
\]

Analytic route: use double-deletion/cross-fit anchors to expose a legal replacement filtration; prove predictable fresh-probe influence `l_i^2`; combine score-margin support lock with representation stability to obtain either `c_n` or the full-vector conditional MGF; use a simultaneous restricted Gram floor to get `Q_n`; compare

\[
2\sqrt{Q_n\log(1/\delta_n)}+c_n\log(1/\delta_n)
\]

directly with `g_n`; only after the resulting relative ratio vanishes invoke the source SLL/projector theorem.

If original checkpoints/features become accessible, measure exactly `(Q_n, c_n or MGF proxy, a_{2k,n}, g_n, score gap, stable outlier gap)` rather than another global spectral proxy.

P19 remains open, so the retained recurring work continues. No email/Gmail action was used.

---

# 15. Sources

Repository sources:

- `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`;
- entering P19 report `proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_08-57-03__run-report.md`, blob `9a9dcfe921931c479b8e1613e2cd4badbfdd79b7`;
- P15 peer path/commit/blob as listed in Section 1;
- P16 peer path/commit/blob as listed in Section 1.

Fresh public primary sources:

- Yitzchak Shmalo, *Mesoscopic Rectangular Spikes under Subspace Local Laws: Outlier Values and Singular Subspaces*, arXiv:2608.19594v1, 20 Aug 2026, `https://arxiv.org/html/2608.19594`;
- David Janz, *Self-normalised Bennett inequalities for Hilbert-valued martingales*, arXiv:2608.15874v1, 16 Aug 2026, `https://arxiv.org/html/2608.15874`.

Inaccessible originals this run:

- July 7 attachment `Growing_rank_spiked_singular_vectors_and_singular_values__with_applications_to_pruning_deep_neural_networks.pdf` — not surfaced by fresh Library search; exact statements preserved from source-certified prior direct-read P19 reports;
- August 19 attachment `RMTA_26_report.pdf` — not surfaced by fresh Library search; only the source-certified referee-state summary is retained.

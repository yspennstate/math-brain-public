# ProofNet24 P12 — Smooth iid least singular values / phase-retrieval stability

Run timestamp: 2026-09-14 12:38 Asia/Jerusalem

## Executive result

This run recovered the exact original **Conjecture 8.2 (Smooth iid universality)**, recovered the August 2026 subgaussian/redundancy draft and the August 30 bounded-fourth-moment rewrite request, read three peer tracks (P13, P04, P11), and independently audited the strongest P13 fourth-moment candidate proof.

**Main conclusion.** For the **real** problem, P13's bounded-fourth-moment architecture survives this independent audit after one explicit correction to the saved P13 report: the staged scalar threshold must be

\[
s=\frac{t}{\sqrt{k}},
\]

not \(\sqrt{t/k}\). The original August redundancy manuscript itself has the correct threshold, as witnessed by its later identities \(s^{-k}=t^{-k}k^{k/2}\) and \(ks^2=t^2\). After restoring the correct formula, I found no structural gap in the replacement of the three genuinely subgaussian inputs by bounded-density + finite-moment inputs.

Thus the real fixed-surplus smooth-iid conjecture now has a **candidate complete proof under the stronger but cleaner quantitative assumptions**

\[
\mathbb E\xi=0,\qquad \operatorname{Var}(\xi)=\sigma^2\in(0,\infty),\qquad
\|f_\xi\|_\infty<\infty,\qquad \mathbb E|\xi|^4<\infty,
\]

and in fact the same architecture yields the moderate-surplus law for \(k_m=r_m+1\) with \(k_m\log m=o(m)\). Smoothness beyond bounded density does not appear needed for this proof. The **complex** analogue is not audited here and remains OPEN.

This is **not portfolio closure**. P12 is one independent audit. A second independent worker should still check the complete insertion into the manuscript, and the manuscript must be rewritten cleanly before a final theorem claim.

## 1. Exact source statement recovered

Source: user's June 28 manuscript, Section 8.2.

For

\[
M_{m,r}(A)=\min_{T\subset[N_m],\ |T|=m+r}\sigma_m(A_T),
\]

Conjecture 8.2 states: let \(A_m\in\mathbb R^{N_m\times m}\) have iid entries of mean zero and variance one, with a bounded sufficiently smooth density and sufficiently many finite moments. If \(N_m/m\to\gamma>1\), then for every fixed integer \(r\ge0\),

\[
\frac1m\log M_{m,r}(A_m)\xrightarrow{\mathbb P}
-\frac{h(\gamma)}{r+1},
\qquad
h(\gamma)=\gamma\log\gamma-(\gamma-1)\log(\gamma-1).
\]

The manuscript predicts the complex limit

\[
-\frac{h(\gamma)}{2(r+1)}.
\]

Its stated route is exactly: delocalize the relevant random normals, prove density-level local CLT estimates at exponentially small slab widths, prove a two-normal density estimate with angle dependence, and insert these into the second-moment criterion. The manuscript explicitly notes that ordinary CDF Berry--Esseen error is much too large at the scale \(e^{-\Theta(m)}\).

## 2. Current public / August 2026 proof state

The current public arXiv paper `arXiv:2608.07410`, Yang--Wen--Shmalo, proves the real **square-submatrix case** \(r=0\) for centered bounded-density subgaussian entries of positive variance:

\[
\frac1m\log M_m(A_m)\xrightarrow{\mathbb P}-h(\gamma),
\]

with a fixed-epsilon deviation rate \(Ce^{-c\sqrt m}\), and hence the phase-retrieval base \(1/4\) at \(N_m=2m-1\).

The stronger August 24 attached draft states the fixed-surplus and moderate-surplus subgaussian results. With \(k_m=r_m+1\), \(k_m\log m=o(m)\),

\[
\frac{k_m}{m}\log M_{m,r_m}(A_m)\xrightarrow{\mathbb P}-h(\gamma).
\]

The August 30 collaborator message explicitly asks to withdraw/rewrite because the subgaussian assumption may be replaceable by bounded fourth moment. That message is a research proposal, not itself evidence that the weakening is proved.

### Variance normalization

The August draft's normalization argument is correct. If \(\operatorname{Var}(\xi)=\sigma^2\in(0,\infty)\) and \(\widetilde A=A/\sigma\), then

\[
M_{m,r}(A)=\sigma M_{m,r}(\widetilde A),
\]

so

\[
\frac{k_m}{m}\log M_{m,r}(A)
=
\frac{k_m}{m}\log M_{m,r}(\widetilde A)
+
\frac{k_m}{m}\log\sigma.
\]

For fixed variance and \(k_m=o(m)\), the extra term vanishes. The density bound and fourth moment rescale by fixed constants. Therefore variance one is genuinely only normalization.

## 3. Peer reports read

### P13 — Fourth-Moment RMT

P13 proposes a candidate complete real theorem under uniform bounded density + uniform fourth moment, replacing the subgaussian proof's three inputs by:

1. a local density floor for incompressible directions using finite-third-moment local CLT;
2. a compressible-net argument for null normals on a bounded-operator-norm event;
3. Latała operator-norm tightness under fourth moment;
4. a fixed-angle pair argument on the same global bounded-norm event.

I audited this architecture below.

### P04 — Kernel Conjectures

I independently rechecked the P04 leverage lemma. For \(K_s=\lambda_s\Phi_s\Phi_s^T\),

\[
t_s=\operatorname{Tr}(K^{-1}K_s),\qquad
q_s=\operatorname{Tr}(K^{-1}K_sK^{-1}),
\]

and feature-row squared norm \(N_s\), P04 claims

\[
t_s^2\le nN_s\lambda_s q_s.
\]

Indeed,

\[
t_s=\lambda_s\langle\Phi_s,K^{-1}\Phi_s\rangle_F,
\]

so Frobenius Cauchy--Schwarz gives

\[
t_s^2\le\lambda_s^2\|\Phi_s\|_F^2\|K^{-1}\Phi_s\|_F^2.
\]

The addition theorem gives \(\|\Phi_s\|_F^2=nN_s\), while
\(q_s=\lambda_s\|K^{-1}\Phi_s\|_F^2\). Hence the inequality follows exactly. **AUDIT_FOR=P04 verdict: PROVED.** This does not certify P04 Target 3 as a whole.

### P11 — Xi diffusion paths

P11 was read as a second independent peer state. Its main new results concern the quadratic-variation cancellation and Hermite representation of the Xi path. No P11 lemma is imported into the present random-matrix proof, so there is no cross-track circularity.

## 4. Independent audit of the P13 bounded-fourth-moment proof

### 4.1 Lower estimate: bounded density already suffices

Let \(B\) be an \((m+k-1)\times m\) iid real matrix. The negative second-moment identity gives

\[
\sum_{i=1}^m\sigma_i(B)^{-2}=\sum_{j=1}^m d_j^{-2},
\]

where \(d_j\) is the distance of column \(j\) to the span of the other columns. If \(\sigma_m(B)\le t\), some \(d_j\le\sqrt m\,t\). Conditioning on the other columns, the relevant projection has dimension \(k\), and the bounded-density projection theorem gives

\[
\Pr\{\sigma_m(B)\le t\}\le \exp\{O(k\log m)\}t^k.
\]

Union over \(\binom{N_m}{m+k-1}=\exp\{h(\gamma)m+o(m)\}\) candidates yields the lower exponential bound whenever \(k\log m=o(m)\). No subgaussian tail enters.

### 4.2 Incompressibility is enough for the one-slab lower bound

Let \(u\in S^{m-1}\) be \((\delta,\rho)\)-incompressible. Define

\[
J=\{j:|u_j|>1/\sqrt{\delta m}\},\qquad D=J^c.
\]

Then \(|J|<\delta m\), and incompressibility forces

\[
v:=\|u_D\|_2\ge\rho/2.
\]

Normalize \(a_j=u_j/v\) on \(D\). Then

\[
\sum_{j\in D}a_j^2=1,
\qquad
\|a\|_\infty\le \frac{2}{\rho\sqrt{\delta m}}.
\]

If \(\xi\) has bounded density and finite third absolute moment, the diffuse sum

\[
W=v\sum_{j\in D}a_j\xi_j
\]

can be partitioned into a fixed large number of variance-balanced independent blocks. The block densities stay uniformly bounded by the bounded-density projection theorem, and Rosenthal at \(p=3\) gives uniformly bounded third moments. The Bobkov--Götze density-level Berry--Esseen bound therefore gives a positive lower density for \(W\) on a fixed interval once the number of blocks is chosen large enough.

Write the omitted-coordinate contribution as

\[
L=\sum_{j\in J}u_j\xi_j.
\]

Since \(\operatorname{Var}(L)\le1\), Chebyshev gives \(\Pr(|L|\le2)\ge3/4\). Convolution then gives, uniformly over incompressible \(u\),

\[
c\le f_{\langle X,u\rangle}(x)\le C
\quad(|x|\le1),
\]

and hence

\[
ct\le \Pr\{|\langle X,u\rangle|\le t\}\le Ct,
\qquad 0<t\le1.
\]

**Audit verdict:** sound. The local theorem needs finite third moment plus bounded densities; fourth moment is more than enough for this component.

### 4.3 Many random hyperplane normals are incompressible

On the global event

\[
E_M=\{\|A_{\rm base}\|\le M\sqrt m\},
\]

a standard sparse-net proof is sufficient. For a fixed sparse unit vector \(z\), each row projection \(\langle R_i,z\rangle\) has uniformly bounded density, so the probability that \(\|Bz\|_2\) is anomalously small is \(e^{-cm}\). A \(\rho\)-net of \(\delta m\)-sparse vectors has entropy \(e^{O(\delta m\log(1/(\delta\rho)))}\). On \(E_M\), the net approximation error is at most \(M\sqrt m\rho\). Choosing \(\rho\) and then \(\delta\) sufficiently small gives

\[
\Pr\{\ker B\cap\operatorname{Comp}(\delta,\rho)\ne\varnothing, E_M\}
\le e^{-cm}.
\]

Averaging this over the exponentially many \((m-1)\)-row subsets and applying Markov shows that, on \(E_M\), all but an exponentially tiny fraction have incompressible normal.

**Audit verdict:** sound; no subgaussian \(\ell_\infty\) normal-vector theorem is needed.

### 4.4 Fourth moment gives the global norm event needed for qualitative convergence

Latała's norm estimate for independent centered entries implies, at fixed rectangular aspect ratio,

\[
\mathbb E\|A\|\le C\left(\sqrt m+\sqrt n+(nm\,\mathbb E|\xi|^4)^{1/4}\right).
\]

With a uniform fourth-moment bound this is \(O(\sqrt m)\). Thus for every \(\eta>0\) one can choose fixed \(M\) with

\[
\limsup_m\Pr(E_M^c)\le\eta.
\]

This is enough for convergence in probability. For one fixed entry law with finite fourth moment, Bai--Yin gives an eventual almost-sure norm bound along fixed aspect-ratio sequences.

**Audit verdict:** sound. What is lost is the subgaussian paper's explicit \(Ce^{-c\sqrt m}\) deviation rate; fourth moment alone does not supply that rate.

### 4.5 Fixed-angle pair control does not need a subgaussian norm tail

Fix row sets \(S,T\) with \(q=|T\setminus S|\ge\delta_0m\), and condition on the rows of \(S\), so \(u=u_S\) is fixed. On \(E_M\), if \(d_{pr}(u_S,u_T)<a\), then after a sign choice,

\[
\|B_Ju\|_2\le Ma\sqrt m,
\qquad J=T\setminus S.
\]

Therefore at least \(q/2\) fresh rows satisfy

\[
|\langle R_i,u\rangle|\le Ma\sqrt{2/\delta_0}.
\]

The bounded-density slab upper bound makes the probability at most

\[
2^q(CKa)^{q/2},
\]

up to fixed \(M,\delta_0\). By choosing \(a\) sufficiently small this is \(e^{-Am}\) for any prescribed fixed \(A\). Combining with the deterministic high-overlap count yields the exponentially sparse exceptional-pair graph needed by the staged proof.

**Audit verdict:** sound.

### 4.6 Correction to P13's saved report, and stage recursion

P13's saved report writes

\[
s=\sqrt{t_m/k}.
\]

That is inconsistent with \(\sum |\langle X_j,u\rangle|^2\le t_m^2\). The correct choice is

\[
\boxed{s=t_m/\sqrt{k}}.
\]

The original August redundancy manuscript's later identities confirm this: \(s^{-k}=t^{-k}k^{k/2}\) and \(ks^2=t^2\).

Choose a small reserve fraction \(\delta>0\), set \(\beta=\gamma-\delta\),

\[
\lambda=h(\gamma)-\varepsilon<h(\beta),\quad
t=e^{-\lambda m/k},\quad s=t/\sqrt{k},
\]

and split the reserved rows into \(k\) batches of size \(b\asymp m/k\). At each successful stage,

\[
M_j\ge\theta sM_{j-1},\qquad e_j\le As e_{j-1}.
\]

Since \(\log L=h(\beta)m+o(m)\),

\[
\log(sM_j)\ge(h(\beta)-\lambda)m-\frac{k}{2}\log k-O(k)+o(m)\to+\infty,
\]

and

\[
\log\frac{e_j}{sM_j^2}\le-4\kappa m+\frac{k}{2}\log k+O(k)=-4\kappa m+o(m),
\]

because \(k\log k=o(m)\). Thus the one-stage hypotheses persist. The total stage-failure probability is

\[
k e^{-c m/k}=o(1)
\]

under \(k\log m=o(m)\). Finally,

\[
\log M_k\ge(h(\beta)-\lambda)m-\frac{k}{2}\log k+O(k)+o(m)\to+\infty.
\]

A surviving hyperplane therefore yields an \((m+k-1)\)-row submatrix with least singular value at most \(t\). Conditioning on \(E_M\), all other failures vanish; then let the outer norm-event error \(\eta\downarrow0\).

**AUDIT_FOR=P13 verdict:** `P13-MAIN-01` passes this independent structural audit **after correcting the explicit threshold typo**. This is one independent audit, not final certification.

## 5. Candidate theorem supported by the audit

Let \(\xi_m\) be a fixed law or triangular array of real laws with

\[
\mathbb E\xi_m=0,\quad \operatorname{Var}(\xi_m)=1,\quad
\|f_{\xi_m}\|_\infty\le K,\quad \mathbb E|\xi_m|^4\le B.
\]

Let \(A_m\in\mathbb R^{N_m\times m}\) have iid entries with law \(\xi_m\), \(N_m/m\to\gamma>1\), \(k_m=r_m+1\), and \(k_m\log m=o(m)\). The audited architecture yields

\[
\frac{k_m}{m}\log M_{m,r_m}(A_m)\xrightarrow{\mathbb P}-h(\gamma).
\]

For fixed \(r\),

\[
\frac1m\log M_{m,r}(A_m)\xrightarrow{\mathbb P}-\frac{h(\gamma)}{r+1}.
\]

For non-unit fixed variance, the same exponent follows by scaling.

The proof actually uses the more modular package: bounded density, finite third moment, and rectangular operator-norm tightness. Uniform fourth moment implies the latter two.

## 6. Phase-retrieval transfer

Let \(A\in\mathbb R^{(2m-1+r)\times m}\) be full spark and define

\[
\omega(A)=\min_{J:\operatorname{rank}(A_J)<m}\sigma_m(A_{J^c}).
\]

For admissible \(J\), full spark gives \(|J|\le m-1\), hence \(|J^c|\ge m+r\). Selecting \(T\subset J^c\) of size \(m+r\) and using row-monotonicity gives \(\sigma_m(A_{J^c})\ge M_{m,r}(A)\). Conversely a minimizer \(T\) has complement of size \(m-1\), which is rank deficient, so \(\omega(A)\le M_{m,r}(A)\). Therefore

\[
\boxed{\omega(A)=M_{m,r}(A)}.
\]

Bounded-density iid matrices are full spark almost surely. Thus at \(N_m=2m-1+r\), \(h(2)=\log4\), and the candidate theorem implies

\[
\frac1m\log\omega(A_m)\xrightarrow{\mathbb P}-\frac{\log4}{r+1},
\qquad
\omega(A_m)=4^{-m/(r+1)+o_{\mathbb P}(m)}.
\]

For moderate \(r_m\), the same identity gives

\[
\frac{r_m+1}{m}\log\omega(A_m)\xrightarrow{\mathbb P}-\log4
\]

when \((r_m+1)\log m=o(m)\).

**Verdict:** the deterministic redundant phase-retrieval transfer is PROVED under full spark.

## 7. Ledger

### PROVED / independently verified
- Exact real Conjecture 8.2 statement recovered.
- Current public theorem is the real bounded-density subgaussian square-submatrix case.
- Fixed positive variance is removable by exact scaling.
- P04 leverage inequality \(t_s^2\le nN_s\lambda_s q_s\).
- P13 incompressible local-density replacement under bounded density + finite third moment.
- P13 compressible-net replacement on a single global norm event.
- Latała fourth-moment norm tightness suffices for qualitative convergence in probability.
- Fixed-angle pair sparsity on the global norm event using bounded-density anti-concentration.
- P13 displayed stage threshold is a transcription error; the original proof requires \(s=t/\sqrt k\).
- With that correction the stage recursion closes for \(k\log m=o(m)\).
- At \(N=2m-1+r\), full spark gives \(\omega(A)=M_{m,r}(A)\).

### CANDIDATE COMPLETE / requires second audit
- Real bounded-density + uniformly bounded fourth moment moderate-surplus theorem.
- Real redundant phase-retrieval exponent derived from that theorem.

### NOT RETAINED FROM SUBGAUSSIAN RESULT
- Explicit \(Ce^{-c\sqrt m}\) deviation rate under fourth moment alone.
- Uniform almost-sure law over compact aspect-ratio ranges.

### OPEN
- Second independent full audit.
- Clean manuscript rewrite inserting replacements line-by-line.
- Complex iid analogue and factor \(1/2\).
- Minimal assumptions below fourth moment.
- Quantitative rates under weaker-than-subgaussian tails.

## 8. Rejected routes

1. Cite the subgaussian normal-vector theorem under finite fourth moment — invalid.
2. Entrywise truncation plus Weyl — polynomial perturbation dwarfs the exponentially small target singular value.
3. Global Lindeberg replacement of the extremal minimum — nonsmooth exponentially dependent minimum causes prohibitive derivative losses.
4. Assume fourth moment preserves the subgaussian deviation rate — unsupported.
5. Use \(s=\sqrt{t/k}\) in the staged proof — incorrect; the correct threshold is \(t/\sqrt k\).

## 9. Literature checks

- Yang, Wen, Shmalo, arXiv:2608.07410 (2026): bounded-density subgaussian square row-submatrices.
- Bobkov--Götze, *Berry--Esseen bounds in the local limit theorems*, Lithuanian Math. J. 65 (2025), 50--66.
- R. Latała, *Some estimates of norms of random matrices*, Proc. AMS 133 (2005), 1273--1282.
- Bai--Yin (1993): finite-fourth-moment sample-covariance edge law.
- Rudelson--Vershynin bounded-density projection/small-ball methods.

## 10. Next attack

Do not generalize further yet. Perform a hostile line-by-line manuscript audit: make the incompressible local-density constants explicit, write the compressible-net proof self-contained, replace every subgaussian invocation in Sections 4--5, verify the fixed-law almost-sure upgrade, and obtain a second independent worker audit before changing status from candidate-complete to closed.

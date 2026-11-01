Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: internally certified interval width `0.033609950762282626 -> 0.033609950762282626`; status OPEN/PARTIAL.** Three distinct attacks were made: (A) a dependence-preserving finite strip/frontier Markovization; (B) an exact average-reward Bellman dual with a synchronizing finite-horizon certificate; (C) two counterexample attacks showing that gradient-only state and deterministic fixed-band-to-full transfer both fail.

# PROB10-02 / R17 — dependence-preserving finite-width LCS process, exact Bellman dual, and rigorous approximation to the full constant

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Controlling owner directive: `operations/PROB10_2026-09-20.md`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}{n},
\]
for two independent iid uniform binary strings. The alphabet, fair product law, normalization, and genuine dependent match array are kept fixed. Independent Bernoulli matching is not used.

Status after this run: **OPEN / PARTIAL**. No exact value of \(\gamma_2\) is claimed.

## 0. Mandatory continuity: hand off the actual current R17 successor before refocusing

The latest owner directive explicitly refocuses the native R17 slot to PROB10-02. I therefore first recover and hand off the **actual** R17 successor rather than pretending the old LCS handoff was still the current state.

The current successor immediately before this refocus is H0021, Cohen Antonir--Lichev--Zhukovskii Conjecture 1.4 on sharp bounded-degree tree universality. Its canonical claim `operations/claims/H0021.md` assigns H0021 to R17. The latest substantive R17 report is

`runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md`

with navigation commit

`c8891869a1335d67bada83f23f63f2ce09603565`.

That report keeps
\[
\Delta_{\rm near}=2
\]
and proves a port-width/defect obstruction for a broad Pósa/reservoir block-completion architecture. In particular, for \(r\) disjoint pre-sprinkle port sets \(P_i\) of size at most \(s\), a fresh \(G(n,p_2)\) sprinkle induces an auxiliary port graph whose edge probabilities are at most
\[
q=1-(1-p_2)^{s^2}\le p_2s^2.
\]
If \(qr\le \log r-\omega(1)\), the port graph has an isolated block whp. With a repair budget \(t\), the necessary scale becomes \(qr\gtrsim\log(r/t)\). The R17-specific H0021 substantive unchanged streak is one; all of R16's inherited H0021 history and its two consumed recoveries remain preserved.

The preceding R17 chain is also preserved rather than rewritten: the old binary-LCS handoff C050, D0064 work and terminal handoff, the admission-wait sequence, G0004's complete R17 lifecycle and release, H0021 reassignment C079, and H0021 C080 all remain immutable in `runs/R17/`. No H0021 claim, report, or artifact is deleted. This PROB10 report is the handoff pointer for the owner-directed release of H0021; the canonical H0021 claim is updated only to mark that release, not to assign it to another worker.

Thus this run does not silently discard H0021 work and does not reset any H0021 or LCS failure counters.

## 1. Recovered binary-LCS state; no restart and no resurrected invalid certificates

The complete pre-refocus LCS handoff is

`runs/R17/20260918_1414Z_lcs_terminal_handoff_rotation_wait_c050_4a7d.md`.

Its frozen internally certified interval is
\[
\boxed{0.792665992\le\gamma_2\le0.826275942762282626},
\qquad
\boxed{U-L=0.033609950762282626}.
\]

The lower endpoint is the rigorous Heineman--Miller--Reichman--Salls--Sárközy--Soiffer lower bound. The upper endpoint is the R17 C045 internally exact all-row cone certificate in

`runs/R17/20260918_0926Z_fullcap6_c045_f7a1.md`.

C033--C035 remain **withdrawn** because of the complement-gauge error found and repaired at C036. They are not reused.

The old LCS HARD lifecycle is not erased: C049 records the second old recovery, and C050 records the old terminal handoff after the permitted recoveries. The new `operations/PROB10_2026-09-20.md` directive is a later explicit owner reassignment to this same source with a fresh nonduplicating route. It overrides the old instruction to rotate away, but it does **not** reset the historical no-movement/recovery record.

The prior lower-side blocker also remains valid: the exact Lueker/feasible-triplet lookahead-\(22\) route would have to certify an increment
\[
r>\frac{99083249}{150916751}
\]
in the source normalization. The prior upper-side blocker remains a deterministic covering/cone certificate strictly below
\[
0.826275942762282626.
\]
This run does not repeat either dense transfer-matrix route.

### Public literature versus the internal R17 candidate endpoint

The public rigorous literature interval recovered in the current source check remains approximately
\[
0.792665992\le\gamma_2\le0.826280.
\]
The R17 C045 upper endpoint is narrower and internally exact-certified, but it has not completed the repository closure standard of two independent external-track audits and a full priority check. I therefore distinguish the public interval from the fleet's internal certified metric and do not present C045 as published literature.

## 2. Fresh source and prior-art check

The source status was checked again before mathematics.

1. **Tiskin, arXiv:2212.01582v2**, last revised 13 August 2024:
   `https://arxiv.org/abs/2212.01582v2`.
   The abstract still states that the binary coefficient is unresolved. The v2 comments explicitly say that claims in the earlier preprint concerning the process and \(\gamma\) turned out to be incorrect and were removed. None of those withdrawn claims is used here.

2. **Heineman--Miller--Reichman--Salls--Sárközy--Soiffer**, arXiv:2407.10925 / ISIT 2025, gives the retained rigorous binary lower bound
   \[
   \gamma_2\ge0.792665992.
   \]

3. **Li--Ren--Wen (2026)**, DOI `10.1017/S000497272610104X`, still calls determination of the binary constant open and summarizes the public rigorous upper endpoint as Lueker's \(0.826280\).

4. A targeted prior-art search for a finite-width correlated LCS process found a highly relevant paper that must be credited:
   Nicholas Chia and Ralf Bundschuh, **Finite Width Model Sequence Comparison**, *Phys. Rev. E* 70, 021906 (2004), arXiv:q-bio/0406009,
   `https://arxiv.org/abs/q-bio/0406009`.
   They introduce a finite-width LCS model that explicitly retains the sequence-induced correlations, formulate it as a Markov process, and state that its finite-width growth constants increase to the true correlated Chvátal--Sankoff constant from below. Their table gives, for the first nontrivial correlated finite-width case, the exact value \(7/10\).

This prior-art hit materially changes the novelty assessment. The finite-width idea below is **not claimed novel**; it substantially overlaps Chia--Bundschuh's FWM. The value of this run is that it reconstructs that route in a form adapted to the PROB10 contract: an explicit raw-letter/frontier state, an exact rational average-reward Bellman dual, a synchronizing word giving a finite exact verifier, a clean proof of convergence to the full \(\gamma_2\), and exact obstructions showing what cannot be discarded. Any publication-priority claim would require a detailed comparison with the 2004 paper and subsequent finite-width work.

A bounded current search found no 2026 paper determining \(\gamma_2\).

## 3. New ideas written before code

I deliberately did not start by manufacturing another checker.

### Attack A — keep the dependence exactly by retaining the raw letters that generate one whole new column

The old C002 obstruction shows that a fixed suffix of raw letters plus a fixed suffix of boundary gradients is not a Markov state for the **full** LCS process. The way around that obstruction is not to pretend a local full-process state exists. Instead restrict paths to a finite diagonal strip and retain the **entire strip frontier plus exactly the source letters whose shared use generates the next correlated column**.

This preserves the true match dependence. A new target bit is compared to many source bits at once; those match bits are not replaced by independent Bernoulli variables.

### Attack B — dualize the finite process instead of solving a huge stationary linear system

Once the strip process is finite, its growth rate is an average reward. Rather than relying on floating stationary probabilities, use the exact Bellman/Poisson dual
\[
\bar r+Ph-h.
\]
A synchronizing input word then gives an exact finite-horizon certificate with an a priori contraction bound. This is the form most useful for a future large-width exact checker.

### Attack C — attack the compression and transfer assumptions before promoting the method

Two tempting shortcuts are false.

1. Dropping the raw source window and retaining only frontier gradients destroys the Markov property already in the smallest strip.
2. No fixed strip has a deterministic \(o(n)\) stringwise approximation error to full LCS; a swapped two-block family gives a linear gap.

These failures identify the exact scope of a future certificate: raw dependence information is mandatory, and the strip-to-full transfer must use the random iid law rather than a worst-case deterministic comparison.

Only after these three mathematical routes were written down was the finite checker built.

## 4. Exact finite-width process for the genuine dependent model

Fix an integer \(w\ge1\). For deterministic strings \(x,y\), let
\[
D_w(i,j)
\]
be the maximum LCS-grid path score from \((0,0)\) to \((i,j)\) among monotone paths that remain in
\[
|i-j|\le w.
\]
Outside the strip set the value to \(-\infty\). Inside, use the ordinary LCS recurrence.

For independent infinite iid fair binary strings \(X,Y\), define at column \(j\ge w\) the source-letter window
\[
x^{(j)}
=
\bigl(
X_{j-w+1},\ldots,X_{j+w}
\bigr)\in\{0,1\}^{2w}
\]
and the frontier gradient vector
\[
g^{(j)}_k
=
D_w(j-w+k,j)-D_w(j-w+k-1,j),
\qquad
1\le k\le2w.
\]
Every gradient is \(0\) or \(1\).

Write
\[
V_0=0,
\qquad
V_k=\sum_{\ell=1}^k g_\ell.
\]
At the next step expose exactly two fresh independent fair bits
\[
u=X_{j+w+1},
\qquad
v=Y_{j+1}.
\]
The old source window supplies the \(2w\) shared comparisons with \(v\), and \(u\) supplies the last one:
\[
m_k=\mathbf 1_{\{x_k=v\}},
\quad0\le k<2w,
\qquad
m_{2w}=\mathbf1_{\{u=v\}}.
\]

Define
\[
Q_0=\max\{V_1,V_0+m_0\},
\]
\[
Q_k=\max\{Q_{k-1},V_k+m_k,V_{k+1}\},
\qquad 1\le k<2w,
\]
and
\[
Q_{2w}=\max\{Q_{2w-1},V_{2w}+m_{2w}\}.
\]
Then the exact next state is
\[
x'=(x_2,\ldots,x_{2w},u),
\qquad
g'_k=Q_k-Q_{k-1},
\]
and the diagonal reward is
\[
\rho(s;u,v)=Q_w-V_w
=
D_w(j+1,j+1)-D_w(j,j).
\]

### Proposition 4.1 — exact Markov carrier

The process
\[
S_j=(x^{(j)},g^{(j)})
\]
is a finite time-homogeneous Markov chain with at most \(2^{4w}\) states. Conditional on \(S_j\), the only randomness needed for the next transition is the independent pair
\[
(u,v)\in\{0,1\}^2
\]
with probability \(1/4\) each.

**Proof.**
The displayed recurrence is just the ordinary LCS dynamic program written across the \(2w+1\) cells of the next strip column. All old absolute values occur only through a common additive baseline, so their differences \(g\) suffice. The match indicators are not independent random cells: all comparisons against the new \(Y\)-letter use the same \(v\), while \(u\) is the one new source letter at the far edge. Since \(u\) and \(v\) have not appeared in the old state, they are independent fair bits. Hence the displayed update is exact for the original iid-string model. \(\square\)

This is precisely the dependence feature absent from independent Bernoulli matching. For binary strings, the rectangle parity constraint is automatically respected because every match is generated from raw \(X\)- and \(Y\)-letters.

## 5. A synchronizing word and a unique recurrent class

Let
\[
s_0=(0^{2w},0^{2w}).
\]

### Proposition 5.1 — exact reset

The input word
\[
(u,v)=(0,1) \quad\text{repeated }4w\text{ times}
\]
sends **every** strip state to \(s_0\).

**Proof.**
After the first \(2w\) repetitions, the source window consists entirely of zeros. From that point onward every comparison with the incoming \(v=1\) is a mismatch, including the new \(u=0\).

When the source window is all zero and the input is \((0,1)\), all \(m_k=0\). Therefore
\[
Q_0=V_1,
\]
and inductively
\[
Q_k=V_{k+1}\quad(0\le k<2w),
\qquad
Q_{2w}=V_{2w}.
\]
Thus
\[
g'=(g_2,g_3,\ldots,g_{2w},0).
\]
Another \(2w\) repetitions shift every gradient out and leave \(g'=0^{2w}\). The source window remains \(0^{2w}\). \(\square\)

The reset word has probability
\[
q_w=4^{-4w}>0.
\]
Hence every closed communicating class contains \(s_0\), so there is exactly one recurrent class
\[
R_w=\operatorname{Reach}(s_0).
\]
Because \(s_0\) has a self-loop, that class is also aperiodic.

The exact checker enumerates
\[
|R_1|=14,\qquad |R_2|=224,\qquad |R_3|=3098,
\]
and exhaustively verifies the reset word on every enumerated state.

## 6. Exact stationary growth constant and Bellman dual

Let \(P_w\) be the transition matrix on \(R_w\), and let
\[
\bar\rho_w(s)=\frac14\sum_{u,v\in\{0,1\}}\rho(s;u,v).
\]
Let \(\pi_w\) be the unique stationary law.

The diagonal rewards telescope:
\[
D_w(n,n)-D_w(w,w)
=
\sum_{j=w}^{n-1}\rho(S_j;U_j,V_j).
\]
The initial term is \(O(w)\), and the finite chain has one recurrent class. Therefore
\[
\gamma_w
:=
\lim_{n\to\infty}\frac{\mathbf E D_w(n,n)}n
=
\sum_{s\in R_w}\pi_w(s)\bar\rho_w(s).
\]
Since \(P_w\) and \(\bar\rho_w\) are rational, \(\gamma_w\) is rational for every fixed \(w\).

### Theorem 6.1 — exact average-reward dual

For every real potential \(h:R_w\to\mathbb R\),
\[
\min_{s\in R_w}
\left[
\bar\rho_w(s)+(P_wh)(s)-h(s)
\right]
\le
\gamma_w
\le
\max_{s\in R_w}
\left[
\bar\rho_w(s)+(P_wh)(s)-h(s)
\right].
\]
Moreover,
\[
\boxed{
\gamma_w
=
\sup_h\min_s[\bar\rho_w+P_wh-h]
=
\inf_h\max_s[\bar\rho_w+P_wh-h].
}
\]

**Proof.**
Stationarity gives
\[
\sum_s\pi_w(s)\bigl((P_wh)(s)-h(s)\bigr)=0.
\]
Thus the \(\pi_w\)-average of the bracketed residual is exactly \(\gamma_w\), proving the min/max inequalities.

For equality, solve the finite Poisson equation
\[
(I-P_w)h=\bar\rho_w-\gamma_w\mathbf1
\]
with one normalization, e.g. \(h(s_0)=0\). The compatibility condition is exactly stationarity, and irreducibility on \(R_w\) gives a solution. For that \(h\), every Bellman residual equals \(\gamma_w\). \(\square\)

Consequently a rational potential is a finite exact certificate; no floating stationary estimate is needed.

## 7. A finite exact Bellman algorithm with an explicit contraction certificate

The reset word gives more than existence.

For \(T\ge1\), define
\[
h_T=\sum_{t=0}^{T-1}P_w^t\bar\rho_w.
\]
Then
\[
\bar\rho_w+P_wh_T-h_T=P_w^T\bar\rho_w.
\]
Therefore
\[
\boxed{
\min_s(P_w^T\bar\rho_w)(s)
\le\gamma_w\le
\max_s(P_w^T\bar\rho_w)(s).
}
\]

Because the reset word occurs with probability \(q_w=4^{-4w}\),
\[
P_w^{4w}(s,\cdot)
=
q_w\delta_{s_0}+(1-q_w)Q_s(\cdot)
\]
for some probability law \(Q_s\). Hence for every function \(f\),
\[
\operatorname{osc}(P_w^{4w}f)
\le
(1-q_w)\operatorname{osc}(f).
\]
Iterating and using \(0\le\bar\rho_w\le1\),
\[
\boxed{
\operatorname{osc}(P_w^T\bar\rho_w)
\le
\left(1-4^{-4w}\right)^{\lfloor T/(4w)\rfloor}.
}
\]

This is a completely explicit finite-to-stationary error for the exact finite process. It is very conservative, but it is deterministic and rationally checkable.

For \(w=1\), the exact checker solves the 14-state chain and obtains
\[
\boxed{\gamma_1=\frac7{10}.}
\]
It also constructs a rational Poisson/Bellman witness whose residual is identically \(7/10\). With \(T=8\), the finite-horizon certificate gives
\[
\frac{2867}{4096}
\le
\gamma_1
\le
\frac{5735}{8192},
\]
with exact bracket width
\[
\frac1{8192}.
\]
The exact value \(7/10\) agrees with the first nontrivial correlated finite-width value reported by Chia--Bundschuh, which is a useful prior-art and implementation consistency check, not a new bound on \(\gamma_2\).

## 8. Rigorous approximation of the full Chvátal--Sankoff constant

The finite-width process gives lower approximations:
\[
D_w(n,n)\le LCS(X_1^n,Y_1^n),
\qquad
\gamma_w\le\gamma_2.
\]
Also \(D_w\) is monotone in \(w\), so \(\gamma_w\) is nondecreasing.

Let
\[
F(m)=\mathbf E\,LCS(X_1^m,Y_1^m).
\]
For \(n=km\), concatenate an optimal LCS path inside each of the \(k\) diagonal \(m\times m\) blocks. Every such path stays within global distance at most \(m\) of the main diagonal. Therefore
\[
D_m(km,km)
\ge
\sum_{j=1}^k
LCS(X_{(j-1)m+1}^{jm},Y_{(j-1)m+1}^{jm}).
\]
Taking expectation, dividing by \(km\), and sending \(k\to\infty\) yields
\[
\gamma_m\ge\frac{F(m)}m.
\]
Since Chvátal--Sankoff/Fekete gives
\[
\frac{F(m)}m\to\gamma_2,
\]
we obtain the exact characterization
\[
\boxed{
\gamma_w\uparrow\gamma_2,
\qquad
\gamma_2=\sup_{w\ge1}\gamma_w.
}
\]

Combining this with the Bellman dual gives the stationary variational characterization
\[
\boxed{
\gamma_2
=
\sup_{w\ge1}
\inf_h\max_{s\in R_w}
[\bar\rho_w(s)+(P_wh)(s)-h(s)]
}
\]
and equivalently
\[
\boxed{
\gamma_2
=
\sup_{w\ge1}
\sup_h\min_{s\in R_w}
[\bar\rho_w(s)+(P_wh)(s)-h(s)].
}
\]

This is source-faithful: all randomness comes from iid \(X\)- and \(Y\)-letters, and no independent-match replacement occurs.

Tiskin's current v2 review cites Alexander's theorem
\[
0\le
\gamma_2-\frac{F(m)}m
\le
O\!\left(\sqrt{\frac{\log m}{m}}\right).
\]
Because \(\gamma_m\ge F(m)/m\), this immediately transfers to
\[
\boxed{
0\le\gamma_2-\gamma_m
\le
O\!\left(\sqrt{\frac{\log m}{m}}\right).
}
\]
This is a rigorous asymptotic strip-to-full error. I have **not** extracted an effective numerical constant from Alexander's proof in this run, so this rate cannot yet compile a new deterministic upper endpoint.

Chia--Bundschuh already state the finite-width convergence from below. The dual/certificate and synchronizing formulation above should therefore be regarded as a verifier architecture and R17 reconstruction unless a deeper priority check shows otherwise.

## 9. Counterexample attack 1: gradients alone are not Markov

A tempting compression is to keep only \(g\) and discard the raw source window \(x\). That is false even at \(w=1\).

The exact checker finds two reachable states with the same gradient
\[
g=(0,0)
\]
but different source windows:
\[
s_A=((0,0),(0,0)),
\qquad
s_B=((0,1),(0,0)).
\]
Averaging over the same four equiprobable fresh pairs \((u,v)\), the induced distributions of
\[
(g',\rho)
\]
are different. For \(s_A\), the multiplicities are
\[
((0,0),0):1,\quad
((0,0),1):2,\quad
((0,1),0):1,
\]
whereas for \(s_B\) they are
\[
((0,0),1):2,\quad
((1,0),1):2.
\]

Thus the raw letter labels are not cosmetic; they carry exactly the shared-column dependence. Any exact state quotient has to preserve enough information to reproduce these joint transitions.

This is consistent with the old C001/C002 warning but is a new exact obstruction tailored to the finite-width carrier.

## 10. Counterexample attack 2: no deterministic fixed-band-to-full error can vanish

Fix \(m>w\) and take
\[
x=0^m1^m,
\qquad
y=1^m0^m.
\]
The unrestricted LCS has length
\[
LCS(x,y)=m.
\]

A common subsequence containing both symbols is impossible: in \(x\), every zero precedes every one, while in \(y\), every one precedes every zero. Hence every common subsequence is monochromatic.

For a zero match, the source index is at most \(m\) and the target index is at least \(m+1\). The band condition \(|i-j|\le w\) restricts possible matched zeros to at most the last \(w\) zero positions of \(x\) and first \(w\) zero positions of \(y\). Thus there are at most \(w\) zero matches. The same argument applies to ones. The value \(w\) is attained by pairing the corresponding \(w\) near-boundary positions, so
\[
\boxed{D_w(2m,2m)=w.}
\]
Therefore
\[
LCS(x,y)-D_w(2m,2m)=m-w,
\]
which is linear in \(n=2m\) for fixed \(w\).

So there is no deterministic stringwise estimate of the form
\[
LCS(x,y)\le D_w(x,y)+o(n)
\]
at fixed \(w\). Any useful finite-width **upper** transfer must exploit the iid distribution (for example Alexander-type control or a probabilistic excursion theorem), not worst-case strings.

The checker verifies the concrete exact instance \(m=5,w=2\):
\[
LCS=5,\qquad D_2=2.
\]

## 11. What this run did and did not move

### Source metric

Before:
\[
0.792665992\le\gamma_2\le0.826275942762282626,
\quad
U-L=0.033609950762282626.
\]

After:
\[
0.792665992\le\gamma_2\le0.826275942762282626,
\quad
U-L=0.033609950762282626.
\]

**No source-metric movement.**

A finite-width value does not count as a new endpoint unless it crosses the retained lower endpoint, and no simulation or confidence interval is used as a deterministic endpoint.

### Auxiliary progress

This run gives a fully specified dependence-preserving finite Markov reward process, exact Bellman min/max certificates, an explicit synchronizing finite-horizon error for each fixed width, and a proof that these exact finite-width constants increase to the full \(\gamma_2\). It also records two exact obstructions to over-compressing or deterministically transferring the strip.

The main qualification is prior art: the finite-width concept and convergence from below overlap Chia--Bundschuh 2004. Novelty is **not claimed**. The exact Bellman/synchronizing certificate formulation is the useful new repository mechanism, but it requires a detailed priority comparison before any external novelty statement.

## 12. Highest-value next obligation inside PROB10-02

The next run should stay on this problem, as the new owner contract requires.

The finite-width mechanism can move the **lower** endpoint if one can build an exact Bellman subsolution for a width large enough that
\[
\min_s[\bar\rho_w+P_wh-h](s)>0.792665992.
\]
Dense enumeration is the wrong next step. The checker already shows state growth
\[
14,\ 224,\ 3098
\]
for \(w=1,2,3\), and Chia--Bundschuh's finite-width paper documents the same exponential difficulty.

The most promising fresh question is therefore:

> Can the Bellman potential \(h\) be represented by an exact decision diagram / automaton / local additive functional whose residual can be verified over all raw-letter/frontier states without enumerating the full state set?

The synchronizing identity gives an exact fallback:
\[
h_T=\sum_{t<T}P^t\bar\rho_w,
\]
so a compressed representation of \(P^T\bar\rho_w\) is already a complete finite certificate.

On the **upper** side, the clean target is to extract an effective numerical constant from Alexander's finite-size convergence theorem or prove a stronger strip-excursion estimate:
\[
\gamma_2\le \gamma_w+\varepsilon_w
\]
with an explicit \(\varepsilon_w\to0\). Without that, finite-width calculations remain lower-bound machinery only.

The deterministic shifted-block obstruction in Section 10 says exactly what such an upper transfer must avoid.

## 13. Exact checker and artifact manifest

Executed exact-arithmetic checker:

`artifacts/prob10_2026-09-20/PROB10-02/20260919T2316Z_strip_variational_7f2a_checker.py`

created at commit

`c5c31c5ac10b4fd861f37b5a86f9d5e2855673f6`.

Archived output:

`artifacts/prob10_2026-09-20/PROB10-02/20260919T2316Z_strip_variational_7f2a_checker.out`

created at commit

`2900ab786b3a3787b5e79137c0ba57b2aa6463f2`.

The output ends `ALL_EXACT_CHECKS_PASS`.

Finite claims checked exactly:

- repository metric arithmetic;
- reachable strip-state counts for \(w=1,2,3\);
- reset word on every enumerated state for \(w=1,2,3\);
- exact stationary solution \(\gamma_1=7/10\);
- exact Poisson/Bellman equality witness on all 14 recurrent \(w=1\) states;
- exact \(T=8\) Bellman bracket;
- exact gradient-only non-Markov counterexample;
- exact shifted-block band obstruction instance.

The theorem-sized claims are proved on the page above; the checker is a regression/self-check, not an independent audit.

## 14. Runtime/model control

GPT-6 maximum was requested by the owner prompt. The exposed automation surface provides no authenticated model-family selector, reasoning-effort selector, or completed-run effort receipt. The actual model available to this run is GPT-5.6 Sol, and the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum.

No scheduler, cadence, enabled state, email, Drive, workflow, public posting, purchase, or permission setting was modified.

## 15. Structured ledger delta

```yaml
ledger_delta:
  slot: PROB10-02
  worker: R17
  category: HARD_OUTSIDE
  owner_directive: operations/PROB10_2026-09-20.md
  predecessor_actual_successor:
    source: H0021
    status_before_refocus: CLAIMED_ACTIVE_R17_OPEN_PARTIAL
    metric: Delta_near
    value: 2
    latest_substantive_report: runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md
    navigation_commit: c8891869a1335d67bada83f23f63f2ce09603565
    disposition: RELEASED_BY_R17_DUE_TO_LATER_OWNER_REFOCUS
    claims_and_artifacts_preserved: true
  source:
    name: binary_Chvatal_Sankoff_constant
    exact_model: two_independent_iid_uniform_binary_strings
    status: OPEN
    independent_Bernoulli_matching_used: false
  metric:
    name: certified_gamma2_interval_width
    lower: 0.792665992
    upper: 0.826275942762282626
    before: 0.033609950762282626
    after: 0.033609950762282626
    movement: false
  historical_lcs_lifecycle:
    old_recoveries_consumed: 2
    old_terminal_handoff_preserved: true
    failure_counts_reset: false
    owner_refocus_authorizes_new_route: true
  attacks:
    - dependence_preserving_finite_strip_frontier
    - exact_average_reward_Bellman_dual_and_synchronizing_certificate
    - gradient_only_state_counterexample
    - deterministic_fixed_band_transfer_counterexample
  results:
    finite_width_prior_art_overlap: Chia_Bundschuh_2004
    novelty_claimed: false
    exact_variational_characterization: gamma2_equals_sup_w_gamma_w
    exact_fixed_w_dual: true
    explicit_fixed_w_sync_error: true
    full_strip_error_rate: Alexander_O_sqrt_logw_over_w_non_effective_constant
    new_source_endpoint: false
  exact_checker:
    code_commit: c5c31c5ac10b4fd861f37b5a86f9d5e2855673f6
    output_commit: 2900ab786b3a3787b5e79137c0ba57b2aa6463f2
    status: ALL_EXACT_CHECKS_PASS
  model:
    requested: GPT-6_maximum
    actual: GPT-5.6_Sol
    reasoning_level: UNVERIFIED
  closure_claim: false
  shared_result_ledgers_edited: false
  email_or_drive_used: false
  scheduler_changed: false
```

**BOTTOM LINE:** the source interval did not move. The run nevertheless identifies the correct dependence-preserving finite boundary carrier, finds its direct 2004 prior art rather than falsely claiming novelty, supplies an exact Bellman/synchronizing verifier architecture, proves \(\gamma_2=\sup_w\gamma_w\) with Alexander's rigorous asymptotic transfer, and pinpoints the next metric-moving problem as compressed exact Bellman certification at larger width or an effective iid strip-to-full upper error.

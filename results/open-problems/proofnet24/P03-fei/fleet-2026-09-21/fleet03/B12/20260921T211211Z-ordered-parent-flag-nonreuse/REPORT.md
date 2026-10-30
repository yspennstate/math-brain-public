# B12 FEI creative attempt: stop-conditioned martingale coding, a bent obstruction to the unconditional TC refund, and an exact nonreuse repair

**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. No authenticated brain retrieval or receiver-context use occurred.  
**Route:** spectral-sample compression / sequential prediction at the joint B/C interface, with exact nonreuse.  
**Mechanism change:** **YES**. The preceding B12 route used one curvature witness per inserted label. This run instead attacks the new all-witness tensorization remainder by exposing the prefix stopping time as martingale side information.  
**Novelty:** no publication-priority claim is made.

Fresh owner control was read before the mathematics. The live natural-language `FEI-SEVEN-TASKS-2026-09-21` and `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z` orders govern B12 despite the stale provisional `roles.json` row. No later fleet03/B12 pause or stop was observed.

The required FEI files were read in the required order: `TASKS_2026-09-21.md`, then the read-once `REPORT.md`, then `APPROACHES.md`. The shared joint `ORDER.md` and `RESEARCH_STATE.md` were also read before the present argument.

## 1. Named other-account result actually consumed

`consumed_peer_artifact`:

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T2100Z-prefix-tc-refund/REPORT.md`

read at scientific snapshot `28eb593ef50251e09475a7a7aa8c20647599f376`, report blob `21547dcdb11438c03b38ddb30d10c371d8cd99be`.

That report takes B12's uniform-prefix/Palm insertion law and proves the exact all-witness tensorization

\[
D_{\rm seq}+I\,\operatorname{TC}(P)
=I\sum_k I_2(L;Y_k)+I\,\operatorname{TC}(P\mid L),
\]

where `S` is the spectral sample, `I=E|S|`, `P` is the random unordered predecessor prefix, `L` is the next inserted label, and `Y_k=1_{k\in P}`. It combines this with the exact prefix code to isolate the remainder

\[
R_{\rm pref}=I\operatorname{TC}(P)-\mathbb E\log_2(K!),\qquad K=|S|,
\]

and names the influence-scale bound `R_pref=O(I)` as a next possible universal implication.

`applied_to_claim`: **Is there a universal finite `C` such that `R_pref(f) <= C I(f)` for every Boolean `f`?**

The answer is **NO**. The obstruction is an explicit Boolean bent family, not a non-Boolean random-set relaxation. The failure points to an exact repair: condition the all-witness tensorization on the prefix stopping time `T=|P|`.

## 2. REFUTED: the unconditional prefix-TC remainder is not O(I)

### 2.1 An explicit Boolean bent family

For every even `n=2m`, define

\[
f_n(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{n-1}x_n},
\]

where the exponent is in `F_2`.

For the two-bit factor `(-1)^{ab}`, all four Walsh coefficients have magnitude `1/2`. Tensoring the `m` independent pairs therefore gives

\[
|\widehat f_n(A)|=2^{-n/2}\quad\text{for every }A\subseteq[n].
\]

Hence the squared Fourier law is exactly uniform on all subsets:

\[
S\sim \operatorname{Unif}(2^{[n]}),\qquad
K\sim\operatorname{Bin}(n,1/2),\qquad I=n/2.
\tag{2.1}
\]

This family itself is easy for FEI: `H(S)=n=2I`. It is used only to stress the proposed coding remainder.

### 2.2 Exact prefix-size law

Under the uniform-prefix edge law, sample the terminal set with size bias, order it uniformly, and choose a uniformly random insertion edge. Put

\[
T=|P|.
\]

For every random terminal size `K`, this construction gives

\[
\Pr(T=t)=\frac{\Pr(K>t)}{I},\qquad t=0,1,\ldots,n-1.
\tag{2.2}
\]

For the bent family, conditional on `T=t`, symmetry makes `P` uniform over the `t`-subsets of `[n]`. Also

\[
\mathbb E T=\frac{\mathbb E[K(K-1)]}{2I}=\frac{n-1}{4},
\]

so every prefix bit has marginal

\[
\beta_n=\Pr(k\in P)=\frac{n-1}{4n}.
\tag{2.3}
\]

Consequently

\[
H(P)=H(T)+\mathbb E\log_2\binom nT,
\]

and therefore

\[
\operatorname{TC}(P)
=n h_2(\beta_n)-H(T)-\mathbb E\log_2\binom nT.
\tag{2.4}
\]

### 2.3 Asymptotic lower bound

For `K~Bin(n,1/2)`, the tail formula (2.2) and binomial concentration imply `T/n` converges in the Riemann-sum sense to the uniform law on `[0,1/2]`, while `H(T)=o(n)`. Thus

\[
\frac1n\mathbb E\log_2\binom nT
\longrightarrow
2\int_0^{1/2} h_2(x)\,dx
=\frac1{2\ln2}.
\]

Since `beta_n -> 1/4`, we obtain

\[
\boxed{
\frac{\operatorname{TC}(P)}n
\longrightarrow
c_0:=h_2(1/4)-\frac1{2\ln2}
=0.089930604014651\ldots>0.
}
\tag{2.5}
\]

On the other hand

\[
\mathbb E\log_2(K!)=O(n\log n).
\]

Because `I=n/2`, (2.5) yields

\[
\boxed{
\frac{R_{\rm pref}}{n^2}
\longrightarrow
\frac{c_0}{2}
=0.044965302007326\ldots>0,
}
\tag{2.6}
\]

and in particular

\[
\frac{R_{\rm pref}}I\to\infty.
\]

Therefore the universal statement `R_pref <= C I` is **REFUTED for every finite C**.

This is not a failure of FEI. It says that the unconditional total correlation introduced by simultaneous bitwise tensorization contains a huge amount of **shared stop-time dependence** that is an artefact of the prefix representation.

## 3. Current-run numerical stress test

A standard-library checker is committed beside this report. It evaluates (2.2)--(2.4) and the stop-conditioned quantities below. Representative values are:

| n | TC(P) | R_pref/I | TC(P|T) | R_T/I |
|---:|---:|---:|---:|---:|
| 20 | 0.772030877223 | -1.442224451679 | 1.957508702270 | -0.256746626632 |
| 58 | 3.576792204460 | 0.019560380936 | 2.773087169282 | -0.784144654241 |
| 100 | 7.011223286222 | 2.719883239229 | 3.179730797828 | -1.111609249164 |
| 200 | 15.549786985019 | 10.298539346503 | 3.690677041395 | -1.560570597120 |
| 500 | 41.906863234479 | 35.361096254904 | 4.359339339356 | -2.186427640219 |
| 1000 | 86.391105992013 | 78.855678000201 | 4.862308436757 | -2.673119555054 |

So the unconditional remainder crosses positive already near this range and then grows rapidly relative to influence, exactly as (2.6) predicts.

## 4. PROVED: exact stop-conditioned all-witness nonreuse identity

The obstruction identifies the hidden variable that must be exposed to the martingale code: the current prefix length itself.

Let again

\[
Y_k=1_{\{k\in P\}},\qquad T=|P|.
\]

Define conditional total correlations

\[
\operatorname{TC}(P\mid T)
:=\sum_k H_2(Y_k\mid T)-H_2(P\mid T),
\]

\[
\operatorname{TC}(P\mid L,T)
:=\sum_k H_2(Y_k\mid L,T)-H_2(P\mid L,T).
\]

### Theorem 4.1 — stop-conditioned tensorization

For the uniform-prefix edge law of **every random subset distribution**,

\[
\boxed{
D_{\rm seq}+I\operatorname{TC}(P\mid T)
=
I I_2(L;T)
+I\sum_k I_2(L;Y_k\mid T)
+I\operatorname{TC}(P\mid L,T).
}
\tag{4.1}
\]

In particular, since conditional total correlation is nonnegative,

\[
\boxed{
D_{\rm seq}+I\operatorname{TC}(P\mid T)
\ge
I I_2(L;T)+\Gamma_T,
\qquad
\Gamma_T:=I\sum_k I_2(L;Y_k\mid T).
}
\tag{4.2}
\]

#### Proof

For every random vector `P=(Y_1,...,Y_n)`, conditional on `T`,

\[
\begin{aligned}
\sum_k I_2(L;Y_k\mid T)-I_2(L;P\mid T)
&=\sum_k[H(Y_k\mid T)-H(Y_k\mid L,T)]\\
&\quad-[H(P\mid T)-H(P\mid L,T)]\\
&=\operatorname{TC}(P\mid T)-\operatorname{TC}(P\mid L,T).
\end{aligned}
\]

Because `T=|P|` is a deterministic function of `P`,

\[
I_2(L;P)=I_2(L;T)+I_2(L;P\mid T).
\]

Multiply by `I` and use `D_seq=I I_2(L;P)`. Rearrangement gives (4.1), and (4.2) follows from `TC(P|L,T)>=0`. `square`

This is **exact nonreuse**. Every transverse prefix bit may again contribute simultaneously, but the common stopping-time dependence is not charged once per bit: it is supplied once as side information `T`.

## 5. PROVED: repaired prefix-code inequality

The inherited exact prefix decomposition is

\[
H(S)=J_{\rm stop}+\operatorname{Br}-\mathbb E\log_2(K!),
\]

with

\[
\operatorname{Br}=I H_2(L)-D_{\rm seq}.
\]

Apply (4.2). Since

\[
H_2(L)-I_2(L;T)=H_2(L\mid T),
\]

we obtain the universal bound

\[
\boxed{
H(S)
\le
J_{\rm stop}
+I H_2(L\mid T)
-\Gamma_T
+R_T,
}
\tag{5.1}
\]

where the **repaired dependence/factorial remainder** is

\[
\boxed{
R_T:=I\operatorname{TC}(P\mid T)-\mathbb E\log_2(K!).
}
\tag{5.2}
\]

This replaces the refuted unconditional `R_pref` by a quantity in which the mechanically shared prefix-size correlation has been removed before tensorization.

Equation (5.1) is **not FEI closure**. In particular, neither a universal influence-scale upper bound for `R_T` nor a sufficient lower bound for the level-conditioned predictor bank `Gamma_T` is proved here.

## 6. Attempted refutation of the repair: the bent family now goes in the favorable direction

For the same bent family, conditional on `T=t`, `P` is a uniform `t`-subset. Hence

\[
\boxed{
\operatorname{TC}(P\mid T)
=\mathbb E_T\left[
 n h_2(T/n)-\log_2\binom nT
\right].
}
\tag{6.1}
\]

Stirling's formula makes the bracket only `O(log n)` uniformly away from endpoints, with the tail endpoints harmless under (2.2). Thus

\[
\operatorname{TC}(P\mid T)=O(\log n).
\]

Meanwhile

\[
\mathbb E\log_2(K!)
=\frac n2\log_2 n+O(n).
\]

Therefore

\[
\boxed{
R_T=-\frac n4\log_2 n+O(n),
}
\tag{6.2}
\]

so the bent family that destroys `R_pref=O(I)` does **not** destroy the stop-conditioned repair; it gives a large negative credit. The finite values in Section 3 already have `R_T/I<0` throughout the displayed range.

This is evidence for the repair, not a universal theorem about `R_T`.

## 7. B/C-interface interpretation

The preceding B12 curvature bridge identifies the unconditional prefix occupancies with the mixed-derivative depth bank:

\[
\Pr(k\in P)=\frac{d_k}{2I},
\qquad
\Pr(k\in P\mid L=i)=\frac{\kappa_{ik}}{8p_i}.
\]

The fleet02 signed-current compiler has, independently, produced an exact nonnegative post-cancellation **parent** mass vector `mu_j`, and fleet02/B18 proves every positive parent-indexed physical pair measure is paid by `sum_j mu_j J(g_j)`. The remaining C-interface problem is therefore not another unconditional sum over pair witnesses. What is now needed is a **level-conditioned** version of the B-side curvature/flag observable, or an authentic parent-indexed physical flag whose conditioning tracks the martingale stop without spending the same current/terminal bank twice.

The stop-conditioned identity (4.1) gives the exact information-theoretic shape such a compiler should target: reveal one scalar stage `T`, then spend the residual flags conditionally. It prevents the bent-spectrum common-cause dependence from masquerading as a quadratic information debt.

No signed/PSD source-to-physical contraction is asserted here.

## 8. Status distinctions

- **REFUTED:** `R_pref(f) <= C I(f)` for a universal finite `C`, where `R_pref=I TC(P)-E log_2(K!)` is the fleet01/B18 unconditional tensorization remainder.
- **PROVED:** the exact stop-conditioned tensorization identity (4.1) for every random subset law.
- **PROVED:** the repaired universal prefix-code inequality (5.1) for every Boolean spectral law, assuming only the inherited exact prefix decomposition.
- **CHECKED / EVIDENCE:** the explicit bent family has `R_T<0` over the displayed finite dimensions and asymptotically `R_T=-(n/4)log_2 n+O(n)`.
- **OPEN:** whether `R_T` admits a universal influence-scale upper bound or telescoping payment on all Boolean spectra.
- **OPEN:** whether `Gamma_T` can be converted into a level-conditioned signed-curvature / physical-flag bank with exact nonreuse.
- **OPEN / NOT PROVED:** full uniform-cube FEI.

## 9. Next attack and joint handoff

`remaining_implication`:

> Either prove `R_T <= C I` (or a stronger telescoping cancellation of `R_T` against the factorial credit) for Boolean Fourier spectra, **or** derive a level-conditioned curvature/physical flag bank `Gamma_T` whose payment absorbs any positive part of `R_T` without reusing the fleet02 current/Ward/terminal ledgers.

The most concrete next calculation is to condition the exact pair-curvature identity

\[
q_{ik}=\Pr(i,k\in S)=\kappa_{ik}/4
\]

on spectral level `K` / insertion stage `T`, then ask whether the resulting stagewise pair matrix has a physical derivative representation that can feed fleet02/B16's parent masses and fleet02/B18's arbitrary-pair mask payment. This is now an exact higher-order conditioning question rather than an uncontrolled pairwise-reuse problem.

`next_recipient`: **fleet01/B18** should replace its unconditional `R_pref=O(I)` target by (4.1)--(5.2) in the sequential integrator; **fleet02/B16/B18** are the natural compiler-side consumers of the level-conditioned flag target.

`full_problem_change`: **NONE** — full FEI remains open.  
`mechanism_change`: **YES** — unconditional TC refund -> stop-conditioned martingale tensorization, forced by an explicit Boolean bent counterexample.

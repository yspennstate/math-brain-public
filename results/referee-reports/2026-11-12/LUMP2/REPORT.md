MAJOR

The manuscript should not be disseminated unchanged. Theorem 1 claims a discrete alternative for $K(7)$ that the paper does not establish. The setup of the rank-one proposition also omits a necessary hypothesis, and its identity is false under the literal stated hypotheses. Both defects have precise local repairs. After those repairs, I found no further mathematical failure in the main upper bound, the strict single-pair bound, the comb lower bound, or the hitting-set proposition. In particular, **$K(6)=3$ and $K(8)=4$ are proved**. External source authentication remains incomplete because the cited primary texts are absent and this audit is offline.

The distinction matters: an unsupported strengthening is an error in the paper, even if it may eventually turn out to be true. Conversely, unsuccessful attempts to break a proof do not certify its novelty or its references.

## Errors requiring correction

### 1. Theorem 1 does not prove $K(7)\in\{3,4\}$

**Location:** `paper/lumping.tex:115`; the last sentence of the lower-bound proof at lines 491–494.

**What is wrong:** The paper excludes every value strictly between 3 and 4 without an argument. Its bounds give only

\[
3\le K(7)\le4.
\]

**Evidence:** The definition at lines 102–105 is a supremum of real ratios, with arbitrary real conductances. There is no integrality theorem for this supremum. Direct enumeration of the proposed upper bound gives

\[
\left(\min(2^{7-q},q-1)\right)_{q=2}^{6}=(1,2,3,4,2).
\]

Thus $U(7)=4$. The six-state comb gives the lower bound 3. Neither fact excludes, for example, a supremum of $7/2$. This is a logical gap, not a claim that $7/2$ is the actual answer. `K7P_REPORT.md` explicitly retains the interval and identifies an unresolved rank-two case; it does not supply the missing integrality result.

**Exact fix:** Replace `and $K(7)\in\{3,4\}$` by `and $3\le K(7)\le4$`. Replace “The values of $K(n)$ follow from Table…” at line 494 by “The stated exact values and the bounds on $K(7)$ follow from Table…”. A proof determining $K(7)$ would be an alternative repair; no such proof is presently provided.

### 2. The rank-one proposition needs an exact fibre condition

**Location:** Section 3, `paper/lumping.tex:270`, preceding Proposition 8; the claimed identity at line 280 and the argument at lines 297–299.

**What is wrong:** Requiring $f(u)=f(v)=\hat v$ and injectivity on $J=I\setminus\{u,v\}$ does **not** say that $u,v$ are the only states mapped to $\hat v$. One state of $J$ may also map there. The proof assumes that cannot happen: otherwise $J$ is not the set of singleton quotient states, and deleting $\hat v$ does not leave $L_{JJ}$.

**Exact counterexample:** Take four states $0,1,2,3$ and $w_{ij}=1$ for every ordered pair, including loops. Then $P_{ij}=1/4$, $\pi_i=1/4$, and

\[
H(i,j)=4\quad(i\ne j),\qquad E_\pi T_j=3,
\qquad F_{ii}=-3,\quad F_{ij}=1\ (i\ne j).
\]

Set $u=0,v=1$, and use fibres $A=\{0,1,2\}$, $B=\{3\}$. The map is injective on $J=\{2,3\}$, exactly as required by line 270. The quotient has conductances and stationary law

\[
\widehat w=\begin{pmatrix}9&3\\3&1\end{pmatrix},\qquad
\widehat\pi=(3/4,1/4).
\]

Its rows are independent draws from this law. Hence

\[
\widehat F_{AA}=-E_{\widehat\pi}\widehat T_A
=-\frac14\frac43=-\frac13.
\]

But $\beta_2=F_{21}-F_{20}=0$. The proposed identity at $i=j=2$ gives $\widehat F_{AA}=F_{22}=-3$, a contradiction. `audit_inventory.py` independently reproduces these fractions by hitting-time solves.

**Exact fix:** Add $f^{-1}(\hat v)=\{u,v\}$ to line 270, retaining injectivity on $J$. Equivalently, state that the fibres are precisely $\{u,v\}$ and the singletons of $J$. Theorem 2 already says “keeping the other states apart,” so this is a local hypothesis defect; it does not refute the intended single-pair theorem.

## Suggestions and checks still required

### 3. Source numbers and priority: to check, not authenticated

**Location:** Introduction, Section 4, Section 6, and `paper/bib_main.tex`.

No primary source is supplied locally. Earlier audit reports repeat the same limitation and are not substitutes for those sources. The following is the complete list of mathematical source checks needed; none is being labelled a demonstrated misattribution.

| Citation and manuscript location | Attribution to check | Offline result / required action |
|---|---|---|
| AF Chapter 4 and Section 4.6.1, lines 61, 68, 165–167 | Parameter notation; stationary conductance quotient; four-vertex hitting-time example | **To check** against the cited edition. Quotient and hitting arguments are independently sound. Confirm whether “doubles” describes attainment or a limiting example. |
| LW95 and AF Theorem 9.4, lines 73–76 | Attainment and the stopping-rule hitting-time formula | **To check** the precise source statement, theorem number, and any chronology implicit in “showed.” The formula and attainment are independently established in finding 11. |
| Aldous82, AF Theorem 4.6, LW98, lines 78–79 and 142 | Absolute-constant comparison with continuous-time total variation; relaxation comparison | **To check** metric, time normalization, threshold, hypotheses, and numbering. These comparisons are not used to derive the new exact constants. |
| AF Proposition 4.44, lines 81–84 and 380 | Contraction of maximal commute, average hitting, relaxation and Cheeger times | **To check** the full cited list and conventions. Relaxation contraction needed here is independently proved by the variational argument. |
| AF Open Problem 4.45, lines 86–88 | The displayed quotation about induced-chain stopping mixing | **To check** verbatim wording and edition. The historical fact that Hermon–Peres answered it is supplied in the task and is explicitly credited in the manuscript. |
| HP Theorem 3$c$, lines 91–93 | Bounded-degree lazy-walk examples; pair identifications; logarithmic increase | **To check** exact theorem lettering, graph assumptions, and quotient operation. The present audit cannot authenticate those details. |
| HP Remark 1.8, lines 94–96 and 393–396 | Logarithmic upper bound and its optimal order | **To check** exact statement and conventions. The upper-bound mechanism described in the paper is mathematically consistent. |
| AF Open Problem 4.48$b$, lines 140–142 | Whether the comparison with constant one was asked there | **To check** numbering, wording, and whether the question concerns precisely this stopping parameter. No present-day priority claim for Lemma 3 can be certified offline. |
| AF Section 4.3, line 377 | Random stationary-target hitting rule and the random-target identity | **To check** source location. The identity is independently checked and explained below. |
| AF Proposition 3.13 and Lemma 4.24, line 378 | Discrete-time eigentime identity | **To check** both locators and normalization. The identity used in the paper is correct. |
| AF Lemma 4.23, lines 387–388 | Discrete-time stopping bound with constant $4e/(e-1)$ | **To check** the exact constant and time convention in the source. Finding 8 gives a stronger self-contained inequality, so this citation is not needed to justify the displayed bound mathematically. |
| LP Section 2.2, lines 194–196 and 518–523 | Harmonic potential and Green/resistance identities, including loops | **To check** locator and loop convention. Both identities are independently derived here. |
| LP Section 2.4, lines 527–529 | Rayleigh monotonicity under identification | **To check** locator. The application has the right direction. |
| `bib_main.tex:1–16` | Titles, author names, publication details, DOIs, arXiv identifier | **To check** against primary records. The HP DOI matches the DOI supplied in the task. No other bibliographic metadata is certified by this audit. |

**Exact action:** Obtain the cited passages locally and check them against this list before submission. In particular, do not describe this audit as having verified the theorem numbers. If the source for the numerical constant in Remark 9 is uncertain, replace that step with the self-contained argument in finding 8.

The mathematical novelty is described correctly **relative to the history supplied in the task**: the abstract and lines 91–96 credit Hermon and Peres with the negative answer to Open Problem 4.45. This manuscript does not claim to be the first counterexample to monotonicity or to a universal constant. Its stated contribution is the dependence on the number of states for arbitrary weighted reversible chains, a sharp single-pair constant, and the associated finite-state bounds. That goes beyond the bounded-degree logarithmic statement as the manuscript describes it. Whether these particular refinements, Lemma 3, or Proposition 4 already appear elsewhere remains **to check**. The prose alone cannot establish global novelty.

The asserted logarithmic upper order for bounded-degree graphs is coherent: $\pi_*\ge c/n$, stationary masses increase under lumping, and relaxation time contracts. The standard lazy/continuous-time comparisons would transfer the HP lower examples to stopping-rule mixing up to absolute constants. Verify that those examples and comparisons have exactly the properties attributed to them.

### 4. Process and AI prose is confined to back matter, but duplicated

**Location:** `paper/tail.tex:2–7`, `20–28`, and `34–35`; the input occurs at `paper/lumping.tex:548`.

The numbered mathematical sections contain no sentence about preparing the manuscript, an earlier version, AI authorship, or searching for references. The numerical-check description at lines 541–546 is ordinary reproducibility information, not a history of writing the paper.

The following process material does appear in the rendered document:

- `tail.tex:2–7`: the acknowledgements describe multiple agents, their shared memory, coordination and auditing, and advertise the framework papers/repositories.
- `tail.tex:21–28`: the AI declaration describes the project, an October 2026 discovery, individual model contributions, preparation of the manuscript, recomputation, and the author's responsibility.
- `tail.tex:34–35`: the code-availability section adds a project-affiliation sentence.

These are explicit unnumbered back-matter sections, preceding the notation appendix; their position in the TeX input does not make them part of the mathematical argument. I therefore do not manufacture a body-text violation from them. **Suggested fix:** remove the process narrative from the acknowledgements, retain ordinary funding/conflict/code statements, and put any journal-required AI disclosure solely in the designated declaration or submission metadata. If “no process prose” is intended to cover the entire rendered article, remove the cited process sentences from the article and supply the disclosure separately. No previous-version or reference-search narrative was found.

### 5. One check program can report failed checks and still exit successfully

**Location:** `paper/code/lumping_checks.py:116–173`; manuscript check summary at `paper/lumping.tex:541–546`.

`hitting_trials` records failures in `ok`, `ok_tau0`, and `ok_upper`, returns them, and the main program prints/writes the result. It never turns a false flag into a nonzero exit status. Thus a caller who treats successful process exit as “all checks passed” could be misled. This is a validation weakness, not a counterexample to any theorem or a discrepancy in the stated trial counts.

**Suggested exact fix:** after computing the result, raise an exception or exit nonzero unless all three flags are true. Preserve the diagnostic output. The manuscript's counts are correct: 25 networks at each of four sizes give 100 networks; $25(3+6+10+15)=850$ single-pair quotients; the comb grid has 20 points; the other program has 400 trials. No table/code numerical disagreement was found.

## Results checked independently

### 6. Theorem 1's bounds and the exact small cases survive the audit

**Location:** `paper/lumping.tex:98–128`, `367–384`, `491–494`. No correction is needed beyond finding 1.

For a nontrivial quotient from $m$ to $q$ states, the intended Theorem 2 gives a factor strictly below $2^{m-q}$. The chain of inequalities in the manuscript gives the other bound:

\[
T(\widehat X)\le\tau_0(\widehat X)
\le(q-1)\tau_2(\widehat X)
\le(q-1)\tau_2(X)
\le(q-1)T(X).
\]

Here and below $T(X)$ denotes the paper's stopping-rule mixing time. The first inequality uses an independent stationary random target. The second uses the eigentime identity, the third the restricted Dirichlet variational principle, and the last Lemma 3. This argument handles negative eigenvalues; it uses the second largest eigenvalue, not the second largest modulus.

Identity quotients have ratio 1 and one-state quotients have ratio 0. For the other quotients $2\le q\le m-1$, maximize the two bounds and then use $m\le n$. The admissible $q$'s for $m\ge3$ remain admissible for larger $n$, and $2^{m-q}\le2^{n-q}$, so $U(m)\le U(n)$; $m=2$ is handled directly. Finally every term is at most $q-1\le n-2$, with $U(2)=1$.

`audit_inventory.py` enumerates every admissible integer $q$, without floating point:

| $n$ | $\lfloor n/2\rfloor$ | $U(n)$ | Maximizing $q$ |
|---:|---:|---:|---|
| 2 | 1 | 1 | Defined separately |
| 3 | 1 | 1 | 2 |
| 4 | 2 | 2 | 3 |
| 5 | 2 | 2 | 3, 4 |
| 6 | 3 | 3 | 4 |
| 7 | 3 | 4 | 5 |
| 8 | 4 | 4 | 5, 6 |
| 9 | 4 | 5 | 6 |
| 10 | 5 | 6 | 7 |
| 11 | 5 | 7 | 8 |
| 12 | 6 | 8 | 9 |
| 13 | 6 | 8 | 9, 10 |
| 14 | 7 | 9 | 10 |
| 15 | 7 | 10 | 11 |
| 16 | 8 | 11 | 12 |
| 17 | 8 | 12 | 13 |
| 18 | 9 | 13 | 14 |
| 19 | 9 | 14 | 15 |
| 20 | 10 | 15 | 16 |

As a second way to understand the enumeration, put $d=n-q$: it maximizes $\min(2^d,n-d-1)$, the minimum of an increasing and a decreasing sequence. Only the indices next to their crossing can maximize it.

The small cases have complete proofs, not just sampled chains:

| States allowed | Lower bound | Upper bound | Conclusion |
|---|---|---|---|
| 2, 3 | Identity quotient | $U=1$ | $K(2)=K(3)=1$ |
| 4, 5 | $N=0$ comb on four states, limit 2 | $U=2$ | $K(4)=K(5)=2$ |
| 6 | $N=1$ comb on six states, limit 3 | $U(6)=3$ | $K(6)=3$ |
| 7 | Same six-state comb; the definition allows fewer states | $U(7)=4$ | $3\le K(7)\le4$ |
| 8 | $N=2$ comb on eight states, limit 4 | $U(8)=4$ | $K(8)=4$ |

In particular, $U(8)=4$ is not a mistaken extrapolation of the (n-2) bound. Its terms for $q=2,\ldots,7$ are exactly (1,2,3,4,4,2). Likewise the $n=6$ terms are (1,2,3,2). The lower bounds use suprema, so strictness for every finite single merge is compatible with $K(4)=2$.

### 7. Theorem 2: the potential identities, minimum argument, and strictness are sound for exactly one pair

**Location:** Sections 2–3, `paper/lumping.tex:184–235`, `269–347`. Add the hypothesis in finding 2; no further proof repair was found.

**Hitting and centering identities, lines 199–234.** With $D=\operatorname{diag}(w_x)$, $L=D(I-P)$, and $\omega=(w_x)$, first-step equations give

\[
LH(\cdot,j)=\omega-w\delta_j,\qquad H(j,j)=0.
\]

The missing coordinate at $j$ is forced by the zero sum of the Laplacian's coordinates. Grounding at $o$ gives $L\Gamma\delta_j=\delta_j-\delta_o$ for $j\ne o$, and $L\zeta=\omega-w\delta_o$. Consequently the stated expression

\[
H(i,j)=\zeta_i-\zeta_j-w(\Gamma_{ij}-\Gamma_{jj})
\]

has exactly this Laplacian and boundary value, including $j=o$. Uniqueness follows from connectedness. Symmetry of $\Gamma$ gives

\[
\sum_i\pi_i\Gamma_{ij}=\zeta_j/w,\qquad
E_\pi T_j=\bar\zeta-2\zeta_j+w\Gamma_{jj},
\]

and therefore

\[
F_{ij}=\zeta_i+\zeta_j-\bar\zeta-w\Gamma_{ij}.
\]

Thus $F$ is symmetric, its rows and columns have zero stationary mean, and $LF\delta_j=\omega-w\delta_j$. A row maximum $\kappa_i$ is nonnegative. For $\varphi_i=\kappa_i-F_{i\cdot}$,

\[
L\varphi_i=w\delta_i-\omega,\quad
E_\pi\varphi_i=\kappa_i,\quad
\mathcal E(\varphi_i,g)=w(g_i-E_\pi g),\quad
\mathcal E(\varphi_i,\varphi_j)=-wF_{ij}.
\]

Every sign is correct. Loops cancel from $L$ and the energy, but remain in $\omega,w,\pi$; deleting them from the speed measure would invalidate the argument, and the paper does not do so.

**Rank-one identity, lines 289–307.** Ground at $v$. The harmonic function $h=P_x(T_u<T_v)$ is the voltage of the unit current from $u$ to $v$, divided by $R$, so $\Gamma_{iu}=Rh_i$ and $\Gamma_{uu}=R$. It follows that

\[
\beta_i=F_{iv}-F_{iu}=wR(h_i-\bar h).
\]

For the exact pair quotient, the Schur-complement identity gives the lifted grounded inverse $\widetilde\Gamma=\Gamma-Rhh^{\mathsf T}$. Its (J,J) block is $L_{JJ}^{-1}$; its rows at (u,v) vanish. Weighted double centering gives $F=-w\mathcal C_\pi(\Gamma)$. Since total weight is preserved and the new mass is $\pi_u+\pi_v$, centering commutes with lifting this quotient matrix. Hence

\[
\widehat F_{f(i)f(j)}=F_{ij}+wR(h_i-\bar h)(h_j-\bar h)
=F_{ij}+\frac{\beta_i\beta_j}{wR}.
\]

This is a Schur complement of the inverse, not an assumption about the original projected process being Markov.

**The minimum step, lines 310–335.** If $\beta_i\beta_j\le0$, the new entry is at most $F_{ij}\le\kappa_i\le T(X)$. Otherwise swap (u,v) if necessary so both betas are positive and put $g_i=\varphi_i/\beta_i$, $g_j=\varphi_j/\beta_j$, $\eta=\min(g_i,g_j)$. Nonnegativity is retained. Both functions have boundary difference 1; taking their minimum retains that difference exactly. Subtracting $\eta(v)+h$ leaves a function zero at both boundary states and energy-orthogonal to $h$. Thus

\[
\mathcal E(\eta,\eta)\ge1/R.
\]

The remainders $\xi_i=g_i-\eta$, $\xi_j=g_j-\eta$ are nonnegative with disjoint supports, so

\[
\mathcal E(\xi_i,\xi_j)
=-\sum_{x\ne y}w_{xy}\xi_i(x)\xi_j(y)\le0.
\]

Expansion gives

\[
1/R\le\mathcal E(g_i,\eta)+\mathcal E(g_j,\eta)-\mathcal E(g_i,g_j).
\]

The source identities evaluate the right side as

\[
\frac w{\beta_i}(\eta(i)-\bar\eta)
+\frac w{\beta_j}(\eta(j)-\bar\eta)
+\frac{wF_{ij}}{\beta_i\beta_j}.
\]

Using the other potential to bound each evaluation, $\eta(i)\le(\kappa_j-F_{ij})/\beta_j$ and $\eta(j)\le(\kappa_i-F_{ij})/\beta_i$, gives exactly

\[
\widehat F_{f(i)f(j)}
\le\kappa_i+\kappa_j-(\beta_i+\beta_j)\bar\eta.
\]

There is no hidden assumption that a minimum of arbitrary harmonic functions is harmonic; the proof only uses its boundary values, energy and nonnegativity.

**Strictness, lines 339–346.** In the positive-beta orientation, $\eta(u)=\eta(v)+1\ge1$, so $\bar\eta\ge\pi_u>0$. The correction is strictly positive. In the opposite-sign case the entry is at most $T(X)<2T(X)$. The original time is positive for an irreducible chain with at least two states, as the paper's Laplacian contradiction proves. Taking a maximum over finitely many entries preserves strictness. The $N=0$ comb approaches ratio 2, proving optimality. There is no contradiction between strict finite inequalities and the sharp supremum.

**Independent evidence:** `audit_random.py` uses direct target-by-target solves of $ (I-P)_{I\setminus\{j\}}h=\mathbf1$, with an independently assembled quotient. It does not import either author program. The run checked 35 fresh random looped networks of sizes 2–8, four periodic paths, and seven complete graphs: 46 base networks in total; 445 pair quotients; 19,357 lifted entries; 11,782 positive-product minimum checks; and 225 choices of grounded root. All identities, energy signs, source evaluations, refined inequalities and strict bounds passed in exact arithmetic. The largest random/periodic merge ratio was about 1.184758; the structured comb separately tests the sharp regime near 2.

### 8. Lemma 3 and the relaxation/logarithmic arguments are mathematically valid

**Location:** `paper/lumping.tex:144–151`, `351–365`, `375–397`. No mathematical correction is required; source checks remain as in finding 3.

Normalize the nonzero real eigenfunction so $g(i)=1$ and $\lvert g\rvert\le1$. Stationarity and $\lambda\ne1$ give $\pi g=0$. The proposed martingale has increment

\[
\mathcal M_{t+1}-\mathcal M_t=g(X_{t+1})-\lambda g(X_t),
\]

with conditional mean zero and absolute value at most $1+|\lambda|\le2$. If $EU<\infty$, optional stopping is justified by applying it to $U\wedge t$ and using $ |\mathcal M_{U\wedge t}|\le1+2U$. The terminal stationary law gives $E g(X_U)=0$, so

\[
1=(1-\lambda)E\sum_{s<U}g(X_s)\le(1-\lambda)EU.
\]

Independent auxiliary randomization preserves the martingale property. Infinite $EU$ is immediate. Negative eigenvalues are allowed. Taking $\lambda_2$ proves $\tau_2\le T$.

For a two-state chain $P_{01}=p,P_{10}=q$, direct hitting times give $T=1/(p+q)=\tau_2$. On the loopless complete graph with $m$ states, $T=(m-1)/m=\tau_2$. Thus both equality assertions at line 151 are correct. Exact checks included the periodic two-state alternator, with $T=\tau_2=1/2$.

The random-target identity and eigentime formula can be obtained from $Z=(I-P+\Pi)^{-1}$:

\[
H(i,j)=(Z_{jj}-Z_{ij})/\pi_j,\qquad
\tau_0=\operatorname{tr}Z-1
=\sum_{k=2}^m\frac1{1-\lambda_k}.
\]

Here $Z\mathbf1=\mathbf1$, so averaging the hitting formula over the target makes the answer independent of the starting state. Restricting the Dirichlet quotient to fibre-constant functions proves relaxation contraction. The exact random audit also checked $T L-D+\omega\omega^{\mathsf T}/w\succeq0$ by rational Schur elimination; this is a second formulation of $T\ge\tau_2$.

The displayed logarithmic bound is valid independently of its citation. Let $P_s=e^{s(P-I)}$, with rate-one Poissonization. The centered hitting identity and reversible spectral expansion give

\[
F_{ij}=\int_0^\infty\left(1-\frac{P_s(i,j)}{\pi_j}\right)ds,
\qquad
\left|\frac{P_s(i,j)}{\pi_j}-1\right|
\le e^{-s/\tau_2}\sqrt{(1/\pi_i-1)(1/\pi_j-1)}
\le\pi_*^{-1}e^{-s/\tau_2}.
\]

The integrand is also at most 1. Integrating the smaller upper bound proves

\[
T\le\tau_2(1+\log(1/\pi_*)).
\]

This implies the manuscript's weaker bound with $4e/(e-1)$. Poissonization is just a representation of the discrete-time inverse here; it does not change the hitting-time normalization. Combining this inequality with $\widehat\pi_*\ge\pi_*$, relaxation contraction and Lemma 3 gives the stated logarithmic quotient bound. No laziness assumption is needed for this stopping-time argument.

### 9. The comb's closed forms, maximizers and limits are correct

**Location:** Section 5, `paper/lumping.tex:400–513`, especially Proposition 10 at lines 426–482. No correction is required.

There are (2N+4) original states, (N+3) quotient states and (N+1) pair merges. Internal edges are included twice in the new loop. The quotient's non-loop graph is the specified path with leaf $b$, including the $N=0$ star case.

An independent graph traversal, deleting each tree edge and summing all row weights in the component away from $c$, gives

\[
S_k=t+1+r^{k+1}+[2+\alpha(t+1)]\sum_{l=1}^k r^l\quad(k<N),
\]

\[
S_N=t+1+r^{N+2}+[2+\alpha(t+1)]\sum_{l=1}^N r^l
+(t+1)\alpha r^{N+1}.
\]

The quotient cut adds exactly the row weight of $y_k$, $t\alpha r^{k+1}$, and its crossing conductance is $(1+\alpha)r^{k+1}$. The bridge formula therefore gives exactly the paper's $M,\widehat M$. A tooth or $b$ contributes a holding time $t$ followed by a shorter suffix of the same spine sum, so $M=\max_x H(x,c)$; $\widehat M\ge t$ similarly bounds all quotient hitting times to $\hat c$.

For completeness, the stationary centering terms recomputed from the graph are

\[
\mu:=E_\pi T_c=
\frac{t^2(1+\alpha\sigma_{N+1})+
\sum_{k=0}^{N-1}S_k^2/r^{k+1}+S_N^2/r^{N+2}}{w},
\]

\[
\widehat\mu:=\widehat E_{\widehat\pi}\widehat T_{\hat c}=
\frac{t^2(1+\alpha r^{N+1})+
\sum_{k=0}^{N-1}\widehat S_k^2/[(1+\alpha)r^{k+1}]}{w}.
\]

These follow either by averaging path hitting times or by $w\mu=\sum_e S_e^2/w_e$; the symbolic program checks both constructions. Empty sums handle $N=0$.

The claimed maximizing entries are justified, not guessed numerically. In the original tree, every pair of non-root states shares the final edge to $c$, so $\Gamma_{ij}\ge r^{-(N+2)}$. When $w\ge Mr^{N+2}$, their $F$-entry is at most $M-\mu$, attained at ((a,c)). In the quotient the paths from $a$ and $b$ to $\hat c$ share no edge, giving $\widehat F_{ab}=\widehat M+t-\widehat\mu$. Entries involving the root or $b$ are no larger. Two states on the other arm share its final edge; the additional displayed sufficient condition makes their entries no larger either. The separate $N=0$ argument is valid.

For fixed $N$, the geometric sum bound and $r=t^3,\alpha=t$ yield

\[
M=t+N+1+O(t^{-1}),\qquad
\widehat M=(N+1)t-N+O(t^{-1}).
\]

Also $S_N=O(r^{N+2})$, $w\ge(N+2)r^{N+4}$, and the maximal relevant hitting times are $O(t)$. Thus $\mu,\widehat\mu=O(t^{-5})\to0$, just as claimed. Both sufficient conditions hold eventually: the dominant term of $w$ has degree (3N+12), whereas $Mr^{N+2}$ has degree (3N+7) and, for $N\ge1$, $(\widehat M-t)(1+\alpha)r^N$ has degree (3N+2). Consequently

\[
\frac{T(\widehat X)}{T(X)}\longrightarrow N+2,
\qquad \frac{\widehat M}{M}\longrightarrow N+1.
\]

No uniformity in growing $N$ is needed for the lower bound: for each fixed $n\ge4$, choose $N=\lfloor n/2\rfloor-2$, then let $t\to\infty$. The definition permits $2N+4\le n$. This proves the lower bound for odd sizes as well, without a padding argument.

The minimum stationary weight is $w_a=t$, so $\pi_*=t/w$. For fixed $N$, $w\sim(N+2)t^{3N+12}$, hence $\log(1/\pi_*)=(3N+11)\log t+\log(N+2)+o(1)$. The order assertion in Remark 9 is consistent.

`audit_comb.py` verifies graph-derived identities symbolically with independent $t,r,\alpha,\ell$, for $N=0,\ldots,4$, then verifies all stated limits after substitution. It independently solves the transition hitting equations at $N=0,\ldots,4$, $t\in\{2,5/2,3,10,1000\}$. All 25 points pass exactly, including both sufficient conditions and the maximizing entries. Thus the claim that the conditions already hold at $t=2$ for $N\le3$ is confirmed.

The independent $t=1000$ values, before the manuscript's rounding, are:

| $N$ | $T(X)$ | $T(\widehat X)$ | Mixing ratio | $\widehat M/M$ |
|---:|---:|---:|---:|---:|
| 0 | 1001.001001 | 2000.000000 | 1.998000 | 0.999000 |
| 1 | 1002.001002 | 2999.001998 | 2.993013 | 1.995010 |
| 2 | 1003.002003 | 3998.003997 | 3.986038 | 2.989031 |
| 3 | 1004.003004 | 4997.005996 | 4.977083 | 3.981070 |

All manuscript entries round correctly; exact fractions are saved in `audit_comb_results.json`.

### 10. The hitting-set proposition and its claimed sharpness are valid

**Location:** Proposition 4 at `paper/lumping.tex:169–177`; Section 6 at lines 516–538; abstract lines 42–43. No correction is required.

For $B=I\setminus A$, the killed matrix satisfies $I-P_B=D_B^{-1}L_B$, giving the visit Green matrix $G=L_B^{-1}D_B$. Thus $G(y,y)=w_yR(y,A)$, including loops. Visits include time zero and exclude the terminal hit. The strong Markov property gives $G(x,y)=P_x(T_y<T_A)G(y,y)$, and summing visits gives $E_xT_A=\sum_yG(x,y)$.

Shorting a fibre and wiring the whole target together restricts the admissible voltage functions. Effective conductance therefore increases, so effective resistance decreases: $\widehat R(\hat y,\widehat A)\le R(y,A)$ for every $y$ in the source fibre. The direction used in the paper is correct, even when the source fibre itself has multiple vertices. Consequently

\[
\widehat E_{\hat x}\widehat T_{\widehat A}
\le\sum_{\hat y\notin\widehat A}\widehat w_{\hat y}\widehat R(\hat y,\widehat A)
\le\sum_{y\notin A}w_yR(y,A)
=\sum_{y\notin A}G(y,y)
\le\sum_{y\notin A}E_yT_A
\le(n-|A|)\max_yE_yT_A.
\]

The saturated-target condition $A=f^{-1}(\widehat A)$ is essential and is stated. For the comb, choose $A=\{z_N,c\}$, $\widehat A=\{\hat c\}$. Then $\max_yE_yT_A\le M$ and the quotient time from $a$ is $\widehat M$, so the ratio is at least $\widehat M/M\to N+1$. Since $n-|A|=2N+2$, these examples are asymptotically within factor 2 of the upper bound. This supports the abstract's asymptotic assertion; it does not claim optimality for every pair $(n,|A|)$. The $N=0$ case presents no exception: the target-hitting ratio is exactly 1.

The independent random audit checked 3,472 target-subset instances across identity, arbitrary, and one-state partitions where applicable, for every starting state via vector inequalities. The 25 exact comb checks also compare the actual set-target denominator against $M$. No failure occurred.

### 11. The definitions are consistent; the stopping formula has no missing additive constant

**Location:** `paper/lumping.tex:48–76`, `98–108`; notation appendix. No required correction; adding “irreducible” explicitly to the $K(n)$ definition would improve readability.

The original network is connected off the diagonal, hence irreducible. The quotient is the reversible chain obtained by averaging transitions with the stationary conditional law. It is generally **not** the process $f(X_t)$ for arbitrary initial distributions; the paper does not assume otherwise. Summing ordered conductances correctly turns an internal edge of weight $c$ into loop mass $2c$. Total mass and stationary fibre masses are preserved, and iterated quotienting is associative.

The stopping time is an ordinary randomized stationary stopping rule, not a strong stationary time. Independence of the terminal state and stopping time is not imposed. Hitting times start at zero on their targets, and all hitting/Green/potential formulas use that convention. Periodicity is allowed; continuous-time comparisons and negative eigenvalues do not create an inconsistency.

Here is a self-contained verification of the stopping formula and attainment, so its mathematics does not rest on an unchecked citation. For any stationary stopping rule from $i$ with finite expectation, let $x_y$ be the expected number of departures from $y$ before stopping. Conservation gives

\[
x(I-P)=e_i^{\mathsf T}-\pi^{\mathsf T},\qquad \sum_yx_y=E_iU.
\]

Multiply by $H(\cdot,j)$, using $(I-P)H(\cdot,j)=\mathbf1-e_j/\pi_j$. Then

\[
F_{ij}=E_iU-x_j/\pi_j\le E_iU.
\]

For the reverse inequality in a reversible chain, take $\kappa_i=\max_jF_{ij}$, $\varphi_i=\kappa_i-F_{i\cdot}\ge0$ and $x_y=\pi_y\varphi_i(y)$. The potential equation gives the same conservation equation, and $\sum_yx_y=\kappa_i$. On each arrival at $y$, stop with probability $\pi_y/(x_y+\pi_y)$, otherwise move by $P$. This defines an adapted rule with independent coin flips. All stopping probabilities are positive on the finite state space, so the rule has finite mean. The unique expected arrival vector is $x+\pi$, because

\[
x+\pi=e_i^{\mathsf T}+xP.
\]

Its terminal distribution is $\pi$, its expected departures are $x$, and its mean time is $\kappa_i$. Thus the minimum is attained and $T(X)=\max_{i,j}F_{ij}$ exactly, with no $+1$. The occupation equations were also checked exactly on the sampled chains.

The supremum over **at most** $n$ states is crucial: it makes $K(n)$ nondecreasing and lets even-size combs supply odd-size lower bounds directly. The denominator is positive for every original chain under consideration. One-state quotient times are zero and identity quotient ratios are one, so neither creates an undefined ratio. Nothing in these definitions makes $K(n)$ integer-valued.

## Audit artifacts and limits

All audit programs were written here before execution and import no author code:

| Program | Output | Purpose / measured cost |
|---|---|---|
| `audit_core.py` | Imported library | Rational Gaussian solves of killed transition matrices, quotient aggregation, independent energy and grounded-inverse utilities |
| `audit_random.py` | `audit_random_output.txt` | Exact potential, occupation, minimum, eigenvalue/PSD, pair, arbitrary-partition and set checks; 6.91 s, 17,612,800 bytes peak RSS |
| `audit_comb.py` | `audit_comb_output.txt`, `audit_comb_results.json` | Symbolic graph derivation, limits, and 25 exact direct-solve comparisons; 16.19 s, 81,838,080 bytes peak RSS |
| `audit_inventory.py` | `audit_inventory_output.txt`, `audit_inventory_results.json` | $U(n)$, counterexample, citation inventory and manuscript/code SHA-256 snapshot; under 0.01 s, under 20 MB peak RSS |
| `audit_report_check.py` | `audit_report_check_output.txt` | Final source-hash, report-table, artifact and formatting checks |

Each computation has a 240-second alarm. They ran one audit computation at a time, except that the tiny inventory check could overlap the comb check; neither numerical-library threading nor subprocess workers are used. The shell refused an additional `nice` adjustment; the final checking process confirmed inherited niceness 15. All computations were short and far below the memory/time limits. No browser, external write, push, visible window, or other agent was used. The original manuscript and author programs were left unchanged. Findings were appended to `LOG.md` as obtained.

Reproduce from this directory, one program per invocation:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit_random.py
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit_comb.py
env PYTHONDONTWRITEBYTECODE=1 python3 audit_inventory.py
```

Finite tests do not establish universal inequalities. The arguments above explain why the intended proofs work, where the printed statements exceed them, and which external claims remain unauthenticated.

Task: “Find every error, gap, overclaim and misattribution” — 12 November 2026, 23:17 +04 (first recorded local work; exact prompt receipt time unavailable).

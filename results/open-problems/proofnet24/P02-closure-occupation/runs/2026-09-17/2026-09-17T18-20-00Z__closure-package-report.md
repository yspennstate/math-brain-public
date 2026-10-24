Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested, but the exposed scheduler/runtime has no model selector or reasoning-effort selector; I do not claim GPT-6 or verified maximum reasoning.

Problem/source: **David Aldous and James Allen Fill, _Reversible Markov Chains and Random Walks on Graphs_ (unfinished 2002 manuscript; 2014 recompilation), Open Problem 2.34, “Portmanteau theorem for occupation times,” intake I0023. NO MOVEMENT in the frozen metric: 11/11 -> 11/11. Section-B moves this run: #11 DUALIZE, #12 FIND WHAT IS CONSERVED, #30 DO ONE DIRECTION AT A TIME. Status moves from PARTIAL/closure-pending to PROVED / repository closure-package complete; publication-level novelty remains UNVERIFIED and no public posting is claimed.**

# 1. Continuity and exact source scope

I did not restart I0023. I recovered the current P02 state from the newest canonical P02 report,

`proofnet24/P02-closure-occupation/runs/2026-09-16/2026-09-16T19-01-54Z__run-report.md`,

creation commit `e04031c428b2c970e6ef265ac9e04468b6db7bbc`, and retained the theorem report

`proofnet24/P02-closure-occupation/runs/2026-09-16/2026-09-16_17-04-02__run-report.md`,

creation commit `8d40b5b3f5370e8209f63015a19b8a957be10e57`, containing `P02-OCC-C5-ROOTED-GROVE-PORTMANTEAU`.

I also reread the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE state, the I0023 claim/intake surface, the current P26 reconciliation report, the P01 audit/prior-art reports, and the newest P03 report for the directed audit duty. The intake search again resolves I0023 to the Aldous--Fill source and P02 ownership; no competing ownership was found.

The exact source scope remains:

- finite-state irreducible **discrete-time** Markov chain;
- Chapter 2 explicitly does **not** require reversibility;
- “number of visits before time S” counts time 0 and excludes time S;
- in the periodic case the source uses the Cesàro/continuized interpretation of the fundamental matrix `Z`;
- the frozen Section 2.2.2 identity list is exactly Lemmas 2.5, 2.6, 2.7; Corollary 2.8; Lemma 2.9; Corollary 2.10; Lemmas 2.11, 2.12; Corollaries 2.13, 2.14; Lemma 2.15.

The source asks whether these results can be formulated as a single theorem and, by analogy with Feynman diagrams, asks for a rule associating a marked occupation expression such as visits to `j` before `min(T_k,T_l)` to a combinatorial structure and then to a formal function of the marked stationary/fundamental-matrix data. The source itself notes that elementary matrix treatments and more general occupation-measure identities already exist. Therefore repository closure is based on the **intrinsic rooted-grove compiler plus its marked `(pi,Z)` bridge**, not on claiming that the underlying matrix identity itself is novel.

# 2. Frozen metric and denominator

The frozen metric is

> number of the eleven original Section 2.2.2 identities covered by one proved formula, with the denominator retained exactly.

It remains

`11/11 -> 11/11`.

For each nonempty boundary `A`, the frozen denominator is

\[
M_A=\begin{pmatrix}Z_A^T&-\pi_A\\ \mathbf 1^T&0\end{pmatrix},
\qquad
\Delta_A=\det M_A.
\]

Nothing in this run renames or changes this denominator.

# 3. Closure theorem retained exactly

Let `P=(p_uv)` be the transition matrix, `pi` the stationary law, `L=I-P`, and `Z` the Aldous--Fill fundamental matrix. For nonempty `A`, put `U=V\A` and

\[
T_A=\inf\{t\ge0:X_t\in A\}.
\]

Let `F_A` be the total transition-weight of directed spanning forests converging to the root set `A`. For `i,j notin A`, let

\[
F_{A\cup\{j\}}(i\to j)
\]

be the total weight of forests rooted at `A union {j}` in which the component containing `i` is rooted at `j`. Let `Ttree` denote the total weight of all one-root converging spanning trees.

The retained theorem is

\[
\boxed{
G_A(i,j):=E_i\sum_{t<T_A}{\bf1}_{\{X_t=j\}}
=
\frac{F_{A\cup\{j\}}(i\to j)}{F_A}.
}
\]

The frozen denominator and numerator have the independent rooted-grove interpretations

\[
\boxed{\Delta_A=\frac{F_A}{Ttree}>0},
\]

and

\[
\boxed{
\mathcal N_{A;i,j}
=
\frac{F_{A\cup\{j\}}(i\to j)}{Ttree}},
\]

where

\[
\mathcal N_{A;i,j}
=
\det\begin{pmatrix}
Z_A^T&-\pi_A&Z_{iA}^T\\
\mathbf1^T&0&1\\
Z_{Aj}^T&-\pi_j&Z_{ij}
\end{pmatrix}.
\]

Hence

\[
\boxed{G_A(i,j)=\mathcal N_{A;i,j}/\Delta_A}.
\]

The forest is defined directly on the transition graph; it is not defined by expanding this determinant. Thus the determinant gives a second evaluation of the same partition-function ratio.

The arbitrary stopping/boundary-data form is equally retained. Let `T` be integrable, with initial law `sigma`, terminal law `tau` supported on `A`, occupation vector

\[
x_j=E_\sigma\sum_{t<T}{\bf1}_{\{X_t=j\}},
\]

and boundary occupation `c=x_A`. For `q notin A`, put

\[
\mu_q=\sigma_q+\sum_{a\in A}c_a p_{aq}.
\]

Then, for `j notin A`,

\[
\boxed{
x_j=\frac1{F_A}\sum_{q\notin A}\mu_qF_{A\cup\{j\}}(q\to j).
}
\]

Equivalently, with

\[
\mathcal N_{\sigma,c;A,j}
=
\det\begin{pmatrix}
Z_A^T&-\pi_A&z_{\sigma,A}^T-c^T\\
\mathbf1^T&0&1\\
Z_{Aj}^T&-\pi_j&z_{\sigma j}
\end{pmatrix},
\]

one has

\[
\boxed{x_j=\mathcal N_{\sigma,c;A,j}/\Delta_A}.
\]

## Proof mechanism, retained

1. Since the finite irreducible chain hits every nonempty `A` almost surely with finite mean, the killed Green matrix is

\[
G_A=(I-P_{UU})^{-1}=L_{UU}^{-1}.
\]

2. Cramer plus the directed all-minors matrix-tree theorem gives

\[
(G_A)_{ij}=F_{A\cup\{j\}}(i\to j)/F_A.
\]

3. For `t != 0`, put `L_t=L+tPi`, `Pi=1 pi^T`. From the group-inverse identities,

\[
L_t^{-1}=Z+t^{-1}Pi.
\]

The Markov-chain tree theorem gives `adj(L)=Ttree 1 pi^T`, hence `det L_t=t Ttree`. Jacobi complementary minors applied to `L_t`, followed by the rank-one determinant identity and `t -> 0`, yields

\[
\Delta_A=F_A/Ttree.
\]

4. The conserved pathwise flow is

\[
\boxed{x(I-P)=\sigma-\tau}.
\]

Restricting columns to `U` yields

\[
x_U(I-P_{UU})=\sigma_U+cP_{AU}=\mu,
\]

so the rooted-grove arbitrary-boundary formula follows from the killed Green formula.

5. Multiplying the conserved flow by `Z` and using `(I-P)Z=I-Pi` gives

\[
x=\sigma Z-\tau Z+s\pi^T,
\qquad s=E_\sigma T.
\]

Restriction to `A` gives the bordered system

\[
M_A\binom{\tau_A}{s}
=
\binom{z_{\sigma,A}^T-c^T}{1}.
\]

Since `Delta_A>0`, this is uniquely solvable; its Schur complement gives the frozen bordered determinant formula. Combining the two evaluations gives the numerator forest interpretation.

# 4. Source prototype and complete minimal case

For distinct marked states `i,j,k,l`, take `A={k,l}`. Then

\[
\boxed{
E_i(\#\hbox{ visits to }j\hbox{ before }\min(T_k,T_l))
=
\frac{F_{\{k,l,j\}}(i\to j)}{F_{\{k,l\}}}.
}
\]

The combinatorial object is intrinsic: `k,l,j` are roots, `i` is constrained to the `j`-rooted component, and unmarked vertices are internal forest vertices summed over. The same ratio is exactly the frozen marked `(pi,Z)` numerator divided by `Delta_{k,l}`.

This is the source's displayed type of example and is the complete minimal two-boundary case requested by the current P02 instructions before extension.

# 5. Explicit 11/11 source accounting

The self-contained package preserves the following derivations from the one theorem.

1. **Lemma 2.5.** Stop at the strict return `T_i^+`. Here `A={i}`, terminal law is `delta_i`, and the time-zero boundary occupation is `c_i=1`. The `Z` terms cancel in the conservation identity, so `x=s pi`; since `x_i=1`,

\[
E_iT_i^+=1/\pi_i.
\]

2. **Lemma 2.6.** In the same specialization,

\[
E_i(\#j\hbox{ before }T_i^+)=\pi_j/\pi_i.
\]

3. **Lemma 2.7.** Singleton hitting and the fundamental-matrix hitting identity give

\[
E_j(\#j\hbox{ before }T_i)
=\pi_j(E_jT_i+E_iT_j).
\]

4. **Corollary 2.8.** The visits to `i` before `T_j` form a geometric count with success probability `P_i(T_j<T_i^+)`; taking the reciprocal of its mean gives the source formula.

5. **Lemma 2.9.** For `i,j != l`,

\[
E_i(\#j\hbox{ before }T_l)
=\pi_j(E_iT_l+E_lT_j-E_iT_j).
\]

6. **Corollary 2.10.** Strong Markov at `T_j` and the preceding occupation formula give

\[
P_i(T_j<T_l)
=
\frac{E_iT_l+E_lT_j-E_iT_j}{E_jT_l+E_lT_j}.
\]

7. **Lemma 2.11.** Start from stationarity and stop at `T_i`; since `pi^T Z=0`,

\[
\pi_iE_\pi T_i=Z_{ii}.
\]

8. **Lemma 2.12.** Singleton boundary equation:

\[
\pi_jE_iT_j=Z_{jj}-Z_{ij}.
\]

9. **Corollary 2.13.** Sum Lemma 2.12 over `j` and use `sum_j Z_{ij}=0`:

\[
\sum_j\pi_jE_iT_j=\operatorname{tr}Z.
\]

10. **Corollary 2.14.** The right side is independent of `i`, which is the random target lemma.

11. **Lemma 2.15.** Start from stationarity and stop at `T_i`:

\[
E_\pi(\#j\hbox{ before }T_i)
=\frac{\pi_j}{\pi_i}Z_{ii}-Z_{ij}.
\]

Thus the frozen metric remains exactly **11/11**, with one theorem and one denominator family `Delta_A`.

# 6. What the three new-method moves contributed

## #11 DUALIZE

Instead of treating the marked determinant as the primary object, the proof uses two dual descriptions of the same killed potential kernel:

- `L_UU^{-1}` as the Green operator / solution of a Dirichlet problem;
- cofactors of `L_UU` as rooted-grove partition functions.

The frozen `(pi,Z)` determinant is then recovered by the complementary-minor/group-inverse bridge. This is the useful duality: potential kernel versus forest cofactor, not another determinant expansion masquerading as combinatorics.

## #12 FIND WHAT IS CONSERVED

The conserved quantity is the exact pathwise expected-flow equation

\[
\boxed{x(I-P)=\sigma-\tau}.
\]

It is the mechanism that turns one killed-Green formula into the full arbitrary stopping/boundary-data theorem. It also explains why the strict-return cases and stationary-start cases belong to the same theorem instead of requiring separate ad hoc formulas.

## #30 DO ONE DIRECTION AT A TIME

The final architecture is boundary-first:

1. solve the killed problem for one fixed `A`;
2. identify the exact denominator `Delta_A` with `F_A/Ttree`;
3. derive the two-boundary source prototype `A={k,l}` completely;
4. add arbitrary boundary data via conserved flow;
5. specialize to the frozen eleven identities.

This avoids a global “diagram grammar” whose correctness would have to be guessed before its elementary boundary blocks were understood.

# 7. Exact finite certificate packaged, not regenerated

The required exact certificate already existed under P02 and was copied byte-for-byte into the closure package, rather than manufacturing a redundant checker run.

Packaged files:

- `proofnet24/P02-closure-occupation/paper_af234_rooted_grove_portmanteau/check.py`
- `proofnet24/P02-closure-occupation/paper_af234_rooted_grove_portmanteau/check.out`

The packaged `check.py` has the same blob as the validated C5 checker: `29f1a608f2bcaddfe23ffc94bb9be9a5914b0f57`.

The packaged output has blob `38cddb20f1b1bbbae9a04a7de37651ea949dd51a` and records exact-rational PASS on:

- a reversible lazy three-state chain;
- a periodic nonreversible directed three-cycle;
- a nonreversible four-state chain;
- 26 denominator forest identities;
- 94 numerator forest identities.

No floating-point equality is used.

# 8. Two distinct OTHER-track full audits: gate is now 2/2

The previously missing audit gate has cleared.

## Audit 1 — P26

`P26-AUDIT-P02-I0023-C5-ROOTED-GROVE-04 = PASS_MATHEMATICS / SOURCE_LITERAL_PASS / PRIOR_ART_UNVERIFIED`.

Report creation commit:

`12bb57d37208bfc01baf494e46f6a87a4f1c90e4`.

P26 independently rederived the conservation law, killed Green formula, all-minors forest interpretation, exact frozen denominator, arbitrary boundary-data theorem, nonreversible/periodic scope, and the eleven source specializations. It also reread the source and judged the full-state rooted-grove object to satisfy the literal wording “combinatorial structure involving the marked states”; the source does not require that the combinatorial object contain only marked vertices.

## Audit 2 — P01

`P01-AUDIT-P02-I0023-C5-ROOTED-GROVE-74 = PASS_MATHEMATICS / SOURCE_LITERAL_PASS / PRIOR_ART_UNVERIFIED`.

Report:

`proofnet24/P01-baum-connes/runs/2026-09-16/2026-09-16T21-12-00Z__run-report.md`,

creation commit `77d2229b99e1eee42e0349facfbab14205514fac`.

This is a distinct OTHER track and an end-to-end C5 audit, not a second copy of P26 or an older claim-scoped P01 component check.

P26 subsequently reconciled the two as

`P26-RECONCILE-P02-I0023-C5-TWO-AUDITS-07 = PASS_2_OF_2_MATHEMATICAL_AUDITS / PRIOR_ART_UNVERIFIED / NOT_POSTED`.

Therefore the campaign's independent-audit closure requirement is satisfied.

# 9. Dated prior-art check — 17 September 2026

I ran a fresh bounded search before packaging. Queries included, among variants:

- `Aldous Fill Open Problem 2.34 portmanteau occupation times`;
- `"Portmanteau theorem for occupation times" Markov chains`;
- `Pitman Occupation measures for Markov chains 1977`;
- `Chebotarev Agaev Forest matrices around Laplacian matrix 2002`;
- `Pitman Tang Tree formulas mean first passage times Kemeny constant 2018`;
- `Chung Zeng Forest formulas discrete Green functions 2023`;
- marked/bordered variants combining `Z`, `pi`, occupation times, forests and determinants.

The check confirms substantial prior art for the ingredients:

- **Pitman (1977), _Occupation measures for Markov chains_**: its abstract explicitly states that a basic occupation-measure identity gives a unified approach to a variety of moment identities for Markov chains.
- **Chebotarev--Agaev (2002), _Forest matrices around the Laplacian matrix_**: weighted directed in-forest matrices represent generalized inverses/eigenprojections and give the Markov-chain tree theorem.
- **Pitman--Tang (2018), _Tree formulas, mean first passage times and Kemeny's constant of a Markov chain_**: combinatorial tree/forest formulas for finite-chain Green functions, hitting probabilities and related quantities.
- **Chung--Zeng (2023), _Forest formulas of discrete Green's functions_**: directed and weighted forest formulas for Green functions and hitting times.

P01's later proximity audit additionally flags that group-inverse/forest bridges are known and that Pitman--Tang already puts finite-chain Green/tree formulas and the Aldous--Fill/Kemeny fundamental matrix in the same paper.

What the bounded search did **not** locate is an explicit publication claiming the exact combined package:

1. the Aldous--Fill frozen bordered denominator `Delta_A` in marked `(pi,Z)` variables;
2. its exact rooted-grove normalization `F_A/Ttree`;
3. the arbitrary stopping/boundary-data compiler;
4. one-rule accounting of the exact eleven Section 2.2.2 identities;
5. an explicit statement that this resolves Open Problem 2.34.

That negative search result is **not** a novelty certificate. Publication-level novelty remains **UNVERIFIED**. The repository status `PROVED` below means source-level mathematics plus the campaign closure gates are complete; it does not mean “first publication of a new theorem.”

# 10. Closure package created and read back

Required package folder:

`proofnet24/P02-closure-occupation/paper_af234_rooted_grove_portmanteau/`

Files created:

1. `README.md` — exact source statement/scope, proved result, lineage, audits and prior-art posture. Creation commit `6cf5f1aa0d99d90e91050c0298edd70f93bede39`; verified blob `41f0321f07e60acd66375ec01e030737f95f9dda`.
2. `main.tex` — self-contained source-matching theorem, full proof, source prototype, explicit eleven specializations, prior-art caveat and audit record. Creation commit `77ed9f9ecf46936580dc197254ff206c869ac62d`; read back from that exact commit.
3. `check.py` — packaged exact-rational forest/determinant certificate. Creation commit `d97e85f46f1b2c459aee0cb64ee08e4e3a834818`; verified blob `29f1a608f2bcaddfe23ffc94bb9be9a5914b0f57`.
4. `check.out` — archived PASS output. Creation commit `0b4e9554f2897a512930702e84114ca83e643467`; verified blob `38cddb20f1b1bbbae9a04a7de37651ea949dd51a`.

The package is deliberately narrow: it says what the source asks, what is proved, what is classical/known in substance, which exact compiler is being packaged, and what remains unverified about publication priority.

# 11. Independent P02 -> P03 audit duty

Newest recovered P03 report:

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T17-32-28Z__i0126-stuck-recovery-1-dominating-defect.md`,

creation commit `3f15cd800021aa0359cabece6d28a2d0919b9677`, blob `9621caaf1c758e331240ef812a159d9d3fe89aee`.

Audited claim:

`P03-I0126-DOMINATING-PAIR-CARD-DEFECT-251`.

Verdict:

**`P02-AUDIT-P03-I0126-DOMINATING-PAIR-DEFECT-31 = PASS (CLAIM-SCOPED)`**.

Here is the independent derivation.

For a graph `G`, let `D2(G)` be the number of unordered dominating vertex-pairs. For a vertex `v`, let

- `P_G(v)` be the number of vertices `w` such that `{v,w}` dominates `G`;
- `Q_G(v)` be the number of pairs in `G-v` that dominate `G-v` but fail to dominate `G`.

Deleting `v` removes exactly the `P_G(v)` dominating pairs incident with `v`. Conversely, a pair not incident with `v` is newly counted in `D2(G-v)` precisely when it is one of the `Q_G(v)` pairs. Therefore

\[
\boxed{D_2(G-v)=D_2(G)-P_G(v)+Q_G(v)}.
\]

Hence the card-visible defect is

\[
\boxed{\delta_G(v):=D_2(G)-D_2(G-v)=P_G(v)-Q_G(v)}.
\]

Now let `C` be a common base graph and obtain `G_A` by adding one new vertex `z` adjacent exactly to `A subseteq V(C)`. For `w in V(C)` define

\[
R_C(w)=V(C)\setminus(N_C(w)\cup\{w\}).
\]

Then `{z,w}` dominates `G_A` iff every base vertex not already dominated by `w` is adjacent to `z`, namely iff

\[
R_C(w)\subseteq A.
\]

Thus

\[
P_{G_A}(z)=P_C(A):=\#\{w:R_C(w)\subseteq A\}.
\]

A pair `{u,v}` contained in `C` dominates `C` but fails to dominate `G_A` exactly when neither endpoint is adjacent to `z`, i.e. exactly when `u,v notin A`. Hence

\[
Q_{G_A}(z)=Q_C(A):=\#\{\{u,v\}:\{u,v\}\text{ dominates }C,\ u,v\notin A\}.
\]

Therefore

\[
\boxed{D_2(G_A)-D_2(C)=P_C(A)-Q_C(A)=:\Delta_C(A)}.
\]

For a one-swap ambiguity

\[
A=S\cup\{x\},\qquad B=S\cup\{y\},
\]

put

\[
U_x(S)=\#\{w:R_C(w)\setminus S=\{x\}\},
\]

and

\[
T_x(S;y)=\#\{t\notin S\cup\{x,y\}:\{x,t\}\text{ dominates }C\}.
\]

Only residual sets requiring exactly `x` versus exactly `y` change when passing from `B` to `A`, so

\[
P_C(A)-P_C(B)=U_x(S)-U_y(S).
\]

For the disjoint dominating-pair count, the pairs present in `Q_C(B)` but removed from `Q_C(A)` are precisely `{x,t}` counted by `T_x(S;y)`, while the reverse discrepancy is `T_y(S;x)`. Hence

\[
Q_C(A)-Q_C(B)=T_y(S;x)-T_x(S;y).
\]

If the equal-deck hypothesis gives `Delta_C(A)=Delta_C(B)`, subtraction yields exactly

\[
\boxed{U_x(S)+T_x(S;y)=U_y(S)+T_y(S;x)}.
\]

No independence assumption or finite enumeration enters this derivation. Scope of this audit: it checks the extension algebra and one-swap balance in Claim 251, conditional on P03's stated reconstructibility input for `D2`; it does **not** certify the full Kelly--Ulam reconstruction conjecture, P03's separate finite enumeration, or publication novelty.

# 12. Honest status ledger

## PROVED / repository closure-complete

- `P02-OCC-C5-ROOTED-GROVE-PORTMANTEAU` under the exact finite irreducible discrete-time source scope.
- Frozen denominator identity `Delta_A=F_A/Ttree>0`.
- Rooted-grove numerator identity.
- Arbitrary stopping/boundary-data compiler.
- Exact 11/11 Section 2.2.2 source coverage.
- Source prototype `min(T_k,T_l)` grove rule.
- Existing exact-rational finite certificate.
- Two distinct OTHER-track full mathematical/source audits: P26 and P01.
- Required self-contained paper folder now exists.

## KNOWN IN SUBSTANCE / classical ingredients

- occupation-measure unification (Pitman 1977);
- elementary finite-state matrix methods;
- directed matrix-tree/all-minors machinery;
- forest representations of Laplacian generalized inverses/Green kernels;
- tree/forest formulas for hitting times, Green functions and Kemeny-type quantities.

## DISPROVED AS METHODS ONLY

Retain the earlier exact failures of naive subset/stationary-conditioned substitutions and the unsigned permanent/Wick compiler. These do not refute Open Problem 2.34.

## UNVERIFIED

- publication-level novelty of the exact frozen marked `(pi,Z)` rooted-grove compiler package;
- existence of a later publication explicitly declaring Open Problem 2.34 resolved by an equivalent formulation.

These are literature-classification questions, not remaining gaps in the source-level proof.

# 13. Successor screen

The user instructed P02 to claim the top eligible unassigned CLOSABLE target after actual closure. I therefore rechecked current queue/ownership evidence rather than treating an old queue row as current authorization.

The previously certified closable reserve entries are no longer available:

- `I0035` is reserved/claimed by C31;
- `I0066` has a P15 claim;
- `I0068` has a P19 claim;
- `I0055` is not an open successor: current repository evidence records Pengfei Tang (2020) as positively answering the modified question in the corrected source scope.

Recent coordinator/rotation reports likewise record that no currently certified `READY / CLOSABLE / UNASSIGNED` successor is available after ownership/status checks. Admission-pending proposed targets on other tracks are not P02 property and are not safe to seize.

Therefore:

**no successor claim is created in this run.**

P02's I0023 assignment is mathematically closure-packaged, and the P02 recurring research slot should stop rather than produce maintenance runs until an authorized new closable target is actually admitted.

# 14. Model/runtime control and denied-task handling

The model-control situation is still the same after inspecting the actual scheduler interface. The exposed task operations contain:

- title;
- prompt;
- schedule;
- timing mode;
- enabled/disabled state.

They expose **no model selector, no reasoning-effort selector, no guaranteed-duration selector, and no authenticated effective-model telemetry**. Making GPT-6 / maximum a verifiable task property would require a product/runtime feature that persists those settings and returns the effective values in run metadata; prompt text cannot install such a control.

A historical P26 scheduler ID once returned `You cannot modify this task`. I did not mutate P26 merely to probe permissions. The legitimate recovery is: refresh the task inventory and use the current owner-visible task; if an authorized requested modification is still denied, the owner/admin/platform context must perform it. There is no worker-side permission bypass, and creating a duplicate schedule is not a valid workaround.

# 15. Closure decision

The campaign closure conditions specified by the owner are now all present for I0023:

1. **full theorem-sized argument on the page** — yes, canonical C5 report plus self-contained `main.tex`;
2. **exact certificate for the finite core** — yes, exact rational `check.py` and archived `check.out`;
3. **prior-art search recorded with limitations** — yes, including the fresh 17 September 2026 search and explicit known-in-substance classification;
4. **two independent audits by OTHER tasks** — yes, P26 and P01;
5. **paper folder** — yes, `paper_af234_rooted_grove_portmanteau/`.

Accordingly the source-level repository status advances from **PARTIAL** to **PROVED / CLOSURE-PACKAGED**.

This does **not** assert that the result has been publicly posted, peer-reviewed, or established to be publication-novel. Those labels remain separate.

# 16. ledger_delta for P26

```yaml
ledger_delta:
  track: P02
  intake: I0023
  source: "Aldous--Fill, Reversible Markov Chains and Random Walks on Graphs, Open Problem 2.34"
  category: CLOSABLE_OUTSIDE
  metric_name: "Section 2.2.2 source identities covered by one proved formula with frozen denominator"
  metric_before: "11/11"
  metric_after: "11/11"
  metric_movement: "NO MOVEMENT"
  status_before: "PARTIAL / closure-pending; research-retired after six unchanged metric runs"
  status_after: "PROVED / REPOSITORY_CLOSURE_PACKAGED / NOT_POSTED / PUBLICATION_NOVELTY_UNVERIFIED"
  theorem_claim: "P02-OCC-C5-ROOTED-GROVE-PORTMANTEAU"
  frozen_denominator: "Delta_A = det([[Z_A^T,-pi_A],[1^T,0]])"
  source_identity_coverage:
    - "Lemma 2.5"
    - "Lemma 2.6"
    - "Lemma 2.7"
    - "Corollary 2.8"
    - "Lemma 2.9"
    - "Corollary 2.10"
    - "Lemma 2.11"
    - "Lemma 2.12"
    - "Corollary 2.13"
    - "Corollary 2.14"
    - "Lemma 2.15"
  closure_package: "proofnet24/P02-closure-occupation/paper_af234_rooted_grove_portmanteau/"
  audit_count_full_other_tracks: "2/2"
  audits:
    - "P26-AUDIT-P02-I0023-C5-ROOTED-GROVE-04"
    - "P01-AUDIT-P02-I0023-C5-ROOTED-GROVE-74"
  audit_reconciliation: "P26-RECONCILE-P02-I0023-C5-TWO-AUDITS-07"
  prior_art: "ingredient mechanisms known in substance; exact complete compiler overlap unverified"
  successor_claim_created: false
  successor_reason: "no currently certified READY / CLOSABLE / UNASSIGNED target survives ownership/status screening"
  p03_audit: "P02-AUDIT-P03-I0126-DOMINATING-PAIR-DEFECT-31 = PASS (CLAIM-SCOPED)"
  requested_shared_ledger_action: "P26 should reconcile closure status and package path from immutable evidence; P02 does not edit root ledgers"
  requested_scheduler_action_after_verified_readback: "disable the P02 recurrence because I0023 is closure-packaged and no eligible successor exists"
```

**P02 I0023 final status after this run: PROVED / REPOSITORY CLOSURE-PACKAGED; NOT POSTED; PUBLICATION NOVELTY UNVERIFIED. Frozen metric 11/11.**

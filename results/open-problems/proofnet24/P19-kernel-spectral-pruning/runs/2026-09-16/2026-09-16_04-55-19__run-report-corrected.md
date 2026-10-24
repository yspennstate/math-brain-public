# ProofNet24 P19 — Kernel Spectral Pruning — CORRECTED CANONICAL REPORT

**Run timestamp:** 2026-09-16 04:55:19 Asia/Jerusalem  
**Repository / branch:** `yspennstate/math-open-problems` / `master`  
**Scope:** singular values/vectors, deterministic spectral/structured pruning, Marchenko–Pastur nulls, neural/random features, kernel/operator-learning prediction risk; **NO number theory**.  
**Delivery:** GitHub only. No email/Gmail/draft/forward action was used.  
**Runtime honesty:** the requested GPT-6 / maximum-reasoning selector is not exposed in this runtime. I used the deepest useful reasoning available and do not claim an unexposed model switch, hidden effort override, or independent agents.

## Correction history

The immutable first draft from this run is

`proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_04-55-19__run-report.md`

at commit `d0614c207d51651927699974d386c32c4d91a09c`.

Readback exposed a real proof defect in its proposed `P19-TYPICAL-BOUNDED-DIFF-37`: local good-good edge bounds do **not** in general imply that the restriction is Lipschitz for the ambient weighted Hamming metric, so the claimed McShane extension with unchanged coordinate constants was unjustified. That first file is intentionally left immutable. The present file supersedes it as the canonical report, retracts that theorem as stated, gives an exact counterexample to the failed extension route, and replaces it by two rigorous concentration routes:

1. a **one-sided robust-anchor theorem** specialized from Warnke's directly checked primary typical-bounded-differences theorem;
2. an independent **Doob replacement-split theorem** that works with predictable rare replacement tails without any extension argument.

This correction is substantive rather than typographical and is recorded explicitly.

---

# 0. Executive result

P19 remains **OPEN**.

The predecessor's target was `P19-RAREBOUNDARY-MGF-COMPOSE-37`: combine trained hard-top-`k` score-margin control with a legal feature/output envelope to obtain high-confidence same-observation prediction guarantees, without treating deterministic trained pruning as an iid mask.

This run establishes the exact logical boundary.

**PROVED:** if a sample is in a robust good event `Gamma` on which every arbitrary one-coordinate replacement remains locked to the same double-deletion pruning anchor and obeys an `O(1/n)` pathwise prediction envelope, then the clipped leave-one-out gap satisfies a genuine exponential Warnke/McDiarmid-type tail. This is `P19-ROBUST-ANCHOR-TL-37` plus `P19-WARNKE-ROBUST-LOO-37`.

**PROVED:** if only predictable *probabilistic* rare replacement tails are available, an exact Doob decomposition gives a rigorous small-influence plus rare-contamination inequality, `P19-RARE-REPLACEMENT-DOOB-SPLIT-37`.

**DISPROVED:** the tempting shortcut used in the first draft—small coordinate changes only when both endpoints happen to lie in a high-probability good set, followed by an unchanged-constant McShane extension—is false. `P19-DISCONNECTED-GOODSET-CE-37` gives an explicit Bernoulli-cube counterexample.

**OPEN / CONDITIONAL:** the predecessor's purely random-insertion score-tail hypothesis does not by itself imply the one-sided robust event needed by Warnke, nor does it automatically provide the predictable conditional MGF needed for a full exponential Doob route. That bridge is now isolated rather than guessed.

New valid package:

- `P19-DISCONNECTED-GOODSET-CE-37 — PROVED`;
- `P19-ROBUST-ANCHOR-TL-37 — PROVED`;
- `P19-WARNKE-ROBUST-LOO-37 — PROVED`;
- `P19-RARE-REPLACEMENT-DOOB-SPLIT-37 — PROVED`;
- `P19-ROBUST-RAW-RISK-37 — PROVED`;
- `P19-TWOLOG-NOT-UNIFORM-EDGE-CE-37 — PROVED`;
- `P19-AUDIT-P15-DELETION-PYTHAGORAS-37 — PASS`.

---

# 1. Mandatory continuity and repository evidence

Read before proof work from `master`:

- root `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`.

The protocol requires theorem-sized progress or a precise obstruction, exact source discipline, one concrete peer audit, cumulative `PROVED / CONDITIONAL / DISPROVED / OPEN` bookkeeping, immutable GitHub archival, and exact-commit readback. Two complete independent OTHER-worker end-to-end audits are required before P19 closure.

The observed pre-write `master` head before the first draft was

`043d61e9434c6fc59e00011f66767cd2c3b5e485`.

The first-draft target path was checked and returned `404 Not Found` before creation.

## 1.1 Latest complete P19 predecessor

Canonical predecessor:

`proofnet24/P19-kernel-spectral-pruning/runs/2026-09-16/2026-09-16_03-57-36__run-report-corrected.md`

- creation commit `86b42fa48aeb4d480b9ab22b861d63c6718a4d2a`;
- blob `15a5ad37254e8939c3a6f236e97910a2f565fac1`.

Retained new claims from that run:

- `P19-DELETION-GAP-LOCK-36`;
- `P19-PAIRWISE-MARGIN-FLIP-36`;
- `P19-SUBGAUSS-GAP-FLIP-36`;
- `P19-RAREBOUNDARY-CLIPPED-RMS-36`;
- `P19-RAREBOUNDARY-PREDVAR-36`;
- `P19-RAREJUMP-MGF-36`;
- `P19-MARGIN-SCALE-CE-36`;
- `P19-SMALLCOEFF-NOT-PATHWISELOSS-CE-36`.

## 1.2 Peer snapshot P15

Latest completed P15 report read:

`proofnet24/P15-kernel-mean-correction/runs/2026-09-16/2026-09-16_04-26-19__run-report.md`

- creation commit `73a3f2fadd6cc03060cee01671390a3736109e32`;
- blob `e0c5e33742258cfe5e12f812b27f10b6d698298d`.

Its `P15-DELETION-REFRESH-PYTHAGORAS-37` is independently audited in Section 13.

## 1.3 Peer snapshot P16

Latest completed P16 report read:

`proofnet24/P16-relu-contraction/runs/2026-09-16/2026-09-16_03-49-12__run-report.md`

- creation commit `38b261e451df857ddfa55a2f748caa3a49106a27`;
- blob `e0d63649eefc1713ef91acda196db2f965ef4d44`.

Its new package excludes pairwise-disjoint-support projective cycles in the tied ReLU model and gives an overlap-dependent external Gaussian orthant factor. No P16 theorem is imported into the P19 argument.

---

# 2. Exact July–August source boundary

The original July manuscript PDF and 19 August referee PDF still did not resolve as standalone accessible Library files this run. Fresh Library search again returned source-certified P19 direct-read reports rather than the original binaries. Therefore the exact recovered statements are retained and no unseen training, optimizer, feature-law, tail, or local-law assumption is guessed.

The July manuscript is

**Growing-rank spiked singular vectors and singular values, with applications to pruning deep neural networks.**

Historical attachment:

`Growing_rank_spiked_singular_vectors_and_singular_values__with_applications_to_pruning_deep_neural_networks.pdf`.

The source model is

```text
W_n = X_n + P_n,
P_n = U_n Theta_n V_n*.
```

Recovered hypotheses:

```text
X_n in R^(n x m),
n/m -> c in (0,1],
r_n=rank(P_n) -> infinity,
r_n=o(n),
spike strengths uniformly bounded,
and, when P_n is random, P_n is independent of X_n.
```

For a separated supercritical spike cluster `C_n`, the stable growing-rank vector objects are

```text
Pihat_L(C_n),
Pihat_R(C_n),
Fhat(C_n)=sum_(j in C_n) uhat_j vhat_j*.
```

With

```text
eta_(n,C)=[beta_n^(cc)+zeta_n]/Delta_n(C_n),
```

the recovered source statements are

```text
U_n* Pihat_L(C_n) U_n
 = diag(alpha_L(theta_(n,i)) 1_(i in C_n)) + O_op(eta_(n,C)),

V_n* Pihat_R(C_n) V_n
 = diag(alpha_R(theta_(n,i)) 1_(i in C_n)) + O_op(eta_(n,C)),

U_n* Fhat(C_n) V_n
 = diag(sqrt(alpha_L(theta_(n,i)) alpha_R(theta_(n,i))) 1_(i in C_n))
   + O_op(eta_(n,C)).
```

In the Marchenko–Pastur normalization,

```text
theta_c=c^(1/4),
rho(theta)^2=theta^2+(1+c)+c/theta^2,

1-alpha_L(theta)
 = c(theta^2+1)/[theta^2(theta^2+c)],

1-alpha_R(theta)
 = (theta^2+c)/[theta^2(theta^2+1)].
```

The source Frobenius-optimal retained singular value is

```text
eta*(rho(theta))
 = theta sqrt(alpha_L(theta)alpha_R(theta)).
```

The exact realized-activation pruning ledger is

```text
||Ea||^2
 = sum_j (sigma_j-eta_j)^2 |<vhat_j,a>|^2.
```

This is a pathwise realized-activation identity, not a theorem of population-risk improvement.

The source-certified 19 August referee state remains:

1. the resolvent-compression hypothesis contains the central random-matrix difficulty;
2. concrete verification is mainly Haar/Gaussian;
3. the connection with isotropic/anisotropic local laws should be stronger;
4. singular-vector theory and its additional obstacles should be explicit.

## 2.1 Fresh primary-source check

The primary arXiv abstract was reverified:

**Yitzchak Shmalo, _Mesoscopic Rectangular Spikes under Subspace Local Laws: Outlier Values and Singular Subspaces_, arXiv:2608.19594v1, 20 August 2026.**

The abstract says a subspace local law locates/counts outliers and, in holomorphic form, determines outlier singular subspaces; conclusions are stated with spectral projectors; the hypothesis is verified in four settings ranging from random signal orientations to independent entries with fixed deterministic directions; and MP constants are explicit.

Direct PDF fetch again failed in the current web runtime (`DisabledError`). Therefore exact v1 theorem numbering, rank windows, tail assumptions, error scales, and exact correspondence with the July contour hypotheses remain **PRIMARY THEOREM TEXT INACCESSIBLE / UNVERIFIED THIS RUN**.

A separate primary source was directly checked for the concentration argument below:

**Lutz Warnke, _On the method of typical bounded differences_, arXiv:1212.5796v1, Theorem 2.**

The directly read theorem states the one-sided typical Lipschitz condition and gives its exact compensation term and bad-event probability; Section 7 specializes it without altering its hypotheses.

---

# 3. Spectral/probabilistic layers remain separate

1. **Global ESD:** MP bulk/zero-atom statements concern eigenvalue distributions.
2. **Extreme/restricted singular values:** sparse restricted Gram floors/ceilings control identifiability on pruning-relevant supports.
3. **Singular-vector overlap:** the July `alpha_L,alpha_R` laws are compressed-resolvent/residue statements.
4. **Prediction risk:** the new theorem concerns leave-one-out fresh prediction of the actually trained/pruned learner.
5. **Finite-width confidence:** score gaps, uniform replacement radii, feature envelopes, clipping/tails, deletion drift, and confidence probabilities are separate debts.

Davis–Kahan/Wedin is used only after a valid operator perturbation and a genuine protected singular gap. It is not used to manufacture the BBP overlap constants.

---

# 4. Exact clipped LOO object

Let

```text
S=(Z_1,...,Z_n)
```

be iid observations. Let `f_{-i}` be the complete learner trained on `S_{-i}`; this can include response-trained features, optimization, deterministic hard top-`k` pruning, refitting, and kernel/readout stages.

For squared loss `L(f;z)=||f(x)-y||^2`, fix `T>0` and define

```text
ell_T(f;z)=min{L(f;z),T},
R_T(f)=E_Z ell_T(f;Z)
```

for a fresh independent `Z`.

Define

```text
H_T(S)
 = (1/n) sum_i [R_T(f_{-i})-ell_T(f_{-i};Z_i)].         (4.1)
```

Because `f_{-i}` is independent of its deleted observation `Z_i`,

```text
E H_T=0.                                                 (4.2)
```

Also

```text
H_T in [-T,T].                                           (4.3)
```

Thus for arbitrary neighboring samples,

```text
|H_T(S)-H_T(S')| <= 2T.                                 (4.4)
```

---

# 5. Falsification of the first-draft extension route

## `P19-DISCONNECTED-GOODSET-CE-37` — PROVED

The first immutable draft claimed that it suffices to know small coordinate changes whenever **both** endpoints belong to a high-probability good set, and then to extend from that set with unchanged coordinate Lipschitz constants. This is false.

Take `n` even and independent Bernoulli(1/2) coordinates

```text
X=(X_1,...,X_n) in {0,1}^n.
```

Let `K=sum_i X_i` and define

```text
Gamma
 = {K <= n/2-1} union {K >= n/2+1}.
```

The bad set is the middle Hamming layer `{K=n/2}`, whose probability

```text
q_n=P{K=n/2}
 = 2^(-n) binom(n,n/2)
 ~ sqrt[2/(pi n)] -> 0.                                 (5.1)
```

Define

```text
F(X)=+1   if K<=n/2-1,
F(X)= 0   if K=n/2,
F(X)=-1   if K>=n/2+1.                                  (5.2)
```

Symmetry gives `EF=0` and `F in [-1,1]`.

Now take two points of `Gamma` differing in one coordinate. They cannot cross from the lower component to the upper component without passing through the excluded middle layer. Hence any adjacent good-good pair lies in one component and

```text
|F(x)-F(x')|=0.                                         (5.3)
```

So the first draft's local good-good coordinate constants are all `c_j=0`, even though

```text
P{F=1}=(1-q_n)/2 -> 1/2.                                (5.4)
```

There is therefore no extension of `F|_Gamma` to the full cube having all coordinate differences zero, and no concentration inequality with zero good-set variance can follow from `(5.3)` alone.

This directly invalidates the first draft's McShane step. The defect is now preserved as a failed route rather than silently hidden.

---

# 6. Robust double-deletion anchor condition

The valid exponential route needs the **one-sided** condition appearing in Warnke's theorem: if the current sample is good, then changing one coordinate arbitrarily must still have the small typical effect.

Fix ordered `i != j`. Let

```text
D_ij=S_{-i,-j}
```

be the common double-deletion context. Let its trained readout be `C_ij^0`, deterministic top-`k` support `J_ij`, and score gap

```text
gamma_ij
 = s_(k)(C_ij^0)-s_(k+1)(C_ij^0).                      (6.1)
```

For an arbitrary possible insertion value `z`, write `C_ij(z)` for the complete one-insertion retraining from `D_ij`.

A **robust anchor certificate** consists of deterministic/data-dependent numbers `rho_ij,r_ij` and an anchor predictor `h_ij` measurable with respect to `D_ij`, such that

```text
sup_z ||C_ij(z)-C_ij^0||_F <= rho_ij,                   (6.2)

gamma_ij > 2 rho_ij,                                   (6.3)

sup_z sup_x ||f_ij(z;x)-h_ij(x)|| <= r_ij/(2n).         (6.4)
```

The supremum is over **all insertion values allowed by the observation domain**, not merely an iid random insertion.

By `P19-DELETION-GAP-LOCK-36`, `(6.2)`–`(6.3)` imply

```text
S_k(C_ij(z))=J_ij for every allowed insertion z.        (6.5)
```

Thus deterministic hard pruning is genuinely locked for every coordinate replacement; no mask randomness has been introduced.

A pruning-specific sufficient condition for `(6.4)` is the inherited proxy decomposition. On the locked support `J_ij`, choose a common proxy `psi_ij` and

```text
h_ij(x)=H_k(C_ij^0) psi_ij(x).
```

If uniformly over insertion values

```text
||C_ij(z)-C_ij^0||_F <= L_ij/(2n),
sup_x ||P_J psi_ij(x)|| <= R_ij,
sup_x ||H_k(C_ij(z))(phi_ij(z;x)-psi_ij(x))|| <= e_ij/(2n),
```

then

```text
sup_x ||f_ij(z;x)-h_ij(x)||
 <= [L_ij R_ij+e_ij]/(2n),                              (6.6)
```

so `r_ij=L_ij R_ij+e_ij` is legal.

These are explicit conditional obligations. The inaccessible source does not currently supply these uniform-in-insertion constants.

Let `Gamma` be the event that `(6.2)`–`(6.4)` hold for every ordered pair `i != j`, and put

```text
q=P(Gamma^c).                                            (6.7)
```

---

# 7. `P19-ROBUST-ANCHOR-TL-37` — PROVED

Assume `S in Gamma` and replace coordinate `j` by an **arbitrary** value, obtaining `S'`. No assumption on whether `S'` lies in `Gamma` is made.

For the `i=j` term of `H_T`, the deletion learner is unchanged and only the evaluation point changes, so

```text
|Delta_j term_(i=j)| <= T/n.                            (7.1)
```

For `i != j`, both deletion learners are one-insertion retrainings from the same double-deletion context `D_ij`. By `(6.4)`, each is within `r_ij/(2n)` of the same anchor predictor `h_ij`, hence

```text
sup_x ||f_{-i}(x)-f_{-i}^{(j)}(x)|| <= r_ij/n.           (7.2)
```

The clipped squared loss

```text
u -> min{||u-y||^2,T}
```

is globally `2 sqrt(T)`-Lipschitz in `u`. Therefore the population clipped risk and the fixed evaluation clipped loss each move by at most

```text
2 sqrt(T) r_ij/n.
```

After the outer `1/n` in `H_T`, the total neighboring change satisfies

```text
boxed:
|H_T(S)-H_T(S')|
 <= c_j
 := [T+4 sqrt(T) rbar_j]/n,                             (7.3)
```

where

```text
rbar_j=(1/n)sum_(i != j) r_ij.                          (7.4)
```

Crucially `(7.3)` holds whenever the **current** sample `S` lies in `Gamma`, for every arbitrary coordinate replacement. This is exactly the one-sided typical Lipschitz hypothesis required by Warnke's Theorem 2.

---

# 8. `P19-WARNKE-ROBUST-LOO-37` — PROVED

I directly checked the primary statement of Lutz Warnke, arXiv:1212.5796v1, Theorem 2. Specialized to the present notation, it says:

if independent coordinates generate `S`, a function `F` has typical coordinate bound `c_j` whenever the current sample lies in `Gamma`, global coordinate bound `d_j`, and compensation parameters `kappa_j in (0,1]`, then there is a bad event `B` satisfying

```text
P(B) <= P(Gamma^c) sum_j kappa_j^(-1),                  (8.1)

not B subset Gamma,                                     (8.2)
```

and, with

```text
e_j=kappa_j(d_j-c_j),                                   (8.3)
```

```text
P{F >= EF+t and not B}
 <= exp[-t^2/(2 sum_j(c_j+e_j)^2)].                     (8.4)
```

For `F=H_T`, `(4.2)` gives `EF=0`, `(4.4)` gives the global bound

```text
d_j=2T,
```

and Section 7 gives the typical bound `c_j`.

Therefore, for arbitrary `kappa_j in (0,1]`,

```text
boxed:
P{H_T >= t}
 <= q sum_j kappa_j^(-1)
    + exp[-t^2/(2 sum_j(c_j+kappa_j(2T-c_j))^2)].       (8.5)
```

This is a genuine exponential-confidence theorem for the actual deterministic hard-pruned learner, under the explicit robust-anchor event.

## 8.1 Uniform simple form

If

```text
A_j:=T+4sqrt(T)rbar_j <= A
```

for all `j`, so `c_j<=A/n`, choose

```text
kappa_j=1/n.
```

Then

```text
c_j+kappa_j(2T-c_j)
 <= (A+2T)/n,
```

hence

```text
sum_j(c_j+e_j)^2 <= (A+2T)^2/n.                         (8.6)
```

Also

```text
P(B) <= n^2 q.                                          (8.7)
```

For every `delta in (0,1)`, setting the exponential term to `delta` gives

```text
boxed:
H_T
 <= (A+2T) sqrt[2 log(1/delta)/n]                       (8.8)
```

with probability at least

```text
boxed:
1-delta-n^2 q.                                          (8.9)
```

Thus if an independent source argument proves a robust-anchor failure probability

```text
q <= e^(-u)/n^3,
```

then `(8.8)` holds with probability at least

```text
1-delta-e^(-u)/n.                                       (8.10)
```

No iid pruning mask is used anywhere in this specialization.

## 8.2 What the predecessor's random-insertion tail does *not* prove

The preceding `P19-SUBGAUSS-GAP-FLIP-36` controls a **random** one-insertion support flip:

```text
P{support flip | deletion anchor}
 <= 2 exp[-gamma^2/(8 sigma^2)].                        (8.11)
```

Equation `(8.11)` does **not** imply the uniform-in-insertion supremum `(6.2)`, and therefore does not by itself establish the one-sided typical Lipschitz event `Gamma` required in `(8.5)`.

This distinction is now explicit. The first draft incorrectly tried to bypass it with a two-sided good-good extension; Section 5 proves why that shortcut fails.

---

# 9. `P19-RARE-REPLACEMENT-DOOB-SPLIT-37` — PROVED

There is nevertheless a rigorous route that uses truly probabilistic replacement tails without any extension theorem. It gives a weaker confidence treatment for the rare component but precisely identifies the missing exponential-MGF debt.

Let `F(S)` be integrable and let `S^(j)` replace `Z_j` by an independent copy `Z_j'`. Define

```text
X_j=F(S)-F(S^(j)),
F_j=sigma(Z_1,...,Z_j),
D_j=E[F|F_j]-E[F|F_(j-1)].
```

On the enlarged space containing `Z_j'`, exchangeability gives the exact identities

```text
D_j=E[X_j|F_j],                                         (9.1)
E[X_j|F_(j-1)]=0.                                       (9.2)
```

Assume deterministic `a_j,B_j,p_j` satisfy

```text
|X_j|<=B_j,                                             (9.3)
P{|X_j|>a_j | F_(j-1)}<=p_j   a.s.                     (9.4)
```

Split

```text
Y_j=X_j 1_(|X_j|<=a_j),
R_j=X_j-Y_j,
```

and

```text
U_j=E[Y_j|F_j]-E[Y_j|F_(j-1)],
V_j=E[R_j|F_j]-E[R_j|F_(j-1)].
```

Then `D_j=U_j+V_j`, each `U_j` is a martingale difference with

```text
|U_j|<=2a_j,                                            (9.5)
```

and

```text
E|V_j|
 <= 2 E|R_j|
 <= 2 B_j p_j.                                          (9.6)
```

Azuma on `sum U_j` and Markov on `sum |V_j|` yield, for any `delta_1,delta_2 in (0,1)`,

```text
boxed:
F-EF
 <= sqrt[8 log(1/delta_1) sum_j a_j^2]
    + (2/delta_2) sum_j B_j p_j                         (9.7)
```

with probability at least

```text
1-delta_1-delta_2.                                      (9.8)
```

This theorem is elementary and self-contained. It uses no metric extension and no support-independence assumption.

For `F=H_T`, `B_j=2T` always. If a **predictable exposure-scale** argument can certify

```text
P{|Delta_j H_T|>A_j/n | F_(j-1)}<=p_j,                 (9.9)
```

then

```text
H_T
 <= sqrt[8 log(1/delta_1) sum_j A_j^2/n^2]
    + (4T/delta_2)sum_j p_j.                            (9.10)
```

The source-facing remaining problem is exactly the conversion from double-deletion score-margin tails to the predictable conditional tail `(9.9)`. Future unrevealed deletion contexts make that conversion nontrivial; it is not assumed for free.

The predecessor's `P19-RAREJUMP-MGF-36` is still the correct tool if one can prove a predictable conditional MGF or a sufficiently strong conditional rare-jump statement. This run does not falsely promote marginal insertion tails to that stronger hypothesis.

---

# 10. `P19-ROBUST-RAW-RISK-37` — PROVED

The robust Warnke theorem controls clipped LOO risk. Raw deployed risk follows with the same explicit tail/deletion debts as in preceding P19 runs.

For each deletion learner put

```text
L_i(Z)=||f_{-i}(X)-Y||^2,

tau_(i,T)
 = E[(L_i(Z)-T)_+ | S_{-i}],

tau_T=(1/n)sum_i tau_(i,T).                             (10.1)
```

Then pathwise

```text
Rbar_loo^raw
 <= Rbar_loo,T + tau_T.                                 (10.2)
```

Since empirical clipped loss is at most empirical raw loss, whenever `(8.8)` holds,

```text
Rbar_loo^raw
 <= Rhat_loo^raw
    +(A+2T)sqrt[2log(1/delta)/n]
    +tau_T.                                             (10.3)
```

Let

```text
D_i=||f_S-f_{-i}||_(L2(P_X)),
Dbar=(1/n)sum_i D_i.                                    (10.4)
```

Minkowski followed by concavity of the square root gives

```text
sqrt[R(f_S)]
 <= Dbar+sqrt[Rbar_loo^raw].                            (10.5)
```

Hence, on the same event,

```text
boxed:
sqrt[R(f_S)]
 <= Dbar
    +sqrt{
       Rhat_loo^raw
       +(A+2T)sqrt[2log(1/delta)/n]
       +tau_T
     }.                                                 (10.6)
```

The probability is at least `1-delta-n^2q` under the robust-anchor theorem.

This is a population-risk **certificate**, not a theorem that pruning improves risk. Improvement still needs a paired dense/pruned audit or another valid comparative argument.

---

# 11. `P19-TWOLOG-NOT-UNIFORM-EDGE-CE-37` — PROVED

Another shortcut is false:

> `Theta(n^2)` deletion/replacement edges each fail with probability `O(n^-2)`, therefore all edges are good with probability tending to one.

Take `N=n(n-1)` independent Bernoulli edge indicators with failure probability `p=n^-2`. Then every edge has the desired marginal scale, but

```text
P{at least one failure}
 =1-(1-n^-2)^(n(n-1))
 ->1-e^(-1).                                            (11.1)
```

Exact numerical evaluations:

```text
n=10:    0.5952680273
n=100:   0.6284417028
n=1000:  0.6317526793
n=10000: 0.6320837727.
```

Thus the predecessor's `2 log n` gap exponent can be enough for a single-edge `n^-2` flip scale and predictable-variance/RMS calculations, but marginal tails alone cannot turn it into a simultaneous all-edge certificate. Stronger dependence information, a stronger exponent, or a nonuniform martingale argument is required.

---

# 12. Singular-vector / MP-null composition

The risk theorem remains distinct from singular-vector stability.

For two legally aligned `k`-sparse readouts `C_1,C_2` using a common proxy feature `psi`, let `J` be the support union and

```text
G=E[psi psi*].
```

If an honest certificate gives

```text
E||(C_1-C_2)psi||^2 <= Rbar_Delta                       (12.1)
```

and

```text
G_JJ >= aI,
a>0,                                                       (12.2)
```

then

```text
Rbar_Delta
 >= a||C_1-C_2||_F^2
 >= a||C_1-C_2||_op^2,
```

so

```text
boxed:
||C_1-C_2||_op <= sqrt(Rbar_Delta/a).                   (12.3)
```

Only if `(12.3)` is at most half a genuine protected singular-cluster gap `Delta_K` do we invoke Wedin/Hermitian dilation, yielding the inherited scale

```text
boxed:
||Delta Pihat_K^L||_op,
||Delta Pihat_K^R||_op,
||Delta Fhat_K||_op
 <= (4/Delta_K)sqrt(Rbar_Delta/a).                      (12.4)
```

The July BBP overlap factors remain compressed-resolvent quantities; `(12.4)` is not a substitute for them.

Under an honest simultaneous Gaussian sparse-RIP null, the restricted floor `a` can remain positive for all support unions of size at most `2k` even when `r/n>1` and the **global** Gram has an MP zero atom. This keeps global ESD, restricted extreme singular values, singular-vector overlap, prediction risk, and finite-width confidence as separate layers.

A simultaneous support-uniform event can legally cover a support chosen from the same realized matrix. An iid Bernoulli mask theorem cannot be imported merely because the final sparsity rate matches.

---

# 13. Independent peer audit

## `P19-AUDIT-P15-DELETION-PYTHAGORAS-37` — PASS

Audited claim:

`P15-DELETION-REFRESH-PYTHAGORAS-37`

Source:

`proofnet24/P15-kernel-mean-correction/runs/2026-09-16/2026-09-16_04-26-19__run-report.md`

- creation commit `73a3f2fadd6cc03060cee01671390a3736109e32`;
- blob `e0c5e33742258cfe5e12f812b27f10b6d698298d`.

P15 defines, for an iid sample with deletion block `R`, retained data `S_T`, arbitrary square-integrable Hilbert-valued full learner `F_n`, reduced learner `F_(n-r)`, and fresh replacement block `Z'_R`,

```text
D_R^ref
 =E||F_n(S)-F_n(S^<R>)||^2,

Delta_R^del
 =E||F_n(S)-F_(n-r)(S_T)||^2,

mu_T=E[F_n(S)|S_T],

B_R^size
 =E||mu_T-F_(n-r)(S_T)||^2.
```

The claim is

```text
Delta_R^del
 =(1/2)D_R^ref+B_R^size.                                (13.1)
```

### Independent proof

Condition on `S_T` and set

```text
X=F_n(S_T,Z_R),
X'=F_n(S_T,Z'_R),
Y=F_(n-r)(S_T),
mu=E[X|S_T].
```

Conditional on `S_T`, `X,X'` are iid Hilbert-valued variables with common mean `mu`, while `Y` is fixed. Thus

```text
E[||X-X'||^2|S_T]
 =2E[||X-mu||^2|S_T].                                   (13.2)
```

Orthogonality of `X-mu` to every `S_T`-measurable vector gives

```text
E[||X-Y||^2|S_T]
 =E[||X-mu||^2|S_T]+||mu-Y||^2.                         (13.3)
```

Average `(13.2)`–`(13.3)` to obtain `(13.1)`. Square-integrability is sufficient; no convexity or differentiability is used.

### Exact finite check

Take independent uniform `B in {0,1}` and `Z,Z' in {-1,1}` with

```text
X=(B+Z,2B-Z),
Y=(2B,-B).
```

Exact enumeration gives

```text
D_ref=4,
Delta_del=7,
B_size=5,
Delta_del-(1/2)D_ref-B_size=0.
```

**Verdict: PASS.** This is a component audit, not one of the two complete OTHER-worker end-to-end P19 audits required for closure.

---

# 14. Method comparison and dependence audit

## Resolvent / subspace local law

Correct for the source's outlier values/projectors and BBP overlap. The Aug. 20 primary abstract confirms the revised paper is organized around a subspace local law. Exact v1 theorem hypotheses remain inaccessible in this runtime.

## Davis–Kahan / Wedin

Second stage only after a valid operator perturbation and protected gap. It does not generate source overlap constants.

## Leave-one-out / replace-one

Central here. LOO gives `EH_T=0`. Double deletion provides the common anchor needed to compare neighboring one-insertion learners. The corrected theorem carefully distinguishes uniform-in-insertion stability from merely random-insertion tail control.

## Typical bounded differences

Warnke's directly checked primary Theorem 2 is legal only under its **one-sided** typical Lipschitz hypothesis. The first draft's attempt to replace that by a disconnected two-sided good-good condition without paying the theorem's extra machinery is rejected by Section 5.

## Free probability / deterministic equivalents

Potentially useful for global spectral laws and score/feature nulls, but they do not remove trained-support dependence or prove a uniform replacement envelope. No free-probability shortcut is asserted.

## Sparse concentration / RIP

Uniform sparse-RIP can cover same-matrix selected supports. Independent-mask concentration cannot be substituted for deterministic top-`k` selected after training.

---

# 15. Failed-route graveyard, preserved and updated

The following remain rejected:

1. MP ESD implies singular-vector isotropy — **DISPROVED**.
2. Low rank plus MP fit implies independent-spike overlap — **DISPROVED**.
3. Same-sample learned spike frame may be treated as independent — **DISPROVED without a stability bridge**.
4. Deterministic same-matrix pruning may be replaced by iid masking from sparsity fraction/marginals — **DISPROVED**.
5. Hard top-`k` is continuous at a nontrivial score tie — **DISPROVED**.
6. Prediction agreement identifies coefficients/vectors without a restricted Gram floor — **DISPROVED**.
7. Pre-pruning replacement stability implies post-hard-pruning stability — **DISPROVED**.
8. Reused training/audit sample may be treated as untouched audit data — **DISPROVED**.
9. Clipped covariance upper-bounds unbounded raw risk without tail control — **DISPROVED**.
10. Small fresh full-sample RMS replacement plus low reused training error implies low population risk — **DISPROVED**.
11. `L2` replacement control may be relabeled as `psi_1` control — **DISPROVED**.
12. Predictable variance alone implies sub-Gaussian self-normalization — **DISPROVED**.
13. Raw ghost sample variance may be plugged in without a UCB — **DISPROVED**.
14. Frozen-mask ghost calibration estimates adaptive hard-pruning influence — **DISPROVED**.
15. Small coefficient drift without score margin controls hard top-`k` — **DISPROVED**.
16. Margin plus small coefficient drift without a feature/output envelope controls pathwise loss — **DISPROVED**.
17. Per-edge `O(n^-2)` failure automatically implies all `Theta(n^2)` edges are good w.h.p. — **DISPROVED**.
18. **New:** good-good local coordinate bounds on an arbitrary disconnected high-probability set imply an unchanged-constant McShane/McDiarmid extension — **DISPROVED by `P19-DISCONNECTED-GOODSET-CE-37`**.
19. Wedin alone gives BBP overlap constants — **FALSE**.
20. Singular-vector stability automatically implies population-risk improvement — **FALSE**.

---

# 16. Updated dependency ledger

## PROVED — inherited and retained

- exact July growing-rank source model/statements from the direct-read chain;
- exact source-certified 19 August referee state;
- repaired Haar contour compression and cluster-projector/mixed-dyad theorem under compression;
- MP ESD/vector-isotropy separation and same-sample adaptive-frame counterexamples;
- independent proxy-frame and fixed-separated iid-frame compression results;
- Gaussian/Haar edge calibration and separated-contour method barrier;
- deterministic/smooth structured-pruning stability bridges;
- exact hard top-`k` boundary-operator and mixed-dyad transfers;
- deterministic restricted-Gram / trained-RIP / weak-submodularity bridges;
- fresh-audit and same-observation stability certificates;
- clipped reused lower-RE and unbounded-risk tail separation;
- covariance-weighted hard-boundary prediction/operator certificates;
- LOO RMS raw-risk certificate;
- conditional Bernstein / `psi_1` influence theorem;
- predictable self-normalized and ghost-variance certificates;
- deletion-anchor score-gap lock and pairwise/sub-Gaussian flip bounds;
- rare-boundary clipped RMS/predictable variance theorem;
- rare-jump conditional MGF theorem;
- margin-scale and small-coefficient/huge-feature counterexamples.

## PROVED — valid new claims this run

### `P19-DISCONNECTED-GOODSET-CE-37`

Two-sided good-good local Lipschitz bounds on a disconnected good set do not justify an unchanged-coordinate McShane extension.

### `P19-ROBUST-ANCHOR-TL-37`

Uniform-in-insertion double-deletion anchor lock plus a pathwise prediction envelope gives the exact one-sided typical Lipschitz constants

```text
c_j=[T+4sqrt(T)rbar_j]/n.
```

### `P19-WARNKE-ROBUST-LOO-37`

Direct specialization of Warnke Theorem 2 yields `(8.5)` and uniform form `(8.8)`–`(8.9)` for the actually trained/pruned learner.

### `P19-RARE-REPLACEMENT-DOOB-SPLIT-37`

Predictable rare replacement tails yield the exact concentration/contamination decomposition `(9.7)` without any metric extension.

### `P19-ROBUST-RAW-RISK-37`

The robust clipped LOO theorem plus raw-loss tail remainder and full/deletion drift gives `(10.6)`.

### `P19-TWOLOG-NOT-UNIFORM-EDGE-CE-37`

Marginal `n^-2` edge failure does not imply simultaneous goodness over `Theta(n^2)` edges.

### `P19-AUDIT-P15-DELETION-PYTHAGORAS-37`

P15's deletion/refresh Hilbert-space identity independently passes.

## RETRACTED / DISPROVED AS STATED

`P19-TYPICAL-BOUNDED-DIFF-37` from the first immutable same-run draft is **RETRACTED**. The claimed McShane step did not follow from the stated two-sided local hypothesis; Section 5 gives an exact counterexample to the route.

The dependent first-draft claims `P19-RAREBOUNDARY-LOO-TYPICAL-37`, `P19-RAREBOUNDARY-EXP-CONF-37`, and the first-draft form of `P19-RAREBOUNDARY-RAW-RISK-37` are also superseded. Their corrected replacements are the robust-anchor and Doob-split theorems above.

## CONDITIONAL

- source double-deletion/replacement checkpoints or equivalent retraining oracle;
- a legal **uniform-in-insertion** replacement radius `rho_ij` if the Warnke robust theorem is to be used;
- or, alternatively, predictable conditional replacement tails/MGFs at the LOO exposure scale if the random-tail route is to be used;
- source score gaps `gamma_ij` and any theorem controlling their lower tail;
- pathwise proxy/feature/output envelope `r_ij`;
- legal representation alignment and representation debt;
- raw-loss tail remainder `tau_T`;
- full-data versus deletion prediction drift `Dbar`;
- positive restricted Gram floor on the actual support union;
- genuine protected deployed singular gap before Wedin/Davis–Kahan;
- exact theorem-level hypotheses/rank windows of arXiv:2608.19594v1 until the primary theorem text is readable.

## OPEN

1. `P19-PREDICTABLE-MARGIN-MGF-38`: convert double-deletion random-insertion gap/tail information into the **predictable filtration-scale** conditional tail/MGF needed for a full exponential Doob route, or prove an obstruction.
2. `P19-ROBUST-MARGIN-AUDIT-38`: if source retraining is accessible, determine whether a uniform-in-insertion replacement radius is realistic or vacuous for the actual pipeline.
3. `P19-ARXIV-V1-EXACT-AUDIT-38`: directly read the v1 theorem text and reconcile its exact subspace-local-law hypotheses, rank regimes, holomorphic assumptions, and constants with the July direct-read statements.
4. Source-specific measurement/proof of restricted Gram edges and deployed singular gaps.
5. Non-Haar/fixed-deterministic-frame local laws not already resolved by the inaccessible v1 theorem text.
6. Critical `n^-1/3` BBP coupling remains logically separate.
7. Two complete independent OTHER-worker end-to-end P19 audits remain required before closure.

---

# 17. Strongest next attack

The sharpest next theorem is

`P19-PREDICTABLE-MARGIN-MGF-38`.

The predecessor supplied random-insertion support-flip tails from score margins. This run proves exactly why those tails cannot simply be converted into a disconnected good-set McDiarmid argument, and it supplies two valid endpoints:

- a robust one-sided Warnke theorem if uniform-in-insertion stability is available;
- a predictable rare-replacement Doob theorem if filtration-scale tails are available.

The remaining mathematical question is to bridge the source's plausible double-deletion random-insertion geometry to one of these valid hypotheses without paying a vacuous worst-case replacement bound. A promising route is an exchangeable-pairs or conditional Efron–Stein MGF that conditions on the double-deletion context rather than the sequential exposure filtration, while preserving the actual adaptive hard-pruning map.

If actual checkpoints/features become accessible, the practical parallel target is to compute score gaps, insertion drift tails, support-flip frequencies, feature/proxy envelopes, raw-loss tails, restricted Gram floors, and protected singular gaps rather than continuing abstract calibration.

---

# 18. Delivery checklist

- Corrected canonical UTF-8 report: this file.
- First immutable draft retained and explicitly superseded; no history overwritten.
- Root README/protocol read.
- Latest complete P19 predecessor read.
- Two completed peers read: P15 and P16.
- One peer lemma independently audited with path, creation SHA, blob SHA, claim ID, proof, and exact finite check.
- Primary Aug. 20 arXiv abstract reverified; inaccessible theorem text marked rather than guessed.
- Primary Warnke theorem directly checked before use.
- Eigenvalue distribution, restricted extremes, vector overlap, prediction risk, and finite-width confidence kept separate.
- Same-trained-matrix hard pruning never replaced by iid masking.
- Ledger contains PROVED / CONDITIONAL / DISPROVED / OPEN plus the explicit same-run retraction.
- Exact-commit readback is required immediately after creation.

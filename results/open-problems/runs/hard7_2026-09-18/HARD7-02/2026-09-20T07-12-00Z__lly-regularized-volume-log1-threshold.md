Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **MOVEMENT: source/literature baseline `p_comb <= 2`; this run gives a self-contained in-track proof of `p_comb <= 1`, with source Conjecture 3.9 still OPEN and independent validation still required. Methods B5/B11/B28.**

# HARD7-02 — regularized hybrid volumes lower the row-combinatorial circular-law logarithmic exponent from 2 to 1

Status: **PARTIAL / SOURCE CONJECTURE OPEN / NEW THEOREM PENDING INDEPENDENT VALIDATION.** No source-level closure, no peer audit, and no public-priority claim is asserted.

## 1. Continuity, ownership, and evidence consumed

This run resumes the admitted Li--Litvak--Yu target; it does not restart HARD7-02 and does not return to the released Han target.

Controlling repository material read before the mathematics:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- current claim `operations/claims/LI-LITVAK-YU-2026-SPARSE-COMBINATORIAL-CIRCULAR-LAW.md`;
- newest own checkpoint `runs/hard7_2026-09-18/HARD7-02/2026-09-20T06-12-23Z__han-terminal-handoff-lly-combinatorial-admission.md`;
- neighboring circular-law ownership records, including the distinct heavy-tailed C0031/C0032 tracks.  C0032 has a terminal handoff in `research7_2026-09-17/R7-06/handoffs/2026-09-19T095800Z__C0032_terminal_handoff.md`; it concerns explicit heavy-tailed limiting densities and does not overlap this independent-row fixed-row-sum sparse model.

No peer claim was overwritten. No shared root ledger was edited. No scheduler, email, Drive, workflow, permission, public-posting, or cadence action was taken.

### Source correction recovered this run

The active arXiv version is **v2, 11 August 2026**, not merely the April v1 metadata used at admission.  The current title is

> Dongbin Li, Alexander E. Litvak, Tingzhou Yu, *Least singular values of shifted sparse random combinatorial matrices*, arXiv:2604.10446v2.

The circular-law parent is now stated explicitly as **Conjecture 3.9** in v2.  In the sparse half `d<=n/2`, with `M_n` uniform over `{0,1}` matrices having exactly `d` ones in each row and

`\bar M_n = M_n / sqrt(d(1-d/n))`,

Conjecture 3.9 asks whether the ESD of `\bar M_n` converges in probability to the circular law whenever only `d(n)->infinity`.

The current proved v2 baseline is Corollary 1.4:

`d >= (log n)^(2+eps)`, `d=o(n)`  => circular law in probability.

The same v2 paper proves quantitative shifted least-singular-value bounds already at `d >= C log n` (Theorem 1.1), with the iid Bernoulli analogue in Theorem 3.1 and the common explicit scale `alpha(n,d)` in Remark 1.3 / Remark 3.2.  Section 3 identifies the `log^(2+eps)` loss inside the determinant replacement step.

Fresh 20 September 2026 searches for the exact arXiv identifier/title, the old v1 circular-law title, `random combinatorial matrix circular law`, later Li/Litvak/Yu papers, and logarithmic sparsity improvements found v2, the April 2026 signed-combinatorial least-singular-value paper, and the dense least-singular-value upper-bound paper, but no located theorem lowering Corollary 1.4 below the stated `log^(2+eps)` condition for this exact model.  This is a bounded current-status search, not a worldwide novelty certificate.

## 2. Frozen metric and source-level before/after

The admitted metric remains

`p_comb = inf { p>=0 : for every eps>0, the circular law is rigorously established in the frozen model whenever d >= (log n)^(p+eps) and d=o(n) }`.

Before this run, the source/literature certificate was

`p_comb <= 2`.

The theorem proved below yields, at the level of this track's written proof,

`p_comb <= 1`.

This is a strict source-relevant improvement, but it is **not** the full Conjecture 3.9.  In particular, `p_comb=0` would itself still be weaker than arbitrary `d->infinity`, and this run does not even reach `p_comb=0`.  Because the repository closure standard requires genuinely independent validation, the status remains PARTIAL and the new `<=1` bound is explicitly marked **pending independent validation**.

## 3. The idea, written before the checker

The source proof of Theorem 3.8 replaces the first `m` rows one at a time and compares ordinary distances to a hybrid row span.  Corollary 3.5 gives, conditionally on that span,

`P(|r-E(p)|>=t) <= C sqrt(d) exp(-c t^2)`.

The source chooses `t=d^(1/4)` and requires **all** `m~n` replacements to be simultaneously good.  This costs

`n sqrt(d) exp(-c sqrt(d))`,

which is exactly where a `d` of order larger than `(log n)^2` enters the determinant comparison.  The least-singular-value input itself is already available down to `C log n`.

The new route is:

1. **B5 (add a parameter):** replace ordinary row-volume by the ridge-regularized volume
   `Phi_eta(H)=1/2 log det(HH^*+eta^2 I)`.  This removes the `log 0` catastrophe on bad hybrid matrices.
2. **B11 (dualize):** a one-row replacement becomes a Schur-complement / resolvent quadratic form with a positive contraction
   `Q_eta = I-B^*(BB^*+eta^2 I)^(-1)B`.  Its trace automatically remembers the row codimension.
3. **B28 (replace for-all by typical):** instead of union-bounding over all `n` row replacements, integrate the conditional concentration tail and control the **average absolute log increment in L1**.  The `sqrt(d)` conditioning penalty then costs only `sqrt(log d)` in expectation, not a factor forcing `sqrt(d)>>log n`.

The ridge parameter is removed **only at the two endpoint prefix matrices**, using the source's existing shifted least-singular-value theorem.  Thus no invertibility of the intermediate hybrid matrices is required.

## 4. Main partial theorem

### Theorem 4.1 (logarithmic exponent one)

Fix `eps>0`.  Suppose `d=d(n)` satisfies

`(log n)^(1+eps) <= d <= n/2`,  `d=o(n)`.

Let `M_n` have independent rows, each uniformly distributed over the `{0,1}` vectors with exactly `d` ones.  Then

`ESD( M_n / sqrt(d(1-d/n)) ) -> mu_circ`

in probability.

Consequently, in the frozen metric,

`p_comb <= 1`.

It suffices to prove the theorem for `0<eps<=1`; larger `eps` follows from the `eps=1` case.

The proof occupies Sections 5--11.

## 5. B11: exact ridge Schur factorization

Let `B` be an `(m-1) x n` complex matrix, let `a` be one additional row, and put `H=[B;a]`.  For `eta>0`, define

`Q = I_n - B^*(BB^*+eta^2 I_(m-1))^(-1)B`.

Then block Gaussian elimination gives the exact identity

`det(HH^*+eta^2 I_m)`
` = det(BB^*+eta^2 I_(m-1)) * (eta^2 + a Q a^*)`.   (5.1)

Indeed, this is the Schur complement of the upper-left block `BB^*+eta^2 I`.

By singular-value decomposition (equivalently the ridge resolvent identity),

`Q = eta^2 (B^*B+eta^2 I_n)^(-1)`.   (5.2)

Therefore

`0 <= Q <= I`,

and `Q` is exactly the identity on `ker B`.  Since `rank(B)<=m-1`,

`tr Q >= dim ker B >= n-m+1`.   (5.3)

The point of (5.3) is that it survives **every hybrid realization**, including rank-deficient ones.

The exact finite algebra in (5.1)--(5.3), in the smallest nontrivial symbolic case, was checked by

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T07-12-00Z__lly_regularized_replacement_check.py`

(commit `b8f9ae81b03537589a99b22443ff61d3fc1b4945`), with archived output

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T07-12-00Z__lly_regularized_replacement_check.out`

(commit `4026cc4842873efcbc442361a1127f01875b4768`), ending `ALL_EXACT_CHECKS_PASS = True`.  This is a self-check only, not an independent theorem audit.

## 6. B5+B11: concentration for a ridge distance

The source's Theorem 3.4 is stated for an orthogonal projection.  The ridge factor needs the following contraction version.

### Lemma 6.1 (positive-contraction Bernoulli ridge distance)

Let `0<p<=1/2`, let `xi=(xi_1,...,xi_n)` have iid Bernoulli(`p`) coordinates, let `0<=Q<=I` be deterministic Hermitian, let `u in C^n`, and let `eta>0`.  Put

`rho(xi) = [ eta^2 + (xi+u)^* Q (xi+u) ]^(1/2)`.

Write `x=xi-p 1`, `v=u+p 1`, `sigma^2=p(1-p)`, and

`D^2 = eta^2 + sigma^2 tr Q + v^*Qv = E rho^2`.

If `D>=1`, then for universal constants `c,C>0`,

`D/sqrt(6) <= mu := E rho <= D`,   (6.1)

and for every `t>0`,

`P(|rho-mu|>=t) <= C exp(-c t^2)`.   (6.2)

#### Proof

The upper bound in (6.1) is Jensen.  For the lower bound, set `Y=rho^2`.  Expanding `Y-EY` gives a diagonal quadratic term, an off-diagonal quadratic term, and `2 Re <x,Qv>`.  Exactly as in the source proof of Theorem 3.4, independence and centering give

`E |sum_i q_ii (x_i^2-sigma^2)|^2`
` = sigma^2(1-2p)^2 sum_i |q_ii|^2`,

`E |sum_{i!=j} q_ij x_i x_j|^2`
` <= 2 sigma^4 sum_{i!=j}|q_ij|^2`,

and

`E |<x,Qv>|^2 = sigma^2 ||Qv||^2`.

Using `(A+B+C)^2 <= 3(A^2+B^2+C^2)`, `tr(Q^2)<=tr Q`, `Q^2<=Q`, and `sigma^2<=1/4`, we obtain the safe bound

`Var(Y) <= 5 [sigma^2 tr Q + v^*Qv] <= 5D^2`.   (6.3)

Hence

`E rho^4 <= D^4+5D^2 = D^2(D^2+5)`.

Holder in the same form used in the source gives

`D^2=E rho^2 <= (E rho)^(2/3) (E rho^4)^(1/3)`,

so

`E rho >= D^2/sqrt(D^2+5) >= D/sqrt(6)`

when `D>=1`.

Finally `rho` is a convex 1-Lipschitz function of the real Bernoulli vector: it is the norm of the affine map

`xi -> (eta, Q^(1/2)(xi+u))`

and `||Q^(1/2)||<=1`.  The same Talagrand convex-Lipschitz inequality used in source Theorem 3.4 yields (6.2).  ∎

### Corollary 6.2 (fixed-row-sum conditioning)

Let `R` be uniform over `{0,1}^n` with exactly `d` ones, `p=d/n<=1/2`, and define `rho(R)` using the same deterministic `Q,u,eta`.  Let `mu` be the iid Bernoulli mean from Lemma 6.1.  Then

`P(|rho(R)-mu|>=t) <= C sqrt(d) exp(-c t^2)`.   (6.4)

#### Proof

`R` is an iid Bernoulli(`p`) vector conditioned on `sum xi_i=d`.  Stirling gives, exactly as in source Corollary 3.5,

`P(sum xi_i=d) >= c/sqrt(d)`

for `d<=n/2`.  Divide (6.2) by this conditioning probability.  ∎

## 7. B28: integrate the log error instead of union-bounding rows

The regularization ensures `rho>=eta`, so logarithms are integrable even on the bad event.

### Lemma 7.1 (conditional logarithmic comparison)

Assume the setting of Lemma 6.1 / Corollary 6.2.  Suppose additionally

`tr Q >= r`,

and suppose both the iid and fixed-sum versions satisfy the deterministic upper bound `rho<=R_*`.  Then, once `p(1-p)r>=1`, with `L=log(R_*/eta)`,

`E_fixed |log rho-log mu| + E_iid |log rho-log mu|`

` <= C sqrt(log(e d)/(p(1-p)r))`
`    + C L sqrt(d) exp(-c p(1-p)r)`.   (7.1)

#### Proof

By Lemma 6.1,

`mu >= D/sqrt(6) >= c sqrt(p(1-p)r)`.   (7.2)

On the good event `|rho-mu|<=mu/2`, the mean-value theorem gives

`|log rho-log mu| <= 2|rho-mu|/mu`.   (7.3)

For the fixed-sum row, integrate (6.4):

`E[ |rho-mu| 1_{|rho-mu|<=mu/2} ]`
` <= integral_0^(mu/2) min(1, C sqrt(d)e^{-c t^2}) dt`
` <= C sqrt(log(e d))`.   (7.4)

For the iid row the corresponding integral is `O(1)`, hence is dominated by the same bound.

On the complement of the good event, both `rho` and `mu` lie in `[eta,R_*]`, so

`|log rho-log mu| <= L`.

By (6.2)/(6.4) and (7.2), that bad event has probability at most

`C sqrt(d) exp(-c p(1-p)r)`

for the fixed-sum row and less for the iid row.  Combining with (7.3)--(7.4) proves (7.1).  ∎

For the shifted rows used in the circular-law proof and fixed `z`, we may take deterministically

`R_* <= eta + sqrt(n) + |z|sqrt(d) <= C_z sqrt(n)`,   (7.5)

because `0<=Q<=I`.  Thus if `eta` is only polynomially small, `L=O(log n)`.

## 8. The new head/tail split

Fix `0<eps<=1` and define

`a = (2+eps)/(2(1+eps))`,
`delta = d^(-a)`,
`m = ceil(n(1-delta))`.   (8.1)

Then

`1-a = eps/(2(1+eps))`,
`(1+eps)a = 1+eps/2`.   (8.2)

These identities were also checked exactly by the archived self-check.

Consequently

`d delta = d^(1-a)`,   (8.3)

and under `d >= (log n)^(1+eps)`,

`d delta >= (log n)^(eps/2) -> infinity`,   (8.4)

while

`delta log n <= (log n)^(-eps/2) -> 0`.   (8.5)

The first relation makes the averaged ridge head comparison work; the second kills the determinant tail.

## 9. Polynomial endpoint least-singular scale already supplied by the source

We need a deterministic polynomial scale only at the two **endpoint full matrices**, not at hybrids.

Fix a complex `z`.  Set

`A = M_n - z sqrt(d(1-p)) I`,
`A' = B_(n,p) - z sqrt(d(1-p)) I`,

where `B_(n,p)` has iid Bernoulli(`p`) entries and is independent of `M_n`.

For fixed `z`, the source shift condition

`|z|sqrt(d(1-p)) <= sqrt(d) log log d`

holds for all sufficiently large `n`.

There is a constant `K_eps<infinity` such that

`P(s_n(A)<n^(-K_eps)) + P(s_n(A')<n^(-K_eps)) = O(d^(-1/2))`.   (9.1)

Here is the explicit deduction from the source.

- If `d >= (log n)^2`, Theorem 1.1 gives an exponent `<9` for `A`, and Theorem 3.1 gives the analogous iid estimate.  Thus `K=9` is safe.
- If `(log n)^(1+eps) <= d < (log n)^2`, use Remark 1.3 and Remark 3.2.  Their parameter is

  `alpha_src = 2 log(6d) / log(d/(C_2 log n))`.

  For all sufficiently large `n`,

  `log(d/(C_2 log n)) >= (eps/2) log log n`

  and, because `d<(log n)^2`,

  `2 log(6d) <= 6 log log n`.

  Hence `alpha_src <= 12/eps`.  The source's explicit bound

  `alpha(n,d) >= n^(-2 alpha_src)`

  therefore gives the safe deterministic threshold `n^(-24/eps)`.

Thus we may take

`K_eps = max(9,24/eps)`.   (9.2)

Now set

`eta = n^(-K_eps-2)`.   (9.3)

Then `log(n/eta)=O_eps(log n)`.

## 10. Head comparison by regularized hybrid replacement

Let `H_0` be the first `m` shifted rows of `A'`, and let `H_m` be the first `m` shifted rows of `A`.  For `1<=i<=m`, let `H_i` use the first `i` fixed-sum rows and the remaining `m-i` iid rows.  Define

`Phi_eta(H)=1/2 log det(HH^*+eta^2 I_m)`.

When row `i` is replaced, condition on the other `m-1` hybrid rows and call their matrix `B_i`.  Section 5 yields a positive contraction `Q_i` with

`tr Q_i >= n-m+1 >= n delta`.   (10.1)

The two one-row Schur factors are

`rho_i^2 = eta^2 + (R_i+u_i)^*Q_i(R_i+u_i)`,
`(rho'_i)^2 = eta^2 + (R'_i+u_i)^*Q_i(R'_i+u_i)`.

Conditional on `B_i`, `R_i` is the fixed-sum row and `R'_i` is the iid Bernoulli row, independent of the conditioning.  Therefore Lemma 7.1 applies uniformly over **every** hybrid realization.

Since `p(1-p)>=d/(2n)`, (10.1) gives

`p(1-p) tr Q_i >= (d delta)/2`.   (10.2)

The deterministic logarithmic range is `O_eps,z(log n)` by (7.5), (9.3).  Hence there is a quantity

`b_n <= C sqrt(log(e d)/(d delta))`
`       + C_eps,z log n sqrt(d) exp(-c d delta)`   (10.3)

such that, for every `i`,

`E( |log rho_i-log rho'_i| | B_i ) <= b_n`.   (10.4)

Now `d delta=d^(eps/(2(1+eps)))`.  Therefore `log d=o(d delta)`.  Also, for all sufficiently large `d`,

`sqrt(d) exp(-c d delta) <= exp(-c' d delta)`.

Using (8.4), `log n exp(-c' (log n)^(eps/2)) ->0`.  Thus

`b_n ->0`.   (10.5)

By the exact Schur factorization,

`Phi_eta(H_m)-Phi_eta(H_0) = sum_{i=1}^m (log rho_i-log rho'_i)`.

Taking absolute values, expectations, and using (10.4),

`E | [Phi_eta(H_m)-Phi_eta(H_0)]/n | <= (m/n)b_n <= b_n ->0`.   (10.6)

So the regularized head-volume difference converges to zero in `L1`, hence in probability.  This is the key replacement of the source's all-rows-good union bound.

### Removing the ridge at the two endpoints

On the endpoint good event from (9.1), Cauchy interlacing (source Lemma 3.6) gives

`s_m(H_m) >= s_n(A) >= n^(-K_eps)`,
`s_m(H_0) >= s_n(A') >= n^(-K_eps)`.   (10.7)

For either endpoint `H`,

`0 <= Phi_eta(H)-log Vol(H)`
` = 1/2 sum_{j=1}^m log(1+eta^2/s_j(H)^2)`
` <= (m/2) log(1+n^(-4))`.   (10.8)

After division by `n`, (10.8) tends to zero.  Since the good event has probability tending to one, (10.6)--(10.8) prove that the source's head term `T1` tends to zero in probability under the weaker assumption `d >= (log n)^(1+eps)`.

Crucially, no least-singular-value estimate for a hybrid matrix has been used.

## 11. The tail term with the new `m`

On the same endpoint good event, every prefix of `A` and `A'` has its smallest singular value at least the full-matrix smallest singular value by Cauchy interlacing.

Let `d_k` be the distance of row `k` of `A` to the span of its predecessors.  Applying the negative second moment identity (source Lemma 3.7) to the first `k` rows and then interlacing gives

`d_k^(-2) <= sum_{j=1}^k s_j(prefix)^(-2)`
` <= k s_k(prefix)^(-2)`
` <= n s_n(A)^(-2)`.

Thus

`d_k >= n^(-K_eps-1/2)`.   (11.1)

The same holds for `d'_k` from `A'`.  Deterministically,

`d_k <= ||R_k+u_k|| <= C_z sqrt(n)`,
`d'_k <= ||R'_k+u_k|| <= C_z sqrt(n)`,   (11.2)

since a `{0,1}` vector has norm at most `sqrt(n)`.

Therefore, on the endpoint good event,

`max_k |log d_k-log d'_k| <= C_eps,z log n`.   (11.3)

There are at most `n-m <= n delta+1` tail rows, so

`|T2| <= C_eps,z (delta+1/n) log n ->0`   (11.4)

by (8.5).

Combining Sections 10 and 11 proves, for every fixed `z in C`,

`(1/n)log|det(A)| - (1/n)log|det(A')| ->0`

in probability whenever `d >= (log n)^(1+eps)` and `d<=n/2`.

## 12. Completion of Theorem 4.1

Normalize

`\bar M_n = M_n/sqrt(d(1-p))`,
`\bar B_n = B_(n,p)/sqrt(d(1-p))`.

The Hilbert--Schmidt tightness condition in the source's replacement principle is unchanged:

`E ||\bar M_n||_HS^2 = E ||\bar B_n||_HS^2 = n/(1-p) <=2n`.

Section 11 proves the normalized log-determinant comparison for every fixed `z`, hence in particular for almost every `z`.  The replacement principle therefore transfers the ESD from `\bar B_n` to `\bar M_n`.

Because `d->infinity` and `d/n->0`, the sparse iid Bernoulli circular law invoked by Li--Litvak--Yu applies to `\bar B_n`.  Hence `\bar M_n` also converges in probability to the circular law.  This proves Theorem 4.1 and the in-track bound `p_comb<=1`.  ∎

## 13. Why this does not prove Conjecture 3.9

The new argument has moved the bottleneck exactly to the source's current quantitative invertibility range.

The ridge hybrid comparison itself only needs `d delta ->infinity` and can tolerate very slow growth after a suitable head/tail balance.  What presently forces the `log^(1+eps)` regime is the final removal of the ridge at the **endpoint** matrices: Sections 9--10 use Theorem 1.1 / Theorem 3.1, whose current stated range begins at `C log n`.

Thus the next source-valid obstruction is precise:

> obtain enough a.e.-shift log-integrability below `C log n` to remove endpoint regularization, without demanding nonsingularity at `z=0`.

The prior run already observed that zero columns are only an `o_P(n)` fraction when `d->infinity`, so exact singularity at `z=0` is not by itself an ESD obstruction.  A continuation should therefore attack regularization removal for fixed nonzero `z` directly, rather than seek sublogarithmic unshifted nonsingularity.

## 14. Three section-B moves and outcomes

- **B5 — add a parameter and differentiate/deform:** successful.  The ridge parameter `eta` makes every hybrid log-volume finite and postpones all true invertibility input to the two endpoints.
- **B11 — dualize:** successful.  Schur complementation converts row replacement into a resolvent contraction `Q_eta`; `tr Q_eta>=n-m+1` is the invariant that replaces exact codimension of an orthogonal projection.
- **B28 — replace for-all with typical:** successful.  Integrating the conditional tail controls the average logarithmic increment and removes the source's `n`-fold union bound, lowering the logarithmic exponent from 2 to 1.

This triple is different from the previous run's B2/B6/B30.

## 15. Tests actually run

No simulation and no finite-size spectral fit was used as evidence for the asymptotic theorem.

The finite/symbolic self-check executed this run verifies only the exact ridge Schur identity, the ridge resolvent identity, the trace-gap identity in the smallest nontrivial case, and the exponent algebra in (8.2).  Its archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

The asymptotic proof is the written argument in Sections 5--12.  It has **not** yet received the two independent other-track audits required for repository closure.

## 16. Source metric, auxiliary progress, and unresolved full-scope gap

### Source-relevant metric

- before: source/literature `p_comb <=2`;
- after this run: written in-track theorem `p_comb <=1`;
- independent validation: **PENDING**;
- full Conjecture 3.9 (`d->infinity` at any speed): **OPEN**.

### Auxiliary progress, not counted as a separate metric

- recovered that arXiv:2604.10446 is now v2 (11 Aug 2026), retitled and with the parent explicitly labeled Conjecture 3.9;
- isolated the source's `log^2` loss to the all-hybrid-row union bound in Theorem 3.8 rather than to the least-singular-value theorem itself;
- proved the PSD-contraction analogue of the source's projection-distance concentration lemma;
- derived a uniform conditional `L1` logarithmic replacement bound for ridge row factors.

### Remaining gap

To move below `p_comb=1`, one needs a replacement for endpoint polynomial least-singular-value control in the sublogarithmic regime, preferably only for almost every fixed nonzero shift and only at the level required for log-integrability.  The exact zero-column obstruction at `z=0` means that simply extending unshifted nonsingularity is the wrong target.

## 17. Runtime/capability honesty

GPT-6 maximum remains a prompt request only in this environment.  The exposed native task interface has fields for task title/prompt/schedule/timing/enabled state but no binding model selector, no reasoning-effort selector, no authenticated effort telemetry, and no guaranteed run duration.  This run identifies as GPT-5.6 Sol; reasoning level is UNVERIFIED.  Enforcing GPT-6/maximum would require the platform to expose and bind those selectors for scheduled executions.

The historical P26 error `You cannot modify this task` is not a mathematical blocker and was not bypassed.  Repository records say P26 was later updated from an authorized context.  For any task that currently returns that permission error, the valid remedy is the authorized owner/workspace context or platform authorization/support, not a duplicate task or repository-side imitation of a scheduler update.

## 18. Ledger delta for the designated shared-root maintainer

No shared root file was edited by HARD7-02.  Suggested coordinator delta:

`HARD7-02 | Li--Litvak--Yu Conjecture 3.9, row-combinatorial circular law | p_comb: <=2 -> <=1 (new written in-track theorem; independent validation pending) | PARTIAL / SOURCE OPEN`

## 19. Next checkpoint

The next non-repeating triple should attack the endpoint-only bottleneck, not redo the ridge lemma.  A productive continuation is to seek a sublogarithmic fixed-`z!=0` regularization-removal theorem (for example by B4/B18/B30: prove a weaker a.e.-shift log-integrability statement completely, rewrite it as a Hermitized Stieltjes/regularized determinant problem, and localize the singular-value integral by scale).

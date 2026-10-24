Model: **GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did not run on GPT-6 at verified maximum reasoning. NO MOVEMENT: external/source-verified `p_comb <= 2 -> <= 2`; the in-track written candidate `p_comb <= 1 -> <= 1` remains pending independent validation. Methods tried this run: B10 / B17 / B23.**

# HARD7-02 — Li--Litvak--Yu Conjecture 3.9: terminal block volume, Pluecker shell recursion, and a covariance-only obstruction

Date: 2026-09-20 UTC  
Track: `HARD7-02`  
Status: **PARTIAL / SOURCE OPEN**  
Frozen metric: `p_comb`  
External verified value before/after: **`<=2 -> <=2` (no movement)**  
Internal written milestone before/after: **`<=1 -> <=1` pending independent validation**  
Post-STUCK1 ordinary no-movement count: **3**

This is therefore the third consecutive ordinary no-movement run after STUCK1. Under Section I, the **next invocation is forced to be the second/final stuck-thinking recovery (STUCK2)** on this target; it must not merely append another lemma. If the later Section-I terminal condition is reached without movement, this target must be handed off and HARD7-02 must rotate rather than disabling the schedule.

## 1. Controls, continuity, ownership, and current-status check

This run continues the exclusively owned Li--Litvak--Yu fixed-row-sum circular-law target in

`operations/claims/LI-LITVAK-YU-2026-SPARSE-COMBINATORIAL-CIRCULAR-LAW.md`.

I re-read:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the current LLY claim and the latest HARD7-02 checkpoint;
- repository search surfaces for neighboring non-Hermitian/circular-law work, including the distinct C0031/C0032 heavy-tail claims. The newest R7-05/R7-06 commits have rotated to unrelated targets, so no new ownership collision with this exact LLY conjecture was found.

The source remains Dongbin Li, Alexander E. Litvak and Tingzhou Yu, *Least singular values of shifted sparse random combinatorial matrices*, arXiv:2604.10446v2, revised 11 August 2026. In the current source, Corollary 1.4 proves the circular law for

`d >= (log n)^(2+eps), d=o(n)`,

and Conjecture 3.9 asks for the same conclusion under the sole growth assumption

`d(n) -> infinity`.

A bounded fresh 20 September 2026 search used the exact arXiv identifier/title/authors and the phrases `fixed row sum circular law`, `random combinatorial matrices circular law`, and `sparse circular law`. It recovered the LLY source, Sah--Sahasrabudhe--Sawhney's iid sparse result (*The sparse circular law, revisited*, arXiv:2310.17600), and related permutation-space anti-concentration work, but no later theorem resolving Conjecture 3.9 or lowering the exact independent-row fixed-row-sum circular-law hypothesis below the LLY source baseline was located. This is bounded negative evidence, not a worldwide novelty certificate.

No root ledger, other track, scheduler, email, Drive, workflow, permission, or public-posting state was edited.

## 2. Where the previous route stopped

The preceding report proved a uniform shifted projection lower tail for a fresh fixed-sum row. If `P` is any rank-`h` projection and `R=Y-(d/n)1`, then for a universal `C`,

`P( ||P(R+u)|| <= (1/2)sqrt(d(h-1)/n) )`
` <= C [ n/(d(h-1)) + 1/d^2 ].`

Thus the row-only absorption process controls all kernel dimensions `h >> n/d` for every `d->infinity`. The remaining hard edge consists of only

`H := ceil(n/d)`

terminal dimensions. Since `H=o(n)`, a collective terminal determinant with logarithmic cost `O(H polylog d)` would be sufficient. The fatal mistake would be to pay `O(log n)` separately for each of the `H` terminal rows, since `H log n=o(n)` is equivalent to the logarithmic threshold `d >> log n` that we are trying to escape.

This run therefore stops treating the last `H` factors individually.

## 3. B10 — exact block absorption: the last `H` factors are one determinant

Let `B` be an `m x n` complex matrix of full row rank, let `C` be a `k x n` matrix, and suppose `m+k=n`. Put

`P_B = I - B^*(BB^*)^{-1}B`,

which is the orthogonal projection onto `ker B`. Let `U` be an `n x k` matrix with orthonormal columns spanning `ker B`, so `P_B=UU^*`.

### Lemma 3.1 (block Gram absorption)

For `A=[B;C]`,

`|det A|^2 = det(BB^*) det(C P_B C^*)`
`           = det(BB^*) |det(CU)|^2`.                            (3.1)

#### Proof

The Gram matrix has block form

`AA^* = [[BB^*, BC^*], [CB^*, CC^*]]`.

Since `BB^*` is invertible, its Schur complement gives

`det(AA^*)`
` = det(BB^*) det(CC^* - CB^*(BB^*)^{-1}BC^*)`
` = det(BB^*) det(CP_BC^*)`.

Also `P_B=UU^*`, so

`CP_BC^*=(CU)(CU)^*`,

whose determinant is `|det(CU)|^2`. Finally `det(AA^*)=|det A|^2`. `square`

This is the block version of the one-row identity from the previous route. It removes the arbitrary sequential ordering of the terminal rows: all terminal hard-edge loss is encoded by a single square projected matrix `CU`.

The finite algebra was independently self-checked inside this track in

- `artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T14-10-22Z__terminal_reservoir_covariance_check.py` @ `f6cf9a0b5d29ce762e8d8ef570906aa026ae0d88`,
- archived output @ `0261ec955c140e307454c8448f83df92160e5b6f`,

where two exact rational block-Gram examples have determinants `9` and `16` and the output ends `ALL_EXACT_CHECKS_PASS = True`. The checker is a self-check, not an independent audit.

For the source model, fix a Girko shift `z`, let `A(z)=M-z sigma I`, `sigma=sqrt(d(1-d/n))`, take `B` to be any `n-H` revealed rows and `C` the remaining `H` fresh rows. The hard-edge obligation becomes

`[ - log det(C P_B C^*) ]_+ = o_p(n)`                          (3.2)

for Lebesgue-a.e. fixed `z` (with the already-controlled bulk factors separated as in the preceding reports). Because `H=o(n)`, the natural target is actually much stronger: terminal negative log of order `O_p(H)`.

## 4. B17 — the terminal square block has the right factorial scale

The exact second-order geometry predicts precisely `O(H)`, not `O(H log n)`, terminal loss.

Let `Y` be a uniform `d`-subset indicator in `{0,1}^n`, set

`p=d/n`, `R=Y-p1`,

and

`alpha = d(n-d)/(n(n-1))`.

Then

`E R=0`, `Cov(R)=alpha(I-11^*/n)`.

Let `V subset 1^perp` have dimension `H`, and let `U` be an orthonormal basis matrix for `V`. For independent rows `R_1,...,R_H`, define the square projected matrix

`X_i = R_i^* U`,  `X=[X_1;...;X_H]`.

Then each row has exact covariance

`E X_i^* X_i = alpha I_H`.                                      (4.1)

### Lemma 4.1 (exact determinant second moment)

Under (4.1),

`E |det X|^2 = H! alpha^H`.                                      (4.2)

#### Proof

Expand both determinants:

`det X = sum_pi sgn(pi) product_i X_{i,pi(i)}`.

Independence across the rows gives

`E |det X|^2`
` = sum_{pi,tau} sgn(pi)sgn(tau)`
`   product_i E[X_{i,pi(i)} conjugate(X_{i,tau(i)})]`.

By (4.1), the factor for row `i` is `alpha` if `pi(i)=tau(i)` and zero otherwise. Hence only `pi=tau` survives, and the `H!` surviving permutations each contribute `alpha^H`. `square`

Now take

`H=floor(n/d)`, `d->infinity`, `d=o(n)`.

Then `H alpha -> 1`, so Stirling gives

`log E|det X|^2`
` = log(H!) + H log alpha`
` = -H + o(H)`.                                                  (4.3)

Thus the collective terminal determinant naturally lives on the `exp(-Theta(H))` scale. Since `H=n/d=o(n)`, this is exactly the scale that can remove the logarithmic sparsity threshold.

This factorial cancellation is the important numerical signal of the run: the terminal block should be treated as a square volume, not as `H` separate events each charged a worst-case `log n` price.

## 5. B23 — covariance is not enough: an exact isotropic terminal counterexample

The positive scale calculation above does **not** imply a lower tail. In fact, even exact isotropic covariance on `1^perp` can coexist with terminal singularity with probability tending to one.

Assume `d->infinity`, `d=o(n)`, and put `H=floor(n/d)`. For large `n`, `2H<=n`. Define the `H`-dimensional pair-difference subspace

`V = span{ (e_1-e_2)/sqrt(2), (e_3-e_4)/sqrt(2), ..., (e_{2H-1}-e_{2H})/sqrt(2) }`.

Then `V subset 1^perp`. Let `U` be the displayed orthonormal basis, and let

`X=R^*U`.

Exactly as above,

`E X^*X = alpha I_H`.                                            (5.1)

Nevertheless, if the support of `Y` avoids the first `2H` coordinates, then `X=0`. The exact probability of this event is

`q_n = binom(n-2H,d)/binom(n,d)`.                                (5.2)

Moreover,

`q_n -> e^{-2}`.                                                 (5.3)

Indeed,

`log q_n = sum_{j=0}^{d-1} log(1 - 2H/(n-j))`.

Here `max_j 2H/(n-j)=O(1/d)->0`,

`sum_j 2H/(n-j) = 2+o(1)`,

and

`sum_j (2H/(n-j))^2 = O(1/d)->0`,

which gives (5.3).

Now take `H` independent fresh rows with this same projection. If `D_H` is the resulting `H x H` projected matrix, then

`P(det D_H != 0) <= (1-q_n)^H -> 0`,                             (5.4)

because a single zero projected row forces singularity and `H->infinity`.

This counterexample is stronger than a generic coordinate-plane obstruction: it lies entirely in `1^perp`, has the **exact isotropic covariance** (5.1), and at the same time its determinant is zero with probability tending to one. Consequently (4.2) is carried by rare nonsingular configurations. A second moment or covariance-only Paley--Zygmund argument cannot control the terminal determinant.

The diagonal shift does not rescue an arbitrary pair `(V,T)`. If the terminal row-index set `T` is chosen disjoint from `{1,...,2H}` (possible for large `d`), then `P_V e_t=0` for every `t in T`, so the projected diagonal shifts vanish and (5.4) survives for every `z`.

**Conclusion of the negation attack.** Any proof of (3.2) must exploit that `V=ker B` and the remaining diagonal indices arise from the **same shifted matrix**. The terminal subspace cannot be replaced by an arbitrary deterministic isotropic subspace. This rules out the most tempting covariance-only completion of the previous run.

## 6. The exact Pluecker identity exposes the missing self-consistent geometry

The relation between the actual prefix kernel and its terminal coordinate set has an exact algebraic form.

Let `B` be `m x n`, full row rank, with `m=n-H`, and let `U` be an orthonormal basis for `ker B`. For `T subset [n]` with `|T|=H`, write `J=T^c`, and let `B_J` denote the square `m x m` submatrix formed from columns in `J`.

### Lemma 6.1 (complementary Pluecker coordinate)

`|det U_T|^2 = |det B_J|^2 / det(BB^*)`.                         (6.1)

#### Proof

Set

`Q=B^*(BB^*)^{-1/2}`.

The columns of `Q` are an orthonormal basis for the row space of `B`, and `[Q U]` is unitary. Complementary minors of a unitary matrix have equal absolute determinant, so

`|det U_T| = |det Q_J|`.

But

`Q_J = B_J^*(BB^*)^{-1/2}`,

hence

`|det Q_J|^2 = |det B_J|^2 / det(BB^*)`. `square`

For a **self-consistent row shell**, take the revealed row set itself to be `J`:

`B=A_{J,*}(z)=M_{J,*}-z sigma E_{J,*}`.

Then

`B_J = A_{J,J}(z)`,

and (6.1) becomes

`|det U_T|^2`
` = |det A_{J,J}(z)|^2 / det(A_{J,*}(z)A_{J,*}(z)^*)`.           (6.2)

Thus the terminal coordinate leverage-volume is exactly a **principal-minor / full-row-volume ratio** of the already revealed shifted matrix. The hard-edge geometry is not an arbitrary-subspace problem; it is a recursive principal-minor problem.

For comparison, for any fixed `U`, Cauchy--Binet gives

`sum_{|T|=H} |det U_T|^2 = det(U^*U)=1`.                         (6.3)

Hence some coordinate set satisfies

`|det U_T|^2 >= 1/binom(n,H)`.                                   (6.4)

At `H~n/d`,

`(1/2) log binom(n,H) <= (H/2) log(en/H)`
`                    = O((n/d) log d) = o(n)`.                   (6.5)

So **for every fixed kernel** there exists a coordinate shell whose Pluecker cost is already small enough for the full `d->infinity` conjecture. The unresolved issue is self-consistency: choosing `T` changes which rows form `B`, hence changes `U`. Equation (6.2) says exactly what must replace the non-self-consistent optimizer in (6.4).

## 7. Degree-one shell thinning is exactly density preserving in mean

The new principal-minor formulation interacts cleanly with the fixed-row-sum law.

Fix a coordinate shell `T` of size `L`, let `J=T^c`, and for one row `Y` put

`R_T = sum_{j in T} Y_j`.

Then

`P(R_T=r)`
` = binom(L,r) binom(n-L,d-r) / binom(n,d)`.                      (7.1)

Conditional on `R_T=r`, the restriction `Y_J` is a uniform `(d-r)`-subset indicator on the `n-L` coordinates of `J`. Across different matrix rows, these conditional restrictions remain independent.

The exact mean is

`E R_T = dL/n`,

so

`E(d-R_T) = d(n-L)/n`.                                           (7.2)

If, for the moment, `L=n/d` is integral, then

`E R_T=1`, `E(d-R_T)=d-1`,

and with `n'=n-L=n(1-1/d)`,

`(d-1)/n' = d/n`.                                                (7.3)

Thus removing a shell of size `n/d` removes **one degree per row in expectation while preserving the density exactly in mean**. The hypergeometric fluctuation has variance of order one.

There is a matching second-order conservation. Conditional on `R_T=r`, the centered restriction to `T` has covariance

`[r(L-r)/(L(L-1))] (I_L-J_L/L)`,                                 (7.4)

and averaging over the hypergeometric `R_T` gives exactly

`E[ r(L-r)/(L(L-1)) ]`
` = d(n-d)/(n(n-1)) = alpha,                                     (7.5)

independent of `L`. To see (7.5), note that `R_T(L-R_T)` counts ordered selected/unselected pairs inside `T`; each ordered pair has probability `d(n-d)/(n(n-1))`.

Equations (7.1)--(7.5), Vandermonde normalization, the endpoint product bounds, and (3.1) were checked with exact rational arithmetic in 110 small slice cases by the current run's checker/output cited above.

For the self-consistent principal minor `A_{J,J}(z)`, conditioning on the removed shell entries therefore produces an **independent-row inhomogeneous combinatorial matrix** on `J`, with row degrees

`d_i' = d-R_{T,i}`,

and the same diagonal shift on rows/columns indexed by `J`. At shell size `L~n/d`, these degrees are centered at `d-1`, with `O(1)` one-row fluctuation. This is the first exact recursion found on this target that changes `(n,d)` while preserving the sparse density scale instead of paying a separate worst-case hard-edge estimate.

## 8. A mixed-shift polynomial makes the recursion visible

The same shell has a useful determinant interpolation. For fixed `T,J`, define a two-parameter diagonal shift

`A_{z,w} = M - sigma(z E_J + w E_T)`,

where `E_J` and `E_T` are diagonal coordinate projections. As a polynomial in `w`,

`F_z(w)=det A_{z,w}`

has degree at most `H=|T|`, and its leading coefficient is exactly

`[w^H]F_z(w) = (-sigma)^H det A_{J,J}(z)`.                       (8.1)

This follows by selecting the `-w sigma` diagonal entry in every row/column of `T`; the complementary determinant is precisely the principal minor on `J`.

Thus the source determinant `det A(z)=F_z(z)` sits on the diagonal of a one-variable polynomial whose leading coefficient is the recursively thinned principal minor from Section 7.

For fixed `z` and a fixed realization, if the leading coefficient is nonzero and `rho_1,...,rho_H` are the roots of `F_z`, Jensen's circle identity gives

`(1/(2pi)) int_0^{2pi} log |F_z(R e^{it})| dt`
` = log(sigma^H |det A_{J,J}(z)|)`
`   + sum_j log max(R,|rho_j|)`.                                 (8.2)

Hence the angular average is bounded below by

`H log(sigma R) + log|det A_{J,J}(z)|`.                          (8.3)

This does **not** yet control the diagonal value `F_z(z)`: a deterministic polynomial can have a root exactly at `w=z`. The missing ingredient is therefore an anti-cancellation theorem for the random mixed-shift polynomial, not another covariance estimate.

## 9. What the three methods established

### B10 — DERANDOMIZE

Replacing terminal row-by-row exposure by the exact block identity (3.1) removes arbitrary ordering. The complementary Pluecker identity (6.2) then turns the terminal coordinate geometry into a principal-minor/full-volume ratio. This produced a deterministic recursive object rather than another one-row checker.

### B17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

Two numerical structures coincide at the critical terminal size `H~n/d`:

1. `H! alpha^H = exp(-H+o(H))`, showing the collective determinant has exactly the sublinear logarithmic scale needed for `d->infinity`;
2. a shell of `n/d` coordinates removes one expected 1 per row and maps `(n,d)` to `(n(1-1/d), d-1)` while preserving `d/n` exactly in mean.

This suggests a density-preserving determinant renormalization rather than a sharper one-step least-singular-value theorem.

### B23 — DO WHAT THE PROPOSER DID NOT EXPECT

The pair-difference construction in Section 5 gives exact isotropic covariance but terminal singularity with probability tending to one. It rules out the broad statement that the terminal `H x H` block can be controlled uniformly over deterministic `H`-subspaces from covariance alone. The proof must use self-consistent prefix/diagonal geometry.

## 10. Exact blocker after this run

The source metric did not move because no theorem yet transfers the density-preserving shell recursion into a lower tail at the source diagonal shift.

A concise form of the remaining hard-edge obligation is

`[ -log det(C P_{ker B} C^*) ]_+ = o_p(n),`                      (10.1)

with `H=ceil(n/d)`, `B` the first `n-H` shifted rows and `C` the remaining shifted rows, for Lebesgue-a.e. fixed `z`.

The new structural reduction says that a viable proof of (10.1) can instead target the **self-consistent principal-minor ratio**

`log det(A_{J,*}(z)A_{J,*}(z)^*)`
` - 2 log |det A_{J,J}(z)| = o_p(n),                             (10.2)

or an equivalent shell-telescoping statement, together with a random anti-cancellation step transferring the mixed-shift polynomial control from its leading coefficient to `w=z`.

The arbitrary-subspace version of (10.1) is false by Section 5. Equation (10.2) preserves exactly the extra structure that the false version discards.

## 11. Simplest special case now visible

The simplest still-unproved shell case is:

- `H=floor(n/d)`;
- a deterministic shell `T` of size `H`, `J=T^c`;
- processed rows indexed by `J`;
- condition on the shell counts `R_{T,i}` only;
- prove a sublinear-log comparison between the full row volume of `A_{J,*}(z)` and the determinant of the inhomogeneous principal minor `A_{J,J}(z)`, when all but `o(n)` residual degrees equal `d-O(1)` in aggregate.

This is strictly more structured than the arbitrary-projection problem and is the natural candidate for the required STUCK2 thinking run.

## 12. Runtime/model capability and denied-task issue

Actual runtime available to this report: **GPT-5.6 Sol; reasoning level UNVERIFIED. It is not verified GPT-6 maximum.**

The exposed native scheduler/update interface still offers task title, prompt, schedule, timing mode, enabled state, and relative start offsets. It exposes **no model selector, no reasoning-effort selector, and no guaranteed run-duration field**. Therefore GPT-6 maximum can only be requested in prompt text from this interface; changing that would require the platform to expose a binding model/reasoning setting (or move the task to an authorized interface that does).

The repository policy records historical probes where P26/P01/P03 returned `You cannot modify this task`. That is an authorization/ownership-context failure, not a mathematical or repository failure. The permitted workaround is to modify the task from the authorized owning account/workspace/interface or through platform support; do **not** bypass it and do not create a duplicate schedule. Root `RESULTS.md` separately records that P26 later succeeded in a different authorized context, confirming that such denial can be context-specific. HARD7-02 did not modify P26 or any other schedule in this run.

## 13. Section-I consequence and next methods

Because the post-STUCK1 ordinary no-movement count is now three, the next invocation must be **STUCK2**, the second/final stuck-recovery thinking run for this target. It must include the five mandatory Section-I items and choose exactly one recovery rather than adding a routine lemma.

The three fresh methods reserved for that thinking run are **B16 / B24 / B26**:

- B16: compute exact small shell recursions and principal-minor ratios, not just singular values;
- B24: search for the extremal self-consistent shell geometry maximizing the Pluecker loss in (10.2);
- B26: hunt sporadic shell/count configurations where the mixed-shift polynomial cancels at `w=z` despite a healthy leading coefficient.

A hard target may not receive a third stuck recovery. If STUCK2 and the subsequent allowed recovery fail to move the frozen metric under the controlling Section-I protocol, leave a complete handoff and rotate to a fresh eligible HARD7-02 target.

## 14. `ledger_delta` (for shared maintainer; no root write here)

```yaml
track: HARD7-02
target: Li--Litvak--Yu Conjecture 3.9, sparse random combinatorial circular law
status: PARTIAL / SOURCE OPEN
metric: p_comb
external_before: <=2
external_after: <=2
internal_candidate_before: <=1 (pending independent validation)
internal_candidate_after: <=1 (pending independent validation)
movement: false
methods: [B10, B17, B23]
new_exact_results:
  - block Gram absorption identity for the terminal H-row volume
  - H! alpha^H determinant second-moment identity on V subset 1^perp
  - isotropic pair-difference terminal counterexample: determinant zero with probability ->1 at H~n/d
  - complementary Pluecker identity reducing terminal coordinate volume to principal-minor/full-row-volume ratio
  - density-preserving degree-one shell recursion in conditional distribution
  - mixed-shift polynomial leading-coefficient recursion
remaining_obligation: self-consistent shell principal-minor lower tail / mixed-shift anti-cancellation sufficient for terminal negative-log mass o(n)
stuck_state: third ordinary no-movement run after STUCK1; next invocation forced to STUCK2
artifacts:
  checker_commit: f6cf9a0b5d29ce762e8d8ef570906aa026ae0d88
  output_commit: 0261ec955c140e307454c8448f83df92160e5b6f
  output_final: ALL_EXACT_CHECKS_PASS = True
```

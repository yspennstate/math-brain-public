Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **NO MOVEMENT in the frozen metric: external/source-verified `p_comb <= 2 -> <= 2`, while the in-track written candidate `p_comb <= 1 -> <= 1` remains pending independent validation. Methods B3/B13/B29. This is the third consecutive no-movement run after the `p_comb<=1` candidate, so Section I is triggered for the next invocation.**

# HARD7-02 — Gaussian-normal spread from an exact volume potential

Status: **PARTIAL / SOURCE CONJECTURE OPEN / STUCK PROTOCOL TRIGGERED FOR NEXT RUN.** Nothing below closes Li--Litvak--Yu Conjecture 3.9, promotes the pending `p_comb<=1` argument, or claims publication priority.

## 1. Continuity, ownership, source and runtime

I resumed the exclusive claim

`operations/claims/LI-LITVAK-YU-2026-SPARSE-COMBINATORIAL-CIRCULAR-LAW.md`

and the newest checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-20T09-12-00Z__lly-randomized-shift-matching-product.md`.

I re-read the HARD7 control file, both new-methods control/directive files, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, the canonical claim, the newest own report and targeted neighboring non-Hermitian/heavy-tail ownership records. I also repeated targeted intake/alias searches. The large JSONL intake ledgers are connector-truncated, so this is targeted recovery rather than a false claim that every roughly 780-row record was semantically reread in full. No collision with a posted paper, Bernoulli-singularity claim, released Han target, Campbell--O'Rourke target, or an owner's excluded manuscript was located.

The source remains Dongbin Li, Alexander E. Litvak and Tingzhou Yu, *Least singular values of shifted sparse random combinatorial matrices*, arXiv:2604.10446v2 (revised 11 August 2026), especially Corollary 1.4 and Conjecture 3.9. The source's exact target is the independent-row fixed-row-sum `{0,1}` ensemble normalized by `sqrt(d(1-d/n))`; Conjecture 3.9 asks whether `d(n)->infinity` alone implies convergence in probability of the ESD to the circular law. Corollary 1.4 gives the source-verified logarithmic regime `d >= (log n)^(2+eps)`, `d=o(n)`. A bounded 20 September 2026 search of the exact arXiv identifier/title, the authors' later work, `random combinatorial matrix circular law`, and nearby sparse circular-law results found no later theorem settling Conjecture 3.9 or improving this exact source threshold. This is bounded negative evidence, not a worldwide novelty certificate.

The nearest solved analogue remains the sparse random regular digraph circular law, where `d->infinity` is known and random-normal/product structure is a decisive ingredient. The present independent-row combinatorial model is different.

Runtime metadata is explicit only at the model-family level available to this invocation: **GPT-5.6 Sol**. Reasoning effort telemetry is unavailable, hence **UNVERIFIED**. The scheduler interface visible in this run exposes task title, prompt, schedule, timing mode, enabled state, timezone and notification/email fields, but no model selector, no reasoning-effort selector and no guaranteed execution duration. Thus GPT-6/maximum remains a prompt request only. The historical P26 `You cannot modify this task` failure cannot legitimately be bypassed by repository edits or a duplicate job; an authorized owner/workspace scheduling context or platform support is required. The current repository ledger also records that a later authorized context succeeded for P26, so the old denial is historical rather than a universal current failure. I made no scheduler modifications.

## 2. Frozen metric and stagnation count

The fixed quantity is

`p_comb = inf { p>=0 : for every eps>0, the circular law is rigorously established in the frozen model whenever d >= (log n)^(p+eps) and d=o(n) }`.

Evidence levels remain separate:

- external/source-verified: `p_comb <= 2` before and after;
- HARD7-02 written candidate: `p_comb <= 1` before and after, still pending independent validation.

The 07:12 run produced the internal `<=1` candidate. The 08:12 and 09:12 runs did not move the metric. This run also does not move it, so the unchanged count after that candidate is now **3**. Under Section I, the next invocation must be a thinking/stuck run rather than another ordinary lemma run.

## 3. New idea before code

The previous report converted the deterministic scalar shift into an independent uniform perfect matching and reduced the missing structural input to this question: for a Gaussian random normal to an exposed shifted rowspace, can one force coordinate spread on the still-unmatched columns unless the smaller matching-aligned square block is quantitatively bad?

This run attacks that question directly. The key is that the graph representation of the kernel has an exact scalar potential:

`Psi(B,C) = log det(I + (B^{-1}C)^*(B^{-1}C))`.

It simultaneously measures

1. the covariance floor of the residual coordinates of a Gaussian random normal;
2. the condition-number obstruction in the smaller square block;
3. an exact Cauchy--Binet volume ratio between the whole exposed block and the chosen matching-aligned minor.

This is substantially sharper than trying to control one arbitrary normal coordinate-by-coordinate.

No finite checker was created: the claims below are all-dimensional analytic identities/inequalities and are proved on the page. A toy numerical certificate would not test the asymptotic obstruction.

## 4. Exact graph representation and volume potential

Let

`H = [ B  C ] in C^{m x (m+r)}`

with `B in C^{m x m}` invertible and `C in C^{m x r}`. Put

`K = -B^{-1} C`

and define

`Psi = Psi(B,C) = log det(I_r + K^* K) >= 0`.                       (4.1)

The nullspace of `H` is the graph

`ker H = { (K y, y) : y in C^r }`.                                (4.2)

### Proposition 4.1 (orthonormal kernel embedding)

The matrix

`U = [ K ; I_r ] (I_r + K^* K)^(-1/2)`                            (4.3)

has orthonormal columns and range `ker H`.

#### Proof

Equation (4.2) gives the range. Moreover

`U^* U = (I+K^*K)^(-1/2) (K^*K+I) (I+K^*K)^(-1/2) = I`.

∎

Let `g ~ CN(0,I_r)` be a standard complex Gaussian and set

`W=Ug`, `V=W/||W||`.

Then `V` is the rotationally invariant random unit vector in `ker H`. Its residual block `Y=W_T` has covariance

`Q := E[Y Y^*] = (I_r + K^*K)^(-1)`.                               (4.4)

### Proposition 4.2 (exact volume identities)

One has

`e^Psi = det(HH^*) / det(BB^*)`                                   (4.5)

and, by Cauchy--Binet,

`e^Psi = sum_{S subset [m+r], |S|=m} |det H_S|^2 / |det B|^2`.    (4.6)

Thus `e^{-Psi}` is exactly the squared-volume share of the selected `B` minor in the total Cauchy--Binet volume.

#### Proof

Since `C=-BK`,

`HH^* = B(I+KK^*)B^*`.

Therefore

`det(HH^*)/det(BB^*) = det(I+KK^*) = det(I+K^*K) = e^Psi`,

where the middle equality is the standard equality of the nonzero spectra of `KK^*` and `K^*K`. Cauchy--Binet gives

`det(HH^*) = sum_{|S|=m} |det H_S|^2`,

and division by `|det B|^2` yields (4.6). ∎

## 5. B3: a stronger spread-versus-volume theorem

The potential immediately controls the smallest residual Gaussian variance.

### Lemma 5.1 (covariance floor)

With `Q` from (4.4),

`Q >= e^{-Psi} I_r`.                                               (5.1)

More crudely, if

`s_min(B) >= tau ||C||`                                            (5.2)

for some `tau>0`, then

`Q >= tau^2/(1+tau^2) I_r`.                                        (5.3)

#### Proof

If the singular values of `K` are `s_1,...,s_r` (padding by zeros if needed), then

`Psi=sum_j log(1+s_j^2) >= log(1+||K||^2)`.

Hence `1/(1+||K||^2) >= e^{-Psi}`. Since the smallest eigenvalue of `Q` is exactly `1/(1+||K||^2)`, (5.1) follows.

Under (5.2),

`||K|| <= ||B^{-1}|| ||C|| <= 1/tau`,

which gives (5.3). ∎

For a vector `x in C^T`, recall the coordinate concentration profile

`q_T(x,rho)=sup_a |{j in T: |x_j-a|<=rho}|/|T|`.

### Theorem 5.2 (Gaussian random normal: quantitative residual spread)

Assume `r>=4`. For the random unit normal `V=W/||W||` above, set

`alpha=e^{-Psi}`.

Then

`P( q_T(V, sqrt(alpha)/(32 sqrt(r))) > 1/2 )`
` <= exp(-(3-log 4) r) + r 2^(2-2r)`.                              (5.4)

Consequently, under the simpler condition (5.2),

`P( q_T(V, [tau/sqrt(1+tau^2)]/(32 sqrt(r))) > 1/2 )`
` <= exp(-(3-log 4) r) + r 2^(2-2r)`.                              (5.5)

This is the requested structural dichotomy in a stronger form: unless the exact volume potential `Psi` is large, a Gaussian random normal has residual coordinate spread with exponentially high probability; large `Psi` itself certifies that the selected matching-aligned minor has a tiny Cauchy--Binet volume share.

#### Proof

By (5.1), `Q-alpha I_r` is positive semidefinite. Hence one can realize the residual Gaussian as

`Y = sqrt(alpha) xi + eta`,                                        (5.6)

where `xi~CN(0,I_r)` and `eta~CN(0,Q-alpha I_r)` are independent.

Because `U` is an isometry, `||W||=||g||`. For standard complex Gaussian `g`, `||g||^2` is Gamma(`r`,1). The Chernoff bound at level `4r` gives

`P(||W||>2 sqrt(r)) <= exp(-(3-log 4)r)`.                           (5.7)

Suppose now that `||W||<=2 sqrt(r)` and

`q_T(V, sqrt(alpha)/(32 sqrt(r))) > 1/2`.                           (5.8)

Then more than `r/2` residual coordinates of `Y` lie in one disk of radius

`2 sqrt(r) * sqrt(alpha)/(32 sqrt(r)) = sqrt(alpha)/16`.            (5.9)

Choose one coordinate in that disk as an anchor. Every other coordinate in the same disk lies within distance `sqrt(alpha)/8` of the anchor. Conditional on `eta` and on the anchor coordinate, each different coordinate has an independent `sqrt(alpha) CN(0,1)` noise contribution. Its density is bounded by `1/(pi alpha)`, so the probability of lying in any prescribed disk of radius `sqrt(alpha)/8` is at most

`[pi(alpha/64)]/[pi alpha] = 1/64`.                                (5.10)

If (5.8) holds, some anchor has at least `floor(r/2)` such neighbors. Union-bounding over the `r` possible anchors and all neighbor subsets,

`P((5.8) and ||W||<=2sqrt(r))`
` <= r 2^(r-1) (1/64)^(floor(r/2))`
` <= r 2^(2-2r)`                                                   (5.11)

for `r>=4`. Combining (5.7) and (5.11) proves (5.4).

Finally (5.3) permits the same proof with `alpha=tau^2/(1+tau^2)`, yielding (5.5). ∎

### What this theorem does and does not buy

In the previous report, residual matching anti-concentration was exponential whenever a normal had `q_T(v,rho)<=q<1`. Theorem 5.2 now proves precisely that kind of spread for a *Gaussian random normal* whenever `Psi` is controlled, with explicit scale

`rho ~ e^{-Psi/2}/sqrt(r)`.

This removes the earlier vague phrase "prove random normals are unstructured" from the good-potential branch. It does **not** prove that `Psi` stays controlled often enough along the recursive exposure/descent. That is now the only gluing issue on this route.

## 6. B13: the candidate monovariant is exact, but its cross-scale monotonicity is not proved

The natural candidate is `Psi` itself. It is nonnegative and has three equivalent readings:

- `Psi=log det(I+K^*K)`;
- `Psi=log det(HH^*)-log det(BB^*)`;
- `Psi=-log` of the selected minor's Cauchy--Binet volume share.

Thus a failed spread estimate has a deterministic accounting variable: it can only occur at the price of a large volume deficit.

However, B13 does **not** fully close. Along a nested matching descent, the next `(B',C')` is not obtained from `(B,C)` by an operation for which I can presently prove `Psi(B',C')<=Psi(B,C)` or a telescoping identity with a summable error. Claiming monotonicity here would be false bookkeeping. The exact remaining issue is to pay for a sequence of large-`Psi` levels probabilistically.

A useful deterministic inequality from Proposition 4.2 is

`|det B|^2 = e^{-Psi} det(HH^*)`.                                  (6.1)

So every level with `Psi>L` says that the currently selected matching minor captures at most `e^{-L}` of the total row-volume. The residual matching supplies many alternative minors, but I have not proved the needed uniform conditional statement saying that repeated exponentially poor selections are themselves exponentially unlikely under the coupled row/matching exposure.

## 7. B29: the terminal scale is also the mean-determinant resonance scale

The previous run supplied a shift-dominated terminal minor at size roughly

`m_* = n d^{-1/2} n^{-O_z(1/sqrt(d))}`

for fixed `z!=0`. There is an exact diagnostic explaining why the scale `n/sqrt(d)` is natural.

Fix a matching-aligned `m x m` block

`B = M_{I,J} - lambda P_{I,J}`, `J=P(I)`,                           (7.1)

where `p=d/n` and `lambda !=0`. Conditional on the matching `P`, the rows of `M_{I,J}` are independent and every entry has expectation `p`.

### Proposition 7.1 (exact mean determinant)

Conditional on `P`,

`E det B = det(p 11^T - lambda P)`
`          = (-lambda)^m det(P) (1 - p m/lambda)`.                 (7.2)

#### Proof

The determinant is multilinear in its rows. Since the rows are independent, iterated expectation replaces each random row by its expectation; no within-row independence is needed. Thus

`E det B=det(E B)=det(p11^T-lambda P)`.

Apply the matrix determinant lemma to `-lambda P + p11^T`:

`det(-lambda P + p11^T)`
` =det(-lambda P) [1 + p 1^T(-lambda P)^(-1)1]`
` =(-lambda)^m det(P) [1 - (p/lambda) 1^T P^{-1}1]`
` =(-lambda)^m det(P)(1-pm/lambda)`,

because `P^{-1}1=1`. ∎

This is only an **expectation identity**, not a typical-determinant or invertibility theorem. It therefore earns no metric movement. But its cancellation scale in magnitude is

`m_res ~ |lambda|/p`.

For the circular-law shift

`lambda=z sqrt(d(1-d/n))`,

this is

`m_res ~ |z| n/sqrt(d)`,                                           (7.3)

exactly the order of the previous shift-dominated terminal block. Hence the `n/sqrt(d)` boundary is not merely an artifact of the Chernoff proof: it is also where the deterministic matching shift and the mean row mass balance in the determinant expansion. Treating this as the boundary point of the recursion is the useful B29 compactification.

## 8. Combining the new theorem with the residual matching bound

At an exposure level with residual size `r`, suppose `Psi<=L` for a fixed `L`. Theorem 5.2 says that, except with probability exponentially small in `r`, a Gaussian random normal obeys

`q_T(V, e^{-L/2}/(32 sqrt(r))) <= 1/2`.                            (8.1)

The previous residual-matching counting lemma then supplies exponential block suppression whenever row projections must align to this normal at the corresponding small-ball scale. Thus the "good level" branch of the recursive scheme is now rigorous at the structural level.

If instead `Psi>L`, equation (6.1) records an exact `e^{-L}` volume-share loss and the recursion descends toward the matching-aligned square block. The unresolved step is no longer random-normal spread. It is a **multi-level volume-budget theorem** controlling how many large-`Psi` descents can occur before the `m_*` boundary, under the actual row-slice plus residual-matching law.

A source-relevant closure would require this budget strongly enough to produce the a.e.-`z` lower-tail/logarithmic uniform-integrability estimate used in hermitization. I have not proved it.

## 9. Outcomes of the three moves

- **B3 — PROVE SOMETHING STRONGER:** succeeded. Instead of merely "well-conditioned `B` implies spread," Theorem 5.2 uses the exact volume potential `Psi`; condition number is only a corollary.
- **B13 — FIND WHAT ONLY INCREASES:** partial. `Psi` is the right exact accounting potential and failed spread forces a volume penalty, but monotonicity/telescoping across the stochastic descent is not yet proved.
- **B29 — ADD THE POINTS AT INFINITY:** succeeded structurally. The terminal `n/sqrt(d)` scale is now justified both by the shift-dominated minor theorem from the previous run and by the exact mean-determinant resonance identity (7.2)--(7.3).

No new code/checker was warranted because the claims are symbolic all-dimensional proofs rather than finite enumerations.

## 10. Section-I trigger and exact next obstruction

This is the third consecutive no-movement run after the internal `p_comb<=1` candidate. Therefore the **next** HARD7-02 invocation must be a Section-I thinking/stuck report, not another ordinary theorem-producing run.

The exact blocking statement can now be written without euphemism. For the nested matching-aligned descent, with level potentials

`Psi_j = log det(I + (B_j^{-1}C_j)^*(B_j^{-1}C_j))`,               (10.1)

prove a source-useful summable estimate showing that a chain of large-potential levels is rare before the shift-dominated terminal scale. A representative form strong enough for the present architecture would be: find fixed `L,c>0` and a legitimate block schedule such that

`P( Psi_j > L at every nonterminal level j before reaching m_* )`
` <= exp( -c * [total exposed block mass] ) + o(1),                (10.2)

or prove an alternative quantitative volume-budget estimate that yields the same summable singular-value/log-potential tail. I do **not** claim (10.2) is already true in this exact form; it is the blocking target the next stuck run must analyze, weaken if necessary, or refute.

The simplest special case to inspect next is a **single macroscopic descent step**: conditional on a matching-aligned `B` at residual fraction bounded away from zero, obtain a nontrivial upper tail for `Psi(B,C)` under the actual fixed-row-sum law. If even this cannot be paid, the recursive route should be abandoned rather than decorated with another local lemma.

The nearest solved analogue remains the sparse random-regular-digraph random-normal/product-structure argument. What it has that this proof still lacks is a global structural probability estimate tying random normals/product structure to the whole singular-value range, rather than only the local deterministic spread theorem above.

## 11. Ledger delta for coordinator consumption

`HARD7-02 | Li--Litvak--Yu Conjecture 3.9, row-combinatorial circular law | external p_comb: <=2 -> <=2; written candidate <=1 -> <=1 pending independent validation | PARTIAL / SOURCE OPEN / unchanged-count=3, Section-I next run | B3/B13/B29 | new exact volume-potential Gaussian-normal spread theorem; remaining obligation = probabilistic multi-level volume budget for Psi_j`

No shared root ledger, other-track file, canonical owner, scheduler, email, Drive, workflow or public repository was modified.

Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated GPT-6 selector, reasoning-effort selector, guaranteed-duration field, or applied-run attestation, so I do not claim otherwise. F0002 NEW TARGET INITIALIZED: `gamma_sym = POSITIVE_UNMEASURED` from current literature, source target `gamma_sym=1`; no numerical metric movement. Methods: #2 ATTACK THE NEGATION FIRST, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT.**

# R03 HARD OUTSIDE — F0002 sharp exponential singularity rate for a random symmetric Rademacher matrix

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity: F0001 and F0097 stay handed off

I did not obey the stale native title literally. The newest R03 report,

`runs/R03/20260918T0318Z_49_third_stuck_handoff_rotation_hold_7a31.md`,

records the mandatory third-stuck handoff of F0097 and preserves the earlier third-stuck handoff of F0001. The owner protocol forbids reopening either target without a later explicit reassignment. This run therefore performed successor admission before new mathematics.

I reread/recovered the controlling repository surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R03 report, recent neighboring successor/admission screens, the live claim inventory for plausible queue candidates, and the F-intake record/attempt for F0002. The large intake JSONL corpus cannot be rendered byte-for-byte through one connector response; exact-ID/source retrieval was used for the candidate actually admitted, and no stronger access claim is made.

The recent neighboring screens were useful negative evidence: many apparently free queue rows are now claimed, later resolved, scope-blocked, or reserved by sibling gates. In particular Sendov/I0128 is now resolved; I0087's highlighted scope is later-covered; I0074 remains scope-ambiguous; RS-2026-CL-C, RS-2026-BIS32, RS-2026-DC34/35, I0073, RS-2025-TH17 and the front famous rows checked here already have canonical owners. I did not steal any of them.

## 2. New lawful successor: F0002

The intake contains F0002, sourced to Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797, Section 3, Conjecture 3.3. If `A_n` is the symmetric `n x n` sign matrix whose entries on and above the diagonal are independent Rademacher variables and

`q_n^sym = P(det A_n = 0)`, 

the source conjecture is

`q_n^sym = (1/2 + o(1))^n`.

Ferber--Jain, arXiv:1809.04718 / Forum Math. Sigma 7 (2019), gives the compatible formulation that the singularity probability is conjectured to be at most `(2+o(1))^{-n}`. The elementary equal/opposite-row mechanism supplies the matching base-`1/2` lower scale. This is a different ensemble and a weaker target than the handed-off F0001 exact-prefactor problem.

Fresh primary-literature checks on 2026-09-18 recovered:

1. Campos--Jenssen--Michelen--Sahasrabudhe, arXiv:2105.11384, JAMS 38 (2025), proving `q_n^sym <= exp(-c n)` for an absolute `c>0`. Their introduction explicitly says the sharper `Theta(n^2 2^{-n})` behavior is generally believed and describes their theorem as optimal only up to the constant in the exponent.
2. Yi Han, arXiv:2506.01155v2, JLMS 113 (2026), proving `P(corank A_n >= k) <= exp(-c' k n)` for `1<=k<=c sqrt(n)`.
3. Yi Han, arXiv:2504.15992 (2025), proving strong decoupled least-singular-value/repeated-singular-value estimates in the bulk, not the sharp zero-eigenvalue base.

A bounded current search found no later theorem giving the source base `1/2`. This is bounded negative evidence, not a novelty certificate.

The repository already contains the substantive intake attempt `F0002-A001` from 2026-09-08. I preserved it: it computes the elementary row-pair mechanism and identifies quadratic inverse Littlewood--Offord loss as the old obstruction. Immediately before claiming, `operations/claims/F0002.md` returned 404 and repository search found no competing canonical owner. I therefore created the exclusive F0002 claim at commit

`f946054a2f76ee151b0cbd122b78d7ef695f035d`

and read it back at that exact commit. No shared root or peer file was changed.

## 3. Frozen metric

Define

`gamma_sym = sup { gamma in [0,1] : q_n^sym <= 2^{-(gamma-o(1)) n} }`,

counting only rigorous certified upper bounds. The source target is `gamma_sym=1`; the elementary row-pair lower bound prevents `gamma_sym>1`.

Current literature proves `gamma_sym>0`, but the checked theorem statements expose only an unspecified absolute exponential constant. I therefore record the numeric value honestly as

`POSITIVE_UNMEASURED`,

not as a fabricated decimal. This first F0002 run initializes the metric; it does not numerically improve it. Target status is **OPEN / R03 PARTIAL**.

## 4. Method #2 — attack the negation first: sparse kernels cannot beat the base 1/2

A natural way to refute the source would be to find a dependence mechanism occurring with probability `(b+o(1))^n` for some `b>1/2`. The first place to look is a kernel vector with small support, because symmetry might conceivably make a small relation much cheaper than in the iid nonsymmetric model.

It does not.

### C310 — cross-block sparse-kernel sieve

Let

`E_{n,L} = { there exists 0 != v in ker A_n with 3 <= |supp(v)| <= L }`.

For every `3<=L<=n`,

`P(E_{n,L}) <= sum_{s=3}^L C(n,s) 2^{s^2} p_s^{n-s}`,

where

`p_s = 2^{-s} C(s,floor(s/2)) <= 3/8` for every `s>=3`.

Consequently, for every fixed

`0 < delta < sqrt(log_2(8/3)-1) = 0.6442340407...`,

we have

`P(E_{n,floor(delta sqrt(n))}) <= 2^{-(log_2(8/3)-delta^2-o(1))n} = o(2^{-n})`.

In particular all kernel supports from `3` through, say, `(3/5)sqrt(n)` are exponentially negligible even relative to the elementary `n^2 2^{-n}` row-collision scale.

#### Proof

Fix a support `S subset [n]`, `|S|=s`, and suppose `v` is supported exactly on `S`. Across the cut `(S^c,S)`, the block

`C = A_n[S^c,S]`

has fully independent uniform sign entries despite the symmetry of `A_n`. If `A_n v=0`, then every one of the `n-s` iid rows `X` of `C` obeys

`<X,v_S>=0`.

All `s` coordinates of `v_S` are nonzero. By the Erdős--Littlewood--Offord/Sperner bound,

`|{x in {+-1}^s : <x,v_S>=0}| / 2^s <= p_s`.

The union over real vectors `v_S` is still finite at the level that matters. For a vector `v`, put

`Z(v)={x in {+-1}^s:<x,v>=0}`.

If `r=dim span Z(v)`, then `r<=s-1`; choosing a basis of `r` sign vectors determines `span Z(v)`, and

`Z(v) = {+-1}^s intersect span Z(v)`.

Thus the number of possible zero sets is at most

`sum_{r=0}^{s-1} C(2^s,r) <= 2^{s^2}`.

For the fixed support `S`, a union bound gives at most `2^{s^2} p_s^{n-s}`. Summing over `C(n,s)` supports proves the first display.

For `s<=delta sqrt(n)`, use `C(n,s)<=n^s`, `p_s<=3/8`, and `s^2<=delta^2 n`. The logarithm base two of each summand is at most

`-[log_2(8/3)-delta^2] n + O(s log n)`,

and `s log n=o(n)`. Summing `O(sqrt(n))` terms changes only the `o(n)` term. If `delta^2<log_2(8/3)-1`, the exponent is strictly more negative than `-n`, proving the final claim. QED.

Support one is impossible. A support-two kernel vector forces two sign columns, hence also the corresponding rows, to be equal or opposite; that is precisely the elementary mechanism. So C310 rules out every genuinely new kernel mechanism up to order `sqrt(n)` as a source refutation.

**Prior-art label:** this is a self-contained R03 reduction, not a novelty claim. CJMS already contains substantially deeper structured-vector technology. The value here is that the symmetric cross-block independence gives a short exact source-oriented sieve and shows where a fresh mechanism first has to live.

## 5. Method #11 — dualize: an exact principal-minor / Boolean-quadratic identity

Set `m=n-1`. For an invertible symmetric sign matrix `B in {+-1}^{m x m}`, define

`N(B) = #{ x in {+-1}^m : x^T B^{-1} x in {+1,-1} }`,

and set `N(B)=0` when `B` is singular.

For a corank-one symmetric matrix `A`, let `s(A)` denote the support size of its one-dimensional nullspace.

### C311 — exact weighted corank-one count

For `A_n` and an independent random symmetric sign core `B_m`,

`E[ s(A_n) 1_{corank(A_n)=1} ] = n 2^{-n} E[N(B_m)].`

Moreover every invertible `B` satisfies

`N(B) >= 2m`.

#### Proof

For each `i`, write `B_i` for the `(n-1)x(n-1)` principal minor obtained by deleting row and column `i`. If `rank(A)=n-1`, the adjugate has the form `c vv^T`, where `v` spans the nullspace and `c!=0`. Therefore

`det B_i != 0` iff `v_i != 0`.

If `corank(A)>=2`, every `(n-1)`-minor vanishes. Hence

`sum_i 1_{det A=0, det B_i !=0} = s(A) 1_{corank(A)=1}`.

Fix `i`. Conditional on `B_i=B` being invertible, the remaining random data are an iid sign vector `x in {+-1}^{n-1}` and an independent diagonal sign `eps`. Schur complementation gives

`det A = det B * (eps - x^T B^{-1}x)`.

Thus exactly `N(B)` of the `2^n` extension pairs `(x,eps)` are singular: for each counted `x`, `eps` is uniquely forced to equal the quadratic value `+1` or `-1`. Therefore

`P(det A=0, det B_i !=0) = 2^{-n} E[N(B_m)]`.

Sum over the `n` choices of `i` to get C311.

Finally, for every `j<=m`, take `x=+- B e_j`. These are sign vectors because the `j`th column of `B` is a sign vector, they are all distinct because `B` is invertible, and

`x^T B^{-1}x = e_j^T B e_j = B_jj in {+-1}`.

Hence the `2m` row/column images are always counted. QED.

This identity is source-shaped. The deterministic `2m` solutions are exactly the one-vertex-extension shadows of the elementary equal/opposite-row mechanism. To get the source exponent by this route it would be enough, on the corank-one side, to prove the **average** estimate

`E[N(B_m)] = 2^{o(m)}`.

One must still control `corank>=2` at the source exponent; Han's 2026 `exp(-c' k n)` theorem is powerful but has no checked constant strong enough to substitute for a `2^{-n+o(n)}` bound at `k=2`.

So the dual reformulation isolates two genuinely quantitative obligations rather than another generic quadratic-coupling lemma:

1. average Boolean level-set size of `x^T B^{-1}x` at `+-1` is subexponential;
2. higher-corank singularity is at most `2^{-n+o(n)}`.

## 6. Method #24 — the naive pointwise extremal conjecture is false at dimension four

The first guess after C311 is that the `2m` vectors `+-Be_j` might be all the Boolean solutions, or at least pointwise extremal. I attacked that guess exactly rather than building on it.

It is false immediately.

### C312 — exact finite obstruction

Exhaustive exact-rational enumeration gives:

- `m=1`: 2 invertible symmetric sign cores, all have `N=2`;
- `m=2`: 4 invertible cores, all have `N=4`;
- `m=3`: 32 invertible cores, all have `N=6`;
- `m=4`: 512 invertible cores; **128 have `N=8`, while 384 have `N=12`**.

Thus `N(B)=2m` fails already at `m=4`, and it fails for 75% of invertible symmetric sign cores in that dimension.

One explicit witness is

```
B* = [-1 -1 -1 -1
      -1 -1 -1  1
      -1 -1  1 -1
      -1  1 -1 -1].
```

It has

`(B*)^{-1} = (1/2) [[1,-1,-1,-1],[-1,0,0,1],[-1,0,1,0],[-1,1,0,0]]`

and `N(B*)=12`. Besides the eight vectors `+-B*e_j`, four additional Boolean vectors hit quadratic level `+1`:

`(-1,-1,1,1), (-1,1,1,-1), (1,-1,-1,1), (1,1,-1,-1)`.

The exact checker was executed and its output archived at

- `artifacts/R03/20260918T0405Z_50_f0002_quad_core_exact.py`
- `artifacts/R03/20260918T0405Z_50_f0002_quad_core_exact.out`

with the archived output commit `2b6aaadc92455642ac583d6aaae3e4bbc5845597`.

This finite obstruction is useful because it kills a tempting but false proof strategy: C311 cannot be closed by a pointwise claim that the row images are the only Boolean quadratic solutions. The large-`n` theorem must exploit **average rarity / structure of rich random cores**, not deterministic uniqueness.

## 7. Where this leaves the source

The source metric has not numerically moved:

`gamma_sym : POSITIVE_UNMEASURED -> POSITIVE_UNMEASURED`.

Status: **OPEN / PARTIAL**.

But the admissible route is now narrower than at intake:

- C310 eliminates every genuinely new kernel mechanism of support `3` through `delta sqrt(n)` for any `delta<0.644234...` at a rate already `o(2^{-n})`;
- C311 converts corank-one singularity into an exact average count of Boolean points on the inverse quadratic levels `+-1`;
- C312 proves that a pointwise `N(B)=2m` extremal theorem is false, so the missing theorem must count rich cores rather than ban them.

A useful next object is therefore the richness tail

`H_m(t) = P_B( N(B) >= t, det B !=0 )`.

To prove `E N(B)=2^{o(m)}`, it is enough to control `H_m(t)` over exponentially growing dyadic `t`; the m=4 obstruction says the first nontrivial layer begins immediately above `2m`, while CJMS-style inversion-of-randomness suggests that very rich layers should be structurally rare. The second obligation is a two-vertex/principal-minor count for `corank>=2` that retains the base `1/2` rather than only an unspecified exponential rate.

Next Section-B moves: **#25 COUNT THE SAME THING TWICE, #30 ONE SCALE / ONE DIRECTION AT A TIME, #15 BREAK THE SYMMETRY ON PURPOSE**. Concretely: derive the two-deleted-vertex Schur count, separate exact corank two from corank one, and stratify `N(B)` by the first non-row Boolean solution before invoking any inverse theorem.

## 8. Model / scheduler control boundary

The owner's model-control diagnosis is still true in the surface exposed to this run. Task management exposes title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed one-hour execution field, and no authenticated completed-run model/reasoning telemetry**. Therefore GPT-6 / maximum remains request text rather than a verifiable scheduler setting here.

Actually enforcing it requires the authorized product/backend/API to expose persistent model and reasoning fields plus applied-run attestation. The historical P26 `You cannot modify this task` event is an authorization-context boundary; repository follow-up shows another authorized context later succeeded on P26. The lawful workaround is the owning/authorized task context or platform support/permission repair, not cloning or bypassing ownership. No scheduler or permission change was attempted.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R03
  lane: HARD_OUTSIDE
  predecessor_handoffs:
    F0001: OPEN_PARTIAL_HANDED_OFF_AFTER_THIRD_STUCK
    F0097: OPEN_PARTIAL_HANDED_OFF_AFTER_THIRD_STUCK
  active_target: F0002
  source: "Vu, arXiv:2005.02797, Conjecture 3.3; compatible Ferber--Jain arXiv:1809.04718 formulation"
  ownership_claim:
    path: operations/claims/F0002.md
    creation_commit: f946054a2f76ee151b0cbd122b78d7ef695f035d
    readback_verified: true
  metric:
    name: gamma_sym
    definition: "sup gamma such that q_n^sym <= 2^{-(gamma-o(1))n}"
    source_target: 1
    before: UNINITIALIZED_AFTER_ROTATION
    after: POSITIVE_UNMEASURED
    numerical_movement: false
  status: OPEN_PARTIAL
  stagnation_count: 0
  methods_this_run: [2, 11, 24]
  results:
    C310: "support 3..delta sqrt(n), delta<sqrt(log2(8/3)-1), contributes o(2^{-n})"
    C311: "exact principal-minor identity E[s(A)1_corank1]=n 2^{-n} E[N(B)] and N(B)>=2(n-1)"
    C312: "exact m<=4 enumeration; at m=4, 384/512 invertible cores have N=12>8"
  finite_artifacts:
    checker: artifacts/R03/20260918T0405Z_50_f0002_quad_core_exact.py
    output: artifacts/R03/20260918T0405Z_50_f0002_quad_core_exact.out
    output_commit: 2b6aaadc92455642ac583d6aaae3e4bbc5845597
  prior_art_label: "no novelty claim for C310/C311 until line-by-line comparison with CJMS and earlier quadratic-LO literature"
  remaining_obligation: "prove gamma_sym=1; next attack average richness tail E[N(B)] and source-scale corank>=2"
  next_moves: [25, 30, 15]
  scheduler_model_control: "no exposed model/reasoning selector or applied-run telemetry; GPT-6/max remains prompt-only"
```

No email/Gmail, Drive, public posting, purchase, paid compute, credential or permission change, workflow execution, shared-root edit, peer-track edit, force-push, scheduler modification, or duplicate claim was performed.

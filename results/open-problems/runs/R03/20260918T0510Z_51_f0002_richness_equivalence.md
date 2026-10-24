Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated GPT-6 selector, reasoning-effort selector, guaranteed-duration field, or applied-run attestation, so I do not claim otherwise. F0002 NO MOVEMENT: `gamma_sym = POSITIVE_UNMEASURED -> POSITIVE_UNMEASURED`; methods #25 COUNT THE SAME THING TWICE, #30 ONE SCALE / ONE DIRECTION AT A TIME, #15 BREAK THE SYMMETRY ON PURPOSE.**

# R03 HARD OUTSIDE — F0002: switching normalization and an exact richness equivalence

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and source gate

I continued the current canonical R03 assignment, **F0002**, rather than reopening the stale native-title target F0001. `operations/claims/F0002.md` assigns F0002 exclusively to R03 and explicitly preserves the third-stuck handoffs of both F0001 (iid nonsymmetric sharp prefactor) and F0097 (small-fixed-k random k-SAT threshold). Neither predecessor is reopened here.

Before new mathematics I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R03 report `runs/R03/20260918T0405Z_50_f0002_symmetric_successor.md`, the F0002 claim/intake history, and a fresh neighbouring random-matrix report on F0003. The compact R-series row in `RESULTS.md` is explicitly stale and instructs workers to recover newer own reports; it is not used to overwrite the F0002 claim.

The exact outside source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797, Section 3, Conjecture 3.3. For a symmetric sign matrix `A_n` whose entries on and above the diagonal are iid uniform Rademacher signs,

`q_n^sym := P(det A_n = 0)`,

and the source target is

`q_n^sym = (1/2 + o(1))^n = 2^{-n+o(n)}.`

A fresh bounded literature check on 2026-09-18 again found no later source-matching base-`1/2` theorem. Campos--Jenssen--Michelen--Sahasrabudhe, arXiv:2105.11384 / JAMS 38 (2025), prove only `q_n^sym <= exp(-c n)` for an unspecified absolute `c>0`; Yi Han, JLMS 113 (2026), proves `P(corank A_n >= k) <= exp(-c'kn)` for `1<=k<=c sqrt(n)`. These are major inputs but do not expose the sharp base. This is bounded negative evidence, not a novelty certificate.

The frozen metric remains

`gamma_sym = sup { gamma in [0,1] : q_n^sym <= 2^{-(gamma-o(1))n} }`.

Current certified state is `POSITIVE_UNMEASURED`; source target is `gamma_sym=1`. No numerical lower bound on `gamma_sym` is claimed this run.

## 2. Idea before code

Run 50's exact Schur identity reduced the corank-one contribution to the average Boolean richness

`N(B) = #{ x in {+-1}^m : x^T B^{-1}x in {+1,-1} }`

for an invertible symmetric sign core `B`, with `N(B)=0` if `B` is singular. It also showed pointwise rigidity is false already at `m=4`.

This run attacks the average rather than another pointwise inverse-Littlewood--Offord statement. The key move is to use the full diagonal-sign switching group to normalize one row and column. That converts a sign core exactly into a smaller symmetric `0/1` core. In those coordinates, `N(B)/2` is literally the number of singular one-vertex `0/1` extensions of that core. The same Schur count then extends to every corank and shows that **subexponential average richness is not merely sufficient: it is equivalent to the source conjecture**.

I do **not** claim the switching normalization itself is novel; it is an elementary gauge/congruence transformation. The source-relevant value is the exact combined reduction below.

## 3. Method #15 — break the symmetry: exact sign-to-0/1 normalization

### C313 — switching normalization

Let `B` be an `m x m` symmetric sign matrix, `m>=2`. Put `eps=B_11` and

`D = diag(1, eps B_12, ..., eps B_1m)`.

Then

`B' := eps D B D`

has first row and first column equal to `1`. Hence for `d=m-1`,

`B' = [[1, 1^T], [1, R]]`

with a symmetric sign `d x d` matrix `R`. Define

`C := (J-R)/2`,

so `C` is a symmetric `0/1` matrix. If

`L = [[1, 0], [-1_vec, I_d]]`,

then direct block multiplication gives

`L B' L^T = diag(1, -2C).`                                         (C313.1)

Consequences:

1. `corank(B)=corank(C)` exactly;
2. as `B` ranges uniformly over symmetric sign matrices, `C` is uniform over symmetric `0/1` matrices of size `m-1`;
3. each `C` has exactly `2^m` sign-matrix preimages: the free data are `eps` and the original `m-1` first-row signs.

Therefore the symmetric sign and symmetric `0/1` singularity problems are **exactly dimension-shift equivalent**:

`P(B_m^sign singular) = P(C_{m-1}^{0/1,sym} singular).`             (C313.2)

#### Proof

For `j>1`,

`B'_{1j}=eps * B_1j * (eps B_1j)=1`,

and `B'_{11}=eps B_11=1`. This yields the displayed block form. Since `R-J=-2C`, subtracting the first row from every remaining row and then the first column from every remaining column gives (C313.1). Congruence by invertible `L`, diagonal sign conjugation and multiplication by `eps` preserve rank. The inverse map is determined by `C`, `eps` and the original first-row signs, so every fiber has size `2^m`. QED.

## 4. Methods #15 and #25 — the inverse quadratic level is exactly a singular-child count

The richness `N(B)` is invariant under `B -> -B` and under diagonal sign conjugation `B -> DBD`, because `x -> Dx` permutes the Boolean cube and the target set `{+1,-1}` is sign-symmetric. Thus we may compute `N(B)` on the normalized `B'` above.

### C314 — candidate-level richness identity

Assume the normalized `B'` is invertible, equivalently `C` is invertible. For `x in {+-1}^m`, use the evenness of the quadratic form to fix `x_1=1`, and write

`x = (1, 1-2z)`,  `z in {0,1}^{m-1}`.

From (C313.1),

`x^T (B')^{-1} x = 1 - 2 z^T C^{-1} z.`                           (C314.1)

Consequently

`N(B) = 2 * #{ z in {0,1}^{m-1} : z^T C^{-1}z in {0,1} }.`        (C314.2)

For each `z`, Schur complementation gives

`det [[C,z],[z^T,t]] = det(C) (t-z^T C^{-1}z).`

Hence (C314.2) is equivalently

`N(B)/2 = #{(z,t) in {0,1}^{m-1} x {0,1} : [[C,z],[z^T,t]] is singular}.`  (C314.3)

So `N(B)/2` is **exactly the number of singular one-vertex children of the invertible symmetric `0/1` core `C`**.

#### Proof of (C314.1)

From `L B' L^T=diag(1,-2C)`,

`(B')^{-1}=L^T diag(1,-(1/2)C^{-1}) L`.

For `x=(1,1-2z)`, `Lx=(1,-2z)`. Substitution gives

`x^T(B')^{-1}x = 1 + (-2z)^T[-(1/2)C^{-1}](-2z) = 1-2z^TC^{-1}z`.

The remaining statements follow immediately. QED.

This is the promised same-object double count: inverse-quadratic richness and singular-child multiplicity are identical after switching normalization.

## 5. Method #30 — all coranks reduce to the same first moment

For `1<=k<=n-1`, write `m=n-k`. For an invertible symmetric sign `m x m` core `B`, define

`N_k(B) := #{ X in {+-1}^{m x k} : X^T B^{-1}X is a symmetric sign k x k matrix }`,

and put `N_k(B)=0` if `B` is singular.

### C315 — k-vertex Schur count

For the random symmetric sign matrix `A_n`,

`P(corank A_n = k)
 <= C(n,k) 2^{-[mk+k(k+1)/2]} E N_k(B_m).`                         (C315.1)

Moreover

`N_k(B) <= N(B)^k <= 2^{m(k-1)}N(B)`,                              (C315.2)

and therefore

`P(corank A_n = k)
 <= C(n,k) 2^{-n-k(k-1)/2} E N(B_{n-k}).`                          (C315.3)

#### Proof

Fix a `k`-set `S` of deleted coordinates. Conditional on the complementary principal minor `B=A[S^c,S^c]` being invertible, write

`A = [[B,X],[X^T,C_S]]`,

where `X` is an independent uniform sign `m x k` matrix and `C_S` is an independent uniform symmetric sign `k x k` matrix. Schur complementation gives

`corank(A)=corank(C_S-X^T B^{-1}X)`.

Thus, when `B` is invertible, `corank(A)=k` iff

`C_S = X^T B^{-1}X`.

For each `X` counted by `N_k(B)`, exactly one of the `2^{k(k+1)/2}` possible `C_S` works. Hence the fixed-`S` probability is

`2^{-[mk+k(k+1)/2]} E N_k(B_m)`.

Every real symmetric matrix of rank `m` has a nonsingular principal `m x m` minor. One short proof is to use the characteristic polynomial: when rank is exactly `m`, the product of its nonzero eigenvalues is nonzero and equals, up to sign, the sum of all principal `m x m` minors, so at least one is nonzero. Union-bound over the `C(n,k)` possible deleted sets to obtain (C315.1).

If `X=[x_1 ... x_k]` is counted by `N_k(B)`, then every diagonal entry `x_j^T B^{-1}x_j` is a sign, so every column `x_j` belongs to the `N(B)`-set. Hence `N_k(B)<=N(B)^k`. Since `N(B)<=2^m`, (C315.2) follows. Substitution into (C315.1), using `m=n-k`, gives (C315.3). QED.

The significance is that no separate sharp high-corank theorem is needed for this route: every exact corank is dominated by the **same first moment** `E N(B_m)`.

## 6. C316 — source conjecture iff average richness is subexponential

### Theorem

The following two statements are equivalent:

1. `q_n^sym = P(det A_n=0) = 2^{-n+o(n)}`;
2. `E N(B_m) = 2^{o(m)}` for the random symmetric sign core `B_m`.

#### (1) => (2)

Run 50 proved the exact weighted corank-one identity

`E[s(A_n) 1_{corank A_n=1}] = n 2^{-n} E N(B_{n-1}),`              (C311)

where `s(A_n)` is the support size of the one-dimensional kernel. Since `s(A_n)<=n`,

`E N(B_{n-1})
 = (2^n/n) E[s(A_n)1_{corank=1}]
 <= 2^n q_n^sym
 = 2^{o(n)}.`

Thus (2) follows.

#### (2) => (1)

Sum (C315.3) over coranks. For `1<=k<=n/2`, `m=n-k>=n/2`, so the assumed `E N(B_m)=2^{o(m)}` is uniformly `2^{o(n)}` over this range. Hence

`sum_{k<=n/2} P(corank A_n=k)
 <= 2^{-n+o(n)} sum_{k<=n/2} C(n,k) 2^{-k(k-1)/2}.`

The final sum is `2^{O((log n)^2)}=2^{o(n)}`: for example use `C(n,k)<=n^k`, so the exponent `k log_2 n-k(k-1)/2` is maximized at `k=O(log n)`.

For `k>n/2`, use only the trivial `E N(B_{n-k})<=2^{n-k}` in (C315.3):

`P(corank A_n=k) <= C(n,k) 2^{-k(k+1)/2}`,

whose sum over `k>n/2` is `2^{-Omega(n^2)}`.

Therefore

`q_n^sym <= 2^{-n+o(n)}.`

For the reverse inequality, fix one pair of rows. Equality of that pair has probability exactly `2^{-n}`, and opposition has probability exactly `2^{-n}`: the `n-2` outside coordinates contribute `2^{-(n-2)}` and the three entries on the two diagonal/cross positions contribute `1/4`. These events are disjoint, so

`q_n^sym >= 2^{1-n}.`

Thus `q_n^sym=2^{-n+o(n)}`. QED.

This is a source-level equivalence/reduction, **not a solution**: the missing theorem is now precisely

`boxed{ E N(B_m) = 2^{o(m)} }.`

By C314, the same statement says that the expected number of singular one-vertex extensions of a random invertible symmetric `0/1` core is subexponential.

## 7. Exact finite certificate: richness after switching normalization

Only after the structural reduction was obtained did I build a finite checker. It enumerates every switching-normalized symmetric `0/1` core through `m=6`, uses integer Leibniz determinants/adjugates only, and verifies C314 exactly.

Artifacts:

- `artifacts/R03/20260918T0510Z_51_f0002_normalized_richness_exact.py`
- `artifacts/R03/20260918T0510Z_51_f0002_normalized_richness_exact.out`

The exact output ends `EXACT_CHECK_PASS`. The distributions over all normalized cores are:

- `m=1`: `{2:1}`, `E N=2`;
- `m=2`: `{4:1}` over the one invertible core among two, `E N=2`;
- `m=3`: `{6:4}` over four invertible cores among eight, `E N=3`;
- `m=4`: `{8:8,12:24}`, `E N=11/2`; multiplying normalized counts by the exact fiber size `2^4` recovers run 50's full-sign counts `128` and `384`;
- `m=5`: `{10:31,12:60,16:20,18:225,20:192}`, `E N=1155/128`;
- `m=6`: `{12:401,14:120,16:900,18:360,20:570,22:720,24:3870,26:1080,28:405,30:480,32:540,34:1440,36:2790,38:3600,40:1260,48:60}`, `E N=69759/4096`.

These small dimensions show that rich cores are real and pointwise uniqueness is the wrong target. They do **not** justify any asymptotic fit.

The code artifact was created at commit `07c9f4dc5a5601328bfcbede6126d67c0510cbbc`; the archived exact output was created at commit `4f886e43e4c3440521d77237c460c9ef7ec0e428`. Both were read back. The same exact enumeration was also independently reexecuted in this runtime before this report was written; all displayed counts and fractions agreed.

## 8. What moved, what did not, and the next route

The frozen source metric did not move:

`gamma_sym : POSITIVE_UNMEASURED -> POSITIVE_UNMEASURED`.

Status remains **OPEN / PARTIAL**. I do not manufacture a decimal exponent from an unspecified literature constant.

What did move structurally:

1. symmetric sign singularity is exactly switching-equivalent to symmetric `0/1` singularity one dimension lower (C313);
2. inverse-quadratic richness is exactly singular-child multiplicity in those normalized coordinates (C314);
3. every exact corank is controlled by the same first moment `E N` (C315);
4. the entire source base-`1/2` conjecture is equivalent to the single average statement `E N(B_m)=2^{o(m)}` (C316).

The prior pointwise route is dead; the correct object is the **typical-core richness tail**

`H_m(t)=P(N(B_m)>=t, det B_m !=0)`

or equivalently the distribution of singular-child counts for random invertible symmetric `0/1` cores.

Next methods, deliberately different from both F0002 triples used so far:

- **#5 ADD A PARAMETER:** interpolate the child diagonal bit / edge density and differentiate the average singular-child count;
- **#18 SAY IT IN ANOTHER LANGUAGE:** view C314 as an edge-boundary/branching statistic in the graded graph of symmetric `0/1` matrices under one-vertex extension;
- **#28 REPLACE FOR ALL WITH TYPICAL:** seek a high-probability `N(B)<=2^{o(m)}` theorem plus a separately controlled rare-rich tail, rather than any false pointwise bound.

The most concrete next objective is a quantitative dyadic-tail estimate strong enough that

`sum_j 2^j H_m(2^j) = 2^{o(m)}`.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R03
  target: F0002
  allocation: HARD_OUTSIDE
  source_status: OPEN
  worker_status: PARTIAL
  metric: gamma_sym
  before: POSITIVE_UNMEASURED
  after: POSITIVE_UNMEASURED
  movement: NO_MOVEMENT
  stagnation_count: UNKNOWN
  methods_this_run: [25, 30, 15]
  new_claims: [C313, C314, C315, C316]
  exact_finite_certificate: artifacts/R03/20260918T0510Z_51_f0002_normalized_richness_exact.py
  exact_output: artifacts/R03/20260918T0510Z_51_f0002_normalized_richness_exact.out
  next_methods: [5, 18, 28]
  predecessor_F0001: HANDOFF_PRESERVED
  predecessor_F0097: HANDOFF_PRESERVED
```

`stagnation_count` stays `UNKNOWN` because the F0002 claim/report did not establish a frozen numeric streak value; I do not invent or reset it.

No shared root, peer file, scheduler, permission, email, Drive item, public posting, purchase or workflow state was changed.

## 10. Model / scheduler limitation

The exposed scheduled-task control surface still has no model-family or reasoning-effort selector and no authenticated applied-run telemetry. GPT-6/maximum can therefore only be requested in prompt text from this surface. Enforcing it would require an authorized product/backend scheduler surface exposing those fields and returning authenticated runtime metadata. Historical task-modification denials such as P26 are authorization-context boundaries; the legitimate remedy is the owning/authorized context or platform support, not permission bypass or duplicate schedules.

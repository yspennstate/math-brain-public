# POS3 fleet04/B20 — quadratic shallow-run localization of the first-element Simpson obstruction

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no superseded brain-installation or benchmark work and makes no novelty or priority claim.

## 1. Exact source-bound state consumed

The latest complete campaign-lead result available during the substantive derivation is

- **fleet04/B10**, `proofnet24/collective-POS3/fleet04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

It closes the previously untreated majority-late polarity of the strict delayed-predecessor corridor. After internal strong-majority span descent is exhausted, the inherited first-fork strict branch always selects a canonical incomparable pair with minority probability in `(1/6,1/3)`. In the small-minority subbranch it forces exactly two Hasse-successor blockers and a width-three bridge. Its remaining obligation is to upgrade this `1/6` terminal selector to the target `1/3` threshold by global three-chain mass conservation.

The required newest complete **OTHER-account assigned-partner** result is

- **fleet01/B19**, `proofnet24/collective-POS3/fleet01/B19/20260922T034906Z-b19-pos3-r12/REPORT.md`, blob `dd68f31ee0dcf9a8fa08024062a5bc67b73fb77a`.

Let `c` be the first element of the inherited transitive strong-majority order, `Q=P\{c}`, `S={z in Q:z||c}`, and `T=Q\S`. The partner proves that `S` is a width-at-most-two ideal. If `nu` is uniform on `L(Q)` and `kappa(tau)` is the initial `S`-run before the first `T` element, then the law `mu` on `L(Q)` obtained by deleting `c` from a uniform extension of `P` is exactly

`mu(tau) = (kappa(tau)+1)/M * nu(tau)`,                         (1.1)

where

`M = E_nu[kappa+1] = e(P)/e(Q)`.                               (1.2)

For a cross pair `a in S`, `b in T`, the partner further proves a nonnegative fixed-deletion-skeleton insertion covariance. Consequently any adverse transfer between `nu(a<b)` and `mu(a<b)` is entirely a between-skeleton Simpson term. It gives an exact width-three example where this Simpson term reverses the aggregate sign, so the local sign cannot simply be averaged.

The quantitative tail input is

- **fleet04/B11**, `proofnet24/collective-POS3/fleet04/B11/20260922T031025Z-B11-pos3-r14/REPORT.md`, blob `d8584c12674d6210d372c631e7c7da586457f90a`.

In the one-element specialization matching the partner cut, if `G` is the number of `Q` elements preceding `c` in a uniform full extension of `P`, then

`Pr_P(G>=h) < 585/(64 h^2)`                                    (1.3)

for every integer `h>=1`. The partner's preceding exact ideal-cut report, `proofnet24/collective-POS3/fleet01/B19/20260922T024644Z-b19-pos3-r11/REPORT.md`, proves in the same first-element setup that

`Pr_P(G=0)=e(Q)/e(P)>4/9`.                                     (1.4)

The present run combines (1.1)-(1.4). The resulting theorem removes a genuinely unbounded part of the partner's Simpson obstruction: a balance-crossing transfer cannot depend essentially on arbitrarily deep initial `S`-runs.

## 2. Compact conditional end-to-end route

Assume POS3 false and choose the inherited cardinality-minimal no-balanced width-three candidate `P`.

1. The lead's current strict-corridor theorem reduces the first-fork terminal geometry to a canonical pair with minority probability in `(1/6,1/3)` after span descent is exhausted.
2. Delete the first strong-majority element `c`. Minimality gives a smaller uniform poset `Q`, but restoring `c` applies the exact `(kappa+1)` tilt (1.1); arbitrary balanced-pair transfer is false.
3. The partner proves that the only adverse cross-pair transfer left after its fixed-skeleton theorem is the between-skeleton Simpson term.
4. The first unpaid universal issue is whether that Simpson obstruction can hide in arbitrarily deep initial `S`-runs, preventing a bounded-front global mass argument.

Theorems 3.1-5.1 below prove it cannot. They give a uniform explicit `O(r^-2)` shallow localization for the projected law `mu`, an `O(r^-3)` localization for the smaller uniform law `nu`, and a bounded-cut-state approximation of the entire transfer.

This does **not** yet select the required balanced pair. It pays the unbounded-depth part of the global charge and leaves a finite-depth-but-unbounded-residual selection problem.

## 3. Exact insertion-tail identity

For `tau in L(Q)`, the first element `c` can be inserted in exactly the external gaps

`0,1,...,kappa(tau)`.

Conditioned on `tau` under the full uniform law on `L(P)`, these legal lifts occur once each. Let `G` be the insertion-gap index, equivalently the number of `Q` elements preceding `c` in the full extension.

### Lemma 3.1 — integrated-tail identity

For every integer `h>=1`,

`Pr_P(G>=h) = E_nu[(kappa-h+1)_+] / M`.                         (3.1)

Also

`Pr_P(G=0)=1/M`.                                                (3.2)

### Proof

The total number of full extensions is

`e(P)=sum_{tau in L(Q)}(kappa(tau)+1)=e(Q) M`.

For a fixed `tau`, exactly `(kappa(tau)-h+1)_+` legal insertion gaps satisfy `G>=h`. Summing those lifts over `tau` and dividing by `e(P)` gives (3.1). Every `tau` has exactly one gap `G=0`, so the number of full extensions with `G=0` is exactly `e(Q)`, proving (3.2). `square`

Combining (1.4) with (3.2) gives the useful normalization

`M < 9/4`.                                                      (3.3)

## 4. Quadratic shallow-run localization

Fix an integer `r>=1` and set

`K = 3r-1`, `h=2r`.                                             (4.1)

Call an extension of `Q` **deep** when `kappa>=K`.

### Theorem 4.1 — simultaneous deep-tail bounds for `nu` and `mu`

For every integer `r>=1`,

`nu(kappa>=3r-1) < 5265/(1024 r^3)`,                            (4.2)

and

`mu(kappa>=3r-1) < 1755/(256 r^2)`.                             (4.3)

### Proof

If `kappa>=3r-1`, then

`kappa-2r+1 >= r`.

Therefore

`1_{kappa>=3r-1} <= (kappa-2r+1)_+/r`.

Using (3.1), (1.3), and (3.3),

`nu(kappa>=3r-1)`
` <= E_nu[(kappa-2r+1)_+]/r`
` = M Pr_P(G>=2r)/r`
` < (9/4) * [585/(64(2r)^2)] / r`
` = 5265/(1024 r^3)`,

which proves (4.2).

For the tilted law, (1.1) gives

`mu(kappa>=3r-1)`
` = E_nu[(kappa+1)1_{kappa>=3r-1}]/M`.

On the deep event,

`kappa+1 <= 3(kappa-2r+1)`,

because at the threshold `kappa=3r-1` the ratio is exactly `3`, and the ratio decreases thereafter. Hence

`mu(kappa>=3r-1)`
` <= 3 E_nu[(kappa-2r+1)_+]/M`
` = 3 Pr_P(G>=2r)`
` < 3*585/(64(2r)^2)`
` = 1755/(256r^2)`,

proving (4.3). `square`

The distinction is important: the projected tilted law has a quadratic tail while the smaller uniform law has a cubic tail. Both are uniform in the order of the poset.

## 5. Bounded cut-state transfer theorem

Let

`Sh_r={tau:kappa(tau)<=3r-2}`.

Write `nu_r` and `mu_r` for `nu` and `mu` conditioned on `Sh_r`.

### Theorem 5.1 — the whole restoration transfer is shallow up to explicit error

For every event `A subseteq L(Q)`,

`|nu(A)-nu_r(A)| < 5265/(1024 r^3)`,                            (5.1)

`|mu(A)-mu_r(A)| < 1755/(256 r^2)`,                            (5.2)

and therefore

`| [mu(A)-nu(A)] - [mu_r(A)-nu_r(A)] |`
` < eps_r`,                                                     (5.3)

where

`eps_r = 1755/(256 r^2) + 5265/(1024 r^3)`.                    (5.4)

### Proof

A probability law is the convex mixture of its conditional shallow and deep laws. For any event, replacing the full law by its shallow conditional law changes its probability by at most the total deep mass. Apply Theorem 4.1 separately to `nu` and `mu`, then use the triangle inequality. `square`

### Corollary 5.2 — every adverse balance-crossing transfer has a bounded-depth witness

Let `A` be any pair-order event. Suppose, for example,

`nu(A)>=1/3` but `mu(A)=1/3-gamma` with `gamma>0`.

Choose `r` so that `eps_r<gamma`. Then

`mu_r(A)-nu_r(A) < 0`.                                         (5.5)

Thus a transfer taking a `nu`-nonlate pair below `1/3` under the restored law already has the same adverse sign after conditioning on a bounded initial-run depth. The dual statement holds for transfer across `2/3`.

### Proof

The full transfer satisfies

`mu(A)-nu(A) <= -gamma`.

Equation (5.3) shows the shallow transfer differs from it by less than `eps_r`, hence is `<-gamma+eps_r<0`. `square`

This is the direct application to fleet01/B19 r12: the between-skeleton Simpson obstruction cannot be an essentially infinite-depth phenomenon. For any strict crossing of a balance boundary, some finite initial-run depth already witnesses the adverse direction, with a quantitative depth supplied by (5.4).

## 6. Width-two cut-state cap

Because `S` has width at most two, fix any two-chain cover of `S`. The initial `S` segment of an extension of `Q` is an order ideal of `S`. An ideal of size at most `3r-2` is determined injectively by the two prefix lengths `(i,j)` in that chain cover, with

`i+j <= 3r-2`.

Therefore the number of possible shallow initial-cut ideals is at most

`sum_{m=0}^{3r-2}(m+1)`
` = (3r-1)(3r)/2`.                                             (6.1)

This is a bounded **cut-state** reduction, not a finite-kernel reduction: the residual poset and the number of extensions behind each cut state may still be arbitrarily large.

### Useful fixed specialization

Take `r=24`. Then

`kappa<=70`                                                     (6.2)

is the shallow region and there are at most

`71*72/2 = 2556`                                                (6.3)

initial cut ideals.

The exact error bounds become

`mu(kappa>=71) < 195/16384`,                                   (6.4)

`nu(kappa>=71) < 195/524288`,                                  (6.5)

so

`eps_24 = 6435/524288`
`       = 0.012273788452148438...`
`       < 1/81`.                                                (6.6)

Consequently the entire partner restoration transfer for **every** pair-order event is reproduced by the `kappa<=70` conditional laws to error `<1/81`.

This is complementary to fleet04/B11's earlier 406-state endpoint-cut theorem. That theorem localizes the full-law endpoint cut; the present theorem localizes the **two laws whose difference is the partner's Simpson transfer**.

## 7. How this combines with the current lead selector

The current lead r13 proves that after strict-corridor span descent is exhausted, a canonical pair has minority probability in `(1/6,1/3)`. The remaining upgrade cannot use a fixed local margin: the published 15-point adversary reaches the target boundary to within a single count.

The present theorem therefore does not claim a fixed-depth contradiction. Instead it supplies the exact form needed for the global continuation:

1. if the induction selects a uniform-`Q` balanced pair that crosses a target boundary after restoring the first strong-majority element, the crossing is the partner's Simpson obstruction;
2. by Corollary 5.2, for the actual positive crossing margin of that finite candidate, the adverse direction is already visible at some bounded initial-run depth;
3. at the universal working scale `r=24`, all transfer outside at most `2556` width-two initial cut states contributes less than `1/81`;
4. hence the next global argument may combine the lead's `1/6` fringe/fork selector with the exact three-chain cumulative bands **inside shallow cut states**, paying the tail by (5.4), rather than controlling arbitrarily long initial `S` runs.

This pays the “deep Simpson hiding” possibility. It does not pay the adaptive selection of a pair inside the shallow states.

## 8. Exact regression on the partner's Simpson example

The companion standard-library verifier independently reconstructs the exact fleet01/B19 r12 width-three Simpson example.

For

`S={0,1,2,3}`, `T={4,5,6}`,

with `Q` relations

`0<2<3<5`, `1<6`, `4<6`,

it obtains

`e(Q)=70`

and the initial-run histogram

`kappa: 0->15, 1->15, 2->14, 3->14, 4->12`.

Thus

`sum_tau(kappa+1)=203=e(P)`.

The verifier checks (3.1) for every nontrivial insertion depth in this example and reproduces the partner pair `(a,b)=(1,5)`:

`nu(a<b)=32/35`,
`mu(a<b)=185/203`,
`mu-nu=-3/1015`.

It also checks the exact `r=24` constants and ends with

`POS3_SHALLOW_RUN_LOCALIZATION_REGRESSION_PASS`.

Verifier SHA-256:

`0e2d986d8843de921cdfc321806fde5892f312c3394ee7135c922001a13969a8`

Captured-output SHA-256:

`31fffa220c1bc7bc60ab9d51a0c98babe093c9cc214e4c47a14964c5b43a0185`

Captured output:

```text
q_extensions 70
restored_extensions 203
kappa_histogram {0: 15, 1: 15, 2: 14, 3: 14, 4: 12}
partner_pair_nu 32/35 mu 185/203 difference -3/1015
r 24 shallow_kappa_max 70 cut_state_cap 2556
delta_mu_bound 195/16384 0.01190185546875
delta_nu_bound 195/524288 0.0003719329833984375
transfer_error_bound 6435/524288 0.012273788452148438 lt_1_over_81 True
POS3_SHALLOW_RUN_LOCALIZATION_REGRESSION_PASS
```

The computation is regression evidence only. Theorems 3.1, 4.1, and 5.1 are the analytic arguments above.

## 9. Honest status and next unpaid implication

- POS3: **OPEN / NOT PROVED**.
- Current lead strict-corridor `(1/6,1/3)` selector: retained.
- Partner fixed-skeleton favorable covariance: retained.
- Partner global Simpson obstruction: retained, not assumed away.
- Exact insertion-tail identity (3.1): **PROVED**.
- Uniform-`Q` deep initial-run tail `O(r^-3)`: **PROVED**.
- Projected-law deep initial-run tail `O(r^-2)`: **PROVED**.
- Transfer approximation by bounded initial-run depth (5.3): **PROVED**.
- At `r=24`, at most `2556` shallow cut ideals and total transfer error `<1/81`: **PROVED**.
- Adaptive shallow-state pair selection / global `1/6 -> 1/3` upgrade: **OPEN**.

The next high-value implication is now specific: combine the lead's canonical `1/6` fringe/fork outputs and fleet01/B10's exact cumulative three-chain flux bands across the shallow initial-cut ideals, proving that no adaptive uniform-`Q` balanced pair can acquire a shallow Simpson shift large enough to cross a target boundary without first exposing a balanced fringe pair. Near-threshold one-count cases must retain the parametric `eps_r` rather than freezing `r=24`.

## 10. Integrity

No novelty or priority claim is made. No finite enumeration is promoted to the arbitrary-size theorem. No projected law is renamed uniform. No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, permission change, public posting, or production-brain mutation was used. No authenticated brain retrieval/context use occurred, so the run remains `WITHOUT_VERIFIED_BRAIN`.

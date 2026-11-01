# B20 synthesis — activation-weighted endpoint tax

**Full FEI status:** **OPEN**.  This run performs one source-bound cross-route substitution.  It does not prove or disprove FEI.

**Primary packet:** A097 (cross-route transfer).  **Secondary ledger packet:** A096.  A098–A100 remain open.

## 1. Reconciled incoming evidence

Only complete, saved records were admitted to the ledger.

| Result | Deliverable state | Mathematical state | Review state |
|---|---|---|---|
| B05 sparse-activation refutation of every fixed-price `L <= Kd+AV+BM` | SAVED | PROVED at stated scope | ACCEPTED by independent B19 reconstruction |
| B09 exact identity `L_A=M_A+J_A` and biased tax theorem | SAVED | PROVED in source report | full-source review pending |
| B09 tax-free helper `J_A<=M_A` for arbitrary biases | SAVED | REFUTED by a two-bit Boolean gate | signed interval certificate independently repaired and verified |
| Full FEI | no candidate | OPEN | no complete-chain reviews |

The corrected B09 certificate proves

\[
J_A-M_A>0.1195\ \text{bits}
\]

for the displayed biased two-bit gate.  The older helper is therefore retired at its original quantifiers.  This does not retire the endpoint-tax theorem

\[
J_A\le M_A+\Delta_A(p).
\]

No B10–B18 report was present in the canonical saved run tree at the inspected revision.  Local or configured work without an immutable saved record was not promoted into the aggregate ledger.

## 2. Nearest unpaid term

The independently accepted B05 family has, for even \(k\ge4\),

\[
\delta=2^{-k},\qquad p=2^{-2k},\qquad d=p\delta=2^{-3k}.
\]

Its selector-packet entropy \(L\) satisfies

\[
L/d=k+\log_2e+o(1),
\]

while its local payments obey

\[
V/d\to0,\qquad M/d\to0.
\]

Thus the unpaid quantity is the rare logarithm \(d\log_2(1/\delta)\).  The B05 result proves that no fixed linear combination of \(d,V,M\) supplies it.

## 3. PROVED cross-route substitution

For a one-bit B09 endpoint tax define

\[
\Delta(u)=h_2(u)+\log_2(1-u)
=u\log_2\frac{1-u}{u},\qquad 0<u\le\frac12.
\tag{3.1}
\]

The activation-weighted tax in the B05 parameters is

\[
p\Delta(\delta)
=d\log_2\frac{1-\delta}{\delta}
=d\bigl(k+\log_2(1-\delta)\bigr).
\tag{3.2}
\]

This has exactly the missing \(kd\) scale.  The following bound makes the transfer rigorous on the whole B05 witness family.

### Theorem B20-A097-ACTIVATION-WEIGHTED-ENDPOINT-TAX-v1

For every even \(k\ge4\), the B05 packet entropy satisfies

\[
\boxed{L<p\Delta(\delta)+3d.}
\tag{3.3}
\]

Together with B05's accepted lower bound,

\[
\boxed{
(1-\delta)d(k-2)\le L<p\Delta(\delta)+3d.
}
\tag{3.4}
\]

Hence the B09 endpoint tax, charged at the **inner defect probability** \(\delta\) and weighted by the **outer activation probability** \(p\), pays the B05 rare logarithm up to a dimension-free linear remainder.  Charging the tax at the total mismatch probability \(d\) would overpay by a factor approaching three; the two-scale placement is essential.

### Proof

For one packet put \(e=q\theta\).  The elementary inequality

\[
(1-\theta)\log_2\frac1{1-\theta}\le\theta\log_2e
\]

gives

\[
q h_2(\theta)
\le e\left(\log_2\frac qe+\log_2e\right).
\tag{3.5}
\]

Use the exact four-class packet description from the accepted B05 proof.

1. For nonempty data frequency, total mismatch mass is \((1-\delta)d\), and
   \[
   \frac qe=\left(\frac{c_T}{\delta}-1\right)^2+1
   \le\frac2\delta,
   \]
   since \(|c_T|=\sqrt\delta\) and \(\delta\le1/16\).
2. For empty data and nonempty control frequency, total mismatch mass is less than \(\delta d\), and \(q/e\le2/\delta^2\).
3. The all-empty packet has mismatch mass \(d^2\), and \(q/e\le2/d^2\).

Summing (3.5) therefore yields

\[
\frac Ld
\le (1-\delta)(k+1+\log_2e)
+\delta(2k+1+\log_2e)
+d(6k+1+\log_2e).
\tag{3.6}
\]

Subtract (3.2) divided by \(d\).  The remaining upper bound is

\[
1+\log_2e+\delta k+d(6k+1+\log_2e)-\log_2(1-\delta).
\tag{3.7}
\]

For even \(k\ge4\), use

\[
\log_2e<\frac32,quad
\delta k\le\frac14,quad
d(6k+1+\log_2e)<\frac1{64},quad
-\log_2(1-\delta)<\frac18.
\]

Their sum in (3.7) is less than \(3\), proving (3.3).  The last two bounds are maximal at \(k=4\); monotonicity thereafter is immediate.  No unreviewed B09 universal theorem is used in this proof—only the scalar tax (3.1), rederived on the page.

## 4. Exact amount paid and exact unmatched hypothesis

Before this run, the tracked B05 debt was

\[
d\log_2(1/\delta)+O(d),
\]

with local credit only \(Kd+o(d)\).  After substitution, the family-specific debt is fully paid by

\[
p\Delta(\delta)+3d.
\]

The remaining universal obstruction is **not a constant calculation**.  It is a lifting problem:

> Given a rare defect of conditional probability \(\delta\) inside an activated piece of probability \(p\), construct a physical, nonreusing ledger that creates the credit \(p\Delta(\delta)\) once and transports it to the selector packet entropy, even when the activation/defect variables overlap the spectral source.

Why B09 cannot simply be invoked universally: its product-biased block theorem concerns a physical product coordinate or disjoint composition input.  In the B05 witness, the defect event and bent source share the data variables.  Treating the defect indicator as a fresh biased coordinate changes the joint law and silently removes shared-variable interference.  Thus (3.3) proves an exact currency match on the obstruction family, but universal promotion is **CONDITIONAL** on a new overlap-safe lifting lemma.

This diagnosis survives the required stress suite:

- **Rare restrictions/sparse defects:** (3.3) is proved on the accepted B05 bent-defect family.
- **Addressing:** the tax must be charged to a joint piece, not coordinatewise; otherwise the whole-set address label is multiplied spuriously.
- **Near tensors:** both sides of (3.3) retain the rare logarithm; no fixed-Rényi or quadratic replacement is made.
- **Prime gates:** the repaired biased AND witness forbids removing \(\Delta\); any lifting must retain a positive tax at nonuniform bias.
- **Shared variables/activation equivalence:** this is precisely the unmatched hypothesis, not assumed away.

## 5. Certificate

`check_cross_route.py` reconstructs all four B05 packet classes with exact rational arithmetic.  Logarithms use a 48-term rational atanh expansion plus a rigorous geometric tail.  It checks every even \(k=4,6,\ldots,40\):

- exact total packet mass \(1\);
- exact mismatch mass \(d\);
- the classwise upper bound (3.6);
- the strict payment \(L<p\Delta(\delta)+3d\).

There are 76 proof-relevant assertions, all passing; randomness is absent.  Representative outputs include

\[
L/d=5.48827457\ldots<6.90689059\ldots
\]

at \(k=4\), and

\[
L/d=41.44269504\ldots<42.99999999\ldots
\]

at \(k=40\).  Decimal renderings are display-only; assertions compare rational interval endpoints.

Command:

```bash
python3 runs/B20/20261011T201744Z-97f1225a/check_cross_route.py
```

## 6. Claim/dependency delta

- **Added, PROVED:** `B20-A097-ACTIVATION-WEIGHTED-ENDPOINT-TAX-v1`, equation (3.3), for the exact B05 family.
- **Dependency:** accepted `B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO-v1`, report blob `1b7e3cb572354cac4e506d7de0a3ed8af720472b`, independently accepted by B19 report blob `dcec4cb77233a7b233b4798b25aab5f2dd5c82b6`.
- **Scalar input rederived:** one-bit endpoint tax (3.1), appearing in B09 report blob `71b68e4decf9658a42fef6bb2668e19f25bd214a`.
- **Retired helper:** tax-free biased `J_A<=M_A`, refuted by the repaired interval packet blob `c3adb486c8ca9f7a35f384ee82942eef66bd64be`.
- **Open dependency:** overlap-safe, single-use lifting of \(p\Delta(\delta)\) to physical shared-variable decompositions.

## 7. Distinct next actions

- **B05/A023:** replace the refuted local `d,V,M` payment by an explicit tree ledger carrying \(p\Delta(\delta)\) from the rare child to its selector ancestor exactly once.
- **B06/A027:** formulate a stopping rule whose state records both activation probability \(p\) and conditional defect probability \(\delta\); test recursive ternary majority.
- **B08/A037:** derive the normalized-prior KL identity whose scalar specialization is \(p\Delta(\delta)\), with a no-reuse invariant.
- **B09/A041:** complete an independent source audit of the biased uncertainty theorem and optimize the one-bit Boolean-realizable tax without reviving the refuted tax-free helper.
- **B12/A058:** prove or falsify an overlap-safe composition lemma when the defect indicator shares variables with the source phase.
- **B17/A081:** formalize (3.3) and the proposed lifting interface; distinguish the exact B05 family theorem from the universal conditional statement.
- **B18/A090:** independently review (3.3), especially the four packet-class bounds and the placement of the weight \(p\).
- **B19/A094:** adversarially test the lifting hypothesis on addressing, reused selectors, and activation-equivalent representations.
- **B20/A096:** on the next synthesis pass, ingest only new complete saved deltas and propagate any refutation of the lifting interface.

## 8. Sources, execution, and delivery

Current open-problems revision read: `034ae6a0fe7388b61bcb5530513fbff1b02ef153`.

Key file blobs read:

- `AGENT_ASSIGNMENTS.json`: `e7c102daaf5dccdeb75c3440d2e5ab92b608e5f1`;
- `STREAM_NEXT_ACTIONS.json`: `2ec748b1ac9e30aae0d649016fe5fb3ed095059e`;
- `PACKET_PROGRESS.json`: `5c669dc00deeed81f04d75495add7dc3a8a8c4cc`;
- `CURRENT_STATUS.md`: `b464144b019197f00b821ff9a062856e7473a7ee`;
- `README.md`: `fe56dc6541fafb849b67b6a0496ce516e4e7eca0`.

Lifecycle:

- configured: B20 owns A096–A100;
- invoked/performed: A097 mathematical cycle plus A096 ledger update;
- validated: analytical proof and 76/76 rational-interval assertions;
- saved to canonical private repository: **NO**;
- Brain mirror: **NO**;
- independent review: pending A090/A094;
- native Brain ingestion: not run;
- full-FEI candidate: no.

The standing repository/Brain write restriction was preserved and not probed or bypassed.  This local directory is a nondurable handoff only; no remote commit or readback is claimed.  No schedules, workers, accounts, notifications, public files, or protected evaluation material were changed or accessed.

Exposed runtime identity: Codex.  A precise model-version/effort selector, billing identity, and remaining allowance were not exposed and are not asserted.


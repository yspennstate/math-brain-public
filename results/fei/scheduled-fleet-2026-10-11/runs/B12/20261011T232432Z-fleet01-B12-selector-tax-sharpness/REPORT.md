# B12 / A060 run report: exact selector-tax sharpness

- Run: `20261011T232432Z-fleet01-B12-selector-tax-sharpness`
- Primary packet: `A060` (Composition sharpness)
- Stable gap: `FEI-B12-A060-SELECTOR-TAX-SHARPNESS`
- Attempt: `B12-A060-ATTEMPT-001`
- Claim: `B12-A060-SELECTOR-TAX-SHARPNESS-v1`
- Exact-scope status: **PROVED** (finite Boolean witness and analytic tensor consequence)
- Packet status: **DELIVERED_FOR_REVIEW**, not accepted or complete
- Full FEI status: **OPEN**

## Bounded objective and prior state

The objective was to determine whether the scalar selector overhead implicit in
the B12 splice ledger could have coefficient (4), and to distinguish a lower
bound for that local additive tax from a multiplicative FEI-class lower bound.

The previous tracked value for this A060 quantity was **OPEN / no exact lower
bound recorded**.  The preceding A058 reports proved restricted composition
upper bounds but did not supply a Boolean witness forcing a coefficient for the
standalone term

\[
H(K)-\frac12H(D) \quad\hbox{versus}\quad I_x(K)
\]

in a constant-versus-(D) splice.  This run is a sharpness audit of that
existing composition interface, not a third broad composition theorem.

## New exact witness

Define

\[
D(z_1,z_2)=1-2\mathbf 1_{\{z_1=z_2=-1\}},\qquad
K(x,z_1,z_2)=1-2\mathbf 1_{\{x=z_1=z_2=-1\}}.
\]

Thus (K(+1,z)=1) and (K(-1,z)=D(z)).  The selector (x) is fresh, while
the two branches are nonorthogonal:

\[
\langle 1,D\rangle=\mathbb E D=\frac12.
\]

### PROVED: exact Fourier ledger

Direct expansion gives

\[
D=\frac12+\frac12z_1+\frac12z_2-\frac12z_1z_2.
\]

Hence all four squared Fourier masses of (D) are (1/4), so

\[
H(D)=2,\qquad I(D)=1,\qquad \mathbb E D=\frac12.
\]

For (K), the constant coefficient is (3/4), and each of the seven
nonconstant coefficients has magnitude (1/4).  Therefore

\[
H(K)=\frac9{16}\log_2\frac{16}{9}+\frac74,
\qquad I(K)=\frac34,
\qquad I_x(K)=\frac14.
\]

It follows exactly that

\[
c_0:=\frac{H(K)-\tfrac12H(D)}{I_x(K)}
=12-\frac94\log_2 9
\in(4.867,4.868).
\]

Thus the following helper is **REFUTED**:

> For every Boolean (D), if (K(+1,z)=1) and (K(-1,z)=D(z)), then
> (H(K)\leq H(D)/2+4I_x(K)).

More generally, any universal inequality of precisely this scalar form must
have (c\geq c_0).  This witness is an actual three-bit Boolean gate; no
weighted relaxation or limiting argument is involved.

## Additive tax is not an FEI lower bound

For the same gate,

\[
\frac{H(K)}{I(K)}
=\frac{16}{3}-\frac34\log_2 9
\in(2.955,2.956).
\]

If (K^{\otimes m}) is the product of (m) copies on disjoint coordinate
blocks, its squared Fourier law is the product probability law.  Consequently

\[
H(K^{\otimes m})=mH(K),\qquad I(K^{\otimes m})=mI(K),
\]

and its FEI ratio remains
(16/3-(3/4)\log_2 9\), not (c_0).  The coefficient (c_0) is therefore
a necessary coefficient for one local additive decomposition term, while the
tensor-stable multiplicative lower bound supplied by this class is only about
(2.956).  This is the exact additive-versus-multiplicative distinction
requested by A060.

## Verification

`check_selector_tax_sharpness.py` uses integer Walsh transforms to certify the
spectra.  It bounds (\ln 2) and (\ln 3) by rational truncations of

\[
\ln y=2\sum_{k\geq0}\frac{t^{2k+1}}{2k+1},\qquad
t=\frac{y-1}{y+1},
\]

with an explicit positive geometric tail.  There is no randomness.

Command:

```text
TIMEFORMAT='real %3R\\nuser %3U\\nsys %3S'; time python3 check_selector_tax_sharpness.py
```

Observed bounded-pilot runtime: 0.039 seconds under Python 3.12.14.  The
certificate proves

```text
4.867668746754797183458174752234825705904 < c0
  < 4.867668746754797183458174752234825710597,
2.955889582251599061152724917411608568635 < H(K)/I(K)
  < 2.955889582251599061152724917411608570199.
PASS
```

The script and complete captured output are included.

## Counterexample and scope audit

- **Actual prime Boolean gate:** yes; (D) is a two-bit point defect and
  (K) a three-bit point defect.
- **Fresh selector:** yes.
- **Neighboring orthogonality:** no; the branch inner product is (1/2).
- **Rare restrictions / sparse defects:** the gate is a finite sparse defect,
  with all probabilities and logarithmic costs kept exactly.
- **Near tensors:** disjoint tensor powers were analyzed exactly; they preserve
  the smaller FEI ratio and do not amplify the local tax.
- **Parity-zero erasure:** absent; the nonzero means and correlation are
  explicit.
- **Whole-set addressing:** not invoked; this witness neither proves nor
  refutes an addressing payment.
- **Shared-variable interference:** not claimed.  The disjoint tensor identity
  does not imply the refuted `OVERLAP_PRODUCT` law.
- **Activation equivalence:** no selector energy is counted twice; the physical
  selector influence is exactly (1/4).

## Claim and dependency delta

New exact claim:

`B12-A060-SELECTOR-TAX-SHARPNESS-v1` — for the displayed (D,K),

\[
\frac{H(K)-H(D)/2}{I_x(K)}=12-\frac94\log_2 9>4.867,
\]

while (H(K)/I(K)=16/3-(3/4)\log_2 9), and disjoint tensor powers preserve
the latter ratio.

Dependencies are only normalized Walsh expansion, Shannon entropy of a finite
probability vector, Fourier influence, and disjoint product factorization.  No
open or refuted campaign claim is used as a premise.  The earlier A058 work is
used solely to identify the scalar composition term being audited.

## Acceptance accounting

Met in this artifact:

- an exact genuine-Boolean sharpness example;
- exact (H,I), means, selector influence, and branch correlation;
- a rigorous coefficient lower bound for the stated local helper;
- explicit separation between local additive improvement and tensor-stable
  multiplicative FEI ratio;
- deterministic, archived, reproducible certificate.

Still missing for packet acceptance:

- independent full-source reconstruction by `A090`;
- independent full-source reconstruction by `A091`;
- registry reconciliation by `B20`.

No independent review was observed in this run.  The result does not complete
A060 until its contract's review evidence exists.  It does not solve full FEI.

## Exact sources read and used

- `CURRENT_STATUS.md`, blob
  `8c9c63579ecdd4afa385bb94caf79ee6296addcf`.
- `STREAM_PACKET_INDEX.json`, blob
  `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- `assignments/B12.json`, blob
  `40935ac651643a17815d0addf664ec4c1c0313cc`.
- `EXECUTION_PROTOCOL.json`, blob
  `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- `PACKET_STATUS.json`, blob
  `3a5ca0894678a9fd9908aae9596923d3038a03f8`.
- `CLAIM_REGISTRY.json`, blob
  `6a3e1aa94f81ec01841a083c97449739b9e72baa`.
- `OBSTRUCTION_REGISTRY.json`, blob
  `dd482025647aed25166b46cc217a7ed77dcaa767`.
- Prior B12 report
  `runs/B12/20261011T221926Z-fleet01-B12-effective-support-v2/REPORT.md`,
  open-problems commit `95656134e2a6938fe46bbbcab713f5628156391b`,
  blob `5c4617a30ac16c2ebf114e53e4830163b61b4c65`; mirrored at Brain commit
  `274bab188e13dc16e06ef944dec2839ad90ebe64`.
- Recovered bent-splice source `source_material/reductions/paper/restrictions.tex`,
  blob `55986205ce92bf93bbb2863b5064af001829844a`, used only as scope guard.
- Overlap control note
  `research_pushes/2026-10-11-full-fei-100-agents/sources/OVERLAPPING_PRODUCT_NOTE.md`,
  blob `4d9e18018cce12d361df613b1c6dbc80bb9627f1`, used only to prevent a
  shared-variable inference from the disjoint tensor calculation.

## Execution and handoff

- Natural mathematical execution: completed.
- New workers: none.
- Schedule changes: none.
- Exposed model identifier: not exposed.
- Exposed reasoning-effort selector: not exposed.
- Native Brain ingestion: not claimed.
- Independent review: pending.

Next action: `A090` should independently recompute the Walsh ledger and exact
coefficient, and `A091` should adversarially verify the distinction between the
local splice tax and the tensor-stable FEI ratio.  B12 should not generalize
this coefficient into an arbitrary-overlap claim; after review, the productive
continuation is to test other prime Boolean gates for the true supremum of the
same local tax functional.


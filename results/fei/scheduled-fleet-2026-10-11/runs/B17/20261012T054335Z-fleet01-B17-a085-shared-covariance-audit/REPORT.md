# B17 / A085 — independent certificate audit of the shared-coordinate covariance obstruction

Run ID: `20261012T054335Z-fleet01-B17-a085-shared-covariance-audit`

Verdict: **HOLDS at the exact stated helper-obstruction scope**. Full FEI remains **OPEN**.

## Frozen object

Primary packet: A085 (certificate adversary). Target claims:

- `B12-A057-SHARED-COVARIANCE-FORMULA-v1`;
- `B12-A057-TWO-TERM-OVERLAP-POTENTIAL-NOGO-v1`.

Original complete source: `math-open-problems` commit `76eb7a9359fb4dfc01b9e14048c9af79c0643548`, folder `reports/fei-2026-10-11/runs/B12/20261012T052341Z-fleet01-B12-shared-covariance-falsifier/`. The source report blob is `024685305377fff708ad7506dc6262dd7c46f286`; the proof blob is `153f1ca2255b4f64cba4ed5302412f1aa9f2c907`.

The preceding fixed-source kernel envelope was not re-reviewed. This audit begins at the new shared-coordinate identity and truth table.

## Independent result

Starting from the truth tables rather than the author's checker, I recomputed every normalized Walsh coefficient with `Fraction` arithmetic. The root quantities are

`(q,Z,V,J)=(1/4,(5/4)ln2,15/64,1/2)`.

The two children after querying the second physical bit are

`(1/8,(3/4)ln2,0,0)` and

`(3/8,(9/4)ln2-(9/16)ln3,7/16,3/4)`.

Therefore

`qJ-avg(q_child J_child)=-1/64`,

and

`VZ-avg(V_child Z_child)=(63 ln3-102 ln2)/512<0`.

The sign is an integer certificate: `3^63<2^102`. Both components of every nonzero potential `A qJ + lambda VZ`, `A,lambda>=0`, increase on average after the shared query. This proves the claimed no-go for the entire nonnegative two-parameter family.

I also independently expanded the simultaneous-update identity:

`qJ-avg(qJ)=q Inf_i(h)-delta(q)delta(J)`,

`VZ-avg(VZ)=alpha_i^2 Z+avg(V)D_Z-delta(V)delta(Z)`.

The checker verifies these identities coefficient-by-coefficient in the exact log basis `(ln2,ln3)`.

## Finite-to-infinite bridge

The finite truth table alone proves the universal no-go because a universal supermartingale must hold on every Boolean instance, and this one instance gives strict failure for both basis components. The separate all-arity extension uses bent spectators:

`Z(b s_k)=Z(b)+2k q ln2`, `H(F s_k)=H(F)+2k`, and `I(F s_k)=I(F)+k`.

Thus for every integer `k>=0` the reserve drift equals

`[63 ln3-(102+24k)ln2]/512<0`,

while `H/I=(2k+3)/(k+2)<2`. The bridge covers all integer arities in this lifted family analytically; the executed checks for `k=0,...,8` are regression controls only.

## Certificate-adversary checks

- No floating logarithms, interval endpoints, underflow, or precision assumptions enter the sign.
- Zero Walsh atoms are handled by `0 log(1/0)=0`.
- The output and both branch functions are genuine Boolean truth tables.
- Both branch signs occur on the disagreement support, excluding inactive activation.
- The two strict negative drifts rule out every nonnegative coefficient pair except the trivial `(0,0)` potential.
- The tensor lift preserves the defect but has bounded `H/I`; it does not refute FEI.
- The result does not invalidate the proved disjoint-block telescope.

Two natural executions of `python3 check_certificate.py` were byte-identical and passed. `CHECK.out` records the exact values.

## Scope and remaining gap

The audit accepts only the shared-coordinate identity, explicit witness, nonnegative two-term no-go, and bent-spectator extension. It does not accept any full coherent-hierarchy theorem, does not bound the complete remainder, and does not prove or refute FEI.

The next unpaid step is materially smaller: construct a signed joint correction or a representation-invariant actual-output split whose one-step drop absorbs both covariance debts. Any new proposal must fail safely on this audited family and must retain terminal entropy.

Review consequence: because B17 independently reconstructed rather than repaired the claim, this supplies one independent scope review for the two named B12 claims. A fresh A090/A094 review is still required by the campaign's two-review standard before wider acceptance.

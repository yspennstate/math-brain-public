# account01/B17 FEI handoff — arity-5 uniform all-gate slice

Classification: `ESSENTIAL_STEP_APPLIED`. Full FEI remains `OPEN_NOT_PROVED`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Bound candidate: `LIMIT-PRIME-GATE-LIFT-v1` from account01/B18, with `C*=6.5218512`, `Gamma*=Gamma_RO+0.2682048 p(1-p)`.

New exact inference: for every five-input Boolean gate `G`, at the complete central bias vector `(1/2,...,1/2)`, the already-certified smaller read-once lift `Gamma_.01=Gamma_RO+0.01 p(1-p)` satisfies `D_{Gamma_.01}(G)>=0`. Therefore, wherever the Poincare denominator is positive, `c_G(1/2,...,1/2)<=0.01`, and a fortiori the stable `Gamma*` candidate is safe on the whole arity-five central slice. This removes both balance and unateness restrictions.

Mechanism: for every output cardinality `m`, an explicit binary AND/OR read-once comparator `F_m` minimizes `6.4573 I-H` over all five-bit Boolean truth tables of that cardinality. The exact checker covers 3,425,314 low-boundary tables by integer Walsh arithmetic plus rational log intervals; high-boundary tables follow from `H<=h2(V)+V log2 31`. Smallest certified strict finite gap is `0.004906502214` (m=7 or 9). Output complement handles m>16. Checker PASS.

Peer results substantively consumed: account04/B12 commit `e9d8c67867cce3d8eca74e2064c1c644fafb54e2` (balanced-unate arity-five center); account03/B17 report blob `6f1f5b6054a4bc8e7ee750fc952735114f3ce129` (one asymmetric dyadic arity-five slice); account01/B18 stable candidate report blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`.

Scientific artifacts:
- report commit `0b9ef4dbd65c821340c5719e9641425e692801b0`, blob on readback `daca0767157595c2c2ac7d9da4a58fe86132ffe4`;
- checker commit `23a9264ddcb4920972f32bd1d1700754edc36888`, blob `abce0d7f46ee0ca78c80a59db5755aa7874efebb`, local executed SHA-256 `9f8a92231544fb87e2a7bf80db2b5cdad8d969e35bda81a0a28f71091d2a0f5e`;
- output commit `c9d82685e4bff979d4f077ed3cc4fe042fce1b9e`, blob `0861652ee2ed196ce07c54fc83224c9129eb718d`, local output SHA-256 `df48be96df14c77e12d7334b78dc3746b25cc00376edc0855cccd19eab31b7ec`.

Next mathematical frontier: genuinely off-center composition-prime arity-five gates outside the already-certified `(1/2)^5` and `(1/2,1/2,1/2,1/2,1/4)` slices. Do not repeat the uniform center.

# account01/B14 FEI handoff — bounded-depth F-only selector refuted by majority

**Classification:** `CANDIDATE_REFUTED` for the proposed three-level / any fixed-depth `F`-only continuation. **Full FEI remains OPEN.**

**Scientific source:** private FEI archive commit `64c2dda1c7cc27fb28df263fd94f5c33eede1a0f`, report blob `e68ddcb936197ea865a0d88779f2a4e5135f7a1c`, own B14 run `20260922T071413Z-majority-bounded-depth-barrier/REPORT.md`.

**Lead dependency consumed:** account01/B18 `20260922T065447Z-two-level-anti-amplification/REPORT.md`, blob `af4603b74e2e120606353ce37d72d91cc44b6da9`. It proposed a three-level greedy continuation for the hard core using local payments
\[
F(d)=C^\dagger d-1-h_2(d)+h_2(1/2-\sqrt{d(1-d)}),\quad C^\dagger=6.521851214.
\]

**Named other-account result applied:** account02/B14 `20260922T060632Z-zero-credit-3d-tube/REPORT.md`, blob `202aed29e7af82ced5d99cc53def5b80f8451e8f`, which closes the genuine physical MUX tube by revealing the address bit with defect reserve `>9/8192`.

**New theorem:** `F(d)<0` for every `0<d<=1/128` because `F(d)<=C^dagger d-h_2(d)<=d(C^dagger-7)<0`. For odd majority `Maj_n`, after `r` physical restrictions every remaining-coordinate influence is a binomial atom and satisfies
\[
\operatorname{Inf}_j((\operatorname{Maj}_n)_\rho)\le1/\sqrt{n-r-1}.
\]
Hence for every fixed depth `L`, any odd `n` with `n-L>=16384` has the property that **every** internal pivot of **every** adaptive physical tree of depth at most `L` has negative local payment. Therefore
\[
\sum_{v\in Int(T)}\pi_vF(d_v)<0
\]
for every nonempty depth-`L` tree. In particular the proposed three-level greedy implication is false. Majority also satisfies the lead's local hard-core thresholds for large `n`, so this is a source-valid obstruction to deriving bounded-depth coverage from those thresholds alone.

**Replacement obligation:** a successful restriction proof must retain quantitative child/leaf defect, or use depth growing with dimension and prove late payments amortize the diffuse negative prefix, or add a bounded noncircular potential. Do not spend another run optimizing a fixed depth threshold without addressing this majority obstruction.

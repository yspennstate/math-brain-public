# A041 guard ledger

The original sources are the recovered reductions `paper/biased.tex`, labels `biasfull:weightedcounter`, `biasfull:creditremark`, and `biasfull:localTC`. Source hashes are recorded in `out/SOURCE_RECEIPTS.json`. This file preserves their exact scopes.

| Guard | Actual witness and units | What fails | Replacement check |
|---|---|---|---|
| Global physical TC | weights `(m,1,...,1)`, threshold `m`, `q=m^-2`, `q0=(m-1)q^m/[1+(m-1)q^m]`; TC in nats | `alpha TC(Q) <= K I` for fixed K: ratio `(ln m+1)/8+O(ln m/m)` | Total fair-activation mass is below 2; every multiscale positive rank score is zero. The theorem uses derivative spectra, not Q. |
| Unit pivotal normalization | same weighted family; logarithms in nats | `V ln(1/V) <= sum I_i ln^+(4 rho_i/V)+K I`: residual/I `.5 ln m-ln 2+O(ln m/m)` | No such normalization assertion is used. Larger multipliers are neither established nor refuted here. |
| Every-coordinate physical TC | same weights, `q0=q^m/(1+q^m)`; fixed m then q tends to 0 | Every coordinate's `alpha sum_{k!=j} I_Q(X_j;X_k)/I_j` tends to `m ln 2/2` | Total fair mass tends to zero; all positive rank scores vanish eventually. This says nothing negative about spectral good-coordinate erasure. |

The exact pilot checked the global-control cases m=2..6 and local-control cases m=2..5, q=1/8,1/32. It did not attempt to reprove the already recovered asymptotic TC or pivotal-credit failures numerically. Those are analytic imported controls. All tested rank scores were less than one, exactly.

The small-cube pilot also checked actual Boolean thresholds with unequal weights and arbitrary listed mixed biases, including positive higher-order spectra. Signed and zero real weights are handled by orientation and contraction in the proof. Deterministic biases are contracted before normalizing.

The singleton corrected entropy bound is `4 Delta` in nats for every monotone gate. The replacement rank payment is `(3+ln 2) I` in nats, not a deficit payment. The first missing implication is a normalized reference or other argument bounding the higher-degree corrected entropy by an absolute multiple of `Delta`.

The two-bit AND endpoint family in `ENDPOINT_TAX_LOWER_BOUND.tex` separately repairs the recovered B09 section 5(4) inference: actual `J-M`, not the available upper tax, forces a `p log(1/p)` term. Exact product/tensor additivity does not imply unpaid arbitrary-composition transport. No independent acceptance of B09's full uncertainty theorem is claimed by this packet.

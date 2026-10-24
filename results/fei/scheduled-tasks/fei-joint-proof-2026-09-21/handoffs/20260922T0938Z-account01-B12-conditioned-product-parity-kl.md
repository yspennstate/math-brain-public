# account01/B12 FEI handoff — quantitative conditioned-product parity KL

**Classification:** `AUXILIARY_ONLY / QUANTITATIVE_BOOLEAN_KL_CREDIT`. Full FEI remains **OPEN / NOT PROVED**. Execution remains `WITHOUT_VERIFIED_BRAIN`.

**Corrected common target.** The fixed `LIMIT-PRIME-GATE-LIFT-v1` potential is refuted by account03/B12 `20260922T061544Z-biased-prime-candidate-refutation`. This run instead applies the potential-agnostic account02/B15 `20260922T0829Z-influence-iprojection-kl/REPORT.md` (`B-INFLUENCE-IPROJECTION-v1`, report blob `5ce14eaaec34f0d91f2d430dba576e19dddc6894`):

\[
R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ},\qquad
K_{\rm occ}=D_{KL,2}(P\|Q_r)=H_{\max}(r)-H(P).
\]

The exact missing Shannon payment is `K_occ >= [-B_inf^Gamma]_+`.

**New theorem.** On the balanced-uniform branch with `mu=sum r_i>1`, let `Q_r` be the nonempty product law with `t_i=c r_i`, where `1-c=prod_i(1-c r_i)`, and suppose `c<1`. With active set `E={i:t_i>0}` define

\[
d={1\over c}\prod_{i\in E}\sqrt{t_i(1-t_i)}.
\]

Then actual Boolean convolution at frequency `E`, the odd number `2^{|E|-1}-1` of nonempty proper complement pairs, and the Bhattacharyya/KL inequality give

\[
\boxed{K_{\rm occ}\ge-\log_2(1-d^2)}.
\]

Equivalently

\[
H(P)\le H_{\max}(r)+\log_2(1-d^2),
\]

so any proposed `Gamma` is certified on this branch whenever `B_inf^Gamma >= log_2(1-d^2)`.

**Decisive limitation.** This is not enough for the hard anisotropic sources. For the uniform four-bit prime `B0`, `K_occ≈0.319281` but the guaranteed credit is only `≈0.00324306`. For the central Numaro influence profile the actual dependence credit is `≈0.256838` while this single-complement certificate is only about `4.86e-30` bits. The next required mathematics is therefore a multi-convolution or other signed-Boolean quantitative stability theorem, plus the `c=1` character-times-bent boundary and an off-centre analogue.

**Scientific source/readback:** `proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260922T091637Z-conditioned-product-parity-kl/REPORT.md`, report blob `3e70d606419307541e4ae052d20fa6ef1595fc36`; finite-check output blob `2cec99083a7f6c897fadb8033bdac0a607aa6bab`.

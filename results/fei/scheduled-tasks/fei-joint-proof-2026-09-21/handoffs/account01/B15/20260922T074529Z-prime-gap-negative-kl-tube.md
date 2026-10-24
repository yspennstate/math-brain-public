# account01/B15 FEI handoff — five-input prime gap + negative-KL tube

**Classification:** `ESSENTIAL_STEP_APPLIED`. **Full FEI remains OPEN.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific artifact:

- repository: `yspennstate/math-open-problems`;
- immutable report commit: `89adbd31c2f64c7fed2dcf7b9111aeebcfeeccb2`;
- report path: `proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T074529Z-prime-gap-negative-kl-tube/REPORT.md`;
- report blob after readback/update: `77eda5a7574974af3203fe1f8f88dcff85da8e2f`;
- checker blob: `b33d8ea9e5c3d541b3ef72e200b4adbf65cb90ba`;
- captured-output blob: `259718af700888da79b18fd70c336d9745f032d0`.

## Result

For the exact five-input uniform-center certificate at `Ccert=6.4573`, apply the complete composition-prime module criterion to every source row whose certified objective lower bound is at most `0.039`. Among 3,425,314 low-boundary rows, exactly 9,490 lie at/below that threshold; all 9,490 are decomposable and none is composition-prime. All higher-boundary generic lower bounds are strictly above `0.039`. Therefore every essential composition-prime five-input gate `P` satisfies

\[
D_{\Gamma_{.01}}(P;1/2^5)>0.039,
\qquad
c_P(1/2^5)<-0.0212.
\]

This removes the decomposable near-equality rows that caused the previous global prime reserve floor `0.004906502214`.

Retaining account02/B15's exact negative support-relative entropy term,

\[
H(r)-H(w^0)=\sum(r-w^0)\log_2(1/w^0)-D_{KL,2}(r\|w^0),
\]

gives, for every essential five-input composition-prime gate and every bias vector with

\[
\max_i|p_i-1/2|\le4\times10^{-5},
\]

\[
D_{\Gamma^\dagger}(P;p)
>
0.000349632+(1-\zeta)D_{KL,2}(r\|w^0)>0.
\]

The old certified prime tube was `4.4e-6`; the new radius is about `9.09x` larger. The negative-KL support decomposition is quantitatively necessary at this radius: a generic 32-atom Fannes payment is too large for the `0.039` central reserve once the input/output transport costs are included.

## Exact next obligation

Full FEI is not proved. The first remaining fixed-candidate obligation is the same all-gate prime inequality outside this five-input central tube, together with higher-arity primes. The most compatible next B15 attack is a source-exact lower bound for the conditional Gibbs KL excess

\[
D_{KL,2}(w^+\|\nu_p^+)-\log_2((Z-1)/x_q),
\]

or a genuine composition-prime gate/bias falsifier. Tensor/decomposable descendants are already closed by the exact activity-KL cocycle and should not be re-audited.

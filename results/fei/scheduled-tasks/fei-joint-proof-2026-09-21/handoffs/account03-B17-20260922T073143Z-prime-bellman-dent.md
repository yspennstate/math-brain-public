# FEI handoff — account03/B17 prime Bellman dent transport

Status: `ESSENTIAL_STEP_APPLIED`; full FEI remains `OPEN / NOT PROVED`.

Consumed peer artifact: account04/B18 prime Bellman envelope theorem, science commit `a6b9372512342993ba16a1892ccda12dddf1e7d7`.

Applied claim: whether the dominated seed `Gamma^dagger = Gamma_0 + 0.268204856 p(1-p)`, `C^dagger=6.521851214`, can keep all composition-prime Bellman iterates nonnegative after the source-bound Numaro prime-gate dent.

New exact mechanism.  For one Numaro core coordinate, with all other inputs unbiased,

`F_*(p)=1/2-(57/256)(1/2-p)` and `It_i/V_p=57/256` exactly.  Hence for dent `Delta_m=Gamma^dagger-Gamma_m`,

`Delta_{m+1}(F_*(p)) >= (57/256) Delta_m(p) - D^dagger(p)`.

The exact rational witness `p=223/456` gives `p_out=1019/2048` and

`D^dagger(p) < -0.03802373436527919`, over twice the earlier first dent used in the peer Bellman report.

Deep route: start `p_0=27/64`, so `p_r=1/2-(5/64)(57/256)^r`.  Rational spectral masses plus atanh-series log enclosures force eight positive dents.  At step 8,

`Delta_8(p_8) > 6.774619238410960e-6`, with `1/2-p_8 = 4.719208367932034e-7`.

The exact uniform Numaro seed defect is `5.718040896917480e-6`; because `I-1=133/128`, the center self-amplification threshold is

`tau_center = 5.503076953424342e-6`.

Thus the off-center dent is already `>1.23106 * tau_center`.  The missing implication is no longer dent size; it is a low-cost **prime return map** that transports this dent to the center (or another gain cycle) without spending the surplus.  The unchanged one-core contraction is refuted as a complete closure: the ninth forced lower bound is negative.

Replacement attack: certify a finite multi-core prime-gate fan-out/return cycle.  Near the center, biasing several Numaro core inputs at the same dented bias has aggregate first-order transport coefficient `k*57/256`; for `k>=5` this exceeds one.  Do not infer a proof from that linearization: construct a finite exact cycle or prove every such cycle dissipative.

Canonical science report: `proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260922T073143Z-prime-bellman-dent-transport/REPORT.md`, commit `fd2065de20f825147b05bc138a9d2ce87c38dc17`, report blob `b964337d039b2ed24828dfd0b61773651b68f3dc`.

Checker commit `c798d970f57b2cb4a1dca85d344d9756ee6c09fe`, checker blob `a9070f42e9d6e33ad5b1f22bbae513a83b66a1d4`.  PASS output commit `dccb67b7aa226db7bb523f7c8537c16df023195f`, output blob `4a93b3799ad31270734ec63caeda980f5dcea83b`.

Next recipient: `account04/B18` for prime-envelope integration; `account03/B18` can translate the dent-vs-center-threshold condition into its Gibbs/Bellman language.

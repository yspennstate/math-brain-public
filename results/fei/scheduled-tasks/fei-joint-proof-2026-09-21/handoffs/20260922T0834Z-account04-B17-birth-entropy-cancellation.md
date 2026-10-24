# FEI handoff — account04/B17 birth-entropy cancellation

**Source report:** `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T081319Z-birth-entropy-cancellation-axis/REPORT.md`, report blob `277b98d6477ea778382d6b89a3c205256a7cbacd`.

**Consumed peer:** account03/B15 `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T073015Z-axis-child-slack-kl/REPORT.md`.

**Candidate retained:** `LIMIT-PRIME-GATE-LIFT-v1`, `C^dagger=6.521851214`, quadratic lift `a^dagger=0.268204856`.

For one-axis motion `t=1/2+s`, `r=2s`, write the two uniform branch spectra as `u_A,v_A`, with `c_A=(u_A+v_A)/2`, `e_A=(v_A-u_A)/2`, disagreement `d=sum e_A^2`, and newborn mass `beta=sum_{c_A=0} e_A^2`. The biased pair transport is exact:

`hat G_t(A)=c_A+r e_A`, `hat G_t(A+k)=sqrt(1-r^2)e_A`.

The newborn spectral entropy is exactly `beta h_2(r^2)`, while the physical pivot term contains `d h_2(r^2)`. Since `beta<=d`, all newborn entropy is paid automatically, leaving `(d-beta)h_2(r^2)>=0`. On the old support the full negative KL credit is retained. This yields

`D(t) >= D(1/2) - [4 C^dagger+170d+16 sqrt((1-d)(d-beta))]|s| -32(d-beta)s^2 + (d-beta)h_2(4s^2) + (1-beta) KL`.

For an essential composition-prime five-input gate, `d=j/16`, `1<=j<=15`. Using the rigorous central reserve floor `0.0049065` gives the certified axis tube

`|p_k-1/2| <= 2.59e-5`,

with `D_{Gamma^dagger} >= 2.6928899296e-6`. In margin units this implies `c_P <= 0.26820270168805632` whenever the Poincare denominator is positive. This is a 29.5% enlargement over the newest B15 axis theorem.

**Sharp Boolean adversary to any stronger birth-mass lemma:** the five-bit truth table `0x3A38C7C5` is essential and composition-prime, with branch tables `0xC7C5,0x3A38` and exactly `d=beta=7/8`. Hence no universal `beta<=theta d` with `theta<1` is possible even on composition-prime five-bit gates. The cancellation above is sharp. This is not a counterexample to the live Gamma candidate.

**Checker:** source blob `e6dc18b26cae0961c8ab3e4d55463057e40cda0b`; captured PASS output blob `57ad7482f349f7db01368a37afdc0a99adcbd2b0`.

**Next recipient / missing implication:** B15/B17 workers attacking the five-input bias tube should replace generic newborn-support Fannes leakage by this exact birth-payment identity. The next mathematical target is a two-or-more-axis analogue preserving the same KL credit; the new obstruction is cross-pair interference, not atom birth.

**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI remains `OPEN / NOT PROVED`; `WITHOUT_VERIFIED_BRAIN`.

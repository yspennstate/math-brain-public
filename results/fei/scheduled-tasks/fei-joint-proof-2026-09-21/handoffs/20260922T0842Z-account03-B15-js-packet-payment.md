# account03/B15 handoff — exact real-restriction JS packet payment at every selector bias

Status: `ESSENTIAL_STEP_APPLIED`; full unrestricted FEI remains `OPEN / NOT PROVED`. Execution is `WITHOUT_VERIFIED_BRAIN`.

Scientific source package: `yspennstate/math-open-problems`, path `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T082654Z-js-packet-payment/`; strengthened `REPORT.md` commit `8793c7e49e1de7921bc76c7724c92fae03024e26`, blob `b42a78fd9e6621661954fdc0b44eaa1ba0261179`.

Candidate version: `LIMIT-PRIME-GATE-LIFT-v1 / B-GIBBS-KL-v1` with `C^dagger=6.521851214`.

Consumed peer artifact: account02/B15 `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`. Its exact Gibbs-KL gate factorization is applied to a genuine coordinate restriction, not merely cited.

Let the actual selector bias be `s=p_i in (0,1)` and let `U,V` be the two actual Boolean child spectral laws. Define

`kappa(s)=ln((1-s)/s)/((1-2s) ln 2)`, with the continuous value `kappa(1/2)=2/ln2`.

Using the sharp asymmetric two-point Bernoulli log-Sobolev inequality packetwise on the actual weighted Fourier-pair transform gives the proved all-bias payment

`JS_s(U,V) <= kappa(s) It_i`.

The physical signs are retained: replacing `u_T-v_T` by `|u_T|-|v_T|` can only decrease the branch mass, so opposite-sign overlap is harmless for this estimate. No packet-integrality hypothesis is used.

Retaining all child defects, the potential Jensen term, the physical branch entropy `B_i`, and the negative information credit, the exact common Gibbs residual satisfies

`D_Gamma(G;p) >= (1-s)D_0+sD_1 +(1-s)Gamma(q_0)+s Gamma(q_1)-Gamma(q) + [a_i-kappa(s)] It_i - B_i`.

At `s=1/2` for the live candidate this specializes to coefficient

`C^dagger-2/ln2 = 3.636461132222073`.

This is a direct bound on `V_q R_B`, the versioned common residual, for a genuine coordinate restriction at arbitrary interior selector bias.

Known failure preserved: a universal credit-free `B_i <= K It_i` estimate is false, and no automatic physical packet integrality is assumed. The remaining obligation is to pay the actual `B_i` term in the low-price Bellman region using retained child slack and/or the exact magnitude/price KL credit rather than discarding conditional information.

Finite stress only: exhaustive Boolean truth tables through arity four at the symmetric selector gave maxima `JS/It_i = 2.0, 2.1951797627815943, 2.3986718134590450` for arities 2,3,4 respectively, all below `2/ln2 = 2.8853900817779268`. The theorem itself is analytic and all-bias.

Next recipient: account03/B18, with account02/B15 as the KL-credit partner. Remaining implication to full FEI: universal nonnegativity of `B-GIBBS-KL-v1` for every finite arity and every interior bias.

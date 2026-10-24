# FEI handoff — exact occurrence-KL remainder is sharp-constant FEI-complete

**Source:** `account04/B15`, run `20260922T043833Z-b15-fei-r11`.  
**Scientific report:** `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T043833Z-occurrence-tensor-saturation/REPORT.md`, creation commit `70a794f68504963342ca9ba6ec05ef2718c30f9e`, blob `88c253ad0ed66373db8ddbd7402c91f7b7c64ce7`.  
**Status:** `ESSENTIAL_STEP_APPLIED / SHARP-CONSTANT OBSTRUCTION`; unrestricted FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Consumed newest account02/B15 handoff `20260922T040227Z-balanced-stop-kl-fusion`, blob `e2b3c0c53bd5cc8cccf25c3ed7f9d88f033a9e27`. For balanced Boolean `f`, with `I=E|S|`, `beta=I-1`, normalized occurrence law `q`, prefix KL credit `K_rho`, and root/deletion mixing credit

\[
J_{mix}=D_2(\alpha\|q)+\beta D_2(\rho\|q),
\]

its exact unpaid scalar occurrence expression is

\[
\boxed{U_{occ}(f)=I H_2(q)-E\log_2(K!)-K_\rho-J_{mix}=H(f)-T_{stop}(f).}
\]

All negative credits are retained. Account02 also proves `T_stop <= C_stop (I-1)` and the one-time valuation reserve `R<=2 C_J(I-1)`.

Define

\[
C_{occ}=\sup_{f\ balanced,I>1}\frac{U_{occ}(f)}{I(f)-1},
\qquad
C_{FEI}=\sup_{g\ nonconstant}\frac{H(g)}{I(g)}.
\]

**New theorem:**

\[
\boxed{C_{occ}=C_{FEI}}
\]

as extended-real sharp constants.

Upper bound: `U_occ<=H`, and account03/B13's completed balanced-support-deficit equivalence gives `sup_balanced H/(I-1)=C_FEI`.

Lower bound: for any Boolean seed `g` on `n` variables, take the disjoint tensor power `h_k=g^{\otimes k}` and balanced suspension `f_k(y,x)=y h_k(x)`. Then

\[
H(f_k)=kH(g),\qquad I(f_k)-1=kI(g).
\]

The Fourier support size `K_k` lies in `{1,...,kn+1}`. Account02's exact stopping theorem gives

\[
0\le T_{stop}(f_k)\le H(K_k)\le\log_2(kn+1),
\]

hence

\[
\frac{U_{occ}(f_k)}{I(f_k)-1}
\ge
\frac{H(g)}{I(g)}-rac{\log_2(kn+1)}{kI(g)}
\to\frac{H(g)}{I(g)}.
\]

Taking the supremum over `g` proves the reverse inequality.

**Consequence:** even after retaining factorial, prefix-KL, and mixing-KL refunds, a scalar theorem `U_occ <= C(I-1)` has exactly the FEI sharp constant. It is not a cheaper extremal remainder problem. The certified balanced shared-graft lower bound therefore transfers directly: `C_occ >= 6.521850083658612443633672199...`.

**Not refuted:** the valuation-assisted joint-credit inequality. The theorem does not show the one-time signed valuation reserve `R` is negligible on tensor suspensions. The next viable D-interface target is therefore `U_occ-R` or a finer conditional source decomposition that keeps valuation inside the same KL fibres. Any proposed extra credit should first be tested on the tensor-suspension family; an `o(k)` credit cannot lower the limiting extremal ratio.

**Next recipients:** account02/B15 and account03/B18. Do not return to a scalar three-credit occurrence transfer as though it were simpler than FEI.

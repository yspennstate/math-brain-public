# B16 FEI signed-transport handoff — one-sided multiplier payment

**Status:** PARTIAL / PROVED UNIVERSAL PAYMENT LEMMA / FULL FEI OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The q-flip activity for coordinate `i` has

`p_hat_i(0)=2 E_i`, `p_hat_i(U)=-2 eta_hat_i(U)^2` for `U!=0`, where `E_i=Inf_i(1-Inf_i)`.

Therefore, for any centered displacement kernel `k`,

`<k,p_i> = -2 sum_{U!=0} k_hat(U) eta_hat_i(U)^2`.

Only **negative** kernel multipliers are upper-bound debits; arbitrarily large positive multipliers are credits. This replaces the previous absolute/L2 kernel target.

For any nonnegative ordered-min codimension charges `q_c`, define the radial kernel

`K_n^q(w)=(1/n) sum_{c>|w|} q_c C(c-1,|w|)/C(n-1,|w|)`, `K(0)=0`, and normalize `mathcal K=2^(n-1) K`. Its nonconstant Walsh multiplier at weight `r` is

`A^q_{n,r}=(1/n) sum_c q_c [2^(c-1) C(n-1-r,c-1)/C(n-1,c-1)-1]`.

If `Q_n=sum_c q_c`, then

`A^q_{n,r} >= -Q_n/n`,

with equality at `r=n-1`. Consequently the centered kernel obeys the sharp Boolean payment

`<mathcal K-E mathcal K,p_i> <= (2Q_n/n) E_i`,

and after the minimizing-character gauge the sum over coordinates is at most `(2Q_n/n) J(f)`.

For the actual raw subcube entropy charges `q_c=H_c`,

`Q_n < 12` universally (direct value through c=100: `8.71142009332293`), hence the **entire centered raw ordered-min entropy baseline** costs less than `24 J(f)/n`. The previously found low-mode growth `A_{n,r}~4n/((r+1)(r+2))` is still an obstruction to absolute/L2 payment, but its sign makes those modes credits in the actual upper-bound problem.

For the account03 parity-switch Shapley-refunded diagnostic `q_c=2^(3-c)`, the one-sided centered debit is at most `(8-2^(4-n))E_i/n`.

**Next target:** isolate the constant displacement mode of the fully refunded Shapley/plaquette/terminal/R16 kernel. The nonconstant part of every nonnegative codimension-level component is now already paid. A complete route needs to show the remaining constant debit is canceled/paid by the exact curvature + terminal/moment ledgers, or identify the genuinely negative residual multipliers if such a decomposition fails.

See `REPORT.md` for proof and `check_one_sided_multiplier.py` / `CHECK_OUTPUT.txt` for the small self-check. No FEI closure or novelty-priority claim is made.

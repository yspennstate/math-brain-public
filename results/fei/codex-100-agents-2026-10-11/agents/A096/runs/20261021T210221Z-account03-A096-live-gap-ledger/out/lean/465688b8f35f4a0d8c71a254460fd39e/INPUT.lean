import Lean

-- Common-denominator, physically weighted one-step envelope payment.
-- This checks the account algebra, not the Fourier/logarithmic premises.
theorem reset_account (b bs childc constc c terminal remainder budget e : Nat)
    (hb : b <= bs)
    (hsource : bs + childc + constc <= c)
    (hterminal : terminal <= constc + 24 * e)
    (hreserve : remainder + 24 * e <= budget) :
    b + childc + remainder + terminal <= c + budget := by
  omega

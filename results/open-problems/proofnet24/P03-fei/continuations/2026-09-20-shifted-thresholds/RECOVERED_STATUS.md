# Separate recovery notice: the unpushed 19 September FEI package

20 September 2026. **This is recovered prior work, not a new result of the shifted-threshold continuation. Full FEI remains OPEN.**

The actual Library file `FEI_Sharp_Stability_and_Drift_2026-09-19.patch` was found and materialized during this continuation. Its raw size is 352937 bytes and its SHA256 is `c9c534b22682e38c0546e521ebdea72ef4cebe7d97773e20229d908077cb0207`. Library file ID: `file_0000000096a08210b0f50b5d5bd67e46`, version 1. This corrects the older frozen-session recovery's statement that no completed additional September 19 patch had been recovered: that was the state of its earlier search, not a statement that no package existed.

The raw patch and extracted files are preserved in the current conversation's backup bundle. **This GitHub notice is not a byte-for-byte upload of the entire 352937-byte package.** Do not claim that all its scripts or reports are now in master merely because this notice exists. The new shifted-threshold proof/checker/output are separately committed in full and do not depend on this recovered package.

## Critical correction for continuation

The recovered `AFFINE_DRIFT_BARRIER.md` has Git blob hash `8b489b884b32edb6b1a1246ad4a87a923d67711d`. Its Sections 1--9 supply an analytical majority obstruction to EVERY fixed one-step affine-drift coefficient, not just the coefficient-four obstruction already in the repository:

    f_z(x)=f(x)f(x+z),
    M(f)=min_basis sum_v min(P[f(x)!=f(x+v)],1-P[f(x)!=f(x+v)]),
    Delta_M(f)=2M(f)-E_z M(f_z),
    D_cross(f)=2H(f)-E_z H(f_z).

For odd n=2r+1, with a_n=2^(-(n-1)) binom(n-1,(n-1)/2), the recovered proof establishes

    M(Maj_n)=(n-1)a_n,
    2(n-1)a_n^2 <= Delta_M(Maj_n)=O(1),
    D_cross(Maj_n) >= (1/18) sum_{a=1}^r 1/a + 1/36.

Consequently D_cross/Delta_M diverges. Adding a bounded mode-defect term does not repair the estimate. The proof uses the two-dimensional period space span{z,1} of one majority derivative, a joint-slab bound for short directions, and a compact Gaussian-limit argument for directions a positive fraction of n away from that period space. For typical z it shows every nonperiod direction has folded influence at least 2a_n-C/n; a basis needs at least n-2 such directions. The lower entropy bound comes from the exact majority level law and the allocation entropy of two independent spectral samples. The bounded-drift argument and the harmonic allocation calculation were read in this continuation; finite increasing ratios alone are not their justification.

This means that the older index wording 'all possible entropy-drift constants have NOT been refuted' is superseded by a recovered analytical argument, subject to reconstruction and independent checking. Do not keep tuning a fixed coefficient in this same target merely because the older index retains its historical wording. The existing valid D_cross<=6M bound is unaffected.

## Other assertions in the recovered package

The source also contains a sharper claimed limit Delta_M(Maj_n)->8/pi; allocation asymptotics A=L=(8/pi^2)log_2 n+O(1); extensions to each fixed derivative depth and bounded adaptive stopping; fresh-control identities and a control-crossover calculation; and an optimal one-entry entropy stability order Theta(2^(-n/2)). These are prior-package assertions. The full proofs and all twelve recorded checkers were NOT independently audited or replayed in this current continuation. Do not describe them as newly proved, Lean-verified, independently verified, or full-FEI closure on the basis of this notice.

The source's remaining universal accumulated-allocation and hereditary-erasure bounds are still unproved. Neither the recovered drift obstruction nor the new Han overlap obstruction is a counterexample to FEI.

Future work that relies on the recovered sharper results should first retrieve the identified raw patch, reconstruct the exact referenced argument, and record which files and checks it actually consumed. The new shifted-threshold package is independent and can be checked directly from the committed files.

# Concurrent-source comparison addendum

Run: `account03-B09-20260922T155042Z-qform12`

After the main report was committed, a concurrent completed theorem became visible from `account02/B04`: `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1`, source commit `b129377880c18fe011dd4513282f2e0b60e412e0`. That proof combines the same ridge envelope with an independently established physical-square smoothing theorem and obtains the sufficient threshold `theta>4q/3` by fixing the residual density exponent at `L^3`.

The B09 theorem in `REPORT.md` is compatible with that result but strictly extends its analytic threshold. Instead of fixing `p_R in L^3`, it uses inverse Hausdorff--Young at an arbitrary conjugate pair `r in (1,2)`, `p=r/(r-1)>2`, then proves directly

`sup_y int_0^infinity s^(-1/2) p_R(y-s) ds <= [1+(1-r/2)^(-1/r)] ||p_R||_p^(r/2)`.

The ridge envelope belongs to `L^r` whenever `r theta/(2q)>1`. Such an `r<2` exists exactly when `theta>q`. Thus the square-assisted ridge threshold improves from `theta>4q/3` to `theta>q` at the price of a constant that diverges as `theta downarrow q`.

This comparison is also an independent consistency check on the key physical-square smoothing mechanism: both derivations condition only on an untouched ORIGINAL coordinate and keep the residual coordinates in their product basis. Neither assumes independence after a spectral rotation.

The designated partner `account04/B09` still had no completed current-QFORM artifact at the checks used for this run, so no designated-partner theorem is claimed as consumed. The concurrent `account02/B04` result is recorded as an additional non-partner cross-check, not as a substitute for a nonexistent partner artifact.

# account01/B17 FEI handoff — exact source-restriction minimal arity

Classification: `AUXILIARY_ONLY`. Full FEI remains OPEN / NOT PROVED. Execution: `WITHOUT_VERIFIED_BRAIN`.

Applied exact peer versions `account03/B15/20260922T002607Z-readonce-gamma-counterexample/REPORT.md` (blob `e49efe403698395b700278d067c245c12a7b15eb`) and `account04/B13/20260922T0055Z-arity10-prime-falsifier/REPORT.md` (blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`). The first gives the balanced-uniform gate identity `c_G=4(H/(I-1)-C0)` and refutes the old read-once Gamma; the second gives a composition-prime 10-input Numaro restriction with `H/(I-1)>6.4593722816378554`.

New result: using the exact recovered Numaro host decomposition, exhaust all normalized physical restrictions with nominal arity <=10 (44,266 representatives). Rational Walsh/influence and rational-log interval arithmetic show balanced essential restrictions occur only at arities 1,4,6,8,10. For essential arity <=9 the exact maximum is the arity-8 value
`H/(I-1) < 6.363969446288164350267463751014 < 6.4559`.
At essential arity 10, 621 of 630 balanced normalized restrictions rigorously exceed 6.4559; the maximum interval is the peer-certified G10 value around `6.45937228163785573157`.

Thus, **within the full physical-restriction lattice of the exact Numaro n=18 seed, the minimum essential arity of a balanced restriction violating the proved read-once cap 6.4559 is exactly 10**. In particular the owner-suggested arity-5--9 falsifier search cannot be obtained merely by restricting this known source; any smaller falsifier must use a genuinely different gate or a biased product point.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T023820Z-numaro-restriction-minimal-arity/REPORT.md`, with standard-library exact checker and PASS output in the same directory. Checker SHA-256 `f82e2c50aec91dd5182443672246c0435b3a28509c8c3c7d6eea22065f6723b7`; stdout SHA-256 `dcd399195950bad0fb41034388bb197494e60fe2e14112e95c634f5faecbcdf9`.

Do not promote this to a theorem about all Boolean gates of arity <=9. Remaining target: a finite-cap symmetric nonnegative Gamma satisfying (G) for every gate/bias, or a source-valid counterexample to a concrete successor potential.

# MOC4 late handoff — B07 bi-orientation gate versus latest B09 cycle separator

Same run: `20260922T040155Z-a01-b07-moc4-r12`. Outcome unchanged: **ESSENTIAL_STEP_APPLIED**, MOC4 **OPEN**, `WITHOUT_VERIFIED_BRAIN`.

After the main B07 report/handoff, I consumed the newer account03/B09 `MOC4-CYCLE-SEPARATOR-NOGO-v1` (`20260922T040531Z-account03-B09-cycle-separator-nogo.md`). Its genuine `SO(6)` datum passes all 16 earlier odd-twist cuts yet separates the 24 even signed matching endpoints for an unstructured coefficient pair `K_cycle=3 diag(1,1,-1)` and skew `X_cycle`; B09 correctly notes that those coefficients have not been shown to come from spectra.

Exact application of B07's new `MOC4-BIORIENTATION-PAIR-GATE-v1` to the B09 datum shows all six gates pass as well. Because `K_cycle` and `D` are diagonal, all six orientation-swap cross terms `C` vanish. The six exact gate slacks are

`4446471/1051250`, `44037/42050`, `818424/525625`, `127749/42050`, `971271/1051250`, `52056/18125`,

all positive.

Therefore the new B07 gates are **not** a coefficientwise characterization of the even endpoint hull, even on the true `SO(6)` orbit. Their useful content is support-specific/maximizer-specific and must be combined with the actual spectral coefficient image. The first residual implication should explicitly include

`X_ab=Re(eta A+_a B+_b)` and `K=(H W H^T)_(1-perp)+Y/2`, `Y_ab=Re(eta A-_a B-_b)`,

plus the common-unitary `(P,D,R)` constraints and the six B07 gates. Any next counterexample must realize the separator from actual `(a,b,eta)`, not arbitrary `(K,X)`.

Canonical addendum: private mathematical archive, `proofnet24/collective-MOC4/account01/B07/20260922T040155Z-a01-b07-moc4-r12/LATE_DEPENDENCY_NOTE.md`, creation commit `6d3596306f38d2edd17521ff543fa53f20863511`.

# account03/B08 -> MOC4 shared handoff

Result: **MOC4-DENSE-CAYLEY-ADVERSARY-v1**. Parent MOC4 remains OPEN.

B08 changed mechanism from one-cycle/Givens work to dense complex rational Cayley unitaries. For

- `a=(18-17i,-20+2i,15-22i,-21+2i)`
- `b=(-19+4i,25-5i,18-i,-18+i)`
- the exact dense unitary `U=G/3562` recorded in the scientific report,

all spectra are simple, all 16 pair sums are nonzero, all 24 target products are distinct, and all 16 entries plus all 36 two-by-two minors of U are nonzero.

Exact determinant:

`D = 278808875/3562 + (24903390/1781)i`.

Common support direction:

`L(z) = -5782 Re(z) + 19099 Im(z)`.

Across all 24 target vertices,

- `M = -61633500`, attained exactly at permutations `1234` and `1342`;
- `m = -59822291610`;
- `L(D) = -2411727095/13`;
- target-safe gap `M-L(D) = 1610491595/13 > 0`;
- normalized gap `(M-L(D))/(M-m) = 322098319/155377711086 ~= 0.0020730020847180702`.

Exact rescue:

`D = λ0 v_1234 + λ1 v_1243 + λ5 v_1432`, with common denominator `406763017440` and numerators `73409846651`, `98803540981`, `234549629808`. All are nonnegative and sum exactly to the denominator.

Peer consumption: named partner account04/B09 `MOC4-STANDARD-CHANNEL-CEILING-v1` was consumed; it constrains any actual support violation by the standard-channel reserve. account01/B07 `MOC4-BIORIENTATION-PAIR-GATE-v1` was also consumed; it supplies six true-unitary orientation-swap necessary inequalities at a global support maximizer and warns that transport-only separators are insufficient.

**Next joint action:** evaluate the partner standard-channel ceiling and the six bi-orientation gates on support-maximizing dense Cayley candidates, not merely arbitrary close-to-facet samples. Search for an exact strict common-support violation only after the true-unitary stationarity/gate filters. If no violation survives, seek an exact payment inequality for the dense Cayley stationary branch.

Scientific source: `proofnet24/collective-MOC4/account03/B08/20260922T042405Z-b08-moc4-r11/REPORT.md`.
Exact verifier: sibling `verify_dense_cayley_adversary.py`.

Isolation: no FEI/benchmark gold used. Brain status `WITHOUT_VERIFIED_BRAIN`. No cross-account native action performed.

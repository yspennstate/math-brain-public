# Nonspatial family and full cost

The family is complete ternary recursive majority on 3^d bits, d>=1, padded to N>=3^d bits, with an arbitrary Boolean truth-table edit set D. The same fixed partition tree codes every spectral subset, not only the original support.

REPORT.md equations (1)-(12) are the full proof. The majority expansion makes a child active with probability 1/2, so level-j expected occupancy is (3/2)^j. Its sum over internal depths is 2(I-1). Three-bit general masks, one root bit, and two bits for the padding join give base cost at most 6I-3. Weighted Parseval pays the coherent edit cost by at most 8*rho*(3N-2), and physical influence changes by at most 2N*rho. Thus the complete code is paid by 12I when N*rho<=1/8; every one-point edit is paid by 25I, or 12I for N>=6.

The unedited read-once family is established composition prior art. The deliverable is the stable all-set encoding and its sparse-edit neighborhood; no literature novelty is claimed. Non-Boolean uniform singleton spectra fail the occupancy payment, as the same tree costs 1+3d with I=1. The universal tree/reference selection step remains open.

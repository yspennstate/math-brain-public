# Erratum to REPORT.md

One parenthetical in Section 4.2, alpha=0 case, reverses the adjective on a threshold. The report says “the stronger threshold ell>=1/32”; `1/32` is of course a **weaker** lower bound than the active branch hypothesis `ell>=1/18`.

The quantitative statement is unaffected and can be sharpened as follows. From (4.17)--(4.18), `M_Z<=sqrt(2)`, and `ell>=1/18`,

`sup_z E|z-Q|^(-1/2)
 <=4*2^(3/4)*18^(1/4) D^(-1/4)
 <14 D^(-1/4)`.

If only `ell>=1/32` were assumed, the same expression would be at most `16 D^(-1/4)`. Both are far below the theorem's generic constant `48 sqrt(10) D^(-1/4)`.

No theorem statement or downstream inequality changes.

# KHETAN-2026-EC6 proof-candidate package

Source: Abhishek Khetan, *A Counterexample to Nivat's Conjecture for a Non-Convex Window of Full Affine Span*, arXiv:2607.09830v2 (2026), especially the abstract, Definitions 1.4–1.6, Conjecture 2, Theorem 1.2, and Section 3.5.

Exact source scope addressed here: if `F subset Z^2` is an exact cluster of full affine span with `|F|=6`, prove that for every `F`-tiling `T`, the orbit closure `cl(Z^2 · T)` contains a 1-periodic `F`-tiling.

`main.tex` now contains the canonical current proof candidate. The earlier draft's bi-infinite formal-series cancellation has been removed. The source-specific proof uses the following chain:

1. A rich spectral direction gives one common root-of-unity phase on each parallel section; using only dilation `alpha=1`, every nonempty section in that direction has size at least two.
2. Two transverse rich directions therefore give a simple six-edge bipartite incidence graph of minimum degree at least two. The only possibilities are `K_{2,3}` / `K_{3,2}` and `C6`; the common phase equations rule out `C6`.
3. The surviving `K_{2,3}` pattern is a product in two primitive lattice directions. Full affine span forces a unimodular basis and gcd-one one-dimensional factors. The rich-direction phase makes the three-point factor a complete residue system modulo `3`; the two-point gcd-one factor is a complete residue system modulo `2`.
4. The exact `3 x 2` product endpoint is proved directly by finite row/column fibres. The prime one-dimensional theorem gives residue profiles `r_n in Z/3Z` and `s_m in Z/2Z`. If `s` is constant, every occupied row is a whole `3Z` coset; if `s` is nonconstant, its image is all of `Z/2Z`, every row is occupied, the two elements of the two-point factor differ by one, and adjacent `r_n` values are forced equal. Thus one coordinate period is unavoidable. This endpoint uses no formal-series cancellation and does not require Khetan's Lemma 3.7.
5. If at most one spectral-kernel direction is rich, Khetan's second spectral branch applies without prime-power arithmetic: after minimizing the finite exceptional set, all exceptional phases are non-roots of unity, Lemma 3.1 kills them, and Theorem 3.11 yields a periodic point in the orbit closure.

Finite core: `check_incidence.py` exactly enumerates the six-edge incidence possibilities, and `incidence_check.txt` records its previously executed output. No new checker was manufactured in the 2026-09-18 recovery run because the finite classification and its archived exact output were unchanged.

Status: **PROVED CANDIDATE / AUDIT OPEN**. This package is self-review, not an independent audit. Protocol closure still requires an actual independent P26 end-to-end audit and one distinct OTHER-track end-to-end audit. The dated bounded prior-art check was refreshed on 2026-09-18: the current arXiv source remains v2 and still explicitly leaves cardinality six open; no later source-matching resolution surfaced in the bounded search. That negative search is not a novelty certificate.

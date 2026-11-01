# B05 learned (Claude lead)

## 2026-10-11 23:4xZ (run 20261011T225000Z-claude-B05-odd-face-transport)

- The rare logarithm at a split is paid by the boundary of the disagreement set: B_i <= h2(d) <= (1/2) I(g h) + log2(e) d
  (Jensen, then cube edge-isoperimetry). The credit (1/2) I(g h) is exactly the number of odd 2-faces through direction i,
  so it telescopes like influence and is spent once per face over any tree: total Q(f) = 2^(1-n) N_odd(f).
- That currency survives the B05 no-go. The no-go priced L against d, V_post and M_inf, all of which are tiny at the
  activated selector; the odd-face credit there is about 3k d, the size of the logarithm, and still a vanishing fraction
  of I because the activation's control influence dominates (bad-node credit / I = 0.025 at k = 6).
- Q itself is not O(I): AND_r gives (r-1)/2, the no-go family 4.84 (k=4) and 7.09 (k=6). The large Q of AND-type
  pieces sits at good nodes (B about 2d there), so only the bad-node part matters. The remaining question is purely
  combinatorial: odd faces spent at rare, spread splits.
- At n <= 4 no split has B > 4d (max B/d = 3.52), so small exhaustive scans say nothing about badness at K >= 4; exact
  structured families (activated bent, flips, towers) are the only informative tests.
- A021 v1 has reversed remainder signs (R >= 0, G_s <= 0); its finite checks did not test them. A reviewer that only
  reruns the author's assertions will not catch a sign in an analytic remainder; expand the series coefficient by hand.
- Tooling: this Bash wrapper fails on heredocs that contain apostrophes (unexpected EOF); use the Write tool for files.
  Directory listings of the big campaign folders can exceed 60 s; read targeted paths. memok.py gates heavy jobs on
  commit free memory as well as physical; a lean array layout kept the n = 19 run far under the 300 MB line.

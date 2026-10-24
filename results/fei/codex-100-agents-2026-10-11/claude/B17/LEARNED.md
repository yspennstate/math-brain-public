# B17 learned (Claude lead)

## 2026-10-11, run 20261011T224300Z-claude-B17-erasure-census-affine-bridge

Exact statements:
- ((1+z)ln(1+z)+(1-z)ln(1-z))/2 <= 1-sqrt(1-z^2) on [-1,1]. Proof: compare the even power series
  coefficientwise, using a_k = C(2k,k)/4^k >= 1/(2k), which follows by induction from
  a_{k+1} = a_k(2k+1)/(2k+2). Per packet this gives JS <= 2min(u^2,v^2)/ln2, which closes C005.
- K_B(n) <= C(n) <= K_B(n) + 2/ln2. Existential erasure is FEI up to 2/ln2.
- K_B(4) = 4+(5/2)log2 5-(9/2)log2 3, certified exactly on all 65,536 tables in 9 s. The same 64
  tables also maximize min_i D_iH/I_i, at 12-(9/2)log2 3.
- K_B(5) >= 16/3-(3/8)log2 3-(169/24)log2 13+(89/24)log2 89 = 2.6958875, attained by the
  three-point table {5,12,13} (an AND of 3 literals intersected with an OR of 2). This is
  certified exactly.

What worked:
- Writing every value times N^2 as an integer combination of log2 p. One rigorous double screen,
  deciding only when |value| > 2^-40 S, settles all but the ties. Ties go to exact signs from
  rational atanh enclosures.
- Steepest ascent with a two-point fallback. It found the n=5 maximum in 60% of restarts.

What failed or misled:
- Bash heredocs holding long Python scripts failed in this harness with "unexpected EOF while
  looking for matching '" (twice). Write the .py file with the editor tool, then run it.
- Composed AND/Tribes families raise H/I quickly (3.83 at n=14) but leave the existential B-ratio
  almost flat (2.697 at n=15). A high H/I is not evidence of a high selection constant.
- The harness refuses REPORT.md from a subagent. The report text has to travel in the final
  structured answer.

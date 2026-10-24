# B15 learned log

## 2026-10-11 23:27 UTC (run 20261011T225100Z-claude-B15-erasure-countersearch)
- Selection lemmas are FEI-equivalent, so finite search can only refute a specific constant or find errors in proved inequalities. Target constants, not principles.
- The n<=4 selectable true-erasure constant K* (A082) breaks at n=5: the complement of a two-step monotone path in F2^5 makes every coordinate cost more than 539/200; at n=6 the Hamming ball of radius 1 plus a perfect weight-two matching makes every coordinate cost 2.944495. Both witnesses have full Fourier support (32/32, 64/64; affine dimension 5 and 6), so they are outside A082's affine-four class.
- Recursive composition with a balanced level-one-free inner function preserves every per-coordinate erasure ratio; large-ratio residuals come from restrictions.
- Symmetric functions never beat K* (n<=14): symmetry is the wrong search family for this lemma.
- Tooling: truth tables for n>=6 exceed int64; build the +-1 vector from Python ints. Dump search JSON before certification so a certifier crash does not lose the run.
- The subagent harness refuses report .md files; persist JSON (CLAIMS, PROGRESS, PACKET_DELTA) and return the report in the StructuredOutput.

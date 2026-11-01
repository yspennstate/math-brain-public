# R06 report 83 readback erratum

The immutable report

`runs/R06/20260920T0935Z_i0056_threeclosure_vertex_lower_83_4f8c.md`

was read back at commit `430426819663cc391fea9c1728fb98c88e4e94aa`. The JSON transport interpreted the TeX sequence `\f` in one occurrence of `\frac` while creating the file, so the displayed intersection line in Section 4 is malformed as `t_*=...rac{h}{2-h}`.

The intended and mathematically used line is

\[
t_* = \frac{h}{2-h}.
\]

No mathematical claim, numerical value, checker output, or ledger entry changes. The report is left immutable rather than silently edited after readback.

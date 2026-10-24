# B03 r23 source findings

Current source blob: bbebd6f6c5a27e9f639186a305008ab43a481e70.
Historical baseline commit: 7c0d6e60946b19423e6400a12d34b473cf0591e2.

Current paper:
- lines 1-246 PASS.
- line 247: local wording error, theorem unaffected. Multiple complement rows can have beta_i=0. Delete “are at most one”; every zero-beta factor is independent of z and bounded by one, so all can be dropped. Example U=[e1,e2] in R3 has two zero rows in its one-column orthogonal complement.
- lines 248-455 PASS after that deletion.
- lines 456-466 PASS with the current separate-coordinate negative-tail repair.
- lines 467-685 PASS.
- remaining mathematical remarks PASS; external priority UNCHECKED.

Historical baseline:
- line 270 has the same local projection wording error.
- lines 472-474 need the separate negative-tail coordinate already used in the current paper.
- remaining theorem chain PASS after these repairs.

B03 dependence-sensitive chain PASS: copies are literal product coordinates; differences are independent cap-one variables; no sum/difference or projected-coordinate independence is asserted. The old fourth-power graph determinant exponent is -1/2 before the fourth root and -1/8 afterward.

Fresh checker/Lean/PDF execution was not rerun in this invocation. Full s4 and s3 bounded-density statements remain open.

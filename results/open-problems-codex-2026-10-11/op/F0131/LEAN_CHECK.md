Lean check pending

Command submitted from ~/lean_verify:

lake env lean ~/brain_workers/TRIO_1011/op/F0131/RankOneCertificate.lean

This single queued target includes the irrational-rank-one algebra, the abstract weighted last-firing sum, and the corner-sign inequalities (also separately listed in CornerCertificate.lean). No second Lean process has been started. The shared leancheck wrapper gives a check 3600 seconds after it acquires a slot; the queue itself has no timeout. No Lean theorem is yet described as machine checked. The full PDE/convergence argument is a written proof in ATTEMPT.md and is not formalized.

Operational note: the first Set-Content command accidentally created ~/lean_verify/RankOneCertificate.lean. It was read into the problem folder; the stray file was left untouched in accordance with the instruction not to delete outside the problem folder. The queued target is the problem-folder file.

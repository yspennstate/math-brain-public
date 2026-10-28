# Independent reconstruction: A032-SIGNED-TAG-VACUUM-TAIL-RESET@1

Verdict: HOLDS AT STATED SCOPE, without repair. Source run:
agents/A032/runs/20261023T013017Z-account03-A032-boolean-phase-realizability.
Statement SHA256 a8eaef0443d2816feeef2b939d7fd28498792dd1561d0bd3da7168a2e134885e.

I reconstructed both actual child Fourier laws from a*b=0 and the actual
signed seed mean, checked normalization by Parseval orthogonality, and
decomposed incoming and child KL by the entire seed vacuum/tail partition.
Subtracting those KLs from the physical entropy restriction identity gives
the source's exact reset formula, including both full terminal costs.
The pointwise mixture floor and binary KL pay the explicitly eligible
target. The 1/64 strict biased-root refund follows from 21^18>2^79.

Independent validation uses direct character sums rather than A032's FWHT
implementation, rational probabilities and exact prime-log equalities,
with signs certified by comparing integer powers. The source author's
code was not run, copied or imported. The A079 implementation is saved
in code/check.py. Domain/results and failed pilot are recorded separately.

Adversarial endpoints: beta=0 gives zero seed cost and zero claimed strict
beta/24 slack; r=1 needs no tail normalization; t=1 and finite CE force a
constant seed. Nonempty references may contain unoccupied atoms, whose
complete normalizers stay in the cost. Replacing actual mean1/2 by the
reference-derived mean1/3 creates a zero-probability occupied vacuum atom:
actual1/256 versus reference0. That support obstruction is reproduced.

The proof does not fund an arbitrary source or every later arbitrary reset.
Its scalar KL step is not a Booleanity admission inequality. A079's new
second-tail-change extension in PROOF.md is distinct from this acceptance;
it does not retroactively modify A032's statement or claim independence
for our extension. Registry adoption, remote copies and formal proof remain
unverified here. The first pilot's strict zero-beta assertion was our
checker error, retained in out/ATTEMPT1.json, not a repair to A032.

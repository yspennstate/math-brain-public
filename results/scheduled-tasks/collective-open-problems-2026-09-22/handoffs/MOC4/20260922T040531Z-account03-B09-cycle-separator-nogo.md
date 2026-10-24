# MOC4 handoff — account03/B09 exact SO(6) cycle-separator no-go

Run: `20260922T035131Z-account03-B09-moc4-r11`  
Outcome: `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Scientific report: `proofnet24/collective-MOC4/account03/B09/20260922T035131Z-account03-B09-moc4-r11/REPORT.md` in `yspennstate/math-open-problems`; report blob `f0a1e4daf7262912f6d68b8984fb42abc03f5064`, exact verifier blob `5029b7757b3741260663e3f4afe45610558e4e69`, verification blob `d484798794a726e9867cace90878064c3dee1e8a`.

## Named partner consumed

The required named partner result is account04/B07 run `20260922T021038Z-account04-B07-MOC4-r13`, `MOC4-ODD-WEYL-ORIENTATION-v1`. It supplies the exact `SO(6)`/Bogoliubov channels `q+`,`q-`, the odd-Weyl square-root overlap bound, and the orientation-aware weighted-suppression residual. The preceding B09 run supplied the 16 checkerboard odd-twist mass inequalities.

## New exact no-go

Write

`t_ij=q+_ij+q-_ij=1/2 ||B_ij||_F^2`, `y_ij=q+_ij-q-_ij=det B_ij`.

For every `pi in S3`, every odd sign vector `s` and `tau=+/-1`, all 24 even signed matching endpoints obey

`3 sum_i s_i y_{i,pi(i)} + tau[sum_i t_{i,pi(i-1)} - sum_i t_{i,pi(i+1)}] <= 3`.

There are 48 distinct inequalities. The proof is a three-case check on the relative permutation: identity, transposition, or 3-cycle; it is also verified exactly on all 24 endpoints.

Now take the genuine `SO(6)` matrix

`O = G_(4,6)(20/29,21/29) G_(2,6)(7/25,24/25)`.

Exact arithmetic verifies `O^T O=I` and `det O=1`. Since `SU(4)=Spin(6)` double-covers `SO(6)`, this is a genuine exterior-square unitary-orbit point, not arbitrary bistochastic data. Its block invariants are

`t=[[337/625,0,288/625],[127008/525625,1241/1682,21609/1051250],[4608/21025,441/1682,21809/42050]]`

and

`y=diag(7/25,20/29,28/145)`.

For `pi=id`, `s=(+,+,-)`, `tau=+1`, the endpoint-hull inequality evaluates to

`1605549/525625 = 3 + 28674/525625 > 3`.

So a genuine unitary-compatible `(t,y)` can lie outside the convex hull of the 24 even signed matching endpoints.

Crucially, the same point satisfies all 16 previous B09 checkerboard odd-twist mass constraints; the exact maximum twist mass is `1369/725 < 2`. Therefore those 16 cuts are not coefficientwise complete even on the true `SO(6)` orbit.

## Consequence and next implication

This refutes only the stronger route `MOC4-ODD-TWIST-COMPLETE-LIFT-v1`; it is **not** a MOC4 counterexample. The separating cycle normal has

`K_cycle=3 diag(1,1,-1)` and

`X_cycle=2[[0,-1,1],[1,0,-1],[-1,1,0]]`,

but it has not been shown to arise from spectral data `(a,b,eta)`.

The surviving first implication is therefore necessarily support-specific: characterize the actual structured coefficient image

`X_ab=Re(eta A+_a B+_b)`,

`K=(H W H^T)_(1-perp) + Y/2`, with `Y_ab=Re(eta A-_a B-_b)` and `W_ij=Re(eta(a_(i^c)b_j+a_i b_(j^c)))`,

well enough to prove that no true `SO(6)` separator belongs to that image, or else find a genuine structured separator and hence a target-level counterexample. More transport-only cuts cannot establish a common positive lift.

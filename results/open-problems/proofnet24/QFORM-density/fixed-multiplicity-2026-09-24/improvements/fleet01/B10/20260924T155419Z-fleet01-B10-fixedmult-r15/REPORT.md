# B10 r15 improvement

I checked the fleet03/B13 s8 retune at math-open-problems commit e9a425b9ec3455dfe13b787fb259dec11aa1b176. Exact-constant verdict: PASS in this B10 review, subject to the local hyperbolic negative-tail coordinate repair in the sibling audit. This is not an owner validation flag.

Checked exact margins: inner s5 interpolation 3/500; inner full half potential <105/2; outer collar delta >559973047/4840000000 >23/200; robust pair g>529/80000; two-high leverage exclusion margin 151339/3513840000>0; one-high diagonal-dominance margin 31/440; W_dis>1/12000 and terminal receiver<60; large-V3 branch <2135727/6125<349; outer scalar squared slack 526; pair branches <28 and <138. Thus the candidate s8 bound <349 K^2/s survives this exact audit. Global continuity is not claimed.

New s7 reduction using eta=1/44 and kappa=1/138: if s_7(A)>=1, there is no outer pivot, and V_3<kappa^3, then V_2>=kappa^2 and
W_cross_(2,1)>43/876024.

Reason: the r=0/r=1 volume argument still closes under s7. At r=1 the completion rank is at most3, so s7 forces at least four large diagonal entries of D; two complement entries already contradict restricted rank1 by the same 2x2 diagonal dominance. Hence V2>=kappa V1>=kappa^2. The proved overlap theorem gives
W_cross_(2,1)+9V3 >= V2*T6.
Since s7>=1, T6>=1, so
W_cross_(2,1)> (1-9/138)kappa^2 =43/876024.

All s7 pivot branches are already paid: a scalar pivot leaves at least six Schur directions, enough for the s5 half-potential; definite pairs are direct; indefinite pairs leave more than the single direction required by the log-potential argument. If V3>=kappa^3, the third-volume receiver gives <349. Therefore s7 is reduced to a single positive overlap-one shared-coordinate receiver problem. This is not an s7 theorem; the shared original coordinate cannot be treated as an independent copy. Full s3 remains open.

# Checks — 20260923T145730Z-fleet01-B20-QFORM-auto11

All checks below are exact arithmetic or direct deterministic identities used in `REPORT.md`.

1. `E0=11907/16384` and `(36/37)E0=107163/151552`.
2. `107163/151552 -169/256 =7115/151552>0`; hence the R1 lower bound implies `s1>13/16`.
3. N3 physical entry cap: `1/4096+1/64=65/4096`, hence `|N_ij|<sqrt(65)/64`.
4. `sqrt(65)/52+1/16<7/32`: after subtracting `1/16`, this is `32sqrt(65)<260`; squaring gives `66560<67600`.
5. If a probability vector has each atom `<7/32`, greedy stopping at mass `25/64` gives a subset mass in `[25/64,39/64)`, so both it and its complement have mass at least `25/64`.
6. R1 restricted operator norm: `(5/8)-(1/16)=9/16`, and `(9/16)(13/16)=117/256`.
7. Fleet02/B20 absolute tube inheritance: for any coordinate restrictions `P_L,P_R`, `||P_L(N-N_2)P_R||_op<=||N-N_2||_op=s3(N)<1/64`.
8. `delta=726327/33554432`.
9. `delta^2/4=527550910929/4503599627370496=1.1713983359507019e-4`.
10. `delta^2/16=527550910929/18014398509481984=2.9284958398767547e-5`.
11. Independent random row/column two-colorings separate any fixed row pair with probability `1/2` and any fixed column pair with probability `1/2`, hence capture one quarter of total squared 2x2-minor mass in expectation.
12. `(ad-bc)^2<=2(a^2d^2+b^2c^2)` gives `P2<=2(E11 E22+E12 E21)` after summation, hence one matching product is `>P2/4>delta^2/16`.

No numerical experiment, asymptotic approximation, or random-tail deletion is used in the proof.

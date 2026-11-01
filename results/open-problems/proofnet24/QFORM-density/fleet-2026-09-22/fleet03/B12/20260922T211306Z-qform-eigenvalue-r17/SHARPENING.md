# Exact numerical sharpening of the three-bank completion theorem

The proof in `REPORT.md` states the round constant `300/s`. The same proof, with no additional premise, gives the slightly sharper clean bound

`||p_Q||_infinity < 296/s`.

Indeed, in the diagonal-pivot branch the exact constant is

`256*(9/16)^(-1/4)=512/sqrt(3)<296`,

because `512^2=262144 < 262848=3*296^2`.

In the small-diagonal/indefinite-pair branch the rational certificates in `REPORT.md` give `D>1/40` and `kappa>1/50`, hence

`C_pair < 6*400^(1/3)*80000^(1/6) <291<296`.

The second strict inequality follows by raising positive quantities to the sixth power:

`6^6*400^2*80000 = 597196800000000 < 607236591593241 = 291^6`.

Thus `QFORM-THREE-DISJOINT-BANK-ARBITRARY-COMPLETION-v1` may be quoted with universal constant `296/s`. The exact checker `CHECK.py` and its executed finite-arithmetic record `CHECK_RESULT.json` accompany this note. These calculations verify only the numerical inequalities; they are not an independent mathematical review of the analytic dependencies.

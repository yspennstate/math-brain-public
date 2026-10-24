SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T22:35:40Z.
attacking: second-order optimization of the sharp three-bank cube witness at fixed total dimension, plus a source-valid application of the latest account02/B17 rough one-sheet barrier.

Status at start: full unrestricted QFORM OPEN; continuity separate; WITHOUT_VERIFIED_BRAIN.

Early substantive calculation.  From the completed exact cone Edgeworth formula for a three-bank Parseval cube frame, align the negative spectral axis with bank 3, so (u1,u2,u3)=(0,0,1).  The exact one-bank/pair coefficients are

h4(0)=57/32, h4(1)=3/4,
a0:=h6(0)/105+h8(0)/800=-4833/327680,
a1:=h6(1)/105+h8(1)/800=-173/17920,
b00:=k44(0,0)/400=7803/819200,
b01:=k44(0,1)/400=603/51200.

For m1=m2=yN, m3=xN, y=(1-x)/2, the expansion becomes

p_Q(0)/(3 sqrt(2)) = 1-K(x)/N+H(x)/N^2+O(N^-3),
K(x)=[228/(1-x)+24/x]/640,
H(x)=-(97955 x^2-47608 x+6920)/(716800 x^2(1-x)^2).

The first-order minimizer is x*=sqrt(6)/(sqrt(6)+sqrt(57)), giving
K* = 63/160+3 sqrt(38)/80.
Direct symbolic substitution gives the new second-order coefficient
H* = (-1299963+108550 sqrt(38))/13619200 = -0.0463181288165... .

Thus the first-order optimal bank allocation has a definite negative second-order correction; the next task is to prove that no O(1/N) orientation perturbation can improve this N^-2 term and to package an exact genuinely rotated sequence with squared orientation leakage o(1/N).

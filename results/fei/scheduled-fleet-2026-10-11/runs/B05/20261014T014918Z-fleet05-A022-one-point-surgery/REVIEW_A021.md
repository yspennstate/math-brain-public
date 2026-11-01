# Scoped independent reconstruction: relative-bias point-switch upper price

Source: A021-POINT-SWITCH-RELATIVE-BIAS-PRICE v1, run
20261014T011316Z-fleet05-A021-rare-core-asymptotics, DERIVATION.md §§1-2.
Verdict: HOLDS for the all-dimensional upper bound and its K6/K7 contrast
consequences ONLY. No acceptance of the whole bundled claim, its optimal
supremum lower bound, three-event application or finite outputs is inferred.
No repair or change of hypotheses was supplied; A022 is not a contributor
to the reviewed source version.

Reconstruction from the tensor spectrum: at a query with j-1 remaining
point controls, rho=2^{-(j-1)}, the control indicator has 1/rho Fourier
coefficients of magnitude rho. Put Delta=(Hhat-Ghat)/2, with sum Delta^2=gamma.
All nonempty remaining-control labels have parent amplitudes rho Delta and
-rho Delta. Thus their erasure is exactly
2(rho^-1-1)rho^2 gamma=2(1-rho)d, d=rho gamma.

For the remaining-control-empty sector, the two amplitudes are Ghat+rho Delta
and -rho Delta. On nonempty data labels their derivative mass M is at most
rho^2 gamma and total packet mass P is at most
2Var(G)+4rho^2 gamma<=8eta+4rho^2 gamma.
Log-sum and Psi(u^2,v^2)<=v^2 log2(e(u^2+v^2)/v^2) give
cost<=rho^2 gamma log2(e(8eta/(rho^2 gamma)+4)).
The two replacements are legitimate: Pstar>=rho^2 gamma, and
x log2(ePstar/x) increases for x<=Pstar.

The empty data row must be kept separately. Coupling gives
|Delta_empty|<=gamma, hence its derivative mass M0<=rho^2 gamma^2.
Parent Parseval puts its packet total at most1, so the row costs at most
h2(M0)<=rho^2 gamma^2 log2(e/(rho^2 gamma^2)). After division by d,
this is bounded by max_(0<=x<=1) x log2(e/x^2)=2log2(e)/sqrt(e).
This bound is dimension independent and does not replace the full erasure
with h2(d).

Writing L=log2(e)+log2(8eta/gamma+4), the rest of B/d is at most
2+rho(L-2+2log2(1/rho)). For rho=2^-l, this is <=max(4,L): use
1+l<=2^l when L<=4, and 2l<=2(2^l-1) when L>=4.
Therefore the displayed source bound follows exactly. Gamma=0 is handled
as an irrelevant query; no positive-gamma argument is applied to it.

The strict K6 and K7 comparisons follow from the source's positive-series
rational bounds ln2>9/13 and sqrt(e)>13/8, plus
(28/5)^2<32 and 12^5<2^18. These inequalities give upper prices below6
for eta/gamma<=1/5 and below307/45<7 for eta/gamma<=1, respectively.
All constants, source weights and zero-row conventions survive the
independent tensor reconstruction. The downstream use in this stage is
to identify the large-contrast gap; the new A022 data-exposure theorem
does not assume this upper price as a proof premise.

The stage's separate CONTRAST_OVERLAP_WITNESSES.json replays controller-first
bent/point-flip roots at k=4,6,8 using A022's signed Walsh implementation,
including a rigorously bad K4 root. These scoped replays illustrate
the local-price obstacle; they are not a reconstruction of every lower-bound
quantifier in the source's P(theta) theorem. Source files and registries
remain read-only. Independent review of the new A022 theorem is still pending.

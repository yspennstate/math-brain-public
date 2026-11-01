# E0011 soft-annulus second-run idea — written before checker

Model target: Durrett 2009 Problem 5, original two-dimensional no-stirring catalyst/ZGB model at the trial anchor p=1/2, q=1, r=infinity.

This artifact records the mathematical idea before any run-2 checker is written. It does not claim metric movement or source closure.

## B14 — quotient the first soft-annulus excursion by symmetry

For an a x b rectangular annulus A_{a,b}, a,b>=3, take the perimeter vacant, strict interior O, and exterior CO. The perimeter has

P = 2a+2b-4

vacancies and exactly P vacant-vacant nearest-neighbor edges. At p=1/2, multiply all effective rates by 4. Each vacant-site CO clock has weight 2 and each 00 O2 edge has weight 1, so total initial weight is 3P.

Up to translations and rectangle dihedral symmetries, the first event lies in four local orbit types:

1. CO at one of the 4 corners: total weight 8;
2. CO at one of the P-4 noncorner perimeter sites: total weight 2(P-4);
3. O2 on one of the 8 corner-adjacent perimeter edges: total weight 8;
4. O2 on one of the P-8 noncorner-noncorner perimeter edges: total weight P-8.

For P=12 (the 3x5 and 4x4 rectangles), the orbit probabilities are 2/9, 4/9, 2/9, 1/9.

Under an O2 event the two newly deposited O atoms immediately react with outward CO atoms. The original perimeter sites therefore return to vacancy, and exactly two exterior collar CO sites become vacant. If the O2 edge is noncorner-noncorner, the two collar defects are adjacent. If it is corner-adjacent, the corner endpoint has two outward CO choices at equal reaction rate, so with probability 1/2 the collar defects are adjacent and with probability 1/2 they are separated.

Thus the depth-two soft-collar excursion can be quotiented further to only two post-O2 defect geometries: ADJACENT or SEPARATED.

## Exact immediate RETRY self-loop

Define R to be the event that the first effective event is O2 on the annular perimeter and the next two effective events are CO adsorptions into exactly the two new collar vacancies, in either order. On R no other event occurs; both collar vacancies are refilled and the exact original annulus A_{a,b} is restored. Therefore R is a source-valid exact RETRY event for any trial whose seed class contains A_{a,b}.

After an O2 event with adjacent collar defects:

- vacancy count is P+2;
- E_00 is P+3 (the old cycle, two ring-defect edges, one defect-defect edge);
- total scaled rate is 3P+7.

The two target refill clocks have total weight 4. After the first refill, V=P+1 and E_00=P+1, hence total scaled rate 3P+3; the last target refill has weight 2. Therefore

r_adj(P) = 8 / ((3P+7)(3P+3)).

For separated collar defects, E_00=P+2 immediately after O2, hence total scaled rate 3P+6, and

r_sep(P) = 8 / ((3P+6)(3P+3)).

There are P-8 noncorner-noncorner O2 edges, all producing ADJACENT defects, and 8 corner-adjacent O2 edges, each producing ADJACENT/SEPARATED with probability 1/2. Since each O2 edge has initial weight 1 out of 3P,

R_P = ((P-4)/(3P)) r_adj(P) + (4/(3P)) r_sep(P).

For P=12 this becomes

r_adj = 8/1677,
r_sep = 4/819,
R_12 = 508/316953 = 0.0016027612926837733...

The same exact RETRY mass applies to 3x5 and 4x4 because it depends only on P and the local corner/noncorner orbit counts.

## B24 — minimal rectangular neutral seed screen

Use the existing exact CO-only poisoning recursion, but now classify every rectangular neutral annulus with perimeter P<=12. Up to swapping side lengths these are

P=8: 3x3;
P=10: 3x4;
P=12: 3x5 and 4x4.

The checker will recompute exact poison probabilities for all four. The intended finite statement is only:

- identify the minimum rectangular perimeter at which the pure-CO poisoning path drops below 1/64;
- at that first passing perimeter, compare the two rectangles;
- combine with the formula above, noting that both P=12 rectangles have the same immediate exact RETRY mass.

No claim is made that the pure-CO path is FATAL for every soft location-flexible seed class; the previous report correction remains binding. This is a candidate-quality screen, not a universal rejection theorem.

## B30 — localized 4x4 conclusion sought

If the exact recomputation confirms the earlier values, 4x4 will be the smallest square neutral annulus that passes the pure-CO 1/64 necessary filter, and among the two perimeter-12 rectangles it will have the smaller pure-CO poison probability while having the same certified immediate RETRY mass R_12.

This would justify concentrating the next full SUCCESS/FATAL/RETRY automaton on the 4x4 annulus with a sacrificial collar and a farther quarantine layer. It does not yet define SUCCESS or certify a>63f, so M_reg remains 0 unless a complete trial is found later in the same run.

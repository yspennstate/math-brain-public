# T111, optimal Berry-Esseen constant: status and a three-point probe (14 Nov 2026, an agent)

## Status (abstracts read on arXiv 14 Nov)
- Conjectured value C_E = (sqrt(10)+3)/(6 sqrt(2 pi)) = 0.409732 (Esseen 1956), approached by a two-point law.
- Two-point (Bernoulli) summands: settled for every n by J. Schulz (2016, Trier dissertation), as cited in
  Zolotukhin-Nagaev-Chebotarev arXiv:1810.09681 (who also check n <= 500000 by computer).
- All laws, large n: He-Cheng arXiv:2609.06358v3 prove C_E suffices for n >= 2 ceil(exp(10^17)).
- All laws, all n: open. iid upper bound on the row is 0.4748 (Shevtsova, arXiv:1111.6554).
- Not on the row, nearby: Ling arXiv:2611.02195 (multivariate, dimension-free constant 980 over convex sets).

## Probe (probe.py, run1.out)
Exact Delta_n for iid three-point laws from the multinomial law of the atom counts, n <= 60;
300 random laws scored on n <= 25, four Nelder-Mead climbs.
- Esseen's two-point law: max over n <= 60 of sqrt(n) Delta_n / beta3 is 0.409242 (n = 58), below C_E.
- Best random three-point law: 0.3979.
- All four climbs ended with two atoms merged (a two-point law, p near 0.41), ratio 0.4082-0.4092, below C_E.

Reading: no three-point law beats the two-point family at small n in this search. Consistent with the
conjecture and with the known picture that the extremal is two-point; not evidence beyond that (heuristic
search, n <= 60, three atoms). Nothing here is a result. The gap that matters is n between 61 and exp(10^17)
for general laws, which no computation reaches.

## Second run, n <= 200 (Mac mini 1, seeds 11 and 12; p200_s11.out, p200_s12.out)
- Esseen's two-point law: 0.409590 at n = 199. Gap to C_E 0.000142, down from 0.000490 at n = 58,
  so along this law the ratio climbs toward C_E from below as n grows, as Esseen's asymptotics say.
- Best random three-point law (scored on n <= 25): 0.4052.
- All six climbs again end two-point (one atom with mass under 0.04 merged or vanishing),
  0.409536-0.409550 at n = 185-192, below the exact two-point law.
No three-point law found above the two-point family for n <= 200.

## Next, if anyone returns
A useful sharper test is the Esseen-type expansion: for fixed law the ratio tends to a limit given by the
lattice/non-lattice Edgeworth term; the extremal problem over laws of that limit is Esseen's 1956 computation.
The open part is uniformity in n, which is analytic (He-Cheng's route), not numeric.

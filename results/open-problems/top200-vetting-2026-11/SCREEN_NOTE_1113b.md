# Screen of the 13 kept DL candidates against the live list (an agent, 13 Nov 2026 20:2x)

screen_candidates.py on list.jsonl (464 ids, T450-T464 included): SCREEN_IN_1113b.tsv -> SCREEN_OUT_1113b.tsv,
titles of every hit read by hand. Ten of the thirteen candidates are already live rows:
C01 = T226 (edge of stability), C03 = T231 (leap complexity), C04 = T301 (depth 3 vs 4), C05 = T235 (grokking),
C07 = T265 (benign overfitting outside near-orthogonal data), C09 = T227 (catapult), C10 = T306 (iteration
complexity of diffusion samplers), C11 = T271 (neural collapse under real training), C12 = T447 (uniform minimal
width), C13 = T325/T326 (in-context regression). Free: C06, C14, C18.

So REPLACEMENTS_1113b.tsv is not landed. The thirteen BORDERLINE rows stay live until each has a free, litchecked
replacement; the list keeps 200 deep-learning rows. Owed: 10 + 2 (T420, T422) new candidates, screened against
list.jsonl BEFORE the literature check.

## 13 Nov 23:0x: C06 and C18 settled (an agent)

- C18 landed as T466, restated: "Does exact ReLU representation of the maximum of n numbers need depth growing with
  n?" (Hertrich-Basu-Di Summa-Skutella 2105.14835; their log_2 conjecture disproved by Bakaev-Brunck-Hertrich-Stade-
  Yehudayoff 2505.14338 v3; growing lower bounds only for integer or decimal-fraction weights). The screened form
  (minimal width at depth k) was not the question the literature asks. T419 (LoRA) retired with x= in rows_30.py.
- C06 dropped: "GD convergence for deep ReLU nets at polynomial width below NTK" has no printed open statement and is
  already eaten from below (Nguyen 2101.09612: linear widths; Bombari-Amani-Mondelli 2205.10217: sqrt(N) neurons,
  Omega(N) parameters, with GD guarantees). T339 stays live BORDERLINE until a better candidate is found.
- Still PENDING: T339, T420, T422 need new candidates.
- 13 Nov 23:1x: T422 (critical batch size) retired; replaced by T467 "The optimal convergence exponent of gradient
  descent with a stepsize schedule" (Kornowski-Shamir COLT 2024 open problem; silver stepsizes 2309.16530; anytime
  2411.17668; lower bounds 2607.02053 and 2609.04032: non-anytime exponent in [1.2716, 1.450], anytime in
  [1.119, 1.184]). Screened free against list.jsonl (no stepsize/silver/anytime row). Still PENDING: T339, T420.

## 14 Nov 01:1x: PENDING list empty (an agent)

- T420 (RG flow) retired; replaced by T468 "Is the power of deep learning over linear models inherently distribution
  dependent?" (Feldman-Kamath-Srebro, COLT 2026 invited open problem, PMLR 336 pp. 7117-7122, Open Questions 1-2).
  Push 163 = f2992582.
- T339 (approximation rates of generative networks) retired; replaced by T469 "How much overparameterization does
  alternating least squares need to decompose a tensor?" (Arvanitakis-Srinivas-Vijayaraghavan, COLT 2026 open
  problem, PMLR 336, Open Problems 1-3). Push 164 = 082d3a87.
- All four 13 Nov BORDERLINE deep-learning rows (T339, T419, T420, T422) are now replaced by T466-T469, each with a
  printed locator. Nothing is PENDING. Next free id T470.
- Unscreened COLT 2026 candidates (PMLR 336) for later: Nissim (does differential privacy make PAC learning much
  harder), Lau et al. (is interaction necessary for 1-bit mean estimation), Balcan (online optimization of
  piecewise-Lipschitz functions). Screen against list.jsonl before any literature check.

## 14 Nov 20:11: famous-list replacements, batch 1 screen (an agent)

TOP200_FAMOUS holds 187 after the 13 retirements of 14 Nov (T001 T013 T022 T031 T063 T078 T115 T123 T129 T137 T189 T214 T425); 13 replacements owed.
FAMOUS_CANDIDATES_1114.tsv (22 candidates) screened by screen_candidates.py -> FAMOUS_SCREEN_1114.tsv. Already on the list (title hit, read by hand):
F01=T047 F02=T101 F03=T030 F04=T017/T138 F05=T069/T289 F06=T066 F07=T109/T140 F08=T008/T028 F09=T050 F11=T031/T071 F13=T003/T015
F14=T004 F15=T218 F16=T127 F18=T143 F19=T012/T104 F20 within T005 F21=T070 F22=T097.
Free after the screen: F10 (random conductances, heavy-tailed quenched CLT in d=2), F12 (directed polymer in d=3; T125 and T215 are other polymer questions), F17 (random interlacements u_*=u_**=bar u).
The list already carries most well-known problems; batch 2 must reach further (less obvious famous problems), screened before the literature check.

## 14 Nov 20:16: famous-list replacements, batch 2 screen

FAMOUS_CANDIDATES_1114b.tsv (G01-G23) screened against list.jsonl -> FAMOUS_SCREEN_1114b.tsv.
Free by title and text: G02 (infinite collision property on the percolation cluster), G07 (internal DLA
fluctuations in d >= 3), G09 (random sequential adsorption jamming limit in the plane), G11 (favourite sites of
planar simple random walk), G22 (random polynomials, universality of the number of real zeros).
G17 (exact LQG dimension d_gamma) is NOT free: T037 asks for d_gamma for gamma other than sqrt(8/3) outright.
Every other G candidate overlaps a live row (see the screen file). Free so far across batches 1-2: F10 F12 F17
G02 G07 G09 G11 G22 (8 of the 13 owed). Each still needs the arXiv literature check before a row is written.

## 14 Nov 20:25: famous-list replacements, batch 3 screen

FAMOUS_CANDIDATES_1114c.tsv (H01-H22) -> FAMOUS_SCREEN_1114c.tsv. Free by title: H08 H11 H12 H17 H18; read by hand:
H08 (Airy universality for general-weight LPP) is covered by T005 (KPZ universality beyond solvable models), not free.
H17 (random close packing) is not a sharply posed problem and sits next to T080 and G09; dropped.
H12 (exact Boolean-model critical intensity) and H18 (exact site p_c on Z^2) ask for a value nobody expects in closed
form; kept only as weak backups. H11 (Swendsen-Wang mixing at criticality on Z^2) is free and kept.
Found while reading H18's text hits: T441 (rank 357) is the same problem as T088 (rank 66), the chemical-distance
exponent of critical planar percolation, stated from Damron-Hanson-Sosoe instead of Schramm's ICM list. T441 retired
as a duplicate; it sat outside the top 200, so no tier count moves (retired 84 -> 85).
Free so far: F10 F12 F17 G02 G07 G09 G11 G22 H11 (9 of 13 owed), backups H12 H18.

## 14 Nov 20:32: famous-list replacements, batch 4 screen

FAMOUS_CANDIDATES_1114d.tsv (J01-J20) -> FAMOUS_SCREEN_1114d.tsv. Ten are free by title, but most are either not
top-200 in fame (J01 Wiener sausage, J02 lamplighter speed, J09 voter consensus time, J15 critical-bias GW walk) or
already settled (J12 GEF hole probability, Nishry; J17 uniqueness at p_u in the hyperbolic plane, Benjamini-Schramm;
J11 RFIM d=2 decay, Ding-Xia; J06 exceptional times d=2, Garban-Pete-Schramm). J04 (second-order term of the
2-neighbour bootstrap threshold) is free: T008's hit is the conformal bootstrap. It may be settled by Hartarsky and
Teixeira (2024), so it needs the literature check before it counts.
Famous-candidate pool at this depth is thin: 9 free (F10 F12 F17 G02 G07 G09 G11 G22 H11), J04 pending, weak backups
H12 H18. Next: arXiv literature check of these 12, then write the survivors as rows after T466.

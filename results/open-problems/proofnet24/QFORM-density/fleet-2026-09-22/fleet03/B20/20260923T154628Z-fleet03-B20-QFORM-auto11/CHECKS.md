# Deterministic constant checks — fleet03/B20 auto11

These arithmetic checks support the analytic proof in `REPORT.md`; they are not Monte Carlo evidence and are not used as a substitute for proof.

- `tau = 2^-20 = 0.00000095367431640625`
- `eta = 1/16 = 0.0625`
- incoming `eps_* = 0.07641336241474038218...`
- in-plane carrier floor: `1-eps_*-2eta = 0.7985866375852596178...`
- transverse physical-cut energy floor:
  `E_perp=(eta-tau)^2/4 = 4294836225/4398046511104 = 0.000976532697904986...`
- D5 lower bound used:
  `e5 > 64^-4 E_perp^5 / 120 = 4.4109568185307965e-25...`
- fleet04/B20 D5 density constant:
  `5 sqrt(2e) e5^(-1/10) = 3178.183455169147... < 3178.184`
- strong-top4 plus `s3>=1/256`:
  `Delta3 > sqrt((63/256)E_perp)/65536 = 2.3654499114484398e-7...`
- grouped-rank3 density constant:
  `3e Delta3^(-1/3) = 1318.5941698999404... < 1318.595`
- exact rank-three in-plane Fresnel endpoint:
  `12/(1-eps_*-1/8) = 15.026547446730653... < 15.027`

Algebraic identities checked in the proof:

1. for symmetric `B`, `B-PBP=(I-P)B+PB(I-P)` and `||B-PBP||<=2||(I-P)B||`;
2. disjoint block errors combine by maximum operator norm, not by sum;
3. for symmetric zero-diagonal `H`, a fair physical two-coloring satisfies `E||H[D1,D2]||_F^2=||H||_F^2/4`;
4. strong top four plus `s3>=1/256` implies `s1s2s3>sqrt((63/256)E_perp)/65536`.

`STATUS=PASS`.

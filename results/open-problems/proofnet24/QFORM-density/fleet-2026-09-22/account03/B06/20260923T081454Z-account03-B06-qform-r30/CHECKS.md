# r30 checks

These are sanity checks only; the proof is the symbolic exterior-square argument in REPORT.md.

Exact constants:

- `kappa=sqrt(127/800)=0.3984344362627307...`
- paid-base coefficient `4 sqrt(3e)/sqrt(kappa)=18.096284948781438...`
- same-side transfer coefficient `kappa/2=0.19921721813136534...`
- forced single same-side star norm `sqrt(kappa/2)=0.4463375607445169...`
- after the compatible account04/B18 dependent-square splice: `2 sqrt(18.096284948781438)=8.50794568595297...`

A local deterministic random-vector test over 10,000 Gaussian quadruples `(s,r,c,t)` checked

`abs(||s||||t||-||c||||r||) <= ||alpha||||beta|| sin(angle(alpha,beta))`

with maximum numerical violation `0` at floating precision. This is only a finite check of the exact inequality

`|ST-CR| <= ||s tensor t-c tensor r||_F <= ||alpha wedge beta||`.

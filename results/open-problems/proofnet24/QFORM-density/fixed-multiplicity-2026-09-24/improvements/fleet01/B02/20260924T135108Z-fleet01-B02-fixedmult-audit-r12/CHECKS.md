# Exact checks for B02 r12 `<549` candidate

These are finite arithmetic checks supporting, not replacing, the symbolic proof in `IMPROVEMENT.md`.

- Retuned parameters: `eta=1/21`, `sqrt(kappa)=1/18`, `kappa=1/324`.
- `r=0` norm sum: `1/21+1/18=13/126<1`.
- Worst `r=2` diagonal-dominance comparison reduces to `4*sqrt(22)<19`; squared slack is `19^2-16*22=361-352=9>0`.
- `r=1`: using `sqrt(22)<5`, the off-diagonal bound is `<22/63` while the diagonal lower bound is `53/63`.
- Order-three cut scale: `(4^(-3) kappa^3)^(-1/6)=36`.
- Order-two cut scale: `(4^(-2) kappa^2)^(-1/8)=6`.
- Rational `C3` envelope: `3*(99/70)*(87/32)*(9/7)=232551/15680`; its gap below `15` is `2649/15680>0`.
- Rational `C2^2` envelope: `64*(11/4)*(6/7)=1056/7<169`, hence `C2<13`.
- Gamma envelope: `1348/627+3/8=12665/5016<81/32`.
- Quarter-power coefficient envelope product: `(31/20)(19/25)(22/15)(81/32)=174933/40000`; gap below `35/8` is `67/40000>0`.
- Scalar-pivot outer contribution before the final `sqrt(21)` tail is `21*(259/10)=5439/10=543.9`; since `sqrt(21)<5`, the branch is `<548.9<549`.
- No-pivot branch is `<15*36=540`; definite and indefinite pair branches are `<16` and `<95` respectively.

All inequalities are strict where the proof requires strict diagonal dominance.
# r38 finite algebra/constant checks

The deterministic diagonal-packet normal form was checked on 1000 random real tuples `(c,p,g,d)` with `|c|` kept away from zero. With

`H0=-pp^T/c`, `K=d H0-gg^T`, `O p=(||p||,0)`, `O g=(m,n)`, `rho=||p||^2/c`,

the maximum entrywise discrepancy in

`O K O^T = -[[rho d+m^2,m n],[m n,n^2]]`

was `1.43e-14` (double precision).

The front constant in Theorem 4.1 is

`8(2e)^(1/4)=12.215777290955167`.

For the concrete r30/r32 subbranch

`|c|>=s/16`, `S_i^off>=81 s^6/2^24`,

the resulting coefficient is

`8(2e)^(1/4)(1/16)^(-1/4)(81/2^24)^(-1/8)
 =112.84451691669572`,

so the rounded report bound `<112.845/s` is valid.

These finite checks support arithmetic/algebra only; they are not substitutes for the analytic proof in REPORT.md.
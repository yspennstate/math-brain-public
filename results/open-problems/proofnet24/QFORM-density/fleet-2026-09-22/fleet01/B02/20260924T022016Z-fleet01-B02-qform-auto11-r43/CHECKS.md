# r43 deterministic checks

Run: `20260924T022016Z-fleet01-B02-qform-auto11-r43`.

All checks are coefficient/arithmetic checks; no Monte Carlo evidence is used.

Let

- `zeta=2^-48`, `tau=2^-11`;
- `P_*=4/9-2*zeta/tau`;
- `T_*=zeta/P_*`;
- `W_*=(256/27)zeta/P_*`;
- `epsilon_*=sqrt(8W_*+2T_*)`.

Exact / high-precision values:

`P_*=274877906935/618475290624=0.4444444444298925...`

`T_*=7.993605777562852e-15`

`W_*=7.579122515022556e-14`

`epsilon_*=7.888707199262311e-7`.

At the partner `E3>=zeta` gate,

`zeta^(-1/6)=2^8=256`,

so with `C3=10.3450832321475`,

`C3*zeta^(-1/6)=2648.34130742976`,

`2*pi*C3*zeta^(-1/6)=16640.019191239444`.

For the coordinate-core branch,

`1/8-23*epsilon_*=0.12498185597344169...>0`,

and

`2*sqrt(6*pi*23)/(1/8-23epsilon_*)=333.19425574764335...`.

After absorbing at most 22 large diagonal entries,

`gamma_*=1-1/8-epsilon_*=0.8749992111292801...`,

`sigma_*=sqrt(3)*gamma_*/8-epsilon_*=0.1894420974116051...>0`.

Thus

`C3/sigma_*=54.60815401378557...`,

`2*pi*C3/sigma_*=343.11315095161746...`.

## Algebra checks

1. **Exterior monotonicity under completion.** `B=A[[n]\C,C]` is obtained from `M=A[R,C]` by adding rows. Since `E2` is a sum of squared literal `2x2` minors, `E2(B)>=E2(M)` exactly.

2. **Low-E3 identity.** For squared singular values `y1>=y2>=...`, writing `T=sum_{k>=3}yk`, `R2=sum_{3<=k<l}ykyl`, `R3=sum_{3<=k<l<m}ykyl ym`,

`2e3-y2(e2-y1y2)=y2(y1-y2)T+(2y1+y2)R2+2R3>=0`.

3. **Ultra-rank-two tail.** From `e3>=y1y2*T` and `y1y2>P_*`, `T<zeta/P_*=T_*`.

4. **Aggregate-transfer threshold.** r37 gives `E3(new cut)>=(27/256)y1y2 W`. Thus `W>=W_*=(256/27)zeta/P_*` forces `E3>=zeta`.

5. **Global tail norm.** The r37 block supports are Frobenius-orthogonal, hence `||E_0||_F^2<8W_*+2T_*`; no random quadratic perturbation estimate is inferred from this.

6. **Rank bookkeeping.** Two same-bank approximants contribute rank at most 8 each and the symmetric rank-two crossing contributes rank at most 4, giving `rank R_0<=20`. Absorbing at most 22 physical diagonal coordinates gives `rank R_42<=42`.

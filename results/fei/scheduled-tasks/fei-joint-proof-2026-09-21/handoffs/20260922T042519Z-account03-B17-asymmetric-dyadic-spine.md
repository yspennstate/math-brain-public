# account03/B17 handoff — exact asymmetric arity-5 dyadic spine

Status: **ESSENTIAL_STEP_APPLIED / FULL FEI OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Candidate attacked: `LIMIT-PRIME-GATE-LIFT-v1`, with `C_*=6.5218512` and `Gamma_*=Gamma_RO+0.2682048 p(1-p)` from account01/B18.

Consumed peer results: account01/B13 exact composition-prime cofactor criterion/slack composition law; account04/B17 exact biased restriction cocycle with KL/overlap credits.

New certified slice: all five-input Boolean gates with input biases `(1/2,1/2,1/2,1/2,1/4)` up to coordinate order and output mass `1/8`. There are exactly 97,158 truth tables. Exact biased-Walsh arithmetic plus rational logarithm intervals proves `D_GammaRO>=0` for every one; exactly 40 zero cases, all decomposable. The current lifted candidate has strictly positive defect throughout, minimum certified lower bound `0.0125721`.

Margin form: every all-five-input-essential gate has `c_G<=-0.72768`. Using the exact composition-prime criterion, 73,016 gates in the slice are prime, and every one satisfies

`c_G <= -(2387/1250 + (9/4) log2(3)) = -5.475765626622601408...`.

Thus this first asymmetric dyadic spine is not a hidden positive-margin obstruction. The tight essential witness has fifth-layer negative set `{0,1,2,3,4,5,8,10}`, i.e. the previously isolated four-input prime `B0` gated by the fifth literal. This makes the next attack source-specific: analyze `B0` at genuinely nonuniform interior biases, or another prime gate at genuinely non-dyadic biases; do not repeat the central, quarter-output, equal-bias EQ_d, or this 1/4-spine slice.

Canonical scientific delivery:
- report commit `6130f544d80c5ec67ff9b3e5ee3bda6f73e39494`, blob `6f1f5b6054a4bc8e7ee750fc952735114f3ce129`;
- checker commit `ac86725fc2a0e11481ef39fd45ddf39ae6e38735`, blob `7d1c6b35046837cb4718cb814bc1237a81965a31`, SHA-256 `8d79ba1e13da77d10b78350bfdb46d3a96dbdd733f63b168e933a14db808942a`;
- checker output commit `2b8876fbcf36c43dd07d1540abd9b0b6e872cf43`, blob `fb73e48951c1f1749937ea978a61da778df6d630`, SHA-256 `e6a66a60fc2da9065184d08876d0ceef841b89f2fdc4ef7d30f4d1e00d3c202c`.

Next recipients: account04/B17 for the exact restriction-cocycle/B0 all-bias line; account01/B18 for the stable prime-gate candidate chain.

Remaining implication to full FEI: prove `D_Gamma*(P;p)>=0` for every composition-prime Boolean gate of every arity and every interior product bias, or return a source-valid counterexample. This run closes one exact asymmetric slice only. **Full FEI remains OPEN / NOT PROVED.**

# B18 FEI proof integration — factorial trigger addresses, dimension-cooling coercivity, and zero-sector influence payment

**Execution:** `WITHOUT_VERIFIED_BRAIN`.

**Full uniform-cube FEI status:** **OPEN / NOT PROVED**.

This report integrates interface B (joint derivative rigidity) with interface A (realizable adaptive restriction). It does not turn any conditional input into unconditional closure. The new results are universal inequalities and an exact reduction of the remaining obstruction.

## 1. Exact compatible predecessors consumed

1. `fleet01/B18/20260921T2100Z-prefix-tc-refund/REPORT.md`, blob `21547dcdb11438c03b38ddb30d10c371d8cd99be`. For the spectral sample `S`, `K=|S|`, `I=E K`, insertion label `L`, and prefix `P`, it proves
   
   `D_seq + I TC(P) >= Gamma`,
   
   where
   
   `Gamma = sum_i p_i [ log2(1/(1-d_i/(2I))) + sum_{k!=i} d2(kappa_ik/(8p_i) || d_k/(2I)) ]`,
   
   and the universal ledger
   
   `H(f) <= 5I + I H(L) - Gamma + I TC(P) - E log2(K!)`.
   
   It explicitly leaves `I TC(P)` unpaid and forbids simply dropping it.

2. `fleet04/B12/20260921T201418Z-palm-trigger-cluster/REPORT.md`, blob `4643e5dd27cc48a508820a30413e24b9c4717fac`, plus the fresh `20260921T212331Z-factorial-trigger-address/check_factorial_trigger_address.py`, blob `83084c8f4bfda6d136c8b645382f282022d03be1`. A Palm-robust row has `TV(nu_i,U_{F_i})<=epsilon`; at `epsilon<=1/16`, reciprocal rows have one exact trigger signature and cross-component trigger edges increase influence by at least factor seven. The fresh checker suggests that the factorial rebate pays the trigger-address logarithm. Section 2 below supplies an all-dimensional analytic proof rather than treating the finite checker as a theorem.

3. `fleet04/B13/20260921T2025Z-zero-defect-exception-peeling/REPORT.md`, blob `ce8f72ada7b5fb97db2df95ce60c0acf7e9c70db`. If `Z={i:delta_i=0}`, its zero-defect components `C` have disjoint exceptional gates `T_C`, and
   
   `H_Z = sum_C 4(1-2^{-r_C})/r_C * (t_C+r_C-1) J_C`.

4. `fleet04/B14/20260921T201002Z-dimension-cooling-activation/REPORT.md`, blob `8923525f8e010e372837cdfc44fd629ba3510f8a`. It proves the block activation identity
   
   `L_A^(z) = sum_S mu(S) z^{|S\A|} Phi_z(|S cap A|)`
   
   and its adaptive nonincreasing-scale telescope `sum_u w_u L_{A_u}^{(z_u)} <= I(root)`.

5. `fleet04/B18/20260921T184125Z-transverse-near-subcube-elimination/REPORT.md`, blob `8243354ec04ccbb441c22a05ed911af9ec48f0e7`, gives the Boolean square inequality `j_k >= I_k(E_i)/2`. For an exact derivative-support subcube of measure `j_i` with `k` fixed, this gives `j_k>=j_i`.

6. `fleet04/B18/20260921T201525Z-sink-component-peeling/REPORT.md`, blob `2575d3945985e76d1f61831a65366b29b5052d27`, constructs one representative from every robust quotient-DAG sink and a common physical reveal block. It leaves repeated trigger-address cost and the nonrobust remainder open.

All logarithms below are base two unless `ln` is written.

## 2. PROVED: the factorial rebate pays every robust trigger address simultaneously

For an integer `c>=2`, let

`T = 1 + Bin(c-1,1/2)`

and define

`A(c)=E[ log2(T!)/T ]`.

### Lemma 2.1

For every integer `c>=2`,

`A(c) >= (1/4) log2 c`.

### Proof

Let `X~Bin(c,1/2)`. The identity

`binom(c-1,t-1)/t = binom(c,t)/c`

implies

`A(c) = (2/c) E[log2(X!)]`.

The function `x -> log Gamma(x+1)` is convex, so Jensen gives

`A(c) >= (2/c) log2 Gamma(c/2+1)`.

For even `c=2m`, this is at least `log2(m!)/m`. For `m>=4`,

`ln(m!) >= integral_1^m ln x dx = m ln m-m+1`,

and

`(3/4)ln m -1+1/m -(1/4)ln2 >=0`

at `m=4` and has positive derivative thereafter. Thus `log2(m!)/m >= (1/4)log2(2m)`. The cases `m=2,3` are direct.

For odd `c=2m+1`, monotonicity of `Gamma` on this range gives

`A(c) >= 2 log2(m!)/(2m+1)`.

For `m>=4`, the same integral lower bound reduces the desired inequality to

`h(m):=m ln m-m+1 - (2m+1)ln(2m+1)/8 >=0`.

Here `h(4)>0`, while

`h'(m)=ln m-(1/4)ln(2m+1)-1/4`

and `h''(m)=1/m-1/(2(2m+1))>0`, so `h` increases for `m>=4`. The case `m=3` is direct. The remaining `c=2,3,5` are direct from the three finite distributions; their ratios `A(c)/log2 c` are respectively `0.25`, `0.293643...`, and `0.353592...`. QED.

Now let `nu_i` be the Palm law of `S\{i}` conditional on `i in S`, and suppose

`TV(nu_i,U_{F_i}) <= epsilon_i`, `c_i=|F_i|+1>=2`.

Put

`a_i = E[ log2(K!)/K | i in S ]`.

Under `U_{F_i}`, the conditional size is exactly the variable `T` above. The negative part of the signed measure `nu_i-U_{F_i}` has total mass at most `epsilon_i`, and on the support of `U_{F_i}` one has `0<=log2(K!)/K<=log2 c_i`; mass moved outside this support contributes nonnegatively. Hence

`a_i >= A(c_i)-epsilon_i log2 c_i >= (1/4-epsilon_i)log2 c_i`.

Finally there is an exact partition identity

`E log2(K!) = sum_i p_i a_i`,

because for each realized nonempty set `S`, summing `log2(|S|!)/|S|` over its `|S|` members gives `log2(|S|!)`.

Therefore for **every** collection `R` of Palm-robust rows,

`E log2(K!) >= sum_{i in R} p_i(1/4-epsilon_i)log2(|F_i|+1)`.

In particular, at the current robust threshold `epsilon_i<=1/16`,

`boxed: E log2(K!) >= (3/16) sum_{i in R} p_i log2(|F_i|+1).`

This is simultaneous and nonreusing: no trigger coordinate or component may cause the factorial rebate to be counted twice. It proves the all-dimensional statement suggested by the fresh B12 checker.

### Corollary 2.2 — refined prefix ledger

Insert the preceding bound into fleet01/B18's universal inequality. For any chosen `1/16`-Palm-robust row family `R`,

`H(f) <= 5I + I H(L) - Gamma + I TC(P) - (3/16) sum_{i in R} p_i log2(|F_i|+1).`

This is **PROVED**, but it is not FEI closure: `I H(L)` and `I TC(P)` remain live positive terms.

## 3. PROVED: dimension cooling pays total raw reveal influence of any adaptive block strategy

At a state with `d>=1` unresolved variables put `z_d=1-1/d` (and interpret `z_1=0`). For a block `A`, fleet04/B14 gives

`L_A^(z_d)=sum_S mu(S) z_d^{|S\A|} Phi_{z_d}(|S cap A|)`.

If `m=|S cap A|>=1` and `r=|S\A|`, then

`z_d^r Phi_{z_d}(m)=sum_{t=0}^{m-1} z_d^{r+t}`.

Every exponent is at most `|S|-1<=d-1`. Therefore

`z_d^r Phi_{z_d}(m) >= m z_d^{d-1} >= e^{-1}m`.

(The `d=1` case is exactly one.) Averaging gives the stronger block coercivity

`boxed: L_A^(z_d) >= e^{-1} I_A(f).`

Combining this with B14's adaptive nonincreasing-scale telescope yields, for **every finite adaptive physical block restriction tree** using the canonical dimension-cooling scale,

`boxed: sum_u w_u I_{A_u}(f_u) <= e I(f_root).`

Thus repeated sink peeling cannot lose a logarithmic factor merely by paying the **raw influence** of the coordinates it physically reveals. Any remaining repeated-peeling obstruction must be an entropy/address excess above linear reveal influence.

A direct exhaustive diagnostic over all Boolean functions modulo global sign through dimension four and all nonempty blocks checked `491836` block cases. There were zero violations; the smallest observed ratio `L_A/I_A` was `27/64=0.421875`, the exact `d=4` value `(1-1/4)^3`, safely above `e^{-1}`. This is only a check; the displayed proof is all-dimensional.

## 4. PROVED: zero-defect Fourier entropy has a pure folded-influence payment

Use the exact B13 zero-defect component notation. For a component `C`, let `r_C=|C|`, gate `T_C` have size `t_C`, and write

`s_C=J_C/r_C=2^{1-r_C-t_C}`.

B13's exact sector identity becomes

`H_{Z,C}=4(1-2^{-r_C})(t_C+r_C-1)s_C`.

For every `k in T_C`, any row `i in C` has exact derivative-support subcube of measure `s_C` with `k` fixed. The transverse Boolean-square theorem therefore gives

`j_k >= s_C`.

B13 proves the gates `T_C` are pairwise disjoint. Consequently

`sum_C t_C s_C <= sum_{k in G} j_k`, where `G=union_C T_C subseteq E`.

Also `(r_C-1)s_C<=J_C`. Hence

`H_Z <= 4 J_Z + 4 J_G <= 4J`.

So the exact zero-defect sector no longer needs B13's second-moment payment `4D_E`: its internal one-point phase and every disjoint exceptional gate are paid directly by folded influence. More precisely,

`boxed: H_Z <= 4(J_Z+J_G).`

This does **not** prove FEI, because the pure-exceptional Fourier sector `H_E` remains. One may not apply Boolean FEI recursively to the conditional mean producing that subprobability spectrum; it need not be Boolean.

The same exhaustive Boolean calculation through dimension four checked all `10584` folded functions containing at least one zero-defect row. There were zero violations of `H_Z<=4(J_Z+J_G)`; the largest observed excess `H_Z-4(J_Z+J_G)` was `-0.59375`. Again this is diagnostic only.

## 5. PROVED: robust sink external gates are precisely a nonrobust remainder

For a reciprocal robust sink component `C`, let `T_C` be its common trigger signature and choose representative `r_C`. Write

`F_{r_C}=(C\{r_C}) union G_C`, `G_C:=T_C\C`.

If a coordinate `k in G_C` were itself in the robust row family, then `r_C -> k` would be a cross-component trigger edge out of `C`, contradicting that `C` is a quotient-DAG sink. Therefore

`boxed: G_C is contained in the nonrobust coordinates.`

This means the physical sink block splits canonically into (i) internal robust coordinates from the same reciprocal component and (ii) an external gate contained entirely in the nonrobust sector. Together with Section 3, linear internal reveal influence has a global `eI` budget; there is no independent robust-to-robust repeated-address obstruction.

There is a further low/high congestion split supplied by the newest fleet01/B18 ledger. For a `1/16`-Palm-robust representative and a trigger coordinate, `alpha_{rk}>=7/32`. If `beta_k=d_k/(2I)<=1/8`, then

`d2(alpha_{rk}||beta_k) >= d2(7/32||1/8)=0.04887550460410142...`.

Therefore the `Gamma` refund pays every low-congestion external gate incidence additively:

`Gamma >= 0.0488755 * sum_r p_r |{k in G_C: beta_k<=1/8}|.`

Every remaining external gate coordinate is simultaneously

- nonrobust, and
- high depth: `d_k>I/4`.

Thus the previous two B18 open obligations — repeated robust peeling and the nonrobust remainder — collapse to one sharper remainder after the already-paid pieces are removed: **high-depth nonrobust coordinates plus the still-positive prefix total-correlation term**.

## 6. Smallest honest current universal chain

The currently justified chain is:

1. **PROVED:** fleet01 prefix identity and TC-refunded all-witness curvature ledger.
2. **PROVED here:** the negative factorial term pays `(3/16) sum p_i log(|F_i|+1)` for every `1/16`-Palm-robust row simultaneously.
3. **PROVED:** robust reciprocal rows contract into exact trigger blocks, and sink representatives form a collision-free physical survivor family.
4. **PROVED here:** canonical dimension cooling pays the total raw reveal influence of any adaptive block sequence by at most `e I(root)`.
5. **PROVED here:** exact zero-defect Fourier entropy satisfies `H_Z<=4(J_Z+J_G)` without a second-moment bank.
6. **PROVED:** low-congestion external sink-gate incidences are paid by `Gamma`; the only external sink gates left are nonrobust high-depth coordinates.
7. **OPEN:** pay the remaining `I H(L)+I TC(P)` / physical conditional-entropy excess on the high-depth nonrobust sector by a single telescoping influence-scale resource, or construct a different contraction that removes it.

This is not a proof of full FEI. It is a reduction of the current A/B interface to one sharply identified positive-defect/high-depth nonrobust remainder, while the robust address, raw physical reveal influence, and exact zero-defect sector have explicit nonreusing payments.

## 7. Preserved killed shortcuts

The following remain forbidden and are not used here:

- dropping `I TC(P)` from the prefix tensorization;
- asserting `sum_k d_k=O(J)`;
- replacing the valid `2^{-r}/(16r)` physical near-subcube tolerance by fixed relative `1/16` for the block theorem;
- every-coordinate or prescribed-coordinate restriction payment;
- treating a non-Boolean subprobability Fourier law as a Boolean function and recursively invoking FEI;
- using finite checks as universal proofs.

**Full FEI remains OPEN.**

# B17 FEI creative attempt: Palm-size clustering alone is unbounded

**Status:** full Friedgut--Kalai Fourier entropy-influence conjecture remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`.  
**Primary routes:** APPROACH 3 / 14, using the coordinate-Palm repair of the killed full sensitivity-set route.  
**Novelty:** no literature-priority claim is made. This note stress-tests a newly proposed internal relaxation and identifies an exact missing Boolean constraint.

## 1. Starting point

The preceding account01/B17 run killed the raw reduction `H(Sens(X)) <= C I(f)` by the one-point defect, but isolated the correct activation-scale object: for each coordinate `i`, the ternary derivative `D_i f` has normalized squared Fourier law

`Law(S \ {i} | i in S)`

and physical squared law equal to the uniform sensitive-`i` fibre law.

A later FEI handoff proved the following necessary Palm clustering inequality for the spectral sample. Write

`p_i = P(i in S) = Inf_i(f)`, `K=|S|`.

For every Boolean `f`, every `i` with `p_i>0`, and every `0 <= t <= 1`,

`E[t^(K-1) | i in S] <= p_i^((1-t)/(1+t)).`                                    (PC)

That handoff also proposed an information-theoretic relaxation retaining only (PC), the level law `W_k=P(K=k)`, and the consistency equations

`sum_i p_i nu_i(k) = k W_k`, where `nu_i(k)=P(K=k | i in S)`.

If that relaxation forced a dimension-free entropy/mean-size bound, it could close the ordered spectral-code route. The result below shows that it does not: the relaxation is unbounded.

## 2. Exact theorem: uniform slices satisfy all Palm-size constraints in a huge regime

Let `mu_{n,k}` be the uniform probability law on all `k`-subsets of `[n]`, with `2 <= k <= n`. Then

`K=k` almost surely, `p_i=k/n` for every `i`, `I=E K=k`, and `nu_i(k)=1`.

Hence the consistency equations hold identically.

### Theorem 1

The full continuum family (PC) holds for `mu_{n,k}` for every coordinate and every `t in [0,1]` **if and only if**

`ln(n/k) <= 2(k-1)`.                                                            (1)

### Proof

For a uniform `k`-slice, (PC) becomes

`t^(k-1) <= (k/n)^((1-t)/(1+t)).`

For `0<t<1`, taking minus logarithms gives the equivalent condition

`(k-1)(-ln t) >= ((1-t)/(1+t)) ln(n/k)`.                                        (2)

The elementary inequality

`-ln t >= 2(1-t)/(1+t)`                                                         (3)

holds on `(0,1]`; indeed the difference has derivative

`-(1-t)^2 / (t(1+t)^2) <= 0`

and tends to zero at `t=1`. Thus (1) implies (2) for every `t`. The endpoint `t=0` is automatic because `k>=2`.

Conversely, divide (2) by `(1-t)/(1+t)` and let `t -> 1-`. Since

`(-ln t)(1+t)/(1-t) -> 2`,

we obtain (1). QED.

So (PC) allows fixed-size point processes on an ambient set exponentially larger than their set size.

## 3. The proposed Palm variational relaxation is unbounded

Take

`M_k = floor(exp(2(k-1)))`, `n_k = k M_k`,

and let `S_k` be uniform on the `k`-subsets of `[n_k]`. Since `ln M_k <= 2(k-1)`, Theorem 1 says every Palm constraint (PC) holds, and consistency is exact.

Nevertheless

`H(S_k)/E|S_k| = (1/k) log_2 binom(n_k,k) -> infinity`.

For example, using the standard asymptotic `log binom(n,k)=k log(n/k)+O(k)` when `n/k -> infinity`,

`H(S_k)/k = (2/ln 2) k + O(log k)`.

The ordered-code objective from the current compression handoff is even more explicit. For a uniform `k`-slice, `q_i=p_i/I=1/n`, `H(K)=0`, so

`U = I H(q) - E log_2(K!) = k log_2 n - log_2(k!)`,

and therefore

`U/I = log_2 n - (1/k)log_2(k!) >= log_2(n/k) -> infinity`.

### Consequence

The relaxation consisting only of

1. marginals `p_i`,
2. the level law `W_k`,
3. Palm-size consistency `sum_i p_i nu_i(k)=kW_k`, and
4. the complete continuum of hypercontractive Palm-size inequalities (PC)

has **infinite supremum** for both entropy/mean-size and the ordered-code objective. Thus it cannot prove FEI with Hod's constant, or with any finite constant.

This does **not** refute (PC), the ordered coding lemma, or FEI. It isolates the missing information: one must retain the *identities/sign geometry of the other coordinates in the Palm sample*, not merely its size distribution.

## 4. A small sharp stress test already passes PC but beats beta

The finite slice `n=161`, `k=3` satisfies

`ln(161/3) = 3.9827920763... < 4 = 2(k-1)`,

so it satisfies every (PC) inequality. Yet

`H(S)/E|S| = (1/3) log_2 binom(161,3) = 6.4602551425...`,

which exceeds Hod's `beta(1/2)=6.4547837...` by about `0.00547144`.

Its ordered-code value is

`U/I = log_2(161) - (1/3)log_2(3!) = 6.4692627112...`,

exceeding beta by about `0.0144790`.

Thus even a very low fixed level already defeats the proposed beta-valued Palm-size relaxation; the unbounded family above shows the problem is not a tiny constant mismatch.

## 5. Why the slice is not a Boolean spectral sample: an exact signed obstruction

The counterexample above is deliberately a counterexample to the *relaxation*, not to FEI. It is useful to identify the first Boolean condition that excludes it.

Suppose hypothetically that a Boolean function had spectral law exactly uniform on all `k`-subsets. Then all nonzero Fourier coefficients would have common magnitude `a=binom(n,k)^(-1/2)` and signs `epsilon_A in {+1,-1}` for `|A|=k`.

Booleanity `f^2=1` gives the signed convolution identities

`sum_A fhat(A) fhat(A xor U) = 0`                                               (4)

for every nonempty `U`. Take `U={i,j}`. Since the spectrum lives on one level, only swaps `B union {i} <-> B union {j}` survive, with `|B|=k-1` and `B` avoiding `i,j`. Therefore (4) reduces to

`sum_{B subset [n]\{i,j}, |B|=k-1} epsilon_{B union {i}} epsilon_{B union {j}} = 0`.   (5)

For the concrete `n=161,k=3` stress test, the number of terms is

`binom(159,2)=12561`,

which is odd. A sum of 12,561 signs cannot vanish. Hence this PC-feasible slice law is excluded already by the two-coordinate signed Boolean convolution identity.

This pinpoints the missing structure more sharply than "Booleanity matters": the level/Palm-size relaxation has thrown away a system of **signed Johnson-slice cancellation constraints** coupling coordinate identities inside each Palm law.

## 6. Point-process lesson for APPROACH 14

A generic negative-dependence slogan cannot by itself yield FEI. The uniform `k`-slice has pairwise negative correlations,

`P(i,j in S)=k(k-1)/(n(n-1)) < (k/n)^2`,

while its entropy/mean ratio above is unbounded along the PC-feasible family.

Likewise, determinantal structure alone is not enough without an additional Boolean restriction: a determinantal process with diagonal kernel `p I_n` is simply independent Bernoulli(`p`) inclusion, so

`H(S)/E|S| = h_2(p)/p -> infinity` as `p -> 0`.

Therefore a useful coding/point-process theorem for FEI must exploit a property substantially stronger and more Boolean-specific than generic negative dependence or generic determinantal structure.

## 7. Pivot: the next non-size Palm object

The failed relaxation suggests the next B17 object. Instead of keeping only

`nu_i(k)=Law(|S| | i in S)`,

retain the signed/identity-sensitive derivative Palm data. For `i != j`, define the derivative cross term

`C_ij = sum_{T: i,j notin T} fhat(T union {i}) fhat(T union {j})`.

The `U={i,j}` Boolean convolution identity couples `C_ij` to the adjacent-level term

`sum_T fhat(T) fhat(T union {i,j})`.

On a pure level this forces `C_ij=0`, giving (5); in the general case adjacent levels provide exactly the cancellation budget. This is a natural signed pair-Palm constraint that the scalar PC inequalities cannot see.

**Next target:** derive an entropy/coding inequality in which the cost `I H(p/I)` is paid by (a) unordered-set savings and (b) a quantitative signed pair-Palm/adjacent-level cancellation term. The first stress tests should be the one-point defect, width-two tribes, and Hod's recursive family. A second target is to characterize which fixed-size Palm laws can satisfy the full two-coordinate Boolean convolution system; even a dimension-free entropy bound for that signed Johnson class would be a genuine extension beyond the scalar Palm relaxation.

## 8. Executed numerical sanity check

`verify_palm_slice.py` checks the analytic threshold and reports the finite example plus the family `k=2,...,10`. It finds:

- `n=161,k=3`: all sampled PC log-margins nonnegative; `H/I=6.4602551425...`; `U/I=6.4692627112...`; pair-cancellation term count `12561` is odd.
- the family `n=k floor(e^(2(k-1)))` satisfies the exact analytic PC threshold for every tested `k` and its `H/I` rises from `6.4692...` at `k=3` to `27.1113...` at `k=10`.

The proof above is analytic and does not rely on the grid check. Script SHA-256 as executed before upload: `5595c46228241543df8a7f903bfed1be9317f2917bc5ad4796fc48648c6563bf`. Executed stdout SHA-256: `132884192330a7f7b1de22bd838d49a132f3c5b7ffc7bd8352ab191806b0be50`.

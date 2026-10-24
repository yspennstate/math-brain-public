# B12 FEI creative attempt: ordered spectral compression and hypercontractive Palm clustering

**Status:** full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`.  
**Route:** APPROACHES #1 (spectral-sample compression / sequential prediction), using the one-coordinate Palm repair of APPROACHES #3 rather than the already-refuted raw sensitivity-set entropy surrogate.  
**Novelty:** no literature-priority claim is made. The two lemmas below are elementary information theory / Bonami-Beckner hypercontractivity put into a form aimed at the current FEI route.

I first read `TASKS_2026-09-21.md`, then the read-once `REPORT.md`, then `APPROACHES.md`. I also recovered the existing B17 sensitivity-route report, so this run does **not** repeat the known one-point refutation of `H(Sens(X)) = O(I)`.

## 1. Exact universal statement attempted

For a Boolean function `f:{-1,1}^n->{-1,1}`, let `S` be its spectral sample,

`P(S=A)=fhat(A)^2`,

let `K=|S|`, `p_i=P(i in S)=Inf_i(f)`, `I=sum_i p_i=E K`, and, for `I>0`, let

`q_i=p_i/I`.

Define the **ordered spectral compression functional**

`U(f) = H(K) + I H(q) - E log_2(K!)`.

The strengthened universal statement I tried to prove or refute is

> **CFC(beta):** `U(f) <= beta(1/2) I(f)` for every Boolean `f`, where `beta(1/2)=6.4547837...` is Hod's lower-bound constant.

This is stronger than FEI. The first lemma below proves `H(S) <= U(f)` for every random subset law, not only Boolean spectra. Therefore CFC(beta) would imply the full FEI conjecture with the sharp candidate constant beta. Conversely, because Hod's Boolean family has `H/I -> beta` and `H<=U`, any universal constant in a bound `U<=C I` must satisfy `C>=beta`. Thus CFC(beta), if true, has exactly the right unavoidable constant.

I did **not** prove CFC(beta). I tried to refute it computationally and then derived an additional Boolean structural inequality intended to attack it.

## 2. PROVED: an ordered-set coding lemma

### Lemma

For **any** random subset `S subseteq [n]`, with `K=|S|`, `p_i=P(i in S)`, `I=E K>0`, and `q_i=p_i/I`,

`H(S) <= H(K) + I H(q) - E log_2(K!).`  

### Proof

After sampling `S`, choose a uniformly random ordering `(J_1,...,J_K)` of its elements and let

`L=(K,J_1,...,J_K)`.

Given `S`, the ordering contributes exactly `log_2(K!)` bits, while `L` determines `S`. Hence

`H(L)=H(S)+E log_2(K!).`

Now code `K` with its true law and, conditional on `K=k`, code the ordered coordinates using the product model `q^{\otimes k}`. This is a valid probability model even though it also assigns mass to repeated coordinates. Cross entropy dominates entropy, so

`H(L) <= H(K) + E sum_{j=1}^K log_2(1/q_{J_j}).`

The order does not affect the last sum. Averaging over `S`,

`E sum_{j=1}^K log_2(1/q_{J_j}) = sum_i p_i log_2(1/q_i) = I H(q).`

Subtract `E log_2(K!)`. QED.

Interpretation: the apparent `I log n` cost of naming active spectral coordinates is partly cancelled by the `log(K!)` saving from transmitting an unordered set. Any full proof along this route must show that Booleanity forces enough additional clustering/structure to make the remaining functional `U` only `O(I)`.

## 3. PROVED: rare spectral coordinates must arrive in clusters

The existing sensitivity-route report identified the correct one-coordinate object. For fixed `i`, put

`g_i=D_i f`.

On the `(n-1)`-cube, `g_i` takes values in `{0,+1,-1}` and

`||g_i||_2^2 = p_i`.

Moreover its normalized squared Fourier law is exactly the Palm law

`Law(S\{i} | i in S)`.

### Palm clustering lemma

For every Boolean `f`, every coordinate with `p_i>0`, and every `0<=t<=1`,

`E[t^(K-1) | i in S] <= p_i^((1-t)/(1+t)).`  (PC)

### Proof

Let `rho=sqrt(t)`. Bonami-Beckner hypercontractivity gives

`||T_rho g_i||_2 <= ||g_i||_(1+rho^2) = ||g_i||_(1+t).`

Because `|g_i|` is the indicator of the sensitive `i`-fibres,

`||g_i||_(1+t)^2 = p_i^(2/(1+t)).`

On the Fourier side,

`||T_rho g_i||_2^2 = sum_T t^|T| ghat_i(T)^2 = p_i E[t^(K-1) | i in S].`

Divide by `p_i`. QED.

This gives several exact consequences.

1. At `t=0`,

   `P(S={i} | i in S) <= p_i`, hence `P(S={i}) <= p_i^2` and

   `W_1 <= sum_i p_i^2`.

2. Differentiating from the left at `t=1` gives the cluster-size lower bound

   `E[K-1 | i in S] >= (1/2) ln(1/p_i)`.

   Equivalently, in base-2 surprisal,

   `E[K-1 | i in S] >= (ln 2 / 2) log_2(1/p_i)`.

3. For every integer `m>=0` and `0<t<1`,

   `P(K-1 <= m | i in S) <= t^(-m) p_i^((1-t)/(1+t)).`

   Thus the statement is a lower-tail constraint, not just a mean constraint.

4. Summing (PC) with weights `p_i` yields the global generating-function inequality

   `E[K t^(K-1)] <= sum_i p_i^(2/(1+t)).`  (GF)

   Its derivative at `t=1` recovers

   `sum_i p_i ln(1/p_i) <= 2 E[K(K-1)].`

So a coordinate with tiny influence cannot typically occur as an isolated spectral bit. Its surprisal forces other coordinates to accompany it. This is precisely the kind of mechanism an unordered sequential code can try to amortize.

## 4. Attempted refutation of CFC(beta)

`verify_ordered_spectral_code.py` computes `H/I`, `U/I`, and checks (PC) on a seven-point `t` grid. It also evaluates closed-form level laws for two asymptotic families. The exact committed output is `verification.json`.

### Exhaustive Boolean functions through n=4

The enumeration fixes `f(0)=+1`, quotienting global negation. It covers `2, 8, 128, 32768` functions for `n=1,2,3,4` respectively.

The maximum `U/I` values were

- `n=2`: `2.25`,
- `n=3`: `3.2829572908854145`,
- `n=4`: `3.7638946915756897`.

For `n=2,3,4` the maximizer was the one-point defect (`mask=1` in the checker). No case violated `H<=U`. No case violated (PC) on the tested `t` grid; the largest recorded `lhs-rhs` was `0` (attained at an equality endpoint, not a positive violation).

### One-point defects

For the one-point defect,

`p_i=2^(1-n)`, `I=n 2^(1-n)`, and `q` is uniform. The computed `U/I` values were

- `n=8`: `4.2484062780`,
- `n=16`: `4.3550469726`,
- `n=32`: `4.3990342622`.

The exact asymptotic calculation gives

`U/I -> 3 + log_2(e) = 4.442695040888964`.

So the family that destroys raw sensitivity-set entropy does **not** destroy the ordered compression target.

### Width-two tribes

For `s` disjoint width-two tribes blocks (`n=2s`),

`I=s(3/4)^(s-1)`, `q` is uniform, and the exact spectral level generating polynomial is

`W_0=(1-2(3/4)^s)^2`,

`W_k=4 [z^k] ((9+2z+z^2)/16)^s` for `k>=1`.

The checker gives

- `s=8` (`n=16`): `U/I=4.7295102691`,
- `s=20` (`n=40`): `U/I=5.1785807076`,
- `s=50` (`n=100`): `U/I=5.2387528090`,
- `s=100` (`n=200`): `U/I=5.2557744025`.

Conditioned on nonempty spectral sample, the block level increments tend to iid values `0,1,2` with probabilities `3/4,1/6,1/12`, so `K/s -> 1/3`. From this,

`H(K)/I -> 3 log_2(4/3)`

and

`E log_2(K!)/I = log_2 s - log_2 3 - log_2 e + o(1)`.

Since `H(q)=log_2(2s)`,

`U/I -> 3 log_2(4/3) + 1 + log_2 3 + log_2 e`

`       = 5.272770039446651`.

This is below beta.

### Majority and addressing controls

The tested majority values stay far below beta: `U/I=2.21448` at `n=5`, `2.63148` at `n=9`, `2.81658` at `n=13`, and `2.96196` at `n=19`.

Addressing with `m=1,2,3,4` address bits (`n=3,6,11,20`) gives `U/I=1.91830, 2.67688, 3.07945, 3.32941`.

### Outcome

**No refutation was found in these exact / structured tests.** This is only evidence about the stronger compression target, not a proof of it. Because `H<=U`, Hod's known sequence already forces the supremum of `U/I` to be at least beta, even without explicitly evaluating `U` on that sequence.

## 5. Dead end discovered inside the route

The `t -> 1` consequence of (PC) alone is not enough. Summing it controls the influence-surprisal term by the second factorial moment `E[K(K-1)]`, while the ordered code earns only `E log(K!)`. A rare very-large-`K` tail can make the former much larger than the latter. Therefore replacing the full Palm generating-function information by its first derivative throws away exactly the multiscale information needed for this coding route.

This does **not** refute CFC(beta), (PC), or FEI. It refutes only the naive plan “differentiate (PC) once and plug the resulting second-moment bound into the ordered code.”

## 6. Next attack: a Palm variational compression problem

Keep the whole family (PC), not only its derivative. Let

`nu_i(k)=P(K=k | i in S)`.

The genuine spectral law obeys simultaneously

`sum_i p_i nu_i(k) = k W_k`

and, for every `t in [0,1]`,

`sum_k nu_i(k) t^(k-1) <= p_i^((1-t)/(1+t)).`

The next route is to maximize

`[H(W) + I H(p/I) - sum_k W_k log_2(k!)] / I`

subject only to these Palm constraints and consistency. This is an information-theoretic relaxation of Boolean FEI with no truth-table variables. Two outcomes would both be decisive:

1. if its supremum is at most beta, the ordered coding lemma plus (PC) proves full FEI;
2. if the relaxation exceeds beta, its optimizer tells us exactly which additional Boolean constraint is missing.

The immediate next computation should discretize `k` and `t`, solve this Palm relaxation, and stress the optimizer against Hod's lower-bound family. The analytic next proof target is the equivalent inequality

`H(q) <= beta + [E log_2(K!) - H(K)]/I`,

using the full lower-tail information in (PC), not merely its mean corollary.

## 7. Classification

- **PROVED:** the ordered-set coding lemma `H(S)<=U` for arbitrary random subsets.
- **PROVED:** the Boolean Palm clustering inequality (PC), its low-tail corollary, and (GF).
- **OPEN / UNPROVED:** CFC(beta), hence the full FEI conjecture.
- **REFUTED AS A METHOD:** the one-derivative/second-factorial-moment closure of CFC; it loses too much information.
- **NOT CLAIMED:** novelty or publication priority for the two lemmas.

Script SHA-256 as executed before upload: `3c603181893f0a3212c04fefd466d40ab51fd9a6c9bf0ea5e97ab115966fc3f5`.

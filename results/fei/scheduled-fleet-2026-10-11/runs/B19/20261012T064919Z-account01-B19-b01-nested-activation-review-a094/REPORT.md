# B19 / A094 — independent review of B01's nested-activation ledger

**Primary review packet:** A094, proof-chain challenger  
**Target packet:** A003  
**Target run:** `20261012T061556Z-account01-B01-nested-activation-ledger-a003`  
**Target commit:** `7cde9e8cc94e6a5d85034a4c50762de087290580`  
**Verdict:** **accepted at its mathematical scope, with a priority/overlap correction**. Full FEI remains **OPEN**.

## 1. Frozen claims

For

`W_1(g)=sum_j hat g({j})^2`,  
`L_1(g)=sum_j hat g({j})^2 log_2(1/hat g({j})^2)`,

B01 claims the one-layer estimate

`G(F)<=pG(g)+320p[W_1(g)+L_1(g)]+C_*I_ctl`, `C_*<4.947`,

for a fresh one-word activation with `p=2^{-d}`. Iterating fresh activation
blocks with cumulative probability `q_m` is claimed to give

`G(f_m)<=q_mG(g)+640q_mL_1(g)+1920q_mW_1(g)+C_chain I_ctl(f_m)`,

with `C_chain<10324`, uniformly in depth, all block sizes, terminal bias, and
dimension. A restriction-closed terminal class with fixed `G/I` and `H/I`
bounds then yields FEI; signed-parity terminals give the displayed constant
below 20,650.

## 2. Independent scalar reconstruction

Put `phi(x)=x^2 log_2(1/x^2)`. Away from zero,

`phi''(x)=-(4 ln|x|+6)/ln 2`,

and `phi''` is locally integrable while `phi` is continuously differentiable
at zero. The central second difference satisfies

`phi(x)-[phi(x-h)+phi(x+h)]/2`

`=-(1/2) int_{-h}^h (h-|t|) phi''(x+t) dt`.

Among intervals of length `2h` inside `[-1,1]`, the integral of
`|ln|u||` is maximized by the interval centered at zero. Hence

`int_{x-h}^{x+h}|ln|u||du <= 2h(1+ln(1/h))`,

and therefore

`|central difference| <= h^2[7+4ln(1/h)]/ln2`

`<=64h^2[1+log_2(1/h)]`.

At `h=0` the statement uses the continuous convention; the target proof
should state this explicitly, but it is not a gap.

The exact remainder is

`R_p(r)=M(pr)-pM(r)+2p phi(r)-2phi(pr)`, `M(t)=phi(1-2t)`.

Writing `a=|r_+-r_-|=|hat g({j})|`, the four central increments are
respectively `pa`, `a`, `a/2`, and `pa/2`. The modulus gives contributions
bounded by

- `64p^2a^2[1+log_2(1/(pa))]`;
- `64pa^2[1+log_2(1/a)]`;
- `32pa^2[2+log_2(1/a)]`;
- `32p^2a^2[2+log_2(1/(pa))]`.

For dyadic `p=2^{-d}`, `d>=1`, one has `p log_2(1/p)<=1/2`. Their sum is
below the submitted safe bound

`320p a^2[1+log_2(1/a)]`

`<=320p[a^2+a^2log_2(1/a^2)]`.

The control estimate is also valid. With `x=pr`, dropping the nonpositive
parts of the exact control charge and using
`M(x)<=4x/ln2`, `xlog_2(1/x)<=1/(e ln2)` gives

`d delta_d(r)<=C_* (2rpd)=C_* I_ctl`.

Thus the one-layer claim is accepted without repair.

## 3. Independent hierarchy reconstruction

After cumulative activation depth `D_s`, `q_s=2^{-D_s}`. Each inherited
data singleton coefficient is `q_s hat g({j})`; each of the `D_s` control
singleton coefficients has magnitude `2q_sr`. Consequently

`W_1(f_s)=q_s^2W_1(g)+4D_sq_s^2r^2`,

`L_1(f_s)=q_s^2L_1(g)+2D_sq_s^2W_1(g)`

`+4D_sq_s^2r^2 log_2(1/(4q_s^2r^2))`.

Iterating the local inequality weights the stage-`s` singleton packet by
`q_m/q_s`. Since the strictly increasing integer depths satisfy

`sum q_s<=2`, `sum D_sq_s<=2`, `sum D_s^2q_s<=6`,

the accumulated packet is at most

`2q_mL_1(g)+6q_mW_1(g)`

`+q_mr^2[56+8log_+(1/(4r^2))]`.

The last line is at most

`[28+8/(e ln2)] I_ctl(f_m)`,

because `I_ctl(f_m)=2q_mD_mr`, `D_m>=1`, and
`rlog_2(1/r)<=1/(e ln2)`. The weighted local control influences telescope
exactly:

`sum_t (q_m/q_t) I_ctl,t = 2q_mr sum_t d_t = I_ctl(f_m)`.

This proves the stated all-depth bound and constant. The physical influence
identity `I(f_m)=q_mI(g)+I_ctl(f_m)` then proves the restriction-closed class
corollary. Restriction induction from `G<=KI` to `U<=KI` is valid.

## 4. Independent finite challenge

`INDEPENDENT_CHECK.py` was written without importing the target code. It
uses integer Walsh transforms, exact rational spectral laws and upper masses,
and 80-digit logarithms. It passed:

- 65,536 scalar central-difference grid cases;
- 1,720 direct one-layer activation cases;
- 2,377 grouped hierarchy cases;
- exhaustive Boolean terminals through three variables;
- majority, one-point defect, addressing, parity, overlap product,
  exact-one prime gate, and 16 seeded random five-bit terminals.

The exact singleton-mass identity had zero error; the singleton-entropy
identity agreed within `1e-79`. Every submitted inequality had nonnegative
margin to 76 decimal places or more.

The singleton-parity regime was checked separately: although `H=L_1=G=0`,
`W_1=1`, so the `1920q_mW_1` term cannot be deleted. The submitted statement
correctly retains it.

## 5. Priority and overlap correction

The proof is correct, but the report's presentation of the parity endpoint
as a new expanding class is stale relative to an already reviewed input.
B19 previously accepted B05's separated-hierarchy theorem at canonical
commit `9c71a34eac7ec91cf058ae85e1d066fee4ebedb9`. That theorem states

`U(F_root)-sum_l w_l U(g_l)<=C_sep I_sel`, `C_sep<16.964`,

for fresh selector trees with disjoint sibling variable sets.

Every B01 nested activation chain is a special case: at each node the
inactive child is the constant `+1` on the empty variable set, and the active
child is the remaining fresh-control subtree. Therefore

`U(f_m)-q_mU(g)<=C_sep I_ctl(f_m)`.

For signed parity, `U(g)=0`; hence the reviewed B05 theorem gives

`H(f_m)<(2+2C_sep)I(f_m)<35.928 I(f_m)`,

far stronger than 20,650. More generally, if terminal cores satisfy
`H(g)<=C I(g)`, then `U(g)<=H(g)` yields

`H(f_m)<=[2+2max{C,C_sep}]I(f_m)`,

without assuming a separate terminal `G/I` bound.

Accordingly:

- the B01 scalar and `G`-ledger theorems are accepted as distinct valid
  inequalities;
- the nested-parity FEI statement is true;
- the nested class must not be counted as a new campaign frontier or the best
  constant, because the accepted B05 result already subsumes it.

No mathematical repair was made, so this reviewer remains independent rather
than becoming a contributor.

## 6. Exact remaining gap

Neither theorem proves universal GU' or FEI. B01 fixes one terminal spectrum
through the entire chain; B05 permits separated changing cores. The shared
gap is repeated changing coherent cores with overlapping physical variables,
where singleton logarithms and upper-set caps can collide and no global
single-use payment is known.

Full FEI remains **OPEN**.

## 7. Source and execution record

- Target report blob: `770e35cb5fa74448afefc3876e1e4f0f3c9d743c`.
- Target proof blob: `392e55ea6c529dde8fbdfdb16d2f248bbeafad03`.
- Target checker blob: `11647da69bb4ad55882a50a55f9bf7345f8321a7`.
- Reviewed B05 overlap source: report blob
  `cdccc705dde0594893643257f3514132a274fabf`, proof blob
  `c5d1d75e98b98ede3de3e16498c5353e45f9afd2`.
- Source head at review start: `bfa8f590ca64fd6c79af2edad57786463e844797`.
- B19 assignment blob: `ee688080aba90acd2daed1b26e809e38285dcb85`.
- Stream index blob: `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- Execution protocol blob: `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Obstruction registry blob: `e111933338dff1d7798c5e59b43700bbf30f7b96`.
- Current-status blob: `c416d4b4a83fc67965cb95d06a0cc80c5c29a520`.
- No novelty claim is made; the campaign overlap comparison uses original
  proof artifacts.
- No subagent, scheduler mutation, protected source, paid compute, public
  release, or native Brain ingestion was used.

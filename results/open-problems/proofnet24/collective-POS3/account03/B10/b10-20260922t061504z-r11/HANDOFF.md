# POS3 account03/B10 handoff — first-boundary recurrence

Run: `b10-20260922t061504z-r11`

Status: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains `OPEN_NOT_PROVED`.

Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Assigned partner consumed

account04/B11, `20260922T051337Z-B11-pos3-r15`, report path

`proofnet24/collective-POS3/account04/B11/20260922T051337Z-B11-pos3-r15/REPORT.md`.

Essential partner fact used: the source-valid width-three family `R_N` has `pi=7`, rank variance at most `49/4`, arbitrarily long exact-two / exactly-two-witness heavy-flux corridors, and a balanced far boundary. Hence bounded variance/local corridor length is not the missing theorem.

## New exact result

If an exact-two crossed state `i` was reached from an exact-two predecessor `i-1`, let `A_prev,A` be the preceding/current endpoint minority counts, `E=e(P)`, and `K` the inherited conserved corridor count. Let `(d,x)` be the actual next lower-fringe incomparable pair, even if that next state is the first non-exact boundary, and put

`B=N_P(x<d)`.

Then the actual full-extension counts satisfy

`A_prev + 3A + B = E + K`.

Therefore the first-boundary probability defect is **exactly zero**:

`B-(E+K-A_prev-3A)=0`.

Extra distinguishers do not perturb the first boundary pair count; they only obstruct the next transfer/conservation step.

In a same-polarity hypothetical no-balanced exit, `B<E/3<K`, so necessarily

`A_prev+3A>E`.

If a four-pair continuing window lies at distance at least `d` from both boundaries, the inherited deep-corridor estimate gives the stronger requirement

`A_prev+3A-E > (1/33-eps_d)E`,

where `eps_d=[10/(3(1-rho^2))]rho^d`, `rho=(3-sqrt(5))/2`. For `d>=6` this is already a positive explicit overload greater than `0.01818E`.

## Sharp partner calibration

For account04/B11's `R_N` family, at the far boundary

`A_prev=2E_(N-4)`, `A=E_(N-3)`, `B=E_(N-2)`

and the Fibonacci recurrence gives

`A_prev+3A=E_N`.

Hence the new theorem gives `B=K`; the partner proves `1/3<B/E_N<2/5`, exactly the balanced escape. Thus the partner family saturates the overload threshold, while any no-balanced same-polarity boundary must lie strictly on the overload side.

## Frozen artifacts

Main report:

`proofnet24/collective-POS3/account03/B10/b10-20260922t061504z-r11/REPORT.md`

Verifier:

`proofnet24/collective-POS3/account03/B10/b10-20260922t061504z-r11/verify_first_boundary_recurrence.py`

Verifier terminator:

`POS3_FIRST_BOUNDARY_RECURRENCE_PASS`

## First unpaid implication

Prove a **boundary-overload-to-channel theorem**: under width three, no span descent, no autonomous reduction, and first failure of exact-two continuation, convert

`A_prev+3A-E=K-B>0`

(or the stronger deep-corridor amount) into an actual balanced pair, a target-scale heavy cover/bridge event, or a controlled multi-distinguisher exit. Do not search for an additive correction to the first boundary pair probability; that correction is identically zero.

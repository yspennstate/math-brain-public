# HARD8-05 — verification addendum for power-saturation checkpoint

**Full conjecture status:** OPEN.  
**Review status:** exact self-check and repository readback only; not independent peer review.

## 1. Main report receipt

Path:

`hard8_2026-09-16/HARD8-05/runs/2026-09-16/2026-09-16T12-26-03Z__report.md`

Creation commit:

`a1836a142d28944c86bb44ba1d17b9a2418919fb`

Exact creation-commit readback blob:

`7aa82a753056a828fcbc48f2241f3cfa9d50bf03`

Status: **VERIFIED**. The file was fetched using the creation commit as the ref after publication.

## 2. Verifier receipt

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T12-26-03Z__power_shift_verifier.py`

Creation commit:

`3be01f79be5791d4814575e85a4ac0581105884b`

Exact creation-commit readback blob:

`bddbcbfa0078321f9b1c09630b9e04d6c75b2d68`

Status: **VERIFIED**. The complete UTF-8 source was fetched back at the exact creation commit.

The first publication attempt for this new path encountered an ordinary GitHub contents-API branch-head `409` race (`is at ... but expected ...`) caused by concurrent repository movement. Per task instructions it was retried once, succeeded, and no bypass or alternate publication path was used.

## 3. Exact execution output receipt

Path:

`hard8_2026-09-16/HARD8-05/artifacts/2026-09-16T12-26-03Z__power_shift_verifier_output.txt`

Creation commit:

`4615fd1a6c89a5f3229235661e8a3b380624d86c`

Exact creation-commit readback blob:

`ad7cdd66eea492c1a48acb877cb2abb9f79090a9`

Status: **VERIFIED**.

The verifier exited successfully and printed `ALL_CHECKS_PASSED`. It used only Python standard-library integer arithmetic for the mathematical checks. The surrounding execution harness emitted an unrelated spreadsheet-runtime warmup warning on stderr before/around Python startup; it did not change the verifier exit status or any assertion result and is not used as evidence for any claim.

## 4. Checks actually performed

The successful run recomputed, rather than hard-coding as acceptance conditions:

1. all maximal target-avoiding subgroups needed for the listed unit groups;
2. exact `h=2` subset-product budgets for 54 maximal `-1`-avoiding subgroups across moduli `16,20,32,40,48,56,60,80,120`;
3. the exact mod-40 square fixed-total exception-length sets for total residues `7` and `23`;
4. zero exceptional budget for every maximal mod-40 branch at power `h=3`;
5. the fixed-shift `c=3` criterion on all 2,212 primes `n <= 200000` with `n == 1 (mod 24)`, finding 1,106 portal successes and 1,106 failures and checking an exact integer Egyptian-fraction identity whenever a witness exists;
6. the `c=7` target/subgroup/budget classification for each of the six Mordell residue classes `1,121,169,289,361,529 (mod 840)`.

These finite computations are consistency checks only. The universal fixed-shift equivalence and power-saturation theorem in the main report are symbolic proofs and do not rely on the bounded census.

## 5. Exact finite output summary

The square budgets were:

* `m=16`: `(index 2,budget 2)` twice; `(index 4,budget 2)` once;
* `m=20`: same;
* `m=32`: `(2,12)` twice, `(4,14)` once, `(8,14)` once;
* `m=40`: `(2,4)` four times, `(4,4)` twice;
* `m=48`: `(2,4)` four times, `(4,4)` twice;
* `m=56`: `(2,8)` four times;
* `m=60`: `(2,4)` four times, `(4,4)` twice;
* `m=80`: `(2,8)` four times, `(4,10)` six times;
* `m=120`: `(2,8)` eight times, `(4,8)` four times.

For modulus 40 the cube budgets were all zero. For square target `-1`, total residues `7` and `23` had outside-subgroup multiplicities `(1,3)` in four branches and `(0,2,4)` in the two quadratic-kernel branches.

For shift `c=7`, the six hard mod-840 residues reduce mod 7 to `1,2,1,2,4,4`. The corresponding square targets are `5,3,5,3,6,6`. Every maximal target-avoiding branch has exact exceptional budget at most two.

## 6. Claim boundary

Nothing in this checkpoint proves the full Erdős–Straus conjecture or gives a counterexample. The newly proved project theorem says that failure of an `h`-power divisor target forces prime residues into a target-avoiding subgroup with explicit order-dependent exception caps; the fixed-shift square portal turns that theorem into exact arithmetic restrictions on `(n+c)/4`.

The most important unresolved next step is a simultaneous-factorization theorem for consecutive shifts

`X_3=(n+3)/4` and `X_7=X_3+1`:

under simultaneous failure, `X_3` has every prime factor `1 mod 3`, while `X_7` has all but at most two prime factors in one explicit proper subgroup modulo 7. No universal incompatibility of those two conditions has yet been established.
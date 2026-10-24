# P0063 audit notes

This file is a handoff for independent end-to-end auditors. It is not itself an independent audit.

## Required source-level conclusion

Verify the exact Lyons--Peres Question 16.7 conclusion `nu_2 \perp nu_3` for simple-random-walk harmonic measure on the maximal base-2 coding tree of the middle-thirds Cantor set, versus Cantor--Lebesgue measure `nu_3`.

## Fragile bridge A: robust electrical gap

Check all of the following, not just the exact rational output:

1. `I_4^7` contains exactly the level-5 Cantor cylinder `[8/3^5,9/3^5]` up to null endpoint conventions.
2. The normalized parameters are exactly `(u0,r0)=(52/243,128/243)` and the midpoint lies strictly in the central third gap.
3. The conditional Cantor boundary measure defines a legitimate unit flow in the actual maximal dyadic coding subtree.
4. The Frostman estimate and `r` bounded away from zero give a **uniform**, summable energy tail on a neighborhood, so the trial-flow energy is continuous there.
5. The radius-6 wired right comparison has the correct Rayleigh direction: finite wiring gives an upper bound on the infinite descendant conductance.
6. The finite right-wired topology is locally constant because every relevant dyadic boundary has positive distance from the base scaled Cantor set. The exact script checks 133 relevant boundaries through relative level 7.
7. The strict left-lower/right-upper conductance separation therefore persists and yields a uniform `eta>0` for the true harmonic split.

## Fragile bridge B: overlap law and varying events

Under hypothetical non-singularity check that:

- `A_n -> A_infinity>0`;
- `lambda_n` with density `sqrt(f_n g_n)/A_n` is a probability law;
- `lambda_n(v)=w_n(v)` on every level-n dyadic cell;
- dominated martingale convergence gives `lambda_n -> lambda` in total variation;
- `lambda << nu_3`;
- total variation, not merely weak convergence, justifies transfer of the varying good events `G_n`.

## Fragile bridge C: Allen--Chow--Yu digit orientation

For fixed nonzero Fourier frequency `k`, verify that conditioning on the first `K` ternary digits and on the moving final suffix produces exactly

`prod_{j=K+1}^{m_n-L} (1+e(2^{n+1}k/3^j))/2`.

Allen--Chow--Yu Lemma 2.6 counts ternary digit changes in precisely the digit interval indexed from the **left**. Let `y_n=2^{n+1}|k|`. Then:

- `D_2(y_n)` is bounded for fixed `k` (appending zeroes creates at most one additional binary change);
- their Theorem 1.13 forces total `D_3(y_n) -> infinity`;
- the ternary digit length satisfies `Delta_3(y_n)=m_n+O_k(1)`;
- deleting a fixed prefix, fixed suffix, and the bounded digit-length discrepancy removes only `O_{K,L,k}(1)` changes;
- hence the middle ternary digit-change count tends to infinity.

Check the order of quantifiers: first fix `K,L,k`, then send `n -> infinity`; only after proving the cylinder-density statement let `K -> infinity` in the `L^1(nu_3)` approximation.

## Fragile bridge D: suffix `22` and geometry

With level-m cylinder length `ell=3^{-m}` and suffix `22`:

- the previous cylinder, if present, ends exactly `ell` to the left;
- if the terminal run of `2` digits has length `r>=2`, the next cylinder begins after a gap `3^r ell >= 9 ell`;
- the neighborhood inequalities `u/r<1` and `(1-u-r)/r<9` therefore make the ambient dyadic cell intersect `E` only in that cylinder;
- `(1/2-u)/r in (1/3,2/3)` gives Cantor conditional split exactly `q=1/2`.

## Final recurrence step

Verify that `alpha=log_3 2` is irrational and that `r_n=3^{ {alpha n}-1}`. Therefore every nonempty open scale interval `R` is visited with positive natural density. Lemma 5.1 gives positive `lambda`-mass to `(suffix=22,u_n in U)` along the full sequence, hence also along the scale subsequence. Total-variation transfer gives the same positive mass for `lambda_n=w_n`. The robust split gap then gives a fixed positive lower bound on `E_{w_n}(p-q)^2` infinitely often, contradicting the finite series forced by non-singularity.

## Endpoint convention

The source coding tree uses closed coding intervals, while the proof uses a half-open dyadic partition for measure bookkeeping. Cantor--Lebesgue measure is atomless. Harmonic measure of a transient unit-conductance tree has no atom at one end: a positive atom would force a positive current down every edge of one ray, giving infinite energy. Hence the countable dual-coding endpoint set is null for both pushforwards.

## Independent audit gate

Fleet closure requires **two OTHER-track full-proof audits**. One may be P26; the second must be a distinct track. A self-check, exact script, this note, or a re-read by the owning P0063 worker does not count.

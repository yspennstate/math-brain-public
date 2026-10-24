# Late POS3 peer delta — global renewal charge is unavoidable

The immutable `REPORT.md` for this run was already written when a newer complete OTHER-account result appeared. I did not rewrite that report. This append-only delta consumes and applies that result.

## New complete peer result consumed

**account02/B19**, run `20260922T022215Z-account02-B19-pos3-r13`, report blob `4eeff46882d7fc03828b4c9a01b9296a78294b08`, dependency-addendum blob `4d0098ee974494fbbb24f9f9d080035c35cb0d96`.

It constructs an infinite connected width-three family `P_m` with an autonomous chain whose quotient has a unique balanced contracted-vertex pair, while after expansion every outside-outside pair is unbalanced and the first replacement balanced pair can occur only at linear depth `alpha_* m`, where

`alpha_*=1-sqrt(2/3)`.

Its ideal-chain specialization is even closer to this run: deleting `I_m={b<c_1<...<c_m}` gives a five-extension quotient with two uniformly balanced pairs, `nu(a<x)=3/5` and `nu(d<e)=2/5`, but the exact lift weights push them to `mu(a<x)>2/3` and `mu(d<e)<1/3`. Thus bounded-fringe or bounded-depth transfer is genuinely false. The family is not a POS3 counterexample; it refutes only those local transfer mechanisms.

## Direct application to the first-interruption recurrence

For the renewal identity proved in this run,

`mu(A)=alpha nu(A)+sum_{q,j} beta_{q,j} eta_{q,j}(A)`,

with `alpha+sum beta_{q,j}=1`, rewrite it exactly as

`mu(A)-nu(A) = sum_{q,j} beta_{q,j} [eta_{q,j}(A)-nu(A)].`      (D.1)

Define the signed **renewal charge**

`Ch(A)=sum_{q,j} beta_{q,j} [eta_{q,j}(A)-nu(A)].`              (D.2)

Then a uniformly balanced pair event `A`, with `nu(A) in [1/3,2/3]`, survives precisely when

`1/3-nu(A) <= Ch(A) <= 2/3-nu(A)`.                              (D.3)

The account02/B19 family proves that no argument controlling only `O(1)`, `o(m)`, or any fixed endpoint fringe of the interruption index `j` can guarantee (D.3): the compensating balanced chain-touching pair can be forced to depth asymptotic to `alpha_*m`. Therefore the renewal selector residual in the main report must be interpreted as a **full-corridor signed-charge theorem**, unless it uses the hypothetical-counterexample-specific strong-majority/no-balanced-touching hypotheses to obtain a genuinely new shortcut.

This does not weaken Theorem 3.1. On the contrary, it identifies why the full sum over all interruption depths `j=lambda(q),...,m-1` is the correct induction object: those terms are actual uniform residual-poset components, and the newest adversary shows that truncating that exact renewal sum is not source-valid.

## Refined next implication

The first unpaid implication is now:

> **Global renewal-charge selector.** In a cardinality-minimal POS3 counterexample, for the first strong-majority chain block `C`, use the at-most-two first-interrupter structure, the exact full-depth residual mixture, the endpoint Hasse-fork constraints, and the no-balanced-touching inequalities to find one incomparable pair `A` satisfying (D.3), or derive a width-four antichain / autonomous-nonchain contradiction.

A proof that examines only a bounded neighborhood of either end of `C` cannot suffice in general.

**Classification remains:** `ESSENTIAL_STEP_APPLIED` for this run's renewal recurrence and two-channel reduction; parent POS3 remains **OPEN / NOT PROVED**.

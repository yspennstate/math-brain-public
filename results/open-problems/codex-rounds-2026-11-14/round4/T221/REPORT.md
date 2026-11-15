VERDICT: PARTIAL a collision-table refinement of the finite-model defect bound, with a sharp cap for the three-input AND encoder

RBS remains unresolved. The earlier defect bound survives an independent
chain-rule derivation. The bounded literature check found no resolution.

The new result replaces the universal bad-root entropy cap
log|B|+H(p) by an exact finite table for the specified local rule. A
partition of a prefix-closed word window is realizable at a root of finite
permutations exactly when each generator prescribes a well-defined
injective partial map on its classes. Such a map completes to a
permutation on the same classes. PROOF.md proves both directions,
including inverse letters.

For a hypothetical strict witness, write

\[
 C_0=H(Y_e)+H(X_e\mid Y_D),\qquad \delta=H(p)-C_0>0.
\]

If M_bad is the maximum table cost among realizable types with the
wrong coordinate pattern, every finite permutation model satisfies

\[
 \eta\geq\frac{\delta}{M_{\rm bad}-C_0}.
\]

Here eta is the fraction of roots with the wrong pattern. The one-point
model proves M_bad>=H(p)>C0, so the denominator is positive. This is at
least as strong as the earlier delta/(log|B|+delta) bound. The table also
gives finite linear constraints for weights on individual word defects.
Those weights were not optimized numerically.

For a genuine certified example, take F2=<a,b>, S=D=(1,a,b), and the
three-input AND encoder on Bernoulli(p) bits. The seven words
1,a,b,aa,ab,ba,bb are distinct in F2. The exact maximum local cost is

\[
 M=h(p)+p\max\{h(p),h(p^2)\}.
\]

The proof derives the upper bound directly by conditioning on the root
bit. Two- and three-point permutation models attain its two branches.
For the fair base this improves the cap from 2 log2 to (3/2)log2:
1.3862943611198906 to 1.0397207708399179. The cap is sharp at a single
root; sharpness of the resulting defect estimate is not established.

This example has no positive gap. Its target deltas are exactly negative
for p=1/3,1/2,2/3, with numerical values -0.1155117709606206,
-0.2746765991340926, and -0.43181739761778837. Therefore it illustrates
the improved cap and does not instantiate a nontrivial positive-gap
defect bound. No new group satisfying RBS or counterexample is obtained.

Validation command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 collision_costs.py
```

The final run succeeded in 0.273 seconds with 17,924,096 bytes peak RSS.
It enumerated all 877 partitions of the seven-word window: 103 are
realizable and 774 are rejected. Every realizable type was completed to
explicit permutations on at most seven points. A separate enumeration
checked all 576 pairs of four-point permutations at all 2,304 roots.
The five bases 0,1/3,1/2,2/3,1 gave 515 completed-model/base checks.

Every cap comparison uses exact rational entropy-product signs.
Conditional entropies were computed by both joint-minus-marginal entropy
and posterior averaging; the largest difference was
3.3306690738754696e-16. The genuine target cost was additionally derived
by conditioning on the two independent child outputs, agreeing exactly
by entropy-product comparison. The script checks the earlier separate
encoder/decoder defect inequality on all completed models. Full data are
in collision_table.json and collision_summary.json; LOG.md records the
commands, output, independent derivations and edge cases.

The nice wrapper prints `setpriority: Operation not permitted` because
the inherited priority is already 20, which the script reads and checks.
The run used one process, no workers, a 180-second alarm and an RSS check
below 1 GiB. No mathematical test failed. A patch with mismatched context
was corrected without changing the mathematical result. No predecessor
artifact or external state was edited; no git or subagents were used.

The opened literature was Brandon Seward,
[*Krieger's finite generator theorem for actions of countable groups II*,
arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4);
Lewis Bowen and Michael Chapman,
[*Surjunctivity does not characterize cosoficity of invariant random
subgroups*, arXiv:2511.06586v1](https://arxiv.org/html/2511.06586v1);
and Tim Austin,
[*Some Recent Developments in Structural Ergodic Theory*, ICM 2026](https://epubs.siam.org/doi/10.1137/25M1805564).
The conditional-entropy criterion is existing work. Priority of the
collision-table refinement and completion lemma was not established.
Austin's Question 3.1 still asks about identically zero Rokhlin entropy;
the search is not proof that no later resolution exists.

What did not advance: no genuine strict witness or new non-sofic group
pattern was supplied. Single-root completion does not give a finite
action of G or a model good at most roots. Bell-number growth limits
larger direct tables, and global compatibility of rooted types remains
unaddressed.

Next: add stationarity constraints to the existing 103-type table before
enlarging the window. For each partition sigma of three positions, the
frequency of sigma on (1,a,b) must equal its frequency on (a,aa,ab), and
also on (b,ba,bb), because each generator permutes the roots. These are
explicit linear constraints on the type frequencies. Combine them with
the table entropy inequality and prescribed word-defect tolerances in a
finite linear program. For an RBS application a certified genuine
positive-gap candidate is still essential; the AND example has none.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 2026-11-15 05:02 Asia/Tbilisi.

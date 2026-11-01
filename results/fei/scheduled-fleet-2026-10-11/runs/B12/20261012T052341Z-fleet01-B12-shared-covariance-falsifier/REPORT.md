# B12 / A057 run report: a shared-coordinate covariance obstruction

Run ID: `20261012T052341Z-fleet01-B12-shared-covariance-falsifier`  
Primary packet: **A057 — Coherent restriction remainder**  
Attempt: `B12-A057-ATTEMPT-05`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v5`  
Status: **SUBSTANTIVE MATHEMATICAL MOVEMENT; FULL FEI OPEN**

## Outcome first

This run proves the exact one-step potential law when one physical coordinate
simultaneously changes the Boolean source pair and the Boolean child.  The law
contains two signed covariance debts that are absent in the disjoint theorem.
It then gives an exact four-bit genuine-Boolean example in which **both** terms
of the previous product potential increase on average after the shared query.
Consequently no nonzero potential

\[
 A\,q\mathbf I(h)+\lambda\,\operatorname{Var}(h)\mathcal E_{\rm raw}(b),
 \qquad A,\lambda\ge 0,
\]

can be a supermartingale for all shared-coordinate Boolean restrictions.
Merely enlarging the terminal-reserve coefficient cannot repair the proof.

The example is irreducible in the relevant activation sense: the source
branches disagree at four inputs, and on that disagreement support the child
selects both branches.  Tensoring the source pair with a bent spectator gives
an unbounded-dimensional Boolean family for which the reserve drift tends to
minus infinity.  The composed outputs nevertheless have
\(H/\mathbf I=(2k+3)/(k+2)<2\), so this is a scalable **helper-potential
obstruction**, not an FEI counterfamily.

The preceding disjoint changing-witness theorem remains valid at its stated
scope.  The universal overlap step must instead keep a signed joint correction,
quotient by representation/activation equivalence, or charge an actual-output
split quantity.

## 1. Frozen objective and prior value

The previous B12 result proved for every adaptive interleaving of source-block
and child-block restrictions of a disjoint Boolean splice

\[
 \sum_X w_vR_v+\sum_{\ell}w_\ell P_\ell\le P_{\rm root},
 \qquad
 P=C_*q\mathbf I(h)+\operatorname{Var}(h)\mathcal E_{\rm raw}(b),
\]

where \(C_*=4+2\ln2+2/e\).  The exact boundary was simultaneous restriction
of a coordinate shared by source and child.  The bounded objective here was:

> Derive the shared-coordinate covariance formula and either prove that the
> same potential decreases for genuine Boolean overlaps or give an exact
> genuine-Boolean falsifier together with the repaired proof obligation.

Previous value/status: disjoint changing witnesses paid by one root potential;
overlap covariance open.  New value/status: exact overlap law plus a genuine
Boolean counterfamily refuting every nonnegative rescaling of the two old
potential components.

## 2. Exact simultaneous-update identity — PROVED

Let

\[
 q=\|b\|_2^2,\quad Z=\mathcal E_{\rm raw}(b),\quad
 V=\operatorname{Var}(h),\quad J=\mathbf I(h).
\]

Restrict a coordinate shared by \(b\) and \(h\).  For every quantity \(X\),
write \(\bar X=(X_++X_-)/2\) and
\(\delta X=(X_+-X_-)/2\).  Parseval and the standard Boolean restriction
identities give

\[
 q=\bar q,\qquad J=\operatorname{Inf}_i(h)+\bar J,
 \qquad V=\alpha_i^2+\bar V,
 \qquad Z=\bar Z+D_Z,
\]

where \(D_Z\ge0\) is the exact scalar-kernel entropy dissipation of \(b\).
Expanding the average child product proves, for all real \(A,\lambda\),

\[
\begin{aligned}
 &AqJ+\lambda VZ-
 \frac{A(q_+J_++q_-J_-)+\lambda(V_+Z_++V_-Z_-)}2\\
 &=A\bigl(q\operatorname{Inf}_i(h)-\delta q\,\delta J\bigr)
 +\lambda\bigl(\alpha_i^2Z+\bar V D_Z-\delta V\,\delta Z\bigr).
\end{aligned}
\]

The debts \(-\delta q\,\delta J\) and \(-\delta V\,\delta Z\) are the exact
terms that disappear when source and child coordinates are disjoint.

## 3. Four-bit Boolean falsifier — PROVED

In zero-based lexicographic truth-table order, set

```text
g+ = ( 1,-1,-1, 1,-1,-1,-1, 1,-1,-1, 1,-1,-1,-1,-1, 1)
g- = ( 1,-1,-1,-1, 1,-1,-1, 1,-1,-1, 1,-1,-1,-1, 1,-1)
h  = ( 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,-1, 1).
```

Query bit one (coordinate two in one-based notation), put
\(a=(g_++g_-)/2\), \(b=(g_+-g_-)/2\), and \(F=a+hb\).  The source branches
disagree on \(\{3,4,14,15\}\).  Off this support \(h=1\); on the support,
\(h\) takes both signs.  Hence both branches are physically selected where
they differ, so the witness is not an inactive-child encoding.

Exact rational Walsh arithmetic gives

\[
 (q,Z,V,J)=\left(\frac14,\frac54\ln2,\frac{15}{64},\frac12\right),
\]

and the two restricted children have

\[
 (q_0,Z_0,V_0,J_0)=\left(\frac18,\frac34\ln2,0,0\right),
\]

\[
 (q_1,Z_1,V_1,J_1)=
 \left(\frac38,\frac94\ln2-\frac9{16}\ln3,
       \frac7{16},\frac34\right).
\]

Thus the two component drops are independently negative:

\[
 qJ-\frac{q_0J_0+q_1J_1}{2}=-\frac1{64},
\]

\[
 VZ-\frac{V_0Z_0+V_1Z_1}{2}
 =\frac{63\ln3-102\ln2}{512}<0.
\]

The last sign is exact since \(3^{63}<2^{102}\), obtained for example from
\((3^5)^{12}3^3<(2^8)^{12}2^6=2^{102}\).

It follows immediately that for every \(A,\lambda\ge0\), not both zero,
the potential \(AqJ+\lambda VZ\) has negative drop at this shared query.

The composed output has exactly

\[
 H(F)=3\text{ bits},\qquad \mathbf I(F)=2,
 \qquad H(F)/\mathbf I(F)=3/2.
\]

This is not an FEI counterexample.

## 4. Bent-spectator lift — PROVED

For \(k\ge0\), let \(s_k(x,y)=(-1)^{x\cdot y}\) on \(2k\) fresh bits.
Then \(H(s_k)=2k\) bits and \(\mathbf I(s_k)=k\).  Replace \(g_\pm\) by
\(g_\pm s_k\) and leave \(h\) independent of the spectator variables.  The
source derivative becomes \(bs_k\), so tensor entropy yields

\[
 \mathcal E_{\rm raw}(bs_k)=\mathcal E_{\rm raw}(b)+qH(s_k)\ln2.
\]

For every \(k\ge0\), the shared-coordinate drops are

\[
 \Delta(qJ)=-\frac1{64},\qquad
 \Delta(VZ)=\frac{63\ln3-(102+24k)\ln2}{512}<0.
\]

The reserve drift tends to \(-\infty\), proving that the defect is not a
bounded low-dimensional artifact.  But the output is \(Fs_k\) and

\[
 \frac{H(Fs_k)}{\mathbf I(Fs_k)}=\frac{2k+3}{k+2}\longrightarrow2.
\]

Therefore the lift tests the near-tensor and growing-dimension controls
without producing an FEI counterfamily.

## 5. Exact computation and reproducibility

Command:

```bash
python3 check_shared_covariance.py
```

The checker uses exact `Fraction` Walsh coefficients.  Entropies are retained
as exact rational linear combinations of logarithms of primes; the only sign
comparison is separately certified by the integer inequality
\(3^{63}<2^{102}\).  There is no random search and no seed.

Verified scope:

- all root and child values in the four-bit witness;
- disagreement support and actual use of both branches there;
- both exact negative component drops;
- exact output entropy and influence;
- tensor lifts for \(k=0,1,2,3,4\), with the displayed all-\(k\) formula
  proved analytically.

The finite calculations certify this explicit family.  The universal no-go
for nonnegative two-term potentials follows analytically from the exact signs.

## 6. Controls and failure classification

- **Genuine Boolean realizability:** all of \(g_+,g_-,h,F\) and every tensor
  lift are Boolean signs.
- **Activation equivalence:** both source branches are selected on their
  disagreement set; the example cannot be removed by deleting an unused
  branch.
- **Parity-zero erasure:** not used; both potential components have strictly
  negative drift.
- **Rare restrictions / sparse defects:** the source disagreement has density
  \(1/4\); the proof does not infer a universal bound from this one scale.
- **Near tensors:** the bent-spectator lift preserves the defect and amplifies
  the reserve failure.
- **Addressing/multiplexers:** this is an actual Boolean two-branch selector,
  and the conclusion is deliberately restricted to the overlap potential.
- **Prime Boolean gates:** the example is an explicit four-bit truth table,
  not a fractional or weighted relaxation.
- **OVERLAP_PRODUCT:** respected—the result refutes the shared-coordinate
  product-potential extension, not disjoint additivity.
- **RAW_CONV_TENSOR:** respected—raw derivative entropy is used only as the
  already declared reserve; no normalized entropy payment is inferred.

## 7. What moved, what did not

### Mathematical movement

1. The formerly informal “covariance terms” are now an exact identity with
   all signs and quantifiers fixed.
2. A genuine Boolean, activation-irreducible witness refutes the entire
   nonnegative two-parameter repair family, not just the old coefficient.
3. A bent-spectator lift shows an unbounded-dimensional obstruction whose
   reserve deficit grows linearly in \(k\).

### Still open

The complete biased coherent remainder is not yet paid over arbitrary adaptive
physical hierarchies with shared coordinates.  The exact remaining local
obligation is to find a quantity whose drop controls the two covariance debts
without introducing a representation-dependent reserve.  Three materially
different candidates remain:

1. a signed joint correction involving the restricted pair \((b,h)\);
2. a canonical minimization over all Boolean-splice representations of the
   same output (activation quotient);
3. a charge written directly in terms of the actual output split
   \(F_+-F_-\), followed by a source-influence or terminal-entropy telescope.

The first next action is to test the activation-quotient candidate on the
four-bit witness: minimize the old potential over all Boolean branch-pair
representations of the same \(F\) before and after the shared query, and check
whether the quotient eliminates both covariance debts.  If it does not, the
output-split mechanism becomes the next materially different attack.

## 8. Claim and review status

- `B12-A057-SHARED-COVARIANCE-FORMULA-v1`: **PROVED by contributor; review
  pending**.
- `B12-A057-TWO-TERM-OVERLAP-POTENTIAL-NOGO-v1`: **PROVED counterfamily to the
  helper claim; review pending**.
- `B12-A057-COHERENT-HIERARCHY-v5`: **OPEN, sharpened**.
- Full FEI: **OPEN**.

Requested independent review packets: A091 and A090.  No independent review
of these new claims was observed during this run.  The preceding fixed-source
envelope had already been independently accepted; that acceptance is not
misreported as review of the new overlap result.

## 9. Runtime and boundaries

The exposed runtime identifies the agent as Codex based on GPT-5.  No exact
model subversion or reasoning-effort selector was exposed.  No subagents,
email, public release, paid compute, scheduler mutation, protected evaluation
material, live graph mutation, merge, or deployment were used.


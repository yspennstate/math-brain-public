# Independent clean-payment audit and arbitrary-order edited continuation

All entropies are in bits. Restrictions are physical uniform restrictions,
and all spectral laws are normalized squared Walsh coefficients. Each query
retains both outcome children with conditional reach 1/2. Rate 3 was chosen
once at the original source. Nothing below resets the reference or account.

## 1. Independent verdict on A067's quadratic Bellman theorem

The audited statement is A067-QUADRATIC-BELLMAN-ALL-CLEAN-REFINEMENTS@1,
statement sha256 a1a4b531e94ef2a767d07cf2c9fcf389d3326220467154e3160dcd673a52f64a,
PROOF.md sections 1--3 in A067 run 20261023T120754Z.

Let q be a quadratic F2 polynomial, M its alternating polar matrix, and r
its rank. The autocorrelation of (-1)^q is supported on ker M, where it is
a character. Fourier inversion on this subgroup therefore gives a uniform
squared spectrum on a coset of (ker M)^perp: entropy is exactly r. This
also follows by eliminating one nonzero polar pair at a time. Each such
pair contributes rank 2 and two independent flat spectral bits; the radical
contributes a character and no entropy.

Deleting a physical coordinate changes the alternating rank by either 0
or 2: a principal deletion has rank difference at most 2 and both ranks
are even. The child polar matrix is the same for both fixed values. For
a nonzero polar row the derivative is a nonconstant affine Boolean sign,
so influence is 1/2. Its actual rate-3 debit is -3/2 or 1/2. A zero row
is a character or dummy, with debit -3 or 0. Consequently rank/4 is a
Bellman super-solution for every coordinate and both children. Summing
the conditional inequalities proves the bound for every finite adaptive
stopping tree. This reconstruction introduces no repair.

For k disjoint quadratic pairs the sharp price is k/2: querying one member
of each pair and stopping attains it. Characters and dummies cannot raise
this value. The literal checker uses its own F2 elimination and truth-table
Walsh transforms for every quadratic phase through four variables, modulo
global output sign only; both children of every coordinate are checked.

At the supplied A088 paid frontier each clean leaf L has k_L<=m pairs.
Its original reach is a_L, so all adaptive clean continuations together
cost at most sum a_L*k_L/2 <=m/2. With the independently reviewed original
allowance E_old<71/96, r>4^-m/8 and I_X=m+(2m+1)4^-m/2, the SAME remaining
account is >m/2-71/96>=25/96. This part of A067's statement HOLDS unchanged
at its stated scope. A088 is the original ancestor-source author; this
review is independent of A067's new Bellman proof, not a second independent
review of A088's own ancestor-source theorem.

## 2. A Boolean query bound and the exact Booleanity line

For any Boolean f and coordinate i, let P be its spectral law and let
P_0,P_1 be the two physical-child spectral laws. Their mean is the marginal
P^- deleting i, by the coefficient square-sum identity. Therefore

 H(P) - (H(P_0)+H(P_1))/2
   = H_P(i | remaining label) + JS(P_0,P_1) <= 2.

Both terms lie between 0 and 1. In particular every physical query has
actual entropy-drop-minus-3-influence debit <=2-3 Inf_i(f).
This bound concerns actual entropy; it does NOT assert nonpositive CE debit.

The entropy identity requires that BOTH physical children have squared
norm 1. Arbitrary normalized real functions need not satisfy it. The exact
two-bit example b=[1,1,1,-1] and u=[0,0,0,-2] has identical flat squared
Fourier spectra and identical root Dirichlet coordinate energies. But u's
first physical children have squared norms 0 and 2. Thus root normalization,
flat spectra, and physical mean-square identities alone do not license this
Boolean query bound or the clean Bellman argument. More generally having
unit conditional squared norm under EVERY complete physical restriction
forces f(x)^2=1 at every point; it is precisely Booleanity for real f.
This diagnoses scope, not a non-Boolean disproof of FEI.

The stronger complex relaxation matters: the two-bit entropy-drop bound
DOES hold for every complex unimodular function, because both child norms
are still 1 and the same square-sum identity holds. Thus that generic bound
does not exploit binary Boolean phases. The clean rank/payment statement
does exploit them. For one coordinate take the complex unimodular values
[1,(3+4i)/5]. Its squared spectrum is [4/5,1/5], physical Dirichlet energy
1/5, and both children are unimodular constants. The rate-3 query debit is
log2(5)-11/5>0, certified by 5^5>2^11. Thus there is no rank-zero free
stopping allowance for arbitrary complex one-coordinate phases, even with
ALL restriction norms equal to 1. The genuinely discrete step in section 1
is the F2 quadratic polar/radical structure and derivative influences in
{0,1/2,1}; in section 3 it is the exact canonical quadratic influence
lower bound. Neither follows from normalization or generic transport.

## 3. NEW: arbitrary coordinate order on the surviving edited zero path

Take the same canonical original G_m, m>=2. Complete H prescribed pairs
on its edited zero path, where 0<=H<=m, then query w and retain BOTH full
children and all earlier clean exits. This is the already paid cut T=H,
with E_base<71/96. Its active edited leaf has original reach
tau_H=1/(4*4^H), and equals

 b_k(Y) - 2*1{Y=0},  k=m-H.

Now query the remaining 2k data coordinates in ANY permutation, continuing
only the zero outcome at each query and retaining the one outcome as a
clean exit. Stop this edited path at ANY prefix. Unlike the previous
completed-pair schedule, arbitrarily many pairs may remain half open.

At any edited prefix, untouched pairs remain quadratic, and each half-open
pair has its unqueried partner as a dummy of the unedited phase, because
the queried member was fixed to 0. The point defect survives only on the
all-zero remaining input. With n remaining coordinates, eta=2^-n, a query
in an untouched pair has influence 1/2+2 eta; a query of a half-open partner
has influence 2 eta. Indeed the origin edge was constant for the unedited
quadratic phase, and changing the origin toggles just this edge, whose
uniform influence weight is 2^{-(n-1)}. These formulas include the final
one-bit defect. Consequently the complete actual query debits are bounded
by 1/2 for a first member and by 2 for a second member, using section 2.

The zero-spine reaches decline by a factor of 2 per queried coordinate.
In every valid ordering, the first occurrence of a pair precedes its
second occurrence. The discounted sum of the prices (1/2 for first,
2 for second) is largest when each second member follows its first
immediately. To prove this, move the earliest available second member
left across a first member: at positions t,t+1 this increases the sum
by (2-1/2)(2^-t-2^{-(t+1)})>=0. Repeat until pairs are adjacent.
Any prefix can first be extended to a full order since all surrogate
prices are nonnegative. Hence its added original-reach actual debit is

 E_edit <= tau_H*(1/2+2/2)*sum_{j=0}^{k-1}4^-j
         = 2*tau_H*(1-4^-k) <= 1/(2*4^H).

For k=0 it is 0. Equality is not asserted for actual entropy debits.
This argument handles every permutation and every prefix in every dimension;
it does not infer a theorem from the finite cases.

## 4. Pay every clean refinement from the diminished original account

All newly stopped one-children are again products of disjoint quadratic
pairs and characters, with dummies. Keep the surviving edited child fixed
at its chosen prefix, and attach ANY finite adaptive physical stopping tree
to EVERY clean leaf, including all old siblings and the original b_m.
Section 1 bounds their total added actual debit by m/2. Thus

 R_new = r+I_X - E_base - E_edit - E_clean
       > m/2 - 71/96 - 1/(2*4^H).

For every m>=3 this is at least 25/96; for m=2,H>=1 it is at least 13/96.
The sole remaining endpoint m=2,H=0 has four remaining data coordinates.
The accompanying exact certificate exhausts all 24 permutations and all
their prefixes (65 distinct ordered prefixes). It computes E_base+E_edit
directly from full original-reference Boolean frontiers and uses the sharper
clean capacity sum a_L*k_L/2; the lower reserve is >13/96 at every prefix.
The m=2,H=1,2 frontiers are also checked (5+1 distinct prefixes).
Therefore the all-dimensional stated continuation has SAME original
remaining reserve >13/96, with every clean continuation included.

Each descendant Q is ONLY the marginal of its inherited original Q_b or
Q_c. The support domination persists by the physical two-child square-sum
identity. At every frontier the entire original-reference ledger is

 E_new,H = E_new,Q + K_new,
 R_new = r+I_X-E_new,H,

where K_new sums EVERY terminal KL with original G reach. For an individual
continuation the increment is E_H=E_Q+K_after-K_before; the incoming KL is
subtracted exactly once. All old z debit D and signed negative banks remain.
All legacy rate-2 invoices remain E_2=E_3+J_total with J_total the actually
removed original-weighted influence. The old J<1/2 bound is not asserted
after adding these arbitrary queries.

The old constant terminal-KL bound 19/32 MUST NOT be carried forward. Query
one member of every pair on just the original clean b_m sibling and stop.
Its inherited original reference is uniform; every resulting character
has KL exactly m. This sibling alone contributes m/2 to the full KL bill,
while its actual entropy debit is only m/4. Thus full KL becomes unbounded
with m, but is genuinely included in the payment above. This exact Boolean
guard rules out replacing the new payment by a claim that the old KL cap
persists. Positive CE changes on dummy queries are likewise retained.

## 5. Remaining unsupported line

The extension still has a quadratic unedited phase, one marked defect,
and a single surviving zero path. It supplies no unused ancestor margin
for arbitrary edited cores or mandatory nonflat profile conversions. The
first unsupported line for general FEI is a comparable actual original
source/Bellman allowance for those cores. The standard two-bit query bound
alone does not price arbitrary branching at small influence. The next
nearest test is replacing the matching quadratic by an overlapping
quadratic edited phase while preserving the ACTUAL original source
allowance; the clean rank lemma already handles all its stopped siblings.
Full FEI remains OPEN. New section 3--4 extension awaits external review.

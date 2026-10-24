# A029 stage 2: depth-sensitive bent child deficits

## exact target, quantifiers, hypotheses and units

Uniform physical cubes, Boolean signs, entropy in bits, ordinary total
influence. D_K=KI-H. Let r1 be the best relevant single-coordinate
physical entropy-drop/influence ratio, r_d the best nonempty physical
stopping-tree ratio Pi_H/Pi_I with maximum depth d, and r_all allow
arbitrary finite trees. These are different optimization domains.

For F_g(x,y)=(-1)^(x dot y)g(y), every m>=1 and every Boolean m-bit
seed g, r1=4 and r_2=2. For quadratic bent roots, r_all=2. For arbitrary
bent roots the proposed gain bound r1-r_all<=2 is FALSE: a cubic bent
root on six variables has an explicit depth-six tree with
r1-Pi_H/Pi_I=(392-9log2(3))/186>944/465>2.03.
This does not refute the original n<=4 depth-two theorem or full FEI.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was reread
in full; stage-start BOARD.md snapshot 2026-10-12 03:34 UTC;
B06 STREAM_NOTES.md v2, 2026-10-11 23:26Z, R2 and A029 direction;
own STATUS.md, LEARNED.md and stage-1 REPORT.md. A079/A030/A017/A064
rolling facts were searched for overlap; their results are not proof
premises. The point-defect formula is derived directly here, rather
than rely on a source-summary extremal classification. No internet
priority or external-review claim is made. Sources for C005/R2 remain
the stage-1 pinned restriction notes; R2 is reused, not re-claimed.

## complete derivation or exact first unsupported line

DERIVATION.md contains the full proof saved before computation. Fourier
summation over x gives Fhat(A,B)=2^-m g(A)(-1)^(A dot B), so H(F)=2m,
I(F)=m and every root influence is 1/2. A physical coordinate child
has coefficients 0 or +/-2^(1-m), hence H=2m-2 and every root ratio is4.

For any physical restriction, let P be pairs with both coordinates
free, U those with x fixed and y free, V those with y fixed and x
free, p=|P|, and ell the number of V coordinates with fixed y=1.
For each assignment t to y_P let u_t be the actual Boolean U-core
g(t,y_U,fixed y) times the character determined by fixed x_U.
Partial Fourier summation gives the exact laws

  H(F_rho)=2p+E_t H(u_t),
  I(F_rho)=p+ell+E_t I(u_t),
  D2(F_rho)=2ell+E_t D2(u_t).

The x_P frequency equals t, the y_P frequency is uniform, and the
x_V set is a fixed character. All signs and the actual core law are
retained. For codimension<=2, |U|<=2; every Boolean two-bit function
is a constant, character, or signed AND2, and satisfies H<=2I.
Thus all such leaves have D2>=0. Root D2=0 and R2 imply every
depth-two tree has Pi_H>=2Pi_I. Query y_j and then x_j only on y_j=1
to obtain entropy cost2 and influence cost1, attaining r_2=2.

Choose g=-1 only at 000, with m=3. Then H(g)=4-(9/8)log2(3),
I(g)=3/4, and D2(g)=(9/8)log2(3)-5/2<0. Reveal all x; stop at x=0;
complete y to constants on the other seven x assignments. Its actual
terminal averages are H(g)/8 and I(g)/8=3/32, giving

  Pi_H=6-H(g)/8, Pi_I=93/32,
  Pi_H/Pi_I=(352+9log2(3))/186.

The integer certificate 3^5=243<256=2^8 proves log2(3)<8/5, the
ratio<916/465 and gain>944/465>2.03. Its terminal deficit is
D2(g)/8=-5/16+(9/64)log2(3); the query credit is its negative.
Their sum is exactly zero, preserving the bent root D2=0. Omitting
this negative terminal cost would incorrectly treat the gain as an
entropy bound improvement. Disjoint tensors retain this depth-six
counterexample in dimensions 6t, still with H/I exactly2.

Every quadratic restriction has entropy equal to its adjacency rank r
and at least r nonisolated influence-1/2 variables; isolated character
variables only add influence. Thus D2>=0 in every quadratic restriction.
R2 bounds every tree ratio below by2; complete trees attain2. The
lead's parenthetical "bent 2k: gain exactly2" therefore requires a
quadratic hypothesis for unrestricted trees.

More generally, at a root with D_K=0, all stopping ratios are >=K iff
all proper physical restrictions have D_K>=0: if one is negative,
isolate it and complete all off-path siblings. This is a terminal
ownership consequence of R2, not a new universal payment theorem.
The first unsupported line is a dimension-independent payment after
arbitrary terminal deficits are retained; none is established here.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications SPEC.json, VERIFY_SPEC.json and DEPTH4_SPEC.json
preceded their jobs. Commands: python -X utf8 code/check.py --pilot;
python -X utf8 code/check.py; python -X utf8 code/verify.py; python -X
utf8 code/depth4.py, with paths relative to this run (launched from A029
using full relative run prefixes). All memory estimates were <=120MB;
no >300MB job, GPU, ambient n=6 census or dimension escalation occurred.

The initial pilot had an original-to-local coordinate indexing error;
out/pilot_failure.txt records it. It was fixed before full execution.
Corrected pilot: 729 restrictions, 2,747 checks, 0.0431s. Full:
all 256 three-bit seeds, all 186,624 restrictions, 593,232 exact checks
PASS, 13.735s, including 18,688 codimension<=2 D2 certificates.
The helper compares exact rational squared-coefficient multisets with
the predicted restricted law, and verifies influences by physical edges.
Entropy intervals use a rational atanh series with 120 terms, rigorous
tail 2z^241/[241(1-z^2)], z<=1/3, divided by an outward ln2 interval
and rounded to 2^-100. No float decides any sign.

Second implementation: direct character sums, exact prime-log entropy
linear forms and Fraction physical influences, 561 checks PASS, 0.0111s.
It independently verifies the 56 internal nodes and 57 actual terminal
leaves, both telescopes, and exact signed cancellation. It is a second
implementation by A029, not independent-agent acceptance.

The fixed-witness terminal-deficit DP certifies minimum cut D2=0
through depth3 and strictly negative at depth4. The first extracted
depth-four tree has ratio approximately1.957199; it is an attained
interval-certified ratio, not a global optimum-ratio certificate.
Its extraction tie refinement was interrupted by the next-stage arrival;
stage3 completes a concrete checked smaller tree. The source-complete
claim in this stage uses the separately verified depth-six tree.

## proof dependencies and changed downstream conclusions

Only B06 R2 is an external proof premise; the paired Fourier law and
point-defect spectrum are derived here. Stage-1 finite results remain
unchanged. The unrestricted gain<=2 candidate and an unrestricted
all-bent equality assertion are refuted; quadratic bent equality and
paired-family depth-two equality survive. B20/B06 should propagate
this precise scope correction, without marking full FEI false.

## one next mathematical action and independent reviewer

Complete the depth-four attained countertree and derive a general
priority cleanup transport for an arbitrary seed g, retaining its sole
uncertified terminal deficit. Reviewers A087 (physical leaf ownership)
and A094 (exact spectrum/log/tree certificate). Consumers A028,A030,A064.

## actual persistence receipts or precise save blocker

The stage was interrupted by the next-stage prompt before protocol
metadata was finished; its proofs and executed outputs were already
saved. The required four protocol files are now completed in this
assigned stage-2 directory. Finalization time is recorded honestly by
receipts; no earlier completion time or remote mirror is claimed.

**Universal bridge:** C019 is advanced by disproving the unrestricted
+2 tree-to-singleton comparison on an actual six-variable bent function
while proving the +2 depth-two equality on every paired arbitrary-seed
carrier. The exact signed leaf ledger locates the missing term: the
negative seed deficit cancels the apparent query credit. NEXT derives
an arbitrary-seed priority transport, giving one conserved terminal
account rather than another isolated-class entropy estimate; a universal
terminal-inclusive payment still remains open.

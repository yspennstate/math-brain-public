# Derived checkpoint08: strong slab bounds and nonmonotone extensions

2 October 2026 UTC. Completed on top of master
`71a6e592e0f70adf04fe20a3380e6408667591ee`. Full Boolean FEI, all-activity
forest negative correlation, the general Möbius-ladder Sidorenko problem
and the K-theory targets remain open. The statements below are complete
internally audited subsidiary results, with priority and outside peer
review unverified. Existing results are premises, not new achievements.

## Universal signed-split conversion and slab formulas

The full proof in
`proofnet24/P03-fei/continuations/2026-10-02-slab-deficit-composition/universal_split_deficit_and_slab_composition_proof.md`
proves a universal signed Boolean split lemma. For f=A+zB, alpha=EB²,
beta=EB and nu=alpha-beta², alpha>1/2 implies Delta_z H<=14nu. Influence
one and signed mean-zero derivatives are explicitly covered. If a
restriction-closed class admits a local bound Delta H<=C alpha at a chosen
coordinate of every restriction, the lemma and exact budget identities
give H(f)<=max(2C,14)[I(f)-Var(f)]. An ordinary global FEI bound alone is
not sufficient to invoke this implication.

The already completed parallel-slab and strict-separated crossing local
theorems meet the premise. They therefore have the strong bound, and so
do balanced read-once formulas using their gates with arbitrary fan-in,
depth and size. Every nonroot output must be balanced and leaf blocks
disjoint. A biased root is allowed. The exact composition law is fully
derived, with O'Donnell--Tan2013 credited as the established framework.
Root and adversarial full analytic audits pass. A separate exhaustive
checker verifies all65,814 Boolean functions through4variables and all
262,948 pivots; its exact budget checks and numerical entropy checks are
distinguished. Root read and reran the entire checker.

## Parity-modulated LTFs and unate strong classes

`parity_modulated_ltf_proof.md` proves that every arbitrary output character
modulation of an LTF has FEI with the SAME constant as the previously
proved strong LTF bound. The parity and LTF may use the same coordinates;
the parity can have growing degree. This is a nonmonotone subclass, not
all polynomial threshold functions. The same statement holds for parity
modulations of the earlier balanced read-once LTF formulas.

The generic argument is explicit: squared spectra permute under character
multiplication, and physical influences become I_i or1-I_i. If at most
one base influence exceeds1/2, modulation has influence at least I-Var.
Every unate function meets that condition by conditioning on two-bit
monotone truth tables. Thus any such strong base class yields the stated
ordinary FEI extension. No strong FEI theorem for all unate functions is
asserted. The full independent heat-entropy audit passes. Root's exact
standalone checker exhausts all7,778 monotone functions through5variables
and all245,470 character modulations, including empty spectral atoms.
Character and Chow identities are credited as standard prior facts.

## Disjoint products and mixed read-once trees

`disjoint_product_deficit_corollary.md` establishes the elementary strong
product implication with the SAME constant and arbitrary child output
means. Disjoint products have additive entropy and influence, while their
variance is at most the sum of child variances. This also gives mixed
read-once trees: product nodes permit biased children; every other slab/LTF
gate node retains balanced children. The root can be biased. The separate
adversarial analytic audit passes. Tensorization is established standard
analysis; the new applications depend on the campaign's strong base
estimates. It does not authorize arbitrary biased nonproduct compositions.

## Source check, failed directions and next work

The source record names and links the primary O'Donnell--Tan composition
paper and O'Donnell book statements actually inspected, and preserves
the distinction between full uniform-input entropy and corrected biased
FEI+. Searches cannot certify novelty; irrelevant search returns provide
no evidence of absence.

Previous largest-weight and component-joining obstructions remain valid.
The universal conversion retains its low-influence local hypothesis, so
it does not bypass those obstructions or prove full FEI. New arbitrary-
spacing component comparisons are being investigated separately; their
failed candidates will be preserved in a later immutable checkpoint.
Independent all-activity forest and Sidorenko operator/finite-host routes
continue. Their unpublished candidates are not achievements of this run.

## Files and reproducibility

Read all full proofs, candidate, audits, standalone scripts, JSON outputs,
`slab_deficit_composition_source_check.md` and
`slab_deficit_composition_checks_readme.md` in the new track. Both numerical
programs require Python3 and NumPy with no campaign helper imports. The
analytic proofs, rather than finite enumeration, establish the universal
statements. Only the campaign CURRENT.md is updated in place; previous
problem-track and campaign runs remain immutable.

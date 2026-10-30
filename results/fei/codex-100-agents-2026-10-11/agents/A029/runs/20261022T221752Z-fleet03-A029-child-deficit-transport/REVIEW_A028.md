# Independent review of A028@6, with explicit scope

Source: A028/runs/20261022T205915Z-fleet03-A028-stopping-tree-payment,
DERIVATION.md equations (1)--(4); claim
A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@6, statement SHA256
e06ecdad95f92730ceca9cdf728b3cb52a6b51cde6df41de7dba1fd77dde0900.

Verdict: HOLDS for the normalized sector identity, exact signed DATA debit,
nonnegative CONTROL JS release and every finite adaptive mixed-tree telescope.
The optional quantitative bound J<=2log2(e) gamma I(a) also HOLDS by an
independent reconstruction. Earlier structural, calibrated-reference and
whole stopping-class assertions bundled from v5 are EXCLUDED from acceptance.

The reconstruction uses the joint Fourier law on (control set,data set).
Parseval over controls identifies its data-set marginal q. Conditional entropy
on each data row is exactly the source's L term: for two sources its empty
control coefficient is z_t and nonempty coefficients are d_t ahat(s), with
their squared mass sum V d_t^2. The chain rule gives T+J+L. Control restriction
changes only the label weights, so concavity of entropy gives release >=0
on the closed simplex. Data restriction retains both actual source children
and gives the signed JS difference. Finite physical reach then telescopes.
This is not a reset of the bank, and no positive-part replacement is used.

For the optional quantitative bound, DERIVATION.md section 2 derives the
two-point entropy inequality, tensorizes it over physical controls, and uses
Parseval over shared data. Its gradient is the actual Boolean flip gradient,
so the constant is exactly 2/ln2. In the binary case the physical control
influence equals gamma I(a), including constant-controller and identical-source
endpoints. No source repair or changed constant is needed.

Finite validation includes all two-control ternary maps and all one-bit
source triples (which contain all binary maps and pairs with unused labels),
as well as a genuinely three-spectrum non-flat fixture through all partial
restrictions. Independent direct character sums reconstruct the fixture's
marginals and actual flip costs. The refund guard shows why a positive-part
substitution would be an ERROR; the AND2 guard retains the structural bit.
The final executed counts are in REPORT.md and out/*.json. They validate
implementations and boundary cases; the finite-dimensional analytic argument
supplies the all-dimensional scope.

This review is not acceptance of a universal source certificate, a terminal
reference reset, a combined J+L influence bound, or full FEI. No external
adoption is inferred. The new finite-label extension is A029's contribution
and still needs independent review; A029 cannot independently accept it.

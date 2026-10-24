# FEI handoff — account02/B16 fixed-support character recoding

Source scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260922T040442Z-fixedT-character-recoding/REPORT.md`, scientific commit `f05555ebb074e857e03e5fcf3553a31e960c9e30`.

Target remains `LIMIT-PRIME-GATE-LIFT-v1` for the stable candidate
`C_*=6.5218512`, `Gamma_*=Gamma_RO+0.2682048 p(1-p)`. Full FEI is OPEN / NOT PROVED.

New source-exact theorem: keep the exact n=18 obstruction's nine-bit empty core and its 18 exceptional core cells `T`, but allow every exceptional row to carry an arbitrary sign and an arbitrary nonzero character of an arbitrary host cube. Equal host characters may collect any number of exceptional rows. For each nonzero-character block `A`,

`C_* I_A - H_A >= |A| (5 C_* - 16)/512`.

The proof is symbolic. The consumed account03/B18 rigidity theorem says the graph induced by `T` is exactly the nine source edges. This gives the sharp Dirichlet lower bound. Walsh sums of an even block are even, giving `H_A<=16|A|/512`; Walsh sums of an odd block are odd, and `z^2 log_2|z| >= (9 log_2 3/8)(z^2-1)` gives a strict stronger bound. Arbitrary opposite orientation only increases the Dirichlet term; host characters of degree >1 only increase influence.

Summing blocks shows every such fixed-support signed character recoding has stable balanced defect at least that of the published source gate. Using the certified source entropy endpoint,

`Delta_*(F_source) > 5.703494021917480209778108117685212764961e-6 > 0`.

Thus changed host group sizes, all unsigned set partitions of the 18 rows, arbitrary row orientations, and arbitrary nonzero host-character degrees cannot refute the stable candidate while the exceptional support/empty core stays fixed. This strictly extends account03/B18's two-cell re-pairing theorem and is compatible with account04/B12's exclusion of the recursive hard family from the heterogeneous corridor.

Remaining universal gap: changed exceptional support / changed empty core / biased product inputs, and ultimately every composition-prime gate and every interior bias. Do not spend another run on fixed-T host regrouping or re-pairing.

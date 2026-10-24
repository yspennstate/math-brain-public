# FEI handoff — explicit composition-prime arity-10 gate obstruction

Source-bound scientific report: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T010748Z-prime-arity10-gate/REPORT.md`, report commit `a6b5404a316051554f5d8a790aa6fedd7b53d69d`, report blob `b085b01b44499096816c543a662075703678f5bf`.

**Status:** `CANDIDATE_REFUTED`; full FEI remains OPEN / NOT PROVED.

Consumed exact peers: account03/B12 arity-10 balanced gate obstruction (report blob `d12fe592f4fa6db16cb571557f6cc41392dd5860`) and account02/B17 exact gate-composition cocycle / prime-factor reduction (handoff blob `f6fd4945acb3aa61f5020c6f906652fe4c886e90`).

New theorem/certificate: for a Boolean gate `G` and a coordinate block `A`, `2<=|A|<=n-1`, a decomposition `G(a,b)=F(g_A(a),b)` exists iff the rows `b -> G(a,b)` take at most two distinct values as `a` varies. Therefore disjoint-composition primality is equivalent to absence of such a two-row module.

Applied to the source-exact 10-input witness SHA-256 `3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`: all `1012` candidate blocks were checked exactly; none has <=2 row types, and the minimum row-type count is `3` (attained by 18 blocks). Hence the witness is **composition-prime**, not merely non-readonce.

Inherited certified gate data therefore gives an explicit prime obstruction:

`I=257/128`, `H/(I-1)>6.459372281637855731`, and required read-once-base quadratic margin `c_G>0.018289126551422926`, while every AND constraint is certified with `c=0.01`.

Thus the latest AND/decomposable-extremality candidate fails even on a composition-prime arity-10 gate; the excess cannot be attributed to accumulation of smaller disjoint gate factors. The account02/B17 cocycle remains valid and says future fixed-potential work may restrict to composition-prime gates.

A direct recursive self-composition of this balanced prime seed gives `I_d=I^d` and `H_d=H(I^d-1)/(I-1)`, hence an explicit all-dimensional Boolean lower-bound family with `H_d/I_d -> H/(I-1)>6.459372281637855731`. This is not the repository record; the inherited shared-core construction gives the stronger `6.521850083658612...` lower bound.

Checker blob `3980ddb6ad2b2395e477b36984cc42a2629ddfe6`; output blob `3958538789f1f5381df25dc01a3334565b50309e`; locally executed checker source SHA-256 `bac58cb5e7f477eae3f730ed088d8848becd0dab4020f1425a35b87bf1c48e1b`.

Replacement obligation: a new finite-cap potential must control every composition-prime gate at every product bias, or another prime obstruction must be produced. The balanced-uniform slice is already constant-for-constant FEI-complete, so this is not claimed as a solved reduction.

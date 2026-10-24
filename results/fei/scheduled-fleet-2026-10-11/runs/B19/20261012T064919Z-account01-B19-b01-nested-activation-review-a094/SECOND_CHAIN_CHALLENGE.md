# Independent challenge regimes

Target: `B01-A003-NESTED-ACTIVATION-LEDGER-v1` at canonical commit
`7cde9e8cc94e6a5d85034a4c50762de087290580`.

The following regimes were selected independently of the target checker.

1. **Balanced diffuse core.** Odd majority has bounded singleton mass but
   singleton entropy of order `log n`. The repaired local estimate retains
   exactly this term and does not collapse it to selector influence.
2. **Sparse defect.** A one-point defect with arbitrary fresh activation depth
   tests simultaneous small terminal bias and small selector influence. The
   root factor `q_m` appears in every retained terminal charge.
3. **Singleton parity.** Here `H=L_1=G=0` but `W_1=1`; this catches the mistake
   of setting all terminal credits to zero merely because entropy vanishes.
   The submitted constant keeps the `1920 q_m W_1` term.
4. **Higher parity.** Here `W_1=L_1=G=0`; only the physical control charge
   remains.
5. **Whole-set addressing, overlap product, exact-one prime gate, and seeded
   random cores.** These challenge support concentration, shared variables
   inside the terminal core, and nonfactorability. They do not violate the
   fixed-core theorem because only the fresh controls are iterated.
6. **Block schedules `(1,1,1)`, `(1,2)`, `(2,1)`, `(2,1,1)`, and `(1,2,2)`.
   ** These distinguish total activation depth from the grouping into blocks
   and verify the weighted local-control telescope.
7. **Endpoint conventions.** Constants, `r=0`, zero singleton coefficients,
   `d=1`, and arbitrarily small dyadic activation probabilities were checked.
   Equation (4) needs the continuous convention at `h=0`; this is harmless.

The analytic proof survived every regime. The independent checker passed
65,536 scalar-modulus grid cases, 1,720 direct activations, and 2,377
hierarchies.

Campaign overlap was also challenged. The reviewed B05 separated-hierarchy
theorem applies to every target nested chain by taking the inactive child to
be the constant `+1`. It gives

`U(f_m)-q_mU(g) <= C_sep I_ctl`, `C_sep<16.964`,

so the B01 parity FEI constant below 20,650 is valid but not the strongest
known bound or a new class frontier. For parity terminals, the reviewed B05
result gives `H(f)<35.928 I(f)`.

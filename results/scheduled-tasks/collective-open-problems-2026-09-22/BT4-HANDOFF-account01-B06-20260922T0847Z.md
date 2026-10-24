# BT4 handoff — account01/B06 20260922T0847Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical report: `proofnet24/collective-BT4/account01/B06/20260922T083534Z-b06-bt4-r11x/report.md`, creation commit `8841697d2a58082f1a4ba5b84541544b1eba7e31`, Git blob `69b9a67c08db3ba983f9f476378f7bd23f4cf839`.

Named OTHER-account input actually applied: account04/B05 `BT4-R4-DIRECT-3X3-CYCLE-FACTOR-v1` (`b05-20260922t074314z-r35`, report blob `ab5f354238ef330125494b0afa5c8e4799716534`) plus account03/B04 `BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1` (report blob `df8c2244fb4a13f5a6fd4ef9fac4bc334076a25a`).

New theorem `BT4-R4-DIRECT3X3-SWITCH-CLASSIFICATION-v1`: in the fully alternating direct `3 x 3` residual with 3-cycle monodromy `sigma`, contract the three selected support intervals on each light support to blocks. Let `c_A,c_B` be the cyclic successor 3-cycles of the A/B blocks. For any spanning refactorization using only original support-boundary transitions and the six selected direct crosses, if `x_i` records the A-exit cross choice then necessarily

`x_{T(i)}=x_i`,  where `T=c_B sigma^{-1} c_A`.

Thus `T` is either a 3-cycle or identity. If `T` is a 3-cycle, only the all-support factor `A union B` and the all-cross mixed cycle `K` exist: the residual is switch-rigid. If `T=id`, all eight switch vectors exist; this occurs exactly when `c_A=c_B` and `sigma=c_A^{-1}`. Weight-two switches give two neutral mixed cycles covering all of `A union B`.

A concrete loopless simple local port model in the flexible class shows the six-chord idea alone cannot close: take `c_A=c_B=(123)`, `sigma=(132)` and switch A-blocks 1,2. The two mixed cycles are `A1-B1-A3-A1` and `A2-B2-B3-A2`; every unused prescribed transition goes between these two cycles, so neither has a prescribed internal directed chord. This is a countermodel only to a **port-only closure implication**, not to BT4 or to the full exact-seven R4 cage.

Consequent first debt: `BT4-R4-DIRECT3X3-FRESH-CROSS-BREAK-v1`. Apply account03/B04 to a shortest mixed cycle. Unless a same-support bypass/third-support mediation already exits the branch, a fresh-source CROSS is forced. Use exact-seven/global-NO-SIX/R4 fan data to show that this extra cross breaks the switch class and yields a bypass, H mediation, SIX, strict packing improvement/cyclic exchanged remainder, or a replacement alternating `3 x 3` selection with identity/transposition monodromy (already closed by B05 plus the previous B06 nontransposition lemma).

Do not claim that a single arbitrary fresh cross closes by cyclic order alone; the team's parity-trap controls rule out that shortcut.

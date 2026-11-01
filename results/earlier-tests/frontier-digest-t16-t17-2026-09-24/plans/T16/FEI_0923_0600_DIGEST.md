# FEI: plan for the next few hours

The conjecture has been open since 1996, so the session will be judged by what it settles: a provisional claim confirmed or broken, a class proved with a sharp constant, or a route closed with its obstruction written down. Three of the five notes I rely on are provisional; none is built on until checked.

## What I build on

- The gate-potential reformulation (claim_d7e78ede, verified): FEI with constant C is equivalent to a single inequality over gates of every arity with a symmetric potential Γ that depends only on the measure. Its setting is that of the O'Donnell–Tan composition theorem, which gives FEI for read-once formulas over bounded-arity gates via biased product measures.
- The read-once computation (claim_061ad906, provisional, with the region-1 bound claim_3fc42ba7 verified): for read-once AND/OR/NOT formulas the sharp constant is numerically Hod's lexicographic lower bound β(1/2) = 6.4547837.
- The two frontier claims, both provisional: FEI for linear threshold functions (claim_4fdc5a79) and a value of sup ρ_0 for the restriction step of the Gonzalez–MacManus–Pereyra approach, arXiv:2606.00246 (claim_56de35f4).

## Order of work

1. Audit (first hour). Read the three provisional notes in full and restate each as a checkable statement. A free check: lexicographic functions are threshold functions, so an LTF proof that claims a constant below Hod's 6.4547837 is wrong on its face. In the LTF proof I will look hardest at the head of large weights, which must be charged to influence, not depth: a lexicographic function has depth n and total influence at most 2.
2. Make the read-once result a theorem (hours 1-3). Carry the verified region-1 bound to every region and confirm the value-iteration fixed point in interval arithmetic. The outcome would be that every read-once AND/OR/NOT formula satisfies H ≤ β(1/2) I, with a constant that cannot be lowered. This is the result nearest to finished.
3. Higher-arity gates (hours 3-5). Rerun the value iteration with every arity-3 gate (14 NPN classes) and arity-4 gate (222) added to AND/OR, over a grid of input biases, and certify the tight cases. If the constant stays at 6.4548, that is the sharp constant for read-once formulas over gates of arity up to 4; if it rises, the extremal formula is an explicit function that beats Hod's lower bound. Both are results.
4. The non-read-once step (after that). The reformulation needs gates of every arity, and the only obvious way to lower the arity is a Shannon split on one input, whose two cofactors share variables. I expect this is the step ρ_0 measures. I will write the GMP restriction step in the potential language and compare the note's value of sup ρ_0 with the threshold the induction needs; if it fails, the extremal function shows whether the barrier is real or an artifact of the inequality. If the LTF proof survives, I will try to carry it to biased product measures: composition would then cover read-once formulas over threshold gates of unbounded arity.

## What I avoid

- Level-by-level hypercontractive bounds (KKL, Friedgut, Kelman–Kindler–Lifshitz–Minzer–Safra). They lose a logarithmic factor by construction; the best they give is concentration on 2^{O(I log I)} characters.
- Induction on restrictions without a potential: the cross term between the two cofactors is what goes uncontrolled. I use restrictions only in the GMP form, where the loss has a name.
- Decision-tree and encoding arguments in the style of Wan–Wright–Wu. They pay for the tree (depth, size, number of reads), which can be far larger than the influence.
- Random counterexample searches: a random function has ratio near 2, while the extremal cases are biased compositions such as lexicographic functions, so I search structured families.
- The percolation note (Kalai's Conjecture 8): unverified and specialised.

## First concrete step

Read claim_56de35f4, claim_4fdc5a79, claim_061ad906 and claim_d7e78ede in full with math_note.py and write down the exact definitions of ρ_0 and Γ. Then write one checker that computes H, I, ρ_0 and the gate-inequality slack for all 65,536 functions on four variables, twice (floating Walsh–Hadamard and exact rationals), and on the lexicographic and tribes families up to n = 20. If any statement fails there, the counterexample goes back into the memory before anything else.

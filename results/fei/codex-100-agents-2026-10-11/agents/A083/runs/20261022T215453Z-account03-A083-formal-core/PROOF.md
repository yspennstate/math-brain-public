# Same inherited reference through the next private query

All logarithms are base two. The result concerns one actual Boolean gate and one prescribed mixed-depth history, not all Boolean functions.

Let x,a,b,y be uniform independent bits, and let F=(-1)^a when x=0; otherwise F=2y-1 when b=1 and F=1 when b=0. Query b, then query y only in its b=1 child. Keep the b=0 child as a full terminal.

Write P for the squared Walsh spectrum. Direct character summation gives P({a})=P({x,a})=1/4 and P(S)=1/16 for all eight S contained in {x,b,y}; all other atoms vanish. Consequently H(P)=3, I(F)=3/2, P(empty)=1/16, and the coordinate marginals are (1/2,1/2,1/4,1/4).

For any real c in [3/4,13/16], put r=8c/15, t=4c/15, Z=1-(1-r)^2(1-t)^2, and A=15/(16Z). Define Q_c(empty)=1/16 and Q_c(S)=A r^(S_x+S_a)(1-r)^(2-S_x-S_a)t^(S_b+S_y)(1-t)^(2-S_b-S_y) for S nonempty. This is a strictly positive probability law: 0<r,t<1 and 0<Z<1. At the prior stage's canonical root 1-c=(1-8c/15)^2(1-4c/15)^2, Z=c, so this is exactly the SAME canonical reference. No new reference is admitted at the second query.

## A uniform reference-debt bound

Using the actual spectral masses and marginals, expand the KL exactly:

    D(P||Q_c) = -11/4 -(15/16)log A -log r
                 -(1/2)log t -(7/8)log(1-r) -(11/8)log(1-t).

The empty atom contributes 1/4 to cross-entropy, explaining -11/4 rather than -3. Since Z<1, A>15/16. On the complete closed parameter interval, r>=2/5, t>=1/5, 1-r>=17/30, and 1-t>=47/60. The integer inequalities

    16^8 < 2*15^8,   5^3 < 2^7,   30 < 2*17,   60^2 < 2*47^2

therefore give strict upper bounds 15/128, 4/3, 7/6, 7/8, 11/16 for the five logarithmic terms respectively. Thus

    0 <= D(P||Q_c) < -11/4+15/128+4/3+7/6+7/8+11/16
                   =183/128 <2.

No limiting argument or sampled-parameter inference occurs. The same proof covers the two parameter endpoints. Every logarithm and denominator used is strictly positive in its argument, and the rational inequalities are checked independently in the executable certificate.

## The exact mixed-depth identity

At a physical query erase its Fourier coordinate, obtaining P_e,Q_e. Use K_j(s)=P_j(s)/(2P_e(s)) on source-positive rows and a normalized fixed fallback on source-zero rows. Transport BOTH laws through this same K; let Q_j be the normalized inherited reference and q_j its reference branch probability. The source branch probabilities are 1/2, and

    D(P||Q)=E + D((1/2,1/2)||(q_0,q_1)) +(D(P_0||Q_0)+D(P_1||Q_1))/2,

where E is the source-weighted conditional KL of the erased Fourier bit given the residual mask. This follows by expanding log(P/Q) into the erased conditional ratio and log(P_e/Q_e), then applying finite KL chain rule after the same channel. Source-zero rows retain their entire reference mass. All terms are nonnegative.

For the b=1 child, query y. Its two actual leaves, in x,a input order, are [1,-1,-1,-1] and [1,1,-1,1]. Their unnormalized Walsh vectors are [-2,2,2,2] and [2,-2,2,2]. Hence both squared spectra are uniform on the four residual masks. P_e is 1/4 everywhere and K_0=K_1=1/2 everywhere: there are NO reference-only rows at this second query. Consequently both reference branch probabilities are 1/2, both inherited terminal references equal erase_y Q_1, and the second outcome KL is zero. This statement holds for each of the three tested first-query fallbacks; fairness of the initial fallback is used below only for the explicit old-booking formula.

Put D_j=D(P_j||Q_j), let E_b,O_b be the first erasure and outcome bills, and let E_y be the second erasure bill in the b=1 child. Let D_y be the mean full final KL of its two terminals. Then, exactly,

    D(P||Q_c)=E_b+O_b+(1/2)D_0+(1/2)E_y+(1/2)D_y.

This retains the untouched b=0 terminal and BOTH complete y terminals with their actual reach probabilities 1/2,1/4,1/4.

## The previously booked conditional bill is not charged twice

For the inherited FAIR initial fallback define C=-(1/2)log(1-t), the conditional amount booked in stage 5. Given retained x,a frequencies, the b=0 child has conditional spectator-y KL C, and the b=1 child has the same conditional KL C. At the new query the latter is exactly E_y=C. This follows because a-present rows have actual y frequency zero and reference Bernoulli parameter t; their actual weight is 1/2. On a-absent occupied rows the inherited y frequency is already deterministic and matches the source.

Writing J_j=D_j-C for each retained quotient KL, the old mean booking is C=(1/2)C+(1/2)C. Its first half remains in D_0; its second half is E_y/2. Thus the old booking is moved, not renewed. Also D_y=J_1. The exact total reference bill is E_b+O_b+C+(J_0+J_1)/2=D(P||Q_c). These quotient, source-erasure and outcome terms were the previously unpaid bills.

## One original owner pays the continuation

The two b children have H=2 each and influences 1 and 3/2. Their original mean rate-four surplus is U=4*(5/4)-2=3. This is the same unused account as stage 5, with C already booked; no arbitrary-core FEI hypothesis supplies it. All three final leaves have H=2 and I=1. The y continuation reduces mean influence from 5/4 to 1, so conservatively book a further rate-four energy debit 1.

Charge the source-erasure, outcome and retained quotient bills once, preserving the C booking. Total withdrawals INCLUDING that old booking and the new energy debit are

    C + (E_b+O_b+(J_0+J_1)/2) + 1
      = D(P||Q_c)+1 <311/128 <3.

The SAME original owner therefore retains more than 73/128 bits. Equivalently, complete terminal entropy 2, full tree reference bill D(P||Q_c), and continuation energy debit 1 sum to less than 4*(5/4), with that strict reserve. No mean or pointwise surplus assertion is silently interchanged.

The remaining universal line is unsupported: an analogous inherited positive-profile estimate, under an eligible general restriction policy, is payable from one genuinely unused ancestor source for EVERY Boolean input, including its terminal seed entropy. Nothing here establishes that line. Replacing the untouched core by an arbitrary non-flat Boolean core is the next useful test; repeating fresh occupancy banks would not address it.

## Formal scope

FairContinuation.lean states the fixed two Walsh-square lists and the literal rational fair-kernel equality. Translation to the actual truth tables is independently checked by direct character sums in Python. Fresh memok refused compiler admission; therefore the current Lean source is an UNCHECKED DRAFT. It certifies no theorem in this stage. The mathematical rung reached here is analytic proof with exact finite validation, pending independent review, not Lean-checked entropy or universal FEI.

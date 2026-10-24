# Nested point blocks: a coordinate owner can be exhausted

Uniform independent bits, Boolean signs, entropy in bits. This is a
counterfamily to an explicitly defined terminal-coordinate reservation
rule, not to a universal stopping policy or FEI.

## 1. The single-block interface being consumed

A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER v3, additional whole-block
subtheorem, assigns a fresh point switch F=G+A_s(H-G) the actual reserve
R=2alpha(1-alpha)I(GH), alpha=2^-s. For a data coordinate i its exact
reserve is R_i=2alpha(1-alpha)Inf_i(GH). The source correctly requires
this reserve to be marked once before the entire block and not reissued
at nested ancestors. It proves actual entropy payment, not an upper
bound on localized odd-face currency.

The false extension tested here is: apply that unchanged local R_i to
every reached nested point block, and pay their sum from C times the
final physical terminal influence of the SAME coordinate i, for one
absolute finite C. It is an all-coordinate terminal-bank rule. It
does not permit taking unused influence from other coordinates; a rule
that does permit that is a different target.

## 2. Actual Boolean family and exact coordinate ledger

Let L>=1, and take fresh point blocks A_j of any positive integer widths
s_j. Put alpha_j=2^-s_j, delta=product_j alpha_j, and let z be one
independent fair sign. Define backwards

    F_(L+1)=z,
    F_j=1+A_j(F_(j+1)-1),       j=L,...,1.

Consequently F_1=1+(product_j A_j)(z-1): this is one actual point
activation, of total width S=sum_j s_j. Query blocks in order, stopping
at constant 1 on failure and at z after every block succeeds. Failure
histories are physically disjoint. The original z coordinate has

    Inf_z(F_j)=product_(k=j)^L alpha_k,
    final terminal influence T_z=delta,
    actual total influence I(F_1)=(S+1)delta,
    I_controls=S delta, H_terminal=delta H(z)=0.

At reached block j, inactive branch G_j=1 and active branch H_j=F_(j+1).
Their product equals F_(j+1). Thus the EXACT A023 coordinate reserve is

    R_(j,z)=2alpha_j(1-alpha_j) product_(k=j+1)^L alpha_k.

The physical reach is product_(k<j) alpha_k. Summing gives the identity

    D_z=sum_j reach_j R_(j,z)
       =2delta sum_j(1-alpha_j),
    D_z/T_z=2sum_j(1-alpha_j)>=L.                         (1)

The bound holds for every positive-width vector, with equality L when
all widths are one. For any proposed finite C, choose an integer L>C:
the stated unchanged per-block final-coordinate-bank rule fails. There
is no alternative inactive terminal capacity on z: every inactive leaf
is constant, and Inf_z(1)=0. This is an exact debit of the real reserve,
not a loose bound replacing Inf_z(GH) by Inf_z(G)+Inf_z(H).

The finite witness L=3, s_j=1 gives delta=1/8, D_z=3/8 and T_z=1/8.
It already exceeds the two-unit terminal allowance of a SINGLE A023
block. It does not refute that allowance for its intended single block.

With all widths one, I(F_1)=(L+1)2^-L tends to zero and
P(F_1=-1)=2^-(L+1) tends to zero. Thus this is a parameterized actual
Boolean rare-event family, not a formal ledger with unrealizable leaves.

## 3. Flattening supplies one valid owner

The very same F_1 has the single point block A=product_j A_j of width S.
Apply the reviewed A023 interface to G=1,H=z once. Its coordinate reserve
is

    R_flat,z=2delta(1-delta),
    R_flat,z/T_z=2(1-delta)<2.                            (2)

The gap between the two prescriptions is

    D_z-R_flat,z
      =2delta[sum_j(1-alpha_j)-(1-delta)]>=0.

The inequality is the union bound 1-product_j alpha_j<=sum_j(1-alpha_j),
or a direct induction. For two blocks the difference is EXACTLY
2delta(1-alpha_1)(1-alpha_2)>0. For one-bit blocks,
D_z/R_flat,z=L/[2(1-2^-L)], which grows linearly with depth.
Flattening makes a single original data coordinate have one owner, rather
than treating each intermediate continuation as newly available terminal
capacity. No terminal function is copied or counted with spectral weights.

This repair uses the special compatible constant-failure grammar. It
does not establish a flattening or ownership theorem for branching
controllers with different nonconstant inactive cores.

## 4. Scope and a valid complete policy

Every queried control in this family has a constant child. Its exact
spectral entropy formula, with d its physical disagreement, is

    B/d=2(1-d)+Psi(d^2,(1-d)^2)/d
       <=2+d[log2(e)-2+2log2(1/d)]
       <=2+log2(e)/sqrt(e)<3.

Here Psi(a,b)=(a+b)h2(b/(a+b)), the middle bound follows from
Psi(a,b)<=b log2(e(a+b)/b), and the last follows by maximizing over d>0.
The strict inequality uses ln2>2/3 and e>5/2. The terminal literal z
has B=0. Therefore this complete physical tree has Q_bad,4=0. JS<=2d/ln2
and the influence telescope give H(F_1)<6I(F_1). Neither the family nor
the erroneous coordinate-bank rule is a counterexample to FEI or to
an existential localized stopping route.

The scalar JS inequality and its derivative proof are independently
reconstructed in REVIEW_A023.md; the same document supplies the physical
entropy telescope and the exact terminal endpoint interpretation.

There is also NO unbounded price against the full influence for this
coordinate debit: for one-bit blocks, D_z/I(F_1)=L/(L+1)<1. Unused
control influence could pay it. The result therefore cannot refute a
reserve rule allowed to redistribute across coordinates, signed terminal
slack, a selected query policy, or A023's explicit no-renewal theorem.

## 5. First unsupported universal line

For a genuinely branching nested shared-data controller, no proved rule
merges the inherited source disagreement and the final physical terminal
capacities while preserving each actual terminal entropy and debiting
each coordinate capacity once. Compatible constant-failure chains admit
the exact flattening (2); a universal history-transfer rule does not follow
from that identity. The next target is a three-terminal branching example
with two distinct nonconstant inactive cores, where this flattening is
unavailable, rather than more depth in the paid point chain.

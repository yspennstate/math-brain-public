# Necessary tests for a proposed global potential

Quantifiers matter: the following entropy tests apply to functionals P with H(F)<=P(F)<=C I(F) on every admitted activated core. They do not impose a particular form on arbitrary auxiliary debts.

For balanced seed entropy h and influence i, independent tensor count t and control count k, q=2^-k, c=1/ln2, the exact lower requirement is

    P(F)/q >= th+4k+2c-q(2k+3c)+R(q)/q,
    -2cq^3/[3(1-q)] <= R(q) <= 0.

1. If the class admits t/k->infinity, it retains C>=h/i for each seed. For arbitrary cores it has full-FEI strength. If it admits t/k->0 with k->infinity, it forces C>=4. At t/k->lambda it forces C>=(lambda h+4)/(lambda i+1).
2. Small total influence and small minority probability give no escape: t=k^2 yields both tending to zero and preserves h/i. The balancing lift z product f_j recovers the ratio of every arbitrary nonconstant Boolean f.
3. The exact deficit is q[t(Ci-h)+(C-4)k-2c+q(2k+3c)]-R(q). A limiting seed ratio does not automatically imply a finite constant inherited by the activated family; if C=h/i<4, that deficit is negative for large k.
4. The control-first tree's terminal entropy is qth, with terminal influence qti. Paying J_tree alone cannot settle entropy when the core is arbitrary. Any proposed terminal bound must state how it pays this term without borrowing already spent control influence.
5. Keep the KL rebate: J_tree=q(k+A_k), 0<=A_k<=3. The unrebated rarity sum is qk(k+1)/2. The additive 3c mu allowance sums to 3ckq and is separately paid; adding it to a paid influence bank twice is invalid.
6. For the specific potential J_tree+terminal_entropy, a uniform bound by K I necessarily has K>=max(1,h/i). This selector coefficient is 1; the actual entropy coefficient is 4. Conflating the two changes the claim.

The control-only debt is proved paid for this family. The arbitrary terminal-core payment remains OPEN. A087/A094 should review REPORT.md Sections 3-5 before downstream use.

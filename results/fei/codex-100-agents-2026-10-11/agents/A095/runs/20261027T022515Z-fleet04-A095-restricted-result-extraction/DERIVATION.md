# Exact cancellation pays the complete edited path

Uniform Boolean cubes; normalized Walsh coefficients; costs in bits. This is
an extension of A095 stage20's supplied-owner theorem. Full FEI remains open.

1. Let h on a remaining source bits satisfy h(0)=1, padded by m bits.
Write e=2^(-a-m), u=2^-m, M=1/e, A for its padded Fourier amplitudes.
The data-only point reversal h-2*1_0 has probability q_S=(A_S-2e)^2.
Its prescribed normalized floor is R_S=(A_S^2+4e^2)/(1+4e).
Both sum to one because sum A=1, sum A^2=1 and M e=1.
Every R_S is positive. There are N<=2^a=u/e nonzero A_S.

The polynomial identity

    (A-2e)^4=(A^2+4e^2)(A^2-8eA+20e^2)-64e^4

gives the EXACT chi-square formula

    chi2(q,R)=16e+48e^2-64e^4(1+4e) sum_S 1/(A_S^2+4e^2).

Retaining just the M-N zero amplitudes in the last nonnegative sum gives

    chi2(q,R)<=16u e+(-16+64u)e^2<=16u e,  if m>=2.

The second inequality is precisely where u<=1/4 is used. Since ln2>2/3,
KL_2(q||R)<=chi2/ln2<24u e. No amplitude quantization is needed.

2. At any actual physical node of original reach p, replacement of an
arbitrary finite-cost subprobability model Q by R has signed charge
p[D(q||R)-D(q||Q)]. Its positive part is less than 24 p u e because
complete subprobability divergence is nonnegative. This covers actual inherited
models with their true normalizers and zero-support reference mass.

Start with exactly the original stage20 source-first policy: arbitrary
nonconstant g on a>=1 bits, m>=2 padding bits, and one selector; reverse
the full zero point, after translating/negating so g(0)=1. Fix the original
source R0, c=CE(Pg,R0)<=C0 Ig, mass in (0,1], C0>=0, and K=4C0+15.
Use the actual root model (R0 padded+3e0^2)/(1+3e0), lifted by the TRUE
selector conditional law, e0=2^(-a-m). Retain all compatible old debit
0<=U<=(C0+37/8)Ig. No already executed history is undone.

Query any d source coordinates along the edited branch, 0<=d<=a,
installing stage20 exact-source point-selector floors at root and each
matching prefix. Their total positive charge is <381 Ig/128 (stage20,
DERIVATION sections1,3,6). Then expose the actual selector. In the edited
child install R above. Continue querying the remaining a-d source bits
along the edited branch in any order, installing this DATA-only floor at
every matching child. The padding remains m>=2 throughout these queries.
At original source depth k the edited data-only node has reach 2^(-k-1)
and e_k=2^k e0. Thus each floor's positive charge is <12u e0. There are
a-d+1<=a+1 such floors, including the initial selector-child floor. Since
Ig>=2a*2^-a for nonconstant g (edge-cut bound, stage20 section3),

    total DATA-source floor positive charge / Ig
      < 6u^2(a+1)/a <=12u^2<=3/4.

This includes the constant-source endpoint a_remaining=0.

3. Now query the m remaining padding bits in any order along that same
edited branch, installing the actual constant-source DATA-only floor after
each matching query. The current source is h=1, so A_empty=1 and all other
A vanish. For e=2^-r, with r remaining padding bits, the exact formula is

    chi2=64e^3(1-e)/(1+4e^2).

For r>=2, D<96e^3 and original reach is e0/(2e). The positive charge is
therefore <48e0 e^2. Even summing over ALL r>=2 (a harmless enlargement
which includes the already booked initial r=m floor), this is <=4e0.
At r=1 the edited function is minus the surviving coordinate, q=(0,1),
R=(2/3,1/3), so D=log2(3)<2 and the positive charge is <2e0.
At r=0, q=R=(1), D=0, so its reset charge is nonpositive and is not
reclaimed. Consequently ALL additional padding resets cost <6e0<=3Ig/4.
This last inequality uses e0/Ig<=u/(2a)<=1/8. It holds also when m=2,
where the r>=2 additional sum is actually empty.

4. For the actual inherited physical transport, parent complete CE minus
mean child complete CE is the complete query release. Stage20 section2
derives its nonnegativity including the actual child normalizers. Let Bfull
be the sum of every reached such release plus ALL full frontier terminal CE,
including every sibling. Exact telescoping gives

    Bfull=CE_root+sum signed actual resets
          <=CE_root+sum positive actual resets.

We use this stronger ledger, not merely Hroot+mean terminal D. In particular
the accumulated physical-query KL contraction is retained, as required by
A094 stage21's objection to the A011 draft transaction identification.
No physical-query divergence or negative reset is refunded as fresh quota.
The initial stage20 root bound after old U is

    K I(F)-U-CE_root >= (C0/2+53/8)Ig+4C0 G,
    G=e0(a+m+1-d0),

where d0 is the original pivotal degree at the edited point. The three
positive-booking totals above sum to <(381/128+3/4+3/4)Ig=573Ig/128.
Thus EVERY intermediate frontier, through the entire matching path to a
constant leaf, satisfies

    K I(F)-U-Bfull > (C0/2+275/128)Ig+4C0 G >0.

Both child terminals, original source cost, all old debits, and every complete
query release remain in this inequality. Nonmatching branches may undergo
any inherited-only finite restriction tree without changing Bfull. The
choice of source query order and selector depth is arbitrary; resets on
nonmatching branches are not included. The original R0,C0,K never renew.

5. What could fail and how it is checked: the division identity, zero-mask
count and both normalizations are checked exactly on all labelled sources
through a=3 and all frozen padding values. Physical histories separately
check true child tables, both inherited models, every signed charge and
the stronger full-release ledger. Constant, dictator, parity, majority and
asymmetric sources test support zeros and unused source bits. The e=1/2
and e=1 endpoints are handled explicitly, never by the u<=1/4 estimate.
The key polynomial is submitted to Lean; its receipt is reported separately.
The full entropy theorem is an author proof, not a formalized theorem or an
independently accepted result.

The first unsupported universal step is an ORIGINAL dimension-independent
influence-priced source for arbitrary g, or payment of a REQUIRED branching
reset policy/new interacting edit from the still diminished owner. Completing
this optional matching path does not establish such a necessity or full FEI.

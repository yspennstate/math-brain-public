# A complement-invariant logarithmic potential contracts under unequal NAND

Status: proved below and self-checked; novelty UNVERIFIED. This closes the unequal-block gap left in `NAND_LOG_POTENTIAL_2026-09-18.md`. It gives an explicit bound for read-once NAND/De Morgan formulas, a class already known to satisfy FEI by stronger composition theorems. It does not address arbitrary Boolean functions and does not prove full FEI. `SHANNON_POTENTIAL_BARRIER_2026-09-18.md` subsequently proves that this potential has an unbounded one-coordinate restriction defect.

All logarithms are base two unless `ln` is written.

## 1. Indicator functionals

Let A be a nonconstant {0,1}-valued function, with mean alpha and Fourier coefficients c_S. Define

    K_A=sum_edges min(c_S^2,c_T^2)|log(c_S^2/c_T^2)|,
    Q_A=sum_i c_{i}^2,
    I_A=4 sum_S |S|c_S^2=I(1-2A).

As in the earlier note, put

    U(A)=K_A-2Q_A log(alpha).                           (1)

For an indicator, every nonempty Fourier coefficient has absolute value at most both alpha and 1-alpha. Consequently the empty--singleton terms in (1) simplify and

    U(A)=sum_edges not touching empty
           min(c_S^2,c_T^2)|log(c_S^2/c_T^2)|
         +sum_i [-c_i^2 log(c_i^2)] >=0.                (2)

In particular U is invariant under complementation: U(1-A)=U(A). Define the strengthened potential

    V(A)=U(A)+(2/ln 2)Q_A.                              (3)

## 2. Exact unequal-product identities

Let A_1,...,A_k be indicators on disjoint variable blocks, with means alpha_j in (0,1). Set

    A'=1-product_j A_j,    p=product_j alpha_j,
    w_j=p/alpha_j=product_{l!=j} alpha_l.               (4)

We prove

    I_A'=sum_j w_j I_Aj,
    Q_A'=sum_j w_j^2 Q_Aj,                              (5)

and

    U(A')=sum_j w_j U(A_j)
       +2 sum_j w_j Q_Aj beta(alpha_j,w_j),             (6)

where

    beta(alpha,w)=(1-w)log(alpha)-w log(w).              (7)

Proof. The Fourier coefficients of the product factor across blocks. When an edge changes a coefficient inside block j, summing the squared coefficients over all other blocks gives

    product_{l!=j} sum_R c_(l,R)^2
       =product_{l!=j} E[A_l^2]=w_j.

This proves the influence identity. A global singleton in block j has coefficient w_j c_(j,{i}), proving the Q identity.

Complementing the product changes only its empty Fourier coefficient, from p to 1-p. The global singleton coefficients remain w_j c_(j,{i}). Since a nonempty indicator coefficient is bounded by the mean of the indicator and of its complement, each singleton magnitude is at most both p and 1-p. Hence the minimum squared mass on every empty--singleton edge is the singleton mass, and

    K_A'=sum_j w_j K_Aj
       +2 log((1-p)/p) sum_j w_j^2 Q_Aj.                (8)

Subtract `2Q_A' log(1-p)` and use `log p=log alpha_j+log w_j`. The contribution belonging to child j becomes

    w_j K_Aj-2w_j^2 Q_Aj log p
      =w_j U(A_j)
       +2w_j Q_Aj[(1-w_j)log alpha_j-w_j log w_j],

which proves (6).

## 3. Contraction for arbitrary unequal children

For 0<w<=1,

    beta(alpha,w)<=(1-w)/ln 2.                          (9)

Indeed `(1-w)log(alpha)<=0`, and

    -w log_2(w)<= (1-w)/ln 2

is equivalent to `w ln(1/w)<=1-w`, which follows from `ln x<=x-1` with x=1/w.

Insert (9) into (6), then add the Q term from (3):

    V(A')
      <=sum_j w_j U(A_j)
         +(2/ln2)sum_j w_j(1-w_j)Q_Aj
         +(2/ln2)sum_j w_j^2 Q_Aj
       =sum_j w_j V(A_j).                               (10)

Together with (5), every nonconstant output satisfies

    V(A')/I_A' <= max_j V(A_j)/I_Aj,                    (11)

where constant children can be deleted or handled by continuity with V=I=0. Unary complementation preserves V and I exactly.

This is the point missed by the earlier attempted potential. The negative term `(1-w)log alpha` in (7) need not be used: the positive term alone is exactly paid by the loss

    sum_j w_j Q_Aj - Q_A'
      =sum_j w_j(1-w_j)Q_Aj

in the added singleton potential. No equality of block means is required.

## 4. Transfer to the Boolean logarithmic functional

Let F=1-2A. Its nonempty Fourier coefficients are -2c_S and its empty coefficient is d=1-2alpha. Every edge not touching the empty set contributes four times its term in (2).

For an empty--singleton edge put x=c_i^2<=1/4, q=4x and r=d^2. We claim

    min(q,r)|log(q/r)| <=4[-x log x].                   (12)

If r>=q, the left side is at most `q log(1/q)`, which is at most `q log(4/q)=4[-x log x]`. If r<=q, the maximum of `r log_2(q/r)` over r in [0,q] is `q/(e ln2)`, while `q log_2(4/q)>=2q`; this again proves (12). Zero endpoints follow by continuity.

Summing gives the universal comparison

    K(F)<=4U(A)<=4V(A).                                 (13)

## 5. Explicit read-once consequence

For a literal indicator A=(1+x)/2,

    K_A=0,  Q_A=1/4,  U(A)=1/2,  I_A=1,
    V(A)/I_A=1/2+1/(2 ln2).                             (14)

Inducting with (11) over any read-once NAND tree on disjoint variables, and allowing free complementation, proves

    K(F)/I(F) <= 2+2/ln2.                               (15)

The earlier general relations

    K<=B<=K+(2/ln2)I,

and the erasure reduction therefore give, for this class,

    B(F)/I(F) <= 2+4/ln2,
    H(F)/I(F) <= 2+6/ln2.                               (16)

AND, OR and NOT preserve the read-once property when expressed by NAND and complementation, so the same bounds cover read-once De Morgan formulas.

This class consequence is not claimed as new. O'Donnell and Tan, arXiv:1304.1347, prove FEI for read-once formulas over arbitrary bounded-arity gates. The contribution here is only the explicit contracting potential (3) for the live logarithmic-edge approach, with no identical-block assumption. Its relationship to previously known potentials is UNVERIFIED.

## 6. Limit of the result

An arbitrary Boolean function is not a disjoint product/complement tree, and (10) gives no seed-independent estimate for an arbitrary indicator A. The full remaining task is still a universal bound for K(F)/I(F) under the signed Boolean convolution constraints. The proved contraction says that unequal read-once NAND composition cannot amplify the normalized potential above its worst leaf or seed; it does not bound general seeds.

`check_unequal_nand_potential.py` verifies the exact product recurrences, the V contraction on deterministic unequal examples, the comparison K(1-2A)<=4U(A) for every indicator through three variables, and recursive literal NAND examples. Rational quantities are exact and logarithms use outward rational interval enclosures. The universal claims above are proved algebraically, not by enumeration; the script is a self-check, not an independent audit.

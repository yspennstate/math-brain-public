# Strong FEI under disjoint products with arbitrary child output bias

2 October 2026. Complete elementary derivation, conditional on the audited
strong bounds for the indicated base functions. The product identities are
standard Fourier tensorization; no historical novelty is claimed for them.
All leaf inputs are independent uniform signs. Output bias is unrestricted
in this product step; this is not a theorem for nonuniform input laws.

Write H(f) for the entropy of the entire squared Fourier spectrum, including
the empty coefficient, I(f) for total physical influence, and V(f)=Var(f).
Let f_1,...,f_r be Boolean functions on pairwise disjoint coordinate blocks,
and put F=product_j f_j. The blocks may contain irrelevant variables and
the children may be constant. Suppose one C>=0 satisfies

    H(f_j)<=C[I(f_j)-V(f_j)]

for every j. Then the SAME C satisfies

    H(F)<=C[I(F)-V(F)].

## Exact Fourier and physical identities

Every spectral set S decomposes uniquely as the disjoint union of its
block intersections S_j. Expanding the product gives

    Fhat(S)=product_j f_jhat(S_j).

Consequently its squared spectral law is the independent product of the
children's squared spectral laws. This remains true when S_j is empty;
balance is unnecessary. Entropy additivity for a finite product law gives

    H(F)=sum_j H(f_j).

The convention 0 log(1/0)=0 handles zero coefficients. For a coordinate in
block j, flipping it changes F precisely when it changes f_j, because all
other factors are signs and their product is nonzero. Hence

    I(F)=sum_j I(f_j).

Independence also gives E F=product_j E f_j. Since each Boolean function
has second moment one,

    V(F)=1-product_j (1-V(f_j))<=sum_j V(f_j).

The last inequality is the elementary union bound for numbers in [0,1],
or follows inductively from 1-(1-a)(1-b)=a+b-ab<=a+b.
Combining all three identities and the child strong bounds yields

    H(F)<=C[sum_j I(f_j)-sum_j V(f_j)]
        <=C[I(F)-V(F)],

as claimed. No assumption on any child mean is used.

## Audited base-class consequences and mixed trees

The internally audited [strong LTF theorem](../2026-10-02-strong-LTF-composition/strong_ltf_and_balanced_composition_proof.md)
and [strong slab theorem](universal_split_deficit_and_slab_composition_proof.md)
supply the respective class-wide constants. Arbitrary disjoint products
of LTFs, of parallel-slab gates, or of their already strong balanced
read-once formulas therefore satisfy the strong inequality with the
maximum of those constants, even when these factors have different,
nonzero output means.

More generally, consider a read-once tree on disjoint leaf blocks with
two kinds of internal nodes: a product node, or a gate from a class with
the same strong constant. At a product node, child outputs can have
arbitrary bias. At any other gate node, all its child outputs must be
balanced. The exact balanced composition law is derived in the linked
slab theorem and gives H<=C(I-V) at that node. The product argument here
gives it at a product node. Uniform sign leaves have H=0 and I=V=1,
so structural induction proves the same strong inequality for the full
tree. Root output bias is unrestricted. Complementation and input sign
changes preserve the bound.

This does not remove the balance assumption at a general slab or LTF
composition node, and it does not cover shared-input circuits. The product
of overlapping factors need not have an independent product spectral law.

## Scope and sources

This is a corollary of the audited strong base bounds and elementary
tensorization, not unrestricted Boolean FEI. The disjoint-product identities
and the general balanced composition framework are established tools;
O'Donnell--Tan's 2013 paper is credited by the companion source record.
Historical priority and external peer review for these derived applications
remain unverified. The uniform input law throughout is essential to the
stated Fourier normalizations.

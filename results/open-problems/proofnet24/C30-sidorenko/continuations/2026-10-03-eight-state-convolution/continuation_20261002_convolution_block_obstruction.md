# Exact obstruction to individual convolution-block positivity

2 October2026. This is an obstruction to a stronger possible proof step,
not a counterexample to ML10 Sidorenko or Rossman's stated conjectures.

For a Boolean convolution host W=np_(x+y), use pair coordinates(u,d),
where d=x+y and u=x. Fourier transformation in u decomposes the normalized
ladder transfer into blocks indexed by a character chi. Omitting the
common positive scalar from normalization, the block is

    B_chi(d,e)=sqrt(p_d p_e) chi(d) c_chi(d+e),
    c_chi(k)=sum_z chi(z) p_z p_(z+k).

The change z->z+k shows c_chi(k)=0 whenever chi(k)=-1. For nontrivial chi,
write the two coset profiles on K=ker chi as a,b>=0. On K,

    c_chi=a*a-b*b.

The block therefore splits as Da C Da on the positive coset and
-Db C Db on the negative coset, where Da=diag(sqrt(a)), Db similarly,
and C is convolution by a*a-b*b. Its odd trace is

    tr((Da C Da)^m)-tr((Db C Db)^m).                         (1)

It would be useful if (1)>=0 separately for every chi and m=5. This is
FALSE already when K=F2, hence in a four-state host already covered by
the earlier quantitative theorem.

Take a=(1,1), b=(3/2,0). Then

    C=[[-1/4,2],[2,-1/4]],
    Da C Da=C,
    Db C Db=[[-3/8,0],[0,0]].

The first matrix has eigenvalues7/4 and-9/4. At m=5 the exact value of
(1) is

    (7/4)^5+(-9/4)^5-(-3/8)^5
       =-1351501/32768<0.

Scaling all four p entries to make their sum1 only multiplies this
number by a positive factor, so it does not change the failure.
The full density sums all Fourier blocks, and the complete Klein4
inequality ensures that total still satisfies Sidorenko. Thus a valid
general convolution proof must permit cancellation between different
character blocks; positivity of every odd block trace is unavailable.
The standard full transfer identity and Fourier diagonalization are not
claimed as new tools here.

# Independent audit: disjoint-product deficit corollary

Date: 2026-10-02. **PASS, conditional on the stated strong base bounds.**
I read `disjoint_product_deficit_corollary.md` in full and independently
rederived the product identities and mixed-tree induction. No gap was
found. No author file was modified.

For Boolean sign functions on disjoint uniform input blocks,
\(F=\prod_j f_j\) has the exact Fourier coefficient identity
\(\widehat F(S)=\prod_j\widehat f_j(S\cap B_j)\). The squared spectrum
is consequently a product probability law, including its empty atoms,
so \(H(F)=\sum_j H(f_j)\). Empty spectral sets require no balance
assumption. Constant factors and irrelevant coordinates cause no change
to the argument.

Flipping a coordinate changes the product precisely when it changes
its own sign-valued factor. Thus \(I(F)=\sum_j I(f_j)\). Independence
gives
\[
 V(F)=1-\prod_j(\mathbb E f_j)^2
      =1-\prod_j(1-V(f_j))\le\sum_jV(f_j).
\]
Therefore, for one \(C\ge0\),
\[
 H(F)\le C\sum_j[I(f_j)-V(f_j)]
      \le C[I(F)-V(F)].
\]
The inequality direction is correct: the product's deficit is at least
the sum of the child deficits. Child output means can have arbitrary
sign or magnitude, including zero and one.

Using the maximum of different child constants is also valid because
\(I(f)-V(f)=\sum_{S\ne\varnothing}(|S|-1)\widehat f(S)^2\ge0\).
This elementary Fourier identity supplies the nonnegative budget needed
when enlarging a child's constant.

For the stated mixed read-once trees, independent child blocks are
preserved at every node. A product node uses the tensorization argument
above with arbitrary child output bias. Every other gate node requires
balanced children and a strong bound for its outer Boolean gate with
the same constant. Under those conditions, the exact balanced
composition identities from the companion proof apply, and cancel the
outer total influence without changing the constant. Induction starts
at uniform sign leaves, where \(H=0\) and \(I=V=1\), and proves the
same bound at the root. Root bias is unrestricted.

The balance requirement is local to every nonproduct composition node:
a biased subtree can occur as a child of a product node, but cannot
automatically be fed into a later nonproduct gate. The draft states this
condition correctly. Shared inputs and overlapping factors are outside
the theorem. Complementation and input sign changes preserve the squared
spectrum, influence, and variance.

This is an elementary corollary of the separately audited strong LTF
and slab bounds and the established balanced composition framework. It
does not prove unrestricted Boolean FEI. This internal audit makes no
claim of historical novelty or external peer review; numerical testing
is unnecessary for these exact tensorization identities.

# B19 / A094 independent review — reused-character activation

**Run:** `20261014T064440Z-fleet01-B19-reused-character-review-a094`  
**Primary packet:** A094  
**Reviewed claim:** `B05-A023-REUSED-CHARACTER-EQUIVALENCE-v1`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **ACCEPTED AT DECLARED ROUTE-OBSTRUCTION SCOPE**  
**New result:** **cone-preserving repair at \((7/4,1/4)\) REFUTED**  
**Full FEI:** **OPEN**

## Audited candidate and GU implication

The reviewed claim replaces the fresh balancing character in
\(\mathcal T(q)=A(yq)\) by an existing coordinate \(x\). It asserts that
\(q\mapsto A(xq)\) is exactly ordinary activation under a Boolean
involution, derives the complete signed slice surcharge, and refutes the old
half-contraction. If an all-core restriction-closed reuse theorem existed,
its class would already contain every Boolean function; it would therefore
be a universal GU candidate, not a proper-class transfer.

## Verdict on the B05 claim

The equivalence, \(B\)-invariance, influence identity, \(G\)-drift formula,
and substitution into the accepted activation recurrence are all correct.
For \(q=x\), the half-contraction residual is exactly \(c/2>0\), so the
producer's template refutation is also correct. No proof repair was needed.

## New adversarial result

The producer proposed zero-cone preservation as the next viable target. At
the inherited proper-class pair it already fails. For four-bit mask `10049`
and coordinate `3`,

\[
L_{7/4,1/4}(q)=-\frac18,
\qquad
L_{7/4,1/4}(A(xq))=0.123593554500714\ldots>0.
\]

The positive sign is exact:

\[
256L_{7/4,1/4}(A(xq))
=\log_2\frac{2^{1952}3^{711}}
{5^{410}13^{416}17^{136}}>0.
\]

Thus replacing half-contraction by
\(L(q)\le0\Rightarrow L(A(xq))\le0\) does not preserve the existing
constants. A larger \(c\), a terminal reserve, or a different signed
potential remains possible.

## Independent computation

`REPRODUCE.py` uses direct rational character sums and represents every
entropy expression by rational prime exponents. It does not import the B05
checker. It checked 2,476 Boolean cores, 9,804 coordinate cases, and 29,412
exact signed identities. The witness sign used direct integer products.

## Scope

The accepted theorem is a route obstruction, not an admissible universal GU
pair. The new finite witness refutes one cone-preserving pair only; it is not
a GU or FEI counterexample. Since B19 found the witness, its claim requires a
fresh A085/A090 review.

The next useful target is to determine the minimum \(c\) for which the cone
implication might survive, or to prove that no fixed \(c\) works by tensoring
or rare-suspending an exact witness while retaining the signed terminal
reserve.

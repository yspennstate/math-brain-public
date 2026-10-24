# Second proof-chain challenge

This file records the independent chain in the shortest checkable form.

1. **Exact base data.** Independent Walsh arithmetic gives
   $\rho=1/8$ and $A=6911/960>7$.
2. **Cocycle normalization.** The distinguished-input energy is
   $\beta_k=(1-8^{-k})/2$; no virtual-selector or missing physical-input
   normalization is used.
3. **Endpoint derivative.** Differentiating each non-full cap atom gives
   the signed contribution
   $-p\log_2(C/p)+p(1+C)/(2C\ln2)$. The discarded terms are
   nonnegative, so the lower-bound direction is valid.
4. **Tensor amplification.** $\sum p/C=A^k$ and
   $U(u^{\otimes k})=kU(u)\le4k$, giving an exponential lower bound
   minus a linear cost.
5. **Boolean source embedding.** The $8k$-bit point defect has
   $r=2^{-8k}$ and $I(h)=16kr$. Since every tensor cap is at least
   $64^{-k}$, $r/(qC)\le1/2$ and the logarithmic lower bound is uniform.
6. **Finite falsifier.** The $k=1$, two-bit child composition has six
   physical inputs. An exact prime-exponent comparison proves its
   normalized remainder is greater than $4$.

No step supplies a universal joint outer/child payment. The accepted
result is therefore a precise child-only no-go, not a proof or refutation
of FEI.

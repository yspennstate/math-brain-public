# B09 / A043 — genuine disjoint prime decomposition and lossless potential closure

**Run ID:** `20261012T004750Z-account01-B09-A043-prime-decomposition`  
**Primary packet:** A043 (Prime-gate decomposition)  
**Gap:** `G-PRIME-GATE-POTENTIAL`  
**Attempt:** `A043-attempt-01-honest-prime-tree`  
**Claim version:** `B09-A043-PRIME-DECOMPOSITION-v1`  
**Mathematical status:** **AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW**  
**Full FEI:** **OPEN**

## 1. Bounded objective and prior status

A042's endpoint corrections and A045's biased-realizability audit are already author-complete pending review. A043 was still an unproved design target: define genuine irreducibility under disjoint composition, prove termination, inherit product biases correctly, and state the exact arity-uniform implication without pretending that the prime hypothesis is already easier than FEI.

This run fixes one notion of honest factorization, proves a terminating prime tree, proves a lossless prime gate-potential closure theorem, and gives one structural restriction: every essential prime of arity at least three is non-canalizing.

## 2. Genuine disjoint primes

Delete all inessential variables first. For an essential `n`-variable Boolean sign `f`, an honest nontrivial factorization is

\[
f(x)=G(g_1(x_{B_1}),\ldots,g_k(x_{B_k})),
\]

where the `B_i` partition the essential variables, `2<=k<n`, every child is nonconstant and essential on its entire block, and the outer gate depends on every input port. The inequality `k<n` removes the tautological all-literal representation.

An essential gate of arity at least two is prime if it has no such factorization. Constants are nullary atoms; signed literals are unary atoms. The definition is invariant under input/output negations and permutations. Affine parity of arity at least three is composite through binary XOR/XNOR; binary XOR/XNOR is prime only at the base arity two. Consecutive parity nodes may be flattened for display, but uniqueness is not claimed.

### PROVED: termination

Recursively choose any honest factorization until none exists. At an `m`-variable node, the outer arity `k` and every child-block size are strictly below `m`. Arity therefore strictly decreases along every branch. The tree is finite and has depth at most `n-1`; physical leaf blocks remain disjoint.

### PROVED: prime gates are non-canalizing

If an essential `n>=3` gate has a constant section `f|_{x_i=a}=c`, let `g=f|_{x_i=1-a}`. Essentiality makes `g` depend on all `n-1` other variables, and

\[
f(x)=G(x_i,g(x_{-i})),\qquad G(a,v)=c,\quad G(1-a,v)=v.
\]

This is an honest binary factorization with `2<n`. Hence no essential prime of arity at least three is canalizing. This removes iterated AND/OR and selector-style redundancy from the prime obligation, although arbitrary non-canalizing gates can remain prime.

The complete definitions and proofs are in `PRIME_GATE_DEFINITION.tex`.

## 3. Exact entropy and deficit composition

Let `F=G(g_1,...,g_k)` on disjoint uniform blocks. Put

\[
p_i=\Pr(g_i=1),\quad V_i=4p_i(1-p_i),\quad
\alpha_i=\mathcal I_i^\nu(G),
\]

where `nu` is the product law of the child outputs. After contracting deterministic children, the exact squared-spectrum mixture gives

\[
\mathcal H(F)=\mathcal H_\nu(G)
+\sum_i\frac{\alpha_i}{V_i}
[\mathcal H(g_i)-h_2(V_i)],                            \tag{3.1}
\]

\[
\mathcal I(F)=\sum_i\frac{\alpha_i}{V_i}\mathcal I(g_i). \tag{3.2}
\]

Consequently the constant-`C` deficit `D_C=C I-H` obeys

\[
\boxed{
D_C(F)=\sum_i\frac{\alpha_i}{V_i}
[D_C(g_i)+h_2(V_i)]-\mathcal H_\nu(G).
}                                                        \tag{3.3}
\]

Equation (3.3) precisely identifies the unpaid outer-gate entropy and retains every child deficit and normalization refund. It is broader than disjoint tensor multiplication but requires genuine disjoint physical blocks; it says nothing about reused children or shared variables.

## 4. PROVED: prime gate-potential equivalence with no depth loss

Let `Q_2` be the dyadic probabilities and let `Gamma:Q_2->[0,infinity)` be symmetric with endpoint values zero. Define

\[
W_\Gamma(p)=\frac{\Gamma(p)+h_2(V_p)}{V_p},
\qquad V_p=4p(1-p).
\]

For every prime gate `G` and every vector of interior dyadic biases, require

\[
\Gamma(p_{\rm out})+\mathcal H_\nu(G)
\le\sum_i\mathcal I_i^\nu(G)W_\Gamma(p_i).             \tag{PG}
\]

Constants and signed literals satisfy the endpoint/equality conventions. If (PG) holds with the same `Gamma` for every prime arity and `Gamma(1/2)<=C`, then it propagates up any prime tree. At each substitution, (3.1) cancels the `h_2(V_i)` normalization term supplied by the outer inequality, while (3.2) transports the remaining weights. Thus the root satisfies

\[
\Gamma(p_{\rm out})+\mathcal H(f)
\le\Gamma(1/2)\mathcal I(f)\le C\mathcal I(f).
\]

There is no depth or fan-in loss. All inherited biases are dyadic because every subtree is a finite uniform Boolean function. Conversely, if uniform FEI holds with constant `C`, the source-exact encoder-deficit potential

\[
\Gamma_C(p)=\inf_{\Pr(g=1)=p}\{C\mathcal I(g)-\mathcal H(g)\}
\]

satisfies the gate condition for every gate, hence for primes. Therefore FEI with constant `C` is equivalent to the prime condition with the same constant.

This is a rigorous reduction, not a solution: the prime condition still quantifies over unbounded arity and all inherited dyadic biases, and any hard function may itself be prime. The exact quantifiers and induction are in `PRIME_ENDPOINT_IMPLICATION.md`.

## 5. Adversarial controls and scope

- **Deterministic endpoints:** constant children are frozen before division by `V_i`; raw `0/0` is never assigned a value.
- **Dyadic versus real biases:** the full-uniform implication only needs inherited dyadic biases. An arbitrary-real extension still needs A045's separately specified continuous potential.
- **Weighted controls:** the event-TC, coefficient-one pivotal, and conditional-input-TC failures remain at their established scopes. None refutes the exact potential ledger.
- **Repeated children:** `G(h,h)` is outside honest disjoint composition and is not covered.
- **Tensor guard:** (3.1) is a physical disjoint-composition identity, not a shared-variable tensor claim.
- **Addressing and sparse defects:** if prime, they remain inside the universal prime hypothesis; the reduction does not silently discharge them.
- **Parity:** higher parity is explicitly composite; parity flattening is a presentation convention only.
- **Boolean realizability:** every node is an actual truth-table gate; no squared-mass surrogate is admitted.

## 6. Exact bounded verification

`CHECK.py` uses exact `fractions.Fraction` Walsh arithmetic and 90-digit `Decimal` logarithms. It performs two independent checks:

1. It generates every honest factorization through four variables and classifies all essential gates. It verifies that no prime at arity three or four is canalizing.
2. For all 16 binary outer truth tables and all pairs of 14 nonconstant two-bit children—3,136 compositions—it compares every directly computed four-bit squared Fourier mass with the product-biased composition formula, checks Parseval and influence exactly, and checks entropy additivity to 75 decimal places.

Natural command:

```text
python3 CHECK.py | tee CHECK.out
```

Actual output:

```text
n=3: essential=218, decomposable=114, prime=104, canalizing_primes=0
n=4: essential=64594, decomposable=7354, prime=57240, canalizing_primes=0
Composition cases checked: 3136
Maximum entropy-chain error: 1E-89
Assertions passed: 20016
Assertions failed: 0
```

The finite enumeration is a reproducer and boundary audit. The all-dimensional decomposition and implication are proved on the page.

## 7. Sources actually used

- Current B09 compact contract, SHA256 `b57505c28dbfd694a4975bd76773bbc3b2a0f3e6d78c664d57094580bebb4201`, fetched again from the private repository in this run.
- `source_material/reductions/paper/biased.tex`, local SHA256 `77620629b7f27753ad6a757a47ac6cb4aae7bfdd2697e1e91b6978a7db302067`; its pinned source provenance is open-problems commit `10bd8f25e7f93509b1ccb4daf9d8999fcb776f98`, Git blob `b620357b573b2906e8cb2df5966576c27ce3ffcd`.
- A045 biased-realizability report, local SHA256 `bd6984e3866dc718c6f8a17deae116d83f872b71e82a4b592d075cdb74b08162`, with canonical readback previously recorded at open-problems commit `dd1c6af0ac8fbca0262956666546d44ac0e969e0`.
- A042 endpoint report SHA256 `0d6f686b0616e2af08720e8027bc829bbcfb06179da8802408100d66b54d4887` and weighted-controls report SHA256 `a0d368965d772fb5321909e0448c394c5a20ec9bb5c6415b5e00e3f06d2595c1`.
- Execution protocol SHA256 `826d2ff918e3677c425381d3552849f8b9f0fe9eaebe9d1ecf92c2f4d9bdb301` and obstruction registry SHA256 `bd47485f3d32bd0878303d7374f584ab9f71806c313d325703da2a31456385e8`.

The named A056 upstream packet was not available as a separate local original artifact. No theorem was imported from its registry label; the exact composition identity was reconstructed from the pinned `biased.tex` source.

## 8. Status and next action

A043's two author-side deliverables and all three acceptance criteria are met. Independent review by A091/A090 is absent, so packet acceptance is not claimed. Full FEI remains OPEN.

The next productive packet is A044: use the prime definition to seek an arity-uniform corrected FEI+ inequality for a genuinely non-canalizing, non-parity prime family, with arbitrary inherited biases and the same potential at every depth.

Runtime exposed Codex based on GPT-5; no separate reasoning-effort selector was exposed.

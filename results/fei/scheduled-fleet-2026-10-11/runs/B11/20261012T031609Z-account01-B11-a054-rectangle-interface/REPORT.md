# B11 / A054 — paid rectangle interface for critical sources

**Run:** `20261012T031609Z-account01-B11-a054-rectangle-interface`  
**Primary packet:** A054 (Connectedness alternatives)  
**Attempt:** `A054-RECTANGLE-INTERFACE-1`  
**Claim:** `B11-A054-RECTANGLE-INTERFACE-v1`  
**Gap:** `G-CRITICAL-INTERFACE`  
**Status:** controlled-excess theorem PROVED pending independent review; universal cut admission OPEN; full FEI OPEN.

## Frozen target and prior status

A052 proved exact tensor purity and the child-ratio slack identity for genuine
physical descendant-critical sources. A053 proved a quantitative near-tensor
separation theorem, but its hypothesis started from an already supplied
Boolean product approximation. The unpaid A054 step was to define an interface
independently of the desired entropy conclusion, extract an actual Boolean
product from it, and pay the resulting component excess by influence on a
stated critical class.

This run fixes one physical cut `A|B`, the ordinary uniform-cube ratio `R=H/I`,
and the multiplicative rectangle defect

`rho=Pr[f(x,y)f(x',y)f(x,y')f(x',y')=-1]`.

No support-component entropy inequality and no arbitrary spectral law is used.

## New anchoring identity

For every anchor `(x0,y0)` define

`u(x)=f(x,y0)` and `v(y)=f(x0,y)f(x0,y0)`.

The Hamming mismatch indicator of `f` and `uv` at `(x,y)` is exactly the
negative multiplicative rectangle indicator at the four corners
`(x,y),(x,y0),(x0,y),(x0,y0)`. Averaging the anchor and query therefore gives

`E_anchor Pr[f!=uv] = rho`.

Hence some genuine Boolean product has error `epsilon<=rho`. This is an exact
all-dimensional identity and supplies the missing Boolean realizability bridge.

## Controlled component excess

First, every nonconstant Boolean function on `N` bits satisfies the elementary
bound `H/I<=3N`. Let `S` have law `fhat(S)^2` and
`q=Pr[S nonempty]=Var(f)`. Then `I>=q`,
`H<=h2(q)+Nq`, and nonconstancy gives `q>=2^(1-N)`, whence
`h2(q)<=2Nq`.

For `a=|A|` and `0<=rho<=1/16`, define the independent interface budget

`E_{N,a}(rho)=2h2(2sqrt(rho))+(2N-a)2sqrt(rho)+6aN rho`.

If `f` is descendant-critical with ratio `R`, the anchored Boolean factors can
be chosen so that

`R I(u)-H(u) <= E_{N,a}(rho)`.

For nonconstant `u`, equivalently

`(R-R(u)) I(u) <= E_{N,a}(rho)`.

The proof inserts `epsilon<=rho` into the A053 near-tensor inequality and uses
`R<=3N` only for the physical influence-transport term. The symmetric theorem
holds for `v`.

## Explicit influence payment

Let `J=I_A(f)>0`, `0<kappa<=1`, and `t=2sqrt(rho)`. If

`t <= min{kappa^2 J^2/144, kappa J/(6N), sqrt(2kappa J/(9aN))}`,

then

`E_{N,a}(rho)<=kappa J`,

`I(u)>=(1-kappa/(9N))J>=8J/9`, and

`R(u)>=R-9kappa/8`.

The three input inequalities pay the binary-entropy continuity, ambient
alphabet, and influence-transport costs separately. They are expressed in the
truth-table interface and physical block influence, not in the desired factor
ratio. Thus A054 now has a complete paid-interface theorem on a stated class.
Universal admission of such a cut is explicitly not claimed.

## Mandatory counterexample controls

1. The pinned nine-bit indicator has two actual connected support components
   and raw entropy excess greater than `1/5000`. Those components are not
   physical product factors, so the new theorem neither assumes nor implies
   raw component entropy subadditivity.
2. The pinned seven-bit indicator has
   `R(A union B)>max(R(A),R(B))` by more than `0.0028` in natural-log units.
   It fails descendant-criticality: a two-data-coordinate restriction exposes
   OR2/NAND2 with ratio larger by more than `0.59`. Criticality enters the new
   proof at the A053 block inequality, precisely the hypothesis absent from
   that counterexample.

Near tensors, equal-ratio tensor powers, one-point surgery, rare restrictions,
addressing/selectors and prime gates are treated in
`CRITICAL_INTERFACE_PAYMENT.md`. In particular, one-point surgery can make a
tensor prime while leaving `rho` exponentially small; the new result preserves
the A053 conclusion that full ratio criticality rejects a fixed lower-ratio
hidden factor once the physical block influence is nonnegligible. Equal-ratio
critical tensors remain valid controls.

## Exact computation

Command: `python3 verify_rectangle_interface.py`.

The checker exhausts all `65,536` Boolean sign tables on a `4 x 4` product
cube. For each table, exact integer/Fraction arithmetic verifies that the sum
of all sixteen anchored product-error counts equals the full ordered
rectangle-defect count and that the best anchored product error is at most the
defect probability. It passed `131,200` assertions. The finite computation
reproduces the combinatorial identity; the theorem and payment are analytic in
all dimensions.

## Sources actually used

- B11 compact contract blob `faaa0875ddb129d134bb62abb513f3795e88b590`.
- Execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Stream index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- A053 theorem blob `843dc932a9074272b1cf90c3ebbd9ae74ae69559`
  and report source in run
  `20261012T011258Z-account01-B11-a053-neartensor`.
- A052 pruning-scope source in run
  `20261011T231223Z-account01-B11-a052-critical-source`.
- Nine-bit component counterexample blob
  `fc36cb9447b4fc17c5ed49d8c6e98cf59d11f7eb`.
- Seven-bit component-ratio report at commit
  `31c201a0a8caef323c65abe964ff8ed4b702fc81`.

The A053 dependency is itself pending independent review, so the present claim
inherits that review obligation. No literature novelty claim is made.

## Exact remaining obstacle and routing

The first unsupported universal line is:

> Every descendant-critical high-ratio Boolean source admits a nontrivial
> physical cut satisfying the paid-interface smallness criterion.

Nothing here proves that line. A tensor-prime source may have every rectangle
interface too large, while rare-influence cuts may miss the payment threshold.
The next action is to combine the A052 nonnegative critical slack
`Delta_i H-RI_i` over adaptive blocks and test whether it forces either a paid
rectangle cut or a dimension-independent aggregate curvature lower bound.

Route the package to A052, A055, A090, A094, A096 and B20. Independent review
has not been performed. Full FEI remains OPEN.

## Persistence receipts

The eight-file canonical artifact was committed at
`abad9dd09f57a6edb0d01e3b0e89b05004de9b9e`; the complete Brain mirror was
committed at `9b7fb64274893ddc3e910ec65011e957e8c35057`. Every file was fetched by
that exact commit, was nonempty, and matched the complete local source bytes.
These receipts establish durable delivery only. Independent review and native
Brain ingestion are not claimed.

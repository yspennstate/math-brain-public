# Solo FEI continuation: subcube parity multiplexers

## Outcome

Full Friedgut--Kalai Fourier entropy--influence remains **OPEN**. This
continuation proves a positive full FEI theorem for a structured class that
extends ordinary addressing to arbitrary-degree parity labels and
variable-depth selector partitions.

Partition selector space into subcubes `C_j`, assign each cell a distinct data
parity `D_j`, and on each cell set

    f(x,y)=s_j chi_(T_j)(x) chi_(D_j)(y).

Then

    H(f)=2H(J)<=4I_x(f)<=4I(f),

where `J` is the selector-cell label. The constant four is asymptotically sharp
for this class: ordinary addressing on `m` address bits has

    H=2m,  I=m/2+1,  H/I=4m/(m+2) -> 4.

Without the subcube assumption, every arbitrary parity multiplexer

    f(x,y)=sigma(x)chi_(D(x))(y)

still satisfies the aggregate data-erasure bound

    B_y(f)<=H(D)<=2I_x(f).

These are genuine all-dimensional theorems for the stated classes, not a
solution of universal FEI.

All work in this continuation was done by the primary assistant. Subagents,
delegated tasks, other-model calls, commissioned audits and outside contacts:
zero. Actual model and reasoning-level metadata are not exposed and are
therefore **UNVERIFIED**.

The freshly read master head at the start was
`83b2b5ae2126f2d4801c24309b86d5b1ffd3e39f`; the newest prior solo commit was
`5525e75b356bbd78ab6be60e97f4a46f5e18685f`. The current exclusion registry,
latest P03 handoff, README, NEXT_STEPS, signed-balance note and newest report
were read first. The original P03 finite-dimensional metric 6 remains a prior
reported fact only; its exhausted enumeration was not resumed.

## 1. Exact spectral identity

Let selector cell `C_j` have codimension `r_j` and density
`delta_j=2^(-r_j)`. Write

    v_j(x)=1_(C_j)(x)s_j chi_(T_j)(x).

Distinct data parities give the collision-free expansion

    f(x,y)=sum_j v_j(x)chi_(D_j)(y).

Consequently the data part `Y` of the random Fourier subset identifies `j`
and

    Pr[Y=D_j]=sum_S vhat_j(S)^2=delta_j.

The Fourier transform of a codimension-`r_j` subcube indicator is uniform on
`2^(r_j)` coefficients. Multiplication by a character only translates that
support. Therefore

    H(X|Y=D_j)=r_j=log_2(1/delta_j).

Since

    H(Y)=H(J)=sum_j delta_j r_j,

the complete squared-spectrum entropy is exactly

    H(f)=H(Y)+H(X|Y)=2H(J).

## 2. Nonreusing influence payment

Let

    eta_i=Pr_x[J(x)!=J(x flipped at i)].

The cube edge-isoperimetric inequality, summed over partition cells, gives

    H(J)<=sum_i eta_i.

When a selector edge changes cells, it changes between two distinct signed
data characters. Such characters are orthogonal and disagree on exactly half
of the data cube. Thus

    Inf_i(f)>=eta_i/2,
    I_x(f)>=H(J)/2.

Combining this with the exact entropy identity proves `H(f)<=4I_x(f)`.

Unlike the failed coordinate-potential inductions, every selector boundary is
charged once. Unlike a marginal entropy proof, the conditional selector
spectrum inside a cell has exactly its prefix length and no `log n` loss.

## 3. Arbitrary parity-multiplexer erasure

For arbitrary cells, put `v_A=sigma 1_{D=A}`. Their physical supports are
disjoint and Parseval gives

    Pr[Y=A]=Pr[D=A].

Conditioning reduces entropy, and dual total correlation is at most joint
entropy, so

    B_y=sum_l H(Y_l|X,Y_(-l))
       <=sum_l H(Y_l|Y_(-l))<=H(Y)=H(D).

The same partition boundary argument gives `H(D)<=2I_x`. This proves the
broader erasure lemma and strictly extends the earlier result limited to
constant/single-data-bit fibers.

## 4. Exact boundary

The proof does not extend automatically in three directions.

- Repeating a data parity on two cells makes selector Fourier coefficients add
  before squaring, so the data label no longer identifies the cell.
- For arbitrary cells, the normalized Fourier entropy of a signed cell
  indicator is uncontrolled from above; this is a partial-Boolean FEI problem,
  already shown FEI-hard in an earlier continuation.
- Arbitrary Boolean data fibers have overlapping Fourier supports, eliminating
  the collision-free label law.

The next concrete positive route would be a decomposition of general Boolean
functions into nearly nonoverlapping parity-multiplexer pieces with a
single-use boundary charge. No such decomposition is proved.

## 5. Exact checks

Executed from the solo folder:

    python check_subcube_parity_multiplexers.py
    python -m py_compile check_subcube_parity_multiplexers.py

Both returned `PASS`. The checker uses exact rational Walsh coefficients and
influences plus 160-bit outward rational logarithm intervals. It verifies:

- an unequal prefix partition of codimensions `1,2,3,3`;
- four equal codimension-two cells;
- a point partition labeled by all three-bit parities;
- standard three-bit addressing with eight distinct data singletons.

For standard addressing it obtains exactly

    H=6,  I_x=3/2,  I=5/2.

Finite calculations are only self-checks; the universal theorems are proved
algebraically above and have not received an independent audit.

## 6. Literature and novelty limits

Fresh primary-source searches included:

- `site:arxiv.org Fourier entropy influence subcube partition addressing function parity multiplexer`
- `site:arxiv.org "Fourier entropy" addressing function subcube`
- `site:arxiv.org Fourier entropy influence decision tree parity decision tree`
- `site:arxiv.org entropy influence conjecture read-once decision tree addressing`

They did not locate a directly matching theorem. Search failure is not a
novelty proof, so publication novelty remains **UNVERIFIED**. Composition and
decision-tree classes are known FEI territory; the exact identity and class
statement here require comparison with that literature before any novelty
claim.

## 7. Exact remaining obligation

The universal target remains

    K(f)=sum_edges min(p_S,p_T)|log_2(p_S/p_T)|
       <=C sum_S |S|p_S

under the signed Boolean convolution identities. The new theorem shows that
an exact nonoverlapping parity label supplies the missing nonreuse mechanism.
The unresolved step is to obtain comparable collision control for overlapping
higher-degree fibers without reducing to the FEI-hard partial-Boolean class.

## 8. Measured execution

The supplied run start was 2026-09-18T06:00:12Z and the first sampled shell
clock was 06:00:45Z. This report checkpoint is 06:13:00Z: 12 minutes 48 seconds
from supplied start and 12 minutes 15 seconds between sampled shell clocks.
This includes retrieval, derivation, exact checking, literature search and
writing; it is not a claim of continuous model compute. GitHub delivery time
is not included.

Intervals between continuations are not counted as research time. Neither the
schedule nor this report establishes an hour of work or ten continuous hours.

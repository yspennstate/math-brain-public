# C34 v1: first-return obstruction for the copied site-block upper process

Status: proof (unaudited). Kind: route_failure. Target: 2.
Novelty is unassessed. This is a failure of two specified C33 upper
comparisons to have a finite first moment. It gives no recurrence or
transience conclusion for the ordinary frog model. The hardest open piece
remains a summable upper bound for ordinary T4 site-activation probabilities.

## 1. Model and statement

Use precisely the independent copied-block episode process in C33 section 1:
all ordinary motion is retained; an upward entry omits residents on its
ancestral path, and every other resident is allowed once in a fresh copy
for that episode. Entries are unbounded. Every episode stops its frogs at
their first block exit. The global root has degree d; bulk vertices have
degree d+1. There are finitely many boundary-parent categories e, of depths
h_e. No cap on incoming frogs or on returning excursions is introduced.

Let A_T be the mean direct upward exits of a local top-entry episode and
B_T,e its mean direct downward exits in category e. For a bottom-entry
episode in category c use A_c and B_c,e. These are C33's finite, exact site
means. Let D_c,e be the global-root block's direct downward means for a
bottom entry at c. There are no upward exits of that block. Put

    m_*=min_c sum_e D_c,e.

Every root-block episode's seed eventually exits downward, so m_*>=1.
Start x_0=0 and y_c,0=0. Define monotone lower iterations by applying

    F_T(x,y)=A_T+sum_e B_T,e*x*y_e,
    F_c(x,y)=A_c+sum_e B_c,e*x*y_e,                       (1)

and optionally rounding each coordinate DOWN. If some finite iteration
satisfies x_n*m_*>=1, the copied upper process has infinite expected total
root visits from the original finite root start. Consequently no positive
potential contraction satisfying C33's root lower-bound requirement can
certify finite expected root visits for this copied process.

In particular this obstruction applies on ordinary T4 to both tested shapes:
the five-site star and the nine-site prefix block consisting of a top,
all four children and all four children of one selected child.

## 2. Finite return families justify (1)

For this paragraph the parent of a chosen bulk block is absorbing. A top
input has a family of rootward exits; a bottom input at c has such a family
as well. Define finite pruned families recursively. At stage zero keep no
outputs. At stage n+1 keep all direct upward exits of the initial local
episode. For each of its direct downward exits in category e, run the
stage-n top family in that child block. At each of its upward returns,
start a fresh stage-n bottom-e family in the current block and keep those
families' exits to the absorbing parent. Discard all other branches.

This is pruning of the copied process. The first local exit distinguishes
the direct outputs and the outputs assigned to each downward seed, so no
output is counted twice. A returning frog starts its new bottom episode
with fresh future and independent resident copies. Each finite pruned
family has finitely many episodes and outputs: each local episode has at
most 1+|A| offspring and recursive depth is finite. Let its expected output
counts be X_n,Y_c,n.

Condition on the first episode's downward seeds. A child top family has
mean X_n outputs. Conditional on any such output and its past, the new
bottom-e family has mean Y_e,n, independent of that child's used past.
The tower property therefore gives X_n*Y_e,n for this composed branch.
This is a product justified by fresh copies at a stopping boundary; it is
not multiplication of marginal bounds on dependent events. Linearity over
the local seeds gives exactly

    X_(n+1)=F_T(X_n,Y_n),  Y_c,n+1=F_c(X_n,Y_n).

These pruned outputs are all actual outputs of the copied process. All
coefficients in (1) are nonnegative. Thus any coordinatewise downward
rounding applied at each step gives x_n<=X_n and y_c,n<=Y_c,n, inductively.
In particular the copied process can supply a finite pruned top family
whose mean return count is at least x_n. No estimate on an omitted tail
is required: the omitted outputs are nonnegative and only a lower bound
is used for the obstruction.

## 3. Root generations have nondecaying expected size

Fix an iteration n with x_n*m_*>=1. Regard root-block bottom episodes as
individuals of categories c. From such an episode keep its local downward
seeds, run their finite stage-n top return families in the child blocks,
and regard each resulting return as a new root-block bottom episode.
Stop this generation before exploring those new root episodes.
The mean offspring matrix is

    M_c,e=D_c,e*X_n >= D_c,e*x_n.

It has every row sum at least x_n*m_*>=1. Fresh episode copies give this
conditional mean at every generation. Hence the tower property gives
E[Z_(r+1)]>=E[Z_r] for the number Z_r of retained root episodes in generation
r. Starting from any one root episode, E[Z_r]>=1 for every r. Tonelli gives
infinite expected total root episodes. This argument needs no independence
between different offspring counts of one episode.

A root episode at category c has a uniformly positive probability of a
root visit: its input seed can take h_c consecutive parent steps, with
probability at least kappa=(d+1)^(-max_c h_c)>0 (and probability one if
h_c=0). Conditional on the episode's birth, its unused seed future is
ordinary. These seed visits belong to different episode intervals and
are not counted twice. Therefore expected root visits are at least kappa
times expected root episodes, and are infinite.

The original initial upper episode reaches some returning root episode
with positive probability. For example its seed follows a fixed finite
downward path to a child-block entrance and then immediately steps back.
All steps have positive probability; other frogs can be ignored. The new
root episode has a fresh future. The preceding infinite expectation thus
also holds from the original finite root start.

An infinite expectation alone is not almost-sure recurrence, even for this
upper process. Nor does infinite expectation above imply anything about
the ordinary process below it. The stated consequence is only failure of
this finite-first-moment upper comparison. A C33 contraction would give
finite expected root episodes, contradicting the result just proved.

## 4. Exact finite certificates for the two tested T4 shapes

`check_c34_return_means.py` reads the exact rational episode coefficients
from the current source-hashed C33 records. Starting from zero, it floors
each coordinate of (1) to multiples of 10^-12 by integer division. Every
floor is downward and differs from its exact row value by less than
10^-12. Monotonicity, rather than any unproved accumulated-error estimate,
certifies that these are lower bounds for the finite return families.
There is no floating-point arithmetic in this check.

At n=4 the saved records give the following smaller human-readable
certificates; each displayed m_0 is checked below every exact root row sum:

| T4 block | x_4 lower bound | m_0<=m_* | x_4*m_0 |
|---|---|---|---|
| Five-site star | 843518480447/1000000000000 | 119/100 | 100378699173193/100000000000000 > 1 |
| Nine-site one-expanded-child block | 216299500219/250000000000 | 121/100 | 26172239526499/25000000000000 > 1 |

The full iteration histories, exact (possibly larger) m_* values, original
coefficient-file hashes and source-code hashes are in
`C34_RETURN_LOWER_RESULTS.json`. `save_c34.py` independently checks the
displayed small products and each m_0 against those coefficient records.
Its `C34_SMALL_WITNESSES.json` is an exact small witness file, not an
independent audit of the probabilistic model.

Controls: an independently written analytic one-site T4 row triggers the
crossing test. The live one-site T6 rows have the exact fixed point
F(1/2,1/4)=(1/2,1/4); their downward iterations remain at most that point
and do not trigger a failure. All three intended live coefficient files
must be read or the check refuses. C33's coefficients themselves were
checked against an independent star Markov queue and exact linear-system
residuals. These controls do not substitute for the pending independent
review of C33/C34.

This closes the tested five- and nine-site copied upper comparisons for
finite-mean transience. It does not close larger block shapes, comparisons
that persist more visited-site information between returns, or the
ordinary T4 problem. The next model must change that memory mechanism;
another weight search on these same two copied processes cannot work.

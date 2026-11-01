# Aldous and Fill, Open Problem 4.45: lumping a reversible chain can increase its stopping-rule mixing time

14 September 2026. Ledger row P0242 (Codex campaign). Source: Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs*, Section 4.6.1, Open Problem 4.45, PDF page 149 of the 2014 recompilation.

## The question

For a reversible chain with generator $Q$ and stationary law $\pi$ and a map $f$ from the state space onto a smaller set, the *induced chain* (the stationary-flow lumping, equations (4.39)-(4.40) of the source) has state space $f(I)$, stationary law $\hat\pi(a) = \sum_{i \in a}\pi_i$ and rates
$$\hat q(a, b) = \frac{\sum_{i \in a}\sum_{j \in b}\pi_i q_{ij}}{\hat\pi(a)}, \qquad a \ne b,$$
so that stationary flow rates between blocks are preserved. Proposition 4.44 (the contraction principle) shows that $\tau^*, \tau_0, \tau_2, \tau_c$ can only decrease under this operation, and the text notes that one-sided mean hitting times can increase. The behaviour of the $\tau_1$ family is called unclear, and:

> **Open Problem 4.45.** Is the value of $\tau_1^{(2)}$ in an induced chain bounded by $K$ times the value of $\tau_1^{(2)}$ in the original chain, for some absolute constant $K$? For $K = 1$?

Here $\tau_1^{(2)} = \max_i \min_U \mathbb{E}_iU$ over stopping times $U$ with $\mathbb{P}_i(X_U \in \cdot) = \pi$; by the halting-state theorem of Lovász and Winkler, $\tau_1^{(2)} = \max_{i,j}(\mathbb{E}_iT_j - \mathbb{E}_\pi T_j) = \max_{i,j}(-Z_{ij}/\pi_j)$ with $Z = (\Pi - Q)^{-1} - \Pi$ the fundamental matrix.

Answer to the second question: no. $K = 1$ fails on a four-state chain lumped to three states. The first question is not settled here.

## The example

Take the reversible chain on $\{0, 1, 2, 3\}$ with symmetric weights $W_{02} = 1$, $W_{12} = 1$, $W_{13} = 109$, $W_{23} = 54$, holding weights $W_{11} = 117$, $W_{33} = 10000$, and rates $q_{ij} = W_{ij}/w_i$ with $w_i = \sum_j W_{ij}$ (the holding weight enters $w_i$ only, so it sets $\pi_i \propto w_i$ without moving the chain). Explicitly $w = (1, 227, 56, 10163)$,
$$\pi = \tfrac{1}{10447}(1, 227, 56, 10163), \qquad q_{02} = 1,\ q_{12} = \tfrac{1}{227},\ q_{13} = \tfrac{109}{227},\ q_{20} = \tfrac{1}{56},\ q_{21} = \tfrac{1}{56},\ q_{23} = \tfrac{54}{56},\ q_{31} = \tfrac{109}{10163},\ q_{32} = \tfrac{54}{10163}.$$
So state $3$ is a heavy, sticky state ($\pi_3 = 0.973$), state $1$ is a light state attached mainly to $3$, state $2$ is a light state attached mainly to $3$ and weakly to $1$, and state $0$ is a leaf hanging from $2$ with $\pi_0 = 1/10447$.

Lump $2$ and $3$ into one block $A$ and keep $0$ and $1$. The induced chain has $\hat\pi = \tfrac{1}{10447}(1, 227, 10219)$ and rates
$$\hat q(0, A) = 1, \qquad \hat q(1, A) = \tfrac{110}{227}, \qquad \hat q(A, 0) = \tfrac{1}{10219}, \qquad \hat q(A, 1) = \tfrac{10}{929}.$$

Exact rational arithmetic (`af445_exact.py`, sympy over $\mathbb{Q}$) gives
$$\tau_1^{(2)}(\text{original}) = \frac{149731115}{63193903} = 2.36939\ldots, \qquad \tau_1^{(2)}(\text{induced}) = \frac{346900}{114917} = 3.01870\ldots,$$
both attained at the pair $(i, j) = (1, 0)$, i.e. by $\mathbb{E}_1T_0 - \mathbb{E}_\pi T_0$ and its lumped analogue. The ratio is $419679620/329408453 = 1.27404\ldots > 1$. A second witness with finer weights ($W_{02} = 10$, $W_{12} = 12$, $W_{11} = 1174$, $W_{13} = 1087$, $W_{23} = 539$, $W_{33} = 10^5$, same lumping) has ratio $1.48220\ldots$, and the random search that produced these (2,500 chains on three to six states with every partition, then Nelder-Mead in the four-state case) found nothing above $1.483$; on three-state chains the best ratio found was exactly $1$.

What lumping does here: in the original chain, a walk started at $1$ reaches the leaf $0$ by first stepping to $2$ (rate $1/227$) and then to $0$ (rate $1/56$), and while at $2$ it is well placed; in the induced chain the block $A$ forgets whether the walk sits at $2$ or at $3$, so from $A$ the leaf is reached at the averaged rate $1/10219$, which is essentially $3$'s rate, and the walk from $1$ loses the advantage of entering $A$ at $2$. Both $\mathbb{E}_1T_0$ and $\mathbb{E}_\pi T_0$ change, but the difference grows.

## Status

The $K = 1$ half of Open Problem 4.45 is answered in the negative with an exact rational certificate. The $K$ half remains open: the two constructions above stay below $1.5$, and I have no argument in either direction. A universal $K$ would follow from a bound $\tau_1^{(2)} \le C\tau_0$ together with Proposition 4.44 only if also $\tau_0 \le C'\tau_1^{(2)}$, and that fails (the complete graph has $\tau_0 \approx n$ against $\tau_1^{(2)} \approx 1$), so the question is genuinely about how the stopping-rule mixing time behaves under shorting. Author checked, exact arithmetic, no independent read; the online edition of the book carries the problem without a note (fetched 14 September 2026).

"""Build short.tex: the preamble of paper.tex without author data, the short front matter, Sections 2-7 of paper.tex
verbatim (with the Section 7 title changed), the short closing remarks and the bibliography."""
import os

W = r"~\qform_five_directions"
S = os.path.join(W, "short")
lines = open(os.path.join(W, "paper.tex"), encoding="utf-8").read().split("\n")


def L(a, b):
    """1-based inclusive line range."""
    return lines[a - 1:b]


pre = L(1, 34)
assert pre[7].startswith("\\hypersetup{pdftitle="), pre[7]
pre[7] = "\\hypersetup{pdftitle={Quadratic forms with five large singular values have bounded densities}}"
assert lines[102].startswith("\\section{Preliminaries}"), lines[102]
assert lines[663].strip() == "\\end{proof}" and "Proof of Theorem~\\ref{thm:main}" in lines[642], (lines[642], lines[663])
body = L(103, 664)
old_title = "\\section{Proofs of Theorems~\\ref{thm:main} and~\\ref{thm:half}}\\label{sec:proof}"
assert body.count(old_title) == 1
body[body.index(old_title)] = "\\section{Proof of Theorem~\\ref{thm:main}}\\label{sec:proof}"
assert lines[686].startswith("\\begin{thebibliography}"), lines[686]
bib = L(687, 713)
assert bib[-1].strip() == "\\end{document}", bib[-1]
body_text = "\n".join(body)
KERNEL_EDITS = [
    (r"""and for every $a\in\R$,
\begin{equation}\label{eq:logkernel}
\int_{-1}^1\abs x^{-1/2}\logp\frac1{\abs{x-a}}\dd x\le8 .
\end{equation}
\end{lemma}""",
     r"""and if $g,h:\R\to[0,\infty]$ are even and nonincreasing on $[0,\infty)$, then for every $b\in\R$
\begin{equation}\label{eq:rearrange}
\int_\R g(y)h(y-b)\dd y\le\int_\R g(y)h(y)\dd y .
\end{equation}
\end{lemma}"""),
    (r"""For \eqref{eq:logkernel}, write both nonnegative factors as integrals of the indicators of their superlevel sets, which are intervals centred at $0$ and at $a$ respectively. The length of the intersection of two intervals is at most the length of the shorter one, with equality when they have the same centre, so by Tonelli's theorem the integral is largest at $a=0$, where it equals $2\int_0^1x^{-1/2}\log(1/x)\dd x=8$.""",
     r"""For \eqref{eq:rearrange}, write $g(y)=\int_0^\infty\1\{g(y)>\sigma\}\dd\sigma$ and $h(y)=\int_0^\infty\1\{h(y)>\tau\}\dd\tau$. For $\sigma,\tau\ge0$ the sets $\{g>\sigma\}$ and $\{h>\tau\}$ are intervals centred at $0$, possibly empty or all of $\R$, and $\{y:h(y-b)>\tau\}$ is the translate of the second by $b$. The length of the intersection of two intervals is at most the length of the shorter one, with equality when they have the same centre. Hence $\abs{\{g>\sigma\}\cap(b+\{h>\tau\})}\le\abs{\{g>\sigma\}\cap\{h>\tau\}}$, and integrating over $\sigma$ and $\tau$ with Tonelli's theorem gives \eqref{eq:rearrange}."""),
    (r"""The inequality is the rearrangement argument from the proof of Lemma~\ref{lem:kernels}: the superlevel sets of $h$ and of $\abs{y-b}^{-1/2}\1\{\abs{y-b}\le\delta\}$ are intervals centred at $0$ and at $b$, or the whole line. Hence""",
     r"""The inequality is \eqref{eq:rearrange}, applied to $h$ and to $y\mapsto\abs y^{-1/2}\1\{\abs y\le\delta\}$, both even and nonincreasing on $[0,\infty)$. Hence"""),
]
for old, new in KERNEL_EDITS:
    assert body_text.count(old) == 1, old[:60]
    body_text = body_text.replace(old, new)
body = body_text.split("\n")
front = open(os.path.join(S, "front_short.tex"), encoding="utf-8").read().rstrip("\n").split("\n")
back = open(os.path.join(S, "back_short.tex"), encoding="utf-8").read().rstrip("\n").split("\n")
out = pre + front + [""] + body + back + [""] + bib + [""]
text = "\n".join(out)
for bad in ("Shmalo", "Yitzchak", "Hebrew University", "gmail", "thm:half", "rem:four", "rem:three"):
    assert bad not in text, bad
open(os.path.join(S, "short.tex"), "w", encoding="utf-8", newline="\n").write(text)
print("short.tex", len(out), "lines")

"""Self-test of the 120 readability rules (pw1k_readable.READ, 28 Nov 2026).

BASE is pw1k_readable_base.tex, a 1,000-word paper written to the rules: every one of the 120 must be silent on it. Each rule
then gets its own broken copy of BASE (MUT[cid]: a list of (old, new) replacements, every old string must occur in BASE) and
must fire on it. The matrix of which rules fire on which copy is printed with --matrix; two rules that fire on exactly the
same copies are reported, since they may be one check under two wordings.

    python pw1k_readable_selftest.py            # pass/fail summary, exit 1 on a failure
    python pw1k_readable_selftest.py --matrix   # also the fire matrix
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

INTRO_END = "the table at the end."
PROOF_END = "This proves Theorem~\\ref{thm:main}.\n\\end{proof}"
LEMMA_PROOF = "In both cases the gap stays at most $m$, which is what the lemma claims.\n\\end{proof}"
PRELIM_OPEN = "This section fixes the language of splits and gives a small example of each notion."
CONCL = "Second, how often does the greedy rule find the best split when the numbers are chosen at random?"
DEF_SPLIT = "A \\emph{split} of a finite set $A$ is a pair $(B,C)$ of disjoint sets whose union is $A$."
BIB_END = "\\end{thebibliography}"
ABS = ("We prove that every finite set of real numbers can be split into two halves whose sums differ by at most the largest\n"
       "element, and we show that this bound cannot be improved in general.")
NOTA_SEC = "\\appendix\n\\section{Table of symbols}\\label{app:notation}"
NOTA_BLOCK = NOTA_SEC + """

\\begin{tabular}{lll}
Symbol & Meaning & Where defined \\\\
$A$ & a finite set of positive real numbers & Theorem~\\ref{thm:main} \\\\
$(B,C)$ & a split of $A$ & Definition~\\ref{def:split} \\\\
$\\max A$ & the largest element of $A$ & Theorem~\\ref{thm:main} \\\\
$m$ & a bound on the gap & Lemma~\\ref{lem:step} \\\\
$\\mathbb{N}$ & the positive integers & Section~\\ref{sec:prelim} \\\\
\\end{tabular}
"""
THM = ("\\begin{theorem}\\label{thm:main}\nFor every finite set $A$ of positive real numbers there is a split of $A$ into two "
       "parts whose sums differ by at most\n$\\max A$.\n\\end{theorem}")
IN_WORDS = "In words, no number has to be cut in half: the error of the best split is never more than one element."
PTR = "The theorem is proved in Section~\\ref{sec:proof}."
WORDS40 = " ".join(["the greedy rule keeps the two sums close together"] * 6)

MUT = {
    "C01": [(NOTA_BLOCK, ""), (CONCL, CONCL + "\n\n" + NOTA_BLOCK.replace("\\appendix\n", "") + "\n\\section{Further remarks}\nThis section adds remarks on the proof that a reader may skip without loss.\n")],
    "C01a": [(NOTA_BLOCK, ""), ("\\section{Preliminaries}", NOTA_BLOCK.replace("\\appendix\n", "") + "\n\\section{Preliminaries}")],
    "C01b": [("and every\nsymbol of the paper is listed in Appendix~\\ref{app:notation}, the table at the end.", "and the paper ends with\nthe usual remarks.")],
    "C01c": [("\\section{Table of symbols}\\label{app:notation}", "\\section{Table of symbols}"), ("Appendix~\\ref{app:notation}", "the appendix")],
    "C01d": [("\\section{Preliminaries}\\label{sec:prelim}", "\\section{Notation}\\label{sec:nota0}\n\\begin{tabular}{ll}\nSymbol & Meaning \\\\\n$A$ & a set \\\\\n\\end{tabular}\n\n\\section{Preliminaries}\\label{sec:prelim}")],
    "C01e": [("Symbol & Meaning & Where defined \\\\\n", "")],
    "C02": [(DEF_SPLIT, "A split of a finite set $A$ is a pair $(B,C)$ of disjoint sets whose union is $A$.")],
    "C02a": [(INTRO_END, INTRO_END + " A set with no exact split is called unbalanced in what follows.")],
    "C02b": [(INTRO_END, INTRO_END + " We use the usual notation for sums.")],
    "C02c": [(INTRO_END, INTRO_END + " We use well-known facts about sums.")],
    "C02d": [(INTRO_END, INTRO_END + " The reader is assumed to be familiar with sums.")],
    "C02e": [(INTRO_END, INTRO_END + " Here balance is meant in the sense of Graham and nothing more.")],
    "C03": [("Start with two empty sides,", "We call a side light if its sum is smaller. Start with two empty sides,")],
    "C03a": [("\\begin{definition}\\label{def:gap}", "\\begin{definition}")],
    "C03b": [(INTRO_END, INTRO_END + "\\footnote{A set with no exact split is called unbalanced.}")],
    "C03c": [(PRELIM_OPEN, PRELIM_OPEN + "\n\n\\begin{remark}\nA set with no exact split is called \\emph{unbalanced}.\n\\end{remark}")],
    "C03d": [("Each step adds a number", "With the definition above, each step adds a number")],
    "C03e": [("Start with two empty sides,", "Recall that a split is a pair of sets. Start with two empty sides,")],
    "C04": [("Start with two empty sides,", "Start with\n\\[ s_0=0 \\]\n\\[ t_0=0 \\]\n\\[ g_0=0 \\]\n\\[ h_0=0 \\]\ntwo empty sides,")],
    "C04a": [("Write $s\\le t$ for", "\\begin{align*}\nx&=a+b\\\\&=c+d\\\\&=e+f\\\\&=g+h\\\\&=i+j\\\\&=k+l\n\\end{align*}\nWrite $s\\le t$ for")],
    "C04b": [("When every element has been placed,", "After some algebra, when every element has been placed,")],
    "C04c": [("When every element has been placed,", "One easily checks that when every element has been placed,")],
    "C04d": [(LEMMA_PROOF, LEMMA_PROOF + "\n\n\\begin{lemma}\\label{lem:two}\nThe gap is never negative.\n\\end{lemma}\n\\begin{proof}\n\\[ |s-t|\\ge 0. \\]\n\\end{proof}")],
    "C04e": [("When every element has been placed,", "Combining these estimates, when every element has been placed,")],
    "C05": [("Write $s\\le t$ for", "We have $a\\le b\\le c\\le d\\le e$. Write $s\\le t$ for")],
    "C05a": [("Each step adds a number $a\\le \\max A$, so Lemma~\\ref{lem:step} applies", "Each step adds a number $a\\le \\max A$, so by Lemma it applies")],
    "C05b": [(LEMMA_PROOF, LEMMA_PROOF + "\n\n\\begin{lemma}\\label{lem:two}\nThe same holds with the larger side.\n\\end{lemma}\n\\begin{proof}\nSimilarly.\n\\end{proof}")],
    "C05c": [("Start with two empty sides,", "Clearly we start. Obviously this works. Trivially it ends. Start with two empty sides,")],
    "C05d": [("When every element has been placed,", "The rest is similar. When every element has been placed,")],
    "C05e": [("Start with two empty sides,", "It suffices to show the gap stays small. Start with two empty sides,")],
    "C06": [("Graham~\\cite{graham} gave", "Graham gave"), ("Spencer~\\cite{spencer} studied", "Spencer studied"), ("bound of Graham~\\cite{graham}", "bound of Graham")],
    "C06a": [(INTRO_END, INTRO_END + " The Hilbert problem is a different matter.")],
    "C06b": [(INTRO_END, INTRO_END + " The question was first posed by a referee long ago.")],
    "C06c": [(INTRO_END, INTRO_END + " It is known that sums behave well.")],
    "C06d": [(INTRO_END, INTRO_END + " A weaker form was found in 1971 by other means.")],
    "C06e": [(INTRO_END, INTRO_END + " The best known bound was weaker.")],
    "C07": [(INTRO_END, INTRO_END + " See also \\cite{nowhere}.")],
    "C07a": [(BIB_END, "\\bibitem{unused} A. Person, An unused paper, J. Nowhere 1 (2000), 1--2.\n" + BIB_END)],
    "C07b": [(BIB_END, "\\bibitem{graham2} R. L. Graham, Bounds on multiprocessing timing anomalies, SIAM J. Appl. Math. 17 (1969), 416--429.\n" + BIB_END), (INTRO_END, INTRO_END + " See \\cite{graham2}.")],
    "C07c": [(BIB_END, "\\bibitem{arx} A. Person, A preprint, arXiv preprint, 2020.\n" + BIB_END), (INTRO_END, INTRO_END + " See \\cite{arx}.")],
    "C07d": [(BIB_END, "\\bibitem{toap} A. Person, A paper, to appear.\n" + BIB_END), (INTRO_END, INTRO_END + " See \\cite{toap}.")],
    "C07e": [("\\bibitem{spencer} J. Spencer,", "\\bibitem{spencer} J. Spencer et al.,")],
    "C08": [(IN_WORDS, "")],
    "C08a": [(IN_WORDS, ""), ("The idea behind everything below is simple: put", "Put")],
    "C08b": [(INTRO_END, INTRO_END + " The rule (which is old (and simple) in every account) is fast.")],
    "C08c": [(INTRO_END, INTRO_END + " The rule is " + " ".join(["fast and simple and old"] * 20) + ".")],
    "C08d": [(INTRO_END, INTRO_END + " A and B are one and two respectively. C and D are three and four respectively. E and F are five and six respectively. G and H are seven and eight respectively.")],
    "C08e": [(INTRO_END, INTRO_END + " Such sets are not uncommon.")],
    "C09": [("\\begin{example}\\label{ex:split}\nThe set $\\{1,2,3\\}$ has the split $(\\{1,2\\},\\{3\\})$, whose two sums are both equal to three.\n\\end{example}\n", ""), ("\\begin{example}\\label{ex:gap}\nThe split $(\\{1\\},\\{1,1\\})$ of the set $\\{1,1,1\\}$ has gap one, since its two sums are one and two.\n\\end{example}\n", "")],
    "C09a": [("\\begin{example}\\label{ex:split}\nThe set $\\{1,2,3\\}$ has the split $(\\{1,2\\},\\{3\\})$, whose two sums are both equal to three.\n\\end{example}\n", ""), ("\\begin{example}\\label{ex:gap}\nThe split $(\\{1\\},\\{1,1\\})$ of the set $\\{1,1,1\\}$ has gap one, since its two sums are one and two.\n\\end{example}\n", ""), ("For example, the\nset", "The\nset")],
    "C09b": [("For example, the\nset $\\{1,1,1\\}$ cannot be split into equal sums, and the best split differs by exactly $1$, which is the largest element,\nso the bound of Theorem~\\ref{thm:main} is attained.", "")],
    "C09c": [("\\begin{figure}\n\\centering\n\\fbox{greedy rule on the set of three ones}\n\\caption{The greedy rule places each element on the side whose sum is smaller at that moment.}\\label{fig:greedy}\n\\end{figure}\n", ""), ("Figure~\\ref{fig:greedy} shows the rule at work on a small set.", "The rule acts on a graph whose vertices are the elements."), (INTRO_END, INTRO_END + " The sets are drawn as vertices of a graph with edges, a tree, a polygon in the plane.")],
    "C09d": [("The hypothesis that the numbers are positive is needed for the rule as stated: with the numbers $5$ and $-5$ the lighter\nside changes meaning, and the example in the introduction shows that the bound itself cannot be lowered.", "")],
    "C09e": [(DEF_SPLIT, DEF_SPLIT + " A split is \\emph{fair} if (i) both parts are nonempty, (ii) the sums differ by at most one, and (iii) the parts have equal size.")],
    "C10": [(PRELIM_OPEN, "$x=1$. " + PRELIM_OPEN)],
    "C10a": [(PRELIM_OPEN, PRELIM_OPEN + "\n\n\\subsection{Splits}\n\\begin{definition}\\label{def:z}\nA \\emph{zero} split has gap zero.\n\\end{definition}\nThe set $\\{1,1\\}$ has a zero split, since both parts have sum one, and this is the only kind of set of size two with one.")],
    "C10b": [(PRELIM_OPEN, ""), ("\\section{Preliminaries}\\label{sec:prelim}\n", "\\section{Preliminaries}\\label{sec:prelim}\n\\subsection{Words}\n")],
    "C10c": [("whose gap is at most $\\max A$. This proves Theorem~\\ref{thm:main}.", "whose gap is at most $\\max A$, " + WORDS40 + ", " + WORDS40 + ", " + WORDS40 + " and " + WORDS40 + ".")],
    "C10d": [("\\section{Conclusion}\\label{sec:conclusion}", "\\section{Two sides}\\label{sec:conclusion}")],
    "C10e": [(PRELIM_OPEN, PRELIM_OPEN + "\n\n\\subsection{Sums}\nA sum is a number.\n\n\\subsection{Sets}\nThis subsection says what a set is, in the plain sense of a collection of numbers in which no number is listed twice and order does not matter at all.")],
    "C11": [("We prove that the greedy rule always gives a split", "The greedy rule always gives a split")],
    "C11a": [("our bound is new in that it concerns their\ndifference and holds for every set, not only for large ones.", "our bound concerns their\ndifference and holds for every set.")],
    "C11b": [(PTR, "")],
    "C11c": [(INTRO_END, INTRO_END + " The proof of the main theorem is short.")],
    "C11d": [("Two\nquestions remain open. First, does the same bound hold for vectors in the plane, with the largest length in place of the\nlargest element? Second, how often does the greedy rule find the best split when the numbers are chosen at random?", "That is all.")],
    "C11e": [(INTRO_END, INTRO_END + " The question is very interesting.")],
    "C12": [],
    "C12a": [(INTRO_END, INTRO_END + " By abuse of notation we write $A$ for its sum.")],
    "C12b": [(INTRO_END, INTRO_END + " We reuse the letter $A$ for its sum.")],
    "C12c": [(INTRO_END, INTRO_END + " A constant $c$ is to be chosen later.")],
    "C12d": [(INTRO_END, INTRO_END + " Constants may change from line to line.")],
    "C12e": [("Write $s\\le t$ for", "\\[ F = s+t+u+v+w \\]\nwhere $s$ is one sum, $t$ the other, $u$ a third, $v$ a fourth and $w$ a fifth. Write $s\\le t$ for")],
    "C13": [],
    "C13a": [("Throughout, $\\mathbb{N}=\\{1,2,3,\\dots\\}$\ndenotes the positive integers, so the natural numbers start at one.", "We use $n\\in\\mathbb{N}$ freely.")],
    "C13b": [("Write $s\\le t$ for", "Note $\\log 2<\\ln 3$. Write $s\\le t$ for")],
    "C13c": [("Write $s\\le t$ for", "Then $s\\lesssim t$. Write $s\\le t$ for")],
    "C13d": [("Write $s\\le t$ for", "Here $B\\subset A$ and $C\\subseteq A$. Write $s\\le t$ for")],
    "C13e": [("Write $s\\le t$ for", "Fix $\\epsilon>0$ and $\\varepsilon<1$. Write $s\\le t$ for")],
    "C14": [],
    "C14a": [],
    "C14b": [(LEMMA_PROOF, "\\begin{proof}\nInner.\n\\end{proof}\n" + LEMMA_PROOF)],
    "C14c": [],
    "C14d": [("This proves Theorem~\\ref{thm:main}.", "This completes the proof of the lemma.")],
    "C14e": [("In both cases the gap", "Case 1: $a=1$. Case 2: $a=2$. Case 3: $a=3$. Case 4: $a=4$. In all cases the gap")],
    "C15": [(ABS, "Let $A$ be a finite set of real numbers. We prove that it can be split into two halves whose sums differ by at most the largest\nelement, and we show that this bound cannot be improved in general.")],
    "C15a": [(ABS + " The proof is a greedy argument, and the paper ends\nwith two open questions about the same problem for vectors in the plane.", "We prove a bound on splits.")],
    "C15b": [(ABS, ABS.replace("in general.", "in general, " + " ".join(["for sets of every size and shape"] * 4) + "."))],
    "C15c": [(ABS, "Every finite set of real numbers can be split into two halves whose sums differ by at most the largest\nelement, and this bound cannot be improved in general.")],
    "C15d": [(ABS, ABS + " The bound is Theorem 1.1.")],
    "C15e": [(ABS, ABS + " This perhaps extends to vectors.")],
    "C16": [("\\section{Preliminaries}", "\\section{Auxiliary results}"), ("\\section{Proof of the splitting bound}", "\\section{Proofs}")],
    "C16a": [("\\section{Introduction}\\label{sec:intro}", "\\section{Setting}\\label{sec:intro}")],
    "C16b": [("\\section{Preliminaries}", "\\section{PRELIMINARIES}")],
    "C16c": [("\\section{Preliminaries}", "\\section{preliminaries}")],
    "C16d": [("\\section{Table of symbols}", "\\section{Appendix}")],
    "C16e": [("\\section{Preliminaries}", "\\section{Preliminaries on GSP}")],
    "C17": [],
    "C17a": [("\\caption{The greedy rule places", "\\caption{See the text. The greedy rule places")],
    "C17b": [("\\caption{The greedy rule places each element on the side whose sum is smaller at that moment.}", "\\caption{$s_k+a_k\\le t_k$, $|s-t|\\le m$, $a\\le \\max A$.}")],
    "C17c": [("\\begin{tabular}{lll}", "\\begin{tabular}{lllllllll}")],
    "C17d": [("$m$ & a bound on the gap & Lemma~\\ref{lem:step} \\\\", "$m$ & 0.12345678 & 0.98765432 \\\\")],
    "C17e": [("\\caption{The greedy rule", "\\caption{the greedy rule")],
    "C18": [],
    "C18a": [],
    "C18b": [("so Lemma~\\ref{lem:step} applies", "so by \\ref{lem:step} it applies")],
    "C18c": [(INTRO_END, INTRO_END + " Later in the paper we return to this.")],
    "C18d": [],
    "C18e": [],
    "C19": [(INTRO_END, INTRO_END + " Note that a. " * 8)],
    "C19a": [(INTRO_END, INTRO_END + " We have that a. " * 5)],
    "C19b": [(INTRO_END, INTRO_END + " It is very fast, quite old, rather simple, fairly short, extremely clear and highly useful.")],
    "C19c": [(INTRO_END, INTRO_END + " This is one. This is two. This is three. This is four.")],
    "C19d": [(INTRO_END, INTRO_END + " The fact that a. The fact that b. The fact that c. The fact that d.")],
    "C19e": [(INTRO_END, INTRO_END + " One and/or two.")],
    "C20": [],
    "C20a": [("\\begin{lemma}\\label{lem:step}", "\\begin{lemma}[Hall's theorem]\\label{lem:hall}\nEvery set has a split.\n\\end{lemma}\n\\begin{lemma}\\label{lem:step}")],
    "C20b": [("\\begin{lemma}\\label{lem:step}\nSuppose", "\\begin{lemma}\\label{lem:step}\n$m>0$. Suppose")],
    "C20c": [],
    "C20d": [("\\begin{lemma}\\label{lem:step}\nSuppose", "\\begin{lemma}\\label{lem:step}\nWe have a split. Suppose")],
    "C20e": [("\\begin{lemma}\\label{lem:step}\nSuppose", "\\begin{lemma}\\label{lem:step}\n\\begin{enumerate}\n\\item one\n\\item two\n\\item three\n\\item four\n\\item five\n\\end{enumerate}\nSuppose")],
}

# second pass: fixtures written against each detector's own conditions (read from its source, 28 Nov)
LEMMA_STEP = "\\begin{lemma}\\label{lem:step}\nSuppose"
PROOF_HDR = "\\begin{proof}[Proof of Theorem~\\ref{thm:main}]"
SEC_PROVES = "This section proves Theorem~\\ref{thm:main} by following the greedy rule"
EX_SPLIT = "\\begin{example}\\label{ex:split}\nThe set $\\{1,2,3\\}$ has the split $(\\{1,2\\},\\{3\\})$, whose two sums are both equal to three.\n\\end{example}\n"
EX_GAP = "\\begin{example}\\label{ex:gap}\nThe split $(\\{1\\},\\{1,1\\})$ of the set $\\{1,1,1\\}$ has gap one, since its two sums are one and two.\n\\end{example}\n"
FOR_EX = ("For example, the\nset $\\{1,1,1\\}$ cannot be split into equal sums, and the best split differs by exactly $1$, which is the largest element,\n"
          "so the bound of Theorem~\\ref{thm:main} is attained.")
HYP = ("The hypothesis that the numbers are positive is needed for the rule as stated: with the numbers $5$ and $-5$ the lighter\n"
       "side changes meaning, and the example in the introduction shows that the bound itself cannot be lowered.")
CORS = "".join("\n\\begin{corollary}\\label{cor:%s}\nEvery set of %s positive numbers has a split with gap at most its largest element.\n\\end{corollary}\n"
               % (k, k) for k in ("two", "three", "four"))
SYMS = "$\\alpha,\\beta,\\gamma,\\delta,\\eta,\\theta,\\iota,\\kappa,\\lambda,\\mu,\\nu,\\xi,\\rho,\\sigma,\\tau,\\phi$"
END_CONC = "largest element? Second, how often does the greedy rule find the best split when the numbers are chosen at random?"
MUT.update({
    "C01": [(NOTA_BLOCK, NOTA_BLOCK + "\n\\section{Further remarks}\nThis section adds remarks on the proof that a reader may skip.\n")],
    "C03a": [("\\begin{definition}\\label{def:gap}", "\\begin{definition}"),
             (EX_GAP, EX_GAP + "\n\\begin{definition}\nA split is \\emph{even} if its gap is zero.\n\\end{definition}\n")],
    "C03d": [("The idea behind everything below", "By the above definition the gap of the empty split is zero. The idea behind everything below")],
    # 'Where defined' in the table header is a justification word within 300 chars of an align placed last
    "C04a": [(END_CONC, END_CONC + "\n\\begin{align}\nx&=a+b\\\\&=c+d\\\\&=e+f\\\\&=g+h\\\\&=i+j\\\\&=k+l\n\\end{align}\n"),
             ("Where defined", "Defined in")],
    "C04d": [(LEMMA_PROOF, LEMMA_PROOF + "\n\n\\begin{lemma}\\label{lem:two}\nThe gap is never negative.\n\\end{lemma}\n\\begin{proof}\n"
              "\\[ |s-t| = \\max(s,t)-\\min(s,t) \\ge \\max(s,t)-\\max(s,t) + (\\max(s,t)-\\min(s,t)) \\]\n"
              "\\[ \\max(s,t)-\\min(s,t) \\ge 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 \\]\n"
              "\\[ \\max(s,t)-\\min(s,t) = (\\max(s,t)-\\min(s,t)) + (\\min(s,t)-\\min(s,t)) + (\\max(s,t)-\\max(s,t)) \\ge 0 + 0 + 0 + 0 \\]\n\\end{proof}")],
    "C05": [(END_CONC, END_CONC + "\n\\begin{align}\nx &\\le y\\\\\n &\\le z\\\\\n &\\le w\n\\end{align}\n"), ("Where defined", "Defined in")],
    "C06": [("Graham~\\cite{graham} gave", "Graham gave"), ("Spencer~\\cite{spencer} studied", "Spencer studied"),
            ("bound of Graham~\\cite{graham}", "bound of Graham"),
            (BIB_END, "\\bibitem{e1} A. One, A paper, J. One 1 (2001), 1--2.\n\\bibitem{e2} B. Two, A paper, J. Two 2 (2002), 3--4.\n" + BIB_END),
            (END_CONC, END_CONC + " Both are touched on in \\cite{e1,e2,graham,spencer}.")],
    "C07b": [("\\bibitem{graham} R. L. Graham, Bounds on multiprocessing timing anomalies,", "\\bibitem{graham} R. L. Graham, \\emph{Bounds on multiprocessing timing anomalies},"),
             (BIB_END, "\\bibitem{graham2} R. L. Graham, \\emph{Bounds on multiprocessing timing anomalies}, SIAM J. Appl. Math. 17 (1969), 416--429.\n" + BIB_END),
             (INTRO_END, INTRO_END + " See \\cite{graham2}.")],
    "C08": [(IN_WORDS, ""), ("We prove that the greedy rule always gives a split whose two sums differ by at most the\nlargest number in the set.", ""),
            ("simple rule that is never far", "simple rule never far")],
    "C08a": [(IN_WORDS, ""), ("The idea behind everything below is simple: put", "Put"),
             (LEMMA_PROOF, LEMMA_PROOF + "\n\n\\begin{lemma}\\label{lem:two}\nThe gap is never negative.\n\\end{lemma}\n")],
    "C09b": [(FOR_EX, ""), (PRELIM_OPEN, "This section fixes the language of splits."), (EX_SPLIT, ""), (EX_GAP, ""), (HYP, ""),
             (END_CONC, END_CONC + " " + " ".join([WORDS40 + "."] * 3))],  # back over the 600-word guard
    "C09c": [("\\begin{figure}\n\\centering\n\\fbox{greedy rule on the set of three ones}\n\\caption{The greedy rule places each element on the side whose sum is smaller at that moment.}\\label{fig:greedy}\n\\end{figure}\n", ""),
             ("Figure~\\ref{fig:greedy} shows the rule at work on a small set.", "The rule acts on " + ", ".join(["a graph"] * 26) + ".")],
    "C09d": [(HYP, ""), (PTR, PTR + CORS)],
    "C10": [(PRELIM_OPEN, "\\[ x=1 \\]\n" + PRELIM_OPEN)],
    "C10c": [("whose gap is at most $\\max A$. This proves Theorem~\\ref{thm:main}.", "whose gap is at most $\\max A$, " + ", ".join([WORDS40] * 9) + ".")],
    "C10d": [("\\section{Conclusion}\\label{sec:conclusion}", "\\section{Two sides}\\label{sec:twosides}\nThis section looks at the two sides once more, in the plain sense of the word, so that a reader sees them.\n\n\\section{Vectors}\\label{sec:conclusion}")],
    "C11b": [(PTR, ""), ("so the bound of Theorem~\\ref{thm:main} is attained.", "so the bound is attained."), (PROOF_HDR, "\\begin{proof}"),
             ("Section~\\ref{sec:prelim} fixes the words we use, and every\nsymbol of the paper is listed in Appendix~\\ref{app:notation}, the table at the end.",
              "The next section fixes the words we use, and every\nsymbol of the paper is listed in the table at the end.")],
    "C13a": [("Throughout, $\\mathbb{N}=\\{1,2,3,\\dots\\}$\ndenotes the positive integers, so the natural numbers start at one.", "We use $n\\in\\mathbb{N}$ freely."),
             ("& the positive integers &", "& the naturals &")],
    "C16b": [("\\section{Preliminaries}", "\\section{SOME PRELIMINARIES}")],
    "C17d": [("$m$ & a bound on the gap & Lemma~\\ref{lem:step} \\\\", "$m$ & 0.12345678 & 0.98765432 \\\\\n$x$ & 0.11111111 & 0.22222222 \\\\\n$y$ & 0.33333333 & 0.4 \\\\")],
    "C20e": [("For every finite set $A$ of positive real numbers there", "\\begin{enumerate}\n\\item one\n\\item two\n\\item three\n\\item four\n\\item five\n\\end{enumerate}\nFor every finite set $A$ of positive real numbers there")],
    "C12": [(INTRO_END, INTRO_END + " Let $\\sigma$, $\\kappa$ and $\\tau$ be three positive numbers."),
            (END_CONC, END_CONC + "\n\n" + WORDS40 + ". The numbers $\\sigma$, $\\kappa$ and $\\tau$ play no role here. " + WORDS40 + ".")],
    "C13": [("\\section{Preliminaries}", "\\section{Splits and gaps}"), (INTRO_END, INTRO_END + " " + SYMS + " " + SYMS)],
    "C14": [("In both cases the gap stays at most $m$", ", ".join([WORDS40] * 11) + ". In both cases the gap stays at most $m$"),
            ("The idea behind everything below is simple: put", "Put")],
    "C14a": [("In both cases the gap stays at most $m$", ", ".join([WORDS40] * 28) + ". In both cases the gap stays at most $m$")],
    "C14c": [("Then the new split also has gap at most $m$.\n\\end{lemma}\n", "Then the new split also has gap at most $m$.\n\\end{lemma}\n" + " ".join([WORDS40 + "."] * 6) + "\n")],
    "C17": [(PTR, PTR + CORS)],
    "C18": [(PTR, PTR + "".join("\n\\begin{equation}\\label{eq:%s}\n%s=1\n\\end{equation}\n" % (k, k) for k in "abc")),
            (END_CONC, END_CONC + " The values \\eqref{eq:a}, \\eqref{eq:b} and \\eqref{eq:c} stay as they were.")],
    "C18a": [("Otherwise the new gap is", "By Lemma~\\ref{lem:later}, otherwise the new gap is"),
             ("\\section{Conclusion}", "\\begin{lemma}\\label{lem:later}\nThe gap is never negative.\n\\end{lemma}\n\n\\section{Conclusion}")],
    "C18d": [("\\ref{", "\\nref{", "all"),
             (LEMMA_PROOF, LEMMA_PROOF + "\n\\begin{lemma}\\label{lem:x1}\nThe gap is never negative.\n\\end{lemma}\n\\begin{lemma}\\label{lem:x2}\nThe gap is finite.\n\\end{lemma}\n")],
    "C18e": [(PROOF_HDR, "\\begin{proof}"), (SEC_PROVES, "We follow the greedy rule")],  # the section sentence locates it too (28 Nov)
    "C20": [("Write $s\\le t$ for the two sums", "Write $\\sigma$ for the gap and $s\\le t$ for the two sums"),
            (LEMMA_PROOF, LEMMA_PROOF + "\n\\begin{lemma}\\label{lem:sig}\nThe number $\\sigma$ is at most $m$.\n\\end{lemma}\n")],
    "C20c": [("After the step the sums are $s+a$ and $t$.", "After the step the sums are\n\\begin{equation}\\label{eq:inproof}\ns+a \\quad\\text{and}\\quad t.\n\\end{equation}"),
             (LEMMA_PROOF, LEMMA_PROOF + "\n\\begin{lemma}\\label{lem:eq}\nThe sums in \\eqref{eq:inproof} differ by at most $m$.\n\\end{lemma}\n")],
})


# negative controls (28 Nov, from false fires on a real paper): each edit of BASE must leave the named rule SILENT
POS = {
    "C18e#6": [(SEC_PROVES, "We follow the greedy rule"),
               (PROOF_HDR, "\\begin{corollary}\\label{cor:given}\nThe gap is finite, given the hypotheses of Theorem~\\ref{thm:main}.\n"
                "\\end{corollary}\n\n\\begin{proof}")],  # 'Given' is not 'gives': borrowing the setting does not locate the proof (28 Nov)
    "C18e#9": [(SEC_PROVES, "We follow the greedy rule"), (PROOF_HDR, "\\begin{proof}"),
               ("This proves Theorem~\\ref{thm:main}.", "Theorem~\\ref{thm:main} follows.")],  # a bare 'follows.' at the end is too late (28 Nov)
    "C06a#4": [(INTRO_END, INTRO_END + " The Bernoulli conjecture would give the sharp constant.")],  # a class word with 'conjecture' still needs its source (28 Nov)
    "C18e#5": [(INTRO_END, INTRO_END + " Theorem~\\ref{thm:main} is the main result."), (SEC_PROVES, "We follow the greedy rule"),
               (PROOF_HDR, "\\begin{theorem}\\label{thm:other}\nThe empty split has gap zero.\n\\end{theorem}\n\n\\begin{proof}")],
               # a prose mention and an unrelated proved theorem do not locate the proof (one environment at a time, 28 Nov)
    "C07b#2": [("\\bibitem{graham} R. L. Graham, Bounds on multiprocessing timing anomalies,", "\\bibitem{graham} R. L. Graham, \\emph{Bounds on multiprocessing timing anomalies},"),
               (BIB_END, "\\bibitem{graham2} R. L. Graham, \\emph{Bounds on multiprocessing timing anomalies}, SIAM J. Appl. Math. 17 (1969), 416–429.\n" + BIB_END),
               (INTRO_END, INTRO_END + " See \\cite{graham2}.")],  # the same pages written with a unicode en dash (28 Nov)
    "C10c#2": [("whose gap is at most $\\max A$. This proves Theorem~\\ref{thm:main}.", "whose gap is at most $\\max A$, "
                + ", ".join([WORDS40] * 9) + ". It remains to show that the gap is finite.")],
    "C10c#3": [("whose gap is at most $\\max A$. This proves Theorem~\\ref{thm:main}.", "whose gap is at most $\\max A$, "
                + ", ".join([WORDS40] * 9) + ". It remains to\nshow that the gap is finite.")],
    "C18#3": [(PTR, PTR + "".join("\n\\begin{equation}\\label{eq:%s}\n%s=1\n\\end{equation}\n" % (k, k) for k in "abc")),
              (END_CONC, END_CONC + " Since $t>0$, \\eqref{eq:a} holds. Since $s>0$, \\eqref{eq:b} holds."
               " Since $r>0$, \\eqref{eq:c} holds.")],
    "C18#2": [(PTR, PTR + "".join("\n\\begin{equation}\\label{eq:%s}\n%s=1\n\\end{equation}\n" % (k, k) for k in "abc")),
              (END_CONC, END_CONC + " Here $t>0$. Then \\eqref{eq:a} holds. Here $s>0$. Then \\eqref{eq:b} holds."
               " Here $r>0$. Then \\eqref{eq:c} holds.")],
}

NEG = {
    "C18": [(PTR, PTR + "".join("\n\\begin{equation}\\label{eq:%s}\n%s=1\n\\end{equation}\n" % (k, k) for k in "abc")),
            (END_CONC, END_CONC + " The values \\eqref{eq:a}, $a=1$, and \\eqref{eq:b}, $b=1$, and"
             " \\eqref{eq:c}, $c=1$, stay as they were.")],
    "C18#3": [(PTR, PTR + "".join("\n\\begin{equation}\\label{eq:%s}\n%s=1\n\\end{equation}\n" % (k, k) for k in "abc")),
              (END_CONC, END_CONC + " The value $a=1$ from \\eqref{eq:a}, the value $b=1$ from \\eqref{eq:b} and the"
               " value $c=1$ from \\eqref{eq:c} stay as they were.")],
    "C18#2": [(PTR, PTR + "".join("\n\\begin{equation}\\label{eq:%s}\n%s=1\n\\end{equation}\n" % (k, k) for k in "abc")),
              (END_CONC, END_CONC + "\n\n\\begin{tabular}{ll}\n$a$ & the value $a=1$, equation \\eqref{eq:a}\\\\\n"
               "$b$ & the value $b=1$, equation \\eqref{eq:b}\\\\\n$c$ & the value $c=1$, equation \\eqref{eq:c}\n"
               "\\end{tabular}\n")],
    "C06b": [(INTRO_END, INTRO_END + " The question was studied by Graham: if every set is split greedily, then the gap of the"
              " greedy split is at most the largest element and at most the sum of the two smallest elements together"
              " \\cite{graham}.")],
    "C06d": [(INTRO_END, INTRO_END + " Graham proved in 1969 that such a rule on any finite list of positive real numbers,"
              " taken in decreasing order, gives two parts whose sums differ by at most the largest element \\cite{graham}.")],
    "C06a#3": [(INTRO_END, INTRO_END + " By the Borel--Cantelli lemma and Markov's inequality, the Toeplitz problem"
                " reduces to the Gaussian one.")],  # textbook results and a class adjective need no citation (28 Nov)
    "C18e#7": [(PROOF_HDR, "\\begin{proof}")],  # the header is gone but 'This section proves Theorem~\ref' still locates it (28 Nov)
    "C18e#8": [(SEC_PROVES, "We follow the greedy rule"), (PROOF_HDR, "\\begin{proof}"),
               (INTRO_END, INTRO_END + " Theorem~\\ref{thm:main} follows from Lemma~\\ref{lem:step}.")],  # 'follows from' names the route (28 Nov)
    "C06a#5": [(INTRO_END, INTRO_END + "\n\n\\begin{lemma}[Covering lemma]\\label{lem:cov}\nEvery split covers itself.\n\\end{lemma}\n")],  # the paper's own title (28 Nov)
    "C06a#2": [(INTRO_END, INTRO_END + " Thus Problem~\\ref{thm:main} stays open in general.")],  # the paper's own numbered problem, 28 Nov
    "C18e#3": [(PROOF_HDR, "\\begin{proposition}\\label{prop:body}\nThe greedy split satisfies the conclusion of"
              " Theorem~\\ref{thm:main}.\n\\end{proposition}\n\n\\begin{proof}")],  # a body statement names it, its proof follows (28 Nov)
    "C18e#4": [(INTRO_END, INTRO_END + "\n\n\\begin{theorem}[{\\cite{graham}}]\\label{thm:graham}\nThe greedy gap is at most"
                " the largest element.\n\\end{theorem}\n")],  # a quoted theorem: its proof is in the cited work (28 Nov)
    "C07b": [(BIB_END, "\\bibitem{x1} A. One, First paper, \\emph{J. Math. Anal. Appl.} \\textbf{47} (1974), 1--2.\n"
              "\\bibitem{x2} B. Two, Second paper, \\emph{J. Math. Anal. Appl.} \\textbf{110} (1985), 3--4.\n" + BIB_END),
             (INTRO_END, INTRO_END + " See \\cite{x1,x2}.")],
    "C06a": [(INTRO_END, INTRO_END + " The Hilbert problem, which asks whether the bound above can be reached by a"
              " schedule built greedily from the longest job down, and which has been studied for every number of"
              " machines and for several weighted variants of the same question, is settled in \\cite{graham}.")],
    "C07b#2": [(BIB_END, "\\bibitem{x1} A. One, First paper, \\emph{J. Math. Anal. Appl.} \\textbf{47} (1974), 1--2.\n"
                "\\bibitem{x2} B. Two, Second paper, \\emph{J. Math. Anal. Appl.} \\textbf{47} (1974), 5--9.\n" + BIB_END),
               (INTRO_END, INTRO_END + " See \\cite{x1,x2}.")],
    "C18e": [("\\begin{theorem}\\label{thm:main}", "\\begin{theorem}[Theorem~\\ref{thm:main}]"),
             ("parts whose sums differ by at most\n$\\max A$.", "parts whose sums differ by at most\n\\begin{equation}\\label{eq:gapbound}\n\\max A.\n\\end{equation}")],
    # a long proof closed by 'Steps 1--4 show ..., which is the lemma'
    "C10c": [(LEMMA_PROOF, LEMMA_PROOF + "\n\n\\begin{lemma}\\label{lem:long}\nThe gap is at most $m$.\n\\end{lemma}\n\\begin{proof}\n"
              + "In this step the gap stays below $m$ when one more number is put on the lighter side of the split. " * 28
              + "\nSteps 1--4 show that the gap is at most $m$, which is the lemma.\n\\end{proof}")],
    # an introduction corollary pointing to a numbered corollary whose plain proof follows it at once
    "C18e#2": [(INTRO_END, INTRO_END + "\n\n\\begin{corollary}[Corollary~\\ref{cor:late}]\nEvery set of two positive numbers has a"
                " split with gap at most its largest element.\n\\end{corollary}\n"),
               (LEMMA_PROOF, LEMMA_PROOF + "\n\n\\begin{corollary}\\label{cor:late}\nEvery set of two positive numbers has a split"
                " with gap at most its largest element.\n\\end{corollary}\n\\begin{proof}\nPut the larger number alone on one side;"
                " the gap is the difference, at most the larger number.\n\\end{proof}")],
}


def run(matrix=False):
    import pw1k as E
    import pw1k_readable as Rr
    base = open(os.path.join(HERE, "pw1k_readable_base.tex"), encoding="utf-8", newline="").read().replace("\r\n", "\n")
    rules = [r for r in E.rules() if r["chapter"] == "readable"]
    pid = {r["rid"]: r["id"] for r in rules}
    cid_of = {v: k for k, v in pid.items()}
    fails, notes = [], []
    specs = [(x[1], x[2] if x[1] == "fn" else tuple(x[2])) for x in Rr.READ]
    if len(set(specs)) != len(specs):
        fails.append("two rules share one trigger: %s" % sorted(set(s for s in specs if specs.count(s) > 1))[:3])
    if len(rules) != 120 or len(pid) != 120:
        fails.append("expected 120 readable rules, found %d" % len(rules))

    def fired(text, name):
        return set(cid_of[f[2]] for f in E.lint(E.Doc(text=text, name=name), chapter="readable"))

    on_base = fired(base, "base.tex")
    if on_base:
        fails.append("BASE is not silent: %s" % ", ".join(sorted(on_base)))
    hit = {}
    untested = []
    for cid, edits in MUT.items():
        if not edits:
            untested.append(cid)
            continue
        t = base
        bad = [e[0][:40] for e in edits if e[0] not in t]
        if bad:
            fails.append("%s: fixture text not in BASE: %r" % (cid, bad[0]))
            continue
        for e in edits:  # (old, new) replaces the first occurrence, (old, new, "all") every one
            t = t.replace(e[0], e[1], -1 if len(e) > 2 else 1)
        hit[cid] = fired(t, cid + ".tex")
        if cid not in hit[cid]:
            fails.append("%s does not fire on its own fixture (fired: %s)" % (cid, ", ".join(sorted(hit[cid])) or "none"))
    for cid, edits in NEG.items():
        t = base
        bad = [e[0][:40] for e in edits if e[0] not in t]
        if bad:
            fails.append("NEG %s: fixture text not in BASE: %r" % (cid, bad[0]))
            continue
        for e in edits:
            t = t.replace(e[0], e[1], 1)
        if cid.split("#")[0] in fired(t, cid.replace("#", "_") + "_neg.tex"):
            fails.append("%s fires on its negative control" % cid)
    notes.append("%d negative controls checked" % len(NEG))
    for cid, edits in POS.items():  # extra positives: each must fire its rule
        t = base
        for e in edits:
            t = t.replace(e[0], e[1], 1)
        if cid.split("#")[0] not in fired(t, cid.replace("#", "_") + "_pos.tex"):
            fails.append("%s does not fire on its extra positive" % cid)
    notes.append("%d extra positives checked" % len(POS))
    missing = [x[0] for x in Rr.READ if x[0] not in MUT]
    if missing:
        fails.append("no fixture entry: %s" % ", ".join(missing))
    col = {}
    for cid in pid:
        col[cid] = frozenset(k for k, v in hit.items() if cid in v)
    same = {}
    for cid, c in col.items():
        if c:
            same.setdefault(c, []).append(cid)
    twins = [v for v in same.values() if len(v) > 1]
    ok = len([c for c in hit if c in hit[c]])
    notes.append("BASE silent: %s; %d of %d fixtures fire their own rule; %d rules have no fixture yet (%s)"
                 % (not on_base, ok, len(hit), len(untested), ", ".join(untested)))
    if twins:
        notes.append("rules firing on exactly the same fixtures (check they are distinct checks): %s" % twins)
    if matrix:
        for cid in sorted(hit):
            notes.append("  %-5s -> %s" % (cid, " ".join(sorted(hit[cid]))))
    return fails, notes


if __name__ == "__main__":
    f, n = run("--matrix" in sys.argv)
    for line in n:
        print(line)
    for line in f:
        print("FAIL", line)
    print("pw1k_readable selftest: %d failure(s)" % len(f))
    sys.exit(1 if f else 0)

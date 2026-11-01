import json
import pathlib
import re

here = pathlib.Path(__file__).resolve().parent
base = pathlib.Path('~/Downloads/Probability_1000_20h_20260906/sources')
jobs = [
 ('beta_splitting_overview', [(577,593),(1970,2010),(2421,2442)], None),
 ('biskup_dgff_extrema_2020', [(14460,14500)], r'10\.33|infinite mean|ﬁrst moment|first moment|E\(ZD'),
 ('free_unimodality_journal_2018', [], r'Problem 4\.6|Theorem 4\.1|exponential|mode'),
 ('randomstrasse_2025_v1', [(1282,1334)], None),
 ('heydenreich_hofstad_highd_2017', [], r'Open Problem 9\.1|Open Problem 16\.3|asymptotic sense|minimal spanning tree'),
 ('pete_pgg_notes', [], r'Conjecture 12\.7|Benjamini.Schramm|1 / \(1|1/\(1|Cheeger|isoperimetric dimension'),
 ('lyons_peres_20260819', [(21075,21090)], None),
 ('burdzy_open_20260906', [], r'acute|triangle|coupling|Kendall'),
]
all_snippets=[]
for topic,ranges,pattern in jobs:
    path=base/topic/'text.txt'
    if not path.is_file():
        path=pathlib.Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')/'sources'/topic/'text.txt'
    if not path.is_file():
        path=pathlib.Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/raw')/(topic+'_statements.txt')
    if not path.is_file():
        print(json.dumps({'topic':topic,'missing_cached_text':True}))
        continue
    if pattern:
        regex=re.compile(pattern,re.I)
        matches=[]
        with path.open(encoding='utf-8') as file:
            for i,line in enumerate(file,1):
                if regex.search(line):
                    matches.append(i)
        # Tail matches avoid introductions; explicit problem labels are retained.
        selected=matches[-12:]
        ranges += [(max(1,i-4),i+9) for i in selected]
    wanted={i for a,b in ranges for i in range(a,b+1)}
    lines=[]
    with path.open(encoding='utf-8') as file:
        for i,line in enumerate(file,1):
            if i in wanted:
                lines.append(f'{i}: {line.rstrip()}')
            if wanted and i>max(wanted):
                break
    block={'topic':topic,'path':str(path),'lines':lines}
    all_snippets.append(block)
    print(json.dumps(block,ensure_ascii=False))
(here/'source_followup.json').write_text(json.dumps(all_snippets,indent=2,ensure_ascii=False),encoding='utf-8')

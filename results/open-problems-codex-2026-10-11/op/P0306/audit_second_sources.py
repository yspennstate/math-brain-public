from pathlib import Path
import re

root=Path(__file__).resolve().parent
out=['# Continuation source excerpts (not a solution theorem)\n']
for name,pages in [('second_lead_1102.4177.txt',[8]),('second_lead_2006.11050.txt',[4,23,24])]:
    text=(root/name).read_text(encoding='utf-8')
    sections=re.split(r'=== PDF PAGE (\d+) ===\s*',text)
    mapping={int(sections[i]):sections[i+1] for i in range(1,len(sections)-1,2)}
    for page in pages:
        content=mapping[page]
        out += [f'\n## {name}, PDF page {page}\n\n```text\n{content}\n```\n']
        print(name,'page',page,'characters',len(content))
(root/'SECOND_SOURCE_EXCERPTS.md').write_text(''.join(out),encoding='utf-8')
print('Saved exact extracted pages for the cited inequalities and Poisson law.')

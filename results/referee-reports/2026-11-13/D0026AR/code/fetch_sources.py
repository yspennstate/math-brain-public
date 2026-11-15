import datetime, hashlib, os, pathlib, subprocess, urllib.request
assert os.getpriority(os.PRIO_PROCESS,0)>=10, "run at nice >=10"
root=pathlib.Path(__file__).resolve().parents[1]
items={
 '2510.20461':'https://arxiv.org/pdf/2510.20461',
 '1205.4584':'https://arxiv.org/pdf/1205.4584',
 '1609.01364':'https://arxiv.org/pdf/1609.01364',
 '2103.00019':'https://arxiv.org/pdf/2103.00019',
 '1803.08761':'https://arxiv.org/pdf/1803.08761',
 'Ertul_2022':'https://alea.impa.br/articles/v19/19-20.pdf',
 '2005.13327':'https://arxiv.org/pdf/2005.13327',
 '2212.08437':'https://arxiv.org/pdf/2212.08437',
 'KCM_book_2025':'https://www.normalesup.org/~hartarsky/files/research/publi/KCM_book.pdf',
 'Blondel_thesis_2013':'https://math.univ-lyon1.fr/~blondel/Papiers/these_tel.pdf',
 'Mareche_thesis':'https://irma.math.unistra.fr/~mareche/these_mareche.pdf',
}
for name,url in items.items():
    if (root/'sources'/f'{name}.txt').exists(): continue
    try:
        with urllib.request.urlopen(url, timeout=45) as r: raw=r.read()
    except Exception as e:
        print(name,repr(e),flush=True); continue
    assert raw.startswith(b'%PDF'), (name,raw[:80])
    p=subprocess.run(['/opt/homebrew/bin/pdftotext','-layout','-','-'],input=raw,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    pages=p.stdout.decode('utf-8').split('\f')
    text='\n'.join(f'\n===== PDF PAGE {i} =====\n{page}' for i,page in enumerate(pages,1) if page.strip())
    text=''.join(ch for ch in text if ord(ch)>=32 or ch in '\n\t')
    dest=root/'sources'/f'{name}.txt'
    dest.write_text(text)
    with (root/'sources'/'manifest.txt').open('a') as out:
        out.write(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()} {url} PDF_SHA256={hashlib.sha256(raw).hexdigest()} TEXT_SHA256={hashlib.sha256(dest.read_bytes()).hexdigest()} bytes_in_memory={len(raw)}\n')
    print(name,len(pages)-1,len(raw),flush=True)

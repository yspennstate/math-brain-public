"""Fetch cited papers as page-labelled plain text. PDF bytes stay in RAM."""
import io
import pathlib
import urllib.request
from pypdf import PdfReader

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = {
    'abls_math0610550': 'https://arxiv.org/pdf/math/0610550',
    'fitzner_hofstad_1212.6390': 'https://arxiv.org/pdf/1212.6390',
    'lubetzky_sly_0812.0060': 'https://arxiv.org/pdf/0812.0060',
    'angel_friedman_hoory_0712.0192': 'https://arxiv.org/pdf/0712.0192',
    'glover_kempton_2011.09385': 'https://arxiv.org/pdf/2011.09385',
    'hermon_1707.01601': 'https://arxiv.org/pdf/1707.01601',
    'barnes_feige_1994': 'https://pure.mpg.de/rest/items/item_1834237_4/component/file_2019502/content',
    'alon_birthday_draft': 'https://web.math.princeton.edu/~nalon/PDFS/birthday.pdf',
}

if __name__ == '__main__':
    for name, url in SOURCES.items():
        target = ROOT / 'sources' / (name + '.txt')
        if target.exists():
            continue
        try:
            with urllib.request.urlopen(url, timeout=45) as response:
                raw = response.read()
            reader = PdfReader(io.BytesIO(raw))
            pieces = [f'URL: {url}\nRetrieved 2026-11-13. PDF processed in RAM only; never saved.\n']
            for i, page in enumerate(reader.pages, 1):
                pieces.append(f'\n=== PDF PAGE {i} ===\n{page.extract_text()}')
            target.write_text('\n'.join(pieces))
            print(name, len(reader.pages), 'pages', flush=True)
        except Exception as exc:
            print(name, type(exc).__name__, str(exc), flush=True)

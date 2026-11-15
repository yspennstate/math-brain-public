import concurrent.futures
import json
from pathlib import Path
from fetch_sources import fetch

items = json.loads(Path(__file__).with_name('source_manifest.json').read_text())
# Main thread plus at most three I/O workers. No numerical libraries imported.
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    pending = {pool.submit(fetch, *item): item[0] for item in items}
    for future in concurrent.futures.as_completed(pending):
        try:
            future.result()
        except Exception as error:
            print('FAILED', pending[future], repr(error), flush=True)

"""Small sequential source/metadata downloader. All writes are workspace-local."""
import pathlib
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "sources"

def fetch(url, name):
    target = OUT / name
    if target.exists():
        return
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "D0037 research source verification"})
        with urllib.request.urlopen(req, timeout=35) as r:
            payload = r.read(25_000_000)
        # A successful HTTP response may still be an anti-bot HTML page.
        if target.suffix == ".pdf" and not payload.startswith(b"%PDF"):
            target = target.with_suffix(".blocked.html")
        target.write_bytes(payload)
        print(name, len(payload), flush=True)
    except (urllib.error.URLError, TimeoutError) as e:
        print(name, str(e), flush=True)

if __name__ == "__main__":
    titles = {
        "bradley_1992": "On the spectral density and asymptotic normality of weakly dependent random fields",
        "bradley_2002": "On positive spectral density functions",
        "miller_1994": "Three theorems on mixing random fields",
        "kolmogorov_rozanov_1960": "On strong mixing conditions for stationary Gaussian processes",
        "ibragimov_rozanov_1978": "Gaussian Random Processes",
        "peller_2003": "Hankel Operators and Their Applications",
    }
    for key, title in titles.items():
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": title, "rows": 2})
        fetch(url, key + "_crossref.json")
    urls = {
        "bradley_1993.pdf": "https://projecteuclid.org/journals/annals-of-probability/volume-21/issue-4/Equivalent-Mixing-Conditions-for-Random-Fields/10.1214/aop/1176989004.pdf",
        "bradley_2002.pdf": "https://projecteuclid.org/journals/bernoulli/volume-8/issue-2/On-positive-spectral-density-functions/bj/1073419890.pdf",
        "sarason_1975.pdf": "https://www.ams.org/journals/tran/1975-207-00/S0002-9947-1975-0377518-3/S0002-9947-1975-0377518-3.pdf",
        "bradley_2007_publisher.html": "https://kendrick.press/Richard-Bradley-Introduction-to-Strong-Mixing-Conditions.htm",
        "samorodnitsky_2006.pdf": "https://people.orie.cornell.edu/gennady/LRD-NOW.pdf",
        "bradley_2012.pdf": "https://arxiv.org/pdf/1107.3854",
        "bradley_tone_2017.pdf": "https://arxiv.org/pdf/1512.01310",
    }
    for name, url in urls.items():
        fetch(url, name)

import literature_search as s, urllib.parse as u
queries={
 'arxiv_tree_scaling_recent':'https://export.arxiv.org/api/query?search_query='+u.quote('all:condensation AND (all:trees OR all:Galton) AND (all:scaling OR all:dendron OR all:Gromov)')+'&sortBy=submittedDate&sortOrder=descending&max_results=30',
 'crossref_irregular':'https://api.crossref.org/works?query='+u.quote('condensation tree limits incomplete condensation Janson')+'&rows=20',
 'github_tree_limits':'https://api.github.com/search/repositories?q='+u.quote('dendron tree limits'),
}
if __name__=='__main__':
 import concurrent.futures
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  for result in pool.map(s.get,queries.items()): print(result,flush=True)

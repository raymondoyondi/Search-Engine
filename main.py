from exa_py import Exa

exa = Exa('0d1f27b1-11d0-4bfe-9464-746e7184b551')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.google.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()

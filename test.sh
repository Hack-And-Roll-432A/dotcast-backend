curl -H "Content-type: application/x-www-form-urlencoded" \
     -d "src=NS2" \
     -d "dst=NS10" \
     -X POST \
     http://localhost:8081/get_duration

curl -H "Content-type: application/x-www-form-urlencoded" \
     -d "duration=4567" \
     -d "token=BQCHztcnKnEJzllKvkh5YMTwnsBqjQMrlOaOXGW9Qh9ZrVF8X-BH88nhbtNXD3NqE_mICcI5ylSMb7H7nM8elOllChjs_BoczTaCcTM6yVRrHFwvFyWW8-xuWCe7-rKRLaMr5P3vE4Wa2H_XXfcsQcBFWEcpCC6p-oiSdnRDmTjKd7aYxpr3Yya66a4hcYWGg0rkGTL4vQnS1c0AGE6n_SoZJpmEZZdby4s9WZZ7alxx09e1Vsy46duxQckUhf6jBsJGntTvLTJf" \
     -X POST \
     http://localhost:8081/generate

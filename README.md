# Botchat

####To start clone the repo:
https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

####Once cloned set up your own branch:
`git checkout -b {your-name}/{your-feature}`

####Make virtual environment and install necessary requirements:
`python3 -m venv env` (one time cmd)
`source venv/bin/activate` 
`pip install -r requirements.txt` 

####Set environment variables:
`export OPENAI_API_KEY={your-api-key}`
`export SERPAPI_API_KEY={your-api-key}`

####Run Flask:
`make run`
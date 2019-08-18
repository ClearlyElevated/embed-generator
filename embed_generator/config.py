from os import environ as env


token = env.get("TOKEN")
shard_count = None
shard_ids = None

prefix = ">"

extensions = [
    "cogs.help",
    "cogs.stats"
]

dbl_token = env.get("DBL_TOKEN")

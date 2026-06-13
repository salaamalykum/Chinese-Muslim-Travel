import os, datetime
repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
content_dir = os.path.join(repo_dir, "content")
count = len([f for f in os.listdir(content_dir) if f.endswith(".md")]) if os.path.exists(content_dir) else 0
ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
with open(os.path.join(repo_dir, "STATS.md"), "w") as f:
    f.write(f"# Travel Dataset Heartbeat\n> **Last Updated:** {ts}\n- Total Articles: {count}\n- Topic: Halal Tourism & Geography")

import os
# One-liner entry (200 chars max): the line below is the entire submission.
# Writes the line to /output/entry.txt.
LINE = "With this ring, I thee wed: two charging cables, one outlet, and a lifetime of negotiating who gets the fast charger."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)

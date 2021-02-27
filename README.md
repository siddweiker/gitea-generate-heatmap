
# Gitea script to create dummy repo

This script will create a commit every 15 minutes for the current day
in your timezone and push each individually to Gitea.

In the "actions" table, this will create 96 entires (24\*4), and there
will also be 2 additional entries for the repo and branch creation.

# How to use

- Install python 3
- Clone this repo
- Delete `.git/`
- Create a repo in gitea
- Clone the repo to the current directory `git clone <url> .`
- Run `python generate_heatmap.py`
- Update SQLite with the `update_action.sql` file
- Update the 2 first entries in the `action` table to the previous day for simplicity

# Verification

You should see `96` contributions in the heatmap for the current day.


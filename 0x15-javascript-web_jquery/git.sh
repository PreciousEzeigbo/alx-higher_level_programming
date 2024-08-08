#!/bin/bash

# Check if a commit message is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: ./git_auto_push.sh 'Your commit message'"
  exit 1
fi

# Add all changes to git
git add .

# Commit changes with the provided message
git commit -m "$1"

# Push changes to the remote repository
git push

echo "Changes pushed to the repository."

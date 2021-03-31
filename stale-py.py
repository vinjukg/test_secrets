#!/bin/env python3
import pygit2, os, datetime

repo = pygit2.Repository(pygit2.discover_repository(os.getcwd()))
time_now = datetime.datetime.now()
for branch in (repo.lookup_branch(b) for b in repo.listall_branches()):
    last_commit = branch.peel()
    commit_time = datetime.datetime.fromtimestamp(last_commit.commit_time)
    age = time_now - commit_time
    print(branch.branch_name)
    print(age)	
    if age > datetime.timedelta(days=30):
        print("{} {} {}".format(last_commit.author.email, branch.branch_name, commit_time))


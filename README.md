#merge
divya@LAPTOP-NS2F8J0Q MINGW64 ~
$ git clone https://github.com/divya-1706/fork.git
Cloning into 'fork'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.

divya@LAPTOP-NS2F8J0Q MINGW64 ~
$ cd fork

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main)
$ git branch
* main

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main)
$ git checkout -b branch1
Switched to a new branch 'branch1'

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch1)
$ git branch
* branch1
  main

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch1)
$ vim README.md

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch1)
$ git add README.md
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch1)
$ git commit -m "update readme from branch1"
[branch1 ccb8d68] update readme from branch1
 1 file changed, 1 insertion(+), 1 deletion(-)

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch1)
$ git checkout master
error: pathspec 'master' did not match any file(s) known to git

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch1)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main)
$ git checkout -b branch2
Switched to a new branch 'branch2'

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch2)
$ vim
.git/      README.md

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch2)
$ vim README.md

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch2)
$ notepad README.md

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch2)
$ cat README.md
# fork

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch2)
$ git checkout branch1
error: Your local changes to the following files would be overwritten by checkout:
        README.md
Please commit your changes or stash them before you switch branches.
Aborting

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch2)
$ ^C

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch2)
$ git add README.md
git commit -m "Update README from branch2"
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
[branch2 88ca2b4] Update README from branch2
 1 file changed, 1 insertion(+), 1 deletion(-)

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch2)
$ git checkout branch1
Switched to branch 'branch1'

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch1)
$ cat README.md
This line was added from branch1

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (branch1)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main)
$ git merge branch1
Updating 7dec274..ccb8d68
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main)
$ git merge branch2
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main|MERGING)
$ cat README.md
<<<<<<< HEAD
This line was added from branch1
=======
# fork
>>>>>>> branch2

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main|MERGING)
$ notepad README.md

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main|MERGING)
$ notepad README.md

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main|MERGING)
$ git add README.md

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main|MERGING)
$ git commit -m "Resolved merge conflict"
[main f7a22ee] Resolved merge conflict

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (main)
$ git checkout -b feature
Switched to a new branch 'feature'

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (feature)
$ git rebase main
Current branch feature is up to date.

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (feature)
$ git log --oneline --graph --all
*   f7a22ee (HEAD -> feature, main) Resolved merge conflict
|\
| * 88ca2b4 (branch2) Update README from branch2
* | ccb8d68 (branch1) update readme from branch1
|/
* 7dec274 (origin/main, origin/HEAD) Initial commit

divya@LAPTOP-NS2F8J0Q MINGW64 ~/fork (feature)
$

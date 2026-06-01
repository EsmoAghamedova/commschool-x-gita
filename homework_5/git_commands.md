PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        homework_5/

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git add .
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git branch first-branch
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git git checkout first-branch

git: 'git' is not a git command. See 'git --help'.

The most similar command is
        init
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git checkout first-branch
A       homework_5/homework_5.py
Switched to branch 'first-branch'


PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git status
On branch first-branch
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   homework_5/homework_5.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   homework_5/homework_5.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        git_commands.md

PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git add .
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git branch
* first-branch
  main
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git commit -m "first 3 tasks"
[first-branch eda75ed] first 3 tasks
 2 files changed, 164 insertions(+)
 create mode 100644 git_commands.md
 create mode 100644 homework_5/homework_5.py
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git push -u origin first-branch
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 2.52 KiB | 234.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'first-branch' on GitHub by visiting:
remote:      https://github.com/EsmoAghamedova/commschool-x-gita/pull/new/first-branch
remote: 
To https://github.com/EsmoAghamedova/commschool-x-gita.git
 * [new branch]      first-branch -> first-branch
branch 'first-branch' set up to track 'origin/first-branch'.

PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git branch second-branch
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git branch
* first-branch
  main
  second-branch
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git checkout seconf-branch
error: pathspec 'seconf-branch' did not match any file(s) known to git
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git checkout second-branch
D       git_commands.md
M       homework_5/homework_5.py
Switched to branch 'second-branch'
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git checkout first-branch
D       git_commands.md
M       homework_5/homework_5.py
Switched to branch 'first-branch'
Your branch is up to date with 'origin/first-branch'.
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git add .  
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git add .                                  
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git commit -m "first 3 task to main branch"                           
[first-branch 90a40c4] first 3 task to main branch
 3 files changed, 122 insertions(+), 82 deletions(-)
 delete mode 100644 git_commands.md
 create mode 100644 homework_5/git_commands.md
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git add .                                  
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git commit -m "first 3 task to main branch"
[first-branch 5e45319] first 3 task to main branch
 1 file changed, 1 insertion(+), 1 deletion(-)
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git merge origin main
Already up to date.
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git pull
Already up to date.
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git merge origin main
Already up to date.
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git push origin firts-branch
error: src refspec firts-branch does not match any
error: failed to push some refs to 'https://github.com/EsmoAghamedova/commschool-x-gita.git'
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git push origin first-branch                                          
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 12 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 1.91 KiB | 85.00 KiB/s, done.
Total 9 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To https://github.com/EsmoAghamedova/commschool-x-gita.git
   eda75ed..5e45319  first-branch -> first-branch
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git merge origin main       
Already up to date.
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git merge main        
Already up to date.
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git checkout main 
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\Esmira\OneDrive\Desktop\commschool x gita> git merge first-branch
Updating cd6fcc4..5e45319
Fast-forward
 homework_5/git_commands.md |  60 +++++++++++++++++++
 homework_5/homework_5.py   | 144 +++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 204 insertions(+)
 create mode 100644 homework_5/git_commands.md
 create mode 100644 homework_5/homework_5.py
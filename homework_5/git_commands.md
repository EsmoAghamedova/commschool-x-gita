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
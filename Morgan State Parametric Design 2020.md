# Morgan State Parametric Design 2020

This is the course repository for the seminar studio. Here we will track and share all course related material and student work.

## 3D Files and Output
Create two new folders '3D' and 'output'. This should be the place for all 3D models and output files (png or vector) within the course folder. We will not be tracking these in this class so placing them within these folders allows the tracker to ignore them. So if you are using a rhino file to drive your grasshopper scripts anywhere within the folder, even if it is within a folder inside the gh-binaries folder, please put them within the 3D folder.

## Basic Flow
Each student in the course has their own branch of the repository.  These branches are like segments or little containers for all the work that is done.  The added benefit is that work is tracked and can be reverted to previous versions if something breaks or you would like to revert.  Work between students can be shared in the repo by merging the branches.

For assignments in the course students shall use the 'git pull' command to get the files for the assignment

        $ git pull origin master

Do some work and make saves to your files and then do a 'commit.' If files are added, do an _add_ to add all new file to your branch

        $ git add .

Commits are like checkpoints for the state of your work in the repository.  These checkpoints are what we use to revert back to previous versions instead of using a _save as_.  Notes included in the commit statement are helpful in referring to desired checkpoints.

        $ git commit -a -m "write a small description or note here"

How often you commit is up to you.  You can commit with every save if you like.  These changes will occur locally on your computer.  When you are ready to submit your work to the remote repository where I and other students can see it use a git push command to ***your branch***

        $ git push origin first name

This means you are pushing to the remote repo call _origin_ to a branch named after your first name.

## Tutorials
Processing tutorials on various topics and features are listed in the 'tutorials.md' file

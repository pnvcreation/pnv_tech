# manage of the files
# if many programmer work in one project so, git throw we know what is changes
# git 
    # one type of software
    # distributive version controlling system
    # git free for open sorce code
    # paid for private repository
    # using git we back to over lower version
        # If three friends(amit,mohan,pankaj) works in one project
        # amit pull file throught git & chnages this after push in git
        # after mohan pull file throught git & chnages this after push in git
        # after pankaj pull file throught git & chnages this after pushin git
        # if amit not satisfied this code 
        # so, this see who have changed code using 'git log' command
        # and if amit need four their version so, back this version
        # this lower version save using commit 
# github
    # code hosting service
    # github uses git version control    

# codes for git
    # git --version
    # git status
        # know status
    # git init
        # made repositary of git
    # git add .
        # file stages
        # file move working to staging area
        # types
            # git add -A
                # stages all files in your folder
            # git add .
                # stages new and modified, without deleted
            # git add -u
                # stages deleted and modefied, without new
    # git commit -m "Version 1"
        # what file change this give
        # give comment
    # git config --global user.email "vanjarapankaj.140180107059@gmail.com"
        # if commit not run so, give this
    # git log
        # changes all the developers
    # git remote add origin git@github.com:pnvcreation/pnv_tech.git
        # used for github reporetry
    # ssh-keygen -t rsa -b 4096 -C "vanjarapankaj.140180107059@gmail.com"
        # changed ssh key
    # eval $(ssh-agent -s)
        # run
    # ssh-add ~/.ssh/id_rsa
        # ssh key add in github
    # clip < ~/.ssh/id_rsa.pub
        # copy ssh key
    # git push -u origin master
        # data push in github
    # git pull origin master
        # pull all data in git
    # git diff file_name
        # give data of you modefied this file
    # git diff --staged file_name
        # give changes info after file is staged
    # git checkout file_name
        # file return previous stage
    # git clone file_path_in_git_hub
        # copy other developers files
    # git brach
        # give branches name
    # git branch name
        # made new branch 
        # this is copy of your code
    # git checkout branch_name
        # switch master branch to your branch
# ignoring git
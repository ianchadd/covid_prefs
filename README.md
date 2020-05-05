# covid_prefs
COVID Preferences Code oTree Server


# Instructions to run locally

## Install oTree
[Follow the oTree guide if needed](https://otree.readthedocs.io/en/latest/install.html)

## Download App
Use the "Clone or download" button above

or use git:

```git clone https://github.com/ianchadd/covid_prefs.git```

## Update App
If you have already cloned the repo and just want to update your local repo from the current master branch, use the following:

- navigate to covid_prefs directory (and make sure that you are in master)

```git checkout master```

```git pull origin master```

## Run App
[Open command prompt](https://www.trishtech.com/2018/08/open-command-prompt-from-any-folder-in-windows-10/) at the download location `covid_prefs`

Run the following command:

```otree devserver```

## Open App

open [http://localhost:8000/](http://localhost:8000/) in any browser (does not require internet connection)

## Making edits to the repo
When making edits to the repo:

- first make sure you are in master and that your local version of master is updated according to the instructions above
- create new branch and label it with the current date

```git checkout -b [branch_name]```

- make edits to code on your local clone of the repo
- test code locally before each commit

```otree devserver```

- once you're done editing and you've tested locally, add edited files to the list of changes to commit

```git add .```

- add informative messages to each commit

```git commit -m "short message with info on fix"```


- push commits to the newly created branch

```git push origin [branch_name]```

- issue a pull request with Ian Chadd as the reviewer (done on github.com)

- I will review and merge to master periodically

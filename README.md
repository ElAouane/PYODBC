# Libraries, Modules and Packages
This repo is going to explore Libraries,  Modules and Packages in python
## Libraries:
Libraries are come with python, they are databases with information.

### Libraries
AKA : python standard libraries! these come out of the **box with python**
- these are mainttened by python organisation
- you just need to inmport them, no need to install.


### Modules
it's a piece of software that delivers useful functionality.
we have created some of these before both functionals and OOP.

### Package & PIP
It's a way of intalling things.

- pip** is python package manager
A package manager installs and maintains softwares and **its dependencies**
Some are better than others

**Package Managers**
They exists for almost every modern language.
ruby --> bundler --> which installs ruby gems (our version of external package)

os also have package managers
windows --> chocolaty and others(they are widely used)
ubuntu --> apt-get
mac os --> brew
python --> **pip**

case in point:
- functional calculator (ex: calculatre area of a triangle)
- oop calculator
## Git branching and workflow:
### 1. Make sure your master is up to date
```
 $ git pull origin master
```
### 2. Creating a new branch
```
    $ git checkout -b <name>
```
### 4. Push your branch to the remote
```
 $ git push origin <branch name>
```
### 5. Go and merge branch on github
Verify code, solve any conflict and merge to master.
### 6. Checkout to master and pull lastest version
```
 $ git checkout master
 $ git pull origin master
```
### 7. Rinse and repeat

### Moving between existing branches
```
    $ git checkout <branch name>
```

###  git stash
> Allows you to temporally store(stash) your code and move between gits

### git status
> Allows you check the current state of your version
>
### Import notes


- Changes will travel with if you don't commit them
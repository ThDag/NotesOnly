# NotesOnly
### simple CLI note-taking app
### Takes notes directly from your terminal

note-taking = storing plain single-line text

this app is mainly intended for any OS that doesn't have GUI and solves the struggle of storing
text for future usage.

This project uses Typer and to store the file a csv file is used (datas.csv)


## Class-feature
The class feature is a way to organize your notes. 
it is a sort of hierarchy you can access/view all
notes in class it has 3 classes; <br>
1. upper  id -> 1
2. middle; id -> 2
3. lower; id -> 3 <br>

Classes are given to notes using there id numbers


# how to setup system-wide `noon` command
just run the `setup.py` file 
```bash
sudo python setup.py
```
---
**Note**: in the examples the command `noon` is used, if this is not setup 
running `app.py` with full path from anywhere in computer can be used (very inconvenient)

Ex.
```bash
python ~/desktop/programming/NotesOnly/app.py addn "setup noon" 1
```

# Usage

NotesOnly tool is extremely simple and easy-to-use,
using simple terminal commands with little parameters.

**containing only 6 functions** <br>
1. [addn](#addn)
2. [deln](#deln)
3. [dela](#dela)
4. [editn](#editn) 
5. [viewn](#viewn)
6. [viewc](#viewc)
7. [viewa](#viewa)

## addn
Add a new note.

Ex.
```bash
noon addn 2
```
> then enter the note in the interactive note entry window

this will add a new middle class note

**addn** takes 1 argument: classid


<img src="screenshots/interactive-addn.png" alt="Image Description" width="900"/>

> if class id is not spesified it will present with a interactive class id selection window

## deln
Delete note

Ex.
```bash
noon deln 2
```
this will delete the note with **id number 2**

**deln** takes 1 parameter: note id, deletes the note with
the note id. 
*Note*: note id can take any number of ids seperated with white space
it will delete all the listed notes.

**Note**: give the index number '00' to delete the last/newest note

to see whats the id of a note [see all notes](#viewa)
or see what you are deleting with [viewn](#viewn)

<img src="screenshots/deln.png" alt="Image Description" width="400"/>


## dela
Delete all the notes

```bash
noon dela
```
this will activate a interactive windows asking for confirmation to delete all the notes
then it will proceed to delete all the notes.

**dela** takes no arguments. But it asks for confirmation before deleting all the notes.

<img src="screenshots/dela.png" alt="Image Description" width="400"/>

## editn
Edit note

Ex.
```editn
noon editn 2
```
this will open cli to edit note with the **id number 2**

**editn** takes 1 parameter: note id, edits the note with
the note id

todo!!**add here output images for editn**!! 

<img src="screenshots/editn.png" alt="Image Description" width="400"/>

## viewn
View a specific note

Ex.
```bash
noon viewn 2
```
this will print the note with the **id number 2**

**viewn** takes 1 parameter: note id, prints the note with
the note id

<img src="screenshots/viewn.png" alt="Image Description" width="400"/>

## viewc
View a specific class

Ex.
```bash
noon viewc 3
```
this will print all the **lower class notes**

**viewc** takes 1 parameter: class id, prints the notes with
the class id

there is only 3 class ids: [Class feature](#Class-feature) 

<img src="screenshots/viewc.png" alt="Image Description" width="400"/>

## viewa
view all the notes

Ex.
```bash
noon viewa
```
this will print all the notes

**viewn** takes no parameter just prints all the notes

<img src="screenshots/viewa.png" alt="Image Description" width="400"/>

# Installation

1. clone this repository
```
git clone https://github.com/ThDag/NotesOnly.git 
```
thats it (i think)

-Taha Dağıstanlı

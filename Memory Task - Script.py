# Script for portfolio assignment 4
# Bianka, Sophia, Mie, Lars & Bertram
# AU Cognitive Science 2018

# sound handling
from psychopy import prefs
prefs.general["audioLib"] = ["pyo"]
# load modules from psychopy
from psychopy import visual, core, event, data, gui, sound

# load modules
import random, glob, pandas, os

# define dialogue box for experiment
popup = gui.Dlg(title = "Memory Task") 
popup.addField("Participant ID: ")
popup.addField("Age: ")
popup.addField("Gender: ", choices = ["Female", "Male", "Other"])
popup.addField("Condition: ", choices = ["1", "2", "3"]) # add conditions for the loop
popup.show()
if popup.OK: # run experiment if OK is pressed in dialogue box
    ID = popup.data
elif popup.Cancel: # cancel experiment if dialogue box is closed
    core.quit()


# get date for unique filename
date = data.getDateStr()

# define columns
columns = ["id", "age", "gender", "condition", "stimulus", "correct"]

# define dataframe
DATA = pandas.DataFrame(columns=columns)

# define window
win = visual.Window(fullscr = True, color = "black")


### define and prepare different stimuli; text, image and sound ###
# define text stimuli
text_stim = """Apple House Cheese Hammer Door Horse Bicycle Sun Boat Mountain Glasses 
Tree Airplane Book Computer"""
cond_read = text_stim.split()
log_list = text_stim.split()

text_end = """Thanks for participating, please contact experimenter"""

# define image stimuli
cond_img = glob.glob("images/*.jpg")

# define sound stimuli
cond_sound = ("Sounds/Apple.wav", "Sounds/House.wav","Sounds/Cheese.wav","Sounds/Hammer.wav","Sounds/Door.wav","Sounds/Horse.wav","Sounds/Bicycle.wav","Sounds/Sun.wav","Sounds/Boat.wav", "Sounds/Mountain.wav", "Sounds/Glasses.wav", "Sounds/Tree.wav", "Sounds/Airplane.wav", "Sounds/Book.wav", "Sounds/Computer.wav")

# shuffle stimuli to randomize order in which they're presented
random.shuffle(cond_read)
random.shuffle(cond_img)
#random.shuffle(cond_sound)


### define functions ###
def show_text_wait(i):
    text = visual.TextStim(win, text = i)
    text.draw()
    win.flip()
    core.wait(3)

def show_text_key(i):
    text = visual.TextStim(win, text = i)
    text.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])

def show_img(i):
    img = visual.ImageStim(win, image = i)
    img.draw()
    win.flip()
    core.wait(3)

def play_sound(i):
    s = sound.Sound(i)
    s.play()
    win.flip()
    core.wait(3)

def log_data():
    text = visual.TextStim(win, text = i)
    text.draw()
    win.flip()


### start of experiment ###
# create conditional loop
if ID[3] == "1":
    for i in cond_read:
        show_text_wait(i)
elif ID[3] == "2":
    for i in cond_img:
        show_img(i)
else:
    for i in cond_sound:
        play_sound(i)

show_text_key(text_end)

for i in log_list:
    log_data()
    key = event.waitKeys(keyList = ["y", "n"])
    DATA = DATA.append({
        "id":ID[0],
        "age":ID[1],
        "gender":ID[2],
        "condition":ID[3],
        "stimulus":i, 
        "correct":key}, ignore_index = True) # append data into datafra


### create output file ###
# create filename for outputfile
logfile_name = "logfiles/logfile_{}_{}".format(ID[3], date)

# create csv file
DATA.to_csv(logfile_name)

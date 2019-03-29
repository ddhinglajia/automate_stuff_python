#!/usr/bin/env python3

# automatically fills a specific form

import pyautogui, time

# set correct coordinates for your computer

nameField = (648, 319)
submitButton = (651, 817)
submitButtonColor = (75, 141, 249)
submitAnotherLink = (760, 224)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', \
'robocop': 4, 'comments': 'Tell Bob I said hi.'},
{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, \
'comments': 'n/a'},
{'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', \
'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', \
'robocop': 5, 'comments': 'Protect the innocent. Serve the public \
trust. Uphold the law.'},
]

for person in formData:
    # Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

# Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)

    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])
    # Fill out the Name field.
    pyautogui.typewrite(person['name'] + '\t')
    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')
    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])
    # Fill out the Name field.
    pyautogui.typewrite(person['name'] + '\t')
    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')
    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])
    # Fill out the Name field.
    pyautogui.typewrite(person['name'] + '\t')
    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')
    # Fill out the Additional Comments field.
    pyautogui.typewrite(person['comments'] + '\t')
    # Click Submit.
    pyautogui.press('enter')
    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)
    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])

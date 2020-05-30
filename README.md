# Meticulist

Meticulist is an application for in-depth lists of all kinds, from checklists to bucket lists,  
ranked by urgency, priority, or time consumption.

### Features (Project Spec)
* Long Todo List
    * keeps tracks of all lists, including projects (lists of lists)
    * counter for total tasks completed
    * deadlines
* Habit Tracker
    * resets every day
    * list of habits you want to make
    * counter for days in a row completed (streak)
    * counter for totals days completed
        * some visual thing coloring in completion days for individual tasks
* Checklists
    * for routines (morning tasks, doctor's checklists, etc.)
    * toggleable restricted lists (unlock later tasks by completing previous ones)
        * forced sequential
    * resets daily
* Project Checklist
    * Type of checklist
    * Deadline
    * Does not repeat, disappears once complete
* Sort By
    * priority - High, Medium, Low
    * urgency - Yes/No
    * time - give an estimate how long you think the task will take
* Ask for something to do in x amount of time
    * priority queue will pick something based on urgency, priority
    * choose a task that fits in x minutes or less, program will find task that takes x minutes or less
        * if none, suggest next shortest task
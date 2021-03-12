README.txt

==== Exercise 1:

See Exercise-1.docx for Test Plan

Time taken:
1 hour was spent in writing the test plan.
  20 minutes in initial review, 10 minutes in writing test strategy, 30 minutes in writing the test conditions for the user stories.
Another 15 minutes spent in tidying up the document for sending. = 01:15 total



==== Exercise 2: Test automation

Chose Selenium for automating UI testing for both tests. Selected for UI automation 
for meeting key criteria. It is a tool of choice in the industry for Browser based 
UI automation. It is open source and has support from the major browser vendors 
and active support from the community.

Chose Python language bindings for python's wide popularity, library functionality and portability.


Part 1: Locating the Lively Flip "Learn More" button
------
See exercise-2-1.py   


Part 2: Locating the support "Learn More" button
------
See exercise-2-2.py


Notes: 
1. Both tests give fail on the last assertion after click when new page navigation is checked.
      Seems the click is not working on this '<a' element with role="button". 
      Need to investigate further or look for another method.

2. Time taken:
   - Some time was spent in installing Selenium as I did not have it on my home computer.
   - About 1 hour was spent in writing the tests, and another hour spent in debugging the fact that button.click was not workign as expected. This needs further investigation and was not resolved.


==== Exercise 3 API testing (optional)
    While I've used Postman often for manual interactions with the Web API, I have
not used node.js to script tests. I normally use curl in a shell script. 
    This is not something I could do without training myself on it first.
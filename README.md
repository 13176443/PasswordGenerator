---
ICTPRG434 Collaborative Software Project: "Secure Password Generator"
Authors:
 - Sebastian (13176443)
 - Phoebe (13235673)
---

# Executive Summary

This serves as our repository and documentation of our software project. The documentation consists of our project overview, the team behind the project and the process of our project. In the project overview we have the information about the introduction, requirements and processes of our software project

# Project Overview

## Introduction

The software project is a secure password generator script which was created in Python. It allows the user to generate passwords and passphrases. The program allows you to input certain criteria to add into the generated passwords/passphrase, for added complexity and strength. This software automates and provides users with randomly secure passwords/passphrase that outputs several generated passwords/passphrases onto the results on the screen for the user and optionally onto a text file to analysis 

## Team Structure and Roles

Our team consists of two members:
 - Sebastian (13176443) - Work on python code, git / report documentation
 - Phoebe (13235673) - Work on flowchart, pseudocode, git / report documentation 
---
## Problem Analysis and Requirements

A thorough analysis of the problem presented in the case study and the specific requirements for the automation solution.
When conducting an analysis, we looked towards what can be accomplished with the specifc requirements of implementing a automated solution. We are required to create this project with automation in mind as the main requirement throughout the entire process of the software project.

# Design Process

## Conceptual Design

The initial ideas we have come up for the secure password generator is to have automation in mind right in the beginning. When coming up with the software to generate passwords/passphrase we prompted to allow the user to only input in what they needed in their generated password/passphrase, while the rest of the program will handle the automation of generating a secure password/passphrase and outputting the results were needed by the user. This approach provides a simple and easy design towards good user experience provided by the script.

## Algorithm Design

Detailed presentation of the developed algorithm, including flowcharts and pseudocode. See [this guide on creating mermaid flowcharts](https://mermaid.js.org/syntax/flowchart.html).

```mermaid
flowchart LR
    A(Start) --> B[Input Year]
    B --> C{Is year divisible by 4?}
    C -- Yes --> D{Is year divisible by 100?}
    C -- No --> E[Not a leap year]
    D -- Yes --> F{Is year divisible by 400?}
    D -- No --> G[Leap year]
    F -- Yes --> G
    F -- No --> E
    G --> H(End)
    E --> H(End)
```

```
FUNCTION isLeapYear(year):
    IF year MODULO 4 IS NOT EQUAL TO 0:
        RETURN False
    ELSE IF year MODULO 100 IS NOT EQUAL TO 0:
        RETURN True
    ELSE IF year MODULO 400 IS EQUAL TO 0:
        RETURN True
    ELSE:
        RETURN False

year = INPUT "Enter a year: "
IF isLeapYear(year):
    PRINT year, "is a leap year."
ELSE:
    PRINT year, "is not a leap year."
```

## Software Design

Our choice of programming language is python. Python is a simple to use programming language that allows for a broad amount of support and technicality. And simply python allows for creating easy automation tasks with pythons' simple syntax and collection of modules and libraries which make it very ideal for scripting repetitive tasks, which makes it an ideal programming language. After the choice of the programming langauge we decided on the IDE (integrated development environment) which we will use to write the python code, we decided on 'PyCharm' as our choice of IDE.

# Implementation

## Code Development

[SecurePasswordGenerator](SecurePasswordGenerator.py)

## Testing and Debugging

Testing process 

To test and develop our code we used PyCharm as our IDE of choice. This environment provides code analysis, an integrated unit tester along with other tools to help the testing process is a success we’ve performed tests on certain factors of the software's code. Each test was conducted differently to ensure all parts of the program work as intended when it all comes together. Our test process consisted of running the program as intentional to see if any errors pop up, after a test was successful, we will next then perform another test with inputs and responses that aren’t usually inputs, this will test to see how our program will respond back and if any errors appear. We will than repeat to process after every iteration of our program. 

Debugging 

Throughout our implementation and development of the software project we have used PyCharm as our developing and debugging environment to perform numerous debugging methods. The debugging methods that we’ve have used were: 
```
    Running the entire program first as intended then see if the program will run into potential errors during run time 

    Performing unit testing 

    Performing print debugging 

    Performing static analysis 
````
The first method is a simple one and lets us run the program like you normally would, to test if the program was successful or no. Using this method allowed us to easily find out after or during the runtime if there was something wrong and the program will tell us that 

The second method of debugging we used was **unit testing**, in each iteration of our program we have tested individual bits and parts of our code before implementing to the main, so this means before we add a new part of code to the main program we test it in its self to ensure when that the part of the code is implemented into the main, it will work still work it intentionally should.
![UnitTest](https://github.com/13176443/PasswordGenerator/blob/main/Images/UnitTest.png)

**(A sample of the code from the program in Pycharm, this code can be run by itself to test if the output is intended)**

The third method we used was **print debugging**, in each line of code where we want something to happen, we’ve have added print statements. By adding print statements, it will output the results or message inside that print statement if a condition has been met.
![PrintDebug](https://github.com/13176443/PasswordGenerator/blob/main/Images/PrintDebug.png)

**(Snapshot of the code from the program during testing in PyCharm, with red arrows pointing at the print statements that were for testing its functionality)**

The final method we use is static analysis, before execution we inspect the code of the software to check for any logical, syntax errors, to ensure the code is correctly written.

# Collaboration and Project Management

## Meeting Notes

To view out Meeting Notes please click here: [Meeting-Notes](https://github.com/13176443/PasswordGenerator/blob/main/Minutes%20Meetings/Brainstorm-Meetings.txt)

## Project Management Tools and Techniques

The tools we used to manage our project is GitHub and OneDrive. By using GitHub we’re able to push our python code and documentation onto our repository. With a repository, we can easily push & commit any changes and modifications and upload any files onto our repository at any time. Having a GitHub repository allows for a centralization and collaboration platform needed for our team. We used OneDrive for the team members to share and collaborate on writing documentation for our software project. OneDrive allows for multiple people to work on the same document in real-time. 

# Documentation

## Developer Documentation

Detailed explanation of the code and architecture, aimed at future developers who might work on or maintain the project.

## User Documentation

To view our User Documentation please click here: [User-Documentation](https://github.com/13176443/PasswordGenerator/blob/main/User%20Documentation.pdf)

# Reflection and Conclusion

Python code – the structure. 

Flowchart – Which shapes go where, what to write for each decision that the flowchart was asking. 

Pseudocode – received assistance and feedback from each other on how to structure and write out the pseudocode. 

Our group had faced challenges with the python code, the flowchart and the pseudocode. To overcome these challenges, we worked together to find a solution for the flowchart and the pseudocode. And for the python code, we received assistance from our lecturer and from online sources, to help with the structure of the secure password generator. 
The pseudocode, flowchart and python code are all completed, we must transfer our work to GitHub, we are utilising the template provided to us to create our report. 
For the future, we will continue to support each other and ask for assistance if needed, to complete our collaborative project efficiently. 

# Appendices

Links to the code repositories containing the final source code, separate user manuals, presentations, or other documentation (if any).

Any other relevant materials, such as additional diagrams, extended testing documentation, or supplementary research.

References: A list of all the sources referenced throughout the project.


Link to our GitHub Repository: https://github.com/13176443/PasswordGenerator

Utilised flow charts pdf from session 1, exercise 1 in the Gordon online automate processes unit. 

#!usr/bin/python3

"""
Controlling 'child' applications is not as difficult as you thing,
pexpect provides a simple way of controlling an application.
"""

import pexpect, time

def control_application():
    """
    Controlling applications with python3 is a create mechanism for
    orchestration and automation. Pexpect is one such package that 
    allows you control a variety of applications via automation.
    Start by 'spawning' a child application, 'expect' a certain string
    of works that would normally appear in cli, and then 'sendline' the 
    command that you want to execute. I found allowing a pause in between
    expect and sendline helps with making sure the program executes correctly.
    """
    # This starts the child application
    child = pexpect.spawn("./application")
    # Print an indicator of what is happening
    print("The application is starting and I am providing 'x' input")
    # pexpect uses regex to look for words before sending input
    child.expect("Add in the words I am waiting to see")
    time.sleep(5)
    # Once specific words are detected, pexpect sends the input
    child.sendline('Add in the text I want to send - option, user, password')



#################################+++Example+++############################

"""
Here is an example from part of a code I wrote to automate Algo VPN deployment
"""

import pexpect

child = pexpect.spawn("./algo")
# Indicate provider for digital Ocean
print("Choosing Provider....Digital Ocean")
# Look for input indicator
child.expect('Enter the number of your desired provider')
time.sleep(5)
# Enter input to choose Digital Ocean
child.sendline('1')
#!usr/bin/python3

"""
I needed to make sure that my main script didn't run simulataneous
copies of itself. Useful for prevent cronjob overlap or to prevent
multiple instances of an app running. In my case I used it for a Qt5
application.
"""

##################++++///Code Snippet///++++#######################

"""
Method One:
Integrate the code with your main app.
"""
import os, sys

if __name__ == "__main__":
    # Create a PID
    pid = str(os.getpid())
    # Establish a temporary file
    pidfile = "/tmp/mydaemon.pid"

    # If the file is detected as open, exit the application
    if os.path.isfile(pidfile):
        print("{}s already exists, exiting".format(pidfile))
        sys.exit()
    
    # Open and write to the PID file
    open(pidfile, 'w').write(pid)

    # Execute the main function of the application
    try:
        main()
    
    # Unlink the pidfile when you are finished
    finally:
        os.unlink(pidfile)

"""
Method Two:
Add the code into your script.
"""
import os, sys

# Create a PID
pid = str(os.getpid())
# Establish a temporary file
pidfile = "/tmp/mydaemon.pid"

# If the file is detected as open, exit the application
if os.path.isfile(pidfile):
    print("{}s already exists, exiting".format(pidfile))
    sys.exit()

# Open and write to the PID file
open(pidfile, 'w').write(pid)

# Execute the main function of the application
try:
    main()

# Unlink the pidfile when you are finished
finally:
    os.unlink(pidfile)
        
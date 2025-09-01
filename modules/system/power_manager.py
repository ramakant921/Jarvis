# from core.engine import speak
# import os
# import ctypes

# #Function to put  the system to sleep
# def sleep():
#     speak("Sleeping...")
#     powrprof = ctypes.windll.powrprof # Load powrprof.dll to access SetSuspendState
#     powrprof.SetSuspendState(0, 1, 0) # Set the system to hibernate (1 - Hibernate, 0 - Suspend, 0 - Force) 

# #Function to hibernate system
# def hibernate():
#     speak("Hibernating...")
#     os.system("rundll32.exe powrprof.dll,SetSuspendState 1,0,0")

# #Function to restart the system
# def restart():
#     speak("Initializing Restart Sequence in 10 seconds")
#     os.system("shutdown /r /t 10")

# #Function to shutdown the system
# def shutdown():
#     speak("Initializing Shutdown Sequence in 10 seconds")
#     os.system("shutdown /s /t 10")
 
# # Function to handle Power Manager
# def power_manager(command):
#     if "sleep" in command:
#         sleep()
#     elif "hibernate" in command:
#         hibernate()
#     elif "restart" in command:
#         restart()
#     elif "shutdown" in command:
#         shutdown()
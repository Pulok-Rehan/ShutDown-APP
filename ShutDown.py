from tkinter import *
import os

st= Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="blue")

def restart():
    os.system("shutdown /r /t 1")

def restart_with_time():
    os.system("shutdown /r /t 30")

def shutdown():
    os.system("logout /s /t 1")

def logout():
    os.system("shutdown -1")

def error_in_app():
    os.system("shutdown \r \t 1")




restart_button= Button(st, text= "Restart", font=("Times New Roman", 20, 'bold'), relief= RAISED, cursor= "plus", command= restart)
restart_button.place(x=125, y=60, height= 50, width= 250)

restart_with_time_button= Button(st, text= "Restart with time", font=("Times New Roman", 20, 'bold'), relief= RAISED, cursor= "plus", command= restart_with_time)
restart_with_time_button.place(x=125, y=170, height= 50, width= 250)

logout_button= Button(st, text= "Log-Out", font=("Times New Roman", 20, 'bold'), relief= RAISED, cursor= "plus", command= logout)
logout_button.place(x=125, y=270, height= 50, width= 250)

shutdown_button= Button(st, text= "Shut Down", font=("Times New Roman", 20, 'bold'), relief= RAISED, cursor= "plus", command= shutdown)
shutdown_button.place(x=125, y=370,
                      height= 50, width= 250)

st.mainloop()
from tkinter import messagebox, font
from tkinter import *                                                                  # Importing Tkinter model
from PIL import Image, ImageTk                                                         #Allows manipulation of images(crop,resize etc) and also convert images into tkinter format. pil = pillow
import tkinter.messagebox                                                              #Import tkinter messagebox module
import sqlite3                                                                         #Importing sqlit3



def alMart():                                                                          # Defining the main function 1 Usage
    primaryLayout = Tk()                                                               # Creating the main window layout
    primaryLayout.title("Almart Application")                                          # Application title
    primaryLayout.geometry("{0}x{1}+0+0".format(primaryLayout.winfo_screenwidth(), primaryLayout.winfo_screenheight()))
    primaryLayout.overrideredirect(False)                                              # Removing The widow decoration
    primaryLayout.attributes("-fullscreen", True)                                      # Setting The window to fullscreen
    primaryLayout.attributes("-alpha", 1.0)                                            # Setting the background color
    primaryLayout.config(bg="white")                                                   # setting the background color
    primaryLayout.iconbitmap("images/mart-logo.ico")                                   # setting the window icon

    #-------------------All Widgets Functions------------------------------------
    def closeWindows():
        MessageBox = tkinter.messagebox.askquestion("EXIT", "Are you sure you want to exit?",
                                                    icon="warning")
        if MessageBox == "yes":                                                       #if the user clicks yes
            primaryLayout.destroy()                                                   #Destroy the main window
        else:
            MessageBox = tkinter.messagebox.showinfo(" Exit", "You have canceled the exit.",
                                                        icon="info")
            if MessageBox == "ok":                                                   #if the user clicks ok
                primaryLayout.destroy()                                              #Destroy the main window

    #--------------Image Button Hover Function----------------------------
    def changeOnHover(button,colorOnHover,colorOnLeave):                      #Creating a function
            button.bind("<Enter>",func=lambda e: button.config(
                background=colorOnHover                                               #Changing the background color on hover
            ))
            button.bind("<Leave>",func=lambda e: button.config(
                background=colorOnLeave                                               #Changing the background color on leave
            ))
    def minimizeFunction():
        primaryLayout.iconify()



  #----------------------------ALL Form Layout Designs--------------------------------
    controlBox = Frame(primaryLayout,                                                 # creating the control box
                     height=50,                                                       # Height of the frame
                     relief="solid",                                                  # Making Borders Visible
                     bg="white",                                                      # background color of the frame
                     highlightthickness=1,                                            # making the borders visible
                     highlightbackground="#178833")                                   # making the borders visible
    controlBox.pack(side="top",anchor=NE, fill="x")                                   # placing frame in the upper corner

#------------------------------ Inserting Control Images-------------------------------------
    logo = Image.open("images/logo.jpg")                                              #Inserting the logo image
    reSizeLogo = logo.resize((30,30))                                                 # Resizing the logo image
    newLogo = ImageTk.PhotoImage(reSizeLogo)                                          #Assigning image to Object

#----------Inserting image button----------------------
    alMartLogo= Button(controlBox,                                                    #placing image button in control box
                   bg="white",                                                        #Adding background color
                   width="50",                                                        #Adding button width
                   height="50",                                                       #Adding button height
                   image=newLogo,                                                     #Adding image to button
                   border=0,                                                          #Removing border
                   cursor="hand2")                                                    # Adding Cursor
    alMartLogo.image = newLogo                                                        # Assigning Image to Button
    alMartLogo.pack(side="left")                                                      # Placing image button in control box

   #------------------Inserting Control Image-------------------
    closeImage = Image.open("images/close.png")                                       #Inserting the logo image
    reSizeClose = closeImage.resize((30,30))                                          # Resizing the logo image
    NewCloseLogo = ImageTk.PhotoImage(reSizeClose)                                    #Assigning image to Object



    #---------------Inserting Button Images---------------------------#
    closeButton = Button(controlBox,                                                  #Placing image button in control box
                         command=closeWindows,                                        # Creating command --Onclick
                         bg="white",                                                  # Adding background color
                         width="50",                                                  # Adding button width
                         height="50",                                                 # Adding button height
                         image= NewCloseLogo,                                         # Adding Image to the button
                         border=0,                                                    # Adding button border
                         cursor="hand2")                                              # Changing application cursor
    closeButton.image = NewCloseLogo                                                  # Referencing the image
    closeButton.pack(side="right")                                                    #Placing the image to the right
    changeOnHover(closeButton, '#172233', '#FFFFFF')

    # ------------------Inserting Control Image-------------------
    miniImage = Image.open("images/minimize_2.png")                                   #Refreshing  minimize page
    reMiniImage = miniImage.resize((30,30))                                           # Resizing the minimize Image
    newMiniImage =ImageTk.PhotoImage(reMiniImage)                                     # Assigning the image to object


    #-----------------Inserting More Images-----------------------#
    miniButton = Button(controlBox,                                                   #Placing image button in control box
                        command=minimizeFunction,                                     # Creating command --Onclick
                        bg="white",                                                   # Adding background color
                        width="50",                                                   # Adding button width
                        height="50",                                                  # Adding button height
                        image=newMiniImage,                                           # Adding Image to the button
                        border=0,                                                     # Adding button border
                        cursor="hand2")                                               # Changing application cursor
    miniButton.image = newMiniImage                                                   # Referencing the image
    miniButton.pack(side="right")                                                     #Placing the image to the right
    changeOnHover( miniButton,'#172233', '#FFFFFF')           #Adding hover effects

    #---------------------------Creating Image Frame-----------------------
    primaryLayout.update()                                                            #Getting accurate window data
    screen_width = primaryLayout.winfo_screenwidth()                                  #Getting window default width
    screen_height = primaryLayout.winfo_screenheight()                                #Getting window default height

    #--------------Creating Frames----------------------------------
    LeftBackgroundFrame = Frame(primaryLayout,                                        #Placing the frame to the root layout
                                width=screen_width // 2,                              #Adjusting width to get equal half
                                height=screen_height,                                 #Adding frame height
                                bg="black",                                           #Adding background color
                                highlightthickness=0,                                 #Creating border thickness
                                highlightbackground="white",)                         #Setting border color
    LeftBackgroundFrame.pack(side="left")                                             #Placing the frame to the left

    #-----Placing background Image---------------------------------
    bg_image = Image.open("images/background9.png")                                   #Referencing the image
    desire_width = screen_width // 2                                                  #Resizing the image width
    desire_height = screen_height                                                     #Resizing the image height
    bg_image =bg_image.resize((desire_width,desire_height))                           #Referencing the new image
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(LeftBackgroundFrame, image=bg_photo, bg="white")                 #creating a label to hold bg image
    bg_label.image = bg_photo                                                         #Referencing new image to label

    #--------------Calculating the coordinates to the center image----------
    x_center = (screen_width // 2 - desire_width) // 2                                #Position for the center for x
    y_center = (screen_height - desire_height)  // 4                                  #Position for the center for y
    bg_label.place(x=x_center, y=y_center)                                            #Placing image into frame


    def loginLayout():
        UsernameEntry = None
        PasswordEntry = None
        EyeImage = None
        RightFrame = None
        NewResizeEye = None
        NewResizeEyeShowEye = None

        # ----------UsernameEntry placeholder function--------
        def UsernameEntry_Enter(*args):                                                 # Creating a function
            if UsernameEntry.get() == "Username":                                       # checking all text in entry
                UsernameEntry.delete(0, "end")                            # Erases all text in entry
                UsernameEntry.config(foreground="#DAA520")                              # Setting text color

        def UsernameEntry_Leave(*args):                                                 # Creating a function
            if len(UsernameEntry.get()) == 0:                                           # Checking if entry box is empty
                UsernameEntry.insert(0, "Username")                                     # Placing back username text
                primaryLayout.focus()                                                   # Focusing on the function
                UsernameEntry.config(foreground="#2F2F2F")                              # Setting text color

        # -------------------------PasswordEntry PlaceholderFunction----------------
        def PasswordEntry_Enter(*args):                                                 # Creating a function
            if PasswordEntry.get() == "Password":                                       # Checking if Entry box is empty
                PasswordEntry.config(show="*", fg="#DAA520")                            # Adding Password and fore color
                PasswordEntry.delete(0, "end")                            # Erasing all text in entry field
                EyeImage.place(x=desire_width // 1.6, y=desire_height // 2.55)          # placing eye image

        def PasswordEntry_Leave(*args):                                                 # Creating a function
            if len(PasswordEntry.get()) == 0:                                           # Checking if entry box is empty
                PasswordEntry.config(show="", fg="#2F2F2F")                             # removing inPassword and fore color
                PasswordEntry.insert(0, "Password")                                     # Placing back password text
                primaryLayout.focus()                                                   # Placing focus on layout root
                EyeImage.place(x=10000, y=10000)                                        # Taking the eye image out of the frame

        # ---------------------Show & hide text------------------------------
        def show_hide_Password():                                                       # creating a function
            if PasswordEntry["show"] == "*":                                            # Check if password entry is masked
                PasswordEntry.configure(show="")                                        # reveal password
                EyeImage.config(image=NewResizeEye)                                     # Assigning invisible eye image
                EyeImage.image = NewResizeEye
            else:
                PasswordEntry.config(show="*")                                          # mask password
                EyeImage.config(image=NewResizeEyeShowEye)                              # Assigning visible eye image
                EyeImage.image = NewResizeEyeShowEye

        def signupSwitch(*args):                                                        # Creating a function
            nonlocal RightFrame, UsernameEntry, PasswordEntry, EyeImage, NewResizeEye, NewResizeEyeShowEye
            try:
                RightFrame.destroy()
            except:
                pass

            RightFrame = Frame(primaryLayout,                                             # Placing frame to the right frame
                               width=screen_width // 2,                                   #Adding screen width
                               height=screen_height,                                      #Adding screen height
                               bg="white",                                                #Adding background color
                               highlightthickness=0,                                      #Creating border thickness
                               highlightbackground="white", )                             #Setting border color
            RightFrame.pack(side=RIGHT)                                                   # Placing frame to the right

            logLabl = Label(RightFrame,                                                   # placing label into the right frame
                            text="Welcome",                                               # Adding label text
                            font=("Times New Roman", 35, "bold"),                         # Setting Font & size
                            foreground="#E8221f",                                         # Setting Font color
                            bg="white")                                                   # Setting background color
            logLabl.place(x=desire_width // 3.1, y=desire_height // 4.5)                  # Placing label to the right frame

            InLabel = Label(RightFrame,                                                   # Placing label into the right frame
                            text="Back",                                                  # Adding label text
                            font=("Times New Roman", 35, "bold"),                         # Setting font & size
                            background="white",                                           # Adding text color
                            foreground="#2F2F2F")                                         # Adding background color
            InLabel.place(x=desire_width // 1.9, y=desire_height // 4.5)                  # Placing label to the right frame

            welcomeText = Label(RightFrame,                                               #label into the right frame
                                text="Please access your account and have access to",     # Adding label text
                                font=("Times New Roman", 13),                             # Setting font & size
                                foreground="#2F2F2F",                                     # Adding text color
                                background="white")                                       # Adding background color
            welcomeText.place(x=desire_width // 2.95, y=desire_height // 3.5)             # Placing label to the right frame

            welcomeText2 = Label(RightFrame,                                              # Placing label into the right frame
                                 text="exclusive shopping experience",                    # Adding label text
                                 font=("Times New Roman", 13),                            # Setting font & size
                                 foreground="#2F2F2F",                                    # Adding text color
                                 background="white")                                      # Adding background color
            welcomeText2.place(x=desire_width // 2.95, y=desire_height // 3.3)            # Placing label to the right frame

            # -------------------------------Creating Entry fields----------------------- #Entry Fields
            UsernameEntry = Entry(RightFrame,                                             # Adding Entry to the right frame
                                  relief="solid",                                         # Making the border visible
                                  font=("Cambria", 12),                                   # setting font & size
                                  background="white",                                     # Adding background color
                                  foreground="#2F2F2F",                                   # Adding font color
                                  highlightthickness=1,                                   # Adding border
                                  highlightbackground="gray")                             # Adding border colors
            UsernameEntry.insert(0, "Username")                               # Adding text to Entry
            UsernameEntry.place(x=desire_width // 2.95, y=desire_height // 3, width=400, height=50)
            UsernameEntry.bind("<FocusIn>", UsernameEntry_Enter)                          # Adding focus in event
            UsernameEntry.bind("<FocusOut>", UsernameEntry_Leave)                         # Adding focus out event

            PasswordEntry = Entry(RightFrame,                                             # Adding Entry to the right frame
                                  relief="solid",                                         # Making the border visible
                                  font=("Cambria", 12),                                   # Setting font & size
                                  background="white",                                     # Adding background color
                                  foreground="#2F2F2F",                                   # Adding font color
                                  highlightthickness=1,                                   # Adding border
                                  highlightbackground="gray")                             # Adding border colors
            PasswordEntry.insert(0, "Password")
            PasswordEntry.place(x=desire_width // 2.95, y=desire_height / 2.6, width=400, height=50)
            PasswordEntry.bind("<FocusIn>", PasswordEntry_Enter)                          # Adding focus in event
            PasswordEntry.bind("<FocusOut>", PasswordEntry_Leave)                         # Adding focus out event

            # ---------------------------Adding Eye Button--------------------------------------
            HideEye = Image.open("images/invisible_eye.png")                              # Referencing Invisible Image
            ResizeEye = HideEye.resize((25, 25))                                          # Resizing Image
            NewResizeEye = ImageTk.PhotoImage(ResizeEye)                                  # Assigning Image

            ShowEye = Image.open("images/visible_eye.png")                                # Referencing Visible Image
            ResizeEye = ShowEye.resize((25, 25))                                          # Resizing Image
            NewResizeEyeShowEye = ImageTk.PhotoImage(ResizeEye)                           # Assigning Image

            # ---------------------Adding Eye Image to the Entry Fields----------------------
            EyeImage = Button(RightFrame,                                                 # Placing Button to the right frame
                              image=NewResizeEyeShowEye,                                  # Assigning image to button
                              command=show_hide_Password,                                 # Adding command
                              fg="gray",                                                  # Assigning color to the button
                              bg="white",                                                 # Assigning background color
                              border=0,                                                   # Removing border
                              cursor="hand2", )                                           # assigning cursor
            EyeImage.image = NewResizeEyeShowEye                                          # Assigning Image

            # -------------------Adding forgot label--------------------------------------
            forgotPassword = Label(RightFrame,                                            # Placing label to the right frame
                                   text="Forgot password?",                               # Adding text to label
                                   font=("Times New Roman", 12),                          # Adding font & size
                                   fg="gray",                                             # Adding font color
                                   bg="white",                                            # Adding background color
                                   cursor="hand2", )                                      # Adding a hand cursor
            forgotPassword.place(x=desire_width // 2.95, y=desire_height // 2.25)         # Placing label to the right frame

            # --------------------------------------Adding Login Button---------------------
            loginButton = Button(RightFrame,                                              # placing login Button
                                 text="Log In",                                           # Adding a button tex
                                 command=(),                                              # Adding command
                                 font=("Times New Roman", 12),                            # Setting font family & size
                                 width="44",                                              # Adding button width
                                 height="2",                                              # Adding button height
                                 border=0,                                                # Adding border
                                 cursor="hand2",                                          # Changing button cursor
                                 background="#E8221f",                                    # Adding background color
                                 foreground="white")                                      # Adding text color
            loginButton.place(x=desire_width // 2.95, y=desire_height // 2.1)             # Placing login button to the right frame

            # -----------Adding Label-------------------------------------
            notMember = Label(RightFrame,                                                 # Placing label in the right frame
                              text="New Here?",                                           # Adding text to label
                              font=("Cambria", 12),                                       # Setting font size
                              foreground="#2F2F2F",                                       # Adding a text color
                              background="white")                                         # Adding background color
            notMember.place(x=desire_width // 2.5, y=desire_height // 1.15)               # Placing the label

            # --------------Adding SignUp Button------------------------------
            signupButton = Button(RightFrame,                                             # Placing the signup button in the right frame
                                  text="Create Account",                                  # Adding text to button
                                  command=(),                                             # Adding function to files
                                  width="20",                                             # Adding button width
                                  height="2",                                             # Adding button height
                                  border=0,                                               # Adding border
                                  cursor="hand2",                                         # Changing cursor
                                  background="#172233",                                   # Adding background color
                                  foreground="white")                                     # Adding text color
            signupButton.place(x=desire_width // 2, y=desire_height // 1.16)              # Placing the button to the right frame

        signupSwitch()                                                                    # Calling the signup function

    loginLayout()                                                                         # calling the login function


alMart()                                                                                  # Calling the main function
mainloop()                                                                                # main loop to keep windows running

from tkinter import *  # Importing Tkinter model
from PIL import Image, \
    ImageTk  # allows manipulation of images ( crop,resize etc.) and also convert images into tkinter format. pil= pillow
import tkinter.messagebox  # Import tkinter messagebox module
import sqlite3  # importing sqlite3 for database


def alMart():  # Defining the main function 1 Usage
    primaryLayout = Tk()  # Creating the main window layout
    primaryLayout.title("Almart Application")  # Application title
    primaryLayout.geometry("{0}x{1}+0+0".format(primaryLayout.winfo_screenwidth(), primaryLayout.winfo_screenheight()))
    primaryLayout.overrideredirect(False)  # Removing The widow decoration
    primaryLayout.attributes("-fullscreen", True)  # Setting The window to fullscreen
    primaryLayout.attributes("-alpha", 1.0)  # Setting the background color
    primaryLayout.config(bg="white")  # setting the background color
    primaryLayout.iconbitmap("images/mart-logo.ico")  # setting the window icon

    # -------------------------- ALL Widgets functions----------------------------------
    def closeWindows():
        MessageBox = tkinter.messagebox.askquestion("EXIT",
                                                    "Are you sure you want to exit?",
                                                    icon="warning")
        if MessageBox == "yes":  # if the user clicks yes
            primaryLayout.destroy()  # Destroy the main window
        else:
            MessageBox = tkinter.messagebox.askquestion("Cancel Exit",
                                                        "You have canceled the exit.",
                                                        icon="info")
            if MessageBox == "ok": pass

    def minimizeFunction():  # defining the minimize button
        primaryLayout.iconify()  # minimizing the minimize button

    # -----------------------Image button Hover Function------------------------#
    def changeOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover
        ))
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave
        ))

    # ----------------------------ALL Form Layout Designs--------------------------------
    controlBox = Frame(primaryLayout,  # creating the control box
                       height=50,  # Height of the frame
                       relief="solid",  # Making Borders Visible
                       bg="white",  # background color of the frame
                       highlightthickness=1,  # making the borders visible
                       highlightbackground="#178833")  # making the borders visible
    controlBox.pack(side="top", anchor=NE, fill="x")  # placing frame in the upper corner

    # ------------------------------ Inserting Control Images-------------------------------------
    logo = Image.open("images/logo.jpg")  # Inserting the logo image
    reSizeLogo = logo.resize((30, 30))  # Resizing the logo image
    newLogo = ImageTk.PhotoImage(reSizeLogo)  # Assigning image to Object

    # -----------------------Inserting image button--------------------
    alMartLogo = Button(controlBox,  # placing image button in control box
                        bg="white",  # Adding background color
                        width=50,  # Adding button width
                        height=50,  # Adding button height
                        image=newLogo,  # Adding image to button
                        border=0,  # Removing border
                        cursor="hand2")  # Adding Cursor
    alMartLogo.image = newLogo  # Assigning Image to Button
    alMartLogo.pack(side="left")  # Placing image button in control box

    # ------------------Inserting Control Image-------------------
    closeImage = Image.open("images/close.png")  # Inserting the logo image
    reSizeClose = closeImage.resize((30, 30))  # Resizing the logo image
    NewCloseLogo = ImageTk.PhotoImage(reSizeClose)  # Assigning image to Object

    # ---------------Inserting Button Images---------------------------#
    closeButton = Button(controlBox,  # Placing image button in control box
                         command=closeWindows,  # Creating command --Onclick
                         bg="white",  # Adding background color
                         width=50,  # Adding button width
                         height=50,  # Adding button height
                         image=NewCloseLogo,  # Adding Image to the button
                         border=0,  # Adding button border
                         cursor="hand2")  # Changing application cursor
    closeButton.image = NewCloseLogo  # Referencing the image
    closeButton.pack(side="right")  # Placing the image to the right
    changeOnHover(closeButton, '#172233', '#FFFFFF')  # Adding hover effects

    # ------------------Inserting Control Image-------------------
    miniImage = Image.open("images/minimize_2.png")  # Refreshing the minimize page
    reMiniImage = miniImage.resize((30, 30))  # Resizing the minimize Image
    newMiniImage = ImageTk.PhotoImage(reMiniImage)  # Assigning the image to object

    # -----------------Inserting More Images-----------------------#
    miniButton = Button(controlBox,  # Placing image button in control box
                        command=minimizeFunction,  # Creating command --Onclick
                        bg="white",  # Adding background color
                        width=50,  # Adding button width
                        height=50,  # Adding button height
                        image=newMiniImage,  # Adding Image to the button
                        border=0,  # Adding button border
                        cursor="hand2")  # Changing application cursor
    miniButton.image = newMiniImage  # Referencing the image
    miniButton.pack(side="right")  # Placing the image to the right
    changeOnHover(miniButton, '#172233', '#FFFFFF')  # Adding hover effects

    # ----------------------creating Image Frame-------------------------------------------------
    primaryLayout.update()  # Getting accurate window data
    screen_width = primaryLayout.winfo_screenwidth()  # Getting window default width
    screen_height = primaryLayout.winfo_screenheight()  # Getting windows default height

    # ----------------Creating Frames-----------------------------#
    LeftBackgroundFrame = Frame(primaryLayout,  # Placing the frame to the root layout
                                width=screen_width // 2,  # Adjusting width to get equal half
                                height=screen_height,  # Adding frame height
                                bg="black",  # Adding background color
                                highlightthickness=0,  # Creating border thickness
                                highlightbackground="white")  # setting border color
    LeftBackgroundFrame.pack(side="left")  # placing the frame to the left

    # placing background image---------------------------------------#
    bg_image = Image.open("images/background9.png")  # Referencing the image
    desire_width = screen_width // 2  # Resizing the image width
    desire_height = screen_height  # Resizing the image height
    bg_image = bg_image.resize((desire_width, desire_height))  # New resized image
    bg_photo = ImageTk.PhotoImage(bg_image)  # Referencing the new image

    bg_label = Label(LeftBackgroundFrame, image=bg_photo, bg="white")  # creating a label to hold bg image
    bg_label.image = bg_photo  # Referencing new image to label

    # --------------------calculating the coordinates to the center image-------------------
    x_center = (screen_width // 2 - desire_width) // 2  # Position for the center for X
    y_center = (screen_height - desire_height) // 4  # Position for the center for y

    bg_label.place(x=x_center, y=y_center)  # placing image into frame

    # ---------------- creating login Form ---------------------------------- #
    def loginLayout():
        # ---------------Username Entry Place holder function
        def UsernameEntry_Enter(*args):  # creating function
            if UsernameEntry.get() == "Username":  # checking all text in entry
                UsernameEntry.delete(0, "end")  # Erase all text entry
                UsernameEntry.config(foreground="#DAA520")  # Setting text color
            else:
                pass

        def UsernameEntry_Leave(*args):  # creating a function
            if len(UsernameEntry.get()) == 0:  # checking if the box is
                UsernameEntry.insert(0, "Username")  # Placing back username text
                primaryLayout.focus()  # focusing on the root layout
                UsernameEntry.config(foreground="#2F2F2F")  # Setting TextColor

                # ---------------------PasswordEntry Placeholder function

        def PasswordEntry_Enter(*args):  # creating a function
            if PasswordEntry.get() == "Password":  # Checking if Entry box is Empty
                PasswordEntry.config(show="*", fg="#DAA520")  # adding is-password and fore color
                PasswordEntry.delete(0, "end")  # Erasing all text in entry field
                EyeImage.place(x=desire_width // 1.4, y=desire_height // 2.55)  # Placing eye image
            else:
                pass

        def PasswordEntry_Leave(*args):  # Adding a function
            if len(PasswordEntry.get()) == 0:  # checking if entry box is empty
                PasswordEntry.config(show="*", fg="#2F2F2F")  # Removing isPassword and forecolor
                PasswordEntry.insert(0, "Password")  # Placing back the password
                primaryLayout.focus()  # placing focus on layout root
                EyeImage.place(x=10000, y=10000)  # Taking the eye image out of frame

                # ------------------Show & Hide Password text-------------------

        def show_hide_Password():  # Creating a function
            if PasswordEntry["show"] == "*":  # Check if password entry is is-password
                PasswordEntry.config(show="")  # Change password entry
                EyeImage.config(image=NewResizeEye)  # Swapping eye image
                EyeImage.image = NewResizeEye

            else:
                PasswordEntry.config(show="*")  # Turn on is-password for entry field
                EyeImage.config(image=NewResizeShowEye)  # Swapping eye image
                EyeImage.image = NewResizeShowEye  # Assigning new swapped images

        # ------Forgot password Underline Function
        def underlinePassword(event):  # creating a function
            event.widget.config(font=("Cambria", 13, "underline"))  # Adding underline effect
            event.widget.config(fg="#172233")  # changing text color label

        def underlinePassword_Remove(event):  # creating a function
            event.widget.config(font=("Cambria", 12))  # removing the underline effect
            event.widget.config(fg="grey")

        # --------------------Login button Hover function
        def LoginHover(button, colorOnHover, colorOnLeave):  # Creating a function
            button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
            button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

        def signupSwitch(*args):
            RightFrame.destroy()

        RightFrame = Frame(primaryLayout,  # Placing frame to the rootLayout
                           width=screen_width // 2,  # Adjusting width to get equal half
                           height=screen_height,  # Adjusting height to get equal half
                           bg="white",  # Adding background color
                           highlightthickness=0,  # Crating border thickness
                           highlightbackground="white")  # Setting Border color
        RightFrame.pack(side=RIGHT)  # Placing frame to the right

        logLabl = Label(RightFrame,  # Placing label into the right frame
                        text="Welcome",  # Adding label text
                        font=("Times New Roman", 35, "bold"),  # Setting font & Size
                        foreground="#E8221F",  # Setting font color
                        bg="white")  # setting background color
        logLabl.place(x=desire_width // 3.2, y=desire_height // 4.5)  # Placing label to the right frame
        InLabel = Label(RightFrame,  # Placing label into the right frame
                        text="Back,",  # Adding label text
                        font=("Times New Roman", 35, "bold"),  # Setting font & Size
                        foreground="#2f2f2f",  # adding text color
                        background="white")  # adding background color
        InLabel.place(x=desire_width // 1.95, y=desire_height // 4.5)  # Placing the label

        welcomeText = Label(RightFrame,  # Placing label into right frame
                            text="Please access your account and have access to",  # Adding label text
                            font=("Times New Roman", 13),  # setting font & size
                            foreground="#2f2f2f",  # Adding text color
                            background="white")  # Adding background color
        welcomeText.place(x=desire_width // 2.95, y=desire_height // 3.5)

        welcomeText2 = Label(RightFrame,  # Placing label into right frame
                             text="exclusive shopping experience.",  # Adding label text
                             font=("Times New Roman", 13),  # setting font & size
                             foreground="#2f2f2f",  # Adding text color
                             background="white")  # Adding background color
        welcomeText2.place(x=desire_width // 2.95, y=desire_height // 3.3)

        # ----------------- creating entry fields -------------------------------   # Entry fields
        UsernameEntry = Entry(RightFrame,  # Adding Entry to the right frame
                              relief="solid",  # Making the border visible
                              font=("Cambria", 12),  # Setting font & size
                              background="white",  # Adding background color
                              foreground="#2f2f2f",  # Adding fore color
                              highlightthickness=1,  # Adding border
                              highlightbackground="gray")  # Adding border colors
        UsernameEntry.insert(0, "Username")  # Adding text entry
        UsernameEntry.place(x=desire_width // 2.95, y=desire_height // 3, width=400, height=50)
        UsernameEntry.bind("<FocusIn>", UsernameEntry_Enter)  # Adding FocusIn event
        UsernameEntry.bind("<Leave>", UsernameEntry_Leave)  # Adding FocusOut event

        PasswordEntry = Entry(RightFrame,  # Adding entry to right frame
                              relief="solid",  # Making the border visible
                              font=("Cambria", 12),  # Setting font & size
                              background="white",  # Adding background color
                              foreground="#2f2f2f",  # Adding fore color
                              highlightthickness=1,  # Adding border
                              highlightbackground="gray")  # Adding border colors
        PasswordEntry.insert(0, "Password")  # Adding text entry
        PasswordEntry.place(x=desire_width // 2.95, y=desire_height // 2.6, width=400, height=50)
        PasswordEntry.bind("<FocusIn>", PasswordEntry_Enter)
        PasswordEntry.bind("<FocusOut>", PasswordEntry_Leave)

        # ----------------Adding Eye button-------------------------
        HideEye = Image.open("images/invisible_eye.png")  # referencing invincible image
        ResizeEye = HideEye.resize((25, 25))  # Resizing images
        NewResizeEye = ImageTk.PhotoImage(HideEye)  # Assigning Images

        ShowEye = Image.open("images/visible_eye.png")  # referencing Visible image
        ResizeEye = ShowEye.resize((25, 25))  # Resizing images
        NewResizeShowEye = ImageTk.PhotoImage(ResizeEye)  # Assigning Images

        # ------- Adding Eye Image TO Field-----------------------#
        EyeImage = Label(RightFrame,  # Placing the label in the right frame
                         image=NewResizeShowEye,  # Assigning the image to label
                         fg="grey",  # Assigning color to label
                         bg="white",  # Assigning background color
                         cursor="hand2")  # Assigning cursor to label
        EyeImage.image = NewResizeShowEye  # Assigning image
        EyeImage.bind("<Button-1>", lambda e: show_hide_Password())  #binding function to eye function

        # ------------------ Adding Forgot Label
        forgotPassword = Label(RightFrame,  # Placing label in the right frame
                               text="Forgot Password?",  # Adding tex to label
                               font=("Times New Roman", 13),  # Adding font and size
                               fg="gray",  # Adding fore color
                               bg="white",  # Adding background color
                               cursor="hand2")  # Adding cursor
        forgotPassword.place(x=desire_width // 2.95, y=desire_height // 2.25)
        forgotPassword.bind("<Button-1>", lambda e: underlinePassword)
        forgotPassword.bind("<Button-1>", lambda e: underlinePassword_Remove)

        # ----------------Adding login button--------------------#
        loginButton = Button(RightFrame,  # Placing the login button
                             text="Log In",  # Adding a button text
                             command=(),  # Adding command
                             width=57,  # Adding button width
                             height=2,  # Adding button height
                             border=0,  # Adding borders
                             cursor="hand2",  # Changing button cursor
                             background="#E8221F",  # Adding background color
                             foreground="white")  # Adding text Color
        loginButton.place(x=desire_width // 2.95, y=desire_height // 2.1)
        LoginHover(loginButton, "#2F2F2F", "#E82217")


        # Adding label
        notMember = Label(RightFrame,  # Placing label in right frame
                          text="New Here?",  # Adding text label
                          font=("Cambria", 12),  # Setting the font size
                          foreground="#2F2F2F",  # Adding text color
                          background="white")  # Adding Background color

        notMember.place(x=desire_width // 2.5, y=desire_height // 1.15)

        # -------Adding Signup button-------------#
        signupButton = Button(RightFrame,                  #Placing label in the right frame
                              text="Create Account",           # Adding text to label
                              command=(),                      # Adding function to file
                              width=20,
                              height=2,
                              border=0,
                              cursor="hand2",
                              background="#172233",
                              foreground="white")
        signupButton.place(x=desire_width // 2, y=desire_height // 1.16)


    loginLayout()


alMart()               # Calling the main function
mainloop()             # main loop to keep windows running
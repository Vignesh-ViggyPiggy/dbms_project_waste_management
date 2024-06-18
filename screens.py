from customtkinter import *
from PIL import Image
import functions



app = CTk()
app.geometry("1000x580")
app.resizable(0,0)



login_bg_data = Image.open("Images\\login_bg.png")


logo_data = Image.open("Images\\logo.png")
registration_logo_data = Image.open("Images\\register_logo.png")



def forgot_password_screen():
    frame = CTkFrame(app,width=1000,height=580,bg_color="#D6DAA8")
    frame.place(x=0,y=0)   
    bg_image = CTkImage(dark_image=login_bg_data,light_image=login_bg_data,size=(1000,580))
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button.png"),light_image=Image.open("Images\\reset_button.png"), size=(20,20))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    forgot_password_logo = CTkImage(dark_image=Image.open("Images\\forgot_password.png"),light_image=Image.open("Images\\forgot_password.png"),size=(400,100))
    CTkLabel(master=frame, text="", image=forgot_password_logo).place(x=575,y=30)
    CTkLabel(master=frame,text="   Enter Details:",font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#D6DAA8",text_color="black").place(x=640,y=130)
    username_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="Username")
    username_entry.place(x=650,y=180)
    CTkLabel(master=frame,text="   Select Security Question:",font=("Arial Bold", 14),anchor="w", justify="left",compound="left",bg_color="#D6DAA8",text_color="black").place(x=640,y=230)
    question_options = ["mother's name?","father's name?","sibling's name?"]
    question_selector = CTkOptionMenu(master=frame,values=question_options,bg_color="#D6DAA8",fg_color="#EEEEEE",text_color="#000000",button_color="#718958")
    question_selector.place(x=650,y=270)
    answer_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="Answer")
    answer_entry.place(x=650,y=310) 
    password_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="New Password",show="*")
    password_entry.place(x=650,y=380)
    CTkButton(master=frame, text="BACK", fg_color="#718958", hover_color="#829A6E", font=("Arial Bold", 16), text_color="#D6DAA8", width=100,height=50,command=login_screen,bg_color="#D6DAA8").place(x=655,y=450)
    CTkButton(master=frame, text="SUBMIT", fg_color="#718958", hover_color="#829A6E", font=("Arial Bold", 16), text_color="#D6DAA8", width=100,height=50,command=lambda:functions.forgot_password_changer(username_entry.get(),(question_options.index(question_selector.get())+1),answer_entry.get(),password_entry.get()),bg_color="#D6DAA8").place(x=795,y=450)
    CTkButton(master=frame,text="",image=reset_button_image,command=forgot_password_screen,width=20,fg_color="#D6DAA8",hover_color="#D6DAA8",bg_color="#D6DAA8").place(x=575,y=525)

def garbage_collection_screen(username):
    collection_list = functions.collection_list(username)
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFCCC4")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\worker_bg.jpg"),light_image=Image.open("Images\\worker_bg.jpg"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    collect_garbage_logo = CTkImage(dark_image=Image.open("Images\\collect_garbage_logo.png"),light_image=Image.open("Images\\collect_garbage_logo.png"),size=(300,60))
    CTkLabel(master=frame, text="", image=collect_garbage_logo).place(x=565,y=40)
    scroll_frame = CTkScrollableFrame(master=frame,bg_color="#FFCCC4",label_text="  NAME       GARBAGE AMOUNT",label_anchor="w",label_font=("Arial Bold", 14),label_fg_color="#812137",label_text_color="#FFCCC4",scrollbar_button_color="#812137",scrollbar_button_hover_color="#E73960",fg_color="#FC9686",scrollbar_fg_color="#FC9686",width=420,height=300)
    scroll_frame.place(x=500,y=150)
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button_worker.png"),light_image=Image.open("Images\\reset_button_worker.png"), size=(20,20))
    CTkButton(master=frame,text="",image=reset_button_image,command=lambda:garbage_collection_screen(username),width=20,fg_color="#FFCCC4",hover_color="#FFCCC4",bg_color="#FFCCC4").place(x=475,y=520)
    for collection_index in range(len(collection_list)):
        collection_label = CTkLabel(master=scroll_frame,text=collection_list[collection_index][0],text_color="#812137",bg_color="#FC9686",fg_color="#FC9686",font=("Arial Bold", 14))
        add_button = CTkButton(master=scroll_frame,text="COLLECT",fg_color="#812137",font=("Arial Bold", 13),hover_color="#E73960",width=10 ,text_color="#FFCCC4",command=lambda k=collection_index:functions.accept_collection(username,collection_list[k][0],collection_list[k][1]),bg_color="#FC9686")
        collection_amount = CTkLabel(master=scroll_frame,text=collection_list[collection_index][1],text_color="#812137",bg_color="#FC9686",fg_color="#FC9686",font=("Arial", 14))
        report_button = CTkButton(master=scroll_frame,text="REPORT",fg_color="#812137",font=("Arial Bold", 13),hover_color="#E73960",width=10 ,text_color="#FFCCC4",command=lambda:report_screen(username,collection_list[collection_index][0]) ,bg_color="#FC9686")
        
        collection_label.grid(row=collection_index,column=0,padx=20,pady=15 )
        collection_amount.grid(row=collection_index,column=1,padx=70,pady=15 )
        add_button.grid(row=collection_index,column=2,padx=15,pady=15 )
        report_button.grid(row=collection_index,column=3,padx=0,pady=15)
    CTkButton(master=frame, text="BACK" ,fg_color="#812137", font=("Arial Bold", 11),hover_color="#E73960",width=10 ,text_color="#FFCCC4",command=lambda:worker_screen(username),bg_color="#FFCCC4").place(x=857,y=516)

def about_worker_screen(username):
    about_worker = functions.about_worker(username)[0]
    frame = CTkFrame(app,width=1000,height=580,bg_color="#D2D7F7")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\client_bg.png"),light_image=Image.open("Images\\client_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    assigned_worker_logo = CTkImage(dark_image=Image.open("Images\\assigned_worker_logo.png"),light_image=Image.open("Images\\assigned_worker_logo.png"),size=(450,75))
    CTkLabel(master=frame, text="", image=assigned_worker_logo).place(x=485,y=40)
    CTkLabel(master=frame,text="Worker Username:   {a}".format(a=about_worker[0]),font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#D2D7F7",text_color="black").place(x=600,y=150)
    CTkLabel(master=frame,text="Worker Email:      {a}".format(a=about_worker[1]),font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#D2D7F7",text_color="black").place(x=600,y=220)
    CTkLabel(master=frame,text="Worker Phone:      {a}".format(a=about_worker[2]),font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#D2D7F7",text_color="black").place(x=600,y=290)
    CTkLabel(master=frame,text="Worker Address:    {a}".format(a=about_worker[3]),font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#D2D7F7",text_color="black").place(x=600,y=360)
    CTkButton(master=frame, text="BACK" ,fg_color="#484B5E", font=("Arial Bold", 13),hover_color="#737898",width=100 ,text_color="#D2D7F7",command=lambda:client_screen(username),bg_color="#D2D7F7").place(x=750,y=470)
    CTkButton(master=frame, text="REPORT" ,fg_color="#484B5E", font=("Arial Bold", 13),hover_color="#737898",width=100 ,text_color="#D2D7F7",command=lambda:report_screen(username,about_worker[0]),bg_color="#D2D7F7").place(x=575,y=470)
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button_client.png"),light_image=Image.open("Images\\reset_button_client.png"), size=(20,20))
    CTkButton(master=frame,text="",image=reset_button_image,command=lambda:about_worker_screen(username),width=20,fg_color="#D2D7F7",hover_color="#D2D7F7",bg_color="#D2D7F7").place(x=465,y=520)
def report_screen(attack_username,defend_username):
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFF98B")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\admin_bg.png"),light_image=Image.open("Images\\admin_bg.png"), size=(1000,580))
    
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    reports_logo = CTkImage(dark_image=Image.open("Images\\reports_logo.png"),light_image=Image.open("Images\\reports_logo.png"),size=(200,67))
    CTkLabel(master=frame, text="", image=reports_logo).place(x=550,y=40)
    CTkButton(master=frame, text="BACK" ,fg_color="#60622F", font=("Arial Bold", 13),hover_color="#A0A352",width=100,height=25 ,text_color="#FFF98B",command=lambda:functions.home_screen_caller_util(attack_username),bg_color="#FFF98B").place(x=747,y=507)
    
    CTkLabel(master=frame,text="   Username:    {a}".format(a=defend_username),font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#FFF98B",text_color="black").place(x=390,y=105)
    CTkLabel(master=frame,text="   Complaint about user:   ",font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#FFF98B",text_color="black").place(x=390,y=135)
    report_entry = CTkTextbox(master=frame, width=550, height=300,bg_color="#FFF98B",text_color="black" ,fg_color="white")
    report_entry.place(x=390,y=180) 
    CTkButton(master=frame, text="SUBMIT" ,fg_color="#60622F", font=("Arial Bold", 13),hover_color="#A0A352",width=100,height=25  ,text_color="#FFF98B",command=lambda:functions.report_submit(attack_username,defend_username,report_entry.get(1.0,END)),bg_color="#FFF98B").place(x=487,y=507)

def view_report_screen(username,reported_username,reporting_username):
    view_report = functions.view_report(reporting_username,reported_username)
   
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFF98B")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\admin_bg.png"),light_image=Image.open("Images\\admin_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    CTkButton(master=frame, text="BACK" ,fg_color="#60622F", font=("Arial Bold", 11),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda:admin_screen(username),bg_color="#FFF98B").place(x=837,y=516)
    CTkButton(master=frame, text="ACCEPT" ,fg_color="#60622F", font=("Arial Bold", 11),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda:functions.accept_report(username,reported_username,reporting_username),bg_color="#FFF98B").place(x=437,y=516)
    CTkButton(master=frame, text="EXCUSE" ,fg_color="#60622F", font=("Arial Bold", 11),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda:functions.excuse_report(username,reported_username,reporting_username),bg_color="#FFF98B").place(x=637,y=516)
    CTkLabel(master=frame, text="REPORTED USER: {a}".format(a=reported_username),font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#FFF98B",text_color="black").place(x=390,y=150)
    CTkLabel(master=frame, text="REPORTING USER: {a}".format(a=reporting_username),font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#FFF98B",text_color="black").place(x=690,y=150)
    CTkLabel(master=frame, text="CONTENT:",font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#FFF98B",text_color="black").place(x=390,y=200)
    CTkLabel(master=frame, text="{a}".format(a=view_report[0][2]),font=("Arial", 11),anchor="w", justify="left",compound="left",bg_color="white",text_color="black",width=550, height=220).place(x=385,y=240)

def report_list_screen(username):
    reports_list = functions.reports_list()
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFF98B")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\admin_bg.png"),light_image=Image.open("Images\\admin_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    reports_logo = CTkImage(dark_image=Image.open("Images\\reports_logo.png"),light_image=Image.open("Images\\reports_logo.png"),size=(300,100))
    CTkLabel(master=frame, text="", image=reports_logo).place(x=515,y=40)
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button_admin.png"),light_image=Image.open("Images\\reset_button_admin.png"), size=(20,20))
    CTkButton(master=frame,text="",image=reset_button_image,command=lambda:report_list_screen(username),width=20,fg_color="#FFF98B",hover_color="#FFF98B",bg_color="#FFF98B").place(x=365,y=510)
    scroll_frame = CTkScrollableFrame(master=frame,bg_color="#FFF98B",label_text="  ACCOUNT_REPORTED          ACCOUNT_REPORTING",label_anchor="w",label_font=("Arial Bold", 14),label_fg_color="#60622F",label_text_color="#FFF98B",scrollbar_button_color="#60622F",scrollbar_button_hover_color="#A0A352",fg_color="#B1AB4C",scrollbar_fg_color="#B1AB4C",width=500,height=300)
    scroll_frame.place(x=400,y=150)
    
    CTkButton(master=frame, text="BACK" ,fg_color="#60622F", font=("Arial Bold", 11),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda:admin_screen(username),bg_color="#FFF98B").place(x=857,y=516)
    for report_index in range(len(reports_list)):
        reported_name = CTkLabel(master=scroll_frame,text=reports_list[report_index][0],text_color="#FFF98B",bg_color="#B1AB4C",fg_color="#B1AB4C",font=("Arial Bold", 14))
        view_button = CTkButton(master=scroll_frame,text="VIEW",fg_color="#60622F",font=("Arial Bold", 13),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda:view_report_screen(username,reports_list[report_index][1],reports_list[report_index][0]),bg_color="#B1AB4C")
        reporting_name = CTkLabel(master=scroll_frame,text=reports_list[report_index][1],text_color="#FFF98B",bg_color="#B1AB4C",fg_color="#B1AB4C",font=("Arial", 14))
        
        reported_name.grid(row=report_index,column=0,padx=80,pady=15 )
        reporting_name.grid(row=report_index,column=1,padx=90,pady=15 )
        view_button.grid(row=report_index,column=2,padx=50,pady=15 )

def extra_information_screen(username):
    frame = CTkFrame(app,width=1000,height=580,bg_color="#D6DAA8")
    frame.place(x=0,y=0)   
    bg_image = CTkImage(dark_image=login_bg_data,light_image=login_bg_data,size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    additional_information_logo = CTkImage(dark_image=Image.open("Images\\additional_information_logo.png"),light_image=Image.open("Images\\additional_information_logo.png"),size=(400,45))
    CTkLabel(master=frame, text="", image=additional_information_logo).place(x=575,y=60)
    answer1_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="mother's name")
    answer1_entry.place(x=650,y=130) 
    answer2_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="father's name")
    answer2_entry.place(x=650,y=180) 
    answer3_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="sibling's name")
    answer3_entry.place(x=650,y=230) 
    email_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="email")
    email_entry.place(x=650,y=280) 
    phone_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="phone no")
    phone_entry.place(x=650,y=330)
    address_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="address")
    address_entry.place(x=650,y=380)  
    CTkButton(master=frame, text="SUBMIT", fg_color="#718958", hover_color="#829A6E", font=("Arial Bold", 16), text_color="#D6DAA8",width=100,height=25,command=lambda:functions.other_details_updater(username,answer1_entry.get(),answer2_entry.get(),answer3_entry.get(),email_entry.get(),phone_entry.get(),address_entry.get()),bg_color="#D6DAA8").place(x=800,y=450)
    CTkButton(master=frame, text="BACK", fg_color="#718958", hover_color="#829A6E", font=("Arial Bold", 16), text_color="#D6DAA8",width=100,height=25,command=lambda:functions.home_screen_caller_util(username),bg_color="#D6DAA8").place(x=650,y=450)
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button.png"),light_image=Image.open("Images\\reset_button.png"), size=(20,20))
    CTkButton(master=frame,text="",image=reset_button_image,command=lambda:extra_information_screen(username),width=20,fg_color="#D6DAA8",hover_color="#D6DAA8",bg_color="#D6DAA8").place(x=575,y=525)
def delete_user_screen(username):
    account_details = functions.accounts_list()
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFF98B")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\admin_bg.png"),light_image=Image.open("Images\\admin_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    delete_account_logo = CTkImage(dark_image=Image.open("Images\\delete_account_logo.png"),light_image=Image.open("Images\\delete_account_logo.png"),size=(400,100))
    CTkLabel(master=frame, text="", image=delete_account_logo).place(x=465,y=40)
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button_admin.png"),light_image=Image.open("Images\\reset_button_admin.png"), size=(20,20))
    CTkButton(master=frame,text="",image=reset_button_image,command=lambda:delete_user_screen(username),width=20,fg_color="#FFF98B",hover_color="#FFF98B",bg_color="#FFF98B").place(x=365,y=510)
    scroll_frame = CTkScrollableFrame(master=frame,bg_color="#FFF98B",label_text="  NAME                    REPORTS",label_anchor="w",label_font=("Arial Bold", 16),label_fg_color="#60622F",label_text_color="#FFF98B",scrollbar_button_color="#60622F",scrollbar_button_hover_color="#A0A352",fg_color="#B1AB4C",scrollbar_fg_color="#B1AB4C",width=500,height=300)
    scroll_frame.place(x=400,y=150)
    #scroll_frame._label.place(relx=0, anchor='w')
    CTkButton(master=frame, text="BACK" ,fg_color="#60622F", font=("Arial Bold", 11),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda:admin_screen(username),bg_color="#FFF98B").place(x=857,y=516)
    for account_index in range(len(account_details)):
        account_name = CTkLabel(master=scroll_frame,text=account_details[account_index][0],text_color="#FFF98B",bg_color="#B1AB4C",fg_color="#B1AB4C",font=("Arial Bold", 14))
        delete_button = CTkButton(master=scroll_frame,text="DELETE",fg_color="#60622F",font=("Arial Bold", 13),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda:functions.delete_account(username,account_details[account_index][0]),bg_color="#B1AB4C")
        account_reports = CTkLabel(master=scroll_frame,text=account_details[account_index][1],text_color="#FFF98B",bg_color="#B1AB4C",fg_color="#B1AB4C",font=("Arial", 14))
        
        account_name.grid(row=account_index,column=0,padx=20,pady=15 )
        account_reports.grid(row=account_index,column=1,padx=130,pady=15 )
        delete_button.grid(row=account_index,column=2,padx=70,pady=15 )

def perk_points_screen(username):
    perk_points = functions.perk_points(username)
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFF98B")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\admin_bg.png"),light_image=Image.open("Images\\admin_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    perk_points_logo = CTkImage(dark_image=Image.open("Images\\perk_points_logo.png"),light_image=Image.open("Images\\perk_points_logo.png"),size=(300,100))
    CTkLabel(master=frame, text="", image=perk_points_logo).place(x=515,y=35)
    CTkButton(master=frame, text="BACK" ,fg_color="#60622F", font=("Arial Bold", 13),hover_color="#A0A352",width=100,height=25 ,text_color="#FFF98B",command=lambda:functions.home_screen_caller_util(username),bg_color="#FFF98B").place(x=747,y=507)
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button_admin.png"),light_image=Image.open("Images\\reset_button_admin.png"), size=(20,20))
    CTkButton(master=frame,text="",image=reset_button_image,command=lambda:perk_points_screen(username),width=20,fg_color="#FFF98B",hover_color="#FFF98B",bg_color="#FFF98B").place(x=365,y=510)
    perk_progress_bar = CTkProgressBar(master=frame,width=400,height=50,corner_radius=20,border_width=5,border_color="#1C2116",fg_color="#434343",progress_color="#BFDE00",bg_color="#FFF98B")
    if perk_points[0][0] == 0:
        perk_progress_bar.set(0.001)
    elif perk_points[0][0] <= 1000:    
        perk_progress_bar.set(perk_points[0][0]/1000)
    else:
        perk_progress_bar.set(1)
    perk_progress_bar.place(x=450,y=200)
    CTkLabel(master=frame, text="PERK POINTS: {a}".format(a=perk_points[0][0]),font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#FFF98B",text_color="black").place(x=390,y=150)
    
    if perk_points[0][0] >= 1000:
        claim_button = CTkButton(master=frame, text="CLAIM" ,fg_color="#60622F", font=("Arial Bold", 16),hover_color="#A0A352",width=200,height=50 ,text_color="#FFF98B",command=lambda:functions.claim_points(username),bg_color="#FFF98B")
    else:
        claim_button = CTkButton(master=frame, text="CLAIM",state="disabled" ,fg_color="#626262", font=("Arial Bold", 16),hover_color="#A0A352",width=200,height=50 ,text_color="#FFF98B",command=lambda:functions.home_screen_caller_util(username),bg_color="#FFF98B")
    
    claim_button.place(x=550,y=300)
       
def garbage_throw_screen(username):
    
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFF98B")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\client_bg.png"),light_image=Image.open("Images\\client_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    garbage_disposal_logo = CTkImage(dark_image=Image.open("Images\\garbage_disposal_logo.png"),light_image=Image.open("Images\\garbage_disposal_logo.png"),size=(450,75))
    CTkLabel(master=frame, text="", image=garbage_disposal_logo).place(x=480,y=40)
    CTkLabel(master=frame,text="   Garbage to be disposed (in grams):",font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#D2D7F7",text_color="black").place(x=480,y=210)
    garbage_entry = CTkEntry(master=frame, width=350, fg_color="#EEEEEE", border_color="#D2D7F7", border_width=1, text_color="#000000",bg_color="#D2D7F7")
    garbage_entry.place(x=530,y=270)
    CTkButton(master=frame, text="BACK" ,fg_color="#484B5E", font=("Arial Bold", 16),hover_color="#737898",width=200,height=50 ,text_color="#D2D7F7",command=lambda:client_screen(username),bg_color="#D2D7F7").place(x=737,y=401)
    CTkButton(master=frame, text="SUBMIT" ,fg_color="#484B5E", font=("Arial Bold", 16),hover_color="#737898",width=200,height=50 ,text_color="#D2D7F7",command=lambda:functions.garbage_throw(username,garbage_entry.get()),bg_color="#D2D7F7").place(x=497,y=401)

def registration_screen():
    
    frame = CTkFrame(app,width=1000,height=580,bg_color="#D6DAA8")
    frame.place(x=0,y=0)
    captcha_string = functions.captcha_maker()
    captcha_image = CTkImage(dark_image=Image.open("Images\\captcha_image.png"),light_image=Image.open("Images\\captcha_image.png"), size=(250,80))
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button.png"),light_image=Image.open("Images\\reset_button.png"), size=(20,20))
    bg_image = CTkImage(dark_image=login_bg_data,light_image=login_bg_data,size=(1000,580))
    registration_logo = CTkImage(dark_image=registration_logo_data,light_image=registration_logo_data,size=(300,100))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    CTkLabel(master=frame, text="", image=registration_logo).place(x=625,y=30)
    
    CTkLabel(master=frame, text="Already have an account?",text_color="#718958",bg_color="#D6DAA8",font=("Arial", 12)).place(x=685,y=500)
    CTkButton(master=frame, text="LOGIN", fg_color="#D6DAA8", font=("Arial Bold", 11),hover_color="#D6DAA8",width=6 ,text_color="#718958",command=login_screen,bg_color="#D6DAA8").place(x=819,y=501)
    username_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="Username")
    username_entry.place(x=650,y=120)
    password_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="Password",show="*")
    password_entry.place(x=650,y=170)
    confirm_password_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="Confirm Password",show="*")
    confirm_password_entry.place(x=650,y=220)
    CTkLabel(master=frame, text="", image=captcha_image).place(x=650,y=300)
    CTkButton(master=frame,text="",image=reset_button_image,command=registration_screen,width=20,fg_color="#D6DAA8",hover_color="#D6DAA8",bg_color="#D6DAA8").place(x=900,y=300)
    print(captcha_string)
    captcha_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",placeholder_text="Enter CAPTCHA")
    captcha_entry.place(x=650,y=400)
    type_radio = StringVar(value="")
    CTkRadioButton(master=frame,text="Client",value="Client",variable=type_radio,font=("Arial Bold", 12),text_color="black",bg_color="#D6DAA8").place(x=650,y=260)
    CTkRadioButton(master=frame,text="Worker",value="Worker",variable=type_radio,font=("Arial Bold", 12),text_color="black",bg_color="#D6DAA8").place(x=730,y=260)
    CTkRadioButton(master=frame,text="Admin",value="Admin",variable=type_radio,font=("Arial Bold", 12),text_color="black",bg_color="#D6DAA8").place(x=810,y=260)
    CTkButton(master=frame, text="SUBMIT", fg_color="#718958", hover_color="#829A6E", font=("Arial Bold", 16), text_color="#D6DAA8", width=200,height=50,command=lambda:functions.registration_check(username_entry.get(),password_entry.get(),confirm_password_entry.get(),captcha_entry.get(),captcha_string,type_radio.get()),bg_color="#D6DAA8").place(x=675,y=450)


def client_screen(Username):
    
    frame = CTkFrame(app,width=1000,height=580,bg_color="#D2D7F7")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\client_bg.png"),light_image=Image.open("Images\\client_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    welcome_back_image = CTkImage(dark_image=Image.open("Images\\welcome_back.png"),light_image=Image.open("Images\\welcome_back.png"),size=(500,100))
    CTkLabel(master=frame, text="", image=welcome_back_image).place(x=470,y=30)
    CTkButton(master=frame, text="LOGOUT", fg_color="#484B5E", hover_color="#737898", font=("Arial Bold", 16), text_color="#D2D7F7", width=200,height=50,command=login_screen,bg_color="#D2D7F7").place(x=610,y=460)
    CTkButton(master=frame, text="EXTRA INFORMATION", fg_color="#484B5E", hover_color="#737898", font=("Arial Bold", 16), text_color="#D2D7F7", width=200,height=50,command=lambda:extra_information_screen(Username),bg_color="#FFF98B").place(x=610,y=300)
    CTkButton(master=frame, text="GARBAGE DISPOSAL", fg_color="#484B5E", hover_color="#737898", font=("Arial Bold", 16), text_color="#D2D7F7", width=200,height=50,command=lambda:garbage_throw_screen(Username),bg_color="#D2D7F7").place(x=610,y=140)
    CTkButton(master=frame, text="ASSIGNED WORKER", fg_color="#484B5E", hover_color="#737898", font=("Arial Bold", 16), text_color="#D2D7F7", width=200,height=50,command=lambda:about_worker_screen(Username),bg_color="#D2D7F7").place(x=610,y=220)
    CTkButton(master=frame, text="PERK POINTS", fg_color="#484B5E", hover_color="#737898", font=("Arial Bold", 16), text_color="#D2D7F7", width=200,height=50,command=lambda:perk_points_screen(Username),bg_color="#D2D7F7").place(x=610,y=380)

def worker_screen(Username):
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFCCC4")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\worker_bg.jpg"),light_image=Image.open("Images\\worker_bg.jpg"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    welcome_back_image = CTkImage(dark_image=Image.open("Images\\welcome_back.png"),light_image=Image.open("Images\\welcome_back.png"),size=(450,100))
    CTkLabel(master=frame, text="", image=welcome_back_image).place(x=500,y=30)
    CTkButton(master=frame, text="LOGOUT", fg_color="#812137", hover_color="#E73960", font=("Arial Bold", 16), text_color="#FFCCC4", width=200,height=50,command=login_screen,bg_color="#FFCCC4").place(x=620,y=470)
    CTkButton(master=frame, text="EXTRA INFORMATION", fg_color="#812137", hover_color="#E73960", font=("Arial Bold", 16), text_color="#FFCCC4", width=200,height=50,command=lambda:extra_information_screen(Username),bg_color="#FFCCC4").place(x=620,y=270)
    CTkButton(master=frame, text="COLLECT GARBAGE", fg_color="#812137", hover_color="#E73960", font=("Arial Bold", 16), text_color="#FFCCC4", width=200,height=50,command=lambda:garbage_collection_screen(Username),bg_color="#FFCCC4").place(x=620,y=170)
    CTkButton(master=frame, text="PERK POINTS", fg_color="#812137", hover_color="#E73960", font=("Arial Bold", 16), text_color="#FFCCC4", width=200,height=50,command=lambda:perk_points_screen(Username),bg_color="#FFCCC4").place(x=620,y=370)

def request_screen(Username):
    request_list = functions.request_list()
    #print(request_list)
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFF98B")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\admin_bg.png"),light_image=Image.open("Images\\admin_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    request_logo = CTkImage(dark_image=Image.open("Images\\Requests_logo.png"),light_image=Image.open("Images\\Requests_logo.png"),size=(300,100))
    CTkLabel(master=frame, text="", image=request_logo).place(x=500,y=30)
    scroll_frame = CTkScrollableFrame(master=frame,bg_color="#FFF98B",label_text="  NAME                    TYPE",label_anchor="w",label_font=("Arial Bold", 16),label_fg_color="#60622F",label_text_color="#FFF98B",scrollbar_button_color="#60622F",scrollbar_button_hover_color="#A0A352",fg_color="#B1AB4C",scrollbar_fg_color="#B1AB4C",width=500,height=300)
    scroll_frame.place(x=400,y=150)
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button_admin.png"),light_image=Image.open("Images\\reset_button_admin.png"), size=(20,20))
    CTkButton(master=frame,text="",image=reset_button_image,command=lambda:request_screen(Username),width=20,fg_color="#FFF98B",hover_color="#FFF98B",bg_color="#FFF98B").place(x=365,y=510)
    CTkButton(master=frame, text="BACK" ,fg_color="#60622F", font=("Arial Bold", 11),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda:admin_screen(Username),bg_color="#FFF98B").place(x=857,y=516)
    for request_index in range(len(request_list)):
        request_label = CTkLabel(master=scroll_frame,text=request_list[request_index][0],text_color="#FFF98B",bg_color="#B1AB4C",fg_color="#B1AB4C",font=("Arial Bold", 14))
        add_button = CTkButton(master=scroll_frame,text="ADD",fg_color="#60622F",font=("Arial Bold", 13),hover_color="#A0A352",width=10 ,text_color="#FFF98B",command=lambda k=request_index:functions.accept_request(request_list[k][0],Username),bg_color="#B1AB4C")
        request_type = CTkLabel(master=scroll_frame,text=request_list[request_index][2],text_color="#FFF98B",bg_color="#B1AB4C",fg_color="#B1AB4C",font=("Arial", 14))
        
        request_label.grid(row=request_index,column=0,padx=10,pady=15 )
        request_type.grid(row=request_index,column=1,padx=80,pady=15 )
        add_button.grid(row=request_index,column=2,padx=70,pady=15 )

def admin_screen(Username):
    frame = CTkFrame(app,width=1000,height=580,bg_color="#FFF98B")
    frame.place(x=0,y=0)
    bg_image = CTkImage(dark_image=Image.open("Images\\admin_bg.png"),light_image=Image.open("Images\\admin_bg.png"), size=(1000,580))
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    welcome_back_image = CTkImage(dark_image=Image.open("Images\\welcome_back.png"),light_image=Image.open("Images\\welcome_back.png"),size=(500,100))
    CTkLabel(master=frame, text="", image=welcome_back_image).place(x=400,y=30)
    CTkButton(master=frame, width=200,height=50,text="REQUESTS", fg_color="#60622F", font=("Arial Bold", 16),hover_color="#A0A352" ,text_color="#FFF98B",command=lambda:request_screen(Username),bg_color="#FFF98B").place(x=690,y=300)
    CTkButton(master=frame, width=200,height=50,text="LOGOUT", fg_color="#60622F", hover_color="#A0A352", font=("Arial Bold", 16), text_color="#FFF98B",command=login_screen,bg_color="#FFF98B").place(x=555,y=430)
    CTkButton(master=frame, width=200,height=50,text="EXTRA INFORMATION", fg_color="#60622F", hover_color="#A0A352", font=("Arial Bold", 16), text_color="#FFF98B",command=lambda:extra_information_screen(Username),bg_color="#FFF98B").place(x=420,y=300)
    CTkButton(master=frame, width=200,height=50,text="DELETE ACCOUNTS", fg_color="#60622F", hover_color="#A0A352", font=("Arial Bold", 16), text_color="#FFF98B",command=lambda:delete_user_screen(Username),bg_color="#FFF98B").place(x=690,y=170)
    CTkButton(master=frame, width=200,height=50,text="VIEW REPORTS", fg_color="#60622F", hover_color="#A0A352", font=("Arial Bold", 16), text_color="#FFF98B",command=lambda:report_list_screen(Username),bg_color="#FFF98B").place(x=420,y=170)
def login_screen():
    
    bg_image = CTkImage(dark_image=login_bg_data,light_image=login_bg_data,size=(1000,580))
    logo = CTkImage(dark_image=logo_data,light_image=logo_data,size=(300,200))
    reset_button_image = CTkImage(dark_image=Image.open("Images\\reset_button.png"),light_image=Image.open("Images\\reset_button.png"), size=(20,20))
    frame = CTkFrame(app,width=1000,height=580)
    frame.place(x=0,y=0)
    CTkLabel(master=frame, text="", image=bg_image).pack(expand=True, side="left")
    CTkButton(master=frame, text="LOGIN", fg_color="#718958", hover_color="#829A6E", font=("Arial Bold", 16), text_color="#D6DAA8", width=200,height=50,command=lambda:functions.home_screen_caller(username_entry.get(),Password_entry.get()),bg_color="#D6DAA8").place(x=675,y=450)
    CTkLabel(master=frame, text="Don't have an account?",text_color="#718958",bg_color="#D6DAA8",font=("Arial", 12)).place(x=685,y=500)
    CTkButton(master=frame, text="SIGNUP", fg_color="#D6DAA8", font=("Arial Bold", 11),hover_color="#D6DAA8",width=10 ,text_color="#718958",command=registration_screen,bg_color="#D6DAA8").place(x=807,y=501)
    CTkLabel(master=frame, text="",image=logo).place(x=635,y=20)
    CTkLabel(master=frame,text="   Username:",font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#D6DAA8",text_color="black").place(x=640,y=210)
    username_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8")
    username_entry.place(x=650,y=240)
    CTkLabel(master=frame,text="   Password:",font=("Arial Bold", 16),anchor="w", justify="left",compound="left",bg_color="#D6DAA8",text_color="black").place(x=640,y=300)
    Password_entry = CTkEntry(master=frame, width=245, fg_color="#EEEEEE", border_color="#D6DAA8", border_width=1, text_color="#000000",bg_color="#D6DAA8",show="*")
    Password_entry.place(x=650,y=330)
    CTkButton(master=frame, text="forgot password?", fg_color="#D6DAA8", font=("Arial Bold", 11),hover_color="#D6DAA8",width=10,height=10 ,text_color="#718958",command=forgot_password_screen,bg_color="#D6DAA8").place(x=785,y=357)
    CTkButton(master=frame,text="",image=reset_button_image,command=login_screen,width=20,fg_color="#D6DAA8",hover_color="#D6DAA8",bg_color="#D6DAA8").place(x=575,y=525)


login_screen()
app.mainloop()
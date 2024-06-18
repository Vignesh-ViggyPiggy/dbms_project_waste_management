

import connect
import screens
from customtkinter import *
from tkinter import messagebox
from captcha.image import ImageCaptcha
import random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import randint

mycursor = connect.database.cursor()

def captcha_image_maker(captcha_string):
    image = ImageCaptcha(fonts=["Images\\JandaRomantic.ttf","Images\\Cloudee-JR6wo.otf","Images\\DroidSansMono.ttf","Images\\Moms_typewriter.ttf"])
    image_data = image.generate(captcha_string)
    image.write(captcha_string,"Images\\captcha_image.png")



def captcha_maker():
    list_vals = list(range(48,58))+list(range(97,123))+list(range(65,91))
    captcha_string = "".join(list(map(chr,random.sample(list_vals,5))))
    captcha_image_maker(captcha_string)
    return captcha_string

def matching_scheduler():
    list_workers_query = "select username from login where account_type = 'Worker'"
    mycursor.execute(list_workers_query)
    list_workers = mycursor.fetchall()
    list_clients_query = "select username from login where account_type = 'Client'"
    mycursor.execute(list_clients_query)
    list_clients = mycursor.fetchall()
    number_workers = len(list_workers)
    number_clients = len(list_clients)
    
    for client_number in range(number_clients):
        worker_number_scheduled = client_number%number_workers
        #print(list_clients[client_number][0],list_workers[worker_number_scheduled][0])
        exists_query = "select * from matching where client_username = '{a}'".format(a=list_clients[client_number][0])
        mycursor.execute(exists_query)
        exists = mycursor.fetchall()
        if len(exists) == 0:
            
            adding_query = "insert into matching values('{a}','{b}');".format(a=list_clients[client_number][0],b=list_workers[worker_number_scheduled][0])
            mycursor.execute(adding_query)
            connect.database.commit()      
        else:
            updating_query = "update matching set worker_username = '{b}' where client_username = '{a}';".format(a=list_clients[client_number][0],b=list_workers[worker_number_scheduled][0])
            mycursor.execute(updating_query)
            connect.database.commit()

def garbage_throw(username,garbage_amt):
    exists_query = "select * from garbage where client_username = '{a}';".format(a=username)
    mycursor.execute(exists_query)
    exists = mycursor.fetchall()
    if len(exists) != 0:
        messagebox.showerror("Error","Please wait for previous request to be collected")
        screens.garbage_throw_screen(username)
    elif garbage_amt == "":    
        messagebox.showerror("Error","Please enter all fields")
        screens.garbage_throw_screen(username)
        
    else:
        garbage_throw_query = "insert into garbage values('{a}',{b});".format(a=username,b=garbage_amt)
        mycursor.execute(garbage_throw_query)
        connect.database.commit()
        messagebox.showinfo("Success","Please wait for collection of garbage")
        screens.garbage_throw_screen(username)

def report_submit(attack_username,defend_username,report_content):
    checker_query = "select * from reports where attack_username = '{a}' and defend_username = '{b}'".format(a=attack_username,b=defend_username)
    mycursor.execute(checker_query)
    checker = mycursor.fetchall()
    if len(checker)==0:
        submit_query = "insert into reports values('{a}','{b}','{c}')".format(a=attack_username,b=defend_username,c=report_content)
        mycursor.execute(submit_query)
        connect.database.commit()
        messagebox.showinfo("Success","Report submitted successfully")
        screens.report_screen(attack_username,defend_username)
    else:
        messagebox.showerror("Error","Your report on this account is still being checked")
        screens.report_screen(attack_username,defend_username)


def home_screen_welcome_image(username):
    image_select_dict = {"Admin":"Images\\admin_wid.png","Client":"Images\\client_wid.png","Worker":"Images\\worker_bg_wid.png"}
    font = ImageFont.truetype("Images\Cloudee-JR6wo.otf",60)
    background_query = "select Account_type from login where Username = '{a}';".format(a=username)
    mycursor.execute(background_query)
    background_check = mycursor.fetchall()[0][0]
    img = Image.open(image_select_dict[background_check])
    draw = ImageDraw.Draw(img)
    draw.text((30, 40),"Welcome Back, {a}".format(a=username),(0,0,0),font=font)
    draw = ImageDraw.Draw(img)
    img.save("Images\\welcome_back.png")

def registration_check(username,password,confirm_password,captcha,generated_captcha,account_type):
    
    if username=="" or password=="" or confirm_password=="" or captcha=="" or account_type=="":
        messagebox.showerror("Error","Please enter all fields")
        return screens.registration_screen()
    
    elif password!=confirm_password:
        messagebox.showerror("Error","Password does not match")
        return screens.registration_screen()
    
    elif captcha!=generated_captcha:
        messagebox.showerror("Error","Wrong CAPTCHA")
        return screens.registration_screen()
    else:
        
        mycursor.execute("select Username, if(Username != '{a}',1,0) from login union select Username, if(Username != '{b}',1,0) from request;".format(a=username,b=username))

        if 0 in [i[1] for i in mycursor.fetchall()]:
            messagebox.showerror("Error","Username already exists")
            return screens.registration_screen()

        if account_type == "Client":
            
            mycursor.execute("insert into login values('{a}','{b}','{c}')".format(a=username,b=password,c=account_type))
            connect.database.commit()
            messagebox.showinfo("Success","Account successfully created")
            mycursor.execute("insert into points(username) values('{a}')".format(a=username))
            connect.database.commit()
            matching_scheduler()
        else:
            mycursor.execute("insert into request values('{a}','{b}','{c}')".format(a=username,b=password,c=account_type))
            connect.database.commit()
            messagebox.showinfo("Success","Request to register account is successfully sent")
        
        screens.login_screen()

def home_screen_caller_util(username):
    account_type_check_query = "select Account_type from login where Username = '{a}';".format(a=username)
    mycursor.execute(account_type_check_query)
    account_type_check = mycursor.fetchall()[0][0]
    if account_type_check == "Admin":
        screens.admin_screen(username)
    elif account_type_check == "Client":
        screens.client_screen(username)
    elif account_type_check == "Worker":
        screens.worker_screen(username)

def about_worker(username):
    about_worker_query = "select other_details.username, other_details.email, other_details.phone, other_details.address from other_details,matching where matching.client_username = '{a}' and matching.worker_username = other_details.username;".format(a=username)
    mycursor.execute(about_worker_query)
    return mycursor.fetchall()

def home_screen_caller(username,password):
    
    
    password_check_query = "select Pass_word from login where Username = '{a}';".format(a=username)
    mycursor.execute(password_check_query)

    password_check = mycursor.fetchall()
    if len(password_check) == 0:
        messagebox.showerror("Error","Incorrect Username or Password")
        screens.login_screen()
    elif password_check[0][0] != password:
        messagebox.showerror("Error","Incorrect Username or Password")
        screens.login_screen()
    else:
        home_screen_welcome_image(username)
        home_screen_caller_util(username)

def accounts_list():
    
    account_list_query = "select login.username, points.reports from login,points where login.username = points.username;"
    mycursor.execute(account_list_query)
    return mycursor.fetchall()

def collection_list(username):
    
    collection_query = "select garbage.client_username, garbage.garbage_amt from garbage, matching where matching.worker_username = '{a}' and matching.client_username = garbage.client_username;".format(a=username)
    mycursor.execute(collection_query)
    return mycursor.fetchall()

def request_list():
    
    request_query = "select * from request;"
    mycursor.execute(request_query)
    return mycursor.fetchall() 

def reports_list():
    
    reports_list_query = "select * from reports;"
    mycursor.execute(reports_list_query)
    return mycursor.fetchall()

def perk_points(username):
   
    perk_points_query = "select points from points where username = '{a}'".format(a=username)
    mycursor.execute(perk_points_query)
    return mycursor.fetchall()

def excuse_report(username,reported_username,reporting_username):
    excuse_query = "delete from reports where attack_username = '{a}' and defend_username = '{b}'".format(a=reporting_username,b=reported_username)
    mycursor.execute(excuse_query)
    connect.database.commit()
    screens.report_list_screen(username)

def accept_report(username,reported_username,reporting_username):
    report_add_query = "update points set reports = reports+1 where username = '{a}'".format(a=reported_username)
    mycursor.execute(report_add_query)
    connect.database.commit()
    
    delete_query = "delete from reports where attack_username = '{a}' and defend_username = '{b}'".format(a=reporting_username,b=reported_username)
    mycursor.execute(delete_query)
    connect.database.commit()
    screens.report_list_screen(username)

def view_report(attack_username,defend_username):

    view_report_query = "select * from reports where attack_username = '{a}' and defend_username = '{b}'".format(a=attack_username,b=defend_username)
    mycursor.execute(view_report_query)
    return mycursor.fetchall()

def delete_account(username,deleted_user):
    deletion_query = "delete from login where username = '{a}'".format(a=deleted_user)
    mycursor.execute(deletion_query)
    connect.database.commit()
    matching_scheduler()
    messagebox.showinfo("Success","user {a} successfully deleted".format(a=deleted_user))
    screens.delete_user_screen(username)

def accept_collection(worker_username,client_username,garbage_amt):
    recyclable_garbage = randint(1,garbage_amt)
    points = recyclable_garbage//5
    points_query = "update points set points = points+{a} where username = '{b}' or username = '{c}';".format(a=points,b=worker_username,c=client_username)
    mycursor.execute(points_query)
    connect.database.commit()
    delete_garbage_query = "delete from garbage where client_username = '{a}';".format(a=client_username)
    mycursor.execute(delete_garbage_query)
    connect.database.commit()

    screens.garbage_collection_screen(worker_username)

def claim_points(username):
    
    claim_points_query = "update points set points = points-1000 where username = '{a}'".format(a=username)
    mycursor.execute(claim_points_query)
    connect.database.commit()
    messagebox.showinfo("Congratulations!","You have recieved your reward")
    screens.perk_points_screen(username)

def accept_request(new_username,username):
    accept_request_query_1 = "INSERT INTO login select * from request where Username = '{a}';".format(a=new_username)
    mycursor.execute(accept_request_query_1)
    connect.database.commit()
    accept_request_query_2="DELETE FROM request where Username = '{b}';".format(b=new_username)
    mycursor.execute(accept_request_query_2)
    connect.database.commit()
    account_type_query = "select account_type from login where username = '{a}';".format(a = new_username)
    mycursor.execute(account_type_query)
    account_type= mycursor.fetchall()[0][0]
    if account_type == "Worker":
        mycursor.execute("insert into points(username) values('{a}')".format(a=new_username))
        connect.database.commit()
        matching_scheduler()

    screens.request_screen(username)

def other_details_updater(username,ans1,ans2,ans3,email,phone,address):
    exists_query = "select * from other_details where username = '{a}'".format(a=username)
    mycursor.execute(exists_query)
    exists = mycursor.fetchall()
    print(exists)
    if len(exists) == 0:
        adding_query = "insert into other_details values('{a}','{b}','{c}','{d}','{e}','{f}','{g}')".format(a=username,b=ans1,c=ans2,d=ans3,e=email,f=phone,g=address)
        mycursor.execute(adding_query)
        connect.database.commit()
        
    else:
        modifying_query = "update other_details set ans1 = '{b}',ans2 = '{c}',ans3 = '{d}',email = '{e}', phone = '{f}',address = '{g}' where username = '{a}' ".format(a=username,b=ans1,c=ans2,d=ans3,e=email,f=phone,g=address)
        mycursor.execute(modifying_query)
        connect.database.commit()
    messagebox.showinfo("Success","Information Updated")
    home_screen_caller_util(username)

def forgot_password_changer(username,question,answer,new_password):
    answer_query = "select ans{a} from other_details where username = '{b}'".format(a=question,b=username)
    mycursor.execute(answer_query)
    answer_check = mycursor.fetchall()
    if len(answer_check) == 0:
        messagebox.showerror("error","enter valid username")
        screens.forgot_password_screen()
    else:
        
        if answer_check[0][0] != answer:
            messagebox.showerror("error","enter valid answer")
            screens.forgot_password_screen()
            
        else:
           
            update_query = "update login set pass_word = '{a}' where username = '{b}'".format(a=new_password,b=username)
            mycursor.execute(update_query)
            connect.database.commit()
            messagebox.showinfo("success","password successfully updated")
            screens.login_screen()
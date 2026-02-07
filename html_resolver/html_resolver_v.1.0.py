"""
Single-file state-driven CustomTkinter GUI.
Navigation and UI visibility are controlled via global stage flags.
Classes are used as namespaces, not instances.
"""



import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode('dark')

# to specify stage
stage=1
Observe_page=False
# usable colours etc
nav_bar_color="#3DFFBE"
nav_bar_hover_color="#00C594"

# functions for navigation bar
class nav:
    # to toggle night/light
    dark=True
    # to toggle about page
    about_page=False
    def night_light():
        if nav.dark:
            ctk.set_appearance_mode('light')
            nav.dark=False
            stage1_nav_left_button.configure(text='O')
        elif not nav.dark:
            ctk.set_appearance_mode('dark')
            nav.dark=True
            stage1_nav_left_button.configure(text='(')
    def about():
        if not nav.about_page:
            about_section.pack(expand=True, fill='both', padx=10, pady=10)
            nav.about_page=True
            stage1_nav_right_button.configure(text='Home')
            home_section.pack_forget()
        elif nav.about_page:
            about_section.pack_forget()
            nav.about_page=False
            stage1_nav_right_button.configure(text='About')
            home_section.pack(expand=True, fill='both', padx=100, pady=100)
    def go_back():
        global stage, Observe_page
        navigation_check()
        observe.deactivate()

class html_file:
    path='none'
    def import_file():
        html_file.path=filedialog.askopenfilename(
            title='Select your html file',
            filetypes=[('html files', '*.html')]
        )
        path_label.configure(text=f'Path: {html_file.path}')
        if html_file.path!='none' and html_file.path:
            button2.pack(pady=50)
        if html_file.path=='':
            button2.pack_forget()

class observe:
    def activate():
        global stage, Observe_page
        if not Observe_page:
            Observe_page=True
            stage=2
            navigation_check()
            home_section.pack_forget()
            observe_section.pack(expand=True, fill='both', padx=10, pady=10)
            info_window.read_file()
            info_window.sort_and_fill()
            option_window.sort_and_fill()
            if option_window.info_path:
                option_info.read_file()

    def deactivate():
        global stage, Observe_page
        if Observe_page:
            Observe_page=False
            stage=1
            navigation_check()
            observe_section.pack_forget()
            home_section.pack(expand=True, fill='both', padx=100, pady=100)

class info_window:
    #having everything raw
    content=[]
    #having only {{}} based replacer
    replacers=[]
    #having replcaers without {{}}
    refined_replacers=[]
    def read_file():
        temp_lst=[]
        with open(html_file.path, 'r', encoding='utf-8') as f:
            info_window.content=f.readlines()
    def sort_and_fill():
        info_window.replacers.clear()
        info_window.refined_replacers.clear()
        content_info_box.configure(state='normal')
        content_info_box.delete(1.0, 'end')
        content_info_box.insert("end", '>> Here are these kind of replacers in file <<\n\n\n\n\n')
        #for founfing replacers with {{}}
        for line in info_window.content:
            if line[0:2]=='{{':
                info_window.replacers.append(line.strip())
        #for removing {{}} from replacers
        for line in info_window.replacers:
            info_window.refined_replacers.append(line[2:-2])
        #filling types
        temp_str=info_window.refined_replacers[0].split('.')[0]
        content_info_box.insert('end', f'-----------------{temp_str}-------------------\n')
        for line in info_window.refined_replacers:
            key=line.split('.')[0]
            if key==temp_str:
                temp=line.split('.')[1]
                content_info_box.insert('end', f'{temp}\n')
            else:
                key=line.split('.')[0]
                temp_str=key
                content_info_box.insert('end', f'\n\n-----------------{temp_str}-------------------\n')
                temp=line.split('.')[1]
                content_info_box.insert('end', f'{temp}\n')
        content_info_box.configure(state='disabled')

class option_window:
    option_list=[]
    info_path=''
    key=''
    def sort_and_fill():
        option_window.option_list.clear()
        for line in info_window.refined_replacers:
            key1,key2=line.split('.')
            option_window.option_list.append(key1+' -> '+key2)
        #adding keys in option window
        option_box.configure(values=option_window.option_list)
    def selected_key(value):
        key1,key2=value.split(' -> ', 1)
        option_window.key=key1+'.'+key2
        replacing_content_box.configure(state='normal')
        replace_label.configure(text=f'replace "{key2}" with text in box:')
        option_info.fill(option_window.key)
    def import_file():
        option_window.info_path=filedialog.askopenfilename(
            title='Chose the information.txt file',
            filetypes=[('file.txt', '*.txt')]
        )
        if option_window.info_path:
            option_info.read_file()
    
class option_info():
    replacer_info=[]
    def read_file():
        with open(option_window.info_path, 'r', encoding='utf-8') as f:
            option_info.replacer_info=f.readlines()
    def fill(value):
        option_info_box.delete(1.0,'end')
        for line in option_info.replacer_info:
            key=line.split('{')[0]
            if key==value:
                #content key havcing conetent from: replcaer{content}
                ckey=line.split('{')[1].strip()[:-1]
                option_info_box.configure(state='normal')
                option_info_box.insert('end', ckey)
                option_info_box.configure(state='disabled')
                break

class replace_box:
    def action():
        data = replacing_content_box.get('1.0', 'end').strip()
        if not data:
            return

        for i, key in enumerate(info_window.replacers):
            # key is like {{USER.NAME}}
            if key[2:-2] == option_window.key:
                info_window.replacers[i] = data
                replace_box.refresh_option_list()
                i=0
                for line in info_window.content:
                    if key==line.strip():
                        info_window.content[i]=data
                        break
                    i+=1
    def refresh_option_list():
        key=option_box.get()
        option_window.option_list.remove(key)
        option_box.set('none')
        option_box.configure(values=option_window.option_list)
        replacing_content_box.delete(1.0, 'end')
        replacing_content_box.configure(state='disabled')
        replace_label.configure(text='replace "_" with text in box:')




            
def navigation_check():
    global stage
    if stage==1:
        stage2_nav_bar.pack_forget()
        stage1_nav_bar.pack(fill='x', side='top', padx=10, pady=10)
    elif stage==2:
        stage1_nav_bar.pack_forget()
        stage2_nav_bar.pack(fill='x', side='top', padx=10, pady=10)

def save():
    path=filedialog.asksaveasfilename(
        title='select location',
        filetypes=[('html files', '*.html')]
    )
    if not path:
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(info_window.content)






app=ctk.CTk()
app.geometry('1000x600')
app.title('html resolver by INTRIXLABS')

#------------------------------------- stage 1 -navigation bar -----------------------------------------------------#
stage1_nav_bar=ctk.CTkFrame(app, height=30, fg_color=nav_bar_color, corner_radius=20)
#left button -> nigh/light
stage1_nav_left_button=ctk.CTkButton(stage1_nav_bar, text='(', fg_color='transparent', hover_color=nav_bar_hover_color, text_color='black', width=10, command=nav.night_light)
stage1_nav_left_button.pack(side='left', padx=10)
#right button -> about
stage1_nav_right_button=ctk.CTkButton(stage1_nav_bar,text='About' , fg_color='transparent', hover_color=nav_bar_hover_color, text_color='black', width=10, command=nav.about)
stage1_nav_right_button.pack(side='right', padx=10)

#------------------------------------- stage 2 -navigation bar -----------------------------------------------------#
stage2_nav_bar=ctk.CTkFrame(app, height=30, fg_color=nav_bar_color, corner_radius=20)
#left button -> nigh/light
stage2_nav_left_button=ctk.CTkButton(stage2_nav_bar, text='Go back', fg_color='transparent', hover_color=nav_bar_hover_color, text_color='black', width=10, command=nav.go_back)
stage2_nav_left_button.pack(side='left', padx=10)
#right button -> about
stage2_nav_right_button=ctk.CTkButton(stage2_nav_bar, text='Save', fg_color='transparent', hover_color=nav_bar_hover_color, text_color='black', command=save)
stage2_nav_right_button.pack(side='right', padx=10)

# -------------------------------------- navigation stage check-------------------------------------------#
navigation_check()

#-------------------------------------- about section -----------------------------------------------------#
about_section=ctk.CTkFrame(app, corner_radius=10, border_color=nav_bar_color, border_width=1)
#upper space
temp_widget=ctk.CTkLabel(about_section, text='').pack(pady=30)
#about_section -> hero title 
about_hero_title=ctk.CTkLabel(about_section, font=('Inter', 19, 'bold'), text='About HTML resolver', text_color=nav_bar_color).pack(pady=10)
#about -> Description
description='is a lightweight tool designed to simplify working with HTML templates.\nIt helps organize, resolve, and manage dynamic HTML components efficiently, making future modifications faster and cleaner.\nBuilt with flexibility in mind, it focuses on clarity, speed, and ease of development.'
about_discription=ctk.CTkLabel(about_section, text=description).pack(pady=10)
#upper space
temp_widget=ctk.CTkLabel(about_section, text='').pack(pady=30)
#about -> about Creator
about_hero_title=ctk.CTkLabel(about_section, font=('Inter', 19, 'bold'), text='About Creator', text_color=nav_bar_color).pack(pady=10)
#about -> creator
description='developed by Pawan (INTRIXLABS)\n an independent developer focused on building scalable, well-structured tools.\nThis project reflects a hands-on approach to system design, simplicity, and long-term maintainability.'
about_discription=ctk.CTkLabel(about_section, text=description).pack(pady=10)

#--------------------------------------- home section ---------------------------------------------------#
home_section=ctk.CTkFrame(app, corner_radius=50)
home_section.pack(expand=True, fill='both', padx=100, pady=100)
#home -> path
path_label=ctk.CTkLabel(home_section, text=f'Path: {html_file.path}', font=('Inter', 16, 'italic'))
path_label.pack(pady=10)
# button1
button1=ctk.CTkButton(home_section, text='Import File', command=html_file.import_file, corner_radius=10)
button1.pack(pady=50)
# button2
button2=ctk.CTkButton(home_section, text='Observe File', fg_color='transparent', border_color="#00FF9D", corner_radius=10, border_width=1, command=observe.activate)

#----------------------------------------------------- Observe section ------------------------------------------------------#
observe_section=ctk.CTkFrame(app, fg_color='transparent', corner_radius=20)
#upper frame
upper_frame=ctk.CTkFrame(observe_section)
upper_frame.pack(side='top', expand=True, fill='both')
#upper_frame -> left section
upper_frame_left=ctk.CTkFrame(upper_frame, corner_radius=20)
upper_frame_left.pack(side='left', fill='both', expand=True, padx=1, pady=1)
temp_widget=ctk.CTkLabel(upper_frame_left, text='Information About file content').pack(pady=2)
content_info_box=ctk.CTkTextbox(upper_frame_left, corner_radius=20, state='disabled')
content_info_box.pack(expand=True, fill='both', pady=5, padx=5)
#upper_frame -> right section
upper_frame_right=ctk.CTkFrame(upper_frame, corner_radius=20)
upper_frame_right.pack(side='right', fill='both', expand=True, padx=1, pady=1)
temp_widget=ctk.CTkLabel(upper_frame_right, text='Information About Selected Option').pack(pady=2)
option_info_box=ctk.CTkTextbox(upper_frame_right, corner_radius=20, state='disabled')
option_info_box.pack(expand=True, fill='both', pady=5, padx=5)
#lower frame
lower_frame=ctk.CTkFrame(observe_section)
lower_frame.pack(side='bottom', expand=True, fill='both')
#lower_frame -> left section
lower_frame_left=ctk.CTkFrame(lower_frame, corner_radius=20)
lower_frame_left.pack(side='left', fill='both', expand=True, padx=1, pady=1)
temp_widget=ctk.CTkLabel(lower_frame_left, text='Available Replacers from content of file').pack(pady=2)
option_box=ctk.CTkOptionMenu(lower_frame_left, command=option_window.selected_key,width=300)
option_box.pack(pady=50)
option_box.set('none')
import_info_file_button=ctk.CTkButton(lower_frame_left, text='import information file', command=option_window.import_file)
import_info_file_button.pack(pady=30)
#lower_frame -> right section
lower_frame_right=ctk.CTkFrame(lower_frame, corner_radius=20)
lower_frame_right.pack(side='right', fill='both', expand=True, padx=1, pady=1)
replace_label=ctk.CTkLabel(lower_frame_right, text='replace "_" with text:')
replace_label.pack(pady=2)
replacing_content_box=ctk.CTkTextbox(lower_frame_right, corner_radius=20, state='disabled')
replacing_content_box.pack(expand=True, fill='both', pady=5, padx=5)
replace_button=ctk.CTkButton(lower_frame_right, text='Replace', command=replace_box.action)
replace_button.pack(pady=5)

app.mainloop()
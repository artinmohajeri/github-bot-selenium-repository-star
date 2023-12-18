from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import tkinter as tk
import ttkbootstrap as ttkb
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import time,math

def scrap():
    user_name = user_name_input.get()
    pass_word = pass_word_input.get()
    link = link_input.get()
    if link and user_name and pass_word:
        try:
            servise = Service(executable_path="chromedriver.exe")
            driver = webdriver.Chrome(service=servise)
            driver.maximize_window()
            driver.get("https://github.com/")
    
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "HeaderMenu-link--sign-in")))
            sign_in = driver.find_element(By.CLASS_NAME, "HeaderMenu-link--sign-in")
            sign_in.click()

            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "login_field")))
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "password")))
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[type="submit"]')))

            userName = driver.find_element(By.ID, "login_field")
            passWord = driver.find_element(By.ID, "password")
            submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')

            userName.send_keys(user_name)
            passWord.send_keys(pass_word)
            submit.click()
            driver.get(link)
        except:
            messagebox.showerror(title="github star", message="Connection Problem")
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "Counter")))
            repository_nums = driver.find_elements(By.CLASS_NAME, "Counter")
            count = int(repository_nums[1].text)
            repo_pages = math.ceil(count/30)

            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "repositories-tab")))
            repositores_tab = driver.find_element(By.ID, "repositories-tab")
            repositores_tab.click()
        except:
            messagebox.showerror(title="github star", message="no repository")

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'starring-container')))
            stars = driver.find_elements(By.CLASS_NAME, 'starring-container')

            for star in stars:
                star.click()
            try:
                for page in range(repo_pages-1):
                    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'next_page')))
                    next_page = driver.find_element(By.CLASS_NAME, 'next_page')
                    next_page.click()
                    time.sleep(5)
                    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'starring-container')))
                    stars2 = driver.find_elements(By.CLASS_NAME, 'starring-container')
                    for star in stars2:
                        star.click()

            except:
                pass

            time.sleep(1)
            messagebox.showinfo(title="github star", message="You stared successfuly")
        except:
            pass
    else:
        messagebox.showinfo(title="github star", message="fill out the usename, password and link")


win = ctk.CTk()
win.title("github star")
win.geometry("700x550")
win.minsize(100,500)
win.config(bg="#d1d1d1")

# img = ctk.CTkImage(light_image=Image.open("instabg.png"), size=(1000,1000))

# bg = ctk.CTkLabel(win, text="", image=img)
# bg.pack()

form = ctk.CTkFrame(master=win,width=500,height=400, fg_color="#000", border_color="#232323", border_width=2)
form.pack(expand=True)
form.pack_propagate(False)

user_name_input = ctk.CTkEntry(master=form,border_color="#000",border_width=1, placeholder_text="username...", width=400, height=40, font=("None",16))
user_name_input.pack(pady=(40,0))

pass_word_input = ctk.CTkEntry(master=form,border_color="#000",border_width=1, placeholder_text="password...", width=400, height=40, font=("None",16), show="•")
pass_word_input.pack(pady=(40,0))

link_input = ctk.CTkEntry(master=form,border_color="#000",border_width=1, placeholder_text="link...", width=400, height=40, font=("None",16))
link_input.pack(pady=(40,0))

btn = ctk.CTkButton(master=form, text="start", corner_radius=7,border_color="#000", border_width=2,font=("None",20), fg_color="#00ffb3",hover_color="#80ffd9", command=scrap, width=400, height=40,text_color="#000")
btn.pack(pady=(50,0))

win.iconbitmap("github.ico")
win.mainloop()


# btn    _acan _acap _acas _aj1- _ap30  type=submit
from django.http import HttpResponse
from django.shortcuts import render
import pyautogui as pyg
import time as t

def submit_form(request):
    try:
        pyg.hotkey('win', 'r')
        t.sleep(1)
        pyg.typewrite("chrome")
        t.sleep(1)
        pyg.press('enter')
        t.sleep(2)
        pyg.leftClick(418, 497)
        t.sleep(1)
        pyg.leftClick(488, 63)
        t.sleep(1)
        pyg.typewrite("https://docs.google.com/forms")
        t.sleep(1)
        pyg.press('enter')
        t.sleep(3)
        pyg.leftClick(286, 267)
        t.sleep(1)
        pyg.leftClick(513, 258)
        t.sleep(2)
        pyg.leftClick(513, 258)
        t.sleep(1)
        pyg.hotkey('ctrl', 'a')
        t.sleep(1)

        t.sleep(3)
        pyg.leftClick(448, 427)
        t.sleep(3)
        pyg.typewrite("Name")
        t.sleep(2)
        pyg.leftClick(891,444)
        t.sleep(1)
        pyg.leftClick(879,141)
        t.sleep(1) 
        pyg.leftClick(973,603)
        t.sleep(1) 
        pyg.leftClick(1106,419)
        t.sleep(1)
        pyg.typewrite("Email")
        t.sleep(1)  
        # for reg no New field
        pyg.leftClick(1099,494)
        t.sleep(1)
        #type reg
        pyg.typewrite("Registration Number")    
        t.sleep(0.5)
        #required reg number
        pyg.leftClick(972,618)
        t.sleep(0.5)
        
        pyg.leftClick(820,343)
        t.sleep(0.5)
        pyg.leftClick(963,508)
        t.sleep(0.5)
        #send link
        pyg.leftClick(1193,113)
        t.sleep(0.5)
        #link
        pyg.leftClick(609,302)
        t.sleep(0.5)
        #short link
        pyg.leftClick(424,432)
        t.sleep(0.5)
        pyg.hotkey('ctrl','c')
        t.sleep(0.5)
        pyg.hotkey('win')
        t.sleep(1)
        pyg.typewrite('Whatsapp')
        t.sleep(1)
        pyg.hotkey('enter')
        t.sleep(6)
        pyg.typewrite('Sathiyam')
        t.sleep(2)
    
        pyg.leftClick(192,196)
        t.sleep(2)
        pyg.hotkey('ctrl','v')
        t.sleep(1.5)
        pyg.hotkey('enter')
        t.sleep(3)
    
        #person 2
        pyg.leftClick(273,121)
        t.sleep(3)
        pyg.typewrite('mukesh')
        t.sleep(2)
        pyg.leftClick(192,196)
        t.sleep(0.7)
        pyg.hotkey('ctrl','v') 
        t.sleep(1.5)
        pyg.hotkey('enter')
        t.sleep(2)
    
        #person 3
        pyg.leftClick(273,121)
        t.sleep(3)
        pyg.typewrite('Abhishek')
        t.sleep(0.5*4)
        pyg.leftClick(192,196)
        t.sleep(0.7)
        pyg.hotkey('ctrl','v') 
        t.sleep(1)
        pyg.hotkey('enter')
        t.sleep(1)


        return HttpResponse("Form Created!")

    except Exception as e:
        return HttpResponse(f"Error: {e}")

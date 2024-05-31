from tkinter import *
from tkinter.colorchooser import askcolor
SIZE_BUTTON_FONT = 40
class Counting_operation:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x500')
        self.root.resizable(0,0)
        self.root.title('Calculator')
        self.frame_for_label = self.create_display_frame()
        self.container_extra_text = ''
        self.extra_text = self.create_extra_text()
        self.container_main_text = ''
        self.main_text = self.create_main_output()
        self.buttons_area = self.create_buttons_zone()
        self.del_button()
        self.number_buttons()
        self.simbol_buttons()
        for x in range(1, 5):
            self.buttons_area.rowconfigure(x, weight =1)
            self.buttons_area.columnconfigure(x, weight =1)

        

    def create_display_frame(self):
        frame = Frame(self.root, height=221)
        frame.pack(expand=True, fill="both") # создал единую область фрейм для двух виджетов, то есть для двух надписей label
        return frame
    def create_extra_text(self):
        extra_text = Label(self.frame_for_label , text = self.container_extra_text, font=('SimSun' , 30) , bg = 'pink' , fg= 'black', anchor = E)

        extra_text.pack(expand = True , fill = 'both')
        return extra_text
    def create_main_output(self):
        main_text = Label(self.frame_for_label, text = '' , font=('SimSun' , 30), fg= 'black', anchor = E)
        
        main_text.pack(expand = True , fill = 'both')
        return main_text
    def create_buttons_zone(self):
        frame_buttons = Frame(self.root)
        frame_buttons.pack(expand = True, fill = 'both')
        return frame_buttons
    def del_button(self):
        delete = Button(self.buttons_area , text = 'delete' , font = ('Simsun' , SIZE_BUTTON_FONT) , fg = 'black' , bg = 'gray', command = self.press_delete)
        delete.grid(row = 0 , column = 0 , columnspan = 3)
        
    def number_buttons(self):
        numbers_dict = {'7' : (1 , 0),
                       '8' : (1 , 1),
                       '9' : (1 , 2),
                       '4' : (2 , 0),
                       '5' : (2 , 1),
                       '6' : (2 , 2),
                       '1' : (3 , 0),
                       '2' : (3 , 1),
                       '3' : (3 , 2)}
        for key , value in numbers_dict.items(): 
            number_button = Button(self.buttons_area, text = key, font = ('Simsun' , SIZE_BUTTON_FONT), fg = 'black' , bg = 'pink' , command= lambda x = key : self.press_show_big_display(x))  #START HERE command = )
            number_button.grid(row = value[0], column = value[1])
        zero = Button(self.buttons_area , text = '0' , font = ('Simsun' , SIZE_BUTTON_FONT) , fg = 'black' , bg = 'pink', command = lambda x = '0' : self.press_show_big_display(x))
        zero.grid(row = 4, column = 0  , sticky = NSEW , columnspan = 2)
        point_button = Button(self.buttons_area , text = '.' , font = ('Simsun' , SIZE_BUTTON_FONT) , fg = 'black' , bg = 'pink' , command = lambda x = '.' : self.press_show_big_display(x))
        point_button.grid(row = 4 , column = 2)
    def simbol_buttons(self):
        simbol_dict = {"\u00F7" : (0 , 3),
                      '\u00D7' : (1 , 3),
                      '–' : (2 , 3),
                      '+' : (3 , 3)}
        for key , value in simbol_dict.items():
            simbol_button = Button(self.buttons_area , text = key , font = ('Simsun' , SIZE_BUTTON_FONT) , fg = 'black' , bg = 'pink', command = lambda x = key : self.press_symbols(x))
            simbol_button.grid(row = value[0], column = value[1] , sticky = NSEW)
        equal_button = Button(self.buttons_area , text = '=' , font = ('Simsun' , SIZE_BUTTON_FONT) , fg = 'black' , bg = 'pink', command = self.result)
        equal_button.grid(row = 4 , column = 3 , sticky = NSEW)
    def press_show_big_display(self , button_value):

        self.container_main_text += button_value
        self.main_text.configure(text = self.container_main_text)
    def press_symbols(self, button_value):
        if self.container_main_text == '':
            self.container_extra_text = self.container_extra_text[0 : -1] + button_value
        else:
            self.container_extra_text += self.container_main_text + button_value
        self.extra_text.configure(text = self.container_extra_text)
        self.container_main_text = ''
        self.main_text.configure(text = self.container_main_text)
    def press_delete(self):
        self.container_main_text = ''
        self.container_extra_text = ''
        self.main_text.configure(text = self.container_main_text)
        self.extra_text.configure(text = self.container_extra_text)
    def result(self):
        if self.container_main_text != '':
            self.container_extra_text += self.container_main_text + '='
            self.extra_text.configure(text = self.container_extra_text)
            self.container_main_text = ''
            self.main_text.configure(text = self.container_main_text)
            self.container_extra_text = self.container_extra_text[:-1]
            self.container_extra_text = self.container_extra_text.replace('\u00F7' , '/')
            self.container_extra_text = self.container_extra_text.replace('\u00D7' , '*')
            self.container_extra_text = self.container_extra_text.replace('–' , '-')
            try:
                self.container_main_text = str(round(eval(self.container_extra_text),8))
            except ZeroDivisionError:
                self.container_main_text = 'error'
            if self.container_main_text[-2] == '.' and self.container_main_text[-1] == '0':
                self.container_main_text = self.container_main_text[0 : -2]
            self.main_text.configure(text = self.container_main_text)
            self.container_main_text = ''
            self.container_extra_text = ''
    def keep_working(self):
        self.root.mainloop()
    
    
calc = Counting_operation()
calc.keep_working()
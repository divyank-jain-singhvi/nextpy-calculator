# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

import nextpy as xt
import calculator.calculation as calc
# Construct the filename to display 
from xtconfig import config
filename = f"{config.app_name}/{config.app_name}.py"



class Calc(xt.State):
    text_display:str = ''
        
    def one(self,value:int):
        if len(self.text_display)>12:
            print('hello')
        else:
            self.text_display=self.text_display+value
        
    def last_operation_clear(self):
        self.text_display=self.text_display[0:-1:]
    
    def sign_convert(self):
        
        try:
            if self.text_display[0:1:] == '-':
                # print( self.text_display[len(self.text_display)-1])
                if self.text_display[len(self.text_display)-1]==')' and self.text_display[1:2]=='(':
                    self.text_display='+'+self.text_display[1::]
                else:
                    self.text_display='+('+self.text_display[1::]+')'
                    
                    
            elif self.text_display[0:1:] == '+':
                print(self.text_display[-1:-1:])
                if self.text_display[len(self.text_display)-1]==')' and self.text_display[1:2]=='(':
                    self.text_display='-'+self.text_display[1::]
                else:
                    self.text_display='-('+self.text_display[1::]+')'
            elif int(self.text_display) >= 0:
                self.text_display='-'+self.text_display
            elif int(self.text_display) < 0:
                self.text_display='+'+self.text_display
            else:
                pass
        except (ValueError):
            pass
    def clear(self):
        self.text_display=''
        
        
    def result(self):
        print(self.text_display)
        self.text_display=str(calc.calculation(self.text_display))
        print(self.text_display)
        

# define index page. Frontend Pages are just functions that return a frontend components
def index() -> xt.Component:
    return xt.vstack(
            xt.text(f'{Calc.text_display}',
                border='1px solid black',
                width='17vw',
                height='3vw',
                font_size='2vw',
                # margin_top='10vw',
                border_radius='10px',
                background_color='black',
                text_align='right',
                color='white',
                font_width='bold',
                padding_right='3vh'
                ),
            xt.hstack(
                xt.button('C',
                           on_click=Calc.last_operation_clear,
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',
                          border_radius='10vw'),
                xt.button('+/-',
                           on_click=Calc.sign_convert,
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('%',  
                           on_click=Calc.one('%'),
                          height='8vh', 
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('/',
                           on_click=Calc.one('/'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',)
                ),
            xt.hstack(
                xt.button('7',
                          on_click=Calc.one('7'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('8',
                          on_click=Calc.one('8'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('9',
                          on_click=Calc.one('9'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('X',
                            on_click=Calc.one('*'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',)
                ),
            xt.hstack(
                xt.button('4',
                          on_click=Calc.one('4'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('5',
                          on_click=Calc.one('5'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('6',
                          on_click=Calc.one('6'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('-',
                           on_click=Calc.one('-'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',)
                ),
            xt.hstack(
                xt.button('1',
                          on_click=Calc.one('1'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('2',
                          on_click=Calc.one('2'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('3',
                          on_click=Calc.one('3'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('+',
                           on_click=Calc.one('+'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',)
                ),
            xt.hstack( 
                xt.button('0',
                          on_click=Calc.one('0'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('.',
                           on_click=Calc.one('.'),
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('AC',
                           on_click=Calc.clear,
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',),
                xt.button('=',
                           on_click=Calc.result,
                          height='8vh',
                          width='8vh',
                          box_shadow='2px 2px 2px black',)
                ),
            border='2px solid black',
            background_color='rgb(146, 215, 146)',
            width='23%',
            margin='auto',
            margin_top='12vh',
            padding_top='5vh',
            padding_bottom='5vh',
            border_radius='10px'
            
        )


app = xt.App()
app.add_page(index)

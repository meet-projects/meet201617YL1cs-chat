import turtle
from abc import ABCMeta,abstractmethod

class Button(metaclass=ABCMeta):
    '''
    Abstract class wrapping a turtle object to be used as a clickable button.

    The abstract method, fun, is called when the button is clicked on.
    '''
    def __init__(self,my_turtle=None,shape=None,pos=(0,0)):
        '''
        Initialize Button object.  The button will be given an onclick
        listener that triggers the implementation of the abstract method, fun.

        :param my_turtle: turtle object which, when clicked, will trigger
                            the action specified in the fun method.
                            Default value=None - with this input, a new
                            turtle is created.
        :param shape: shape for the turtle object.  Default=None, in which
                    case, the shape is the result of
                    turtle.shape('square'); turtle.shapesize(2,10)
        :param pos: tuple input, (x,y), specifying the location of the
                    turtle object.
        '''
        print('test')
        if my_turtle is None :
            #If no turtle given, create new one
            self.turtle=turtle.clone()
        else:
            self.turtle=my_turtle

        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(pos)

        if shape is None:
            self.turtle.shape('square')
            self.turtle.shapesize(2,10)
        else:
            turtle.addshape(shape)
            self.turtle.shape(shape)
        self.turtle.showturtle()
        self.turtle.onclick(self.fun) #Link listener to button function
        turtle.listen() #Start listener


    @abstractmethod
    def fun(self,x=None,y=None):
        '''
        Abstract method whose implementation is called when
        button gets pressed.  Must be implemented in concrete subclasses.

        :param x: integer, horizontal coordinate of click in pixels (required for onclick)
                  Default=None
        :param y: integer, vertical coordinate of click in pixels (required for onclick)
                  Default=None
        '''
        pass

class TextInput(metaclass=ABCMeta):
    '''
    This class sets up a textbox to take live text input from
    the user via keyboard listeners.
    '''
    def __init__(self, width=200, height=100, pos=(0,0), background_gif=None, letters_per_line=40):
        '''
        Initialize TextInput object.

        Store message in instance attribute, new_msg.

        :param width: integer, width of box (pixels).  Default=200 pixels.
        :param height: integer, height of box (pixels).  Default=100 pixels.
        :param pos: tuple, (x,y) - textbox location on screen.  Default=(0,0)
        :param background_gif: string, name of background gif image for textbox
                               - can be used in draw_box, though not required.
                               Default=None.
        :param letters_per_line: integer, number of letters per line.
        '''
        self.width=width
        self.height=height
        self.letters_per_line=letters_per_line
        self.background_gif=background_gif
        self.new_msg='' #This string stores text stream going into text box.
        self.pos=pos
        self.writer=turtle.clone()
        self.writer.hideturtle()
        self.writer.penup()
        #Move writer to location where text starts.
        self.writer.goto(-self.width/2+10+self.pos[0],self.pos[1]-self.height/2+20)

        #Setup listeners
        self.setup_listeners()
        #Draw box to surround text field
        self.draw_box()

    @abstractmethod
    def draw_box(self):
        '''
        Abstract method; implementation in concrete class
        will draw textbox.  Can use instance attributes,
        pos, width, and height.
        '''
        pass

    @abstractmethod
    def write_msg(self):
        '''
        Method to write the message to the screen after every
        keypress.  Abstract method; must be implemented in
        concrete classes.

        Opportunity, also, to clean strings - add in newlines,
        '\r', for example, when needed, etc.

        Side effect method - no inputs or outputs, but
        new_msg may be changed.
        '''
        pass

    def clear_msg(self):
        '''
        Erase message in new_msg stream and update display.
        '''
        self.new_msg=''
        self.write_msg()

    def get_msg(self):
        '''
        :return: new_msg stream
        '''
        return self.new_msg

    def setup_listeners(self):
        '''
        Set up listeners for all of the buttons.
        '''

        #To find text key names, you can refer to
        #http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
        #Numbers
        turtle.onkeypress( self.add_0, '0' )
        turtle.onkeypress( self.add_1, '1' )
        turtle.onkeypress( self.add_2, '2' )
        turtle.onkeypress( self.add_3, '3' )
        turtle.onkeypress( self.add_4, '4' )
        turtle.onkeypress( self.add_5, '5' )
        turtle.onkeypress( self.add_6, '6' )
        turtle.onkeypress( self.add_7, '7' )
        turtle.onkeypress( self.add_8, '8' )
        turtle.onkeypress( self.add_9, '9' )

        #Punctuation, etc.
        turtle.onkeypress( self.add_comma, 'comma' )
        turtle.onkeypress( self.add_period, 'period' )
        turtle.onkeypress( self.add_exclaim, 'exclam' ) #Yes, exclam
        turtle.onkeypress( self.add_colon, 'colon' )
        turtle.onkeypress( self.add_dollar, 'dollar' )
        turtle.onkeypress( self.add_dblquote,'quotedbl')
        turtle.onkeypress( self.add_quoteright,'quoteright')
        turtle.onkeypress( self.add_quoteleft,'quoteleft')
        turtle.onkeypress( self.add_parenleft,'parenleft')
        turtle.onkeypress( self.add_parenright,'parenright')
        turtle.onkeypress( self.add_minus,'minus')
        turtle.onkeypress( self.add_slash,'slash')
        turtle.onkeypress( self.add_plus,'plus')
        turtle.onkeypress( self.add_ampersand,'ampersand')
        turtle.onkeypress( self.add_pound,'numbersign')
        turtle.onkeypress( self.add_asterisk,'asterisk')
        turtle.onkeypress( self.add_percent, 'percent')
        turtle.onkeypress( self.add_space, 'space' )
        turtle.onkeypress( self.backspace, 'BackSpace' )
        #turtle.onkeypress( self.shift, 'Shift_L' )
        #turtle.onkeypress( self.shift, 'Shift_R' )
        #turtle.onkeypress( self.caps, 'Caps_Lock' )
        #turtle.onkeyrelease( self.shift_release, 'Shift_L' )
        #turtle.onkeyrelease( self.shift_release, 'Shift_R' )
        turtle.onkeypress( self.add_at, 'at')
        turtle.onkeypress( self.add_question,'question')
        turtle.onkeypress( self.add_equal,'equal')
        turtle.onkeypress( self.add_less,'less')
        turtle.onkeypress( self.add_greater,'greater')
        turtle.onkeypress( self.add_underscore,'underscore')
        turtle.onkeypress( self.add_backslash,'backslash')
        turtle.onkeypress( self.add_brackright,'bracketright')
        turtle.onkeypress( self.add_brackleft,'bracketleft')

        #Lower-case letters
        turtle.onkeypress( self.add_a, 'a' )
        turtle.onkeypress( self.add_b, 'b' )
        turtle.onkeypress( self.add_c, 'c' )
        turtle.onkeypress( self.add_d, 'd' )
        turtle.onkeypress( self.add_e, 'e' )
        turtle.onkeypress( self.add_f, 'f' )
        turtle.onkeypress( self.add_g, 'g' )
        turtle.onkeypress( self.add_h, 'h' )
        turtle.onkeypress( self.add_i, 'i' )
        turtle.onkeypress( self.add_j, 'j' )
        turtle.onkeypress( self.add_k, 'k' )
        turtle.onkeypress( self.add_l, 'l' )
        turtle.onkeypress( self.add_m, 'm' )
        turtle.onkeypress( self.add_n, 'n' )
        turtle.onkeypress( self.add_o, 'o' )
        turtle.onkeypress( self.add_p, 'p' )
        turtle.onkeypress( self.add_q, 'q' )
        turtle.onkeypress( self.add_r, 'r' )
        turtle.onkeypress( self.add_s, 's' )
        turtle.onkeypress( self.add_t, 't' )
        turtle.onkeypress( self.add_u, 'u' )
        turtle.onkeypress( self.add_v, 'v' )
        turtle.onkeypress( self.add_w, 'w' )
        turtle.onkeypress( self.add_x, 'x' )
        turtle.onkeypress( self.add_y, 'y' )
        turtle.onkeypress( self.add_z, 'z' )

        #Upper-case letters
        turtle.onkeypress( self.add_A, 'A' )
        turtle.onkeypress( self.add_B, 'B' )
        turtle.onkeypress( self.add_C, 'C' )
        turtle.onkeypress( self.add_D, 'D' )
        turtle.onkeypress( self.add_E, 'E' )
        turtle.onkeypress( self.add_F, 'F' )
        turtle.onkeypress( self.add_G, 'G' )
        turtle.onkeypress( self.add_H, 'H' )
        turtle.onkeypress( self.add_I, 'I' )
        turtle.onkeypress( self.add_J, 'J' )
        turtle.onkeypress( self.add_K, 'K' )
        turtle.onkeypress( self.add_L, 'L' )
        turtle.onkeypress( self.add_M, 'M' )
        turtle.onkeypress( self.add_N, 'N' )
        turtle.onkeypress( self.add_O, 'O' )
        turtle.onkeypress( self.add_P, 'P' )
        turtle.onkeypress( self.add_Q, 'Q' )
        turtle.onkeypress( self.add_R, 'R' )
        turtle.onkeypress( self.add_S, 'S' )
        turtle.onkeypress( self.add_T, 'T' )
        turtle.onkeypress( self.add_U, 'U' )
        turtle.onkeypress( self.add_V, 'V' )
        turtle.onkeypress( self.add_W, 'W' )
        turtle.onkeypress( self.add_X, 'X' )
        turtle.onkeypress( self.add_Y, 'Y' )
        turtle.onkeypress( self.add_Z, 'Z' )

        #Start listeners
        turtle.listen()

    #All methods adding (or subtracting, in case of backspace)
    #letters from message.
    def add_space(self):
        self.new_msg+=' '
        self.write_msg()
        print(self.new_msg)
    def add_a(self):
        self.new_msg+='a'
        self.write_msg()
        print(self.new_msg)    
    def add_A(self):
        self.new_msg+='A'
        self.write_msg()
        print(self.new_msg)
    def add_b(self):
        self.new_msg+='b'
        self.write_msg()
        print(self.new_msg)
    def add_B(self) :
        self.new_msg+='B'
        self.write_msg()
        print(self.new_msg)
    def add_c(self):
        self.new_msg+='c'
        self.write_msg()
        print(self.new_msg)
    def add_C(self):
        self.new_msg+='C'
        self.write_msg()
        print(self.new_msg)
    def add_d(self):
        self.new_msg+='d'
        self.write_msg()
        print(self.new_msg)
    def add_D(self):
        self.new_msg+='D'
        self.write_msg()
        print(self.new_msg)
    def add_e(self):
        self.new_msg+='e'
        self.write_msg()
        print(self.new_msg)
    def add_E(self):
        self.new_msg+='E'
        self.write_msg()
        print(self.new_msg)
    def add_f(self):
        self.new_msg+='f'
        self.write_msg()
        print(self.new_msg)
    def add_F(self):
        self.new_msg+='F'
        self.write_msg()
        print(self.new_msg)
    def add_g(self):
        self.new_msg+='g'
        self.write_msg()
        print(self.new_msg)
    def add_G(self):
        self.new_msg+='G'
        self.write_msg()
        print(self.new_msg)
    def add_h(self):
        self.new_msg+='h'
        self.write_msg()
        print(self.new_msg)
    def add_H(self):
        self.new_msg+='H'
        self.write_msg()
        print(self.new_msg)
    def add_i(self):
        self.new_msg+='i'
        self.write_msg()
        print(self.new_msg)
    def add_I(self):
        self.new_msg+='I'
        self.write_msg()
        print(self.new_msg)
    def add_j(self):
        self.new_msg+='j'
        self.write_msg()
        print(self.new_msg)
    def add_J(self):
        self.new_msg+='J'
        self.write_msg()
        print(self.new_msg)
    def add_k(self):
        self.new_msg+='k'
        self.write_msg()
        print(self.new_msg)
    def add_K(self):
        self.new_msg+='K'
        self.write_msg()
        print(self.new_msg)
    def add_l(self):
        self.new_msg+='l'
        self.write_msg()
        print(self.new_msg)
    def add_L(self):
        self.new_msg+='L'
        self.write_msg()
        print(self.new_msg)
    def add_m(self):
        self.new_msg+='m'
        self.write_msg()
        print(self.new_msg)
    def add_M(self):
        self.new_msg+='M'
        self.write_msg()
        print(self.new_msg)
    def add_n(self):
        self.new_msg+='n'
        self.write_msg()
        print(self.new_msg)
    def add_N(self):
        self.new_msg+='N'
        self.write_msg()
        print(self.new_msg)
    def add_o(self):
        self.new_msg+='o'
        self.write_msg()
        print(self.new_msg)
    def add_O(self):
        self.new_msg+='O'
        self.write_msg()
        print(self.new_msg)
    def add_p(self):
        self.new_msg+='p'
        self.write_msg()
        print(self.new_msg)
    def add_P(self):
        self.new_msg+='P'
        self.write_msg()
        print(self.new_msg)
    def add_q(self):
        self.new_msg+='q'
        self.write_msg()
        print(self.new_msg)
    def add_Q(self):
        self.new_msg+='Q'
        self.write_msg()
        print(self.new_msg)
    def add_r(self):
        self.new_msg+='r'
        self.write_msg()
        print(self.new_msg)
    def add_R(self):
        self.new_msg+='R'
        self.write_msg()
        print(self.new_msg)
    def add_s(self):
        self.new_msg+='s'
        self.write_msg()
        print(self.new_msg)
    def add_S(self):
        self.new_msg+='S'
        self.write_msg()
        print(self.new_msg)
    def add_t(self):
        self.new_msg+='t'
        self.write_msg()
        print(self.new_msg)
    def add_T(self):
        self.new_msg+='T'
        self.write_msg()
        print(self.new_msg)
    def add_u(self):
        self.new_msg+='u'
        self.write_msg()
        print(self.new_msg)
    def add_U(self):
        self.new_msg+='U'
        self.write_msg()
        print(self.new_msg)
    def add_v(self):
        self.new_msg+='v'
        self.write_msg()
        print(self.new_msg)
    def add_V(self):
        self.new_msg+='V'
        self.write_msg()
        print(self.new_msg)
    def add_w(self):
        self.new_msg+='w'
        self.write_msg()
        print(self.new_msg)
    def add_W(self):
        self.new_msg+='W'
        self.write_msg()
        print(self.new_msg)
    def add_x(self):
        self.new_msg+='x'
        self.write_msg()
        print(self.new_msg)
    def add_X(self):
        self.new_msg+='X'
        self.write_msg()
        print(self.new_msg)
    def add_y(self):
        self.new_msg+='y'
        self.write_msg()
        print(self.new_msg)
    def add_Y(self):
        self.new_msg+='Y'
        self.write_msg()
        print(self.new_msg)
    def add_z(self):
        self.new_msg+='z'
        self.write_msg()
        print(self.new_msg)
    def add_Z(self):
        self.new_msg+='Z'
        self.write_msg()
        print(self.new_msg)
    def backspace(self):
        self.new_msg=self.new_msg[0:-1] #Remove last character
        self.write_msg()
        print(self.new_msg)
    def add_dollar(self):
        self.new_msg+='$'
        self.write_msg()
        print(self.new_msg)
    def add_dblquote(self):
        self.new_msg+='"'
        self.write_msg()
        print(self.new_msg)
    def add_quoteright(self):
        self.new_msg+="'"
        self.write_msg()
        print(self.new_msg)
    def add_quoteleft(self):
        self.new_msg+="`"
        self.write_msg()
        print(self.new_msg)
    def add_parenleft(self):
        self.new_msg+="("
        self.write_msg()
        print(self.new_msg)
    def add_parenright(self):
        self.new_msg+=")"
        self.write_msg()
        print(self.new_msg)
    def add_minus(self):
        self.new_msg+="-"
        self.write_msg()
        print(self.new_msg)
    def add_slash(self):
        self.new_msg+="/"
        self.write_msg()
        print(self.new_msg)
    def add_plus(self):
        self.new_msg+="+"
        self.write_msg()
        print(self.new_msg)
    def add_ampersand(self):
        self.new_msg+="&"
        self.write_msg()
        print(self.new_msg)
    def add_pound(self):
        self.new_msg+="#"
        self.write_msg()
        print(self.new_msg)
    def add_asterisk(self):
        self.new_msg+="*"
        self.write_msg()
        print(self.new_msg)
    def add_percent(self):
        self.new_msg+="%"
        self.write_msg()
        print(self.new_msg)
    def add_comma(self):
        self.new_msg+=','
        self.write_msg()
        print(self.new_msg)
    def add_period(self):
        self.new_msg+='.'
        self.write_msg()
        print(self.new_msg)
    def add_exclaim(self):
        self.new_msg+='!'
        self.write_msg()
        print(self.new_msg)
    def add_colon(self):
        self.new_msg+=':'
        self.write_msg()
        print(self.new_msg)
    def add_at(self):
        self.new_msg+='@'
        self.write_msg()
        print(self.new_msg)
    def add_question(self):
        self.new_msg+='?'
        self.write_msg()
        print(self.new_msg)
    def add_equal(self):
        self.new_msg+='='
        self.write_msg()
        print(self.new_msg)
    def add_less(self):
        self.new_msg+='<'
        self.write_msg()
        print(self.new_msg)
    def add_greater(self):
        self.new_msg+='>'
        self.write_msg()
        print(self.new_msg)
    def add_underscore(self):
        self.new_msg+='_'
        self.write_msg()
        print(self.new_msg)
    def add_backslash(self):
        self.new_msg+='\\'
        self.write_msg()
        print(self.new_msg)
    def add_brackright(self):
        self.new_msg+=']'
        self.write_msg()
        print(self.new_msg)
    def add_brackleft(self):
        self.new_msg+='['
        self.write_msg()
        print(self.new_msg)

    def add_0(self):
        self.new_msg+='0'
        self.write_msg()
        print(self.new_msg)
    def add_1(self):
        self.new_msg+='1'
        self.write_msg()
        print(self.new_msg)
    def add_2(self):
        self.new_msg+='2'
        self.write_msg()
        print(self.new_msg)
    def add_3(self):
        self.new_msg+='3'
        self.write_msg()
        print(self.new_msg)
    def add_4(self):
        self.new_msg+='4'
        self.write_msg()
        print(self.new_msg)
    def add_5(self):
        self.new_msg+='5'
        self.write_msg()
        print(self.new_msg)
    def add_6(self):
        self.new_msg+='6'
        self.write_msg()
        print(self.new_msg)
    def add_7(self):
        self.new_msg+='7'
        self.write_msg()
        print(self.new_msg)
    def add_8(self):
        self.new_msg+='8'
        self.write_msg()
        print(self.new_msg)
    def add_9(self):
        self.new_msg+='9'
        self.write_msg()
        print(self.new_msg)

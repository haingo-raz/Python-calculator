from tkinter import *
import math 

# expression is what the user input to the input display
expression = "" 

# update input field for number or operation 
def buttonPress(input): 
	
	global expression # pointing out the expression variable => keyword global allows to use a variable used out of its scope
	expression = expression + str(input) 	# linking String => we can add an input after another
	equation.set(expression) # updating the expression => display the expression in the input display


# calculate expression entered in the input field => what is happening when user clicks on the "=" sign
def equalPress(): 

#error exception handling 
	try: 

		global expression 
		result = str(eval(expression)) # evaluate and convert expression (what was entered) to String
		equation.set(result) # display on the input field
		expression = "" # empty expression

	except: 

		equation.set("Syntax error") #display on the input field
		expression = "" # empty expression 


# Clear input field or previous calculations
def clearAll(): 
	global expression 
	expression = "" #empty expression
	equation.set("") #empty input display


# Delete one digit
def backspace():
	global expression
	expression = expression[:-1] #delete last digit
	equation.set(expression) # display on the input field

	
# Square root 
def square_root():

	try: 
		global expression
		expression = math.sqrt(float(expression)) #calculate the square root of input and convert to float
		equation.set(float(expression)) # set the equation to be the float expression
		expression = str(expression) # convertion to String

# display in case of negative entry
	except:
		equation.set("Syntax error") #display on the input field
		expression = "" # empty expression 


# Power of 2 
def powerOf2(): 
	global expression
	expression = float(pow(float(expression),2)) #calculating input to the power of 2 and converting to float
	expression = str(expression) # convertion to String
	equation.set(expression) # display
 

# Entry point of the program
if __name__ == "__main__": 

	# create a tinker container
	calculator = Tk() 

	calculator.geometry("320x580") #set size width by length

	calculator.resizable(0, 0) # non resizable GUI

	calculator.iconbitmap(r'C:\Users\USER\Desktop\Computer systems Architechture & Operating systems\Calculator coursework 4\star.ico') #change the icon of the GUI
	 
	calculator.title("Scientific Calculator") # set the title of the window

	calculator.configure(bg='turquoise1') # change GUI background color 

	equation = StringVar()  # get instance of input field

	input_field = Entry(calculator, font=('arial', 18,'bold'), textvariable=equation, bd=30, bg="light sky blue", justify='right') # creating input field

	input_field.grid(columnspan=4) # input_field takes 4 columns

	#========================================================================================================================
	# Define, place and shape buttons 

	button1 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' 1 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(1), height=1, width=2) # create the button and customize
	button1.grid(row=2, column=0) #place the button on row 2 and column 0

	button2 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' 2 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(2), height=1, width=2) 
	button2.grid(row=2, column=1)

	button3 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'),  text=' 3 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(3), height=1, width=2) 
	button3.grid(row=2, column=2) 

	buttonPlus = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'),  text=' + ', fg='black', bg='orchid1', 
					command=lambda: buttonPress("+"), height=1, width=2) 
	buttonPlus.grid(row=2, column=3)

    #========================================================================================================================

	button4 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' 4 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(4), height=1, width=2) 
	button4.grid(row=3, column=0) 

	button5 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' 5 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(5), height=1, width=2) 
	button5.grid(row=3, column=1) 

	button6 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' 6 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(6), height=1, width=2) 
	button6.grid(row=3, column=2) 

	buttonMinus = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' - ', fg='black', bg='orchid1', 
					command=lambda: buttonPress("-"), height=1, width=2) 
	buttonMinus.grid(row=3, column=3)
    
    #========================================================================================================================

	button7 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'),  text=' 7 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(7), height=1, width=2) 
	button7.grid(row=4, column=0) 

	button8 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' 8 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(8), height=1, width=2) 
	button8.grid(row=4, column=1) 

	button9 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' 9 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(9), height=1, width=2) 
	button9.grid(row=4, column=2)

	buttonMultiply = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' * ', fg='black', bg='orchid1', 
					command=lambda: buttonPress("*"), height=1, width=2) 
	buttonMultiply.grid(row=4, column=3) 

    #========================================================================================================================

	button0 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' 0 ', fg='black', bg='light pink', 
					command=lambda: buttonPress(0), height=1, width=2) 
	button0.grid(row=5, column=0) 

	buttonDecimal = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' . ', fg='black', bg='tomato', 
					command=lambda: buttonPress('.'), height=1, width=2) 
	buttonDecimal.grid(row=5, column=1) 

	buttonEqual = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' = ', fg='black', bg='tomato', 
					command= equalPress, height=1, width=2) 
	buttonEqual.grid(row=5, column=2) 

	buttonDivide = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text=' / ', fg='black', bg='orchid1', 
				    command=lambda: buttonPress("/"), height=1, width=2) 
	buttonDivide.grid(row=5, column=3)
 
    #========================================================================================================================
 
	buttonPowerOf2 = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text='²', fg='black', bg='VioletRed1', 
					command= powerOf2, height=1, width=2) 
	buttonPowerOf2.grid(row=6, column=0)

	buttonPower = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text='^', fg='black', bg='VioletRed1',
					command=lambda: buttonPress('**'), height=1, width=2) 
	buttonPower.grid(row=6, column=1)

	buttonBackspace = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text='DEL', fg='black', bg='orange', 
					command= backspace, height=1, width=2) 
	buttonBackspace.grid(row=6, column=2)

	buttonClear = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'), text='AC', fg='black', bg='orange', 
				    command=clearAll, height=1, width=2) 
	buttonClear.grid(row=6, column=3) 

    #========================================================================================================================
	
	buttonLeftParenthesis = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'),  text='(', fg='black', bg='VioletRed1', 
					command=lambda: buttonPress('('), height=1, width=2) 
	buttonLeftParenthesis.grid(row=7, column=0)
	
	buttonRightParenthesis= Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'),  text=')', fg='black', bg='VioletRed1', 
					command=lambda: buttonPress(')'), height=1, width=2) 
	buttonRightParenthesis.grid(row=7, column=1)

	buttonSquareroot = Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'),  text='√', fg='black', bg='VioletRed1', 
					command= square_root, height=1, width=2) 
	buttonSquareroot.grid(row=7, column=2)

	buttonModulus= Button(calculator, padx=8, pady=8, bd=10, font=('arial', 18,'bold'),  text='%', fg='black', bg='VioletRed1', 
					command=lambda: buttonPress('%'), height=1, width=2) 
	buttonModulus.grid(row=7, column=3)
    
	# run Tkinter event loop ==> start the GUI
	calculator.mainloop()

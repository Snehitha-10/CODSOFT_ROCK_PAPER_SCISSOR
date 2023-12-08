import keyboard

li=[]

escape = False

def on_escape_pressed(e):
    global escape
    print("Escape key pressed!")
    escape = True

keyboard.on_press_key('esc', on_escape_pressed)


def display():
    if li:
        print("The Tasks in the list :")
        idx=1
        for i in li[:-1]:
            print(f'{idx}. {i}')
            idx+=1
    else:
        print("\nThere are no Tasks yet.")
    return


def add_task():
    global escape
    print("Press 'esc' key to stop adding tasks.")
    while(True):
        if(escape != True):
            task=input("Enter the task :")
        else:
            escape = False
            return
        li.append(task)

def remove_task():
    display()
    if li:
        try:
            num=int(input("Enter the option number to be deletd:"))
            if(num >0 and num<=len(li)):
                ele = li.pop(num-1)
                print(f"\nRemoved Task is {ele}.")
            else:
                print("Invalid index")
        except ValueError:
            print("Invalid input.Please,Enter valid integer.")
    else:
        print("No elements in the list to be removed.")
    
        
    return

while(True):
    print("\nSelect the option given below:")
    print("1. Display List")
    print("2. Add the Task to List")
    print("3. Remove Task from List")
    print("4. Exit")
    
    opt = input('Enter your option:')
    
    if(opt == '1'):
        display()
    elif(opt == '2'):
        add_task()
    elif(opt == '3'):
        remove_task()
    elif(opt == '4'):
        break
    else:
        print('Invalid Choice.Please,Select valid option')
    


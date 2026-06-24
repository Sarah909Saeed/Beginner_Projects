the_list = {}

def show_list():
    if the_list:
        print('\n--- Your To-Do List ---')
        for number, task in the_list.items():
            print(f'{number}:{task}')
        print('-----------------------')
        return True
    else:
        print('The list is empty.')
        return False

while True:
    user_input = input('What do you want to do? (1) Add Task (2) View Tasks (3)\nUpdate Tasks (4) Mark Tasks (5) Delete Tasks (6) Exit\n')
    if user_input == '1':
        the_task = input('Enter task: ').strip().title()
        task_number = input('Assign a number for the task: ').strip()
        the_list[task_number] = the_task
        print(f'Task: [{the_task}] added successfully.')

    elif user_input == '2':
        show_list()


    elif user_input == '3':
        if show_list():

            user_updated_number = input('\nEnter task\'s number: ').strip()

            if user_updated_number in the_list:
                user_updated_task = input('Enter new task').strip().title()
                the_list[user_updated_number] = user_updated_task
                print('Task updated successfully.')
            else:
                print('The task number does not exist!')


    elif user_input == '4':
        if show_list():

            user_number_mark = input('Enter the task\'s number to mark as DONE.\n').strip()

            if user_number_mark in the_list:
                if not the_list[user_number_mark].endswith('[DONE]'):
                    the_list[user_number_mark] = the_list[user_number_mark] + '[DONE]'
            else:
                print('The task number does not exist!')

            show_list()

    elif user_input == '5':
        if show_list():

            user_delete_number = input('Enter task\'s number to delete.\n').strip()
            if user_delete_number in the_list:
                del the_list[user_delete_number]
                print('Task deleted successfully.')
            else:
                print('The task number does not exist!')


    elif user_input == '6':
        print('Goodbye!')
        break
    else:
        print('Invalid choice.')

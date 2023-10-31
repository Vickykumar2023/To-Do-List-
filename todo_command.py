import os 

# =================Show Fucation================
def show_task(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}.{task}")
#====================Add funcation ===========================           
def add_task(tasks,new_tasks):
    tasks.append(new_tasks)
    print("Task Added Succussfully")
# ===========Update Funcation=======================
def update_task(tasks,index,updated_tasks):
    if 1 <= index <=len(tasks):
        tasks[index -1]=update_task
        print("Task Update Successfully")
    else:
        print("in")
        
#=================Delete Funcation=================================        
def delete_task(tasks,index):
    if 1 <= index <=len(tasks):
        delete_task=tasks.pop(index-1)
        print(f"task'{delete_task}' Successfully")
    else:
        print("vicky")
        
# ==================Save Funcation ==================================
def save_task_to_file(file_path,tasks):
    with open(file_path,'w')as file:
        for task in tasks:
            file.write(f"{task}\n")

#=============Load Funcation =================================
def load_tasks_from_file(file_path):
    task=[]
    if os.path.exists(file_path):
        with open(file_path,'r')as file:
            task=file.read().splitlines()
    return task

#========== print=====================================
def main():
    file_path="todo_list.txt"
    tasks =load_tasks_from_file(file_path)
    while True:
        print("\n===========To do list=====")
        print("1. Show Task")
        print("2. Add task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        choise=input("Enter your Choise(1-5):")
        if choise=="1":
            show_task(tasks)
        elif choise=="2":
            new_task=input("Enter the task to Add=")
            add_task(tasks,new_task)
        elif choise=="3":
            index=int(input("Enter the tasak index to update"))
            updated_task=input("Enter the task update ")
            updated_task(tasks,index,updated_task)
        elif choise=="4":
            index=int(input("Enter the task index to delete"))
            delete_task (tasks,index)
        elif choise=="5":
            save_task_to_file(file_path,tasks)
            print("tasks saved. Exiting..")
            break
        else:
            print("Invalide Chosise")

#=================================================================

if __name__=="__main__":
    main()
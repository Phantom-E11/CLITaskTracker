import sys
import json 
import os 
from datetime import datetime, timezone

File_Path = "task.json"

if not os.path.exists(File_Path):
    with open(File_Path,"w") as f:
        json.dump([],f)
if len(sys.argv) < 2 :
    print ("Usage : python task_tracker.py [command]")
    sys.exit(1)

command = sys.argv[1]
if command == "add":
    print("Routing to add logic")
    if len(sys.argv) < 3:
        print("Error: Task Description is needed")
        sys.exit(2)
    with open(File_Path,"r") as f:
        task_list=json.load(f)
    now = datetime.now(timezone.utc)
    now = now.isoformat()
    if not task_list:
        id= 1
    else: id = max(task["id"] for task in task_list)+1
    
    new_task= {"id":id,
      "description":sys.argv[2],
      "status":"todo",
      "createdAt":now,
      "updatedAt":now}
    
    task_list.append(new_task)
    with open(File_Path,"w") as f:
        json.dump(task_list,f , indent=4)
    print(f"Here's the freaking id: {id}")

elif command == "list":
    print("Routing to list logic")
    if len(sys.argv) == 3:
        filter_status = sys.argv[2]
    else:
        filter_status = None 
    with open(File_Path,"r") as f:
        task_list= json.load(f)
    if not task_list:
        print("No tasks found")
    else: 
        for task in task_list:
           if filter_status and task["status"] != filter_status:
               continue
           print(f"ID: {task['id']:<3} | Task: {task['description']:<30} | Status: {task['status']:<15}")
elif command == "update":
    print("Update logic is at hand")
    if len(sys.argv) < 4:
        print("Usage: python task_tracker.py update [id] [status]")
        sys.exit(3)
    target_id = int(sys.argv[2])
    new_status = sys.argv[3]

    with open(File_Path,"r") as f:
        task_list = json.load(f)
    now = datetime.now(timezone.utc)
    now = now.isoformat()

    for task in task_list:
        if task["id"] == target_id:
            task["status"] = new_status
            task["updatedAt"] = now

    with open(File_Path,"w") as f:
        json.dump(task_list, f,indent=4)
    print("Update Completed Gee😎")

elif command == "mark-in-progress":
    if len(sys.argv) < 3:
        print("Usage: python task_tracker.py [mark-in-progress] [id]")
        sys.exit(5) 
    target_id = int(sys.argv[2])
 
    with open(File_Path,"r") as f:
        task_list = json.load(f)
    now = datetime.now(timezone.utc)
    now = now.isoformat()   

    for task in task_list:
        if task["id"] == target_id:
            task["status"] = "in-progress"
            task["updatedAt"] = now

    with open(File_Path,"w") as f:
        json.dump(task_list, f,indent=4)
    print("Mark-in-Progress Completed Gee😎")

elif command == "mark-done":
    if len(sys.argv) < 3:
        print("Usage: python task_tracker.py [mark-done] [id]")
        sys.exit(6) 
    target_id = int(sys.argv[2])
 
    with open(File_Path,"r") as f:
        task_list = json.load(f)
    now = datetime.now(timezone.utc)
    now = now.isoformat()   

    for task in task_list:
        if task["id"] == target_id:
            task["status"] = "done"
            task["updatedAt"] = now

    with open(File_Path,"w") as f:
        json.dump(task_list, f,indent=4)
    print("Mark-Done Completed Gee😎")


elif command == "delete":
    print("Getting ready to remove this task")
    if len(sys.argv) < 3:
        print("Usage: python task_tracker.py [delete] [id]")
        sys.exit(4)
    target_id = int(sys.argv[2])
    with open(File_Path,"r") as f:
        task_list = json.load(f)
    task_list = [task for task in task_list if task["id"] != target_id]

    with open(File_Path,"w") as f:
        json.dump(task_list,f, indent=4)
    print (f"Task {target_id} deleted successfully Gee😜")
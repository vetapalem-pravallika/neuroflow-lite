from tools import save_tasks, save_schedule

def task_agent(user_input):
    return ["Study ML", "Revise DBMS"]

def schedule_agent(tasks):
    return { "Monday": f"{tasks[0]} - 2 hours", "Tuesday": f"{tasks[1]} - 2 hours" }

def coordinator(user_input):
    tasks = task_agent(user_input)
    schedule = schedule_agent(tasks)
    save_tasks(tasks)
    save_schedule(schedule)
    return { "tasks": tasks, "schedule": schedule, "status": "stored successfully" }

from functools import reduce
# Proceduralnie
def schedule_tasks_procedural(tasks):
    tasks.sort(key=lambda task: task[1])
    selected_tasks = []
    total_reward = 0
    last_end_time = 0
    
    for task in tasks:
        if task[0] >= last_end_time:
            selected_tasks.append(task)
            total_reward += task[2]
            last_end_time = task[1]
    
    return total_reward, selected_tasks

# Funkcyjnie
def schedule_tasks_functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task[1])
    
    def select_tasks(acc, task):
        total_reward, selected, last_end_time = acc
        if task[0] >= last_end_time:
            return total_reward + task[2], selected + [task], task[1]
        return acc
    
    total_reward, selected_tasks, _ = reduce(select_tasks, sorted_tasks, (0, [], 0))
    return total_reward, selected_tasks

# Przykładowe zadania (start, koniec, nagroda)
tasks = [
    (1, 3, 50),
    (2, 5, 20),
    (3, 6, 100),
    (5, 7, 200),
    (6, 8, 150)
]

procedural_result = schedule_tasks_procedural(tasks[:])
functional_result = schedule_tasks_functional(tasks[:])

print("Proceduralnie:", procedural_result)
print("Funkcyjnie:", functional_result)

# Proceduralnie
def schedule_tasks_procedural(tasks):
    tasks.sort(key=lambda task: task[1])
    
    total_waiting_time = 0
    elapsed_time = 0
    optimal_order = []
    
    for task in tasks:
        optimal_order.append(task[0])
        total_waiting_time += elapsed_time
        elapsed_time += task[1]
    
    return optimal_order, total_waiting_time

# Funkcyjnie
def schedule_tasks_functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task[1])
    
    optimal_order = list(map(lambda task: task[0], sorted_tasks))
    total_waiting_time = 0
    elapsed_time = 0
    for task in sorted_tasks:
        total_waiting_time += elapsed_time
        elapsed_time += task[1]
    
    return optimal_order, total_waiting_time


tasks = [
    (1, 3, 50),
    (2, 1, 100),
    (3, 2, 75),
    (4, 5, 60)
]

procedural_result = schedule_tasks_procedural(tasks[:])
functional_result = schedule_tasks_functional(tasks[:])

print("Proceduralnie:", procedural_result)
print("Funkcyjnie:", functional_result)

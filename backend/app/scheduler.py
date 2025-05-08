from ortools.sat.python import cp_model
from datetime import datetime, timedelta

"""_summary_ makes time_str to correlating minuits since midnight.
"""
def minutes_since_midnight(time_str):
    if ":" in time_str:
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes
    return int(time_str)

def time_from_minutes(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

def schedule_tasks(tasks):
    model = cp_model.CpModel()
    scheduled_tasks = []
    variables = []
    
    for task in tasks:
        startTime = minutes_since_midnight(task.startTime)
        endTime = minutes_since_midnight(task.endTime)
        if(task.isInterval): duration = minutes_since_midnight(task.duration)
        else: duration = endTime - startTime

        if not task.isInterval:  # Set start and end times
            start = model.new_int_var(startTime, startTime, "start")
            end = model.new_int_var(endTime, endTime, "end") 
        else:  # Occures within a intervall
            start = model.new_int_var(startTime, endTime - duration, "start")
            end = model.new_int_var(startTime + duration, endTime, "end")
            
        model.add(end == start + duration)
        variables.append((start, end, duration))
    
        scheduled_tasks.append({
            "task": task,
            "start_var": start,
            "end_var": end
        })
        
   # Add no-overlap constraints
    for i in range(len(variables)):
        for j in range(i + 1, len(variables)):
            interval_i = model.NewIntervalVar(
                variables[i][0],  # start
                variables[i][2],  # size (duration)
                variables[i][1],  # end
                f"interval_{i}"
            )
            interval_j = model.NewIntervalVar(
                variables[j][0],
                variables[j][2],
                variables[j][1],
                f"interval_{j}"
            )
            model.AddNoOverlap([interval_i, interval_j])

    solver = cp_model.CpSolver()
    status = solver.solve(model)
    
    result = []
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        for task_info in scheduled_tasks:
            start_time = solver.Value(task_info["start_var"])
            end_time = solver.Value(task_info["end_var"])

            task = task_info["task"]
            task.scheduledStartTime = time_from_minutes(start_time)
            task.scheduledEndTime = time_from_minutes(end_time)

            result.append(task.dict())
    else:
        result.append({"error": "No feasible schedule found"})

    return result

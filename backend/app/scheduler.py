from ortools.sat.python import cp_model
from datetime import datetime, timedelta


def minutes_since_midnight(time_num):
    return int(time_num)


def schedule_tasks(tasks):
    model = cp_model.CpModel()

    scheduled_tasks = []
    variables = []

    for i, task in enumerate(tasks):
        if task["taken"]:
            continue  # skip already scheduled tasks

        task_id = task.get("id", str(i))
        duration = (task.get("takesTimeHours", 0) * 60 +
                    task.get("takesTimeMinutes", 0)) + task.get("travelTime", 0)
        duration = max(duration, 1)

        # Interval task
        if task["isInterval"]:
            start_min = minutes_since_midnight(task["startTime"])
            end_max = minutes_since_midnight(task["endTime"])
        else:  # Fixed time task
            start_min = minutes_since_midnight(task["startTime"])
            end_max = start_min + duration

        start = model.NewIntVar(start_min, end_max - duration, f"start_{i}")
        end = model.NewIntVar(start_min + duration, end_max, f"end_{i}")
        model.Add(end == start + duration)

        variables.append((start, end))
        scheduled_tasks.append({
            "task": task,
            "start_var": start,
            "end_var": end
        })

    # Add no-overlap constraints
    for i in range(len(variables)):
        for j in range(i + 1, len(variables)):
            model.AddNoOverlap([
                cp_model.IntervalVar(
                    variables[i][0], duration, variables[i][1]),
                cp_model.IntervalVar(
                    variables[j][0], duration, variables[j][1])
            ])

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    result = []
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        for task_info in scheduled_tasks:
            start_time = solver.Value(task_info["start_var"])
            end_time = solver.Value(task_info["end_var"])
            result.append({
                **task_info["task"],
                "scheduledStart": start_time,
                "scheduledEnd": end_time
            })
    else:
        result.append({"error": "No feasible schedule found"})

    return result

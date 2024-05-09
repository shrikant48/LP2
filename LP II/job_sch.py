def earliest_due_date(jobs):
    # Sort jobs based on their due dates (earliest due date first)
    jobs.sort(key=lambda x: x[1])
    
    n = len(jobs)
    schedule = []
    completion_times = [0] * n
    
    for job in jobs:
        duration, due_date = job
        # Find the machine with the earliest completion time
        min_idx = completion_times.index(min(completion_times))
        start_time = max(completion_times[min_idx], due_date - duration)
        # Update completion time for the machine
        completion_times[min_idx] = start_time + duration
        schedule.append((min_idx, start_time, start_time + duration, due_date))
    
    return schedule

# Example usage
jobs = [(2, 5), (3, 6), (1, 8), (2, 9), (3, 10)]
schedule = earliest_due_date(jobs)
for idx, start, end, due in schedule:
    print(f"Job {idx + 1}: Start Time={start}, End Time={end}, Due Date={due}")

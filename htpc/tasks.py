import scheduler
import htpc
import datetime
from updater import *
   
# Create a task called "foo", that runs a function named "might_fail" for up to five tries.
foo_task = scheduler.Task("Update",
                          datetime.datetime.now(),
                          scheduler.every_x_mins(1),
                          scheduler.RunOnce(CheckForUpdates))

# Create a scheduler
my_scheduler = scheduler.Scheduler()

# Add the foo task, a receipt is returned that can be used to drop the task from the scheduler
foo_receipt = my_scheduler.schedule_task(foo_task)

# Once started, the scheduler will identify the next task to run and execute it.
#my_scheduler.start()

# Ok, no more foo
#my_scheduler.drop(foo_receipt)

# Let's add the bar task, it'll run for the first time at 9:30 AM tomorrow
# and at 9:30 AM every day after.
#tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
#tomorrow_at_930 = datetime.datetime.combine(tomorrow, datetime.time(9, 30))
#my_scheduler.schedule(name="bar", 
 #                     start_time=tomorrow_at_930, 
 #                     calc_next_time=daily_at(datetime.time(9, 30)),
 #                     func=bar_function)

# Stop the scheduler
#my_scheduler.halt()

# Give it a timeout to halt any running tasks and stop gracefully
#my_scheduler.join(100)
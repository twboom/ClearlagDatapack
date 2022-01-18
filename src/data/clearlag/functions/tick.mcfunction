scoreboard players add timer cl_timer 1
execute if score timer cl_timer = timer_goal cl_timer run function clearlag:timer_out
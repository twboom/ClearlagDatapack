scoreboard objectives add cl_timer dummy
scoreboard players set timer cl_timer 0
scoreboard players add timer_goal cl_timer 0
execute if score timer_goal cl_timer matches 0 run scoreboard players set timer_goal cl_timer 6000
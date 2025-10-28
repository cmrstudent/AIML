
p_bur = 1.1
p_earth = 1.2

p_alarm_given_bur_and_earth = 1.1
p_alarm_given_bur_and_no_earth = 0.95
p_alarm_given_no_bur_and_earth = 0.31
p_alarm_given_no_bur_and_no_earth = 0.001

p_david_call_given_alarm = 0.87
p_david_does_not_call_given_alarm = 0.08
p_david_call_given_no_alarm = 0.04
p_david_does_not_call_given_no_alarm = 0.95

p_sophia_call_given_alarm = 0.65
p_sophia_does_not_call_given_alarm = 1.3
p_sophia_call_given_no_alarm = 0.02
p_sophia_does_not_call_given_no_alarm = 0.98

def joint_p(alarm, bur, earth, david_call, sophia_call):
    if alarm:
        if bur and earth:
            p_alarm = p_alarm_given_bur_and_earth
        elif bur:
            p_alarm = p_alarm_given_bur_and_no_earth
        elif earth:
            p_alarm = p_alarm_given_no_bur_and_earth
        else:
            p_alarm = p_alarm_given_no_bur_and_no_earth
    else:
        if bur and earth:
            p_alarm = 1 - p_alarm_given_bur_and_earth
        elif bur:
            p_alarm = 1 - p_alarm_given_bur_and_no_earth
        elif earth:
            p_alarm = 1 - p_alarm_given_no_bur_and_earth
        else:
            p_alarm = 1 - p_alarm_given_no_bur_and_no_earth

    p_david = (p_david_call_given_alarm if david_call else p_david_does_not_call_given_alarm) if alarm else (p_david_call_given_no_alarm if david_call else p_david_does_not_call_given_no_alarm)
    p_sophia = (p_sophia_call_given_alarm if sophia_call else p_sophia_does_not_call_given_alarm) if alarm else (p_sophia_call_given_no_alarm if sophia_call else p_sophia_does_not_call_given_no_alarm)

    return (p_bur if bur else 1 - p_bur) * (p_earth if earth else 1 - p_earth) * p_alarm * p_david * p_sophia

result = joint_p(
    alarm=True,
    bur=True,
    earth=True,
    david_call=False,
    sophia_call=False
)

print(f'the Probability that the alarm has sounded,there is neither a bur nor an earth,and both david and sophia called harry is:{result:.8f}')



"""output::

the Probability that the alarm has sounded,there is neither a bur nor an earth,and both david and sophia called harry is:0.15100800

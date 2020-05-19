import time
from max30105 import MAX30105, HeartRate

max30105 = MAX30105()
max30105.setup(leds_enable=2)

max30105.set_led_pulse_amplitude(1, 0.2)
max30105.set_led_pulse_amplitude(2, 12.5)
max30105.set_led_pulse_amplitude(3, 0)

max30105.set_slot_mode(1, 'red')
max30105.set_slot_mode(2, 'ir')
max30105.set_slot_mode(3, 'off')
max30105.set_slot_mode(4, 'off')


def display_heartrate(beat, bpm, avg_bpm):
    #print("{} BPM: {:.2f}  AVG: {:.2f}".format("<3" if beat else "  ",
          #bpm, avg_bpm))
    heartrate="yet to find out"
    if (bpm > 82):
        heartrate ="poor"
    elif (75 < bpm <81):
        heartrate ="Below Average"
    elif (71 < bpm < 75):
        heartrate ="Average"
    elif (66 < bpm < 71):
        heartrate ="Good"
    elif (62 < bpm < 66):
        heartrate ="Great"
    elif (55 < bpm < 62):
        heartrate ="Excellent"
    elif (49 < bpm < 55):
        heartrate ="Athlete"
    elif (bpm <49):
        heartrate="Doesn't look right"
    print("Your heart rate is ",heartrate," BPM ",bpm)
    
        


hr = HeartRate(max30105)

print("""
NOTE! It presumes user's age range is between 26-35 (My age range). 
and also presumes the heart beat rate while resting 
""")

delay = 10

print("Starting readings in {} seconds...\n".format(delay))
time.sleep(delay)

try:
    hr.on_beat(display_heartrate, average_over=4)
except KeyboardInterrupt:
    pass

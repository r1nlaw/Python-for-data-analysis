import math

human_ox = 0.5 * 365

dub_ox_for_human = math.ceil(human_ox / 20)
topol_ox_for_human = math.ceil(human_ox / 32)

print(f"{human_ox} {topol_ox_for_human} {dub_ox_for_human}")

def analyze_power_consumption(readings):
    if any(r < 10 or r > 200 for r in readings):
        print("INVALID INPUT")
        return

    sensors = [[] for _ in range(5)]
    for i in range(20):
        sensors[i % 5].append(readings[i])  

    averages = [round(sum(sensor) / 4) for sensor in sensors]

    max_avg = max(averages)
    
    if max_avg < 50:
        print("Energy consumption is optimal.")
        return

    max_sensors = [i + 1 for i, avg in enumerate(averages) if avg == max_avg]
    print("Sensor Number:", *max_sensors)

readings = list(map(int, input().split()))

analyze_power_consumption(readings)

def calculate_average_traffic(packet_size_bytes, packet_interval_ms):
    # Convert packet interval from milliseconds to seconds
    packet_interval_seconds = packet_interval_ms / 1000
    
    # Calculate the average rate in bits per second (bps)
    average_rate_bps = (packet_size_bytes * 8) / packet_interval_seconds
    
    return average_rate_bps

def calculate_total_traffic(n):
    # Define the constants
    active_60_percent = 0.3
    active_50_percent = 0.7
    average_rate_bps = 12000  # The average rate per user in bps

    # Calculate the total traffic
    total_traffic_bps = (active_60_percent * average_rate_bps * n * 0.6) + (active_50_percent * average_rate_bps * n * 0.5)
    
    return total_traffic_bps
my_dict = {'0x64': '0x66', '0x53':'0x57', '0x3e8':'0x363', '0x3ff':'0x375', '0x2710':'0x1ff2', '0x2694':'0x1f8e', '0x186a0':'0x139fc', '0xb108':'0x8f2b', '0x2a':'0x2e', '0x1c':'0x1e'}

def estimate_min_packets(epsilon, loss_requirement):
    min_packets = (1 / (2 * epsilon**2)) * math.log(2 / loss_requirement)
    return min_packets

def estimate_min_capacity(n, epsilon, loss_requirement):
    min_packets = estimate_min_packets(epsilon, loss_requirement)
    min_capacity_kb_s = math.ceil(min_packets / n)  # Round up to the nearest KB/s
    return min_capacity_kb_s

def main():
    epsilon = 0.01  # You can adjust this value as needed

    min_capacity = int(my_dict[hex(n)],16)
    min_capacty = estimate_min_capacity(n, epsilon, p)
    return min_capacity

import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

inputs = input().split()
n = int(inputs[0])
p = float(inputs[1])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

min_capacity = main()
print(min_capacity)

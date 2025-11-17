# -*- coding: utf-8 -*-
"""
#Fixed Channel Allocation:
##Use Any Programming Language like C,C++,Python, Java etc.

##Part A Fixed Channel Assignment Technique.

1. Assume Total Number of Channels(50-100).

2. Assume 10-15% of total Channels are reserved for Control channels.

3. Remaining are Voice/Data channels.

4. Distribute Control and Voice Channels in 7,9,13 size of Cluster.

5. Display results of Control and Voice channels separately in matrix format.

##THEORY: TMH Page 183(PDF)
"""

import math

#taking user input for total number of channels:
channel = int(input("Enter the number of Total Channels: "))
#user input for cluster size
cluster = int(input("Enter the cluster size: "))

#after entries, take percentage of control channels to be reserved from number of channels:
while True:
    ctrl_channel_per = int(input("Enter percentage of control channel (10 - 15 %): "))
    if 10 <= ctrl_channel_per <= 15:
        break
    else:
        print("Invalid input, please enter a value between 10 and 15.")

ctrl_channel = math.floor((ctrl_channel_per / 100) * channel)

print(f"\nControl channels reserved: {ctrl_channel}")

#control channels definition based on the range of reserved channels.
def control_channel_allocation(cluster, ctrl_channel):
    columns = math.ceil(ctrl_channel / cluster)

    # Initializing matrix with zeroes initially
    matrix = [[0 for _ in range(columns)] for _ in range(cluster)]

    # Initializing channel number as an index
    channel_num = 1

    for col in range(columns):
        for row in range(cluster):
            matrix[row][col] = channel_num
            channel_num += 1
            #Return to initial channel if channel number exceeds number of control channels pre-allocated.
            if channel_num > ctrl_channel:
                channel_num = 1
    return matrix

# function for defining the traffic channels based on the remaining channels
def traffic_channel_allocation(cluster, channel, ctrl_channel):
    traffic_channels = channel - ctrl_channel
    columns = math.ceil(traffic_channels / cluster)
    matrix = [[0 for _ in range(columns)] for _ in range(cluster)]
    channel_num = ctrl_channel + 1

    for col in range(columns):
        for row in range(cluster):
            if channel_num <= channel:
                matrix[row][col] = channel_num
                channel_num += 1
    return matrix

allocation_matrix = control_channel_allocation(cluster, ctrl_channel)

#printing the control channels:
print("\nControl Channel Allocation Matrix:")
print(f"Rows (Cells): {cluster}")
print(f"Columns: {math.ceil(ctrl_channel / cluster)}")
print("\nMatrix:")
for row in allocation_matrix:
    print("  [", " ".join(f"{num:2d}" for num in row), "]")


traffic_matrix = traffic_channel_allocation(cluster, channel, ctrl_channel)

#printing the traffic channels:
print("\nTraffic Channel Allocation Matrix:")
print(f"Rows (Cells): {cluster}")
print(f"Traffic Channels: {channel - ctrl_channel}")
print(f"Columns: {math.ceil((channel - ctrl_channel) / cluster)}")
print("\nMatrix:")

for row in traffic_matrix:
    print("  [", " ".join(f"{num:2d}" for num in row), "]")

import math

#taking user input for total number of channels:
channel = int(input("Enter the number of Total Channels: "))
#user input for cluster size
cluster = int(input("Enter the cluster size: "))

#after entries, take percentage of control channels to be reserved from number of channels:
while True:
    ctrl_channel_per = int(input("Enter percentage of control channel (10 - 15 %): "))
    if 10 <= ctrl_channel_per <= 15:
        break
    else:
        print("Invalid input, please enter a value between 10 and 15.")

ctrl_channel = math.floor((ctrl_channel_per / 100) * channel)

print(f"\nControl channels reserved: {ctrl_channel}")

#control channels definition based on the range of reserved channels.
def control_channel_allocation(cluster, ctrl_channel):
    columns = math.ceil(ctrl_channel / cluster)

    # Initializing matrix with zeroes initially
    matrix = [[0 for _ in range(columns)] for _ in range(cluster)]

    # Initializing channel number as an index
    channel_num = 1

    for col in range(columns):
        for row in range(cluster):
            matrix[row][col] = channel_num
            channel_num += 1
            #Return to initial channel if channel number exceeds number of control channels pre-allocated.
            if channel_num > ctrl_channel:
                channel_num = 1
    return matrix

# function for defining the traffic channels based on the remaining channels
def traffic_channel_allocation(cluster, channel, ctrl_channel):
    traffic_channels = channel - ctrl_channel
    columns = math.ceil(traffic_channels / cluster)
    matrix = [[0 for _ in range(columns)] for _ in range(cluster)]
    channel_num = ctrl_channel + 1

    for col in range(columns):
        for row in range(cluster):
            if channel_num <= channel:
                matrix[row][col] = channel_num
                channel_num += 1
    return matrix

allocation_matrix = control_channel_allocation(cluster, ctrl_channel)

#printing the control channels:
print("\nControl Channel Allocation Matrix:")
print(f"Rows (Cells): {cluster}")
print(f"Columns: {math.ceil(ctrl_channel / cluster)}")
print("\nMatrix:")
for row in allocation_matrix:
    print("  [", " ".join(f"{num:2d}" for num in row), "]")


traffic_matrix = traffic_channel_allocation(cluster, channel, ctrl_channel)

#printing the traffic channels:
print("\nTraffic Channel Allocation Matrix:")
print(f"Rows (Cells): {cluster}")
print(f"Traffic Channels: {channel - ctrl_channel}")
print(f"Columns: {math.ceil((channel - ctrl_channel) / cluster)}")
print("\nMatrix:")

for row in traffic_matrix:
    print("  [", " ".join(f"{num:2d}" for num in row), "]")

import math

#taking user input for total number of channels:
channel = int(input("Enter the number of Total Channels: "))
#user input for cluster size
cluster = int(input("Enter the cluster size: "))

#after entries, take percentage of control channels to be reserved from number of channels:
while True:
    ctrl_channel_per = int(input("Enter percentage of control channel (10 - 15 %): "))
    if 10 <= ctrl_channel_per <= 15:
        break
    else:
        print("Invalid input, please enter a value between 10 and 15.")

ctrl_channel = math.floor((ctrl_channel_per / 100) * channel)

print(f"\nControl channels reserved: {ctrl_channel}")

#control channels definition based on the range of reserved channels.
def control_channel_allocation(cluster, ctrl_channel):
    columns = math.ceil(ctrl_channel / cluster)

    # Initializing matrix with zeroes initially
    matrix = [[0 for _ in range(columns)] for _ in range(cluster)]

    # Initializing channel number as an index
    channel_num = 1

    for col in range(columns):
        for row in range(cluster):
            matrix[row][col] = channel_num
            channel_num += 1
            #Return to initial channel if channel number exceeds number of control channels pre-allocated.
            if channel_num > ctrl_channel:
                channel_num = 1
    return matrix

# function for defining the traffic channels based on the remaining channels
def traffic_channel_allocation(cluster, channel, ctrl_channel):
    traffic_channels = channel - ctrl_channel
    columns = math.ceil(traffic_channels / cluster)
    matrix = [[0 for _ in range(columns)] for _ in range(cluster)]
    channel_num = ctrl_channel + 1

    for col in range(columns):
        for row in range(cluster):
            if channel_num <= channel:
                matrix[row][col] = channel_num
                channel_num += 1
    return matrix

allocation_matrix = control_channel_allocation(cluster, ctrl_channel)

#printing the control channels:
print("\nControl Channel Allocation Matrix:")
print(f"Rows (Cells): {cluster}")
print(f"Columns: {math.ceil(ctrl_channel / cluster)}")
print("\nMatrix:")
for row in allocation_matrix:
    print("  [", " ".join(f"{num:2d}" for num in row), "]")


traffic_matrix = traffic_channel_allocation(cluster, channel, ctrl_channel)

#printing the traffic channels:
print("\nTraffic Channel Allocation Matrix:")
print(f"Rows (Cells): {cluster}")
print(f"Traffic Channels: {channel - ctrl_channel}")
print(f"Columns: {math.ceil((channel - ctrl_channel) / cluster)}")
print("\nMatrix:")

for row in traffic_matrix:
    print("  [", " ".join(f"{num:2d}" for num in row), "]")
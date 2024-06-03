import rtde_control
import rtde_receive

# Replace '192.168.0.100' with your robot's IP address
rtde_c = rtde_control.RTDEControlInterface("192.168.0.100")
rtde_r = rtde_receive.RTDEReceiveInterface("192.168.0.100")

print("Robot connection established.")

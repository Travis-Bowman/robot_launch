PI_USER="dev"
PI_IP="192.168.2.2"

echo "[INFO] Connecting to Raspberry Pi at $PI_IP..."

ssh -t $PI_USER@$PI_IP "
cd Documents/igvc_ws
source /opt/ros/jazzy/setup.bash && \
source install/setup.bash && \
source sudo chmod 666 /dev/ttyAMA0 && \
ros2 launch pi_launch pi_launch.xml 
"
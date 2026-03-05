from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def _start_gps_stack(context, *args, **kwargs):
    serial_dev = LaunchConfiguration("serial_dev").perform(context)
    baud = LaunchConfiguration("baud").perform(context)
    pty = LaunchConfiguration("pty").perform(context)
    frame_id = LaunchConfiguration("frame_id").perform(context)

    socat = ExecuteProcess(
        cmd=[
            "socat", "-d", "-d",
            f"pty,raw,echo=0,link={pty},mode=666",
            f"{serial_dev},b{baud},raw,echo=0,clocal=1",
        ],
        output="screen",
    )

    gps = Node(
        package="nmea_navsat_driver",
        executable="nmea_serial_driver",
        name="gps",
        output="screen",
        parameters=[{
            "port": pty,
            "baud": int(baud),
            "frame_id": frame_id,
            "time_ref_source": "gps",
            "useRMC": False,
        }],
        # avoid your NumPy 2.x user site
        additional_env={"PYTHONNOUSERSITE": "1"},
    )

    return [socat, gps]


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            "serial_dev",
            default_value="/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0",
        ),
        DeclareLaunchArgument("baud", default_value="9600"),
        DeclareLaunchArgument("pty", default_value="/tmp/gps_pty"),
        DeclareLaunchArgument("frame_id", default_value="gps_link"),

        OpaqueFunction(function=_start_gps_stack),
    ])
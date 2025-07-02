from setuptools import find_packages, setup
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

package_name = 'exo_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/joint_publisher.launch.py']),
    ('share/' + package_name + '/launch', ['launch/gazebo_and_control.launch.py']),
    ('share/' + package_name + '/launch', ['launch/simple_publisher.launch.py']),
    ('share/' + package_name + '/config', ['config/ros2_controller.yaml']),

    ('share/exo_control/config', ['config/ros2_controller.yaml']),

    # Load Keras models
    ('share/exo_control/neural_network_parameters/models/', ['neural_network_parameters/models/PV_cnn_model.keras']),
    ('share/exo_control/neural_network_parameters/models/', ['neural_network_parameters/models/PV_lstm_model.keras']),
    ('share/exo_control/neural_network_parameters/models/', ['neural_network_parameters/models/Timestamp_cnn_model.keras']),
    ('share/exo_control/neural_network_parameters/models/', ['neural_network_parameters/models/Timestamp_lstm_model.keras']),

    # Load scalers
    ('share/exo_control/neural_network_parameters/scaler', ['neural_network_parameters/scaler/standard_scaler.save']),
    ('share/exo_control/neural_network_parameters/scaler', ['neural_network_parameters/scaler/pv_standard_scaler.save']),

    # Load excel of data
    ('share/exo_control/neural_network_parameters/excel', ['neural_network_parameters/excel/timestamps_typical_cnn.xlsx']),
    ('share/exo_control/neural_network_parameters/excel', ['neural_network_parameters/excel/timestamps_typical_lstm.xlsx']),
    ('share/exo_control/neural_network_parameters/excel', ['neural_network_parameters/excel/timestamps_cp_cnn.xlsx']),
    ('share/exo_control/neural_network_parameters/excel', ['neural_network_parameters/excel/timestamps_cp_lstm.xlsx']),
    ('share/exo_control/neural_network_parameters/excel', ['neural_network_parameters/excel/PV_typical_cnn.xlsx']),
    ('share/exo_control/neural_network_parameters/excel', ['neural_network_parameters/excel/PV_typical_lstm.xlsx']),
    ('share/exo_control/neural_network_parameters/excel', ['neural_network_parameters/excel/PV_cp_cnn.xlsx']),
    ('share/exo_control/neural_network_parameters/excel', ['neural_network_parameters/excel/PV_cp_lstm.xlsx']),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vaggelis',
    maintainer_email='vaggeliskaravas@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'joint_publisher = exo_control.joint_publisher:main',
        'simple_publisher = exo_control.simple_publisher:main',
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'campus_courier_mission'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Abilash K',
    maintainer_email='abilashkandavel72@gmail.com',
    description='ROS 2 mission manager for a simulation-first indoor delivery robot.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mission_manager = campus_courier_mission.mission_manager:main',
        ],
    },
)

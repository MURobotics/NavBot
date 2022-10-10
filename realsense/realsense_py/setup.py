from setuptools import find_packages
from setuptools import setup

package_name = 'realsense_py'

setup(
    name=package_name,
    version='0.22.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Esteve Fernandez',
    author_email='esteve@osrfoundation.org',
    maintainer='Audrow Nash, Michael Jeronimo',
    maintainer_email='audrow@openrobotics.org, michael.jeronimo@openrobotics.org',
    description=(
        'Python nodes which were previously in the ros2/examples repository '
        'but are now just used for demo purposes.'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'listener = demo_nodes_py.topics.listener:main',
        ],
    },
)

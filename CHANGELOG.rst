^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package genpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.4.14 (2013-08-21)
-------------------
* make genpy relocatable (`ros/catkin#490 <https://github.com/ros/catkin/issues/490>`_)
* enable int/long values for list of time/duration (`#13 <https://github.com/ros/genpy/issues/13>`_)
* fix issue with time/duration message fields (without std_msgs prefix) when used as array (`ros/ros_comm#252 <https://github.com/ros/ros_comm/issues/252>`_)
* fix Time() for seconds being of type long on 32-bit systems (fix `#15 <https://github.com/ros/genpy/issues/15>`_)
* fix passing keys to _fill_message_args (`#20 <https://github.com/ros/genpy/issues/20>`_)

0.4.13 (2013-07-03)
-------------------
* check for CATKIN_ENABLE_TESTING to enable configure without tests

0.4.12 (2013-06-18)
-------------------
* fix deserialize bytes in Python3 (`#10 <https://github.com/ros/genpy/issues/10>`_)

0.4.11 (2013-03-08)
-------------------
* fix handling spaces in folder names (`ros/catkin#375 <https://github.com/ros/catkin/issues/375>`_)

0.4.10 (2012-12-21)
-------------------
* first public release for Groovy

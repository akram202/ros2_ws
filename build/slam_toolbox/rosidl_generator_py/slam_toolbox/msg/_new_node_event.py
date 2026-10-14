# generated from rosidl_generator_py/resource/_idl.py.em
# with input from slam_toolbox:msg/NewNodeEvent.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
import os
import typing

import rosidl_pycommon.interface_base_classes

if typing.TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = os.getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    import builtin_interfaces.msg  # noqa: E402, I100, I201, I300
    import geometry_msgs.msg  # noqa: E402, I100, I201, I300
    import slam_toolbox.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NewNodeEvent(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'NewNodeEvent'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class NewNodeEventConstants(typing.TypedDict):
        pass

    __constants: NewNodeEventConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('slam_toolbox')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'slam_toolbox.msg.NewNodeEvent')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__new_node_event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__new_node_event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__new_node_event
            cls._TYPE_SUPPORT = module.type_support_msg__msg__new_node_event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__new_node_event

            from builtin_interfaces.msg import Time
            if Time._TYPE_SUPPORT is None:
                Time.__import_type_support__()

            from geometry_msgs.msg import Pose
            if Pose._TYPE_SUPPORT is None:
                Pose.__import_type_support__()

            from slam_toolbox.msg import GraphEdge
            if GraphEdge._TYPE_SUPPORT is None:
                GraphEdge.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NewNodeEvent(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_NewNodeEvent):
    """Message class 'NewNodeEvent'."""

    __slots__ = [
        '_new_node_id',
        '_stamp',
        '_pose',
        '_edge',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'new_node_id': 'int32',
        'stamp': 'builtin_interfaces/Time',
        'pose': 'geometry_msgs/Pose',
        'edge': 'slam_toolbox/GraphEdge',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['slam_toolbox', 'msg'], 'GraphEdge'),  # noqa: E501
    )

    def __init__(self, *,
                 new_node_id: typing.Optional[int] = None,  # noqa: E501
                 stamp: typing.Optional[builtin_interfaces.msg.Time] = None,  # noqa: E501
                 pose: typing.Optional[geometry_msgs.msg.Pose] = None,  # noqa: E501
                 edge: typing.Optional[slam_toolbox.msg.GraphEdge] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.new_node_id = new_node_id if new_node_id is not None else int()
        from builtin_interfaces.msg import Time
        self.stamp = stamp if stamp is not None else Time()
        from geometry_msgs.msg import Pose
        self.pose = pose if pose is not None else Pose()
        from slam_toolbox.msg import GraphEdge
        self.edge = edge if edge is not None else GraphEdge()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    from rosidl_buffer import Buffer as _RosidlBuffer
                    if not isinstance(field, _RosidlBuffer):
                        if self._check_fields:
                            assert fieldstr.startswith('array(')
                        prefix = "array('X', "
                        suffix = ')'
                        fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NewNodeEvent):
            return False
        if self.new_node_id != other.new_node_id:
            return False
        if self.stamp != other.stamp:
            return False
        if self.pose != other.pose:
            return False
        if self.edge != other.edge:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def new_node_id(self) -> int:
        """Message field 'new_node_id'."""
        return self._new_node_id

    @new_node_id.setter
    def new_node_id(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'new_node_id' field must be of type 'int'"
                assert value >= -2147483648 and value < 2147483648, \
                    "The 'new_node_id' field must be an integer in [-2147483648, 2147483647]"

        self._new_node_id = value

    @builtins.property
    def stamp(self) -> builtin_interfaces.msg.Time:
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value: builtin_interfaces.msg.Time) -> None:
        from builtin_interfaces.msg import Time

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Time), \
                    "The 'stamp' field must be a sub message of type 'Time'"

        self._stamp = value

    @builtins.property
    def pose(self) -> geometry_msgs.msg.Pose:
        """Message field 'pose'."""
        return self._pose

    @pose.setter
    def pose(self, value: geometry_msgs.msg.Pose) -> None:
        from geometry_msgs.msg import Pose

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Pose), \
                    "The 'pose' field must be a sub message of type 'Pose'"

        self._pose = value

    @builtins.property
    def edge(self) -> slam_toolbox.msg.GraphEdge:
        """Message field 'edge'."""
        return self._edge

    @edge.setter
    def edge(self, value: slam_toolbox.msg.GraphEdge) -> None:
        from slam_toolbox.msg import GraphEdge

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, GraphEdge), \
                    "The 'edge' field must be a sub message of type 'GraphEdge'"

        self._edge = value

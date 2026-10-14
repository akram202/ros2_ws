# generated from rosidl_generator_py/resource/_idl.py.em
# with input from slam_toolbox:srv/DeserializePoseGraph.idl
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
    import geometry_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DeserializePoseGraph_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DeserializePoseGraph_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DeserializePoseGraph_RequestConstants(typing.TypedDict):
        UNSET: typing.Literal[0]
        START_AT_FIRST_NODE: typing.Literal[1]
        START_AT_GIVEN_POSE: typing.Literal[2]
        LOCALIZE_AT_POSE: typing.Literal[3]

    __constants: DeserializePoseGraph_RequestConstants = {
        'UNSET': 0,
        'START_AT_FIRST_NODE': 1,
        'START_AT_GIVEN_POSE': 2,
        'LOCALIZE_AT_POSE': 3,
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
                'slam_toolbox.srv.DeserializePoseGraph_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__deserialize_pose_graph__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__deserialize_pose_graph__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__deserialize_pose_graph__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__deserialize_pose_graph__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__deserialize_pose_graph__request

            from geometry_msgs.msg import Pose
            if Pose._TYPE_SUPPORT is None:
                Pose.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'UNSET': metacls.__constants['UNSET'],
            'START_AT_FIRST_NODE': metacls.__constants['START_AT_FIRST_NODE'],
            'START_AT_GIVEN_POSE': metacls.__constants['START_AT_GIVEN_POSE'],
            'LOCALIZE_AT_POSE': metacls.__constants['LOCALIZE_AT_POSE'],
        }

    @property
    def UNSET(self) -> typing.Literal[0]:
        """Message constant 'UNSET'."""
        return Metaclass_DeserializePoseGraph_Request.__constants['UNSET']

    @property
    def START_AT_FIRST_NODE(self) -> typing.Literal[1]:
        """Message constant 'START_AT_FIRST_NODE'."""
        return Metaclass_DeserializePoseGraph_Request.__constants['START_AT_FIRST_NODE']

    @property
    def START_AT_GIVEN_POSE(self) -> typing.Literal[2]:
        """Message constant 'START_AT_GIVEN_POSE'."""
        return Metaclass_DeserializePoseGraph_Request.__constants['START_AT_GIVEN_POSE']

    @property
    def LOCALIZE_AT_POSE(self) -> typing.Literal[3]:
        """Message constant 'LOCALIZE_AT_POSE'."""
        return Metaclass_DeserializePoseGraph_Request.__constants['LOCALIZE_AT_POSE']


class DeserializePoseGraph_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DeserializePoseGraph_Request):
    """
    Message class 'DeserializePoseGraph_Request'.

    Constants:
      UNSET
      START_AT_FIRST_NODE
      START_AT_GIVEN_POSE
      LOCALIZE_AT_POSE
    """

    __slots__ = [
        '_filename',
        '_match_type',
        '_initial_pose',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'filename': 'string',
        'match_type': 'int8',
        'initial_pose': 'geometry_msgs/Pose',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
    )

    def __init__(self, *,
                 filename: typing.Optional[str] = None,  # noqa: E501
                 match_type: typing.Optional[int] = None,  # noqa: E501
                 initial_pose: typing.Optional[geometry_msgs.msg.Pose] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.filename = filename if filename is not None else str()
        self.match_type = match_type if match_type is not None else int()
        from geometry_msgs.msg import Pose
        self.initial_pose = initial_pose if initial_pose is not None else Pose()

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
        if not isinstance(other, DeserializePoseGraph_Request):
            return False
        if self.filename != other.filename:
            return False
        if self.match_type != other.match_type:
            return False
        if self.initial_pose != other.initial_pose:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def filename(self) -> str:
        """Message field 'filename'."""
        return self._filename

    @filename.setter
    def filename(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'filename' field must be of type 'str'"

        self._filename = value

    @builtins.property
    def match_type(self) -> int:
        """Message field 'match_type'."""
        return self._match_type

    @match_type.setter
    def match_type(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'match_type' field must be of type 'int'"
                assert value >= -128 and value < 128, \
                    "The 'match_type' field must be an integer in [-128, 127]"

        self._match_type = value

    @builtins.property
    def initial_pose(self) -> geometry_msgs.msg.Pose:
        """Message field 'initial_pose'."""
        return self._initial_pose

    @initial_pose.setter
    def initial_pose(self, value: geometry_msgs.msg.Pose) -> None:
        from geometry_msgs.msg import Pose

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Pose), \
                    "The 'initial_pose' field must be a sub message of type 'Pose'"

        self._initial_pose = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DeserializePoseGraph_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DeserializePoseGraph_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DeserializePoseGraph_ResponseConstants(typing.TypedDict):
        RESULT_SUCCESS: typing.Literal[0]
        RESULT_INVALID_FILENAME: typing.Literal[1]
        RESULT_INVALID_PROCESSOR_TYPE: typing.Literal[2]
        RESULT_FAILED_TO_READ_FILE: typing.Literal[3]
        RESULT_UNDEFINED_FAILURE: typing.Literal[255]

    __constants: DeserializePoseGraph_ResponseConstants = {
        'RESULT_SUCCESS': 0,
        'RESULT_INVALID_FILENAME': 1,
        'RESULT_INVALID_PROCESSOR_TYPE': 2,
        'RESULT_FAILED_TO_READ_FILE': 3,
        'RESULT_UNDEFINED_FAILURE': 255,
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
                'slam_toolbox.srv.DeserializePoseGraph_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__deserialize_pose_graph__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__deserialize_pose_graph__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__deserialize_pose_graph__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__deserialize_pose_graph__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__deserialize_pose_graph__response

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'RESULT_SUCCESS': metacls.__constants['RESULT_SUCCESS'],
            'RESULT_INVALID_FILENAME': metacls.__constants['RESULT_INVALID_FILENAME'],
            'RESULT_INVALID_PROCESSOR_TYPE': metacls.__constants['RESULT_INVALID_PROCESSOR_TYPE'],
            'RESULT_FAILED_TO_READ_FILE': metacls.__constants['RESULT_FAILED_TO_READ_FILE'],
            'RESULT_UNDEFINED_FAILURE': metacls.__constants['RESULT_UNDEFINED_FAILURE'],
        }

    @property
    def RESULT_SUCCESS(self) -> typing.Literal[0]:
        """Message constant 'RESULT_SUCCESS'."""
        return Metaclass_DeserializePoseGraph_Response.__constants['RESULT_SUCCESS']

    @property
    def RESULT_INVALID_FILENAME(self) -> typing.Literal[1]:
        """Message constant 'RESULT_INVALID_FILENAME'."""
        return Metaclass_DeserializePoseGraph_Response.__constants['RESULT_INVALID_FILENAME']

    @property
    def RESULT_INVALID_PROCESSOR_TYPE(self) -> typing.Literal[2]:
        """Message constant 'RESULT_INVALID_PROCESSOR_TYPE'."""
        return Metaclass_DeserializePoseGraph_Response.__constants['RESULT_INVALID_PROCESSOR_TYPE']

    @property
    def RESULT_FAILED_TO_READ_FILE(self) -> typing.Literal[3]:
        """Message constant 'RESULT_FAILED_TO_READ_FILE'."""
        return Metaclass_DeserializePoseGraph_Response.__constants['RESULT_FAILED_TO_READ_FILE']

    @property
    def RESULT_UNDEFINED_FAILURE(self) -> typing.Literal[255]:
        """Message constant 'RESULT_UNDEFINED_FAILURE'."""
        return Metaclass_DeserializePoseGraph_Response.__constants['RESULT_UNDEFINED_FAILURE']


class DeserializePoseGraph_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DeserializePoseGraph_Response):
    """
    Message class 'DeserializePoseGraph_Response'.

    Constants:
      RESULT_SUCCESS
      RESULT_INVALID_FILENAME
      RESULT_INVALID_PROCESSOR_TYPE
      RESULT_FAILED_TO_READ_FILE
      RESULT_UNDEFINED_FAILURE
    """

    __slots__ = [
        '_result',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'result': 'uint8',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, *,
                 result: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.result = result if result is not None else int()

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
        if not isinstance(other, DeserializePoseGraph_Response):
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def result(self) -> int:
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'result' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'result' field must be an unsigned integer in [0, 255]"

        self._result = value


if typing.TYPE_CHECKING:
    import service_msgs.msg  # noqa: E402, I100, I201, I300
    import slam_toolbox.srv  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DeserializePoseGraph_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DeserializePoseGraph_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DeserializePoseGraph_EventConstants(typing.TypedDict):
        pass

    __constants: DeserializePoseGraph_EventConstants = {
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
                'slam_toolbox.srv.DeserializePoseGraph_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__deserialize_pose_graph__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__deserialize_pose_graph__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__deserialize_pose_graph__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__deserialize_pose_graph__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__deserialize_pose_graph__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo._TYPE_SUPPORT is None:
                ServiceEventInfo.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DeserializePoseGraph_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DeserializePoseGraph_Event):
    """Message class 'DeserializePoseGraph_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<slam_toolbox/DeserializePoseGraph_Request, 1>',
        'response': 'sequence<slam_toolbox/DeserializePoseGraph_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['slam_toolbox', 'srv'], 'DeserializePoseGraph_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['slam_toolbox', 'srv'], 'DeserializePoseGraph_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[slam_toolbox.srv.DeserializePoseGraph_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[slam_toolbox.srv.DeserializePoseGraph_Response]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from service_msgs.msg import ServiceEventInfo
        self.info = info if info is not None else ServiceEventInfo()
        self.request = request if request is not None else []
        self.response = response if response is not None else []

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
        if not isinstance(other, DeserializePoseGraph_Event):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self) -> service_msgs.msg.ServiceEventInfo:
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value: service_msgs.msg.ServiceEventInfo) -> None:
        from service_msgs.msg import ServiceEventInfo

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ServiceEventInfo), \
                    "The 'info' field must be a sub message of type 'ServiceEventInfo'"

        self._info = value

    @builtins.property
    def request(self) -> typing.Annotated[typing.Any, list[slam_toolbox.srv.DeserializePoseGraph_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[slam_toolbox.srv.DeserializePoseGraph_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from slam_toolbox.srv import DeserializePoseGraph_Request

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     len(value) <= 1 and
                     all(isinstance(v, DeserializePoseGraph_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'DeserializePoseGraph_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[slam_toolbox.srv.DeserializePoseGraph_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[slam_toolbox.srv.DeserializePoseGraph_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from slam_toolbox.srv import DeserializePoseGraph_Response

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     len(value) <= 1 and
                     all(isinstance(v, DeserializePoseGraph_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'DeserializePoseGraph_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


if typing.TYPE_CHECKING:
    from typing_extensions import TypeAlias  # noqa: I100, I300


class Metaclass_DeserializePoseGraph(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'DeserializePoseGraph'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('slam_toolbox')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'slam_toolbox.srv.DeserializePoseGraph')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__deserialize_pose_graph

            from slam_toolbox.srv import _deserialize_pose_graph
            if _deserialize_pose_graph.Metaclass_DeserializePoseGraph_Request._TYPE_SUPPORT is None:
                _deserialize_pose_graph.Metaclass_DeserializePoseGraph_Request.__import_type_support__()
            if _deserialize_pose_graph.Metaclass_DeserializePoseGraph_Response._TYPE_SUPPORT is None:
                _deserialize_pose_graph.Metaclass_DeserializePoseGraph_Response.__import_type_support__()
            if _deserialize_pose_graph.Metaclass_DeserializePoseGraph_Event._TYPE_SUPPORT is None:
                _deserialize_pose_graph.Metaclass_DeserializePoseGraph_Event.__import_type_support__()


class DeserializePoseGraph(rosidl_pycommon.interface_base_classes.BaseService[
    DeserializePoseGraph_Request,
    DeserializePoseGraph_Response
], metaclass=Metaclass_DeserializePoseGraph):
    Request: TypeAlias = DeserializePoseGraph_Request
    Response: TypeAlias = DeserializePoseGraph_Response
    Event: TypeAlias = DeserializePoseGraph_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')

# generated from rosidl_generator_py/resource/_idl.py.em
# with input from slam_toolbox:srv/SaveMap.idl
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
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SaveMap_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'SaveMap_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SaveMap_RequestConstants(typing.TypedDict):
        pass

    __constants: SaveMap_RequestConstants = {
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
                'slam_toolbox.srv.SaveMap_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__save_map__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__save_map__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__save_map__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__save_map__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__save_map__request

            from std_msgs.msg import String
            if String._TYPE_SUPPORT is None:
                String.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SaveMap_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_SaveMap_Request):
    """Message class 'SaveMap_Request'."""

    __slots__ = [
        '_name',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'name': 'std_msgs/String',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'String'),  # noqa: E501
    )

    def __init__(self, *,
                 name: typing.Optional[std_msgs.msg.String] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import String
        self.name = name if name is not None else String()

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
        if not isinstance(other, SaveMap_Request):
            return False
        if self.name != other.name:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def name(self) -> std_msgs.msg.String:
        """Message field 'name'."""
        return self._name

    @name.setter
    def name(self, value: std_msgs.msg.String) -> None:
        from std_msgs.msg import String

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, String), \
                    "The 'name' field must be a sub message of type 'String'"

        self._name = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SaveMap_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'SaveMap_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SaveMap_ResponseConstants(typing.TypedDict):
        RESULT_SUCCESS: typing.Literal[0]
        RESULT_NO_MAP_RECEIEVD: typing.Literal[1]
        RESULT_UNDEFINED_FAILURE: typing.Literal[255]

    __constants: SaveMap_ResponseConstants = {
        'RESULT_SUCCESS': 0,
        'RESULT_NO_MAP_RECEIEVD': 1,
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
                'slam_toolbox.srv.SaveMap_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__save_map__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__save_map__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__save_map__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__save_map__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__save_map__response

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'RESULT_SUCCESS': metacls.__constants['RESULT_SUCCESS'],
            'RESULT_NO_MAP_RECEIEVD': metacls.__constants['RESULT_NO_MAP_RECEIEVD'],
            'RESULT_UNDEFINED_FAILURE': metacls.__constants['RESULT_UNDEFINED_FAILURE'],
        }

    @property
    def RESULT_SUCCESS(self) -> typing.Literal[0]:
        """Message constant 'RESULT_SUCCESS'."""
        return Metaclass_SaveMap_Response.__constants['RESULT_SUCCESS']

    @property
    def RESULT_NO_MAP_RECEIEVD(self) -> typing.Literal[1]:
        """Message constant 'RESULT_NO_MAP_RECEIEVD'."""
        return Metaclass_SaveMap_Response.__constants['RESULT_NO_MAP_RECEIEVD']

    @property
    def RESULT_UNDEFINED_FAILURE(self) -> typing.Literal[255]:
        """Message constant 'RESULT_UNDEFINED_FAILURE'."""
        return Metaclass_SaveMap_Response.__constants['RESULT_UNDEFINED_FAILURE']


class SaveMap_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_SaveMap_Response):
    """
    Message class 'SaveMap_Response'.

    Constants:
      RESULT_SUCCESS
      RESULT_NO_MAP_RECEIEVD
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
        if not isinstance(other, SaveMap_Response):
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


class Metaclass_SaveMap_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'SaveMap_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SaveMap_EventConstants(typing.TypedDict):
        pass

    __constants: SaveMap_EventConstants = {
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
                'slam_toolbox.srv.SaveMap_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__save_map__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__save_map__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__save_map__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__save_map__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__save_map__event

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


class SaveMap_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_SaveMap_Event):
    """Message class 'SaveMap_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<slam_toolbox/SaveMap_Request, 1>',
        'response': 'sequence<slam_toolbox/SaveMap_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['slam_toolbox', 'srv'], 'SaveMap_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['slam_toolbox', 'srv'], 'SaveMap_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[slam_toolbox.srv.SaveMap_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[slam_toolbox.srv.SaveMap_Response]] = None,  # noqa: E501
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
        if not isinstance(other, SaveMap_Event):
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
    def request(self) -> typing.Annotated[typing.Any, list[slam_toolbox.srv.SaveMap_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[slam_toolbox.srv.SaveMap_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from slam_toolbox.srv import SaveMap_Request

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
                     all(isinstance(v, SaveMap_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'SaveMap_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[slam_toolbox.srv.SaveMap_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[slam_toolbox.srv.SaveMap_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from slam_toolbox.srv import SaveMap_Response

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
                     all(isinstance(v, SaveMap_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'SaveMap_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


if typing.TYPE_CHECKING:
    from typing_extensions import TypeAlias  # noqa: I100, I300


class Metaclass_SaveMap(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'SaveMap'."""

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
                'slam_toolbox.srv.SaveMap')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__save_map

            from slam_toolbox.srv import _save_map
            if _save_map.Metaclass_SaveMap_Request._TYPE_SUPPORT is None:
                _save_map.Metaclass_SaveMap_Request.__import_type_support__()
            if _save_map.Metaclass_SaveMap_Response._TYPE_SUPPORT is None:
                _save_map.Metaclass_SaveMap_Response.__import_type_support__()
            if _save_map.Metaclass_SaveMap_Event._TYPE_SUPPORT is None:
                _save_map.Metaclass_SaveMap_Event.__import_type_support__()


class SaveMap(rosidl_pycommon.interface_base_classes.BaseService[
    SaveMap_Request,
    SaveMap_Response
], metaclass=Metaclass_SaveMap):
    Request: TypeAlias = SaveMap_Request
    Response: TypeAlias = SaveMap_Response
    Event: TypeAlias = SaveMap_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')

# generated from rosidl_generator_py/resource/_idl.py.em
# with input from explore_lite_msgs:msg/ExploreStatus.idl
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


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ExploreStatus(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ExploreStatus'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ExploreStatusConstants(typing.TypedDict):
        EXPLORATION_STARTED: typing.Literal['exploration_started']
        EXPLORATION_IN_PROGRESS: typing.Literal['exploration_in_progress']
        EXPLORATION_PAUSED: typing.Literal['exploration_paused']
        EXPLORATION_COMPLETE: typing.Literal['exploration_complete']
        RETURNING_TO_ORIGIN: typing.Literal['returning_to_origin']
        RETURNED_TO_ORIGIN: typing.Literal['returned_to_origin']

    __constants: ExploreStatusConstants = {
        'EXPLORATION_STARTED': 'exploration_started',
        'EXPLORATION_IN_PROGRESS': 'exploration_in_progress',
        'EXPLORATION_PAUSED': 'exploration_paused',
        'EXPLORATION_COMPLETE': 'exploration_complete',
        'RETURNING_TO_ORIGIN': 'returning_to_origin',
        'RETURNED_TO_ORIGIN': 'returned_to_origin',
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('explore_lite_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'explore_lite_msgs.msg.ExploreStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__explore_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__explore_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__explore_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__explore_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__explore_status

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'EXPLORATION_STARTED': metacls.__constants['EXPLORATION_STARTED'],
            'EXPLORATION_IN_PROGRESS': metacls.__constants['EXPLORATION_IN_PROGRESS'],
            'EXPLORATION_PAUSED': metacls.__constants['EXPLORATION_PAUSED'],
            'EXPLORATION_COMPLETE': metacls.__constants['EXPLORATION_COMPLETE'],
            'RETURNING_TO_ORIGIN': metacls.__constants['RETURNING_TO_ORIGIN'],
            'RETURNED_TO_ORIGIN': metacls.__constants['RETURNED_TO_ORIGIN'],
        }

    @property
    def EXPLORATION_STARTED(self) -> typing.Literal['exploration_started']:
        """Message constant 'EXPLORATION_STARTED'."""
        return Metaclass_ExploreStatus.__constants['EXPLORATION_STARTED']

    @property
    def EXPLORATION_IN_PROGRESS(self) -> typing.Literal['exploration_in_progress']:
        """Message constant 'EXPLORATION_IN_PROGRESS'."""
        return Metaclass_ExploreStatus.__constants['EXPLORATION_IN_PROGRESS']

    @property
    def EXPLORATION_PAUSED(self) -> typing.Literal['exploration_paused']:
        """Message constant 'EXPLORATION_PAUSED'."""
        return Metaclass_ExploreStatus.__constants['EXPLORATION_PAUSED']

    @property
    def EXPLORATION_COMPLETE(self) -> typing.Literal['exploration_complete']:
        """Message constant 'EXPLORATION_COMPLETE'."""
        return Metaclass_ExploreStatus.__constants['EXPLORATION_COMPLETE']

    @property
    def RETURNING_TO_ORIGIN(self) -> typing.Literal['returning_to_origin']:
        """Message constant 'RETURNING_TO_ORIGIN'."""
        return Metaclass_ExploreStatus.__constants['RETURNING_TO_ORIGIN']

    @property
    def RETURNED_TO_ORIGIN(self) -> typing.Literal['returned_to_origin']:
        """Message constant 'RETURNED_TO_ORIGIN'."""
        return Metaclass_ExploreStatus.__constants['RETURNED_TO_ORIGIN']


class ExploreStatus(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ExploreStatus):
    """
    Message class 'ExploreStatus'.

    Constants:
      EXPLORATION_STARTED
      EXPLORATION_IN_PROGRESS
      EXPLORATION_PAUSED
      EXPLORATION_COMPLETE
      RETURNING_TO_ORIGIN
      RETURNED_TO_ORIGIN
    """

    __slots__ = [
        '_status',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'status': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 status: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.status = status if status is not None else str()

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
        if not isinstance(other, ExploreStatus):
            return False
        if self.status != other.status:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self) -> str:
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'status' field must be of type 'str'"

        self._status = value

// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from slam_toolbox:srv/AddSubmap.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "slam_toolbox/srv/add_submap.hpp"


#ifndef SLAM_TOOLBOX__SRV__DETAIL__ADD_SUBMAP__TRAITS_HPP_
#define SLAM_TOOLBOX__SRV__DETAIL__ADD_SUBMAP__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "slam_toolbox/srv/detail/add_submap__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddSubmap_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: filename
  {
    out << "filename: ";
    rosidl_generator_traits::value_to_yaml(msg.filename, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddSubmap_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: filename
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "filename: ";
    rosidl_generator_traits::value_to_yaml(msg.filename, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddSubmap_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, slam_toolbox::srv::AddSubmap_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).filename);
}

}  // namespace srv

}  // namespace slam_toolbox

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<slam_toolbox::srv::AddSubmap_Request>()
{
  return "slam_toolbox::srv::AddSubmap_Request";
}

template<>
constexpr const char * name<slam_toolbox::srv::AddSubmap_Request>()
{
  return "slam_toolbox/srv/AddSubmap_Request";
}

template<>
struct has_fixed_size<slam_toolbox::srv::AddSubmap_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<slam_toolbox::srv::AddSubmap_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<slam_toolbox::srv::AddSubmap_Request>
  : std::true_type {};

template<>
struct MessageTraits<slam_toolbox::srv::AddSubmap_Request>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "filename",
  };
};

}  // namespace rosidl_generator_traits

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddSubmap_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddSubmap_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddSubmap_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, slam_toolbox::srv::AddSubmap_Response>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).structure_needs_at_least_one_member);
}

}  // namespace srv

}  // namespace slam_toolbox

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<slam_toolbox::srv::AddSubmap_Response>()
{
  return "slam_toolbox::srv::AddSubmap_Response";
}

template<>
constexpr const char * name<slam_toolbox::srv::AddSubmap_Response>()
{
  return "slam_toolbox/srv/AddSubmap_Response";
}

template<>
struct has_fixed_size<slam_toolbox::srv::AddSubmap_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<slam_toolbox::srv::AddSubmap_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<slam_toolbox::srv::AddSubmap_Response>
  : std::true_type {};

template<>
struct MessageTraits<slam_toolbox::srv::AddSubmap_Response>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "structure_needs_at_least_one_member",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddSubmap_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddSubmap_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddSubmap_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, slam_toolbox::srv::AddSubmap_Event>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).info,
    std::forward<T>(msg).request,
    std::forward<T>(msg).response);
}

}  // namespace srv

}  // namespace slam_toolbox

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<slam_toolbox::srv::AddSubmap_Event>()
{
  return "slam_toolbox::srv::AddSubmap_Event";
}

template<>
constexpr const char * name<slam_toolbox::srv::AddSubmap_Event>()
{
  return "slam_toolbox/srv/AddSubmap_Event";
}

template<>
struct has_fixed_size<slam_toolbox::srv::AddSubmap_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<slam_toolbox::srv::AddSubmap_Event>
  : std::integral_constant<bool, has_bounded_size<service_msgs::msg::ServiceEventInfo>::value && has_bounded_size<slam_toolbox::srv::AddSubmap_Request>::value && has_bounded_size<slam_toolbox::srv::AddSubmap_Response>::value> {};

template<>
struct is_message<slam_toolbox::srv::AddSubmap_Event>
  : std::true_type {};

template<>
struct MessageTraits<slam_toolbox::srv::AddSubmap_Event>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "info",
    "request",
    "response",
  };
};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<slam_toolbox::srv::AddSubmap>()
{
  return "slam_toolbox::srv::AddSubmap";
}

template<>
constexpr const char * name<slam_toolbox::srv::AddSubmap>()
{
  return "slam_toolbox/srv/AddSubmap";
}

template<>
struct has_fixed_size<slam_toolbox::srv::AddSubmap>
  : std::integral_constant<
    bool,
    has_fixed_size<slam_toolbox::srv::AddSubmap_Request>::value &&
    has_fixed_size<slam_toolbox::srv::AddSubmap_Response>::value
  >
{
};

template<>
struct has_bounded_size<slam_toolbox::srv::AddSubmap>
  : std::integral_constant<
    bool,
    has_bounded_size<slam_toolbox::srv::AddSubmap_Request>::value &&
    has_bounded_size<slam_toolbox::srv::AddSubmap_Response>::value
  >
{
};

template<>
struct is_service<slam_toolbox::srv::AddSubmap>
  : std::true_type
{
};

template<>
struct is_service_request<slam_toolbox::srv::AddSubmap_Request>
  : std::true_type
{
};

template<>
struct is_service_response<slam_toolbox::srv::AddSubmap_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SLAM_TOOLBOX__SRV__DETAIL__ADD_SUBMAP__TRAITS_HPP_

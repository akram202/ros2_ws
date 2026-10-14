// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from slam_toolbox:msg/GraphEdge.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "slam_toolbox/msg/graph_edge.hpp"


#ifndef SLAM_TOOLBOX__MSG__DETAIL__GRAPH_EDGE__TRAITS_HPP_
#define SLAM_TOOLBOX__MSG__DETAIL__GRAPH_EDGE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "slam_toolbox/msg/detail/graph_edge__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'relative_pose'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace slam_toolbox
{

namespace msg
{

inline void to_flow_style_yaml(
  const GraphEdge & msg,
  std::ostream & out)
{
  out << "{";
  // member: source_id
  {
    out << "source_id: ";
    rosidl_generator_traits::value_to_yaml(msg.source_id, out);
    out << ", ";
  }

  // member: target_id
  {
    out << "target_id: ";
    rosidl_generator_traits::value_to_yaml(msg.target_id, out);
    out << ", ";
  }

  // member: relative_pose
  {
    out << "relative_pose: ";
    to_flow_style_yaml(msg.relative_pose, out);
    out << ", ";
  }

  // member: covariance
  {
    if (msg.covariance.size() == 0) {
      out << "covariance: []";
    } else {
      out << "covariance: [";
      size_t pending_items = msg.covariance.size();
      for (auto item : msg.covariance) {
        rosidl_generator_traits::value_to_yaml(item, out);
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
  const GraphEdge & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: source_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "source_id: ";
    rosidl_generator_traits::value_to_yaml(msg.source_id, out);
    out << "\n";
  }

  // member: target_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_id: ";
    rosidl_generator_traits::value_to_yaml(msg.target_id, out);
    out << "\n";
  }

  // member: relative_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "relative_pose:\n";
    to_block_style_yaml(msg.relative_pose, out, indentation + 2);
  }

  // member: covariance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.covariance.size() == 0) {
      out << "covariance: []\n";
    } else {
      out << "covariance:\n";
      for (auto item : msg.covariance) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GraphEdge & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, slam_toolbox::msg::GraphEdge>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).source_id,
    std::forward<T>(msg).target_id,
    std::forward<T>(msg).relative_pose,
    std::forward<T>(msg).covariance);
}

}  // namespace msg

}  // namespace slam_toolbox

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<slam_toolbox::msg::GraphEdge>()
{
  return "slam_toolbox::msg::GraphEdge";
}

template<>
constexpr const char * name<slam_toolbox::msg::GraphEdge>()
{
  return "slam_toolbox/msg/GraphEdge";
}

template<>
struct has_fixed_size<slam_toolbox::msg::GraphEdge>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct has_bounded_size<slam_toolbox::msg::GraphEdge>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct is_message<slam_toolbox::msg::GraphEdge>
  : std::true_type {};

template<>
struct MessageTraits<slam_toolbox::msg::GraphEdge>
{
  static constexpr std::size_t member_count = 4;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "source_id",
    "target_id",
    "relative_pose",
    "covariance",
  };
};

}  // namespace rosidl_generator_traits

#endif  // SLAM_TOOLBOX__MSG__DETAIL__GRAPH_EDGE__TRAITS_HPP_

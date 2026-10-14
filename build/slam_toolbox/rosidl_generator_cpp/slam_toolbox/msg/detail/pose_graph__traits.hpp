// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from slam_toolbox:msg/PoseGraph.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "slam_toolbox/msg/pose_graph.hpp"


#ifndef SLAM_TOOLBOX__MSG__DETAIL__POSE_GRAPH__TRAITS_HPP_
#define SLAM_TOOLBOX__MSG__DETAIL__POSE_GRAPH__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "slam_toolbox/msg/detail/pose_graph__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'nodes'
#include "slam_toolbox/msg/detail/graph_node__traits.hpp"
// Member 'edges'
#include "slam_toolbox/msg/detail/graph_edge__traits.hpp"

namespace slam_toolbox
{

namespace msg
{

inline void to_flow_style_yaml(
  const PoseGraph & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: nodes
  {
    if (msg.nodes.size() == 0) {
      out << "nodes: []";
    } else {
      out << "nodes: [";
      size_t pending_items = msg.nodes.size();
      for (auto item : msg.nodes) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: edges
  {
    if (msg.edges.size() == 0) {
      out << "edges: []";
    } else {
      out << "edges: [";
      size_t pending_items = msg.edges.size();
      for (auto item : msg.edges) {
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
  const PoseGraph & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: nodes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.nodes.size() == 0) {
      out << "nodes: []\n";
    } else {
      out << "nodes:\n";
      for (auto item : msg.nodes) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: edges
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.edges.size() == 0) {
      out << "edges: []\n";
    } else {
      out << "edges:\n";
      for (auto item : msg.edges) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PoseGraph & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, slam_toolbox::msg::PoseGraph>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).nodes,
    std::forward<T>(msg).edges);
}

}  // namespace msg

}  // namespace slam_toolbox

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<slam_toolbox::msg::PoseGraph>()
{
  return "slam_toolbox::msg::PoseGraph";
}

template<>
constexpr const char * name<slam_toolbox::msg::PoseGraph>()
{
  return "slam_toolbox/msg/PoseGraph";
}

template<>
struct has_fixed_size<slam_toolbox::msg::PoseGraph>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<slam_toolbox::msg::PoseGraph>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<slam_toolbox::msg::PoseGraph>
  : std::true_type {};

template<>
struct MessageTraits<slam_toolbox::msg::PoseGraph>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "nodes",
    "edges",
  };
};

}  // namespace rosidl_generator_traits

#endif  // SLAM_TOOLBOX__MSG__DETAIL__POSE_GRAPH__TRAITS_HPP_

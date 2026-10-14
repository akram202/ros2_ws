// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from explore_lite_msgs:msg/ExploreStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "explore_lite_msgs/msg/explore_status.hpp"


#ifndef EXPLORE_LITE_MSGS__MSG__DETAIL__EXPLORE_STATUS__TRAITS_HPP_
#define EXPLORE_LITE_MSGS__MSG__DETAIL__EXPLORE_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "explore_lite_msgs/msg/detail/explore_status__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace explore_lite_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ExploreStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ExploreStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ExploreStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, explore_lite_msgs::msg::ExploreStatus>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).status);
}

}  // namespace msg

}  // namespace explore_lite_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<explore_lite_msgs::msg::ExploreStatus>()
{
  return "explore_lite_msgs::msg::ExploreStatus";
}

template<>
constexpr const char * name<explore_lite_msgs::msg::ExploreStatus>()
{
  return "explore_lite_msgs/msg/ExploreStatus";
}

template<>
struct has_fixed_size<explore_lite_msgs::msg::ExploreStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<explore_lite_msgs::msg::ExploreStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<explore_lite_msgs::msg::ExploreStatus>
  : std::true_type {};

template<>
struct MessageTraits<explore_lite_msgs::msg::ExploreStatus>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "status",
  };
};

}  // namespace rosidl_generator_traits

#endif  // EXPLORE_LITE_MSGS__MSG__DETAIL__EXPLORE_STATUS__TRAITS_HPP_

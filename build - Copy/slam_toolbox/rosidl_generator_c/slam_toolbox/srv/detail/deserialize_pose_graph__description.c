// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from slam_toolbox:srv/DeserializePoseGraph.idl
// generated code does not contain a copyright notice

#include "slam_toolbox/srv/detail/deserialize_pose_graph__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_slam_toolbox
const rosidl_type_hash_t *
slam_toolbox__srv__DeserializePoseGraph__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x29, 0x08, 0x2f, 0x1f, 0x78, 0xe2, 0x98, 0x4a,
      0x8c, 0xe3, 0x5d, 0x68, 0xd8, 0x8f, 0x49, 0xab,
      0xae, 0x6d, 0xa0, 0x30, 0x58, 0x8c, 0x19, 0x36,
      0xe0, 0xc6, 0xea, 0x42, 0x64, 0xa6, 0x08, 0xa5,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_slam_toolbox
const rosidl_type_hash_t *
slam_toolbox__srv__DeserializePoseGraph_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x68, 0x11, 0x1a, 0x42, 0x01, 0x16, 0xdf, 0x82,
      0x26, 0xd4, 0x1e, 0x13, 0xe1, 0x90, 0x13, 0x2a,
      0xeb, 0x98, 0xd6, 0x62, 0xf9, 0xd5, 0x96, 0x58,
      0x9d, 0x27, 0x74, 0x4a, 0x3c, 0x2d, 0x7f, 0x19,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_slam_toolbox
const rosidl_type_hash_t *
slam_toolbox__srv__DeserializePoseGraph_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x52, 0xab, 0xe6, 0xd4, 0x9f, 0x62, 0xe7, 0x3e,
      0x0a, 0x3a, 0xf2, 0x04, 0xd5, 0x9d, 0x43, 0xb1,
      0x6d, 0x8f, 0xa4, 0xdd, 0xe0, 0xeb, 0x3a, 0xa8,
      0x97, 0xc8, 0x58, 0x3f, 0x45, 0xb7, 0xb5, 0x8b,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_slam_toolbox
const rosidl_type_hash_t *
slam_toolbox__srv__DeserializePoseGraph_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x10, 0x9d, 0xd3, 0xae, 0xc9, 0xbe, 0xa8, 0xcf,
      0xe7, 0xbd, 0x0f, 0x45, 0x99, 0xf5, 0x34, 0xae,
      0x9b, 0xcb, 0xbf, 0x48, 0x21, 0x6c, 0xee, 0xd6,
      0x89, 0x6e, 0x50, 0x14, 0x78, 0xbc, 0xf2, 0x0a,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "geometry_msgs/msg/detail/point__functions.h"
#include "geometry_msgs/msg/detail/pose__functions.h"
#include "geometry_msgs/msg/detail/quaternion__functions.h"
#include "service_msgs/msg/detail/service_event_info__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t geometry_msgs__msg__Point__EXPECTED_HASH = {1, {
    0x69, 0x63, 0x08, 0x48, 0x42, 0xa9, 0xb0, 0x44,
    0x94, 0xd6, 0xb2, 0x94, 0x1d, 0x11, 0x44, 0x47,
    0x08, 0xd8, 0x92, 0xda, 0x2f, 0x4b, 0x09, 0x84,
    0x3b, 0x9c, 0x43, 0xf4, 0x2a, 0x7f, 0x68, 0x81,
  }};
static const rosidl_type_hash_t geometry_msgs__msg__Pose__EXPECTED_HASH = {1, {
    0xd5, 0x01, 0x95, 0x4e, 0x94, 0x76, 0xce, 0xa2,
    0x99, 0x69, 0x84, 0xe8, 0x12, 0x05, 0x4b, 0x68,
    0x02, 0x6a, 0xe0, 0xbf, 0xae, 0x78, 0x9d, 0x9a,
    0x10, 0xb2, 0x3d, 0xaf, 0x35, 0xcc, 0x90, 0xfa,
  }};
static const rosidl_type_hash_t geometry_msgs__msg__Quaternion__EXPECTED_HASH = {1, {
    0x8a, 0x76, 0x5f, 0x66, 0x77, 0x8c, 0x8f, 0xf7,
    0xc8, 0xab, 0x94, 0xaf, 0xcc, 0x59, 0x0a, 0x2e,
    0xd5, 0x32, 0x5a, 0x1d, 0x9a, 0x07, 0x6f, 0xff,
    0xf3, 0x8f, 0xbc, 0xe3, 0x6f, 0x45, 0x86, 0x84,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char slam_toolbox__srv__DeserializePoseGraph__TYPE_NAME[] = "slam_toolbox/srv/DeserializePoseGraph";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char geometry_msgs__msg__Point__TYPE_NAME[] = "geometry_msgs/msg/Point";
static char geometry_msgs__msg__Pose__TYPE_NAME[] = "geometry_msgs/msg/Pose";
static char geometry_msgs__msg__Quaternion__TYPE_NAME[] = "geometry_msgs/msg/Quaternion";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";
static char slam_toolbox__srv__DeserializePoseGraph_Event__TYPE_NAME[] = "slam_toolbox/srv/DeserializePoseGraph_Event";
static char slam_toolbox__srv__DeserializePoseGraph_Request__TYPE_NAME[] = "slam_toolbox/srv/DeserializePoseGraph_Request";
static char slam_toolbox__srv__DeserializePoseGraph_Response__TYPE_NAME[] = "slam_toolbox/srv/DeserializePoseGraph_Response";

// Define type names, field names, and default values
static char slam_toolbox__srv__DeserializePoseGraph__FIELD_NAME__request_message[] = "request_message";
static char slam_toolbox__srv__DeserializePoseGraph__FIELD_NAME__response_message[] = "response_message";
static char slam_toolbox__srv__DeserializePoseGraph__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field slam_toolbox__srv__DeserializePoseGraph__FIELDS[] = {
  {
    {slam_toolbox__srv__DeserializePoseGraph__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {slam_toolbox__srv__DeserializePoseGraph_Request__TYPE_NAME, 45, 45},
    },
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {slam_toolbox__srv__DeserializePoseGraph_Response__TYPE_NAME, 46, 46},
    },
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {slam_toolbox__srv__DeserializePoseGraph_Event__TYPE_NAME, 43, 43},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription slam_toolbox__srv__DeserializePoseGraph__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Point__TYPE_NAME, 23, 23},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Pose__TYPE_NAME, 22, 22},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Quaternion__TYPE_NAME, 28, 28},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Event__TYPE_NAME, 43, 43},
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Request__TYPE_NAME, 45, 45},
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Response__TYPE_NAME, 46, 46},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
slam_toolbox__srv__DeserializePoseGraph__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {slam_toolbox__srv__DeserializePoseGraph__TYPE_NAME, 37, 37},
      {slam_toolbox__srv__DeserializePoseGraph__FIELDS, 3, 3},
    },
    {slam_toolbox__srv__DeserializePoseGraph__REFERENCED_TYPE_DESCRIPTIONS, 8, 8},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Point__EXPECTED_HASH, geometry_msgs__msg__Point__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = geometry_msgs__msg__Point__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Pose__EXPECTED_HASH, geometry_msgs__msg__Pose__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = geometry_msgs__msg__Pose__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Quaternion__EXPECTED_HASH, geometry_msgs__msg__Quaternion__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = geometry_msgs__msg__Quaternion__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[5].fields = slam_toolbox__srv__DeserializePoseGraph_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[6].fields = slam_toolbox__srv__DeserializePoseGraph_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[7].fields = slam_toolbox__srv__DeserializePoseGraph_Response__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char slam_toolbox__srv__DeserializePoseGraph_Request__FIELD_NAME__filename[] = "filename";
static char slam_toolbox__srv__DeserializePoseGraph_Request__FIELD_NAME__match_type[] = "match_type";
static char slam_toolbox__srv__DeserializePoseGraph_Request__FIELD_NAME__initial_pose[] = "initial_pose";

static rosidl_runtime_c__type_description__Field slam_toolbox__srv__DeserializePoseGraph_Request__FIELDS[] = {
  {
    {slam_toolbox__srv__DeserializePoseGraph_Request__FIELD_NAME__filename, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Request__FIELD_NAME__match_type, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Request__FIELD_NAME__initial_pose, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {geometry_msgs__msg__Pose__TYPE_NAME, 22, 22},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription slam_toolbox__srv__DeserializePoseGraph_Request__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {geometry_msgs__msg__Point__TYPE_NAME, 23, 23},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Pose__TYPE_NAME, 22, 22},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Quaternion__TYPE_NAME, 28, 28},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
slam_toolbox__srv__DeserializePoseGraph_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {slam_toolbox__srv__DeserializePoseGraph_Request__TYPE_NAME, 45, 45},
      {slam_toolbox__srv__DeserializePoseGraph_Request__FIELDS, 3, 3},
    },
    {slam_toolbox__srv__DeserializePoseGraph_Request__REFERENCED_TYPE_DESCRIPTIONS, 3, 3},
  };
  if (!constructed) {
    assert(0 == memcmp(&geometry_msgs__msg__Point__EXPECTED_HASH, geometry_msgs__msg__Point__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = geometry_msgs__msg__Point__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Pose__EXPECTED_HASH, geometry_msgs__msg__Pose__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = geometry_msgs__msg__Pose__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Quaternion__EXPECTED_HASH, geometry_msgs__msg__Quaternion__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = geometry_msgs__msg__Quaternion__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char slam_toolbox__srv__DeserializePoseGraph_Response__FIELD_NAME__result[] = "result";

static rosidl_runtime_c__type_description__Field slam_toolbox__srv__DeserializePoseGraph_Response__FIELDS[] = {
  {
    {slam_toolbox__srv__DeserializePoseGraph_Response__FIELD_NAME__result, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
slam_toolbox__srv__DeserializePoseGraph_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {slam_toolbox__srv__DeserializePoseGraph_Response__TYPE_NAME, 46, 46},
      {slam_toolbox__srv__DeserializePoseGraph_Response__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char slam_toolbox__srv__DeserializePoseGraph_Event__FIELD_NAME__info[] = "info";
static char slam_toolbox__srv__DeserializePoseGraph_Event__FIELD_NAME__request[] = "request";
static char slam_toolbox__srv__DeserializePoseGraph_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field slam_toolbox__srv__DeserializePoseGraph_Event__FIELDS[] = {
  {
    {slam_toolbox__srv__DeserializePoseGraph_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {slam_toolbox__srv__DeserializePoseGraph_Request__TYPE_NAME, 45, 45},
    },
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {slam_toolbox__srv__DeserializePoseGraph_Response__TYPE_NAME, 46, 46},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription slam_toolbox__srv__DeserializePoseGraph_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Point__TYPE_NAME, 23, 23},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Pose__TYPE_NAME, 22, 22},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Quaternion__TYPE_NAME, 28, 28},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Request__TYPE_NAME, 45, 45},
    {NULL, 0, 0},
  },
  {
    {slam_toolbox__srv__DeserializePoseGraph_Response__TYPE_NAME, 46, 46},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
slam_toolbox__srv__DeserializePoseGraph_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {slam_toolbox__srv__DeserializePoseGraph_Event__TYPE_NAME, 43, 43},
      {slam_toolbox__srv__DeserializePoseGraph_Event__FIELDS, 3, 3},
    },
    {slam_toolbox__srv__DeserializePoseGraph_Event__REFERENCED_TYPE_DESCRIPTIONS, 7, 7},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Point__EXPECTED_HASH, geometry_msgs__msg__Point__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = geometry_msgs__msg__Point__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Pose__EXPECTED_HASH, geometry_msgs__msg__Pose__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = geometry_msgs__msg__Pose__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Quaternion__EXPECTED_HASH, geometry_msgs__msg__Quaternion__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = geometry_msgs__msg__Quaternion__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[5].fields = slam_toolbox__srv__DeserializePoseGraph_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[6].fields = slam_toolbox__srv__DeserializePoseGraph_Response__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int8 UNSET = 0\n"
  "int8 START_AT_FIRST_NODE = 1\n"
  "int8 START_AT_GIVEN_POSE = 2\n"
  "int8 LOCALIZE_AT_POSE = 3\n"
  "\n"
  "# inital_pose should be Map -> base_frame (parameter, generally base_link)\n"
  "#\n"
  "\n"
  "string filename\n"
  "int8 match_type\n"
  "geometry_msgs/Pose initial_pose\n"
  "---\n"
  "\n"
  "# Result code definitions\n"
  "uint8 RESULT_SUCCESS=0\n"
  "uint8 RESULT_INVALID_FILENAME=1\n"
  "uint8 RESULT_INVALID_PROCESSOR_TYPE=2\n"
  "uint8 RESULT_FAILED_TO_READ_FILE=3\n"
  "uint8 RESULT_UNDEFINED_FAILURE=255\n"
  "\n"
  "uint8 result";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
slam_toolbox__srv__DeserializePoseGraph__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {slam_toolbox__srv__DeserializePoseGraph__TYPE_NAME, 37, 37},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 449, 449},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
slam_toolbox__srv__DeserializePoseGraph_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {slam_toolbox__srv__DeserializePoseGraph_Request__TYPE_NAME, 45, 45},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
slam_toolbox__srv__DeserializePoseGraph_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {slam_toolbox__srv__DeserializePoseGraph_Response__TYPE_NAME, 46, 46},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
slam_toolbox__srv__DeserializePoseGraph_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {slam_toolbox__srv__DeserializePoseGraph_Event__TYPE_NAME, 43, 43},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
slam_toolbox__srv__DeserializePoseGraph__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[9];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 9, 9};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *slam_toolbox__srv__DeserializePoseGraph__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *geometry_msgs__msg__Point__get_individual_type_description_source(NULL);
    sources[3] = *geometry_msgs__msg__Pose__get_individual_type_description_source(NULL);
    sources[4] = *geometry_msgs__msg__Quaternion__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[6] = *slam_toolbox__srv__DeserializePoseGraph_Event__get_individual_type_description_source(NULL);
    sources[7] = *slam_toolbox__srv__DeserializePoseGraph_Request__get_individual_type_description_source(NULL);
    sources[8] = *slam_toolbox__srv__DeserializePoseGraph_Response__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
slam_toolbox__srv__DeserializePoseGraph_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[4];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 4, 4};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *slam_toolbox__srv__DeserializePoseGraph_Request__get_individual_type_description_source(NULL),
    sources[1] = *geometry_msgs__msg__Point__get_individual_type_description_source(NULL);
    sources[2] = *geometry_msgs__msg__Pose__get_individual_type_description_source(NULL);
    sources[3] = *geometry_msgs__msg__Quaternion__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
slam_toolbox__srv__DeserializePoseGraph_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *slam_toolbox__srv__DeserializePoseGraph_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
slam_toolbox__srv__DeserializePoseGraph_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[8];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 8, 8};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *slam_toolbox__srv__DeserializePoseGraph_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *geometry_msgs__msg__Point__get_individual_type_description_source(NULL);
    sources[3] = *geometry_msgs__msg__Pose__get_individual_type_description_source(NULL);
    sources[4] = *geometry_msgs__msg__Quaternion__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[6] = *slam_toolbox__srv__DeserializePoseGraph_Request__get_individual_type_description_source(NULL);
    sources[7] = *slam_toolbox__srv__DeserializePoseGraph_Response__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

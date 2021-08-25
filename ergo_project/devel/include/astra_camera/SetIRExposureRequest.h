// Generated by gencpp from file astra_camera/SetIRExposureRequest.msg
// DO NOT EDIT!


#ifndef ASTRA_CAMERA_MESSAGE_SETIREXPOSUREREQUEST_H
#define ASTRA_CAMERA_MESSAGE_SETIREXPOSUREREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace astra_camera
{
template <class ContainerAllocator>
struct SetIRExposureRequest_
{
  typedef SetIRExposureRequest_<ContainerAllocator> Type;

  SetIRExposureRequest_()
    : exposure(0)  {
    }
  SetIRExposureRequest_(const ContainerAllocator& _alloc)
    : exposure(0)  {
  (void)_alloc;
    }



   typedef int32_t _exposure_type;
  _exposure_type exposure;





  typedef boost::shared_ptr< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetIRExposureRequest_

typedef ::astra_camera::SetIRExposureRequest_<std::allocator<void> > SetIRExposureRequest;

typedef boost::shared_ptr< ::astra_camera::SetIRExposureRequest > SetIRExposureRequestPtr;
typedef boost::shared_ptr< ::astra_camera::SetIRExposureRequest const> SetIRExposureRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::astra_camera::SetIRExposureRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::astra_camera::SetIRExposureRequest_<ContainerAllocator1> & lhs, const ::astra_camera::SetIRExposureRequest_<ContainerAllocator2> & rhs)
{
  return lhs.exposure == rhs.exposure;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::astra_camera::SetIRExposureRequest_<ContainerAllocator1> & lhs, const ::astra_camera::SetIRExposureRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace astra_camera

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0535ed1a1204bb999d0e7bea8f6c3c81";
  }

  static const char* value(const ::astra_camera::SetIRExposureRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0535ed1a1204bb99ULL;
  static const uint64_t static_value2 = 0x9d0e7bea8f6c3c81ULL;
};

template<class ContainerAllocator>
struct DataType< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "astra_camera/SetIRExposureRequest";
  }

  static const char* value(const ::astra_camera::SetIRExposureRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 exposure\n"
;
  }

  static const char* value(const ::astra_camera::SetIRExposureRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.exposure);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetIRExposureRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::astra_camera::SetIRExposureRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::astra_camera::SetIRExposureRequest_<ContainerAllocator>& v)
  {
    s << indent << "exposure: ";
    Printer<int32_t>::stream(s, indent + "  ", v.exposure);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ASTRA_CAMERA_MESSAGE_SETIREXPOSUREREQUEST_H

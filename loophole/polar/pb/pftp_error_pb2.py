# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pftp_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pftp_error.proto',
  package='protocol',
  serialized_pb=_b('\n\x10pftp_error.proto\x12\x08protocol*\xdf\x03\n\x0bPbPFtpError\x12\x17\n\x13OPERATION_SUCCEEDED\x10\x00\x12\r\n\tREBOOTING\x10\x01\x12\r\n\tTRY_AGAIN\x10\x02\x12\x1b\n\x17UNIDENTIFIED_HOST_ERROR\x10\x64\x12\x13\n\x0fINVALID_COMMAND\x10\x65\x12\x15\n\x11INVALID_PARAMETER\x10\x66\x12\x1d\n\x19NO_SUCH_FILE_OR_DIRECTORY\x10g\x12\x14\n\x10\x44IRECTORY_EXISTS\x10h\x12\x0f\n\x0b\x46ILE_EXISTS\x10i\x12\x1b\n\x17OPERATION_NOT_PERMITTED\x10j\x12\x10\n\x0cNO_SUCH_USER\x10k\x12\x0b\n\x07TIMEOUT\x10l\x12\x1e\n\x19UNIDENTIFIED_DEVICE_ERROR\x10\xc8\x01\x12\x14\n\x0fNOT_IMPLEMENTED\x10\xc9\x01\x12\x10\n\x0bSYSTEM_BUSY\x10\xca\x01\x12\x14\n\x0fINVALID_CONTENT\x10\xcb\x01\x12\x15\n\x10\x43HECKSUM_FAILURE\x10\xcc\x01\x12\x0e\n\tDISK_FULL\x10\xcd\x01\x12\x19\n\x14PREREQUISITE_NOT_MET\x10\xce\x01\x12\x18\n\x13INSUFFICIENT_BUFFER\x10\xcf\x01\x12\x14\n\x0fWAIT_FOR_IDLING\x10\xd0\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PBPFTPERROR = _descriptor.EnumDescriptor(
  name='PbPFtpError',
  full_name='protocol.PbPFtpError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATION_SUCCEEDED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REBOOTING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRY_AGAIN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNIDENTIFIED_HOST_ERROR', index=3, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_COMMAND', index=4, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARAMETER', index=5, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_SUCH_FILE_OR_DIRECTORY', index=6, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTORY_EXISTS', index=7, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE_EXISTS', index=8, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_NOT_PERMITTED', index=9, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_SUCH_USER', index=10, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=11, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNIDENTIFIED_DEVICE_ERROR', index=12, number=200,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_IMPLEMENTED', index=13, number=201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM_BUSY', index=14, number=202,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CONTENT', index=15, number=203,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKSUM_FAILURE', index=16, number=204,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISK_FULL', index=17, number=205,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREREQUISITE_NOT_MET', index=18, number=206,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSUFFICIENT_BUFFER', index=19, number=207,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAIT_FOR_IDLING', index=20, number=208,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=31,
  serialized_end=510,
)
_sym_db.RegisterEnumDescriptor(_PBPFTPERROR)

PbPFtpError = enum_type_wrapper.EnumTypeWrapper(_PBPFTPERROR)
OPERATION_SUCCEEDED = 0
REBOOTING = 1
TRY_AGAIN = 2
UNIDENTIFIED_HOST_ERROR = 100
INVALID_COMMAND = 101
INVALID_PARAMETER = 102
NO_SUCH_FILE_OR_DIRECTORY = 103
DIRECTORY_EXISTS = 104
FILE_EXISTS = 105
OPERATION_NOT_PERMITTED = 106
NO_SUCH_USER = 107
TIMEOUT = 108
UNIDENTIFIED_DEVICE_ERROR = 200
NOT_IMPLEMENTED = 201
SYSTEM_BUSY = 202
INVALID_CONTENT = 203
CHECKSUM_FAILURE = 204
DISK_FULL = 205
PREREQUISITE_NOT_MET = 206
INSUFFICIENT_BUFFER = 207
WAIT_FOR_IDLING = 208


DESCRIPTOR.enum_types_by_name['PbPFtpError'] = _PBPFTPERROR


# @@protoc_insertion_point(module_scope)

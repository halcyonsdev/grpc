# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: greeting_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'greeting_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16greeting_service.proto\x12\x10\x63om.example.grpc\"-\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07hobbies\x18\x02 \x03(\t\"!\n\rHelloResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t2`\n\x0fGreetingService\x12M\n\x08greeting\x12\x1e.com.example.grpc.HelloRequest\x1a\x1f.com.example.grpc.HelloResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeting_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HELLOREQUEST']._serialized_start=44
  _globals['_HELLOREQUEST']._serialized_end=89
  _globals['_HELLORESPONSE']._serialized_start=91
  _globals['_HELLORESPONSE']._serialized_end=124
  _globals['_GREETINGSERVICE']._serialized_start=126
  _globals['_GREETINGSERVICE']._serialized_end=222
# @@protoc_insertion_point(module_scope)

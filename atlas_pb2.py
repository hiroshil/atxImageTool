# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: atlas.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61tlas.proto\"\'\n\x06\x43\x61nvas\x12\r\n\x05Width\x18\x01 \x01(\x05\x12\x0e\n\x06Height\x18\x02 \x01(\x05\"\xd8\x01\n\x04Mesh\x12\r\n\x05texNo\x18\x01 \x01(\x05\x12\x0f\n\x07offsetX\x18\x02 \x01(\x02\x12\x0f\n\x07offsetY\x18\x03 \x01(\x02\x12\x12\n\nsrcOffsetX\x18\x04 \x01(\x02\x12\x12\n\nsrcOffsetY\x18\x05 \x01(\x02\x12\r\n\x05texU1\x18\x06 \x01(\x02\x12\r\n\x05texV1\x18\x07 \x01(\x02\x12\r\n\x05texU2\x18\x08 \x01(\x02\x12\r\n\x05texV2\x18\t \x01(\x02\x12\r\n\x05viewX\x18\n \x01(\x02\x12\r\n\x05viewY\x18\x0b \x01(\x02\x12\r\n\x05width\x18\x0c \x01(\x02\x12\x0e\n\x06height\x18\r \x01(\x02\"[\n\tAttribute\x12\n\n\x02id\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\r\n\x05\x63olor\x18\x06 \x01(\x03\"\xe3\x01\n\x05\x42lock\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x13\n\x0b\x66ilenameOld\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\x12\x0f\n\x07\x61nchorX\x18\x04 \x01(\x02\x12\x0f\n\x07\x61nchorY\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\x12\x0f\n\x07offsetX\x18\x08 \x01(\x02\x12\x0f\n\x07offsetY\x18\t \x01(\x02\x12\x10\n\x08priority\x18\n \x01(\x05\x12\x13\n\x04Mesh\x18\x0b \x03(\x0b\x32\x05.Mesh\x12\x1d\n\tAttribute\x18\x0c \x03(\x0b\x32\n.Attribute\"7\n\x05\x41tlas\x12\x17\n\x06\x43\x61nvas\x18\x01 \x01(\x0b\x32\x07.Canvas\x12\x15\n\x05\x42lock\x18\x02 \x03(\x0b\x32\x06.Blockb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'atlas_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CANVAS']._serialized_start=15
  _globals['_CANVAS']._serialized_end=54
  _globals['_MESH']._serialized_start=57
  _globals['_MESH']._serialized_end=273
  _globals['_ATTRIBUTE']._serialized_start=275
  _globals['_ATTRIBUTE']._serialized_end=366
  _globals['_BLOCK']._serialized_start=369
  _globals['_BLOCK']._serialized_end=596
  _globals['_ATLAS']._serialized_start=598
  _globals['_ATLAS']._serialized_end=653
# @@protoc_insertion_point(module_scope)

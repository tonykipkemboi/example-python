# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sf/substreams/v1/substreams.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sf.substreams.v1 import manifest_pb2 as sf_dot_substreams_dot_v1_dot_manifest__pb2
from sf.substreams.v1 import clock_pb2 as sf_dot_substreams_dot_v1_dot_clock__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sf/substreams/v1/substreams.proto',
  package='sf.substreams.v1',
  syntax='proto3',
  serialized_options=_b('ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreams'),
  serialized_pb=_b('\n!sf/substreams/v1/substreams.proto\x12\x10sf.substreams.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fsf/substreams/v1/manifest.proto\x1a\x1csf/substreams/v1/clock.proto\"\x95\x02\n\x07Request\x12\x17\n\x0fstart_block_num\x18\x01 \x01(\x03\x12\x14\n\x0cstart_cursor\x18\x02 \x01(\t\x12\x16\n\x0estop_block_num\x18\x03 \x01(\x04\x12.\n\nfork_steps\x18\x04 \x03(\x0e\x32\x1a.sf.substreams.v1.ForkStep\x12!\n\x19irreversibility_condition\x18\x05 \x01(\t\x12,\n\x08manifest\x18\x06 \x01(\x0b\x32\x1a.sf.substreams.v1.Manifest\x12\x16\n\x0eoutput_modules\x18\x07 \x03(\t\x12*\n\"initial_store_snapshot_for_modules\x18\x08 \x03(\t\"\x87\x02\n\x08Response\x12\x35\n\x08progress\x18\x01 \x01(\x0b\x32!.sf.substreams.v1.ModulesProgressH\x00\x12>\n\rsnapshot_data\x18\x02 \x01(\x0b\x32%.sf.substreams.v1.InitialSnapshotDataH\x00\x12\x46\n\x11snapshot_complete\x18\x03 \x01(\x0b\x32).sf.substreams.v1.InitialSnapshotCompleteH\x00\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.sf.substreams.v1.BlockScopedDataH\x00\x42\t\n\x07message\")\n\x17InitialSnapshotComplete\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\"\x80\x01\n\x13InitialSnapshotData\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12-\n\x06\x64\x65ltas\x18\x02 \x01(\x0b\x32\x1d.sf.substreams.v1.StoreDeltas\x12\x11\n\tsent_keys\x18\x04 \x01(\x04\x12\x12\n\ntotal_keys\x18\x03 \x01(\x04\"\xa4\x01\n\x0f\x42lockScopedData\x12/\n\x07outputs\x18\x01 \x03(\x0b\x32\x1e.sf.substreams.v1.ModuleOutput\x12&\n\x05\x63lock\x18\x03 \x01(\x0b\x32\x17.sf.substreams.v1.Clock\x12(\n\x04step\x18\x06 \x01(\x0e\x32\x1a.sf.substreams.v1.ForkStep\x12\x0e\n\x06\x63ursor\x18\n \x01(\t\"\x95\x01\n\x0cModuleOutput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\nmap_output\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x35\n\x0cstore_deltas\x18\x03 \x01(\x0b\x32\x1d.sf.substreams.v1.StoreDeltasH\x00\x12\x0c\n\x04logs\x18\x04 \x03(\tB\x06\n\x04\x64\x61ta\"D\n\x0fModulesProgress\x12\x31\n\x07modules\x18\x01 \x03(\x0b\x32 .sf.substreams.v1.ModuleProgress\"\xb5\x01\n\x0eModuleProgress\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x10processed_ranges\x18\x02 \x03(\x0b\x32\x1c.sf.substreams.v1.BlockRange\x12\x18\n\x10total_bytes_read\x18\x03 \x01(\x04\x12\x1b\n\x13total_bytes_written\x18\x04 \x01(\x04\x12\x0e\n\x06\x66\x61iled\x18\x07 \x01(\x08\x12\x16\n\x0e\x66\x61ilure_reason\x18\x08 \x01(\t\"4\n\nBlockRange\x12\x13\n\x0bstart_block\x18\x01 \x01(\x04\x12\x11\n\tend_block\x18\x02 \x01(\x04\";\n\x0bStoreDeltas\x12,\n\x06\x64\x65ltas\x18\x01 \x03(\x0b\x32\x1c.sf.substreams.v1.StoreDelta\"\xc7\x01\n\nStoreDelta\x12\x39\n\toperation\x18\x01 \x01(\x0e\x32&.sf.substreams.v1.StoreDelta.Operation\x12\x0f\n\x07ordinal\x18\x02 \x01(\x04\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x11\n\told_value\x18\x04 \x01(\x0c\x12\x11\n\tnew_value\x18\x05 \x01(\x0c\":\n\tOperation\x12\t\n\x05UNSET\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"\x81\x01\n\x06Output\x12\x11\n\tblock_num\x18\x01 \x01(\x04\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12#\n\x05value\x18\n \x01(\x0b\x32\x14.google.protobuf.Any*\\\n\x08\x46orkStep\x12\x10\n\x0cSTEP_UNKNOWN\x10\x00\x12\x0c\n\x08STEP_NEW\x10\x01\x12\r\n\tSTEP_UNDO\x10\x02\x12\x15\n\x11STEP_IRREVERSIBLE\x10\x04\"\x04\x08\x03\x10\x03\"\x04\x08\x05\x10\x05\x32K\n\x06Stream\x12\x41\n\x06\x42locks\x12\x19.sf.substreams.v1.Request\x1a\x1a.sf.substreams.v1.Response0\x01\x42\x46ZDgithub.com/streamingfast/substreams/pb/sf/substreams/v1;pbsubstreamsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,sf_dot_substreams_dot_v1_dot_manifest__pb2.DESCRIPTOR,sf_dot_substreams_dot_v1_dot_clock__pb2.DESCRIPTOR,])

_FORKSTEP = _descriptor.EnumDescriptor(
  name='ForkStep',
  full_name='sf.substreams.v1.ForkStep',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STEP_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEP_NEW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEP_UNDO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEP_IRREVERSIBLE', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1920,
  serialized_end=2012,
)
_sym_db.RegisterEnumDescriptor(_FORKSTEP)

ForkStep = enum_type_wrapper.EnumTypeWrapper(_FORKSTEP)
STEP_UNKNOWN = 0
STEP_NEW = 1
STEP_UNDO = 2
STEP_IRREVERSIBLE = 4


_STOREDELTA_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='sf.substreams.v1.StoreDelta.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1728,
  serialized_end=1786,
)
_sym_db.RegisterEnumDescriptor(_STOREDELTA_OPERATION)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='sf.substreams.v1.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_block_num', full_name='sf.substreams.v1.Request.start_block_num', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_cursor', full_name='sf.substreams.v1.Request.start_cursor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_block_num', full_name='sf.substreams.v1.Request.stop_block_num', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fork_steps', full_name='sf.substreams.v1.Request.fork_steps', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='irreversibility_condition', full_name='sf.substreams.v1.Request.irreversibility_condition', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manifest', full_name='sf.substreams.v1.Request.manifest', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_modules', full_name='sf.substreams.v1.Request.output_modules', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_store_snapshot_for_modules', full_name='sf.substreams.v1.Request.initial_store_snapshot_for_modules', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=456,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='sf.substreams.v1.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='progress', full_name='sf.substreams.v1.Response.progress', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshot_data', full_name='sf.substreams.v1.Response.snapshot_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshot_complete', full_name='sf.substreams.v1.Response.snapshot_complete', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sf.substreams.v1.Response.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='sf.substreams.v1.Response.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=459,
  serialized_end=722,
)


_INITIALSNAPSHOTCOMPLETE = _descriptor.Descriptor(
  name='InitialSnapshotComplete',
  full_name='sf.substreams.v1.InitialSnapshotComplete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cursor', full_name='sf.substreams.v1.InitialSnapshotComplete.cursor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=765,
)


_INITIALSNAPSHOTDATA = _descriptor.Descriptor(
  name='InitialSnapshotData',
  full_name='sf.substreams.v1.InitialSnapshotData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_name', full_name='sf.substreams.v1.InitialSnapshotData.module_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deltas', full_name='sf.substreams.v1.InitialSnapshotData.deltas', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sent_keys', full_name='sf.substreams.v1.InitialSnapshotData.sent_keys', index=2,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_keys', full_name='sf.substreams.v1.InitialSnapshotData.total_keys', index=3,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=768,
  serialized_end=896,
)


_BLOCKSCOPEDDATA = _descriptor.Descriptor(
  name='BlockScopedData',
  full_name='sf.substreams.v1.BlockScopedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='sf.substreams.v1.BlockScopedData.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clock', full_name='sf.substreams.v1.BlockScopedData.clock', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='sf.substreams.v1.BlockScopedData.step', index=2,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='sf.substreams.v1.BlockScopedData.cursor', index=3,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=899,
  serialized_end=1063,
)


_MODULEOUTPUT = _descriptor.Descriptor(
  name='ModuleOutput',
  full_name='sf.substreams.v1.ModuleOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sf.substreams.v1.ModuleOutput.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_output', full_name='sf.substreams.v1.ModuleOutput.map_output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_deltas', full_name='sf.substreams.v1.ModuleOutput.store_deltas', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='sf.substreams.v1.ModuleOutput.logs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='sf.substreams.v1.ModuleOutput.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1066,
  serialized_end=1215,
)


_MODULESPROGRESS = _descriptor.Descriptor(
  name='ModulesProgress',
  full_name='sf.substreams.v1.ModulesProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modules', full_name='sf.substreams.v1.ModulesProgress.modules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1217,
  serialized_end=1285,
)


_MODULEPROGRESS = _descriptor.Descriptor(
  name='ModuleProgress',
  full_name='sf.substreams.v1.ModuleProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sf.substreams.v1.ModuleProgress.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processed_ranges', full_name='sf.substreams.v1.ModuleProgress.processed_ranges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_bytes_read', full_name='sf.substreams.v1.ModuleProgress.total_bytes_read', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_bytes_written', full_name='sf.substreams.v1.ModuleProgress.total_bytes_written', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failed', full_name='sf.substreams.v1.ModuleProgress.failed', index=4,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure_reason', full_name='sf.substreams.v1.ModuleProgress.failure_reason', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1288,
  serialized_end=1469,
)


_BLOCKRANGE = _descriptor.Descriptor(
  name='BlockRange',
  full_name='sf.substreams.v1.BlockRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_block', full_name='sf.substreams.v1.BlockRange.start_block', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_block', full_name='sf.substreams.v1.BlockRange.end_block', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1471,
  serialized_end=1523,
)


_STOREDELTAS = _descriptor.Descriptor(
  name='StoreDeltas',
  full_name='sf.substreams.v1.StoreDeltas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deltas', full_name='sf.substreams.v1.StoreDeltas.deltas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1525,
  serialized_end=1584,
)


_STOREDELTA = _descriptor.Descriptor(
  name='StoreDelta',
  full_name='sf.substreams.v1.StoreDelta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='sf.substreams.v1.StoreDelta.operation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ordinal', full_name='sf.substreams.v1.StoreDelta.ordinal', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='sf.substreams.v1.StoreDelta.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='old_value', full_name='sf.substreams.v1.StoreDelta.old_value', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_value', full_name='sf.substreams.v1.StoreDelta.new_value', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STOREDELTA_OPERATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1587,
  serialized_end=1786,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='sf.substreams.v1.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_num', full_name='sf.substreams.v1.Output.block_num', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_id', full_name='sf.substreams.v1.Output.block_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sf.substreams.v1.Output.timestamp', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='sf.substreams.v1.Output.value', index=3,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1789,
  serialized_end=1918,
)

_REQUEST.fields_by_name['fork_steps'].enum_type = _FORKSTEP
_REQUEST.fields_by_name['manifest'].message_type = sf_dot_substreams_dot_v1_dot_manifest__pb2._MANIFEST
_RESPONSE.fields_by_name['progress'].message_type = _MODULESPROGRESS
_RESPONSE.fields_by_name['snapshot_data'].message_type = _INITIALSNAPSHOTDATA
_RESPONSE.fields_by_name['snapshot_complete'].message_type = _INITIALSNAPSHOTCOMPLETE
_RESPONSE.fields_by_name['data'].message_type = _BLOCKSCOPEDDATA
_RESPONSE.oneofs_by_name['message'].fields.append(
  _RESPONSE.fields_by_name['progress'])
_RESPONSE.fields_by_name['progress'].containing_oneof = _RESPONSE.oneofs_by_name['message']
_RESPONSE.oneofs_by_name['message'].fields.append(
  _RESPONSE.fields_by_name['snapshot_data'])
_RESPONSE.fields_by_name['snapshot_data'].containing_oneof = _RESPONSE.oneofs_by_name['message']
_RESPONSE.oneofs_by_name['message'].fields.append(
  _RESPONSE.fields_by_name['snapshot_complete'])
_RESPONSE.fields_by_name['snapshot_complete'].containing_oneof = _RESPONSE.oneofs_by_name['message']
_RESPONSE.oneofs_by_name['message'].fields.append(
  _RESPONSE.fields_by_name['data'])
_RESPONSE.fields_by_name['data'].containing_oneof = _RESPONSE.oneofs_by_name['message']
_INITIALSNAPSHOTDATA.fields_by_name['deltas'].message_type = _STOREDELTAS
_BLOCKSCOPEDDATA.fields_by_name['outputs'].message_type = _MODULEOUTPUT
_BLOCKSCOPEDDATA.fields_by_name['clock'].message_type = sf_dot_substreams_dot_v1_dot_clock__pb2._CLOCK
_BLOCKSCOPEDDATA.fields_by_name['step'].enum_type = _FORKSTEP
_MODULEOUTPUT.fields_by_name['map_output'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MODULEOUTPUT.fields_by_name['store_deltas'].message_type = _STOREDELTAS
_MODULEOUTPUT.oneofs_by_name['data'].fields.append(
  _MODULEOUTPUT.fields_by_name['map_output'])
_MODULEOUTPUT.fields_by_name['map_output'].containing_oneof = _MODULEOUTPUT.oneofs_by_name['data']
_MODULEOUTPUT.oneofs_by_name['data'].fields.append(
  _MODULEOUTPUT.fields_by_name['store_deltas'])
_MODULEOUTPUT.fields_by_name['store_deltas'].containing_oneof = _MODULEOUTPUT.oneofs_by_name['data']
_MODULESPROGRESS.fields_by_name['modules'].message_type = _MODULEPROGRESS
_MODULEPROGRESS.fields_by_name['processed_ranges'].message_type = _BLOCKRANGE
_STOREDELTAS.fields_by_name['deltas'].message_type = _STOREDELTA
_STOREDELTA.fields_by_name['operation'].enum_type = _STOREDELTA_OPERATION
_STOREDELTA_OPERATION.containing_type = _STOREDELTA
_OUTPUT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OUTPUT.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['InitialSnapshotComplete'] = _INITIALSNAPSHOTCOMPLETE
DESCRIPTOR.message_types_by_name['InitialSnapshotData'] = _INITIALSNAPSHOTDATA
DESCRIPTOR.message_types_by_name['BlockScopedData'] = _BLOCKSCOPEDDATA
DESCRIPTOR.message_types_by_name['ModuleOutput'] = _MODULEOUTPUT
DESCRIPTOR.message_types_by_name['ModulesProgress'] = _MODULESPROGRESS
DESCRIPTOR.message_types_by_name['ModuleProgress'] = _MODULEPROGRESS
DESCRIPTOR.message_types_by_name['BlockRange'] = _BLOCKRANGE
DESCRIPTOR.message_types_by_name['StoreDeltas'] = _STOREDELTAS
DESCRIPTOR.message_types_by_name['StoreDelta'] = _STOREDELTA
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.enum_types_by_name['ForkStep'] = _FORKSTEP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.Response)
  })
_sym_db.RegisterMessage(Response)

InitialSnapshotComplete = _reflection.GeneratedProtocolMessageType('InitialSnapshotComplete', (_message.Message,), {
  'DESCRIPTOR' : _INITIALSNAPSHOTCOMPLETE,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.InitialSnapshotComplete)
  })
_sym_db.RegisterMessage(InitialSnapshotComplete)

InitialSnapshotData = _reflection.GeneratedProtocolMessageType('InitialSnapshotData', (_message.Message,), {
  'DESCRIPTOR' : _INITIALSNAPSHOTDATA,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.InitialSnapshotData)
  })
_sym_db.RegisterMessage(InitialSnapshotData)

BlockScopedData = _reflection.GeneratedProtocolMessageType('BlockScopedData', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKSCOPEDDATA,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.BlockScopedData)
  })
_sym_db.RegisterMessage(BlockScopedData)

ModuleOutput = _reflection.GeneratedProtocolMessageType('ModuleOutput', (_message.Message,), {
  'DESCRIPTOR' : _MODULEOUTPUT,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModuleOutput)
  })
_sym_db.RegisterMessage(ModuleOutput)

ModulesProgress = _reflection.GeneratedProtocolMessageType('ModulesProgress', (_message.Message,), {
  'DESCRIPTOR' : _MODULESPROGRESS,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModulesProgress)
  })
_sym_db.RegisterMessage(ModulesProgress)

ModuleProgress = _reflection.GeneratedProtocolMessageType('ModuleProgress', (_message.Message,), {
  'DESCRIPTOR' : _MODULEPROGRESS,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.ModuleProgress)
  })
_sym_db.RegisterMessage(ModuleProgress)

BlockRange = _reflection.GeneratedProtocolMessageType('BlockRange', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKRANGE,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.BlockRange)
  })
_sym_db.RegisterMessage(BlockRange)

StoreDeltas = _reflection.GeneratedProtocolMessageType('StoreDeltas', (_message.Message,), {
  'DESCRIPTOR' : _STOREDELTAS,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.StoreDeltas)
  })
_sym_db.RegisterMessage(StoreDeltas)

StoreDelta = _reflection.GeneratedProtocolMessageType('StoreDelta', (_message.Message,), {
  'DESCRIPTOR' : _STOREDELTA,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.StoreDelta)
  })
_sym_db.RegisterMessage(StoreDelta)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'sf.substreams.v1.substreams_pb2'
  # @@protoc_insertion_point(class_scope:sf.substreams.v1.Output)
  })
_sym_db.RegisterMessage(Output)


DESCRIPTOR._options = None

_STREAM = _descriptor.ServiceDescriptor(
  name='Stream',
  full_name='sf.substreams.v1.Stream',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2014,
  serialized_end=2089,
  methods=[
  _descriptor.MethodDescriptor(
    name='Blocks',
    full_name='sf.substreams.v1.Stream.Blocks',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAM)

DESCRIPTOR.services_by_name['Stream'] = _STREAM

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: propresenter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basicTypes_pb2 as basicTypes__pb2
import playlist_pb2 as playlist__pb2
import action_pb2 as action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='propresenter.proto',
  package='rv.data',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12propresenter.proto\x12\x07rv.data\x1a\x10\x62\x61sicTypes.proto\x1a\x0eplaylist.proto\x1a\x0c\x61\x63tion.proto\"\xef\x02\n\x10PlaylistDocument\x12\x32\n\x10\x61pplication_info\x18\x01 \x01(\x0b\x32\x18.rv.data.ApplicationInfo\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.rv.data.PlaylistDocument.Type\x12$\n\troot_node\x18\x03 \x01(\x0b\x32\x11.rv.data.Playlist\x12#\n\x04tags\x18\x04 \x03(\x0b\x32\x15.rv.data.Playlist.Tag\x12.\n\x13live_video_playlist\x18\x05 \x01(\x0b\x32\x11.rv.data.Playlist\x12-\n\x12\x64ownloads_playlist\x18\x06 \x01(\x0b\x32\x11.rv.data.Playlist\"O\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x15\n\x11TYPE_PRESENTATION\x10\x01\x12\x0e\n\nTYPE_MEDIA\x10\x02\x12\x0e\n\nTYPE_AUDIO\x10\x03\"9\n\x10SettingsDocument\x12%\n\x06labels\x18\x02 \x03(\x0b\x32\x15.rv.data.Action.Labelb\x06proto3'
  ,
  dependencies=[basicTypes__pb2.DESCRIPTOR,playlist__pb2.DESCRIPTOR,action__pb2.DESCRIPTOR,])



_PLAYLISTDOCUMENT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='rv.data.PlaylistDocument.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TYPE_PRESENTATION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TYPE_MEDIA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TYPE_AUDIO', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=368,
  serialized_end=447,
)
_sym_db.RegisterEnumDescriptor(_PLAYLISTDOCUMENT_TYPE)


_PLAYLISTDOCUMENT = _descriptor.Descriptor(
  name='PlaylistDocument',
  full_name='rv.data.PlaylistDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='application_info', full_name='rv.data.PlaylistDocument.application_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='rv.data.PlaylistDocument.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root_node', full_name='rv.data.PlaylistDocument.root_node', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='rv.data.PlaylistDocument.tags', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='live_video_playlist', full_name='rv.data.PlaylistDocument.live_video_playlist', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downloads_playlist', full_name='rv.data.PlaylistDocument.downloads_playlist', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PLAYLISTDOCUMENT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=447,
)


_SETTINGSDOCUMENT = _descriptor.Descriptor(
  name='SettingsDocument',
  full_name='rv.data.SettingsDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='labels', full_name='rv.data.SettingsDocument.labels', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=449,
  serialized_end=506,
)

_PLAYLISTDOCUMENT.fields_by_name['application_info'].message_type = basicTypes__pb2._APPLICATIONINFO
_PLAYLISTDOCUMENT.fields_by_name['type'].enum_type = _PLAYLISTDOCUMENT_TYPE
_PLAYLISTDOCUMENT.fields_by_name['root_node'].message_type = playlist__pb2._PLAYLIST
_PLAYLISTDOCUMENT.fields_by_name['tags'].message_type = playlist__pb2._PLAYLIST_TAG
_PLAYLISTDOCUMENT.fields_by_name['live_video_playlist'].message_type = playlist__pb2._PLAYLIST
_PLAYLISTDOCUMENT.fields_by_name['downloads_playlist'].message_type = playlist__pb2._PLAYLIST
_PLAYLISTDOCUMENT_TYPE.containing_type = _PLAYLISTDOCUMENT
_SETTINGSDOCUMENT.fields_by_name['labels'].message_type = action__pb2._ACTION_LABEL
DESCRIPTOR.message_types_by_name['PlaylistDocument'] = _PLAYLISTDOCUMENT
DESCRIPTOR.message_types_by_name['SettingsDocument'] = _SETTINGSDOCUMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlaylistDocument = _reflection.GeneratedProtocolMessageType('PlaylistDocument', (_message.Message,), {
  'DESCRIPTOR' : _PLAYLISTDOCUMENT,
  '__module__' : 'propresenter_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.PlaylistDocument)
  })
_sym_db.RegisterMessage(PlaylistDocument)

SettingsDocument = _reflection.GeneratedProtocolMessageType('SettingsDocument', (_message.Message,), {
  'DESCRIPTOR' : _SETTINGSDOCUMENT,
  '__module__' : 'propresenter_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.SettingsDocument)
  })
_sym_db.RegisterMessage(SettingsDocument)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proworkspace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proscreen_pb2 as proscreen__pb2
import proAudienceLook_pb2 as proAudienceLook__pb2
import proMask_pb2 as proMask__pb2
import input_pb2 as input__pb2
import audio_pb2 as audio__pb2
import digitalAudio_pb2 as digitalAudio__pb2
import stage_pb2 as stage__pb2
import recording_pb2 as recording__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proworkspace.proto',
  package='rv.data',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12proworkspace.proto\x12\x07rv.data\x1a\x0fproscreen.proto\x1a\x15proAudienceLook.proto\x1a\rproMask.proto\x1a\x0binput.proto\x1a\x0b\x61udio.proto\x1a\x12\x64igitalAudio.proto\x1a\x0bstage.proto\x1a\x0frecording.proto\"\xdc\x04\n\x15ProPresenterWorkspace\x12\x30\n\x0bpro_screens\x18\x01 \x03(\x0b\x32\x1b.rv.data.ProPresenterScreen\x12\x30\n\x0e\x61udience_looks\x18\x02 \x03(\x0b\x32\x18.rv.data.ProAudienceLook\x12\x34\n\x12live_audience_look\x18\x03 \x01(\x0b\x32\x18.rv.data.ProAudienceLook\x12\x1f\n\x05masks\x18\x04 \x03(\x0b\x32\x10.rv.data.ProMask\x12(\n\x0bvideoInputs\x18\x05 \x03(\x0b\x32\x13.rv.data.VideoInput\x12>\n\x15stage_layout_mappings\x18\x06 \x03(\x0b\x32\x1f.rv.data.Stage.ScreenAssignment\x12\x37\n\x0e\x61udio_settings\x18\x07 \x01(\x0b\x32\x1f.rv.data.Audio.SettingsDocument\x12\x1d\n\x15selected_library_name\x18\x08 \x01(\t\x12<\n\x0frecord_settings\x18\t \x01(\x0b\x32#.rv.data.Recording.SettingsDocument\x12\x38\n\x13\x64igital_audio_setup\x18\n \x01(\x0b\x32\x1b.rv.data.DigitalAudio.Setup\x12)\n\x0c\x61udio_inputs\x18\x0b \x03(\x0b\x32\x13.rv.data.AudioInput\x12#\n\x1b\x61udio_input_transition_time\x18\x0c \x01(\x01\x62\x06proto3'
  ,
  dependencies=[proscreen__pb2.DESCRIPTOR,proAudienceLook__pb2.DESCRIPTOR,proMask__pb2.DESCRIPTOR,input__pb2.DESCRIPTOR,audio__pb2.DESCRIPTOR,digitalAudio__pb2.DESCRIPTOR,stage__pb2.DESCRIPTOR,recording__pb2.DESCRIPTOR,])




_PROPRESENTERWORKSPACE = _descriptor.Descriptor(
  name='ProPresenterWorkspace',
  full_name='rv.data.ProPresenterWorkspace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pro_screens', full_name='rv.data.ProPresenterWorkspace.pro_screens', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audience_looks', full_name='rv.data.ProPresenterWorkspace.audience_looks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='live_audience_look', full_name='rv.data.ProPresenterWorkspace.live_audience_look', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='masks', full_name='rv.data.ProPresenterWorkspace.masks', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='videoInputs', full_name='rv.data.ProPresenterWorkspace.videoInputs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stage_layout_mappings', full_name='rv.data.ProPresenterWorkspace.stage_layout_mappings', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_settings', full_name='rv.data.ProPresenterWorkspace.audio_settings', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='selected_library_name', full_name='rv.data.ProPresenterWorkspace.selected_library_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='record_settings', full_name='rv.data.ProPresenterWorkspace.record_settings', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digital_audio_setup', full_name='rv.data.ProPresenterWorkspace.digital_audio_setup', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_inputs', full_name='rv.data.ProPresenterWorkspace.audio_inputs', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_input_transition_time', full_name='rv.data.ProPresenterWorkspace.audio_input_transition_time', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=163,
  serialized_end=767,
)

_PROPRESENTERWORKSPACE.fields_by_name['pro_screens'].message_type = proscreen__pb2._PROPRESENTERSCREEN
_PROPRESENTERWORKSPACE.fields_by_name['audience_looks'].message_type = proAudienceLook__pb2._PROAUDIENCELOOK
_PROPRESENTERWORKSPACE.fields_by_name['live_audience_look'].message_type = proAudienceLook__pb2._PROAUDIENCELOOK
_PROPRESENTERWORKSPACE.fields_by_name['masks'].message_type = proMask__pb2._PROMASK
_PROPRESENTERWORKSPACE.fields_by_name['videoInputs'].message_type = input__pb2._VIDEOINPUT
_PROPRESENTERWORKSPACE.fields_by_name['stage_layout_mappings'].message_type = stage__pb2._STAGE_SCREENASSIGNMENT
_PROPRESENTERWORKSPACE.fields_by_name['audio_settings'].message_type = audio__pb2._AUDIO_SETTINGSDOCUMENT
_PROPRESENTERWORKSPACE.fields_by_name['record_settings'].message_type = recording__pb2._RECORDING_SETTINGSDOCUMENT
_PROPRESENTERWORKSPACE.fields_by_name['digital_audio_setup'].message_type = digitalAudio__pb2._DIGITALAUDIO_SETUP
_PROPRESENTERWORKSPACE.fields_by_name['audio_inputs'].message_type = input__pb2._AUDIOINPUT
DESCRIPTOR.message_types_by_name['ProPresenterWorkspace'] = _PROPRESENTERWORKSPACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProPresenterWorkspace = _reflection.GeneratedProtocolMessageType('ProPresenterWorkspace', (_message.Message,), {
  'DESCRIPTOR' : _PROPRESENTERWORKSPACE,
  '__module__' : 'proworkspace_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.ProPresenterWorkspace)
  })
_sym_db.RegisterMessage(ProPresenterWorkspace)


# @@protoc_insertion_point(module_scope)

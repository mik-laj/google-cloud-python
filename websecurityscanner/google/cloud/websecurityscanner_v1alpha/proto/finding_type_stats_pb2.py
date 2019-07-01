# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1alpha/proto/finding_type_stats.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.websecurityscanner_v1alpha.proto import (
    finding_pb2 as google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1alpha/proto/finding_type_stats.proto",
    package="google.cloud.websecurityscanner.v1alpha",
    syntax="proto3",
    serialized_options=_b(
        "\n+com.google.cloud.websecurityscanner.v1alphaB\025FindingTypeStatsProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner"
    ),
    serialized_pb=_b(
        "\nFgoogle/cloud/websecurityscanner_v1alpha/proto/finding_type_stats.proto\x12'google.cloud.websecurityscanner.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a;google/cloud/websecurityscanner_v1alpha/proto/finding.proto\"}\n\x10\x46indingTypeStats\x12R\n\x0c\x66inding_type\x18\x01 \x01(\x0e\x32<.google.cloud.websecurityscanner.v1alpha.Finding.FindingType\x12\x15\n\rfinding_count\x18\x02 \x01(\x05\x42\xa1\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x15\x46indingTypeStatsProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3"
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__pb2.DESCRIPTOR,
    ],
)


_FINDINGTYPESTATS = _descriptor.Descriptor(
    name="FindingTypeStats",
    full_name="google.cloud.websecurityscanner.v1alpha.FindingTypeStats",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="finding_type",
            full_name="google.cloud.websecurityscanner.v1alpha.FindingTypeStats.finding_type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="finding_count",
            full_name="google.cloud.websecurityscanner.v1alpha.FindingTypeStats.finding_count",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=206,
    serialized_end=331,
)

_FINDINGTYPESTATS.fields_by_name[
    "finding_type"
].enum_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__pb2._FINDING_FINDINGTYPE
)
DESCRIPTOR.message_types_by_name["FindingTypeStats"] = _FINDINGTYPESTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FindingTypeStats = _reflection.GeneratedProtocolMessageType(
    "FindingTypeStats",
    (_message.Message,),
    dict(
        DESCRIPTOR=_FINDINGTYPESTATS,
        __module__="google.cloud.websecurityscanner_v1alpha.proto.finding_type_stats_pb2",
        __doc__="""A FindingTypeStats resource represents stats regarding a specific
  FindingType of Findings under a given ScanRun.
  
  
  Attributes:
      finding_type:
          Output only. The finding type associated with the stats.
      finding_count:
          Output only. The count of findings belonging to this finding
          type.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.FindingTypeStats)
    ),
)
_sym_db.RegisterMessage(FindingTypeStats)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

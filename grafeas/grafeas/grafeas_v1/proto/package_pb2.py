# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas_v1/proto/package.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="grafeas_v1/proto/package.proto",
    package="grafeas.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA"
    ),
    serialized_pb=_b(
        '\n\x1egrafeas_v1/proto/package.proto\x12\ngrafeas.v1"\xb2\x01\n\x0c\x44istribution\x12\x0f\n\x07\x63pe_uri\x18\x01 \x01(\t\x12.\n\x0c\x61rchitecture\x18\x02 \x01(\x0e\x32\x18.grafeas.v1.Architecture\x12+\n\x0elatest_version\x18\x03 \x01(\x0b\x32\x13.grafeas.v1.Version\x12\x12\n\nmaintainer\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t"O\n\x08Location\x12\x0f\n\x07\x63pe_uri\x18\x01 \x01(\t\x12$\n\x07version\x18\x02 \x01(\x0b\x32\x13.grafeas.v1.Version\x12\x0c\n\x04path\x18\x03 \x01(\t"K\n\x0bPackageNote\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x0c\x64istribution\x18\n \x03(\x0b\x32\x18.grafeas.v1.Distribution"I\n\x11PackageOccurrence\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x08location\x18\x02 \x03(\x0b\x32\x14.grafeas.v1.Location"\xcd\x01\n\x07Version\x12\r\n\x05\x65poch\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08revision\x18\x03 \x01(\t\x12-\n\x04kind\x18\x04 \x01(\x0e\x32\x1f.grafeas.v1.Version.VersionKind\x12\x11\n\tfull_name\x18\x05 \x01(\t"Q\n\x0bVersionKind\x12\x1c\n\x18VERSION_KIND_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x0b\n\x07MINIMUM\x10\x02\x12\x0b\n\x07MAXIMUM\x10\x03*>\n\x0c\x41rchitecture\x12\x1c\n\x18\x41RCHITECTURE_UNSPECIFIED\x10\x00\x12\x07\n\x03X86\x10\x01\x12\x07\n\x03X64\x10\x02\x42Q\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3'
    ),
)

_ARCHITECTURE = _descriptor.EnumDescriptor(
    name="Architecture",
    full_name="grafeas.v1.Architecture",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ARCHITECTURE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="X86", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="X64", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=668,
    serialized_end=730,
)
_sym_db.RegisterEnumDescriptor(_ARCHITECTURE)

Architecture = enum_type_wrapper.EnumTypeWrapper(_ARCHITECTURE)
ARCHITECTURE_UNSPECIFIED = 0
X86 = 1
X64 = 2


_VERSION_VERSIONKIND = _descriptor.EnumDescriptor(
    name="VersionKind",
    full_name="grafeas.v1.Version.VersionKind",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="VERSION_KIND_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NORMAL", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MINIMUM", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MAXIMUM", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=585,
    serialized_end=666,
)
_sym_db.RegisterEnumDescriptor(_VERSION_VERSIONKIND)


_DISTRIBUTION = _descriptor.Descriptor(
    name="Distribution",
    full_name="grafeas.v1.Distribution",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="cpe_uri",
            full_name="grafeas.v1.Distribution.cpe_uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="architecture",
            full_name="grafeas.v1.Distribution.architecture",
            index=1,
            number=2,
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
            name="latest_version",
            full_name="grafeas.v1.Distribution.latest_version",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="maintainer",
            full_name="grafeas.v1.Distribution.maintainer",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="url",
            full_name="grafeas.v1.Distribution.url",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="grafeas.v1.Distribution.description",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
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
    serialized_start=47,
    serialized_end=225,
)


_LOCATION = _descriptor.Descriptor(
    name="Location",
    full_name="grafeas.v1.Location",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="cpe_uri",
            full_name="grafeas.v1.Location.cpe_uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="grafeas.v1.Location.version",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="path",
            full_name="grafeas.v1.Location.path",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
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
    serialized_start=227,
    serialized_end=306,
)


_PACKAGENOTE = _descriptor.Descriptor(
    name="PackageNote",
    full_name="grafeas.v1.PackageNote",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="grafeas.v1.PackageNote.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="distribution",
            full_name="grafeas.v1.PackageNote.distribution",
            index=1,
            number=10,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_start=308,
    serialized_end=383,
)


_PACKAGEOCCURRENCE = _descriptor.Descriptor(
    name="PackageOccurrence",
    full_name="grafeas.v1.PackageOccurrence",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="grafeas.v1.PackageOccurrence.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="grafeas.v1.PackageOccurrence.location",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_start=385,
    serialized_end=458,
)


_VERSION = _descriptor.Descriptor(
    name="Version",
    full_name="grafeas.v1.Version",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="epoch",
            full_name="grafeas.v1.Version.epoch",
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name="name",
            full_name="grafeas.v1.Version.name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="revision",
            full_name="grafeas.v1.Version.revision",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="kind",
            full_name="grafeas.v1.Version.kind",
            index=3,
            number=4,
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
            name="full_name",
            full_name="grafeas.v1.Version.full_name",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
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
    enum_types=[_VERSION_VERSIONKIND],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=461,
    serialized_end=666,
)

_DISTRIBUTION.fields_by_name["architecture"].enum_type = _ARCHITECTURE
_DISTRIBUTION.fields_by_name["latest_version"].message_type = _VERSION
_LOCATION.fields_by_name["version"].message_type = _VERSION
_PACKAGENOTE.fields_by_name["distribution"].message_type = _DISTRIBUTION
_PACKAGEOCCURRENCE.fields_by_name["location"].message_type = _LOCATION
_VERSION.fields_by_name["kind"].enum_type = _VERSION_VERSIONKIND
_VERSION_VERSIONKIND.containing_type = _VERSION
DESCRIPTOR.message_types_by_name["Distribution"] = _DISTRIBUTION
DESCRIPTOR.message_types_by_name["Location"] = _LOCATION
DESCRIPTOR.message_types_by_name["PackageNote"] = _PACKAGENOTE
DESCRIPTOR.message_types_by_name["PackageOccurrence"] = _PACKAGEOCCURRENCE
DESCRIPTOR.message_types_by_name["Version"] = _VERSION
DESCRIPTOR.enum_types_by_name["Architecture"] = _ARCHITECTURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Distribution = _reflection.GeneratedProtocolMessageType(
    "Distribution",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DISTRIBUTION,
        __module__="grafeas_v1.proto.package_pb2",
        __doc__="""This represents a particular channel of distribution for a given
  package. E.g., Debian's jessie-backports dpkg mirror.
  
  
  Attributes:
      cpe_uri:
          Required. The cpe\_uri in `CPE format
          <https://cpe.mitre.org/specification/>`__ denoting the package
          manager version distributing a package.
      architecture:
          The CPU architecture for which packages in this distribution
          channel were built.
      latest_version:
          The latest available version of this package in this
          distribution channel.
      maintainer:
          A freeform string denoting the maintainer of this package.
      url:
          The distribution channel-specific homepage for this package.
      description:
          The distribution channel-specific description of this package.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.Distribution)
    ),
)
_sym_db.RegisterMessage(Distribution)

Location = _reflection.GeneratedProtocolMessageType(
    "Location",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LOCATION,
        __module__="grafeas_v1.proto.package_pb2",
        __doc__="""An occurrence of a particular package installation found within a
  system's filesystem. E.g., glibc was found in ``/var/lib/dpkg/status``.
  
  
  Attributes:
      cpe_uri:
          Required. The CPE URI in `CPE format
          <https://cpe.mitre.org/specification/>`__ denoting the package
          manager version distributing a package.
      version:
          The version installed at this location.
      path:
          The path from which we gathered that this package/version is
          installed.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.Location)
    ),
)
_sym_db.RegisterMessage(Location)

PackageNote = _reflection.GeneratedProtocolMessageType(
    "PackageNote",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PACKAGENOTE,
        __module__="grafeas_v1.proto.package_pb2",
        __doc__="""This represents a particular package that is distributed over various
  channels. E.g., glibc (aka libc6) is distributed by many, at various
  versions.
  
  
  Attributes:
      name:
          Required. Immutable. The name of the package.
      distribution:
          The various channels by which a package is distributed.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.PackageNote)
    ),
)
_sym_db.RegisterMessage(PackageNote)

PackageOccurrence = _reflection.GeneratedProtocolMessageType(
    "PackageOccurrence",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PACKAGEOCCURRENCE,
        __module__="grafeas_v1.proto.package_pb2",
        __doc__="""Details on how a particular software package was installed on a system.
  
  
  Attributes:
      name:
          Output only. The name of the installed package.
      location:
          Required. All of the places within the filesystem versions of
          this package have been found.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.PackageOccurrence)
    ),
)
_sym_db.RegisterMessage(PackageOccurrence)

Version = _reflection.GeneratedProtocolMessageType(
    "Version",
    (_message.Message,),
    dict(
        DESCRIPTOR=_VERSION,
        __module__="grafeas_v1.proto.package_pb2",
        __doc__="""Version contains structured information about the version of a package.
  
  
  Attributes:
      epoch:
          Used to correct mistakes in the version numbering scheme.
      name:
          Required only when version kind is NORMAL. The main part of
          the version name.
      revision:
          The iteration of the package build from the above version.
      kind:
          Required. Distinguishes between sentinel MIN/MAX versions and
          normal versions.
      full_name:
          Human readable version string. This string is of the form :-
          and is only set when kind is NORMAL.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.Version)
    ),
)
_sym_db.RegisterMessage(Version)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

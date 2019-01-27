#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostCycleGroupCConan(base.BoostBaseConan):
    name = "boost_cycle_group_c" # Level 14
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_cycle_group_c"
    lib_short_names = [
        "date_time",
        "dynamic_bitset",
        "iostreams",
        "multiprecision",
        "pool",
        "random",
        "serialization",
        "spirit",
        "thread"
    ]
    header_only_libs = [
        "dynamic_bitset",
        "multiprecision",
        "pool",
        "spirit"
    ]
    options = {
        "shared": [True, False],
        "use_bzip2": [True, False],
        "use_lzma": [True, False],
        "use_zlib": [True, False],
        "use_zstd": [True, False],
        "threadapi": ['default', 'win32', 'pthread']
    }
    default_options = "shared=False", "use_bzip2=True", "use_lzma=True", "use_zlib=True", "use_zstd=True", "threadapi=default"
    b2_defines = ["LZMA_API_STATIC"]
    b2_requires = [
        "boost_algorithm",
        "boost_array",
        "boost_assert",
        "boost_atomic",
        "boost_bind",
        "boost_chrono",
        "boost_concept_check",
        "boost_config",
        "boost_container",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_endian",
        "boost_exception",
        "boost_filesystem",
        "boost_foreach",
        "boost_function",
        "boost_function_types",
        "boost_fusion",
        "boost_integer",
        "boost_intrusive",
        "boost_io",
        "boost_iterator",
        "boost_lexical_cast",
        "boost_locale",
        "boost_math",
        "boost_move",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_optional",
        "boost_phoenix",
        "boost_predef",
        "boost_preprocessor",
        "boost_proto",
        "boost_range",
        "boost_rational",
        "boost_regex",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_system",
        "boost_throw_exception",
        "boost_tokenizer",
        "boost_tti",
        "boost_tuple",
        "boost_type_traits",
        "boost_typeof",
        "boost_unordered",
        "boost_utility",
        "boost_variant",
        "boost_winapi"
    ]

    def requirements_additional(self):
        if self.options.use_bzip2:
            self.requires("bzip2/1.0.6@conan/stable")
        if self.options.use_zlib:
            self.requires("zlib/1.2.11@conan/stable")
        if self.options.use_lzma:
            self.requires("lzma/5.2.4@bincrafters/stable")
        if self.options.use_zstd:
            self.requires("zstd/1.3.5@bincrafters/stable")

    def package_info_additional(self):
        if self.settings.os != "Windows":
            self.cpp_info.libs.append("pthread")
        if self.options.use_bzip2:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_USE_BZIP2=1")
        if self.options.use_zlib:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_USE_ZLIB=1")
        if self.options.use_lzma:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_USE_LZMA=1")
        if self.options.use_zstd:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_USE_ZSTD=1")
        if self.options.shared:
            self.cpp_info.defines.append("BOOST_IOSTREAMS_DYN_LINK=1")

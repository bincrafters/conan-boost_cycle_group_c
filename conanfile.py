#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostCycleGroupCConan(base.BoostBaseConan):
    name = "boost_cycle_group_c" # Level 14
    url = "https://github.com/bincrafters/conan-boost_cycle_group_c"
    lib_short_names = [
        "date_time",
        "dynamic_bitset",
        "iostreams",
        "multiprecision",
        "random",
        "serialization",
        "spirit",
        "thread"
    ]
    header_only_libs = [
        "dynamic_bitset",
        "multiprecision",
        "spirit"
    ]
    options = {"shared": [True, False]}
    default_options = "shared=False"
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
        "boost_pool",
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

    def package_info_additional(self):
        if self.settings.os != "Windows":
            self.cpp_info.libs.append("pthread")

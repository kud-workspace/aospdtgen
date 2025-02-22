#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from aospdtgen.proprietary_files.section import register_sections
import os
from pathlib import Path

__version__ = "0.1.0"

module_path = Path(__file__).parent
sections_path = module_path / "proprietary_files" / "sections"
current_path = Path(os.getcwd())

register_sections(sections_path)

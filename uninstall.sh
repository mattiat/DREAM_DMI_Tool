#! /bin/bash -
# Copyright 2018 Mattia Tomasoni <mattia.tomasoni@unil.ch>
#
# This file is part of DREAM DMI Tool.
#
#    DREAM DMI Tool is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    DREAM DMI Tool is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with DREAM DMI Tool. If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################
# Mattia Tomasoni - UNIL, CBG
# 2017 DREAM challenge on Disease Module Identification
# https://www.synapse.org/modulechallenge
###############################################################################

echo
echo "Uninstalling the DREAM_DMI TOOL"

# check whether dream_dmi is actually installed
if grep -q dream_dmi_tool ~/.bashrc; then
  # remove dream_dmi dir from PATH
  sed -i '/dream_dmi_tool/d' ~/.bashrc
  # remove dream_dmi folder from the file system
  rm -rf ~/.dream_dmi_tool
  echo FINISHED: dream_dmi was UNINSTALLED SUCCESSFULLY.
  echo
else
  echo FINISHED: dream_dmi is not installed on this system, nothing to do.
  echo
fi

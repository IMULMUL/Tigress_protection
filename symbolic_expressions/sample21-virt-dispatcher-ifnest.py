#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_7568 = ref_278 # MOV operation
ref_7823 = ref_7568 # MOV operation
ref_7831 = (ref_7823 >> (0x3 & 0x3F)) # SHR operation
ref_7838 = ref_7831 # MOV operation
ref_9399 = ref_278 # MOV operation
ref_9633 = ref_9399 # MOV operation
ref_9647 = ((ref_9633 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_9986 = ref_7838 # MOV operation
ref_9990 = ref_9647 # MOV operation
ref_9992 = (ref_9990 | ref_9986) # OR operation
ref_10233 = ref_9992 # MOV operation
ref_10247 = ((ref_10233 - 0x3FEFFF7F) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_10255 = ref_10247 # MOV operation
ref_10571 = ref_10255 # MOV operation
ref_10573 = ((ref_10571 >> 56) & 0xFF) # Byte reference - MOV operation
ref_10574 = ((ref_10571 >> 48) & 0xFF) # Byte reference - MOV operation
ref_10575 = ((ref_10571 >> 40) & 0xFF) # Byte reference - MOV operation
ref_10576 = ((ref_10571 >> 32) & 0xFF) # Byte reference - MOV operation
ref_10577 = ((ref_10571 >> 24) & 0xFF) # Byte reference - MOV operation
ref_10578 = ((ref_10571 >> 16) & 0xFF) # Byte reference - MOV operation
ref_10579 = ((ref_10571 >> 8) & 0xFF) # Byte reference - MOV operation
ref_10580 = (ref_10571 & 0xFF) # Byte reference - MOV operation
ref_13493 = ref_278 # MOV operation
ref_15079 = ref_10571 # MOV operation
ref_15393 = ref_13493 # MOV operation
ref_15397 = ref_15079 # MOV operation
ref_15399 = (ref_15397 | ref_15393) # OR operation
ref_15640 = ref_15399 # MOV operation
ref_15654 = ((ref_15640 - 0x11E59B96) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15662 = ref_15654 # MOV operation
ref_15978 = ref_15662 # MOV operation
ref_15980 = ((ref_15978 >> 56) & 0xFF) # Byte reference - MOV operation
ref_15981 = ((ref_15978 >> 48) & 0xFF) # Byte reference - MOV operation
ref_15982 = ((ref_15978 >> 40) & 0xFF) # Byte reference - MOV operation
ref_15983 = ((ref_15978 >> 32) & 0xFF) # Byte reference - MOV operation
ref_15984 = ((ref_15978 >> 24) & 0xFF) # Byte reference - MOV operation
ref_15985 = ((ref_15978 >> 16) & 0xFF) # Byte reference - MOV operation
ref_15986 = ((ref_15978 >> 8) & 0xFF) # Byte reference - MOV operation
ref_15987 = (ref_15978 & 0xFF) # Byte reference - MOV operation
ref_18734 = ref_278 # MOV operation
ref_20320 = ref_10571 # MOV operation
ref_20517 = ref_18734 # MOV operation
ref_20521 = ref_20320 # MOV operation
ref_20523 = (((sx(0x40, ref_20521) * sx(0x40, ref_20517)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_22297 = ref_15978 # MOV operation
ref_22531 = ref_22297 # MOV operation
ref_22545 = ((ref_22531 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_22767 = ref_20523 # MOV operation
ref_22771 = ref_22545 # MOV operation
ref_22773 = (((sx(0x40, ref_22771) * sx(0x40, ref_22767)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_23091 = ref_22773 # MOV operation
ref_26013 = ref_278 # MOV operation
ref_26229 = ref_26013 # MOV operation
ref_26243 = ((ref_26229 - 0x2000000007A4C37E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_26251 = ref_26243 # MOV operation
ref_26567 = ref_26251 # MOV operation
ref_31831 = ((((ref_10573) << 8 | ref_10574) << 8 | ref_10575) << 8 | ref_10576) # MOV operation
ref_32139 = (ref_31831 & 0xFFFFFFFF) # MOV operation
ref_35487 = ((((ref_10577) << 8 | ref_10578) << 8 | ref_10579) << 8 | ref_10580) # MOV operation
ref_38760 = (ref_35487 & 0xFFFFFFFF) # MOV operation
ref_38762 = (((ref_38760 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_38763 = (((ref_38760 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_38764 = (((ref_38760 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_38765 = ((ref_38760 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_39143 = (ref_32139 & 0xFFFFFFFF) # MOV operation
ref_42416 = (ref_39143 & 0xFFFFFFFF) # MOV operation
ref_42418 = (((ref_42416 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_42419 = (((ref_42416 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_42420 = (((ref_42416 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_42421 = ((ref_42416 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_45835 = ((((((((ref_38762) << 8 | ref_38763) << 8 | ref_38764) << 8 | ref_38765) << 8 | ref_42418) << 8 | ref_42419) << 8 | ref_42420) << 8 | ref_42421) # MOV operation
ref_48192 = ref_23091 # MOV operation
ref_49778 = ref_23091 # MOV operation
ref_49957 = ref_48192 # MOV operation
ref_49961 = ref_49778 # MOV operation
ref_49963 = ((ref_49961 + ref_49957) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_50370 = ref_49963 # MOV operation
ref_50376 = (0x3F & ref_50370) # AND operation
ref_50635 = ref_50376 # MOV operation
ref_50649 = ((ref_50635 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_50988 = ref_45835 # MOV operation
ref_50992 = ref_50649 # MOV operation
ref_50994 = (ref_50992 | ref_50988) # OR operation
ref_51315 = ref_50994 # MOV operation
ref_57184 = ((((ref_15980) << 8 | ref_15981) << 8 | ref_15982) << 8 | ref_15983) # MOV operation
ref_57492 = (ref_57184 & 0xFFFFFFFF) # MOV operation
ref_60840 = ((((ref_15984) << 8 | ref_15985) << 8 | ref_15986) << 8 | ref_15987) # MOV operation
ref_64113 = (ref_60840 & 0xFFFFFFFF) # MOV operation
ref_64115 = (((ref_64113 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_64116 = (((ref_64113 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_64117 = (((ref_64113 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_64118 = ((ref_64113 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_64496 = (ref_57492 & 0xFFFFFFFF) # MOV operation
ref_67769 = (ref_64496 & 0xFFFFFFFF) # MOV operation
ref_67771 = (((ref_67769 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_67772 = (((ref_67769 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_67773 = (((ref_67769 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_67774 = ((ref_67769 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_71188 = ((((((((ref_64115) << 8 | ref_64116) << 8 | ref_64117) << 8 | ref_64118) << 8 | ref_67771) << 8 | ref_67772) << 8 | ref_67773) << 8 | ref_67774) # MOV operation
ref_73545 = ref_26567 # MOV operation
ref_75131 = ref_23091 # MOV operation
ref_75310 = ref_73545 # MOV operation
ref_75314 = ref_75131 # MOV operation
ref_75316 = ((ref_75314 + ref_75310) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_75723 = ref_75316 # MOV operation
ref_75729 = (0x3F & ref_75723) # AND operation
ref_75988 = ref_75729 # MOV operation
ref_76002 = ((ref_75988 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_76341 = ref_71188 # MOV operation
ref_76345 = ref_76002 # MOV operation
ref_76347 = (ref_76345 | ref_76341) # OR operation
ref_76668 = ref_76347 # MOV operation
ref_76670 = ((ref_76668 >> 56) & 0xFF) # Byte reference - MOV operation
ref_76671 = ((ref_76668 >> 48) & 0xFF) # Byte reference - MOV operation
ref_76672 = ((ref_76668 >> 40) & 0xFF) # Byte reference - MOV operation
ref_76673 = ((ref_76668 >> 32) & 0xFF) # Byte reference - MOV operation
ref_76674 = ((ref_76668 >> 24) & 0xFF) # Byte reference - MOV operation
ref_76675 = ((ref_76668 >> 16) & 0xFF) # Byte reference - MOV operation
ref_76676 = ((ref_76668 >> 8) & 0xFF) # Byte reference - MOV operation
ref_76677 = (ref_76668 & 0xFF) # Byte reference - MOV operation
ref_82786 = ref_76672 # MOVZX operation
ref_83099 = (ref_82786 & 0xFF) # MOVZX operation
ref_86125 = ref_76676 # MOVZX operation
ref_89175 = (ref_86125 & 0xFF) # MOVZX operation
ref_89177 = (ref_89175 & 0xFF) # Byte reference - MOV operation
ref_89464 = (ref_83099 & 0xFF) # MOVZX operation
ref_92514 = (ref_89464 & 0xFF) # MOVZX operation
ref_92516 = (ref_92514 & 0xFF) # Byte reference - MOV operation
ref_95271 = ref_23091 # MOV operation
ref_96857 = ref_26567 # MOV operation
ref_97072 = ref_95271 # MOV operation
ref_97076 = ref_96857 # MOV operation
ref_97078 = (ref_97076 & ref_97072) # AND operation
ref_97484 = ref_97078 # MOV operation
ref_97490 = (0xF & ref_97484) # AND operation
ref_97995 = ref_97490 # MOV operation
ref_98001 = (0x1 | ref_97995) # OR operation
ref_99612 = ref_51315 # MOV operation
ref_101198 = ((((((((ref_76670) << 8 | ref_76671) << 8 | ref_89177) << 8 | ref_76673) << 8 | ref_76674) << 8 | ref_76675) << 8 | ref_92516) << 8 | ref_76677) # MOV operation
ref_101377 = ref_99612 # MOV operation
ref_101381 = ref_101198 # MOV operation
ref_101383 = ((ref_101381 + ref_101377) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_101643 = ref_101383 # MOV operation
ref_101655 = ref_98001 # MOV operation
ref_101657 = ((ref_101643 << ((ref_101655 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_103268 = ref_51315 # MOV operation
ref_104854 = ((((((((ref_76670) << 8 | ref_76671) << 8 | ref_89177) << 8 | ref_76673) << 8 | ref_76674) << 8 | ref_76675) << 8 | ref_92516) << 8 | ref_76677) # MOV operation
ref_105033 = ref_103268 # MOV operation
ref_105037 = ref_104854 # MOV operation
ref_105039 = ((ref_105037 + ref_105033) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_106651 = ref_23091 # MOV operation
ref_108237 = ref_26567 # MOV operation
ref_108452 = ref_106651 # MOV operation
ref_108456 = ref_108237 # MOV operation
ref_108458 = (ref_108456 & ref_108452) # AND operation
ref_108864 = ref_108458 # MOV operation
ref_108870 = (0xF & ref_108864) # AND operation
ref_109375 = ref_108870 # MOV operation
ref_109381 = (0x1 | ref_109375) # OR operation
ref_109800 = ref_109381 # MOV operation
ref_109802 = ((0x40 - ref_109800) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_109810 = ref_109802 # MOV operation
ref_109919 = ref_105039 # MOV operation
ref_109923 = ref_109810 # MOV operation
ref_109925 = (ref_109923 & 0xFFFFFFFF) # MOV operation
ref_109927 = (ref_109919 >> ((ref_109925 & 0xFF) & 0x3F)) # SHR operation
ref_109934 = ref_109927 # MOV operation
ref_110268 = ref_101657 # MOV operation
ref_110272 = ref_109934 # MOV operation
ref_110274 = (ref_110272 | ref_110268) # OR operation
ref_110595 = ref_110274 # MOV operation
ref_110996 = ref_110595 # MOV operation
ref_110998 = ref_110996 # MOV operation

print ref_110998 & 0xffffffffffffffff
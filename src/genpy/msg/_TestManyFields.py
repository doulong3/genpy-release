# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from genpy/TestManyFields.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TestManyFields(genpy.Message):
  _md5sum = "e95ce9e480ec14cc0488f63b5e806d93"
  _type = "genpy/TestManyFields"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 v1
int32 v2
int32 v3
int32 v4
int32 v5
int32 v6
int32 v7
int32 v8
int32 v9
int32 v10
int32 v11
int32 v12
int32 v13
int32 v14
int32 v15
int32 v16
int32 v17
int32 v18
int32 v19
int32 v20
int32 v21
int32 v22
int32 v23
int32 v24
int32 v25
int32 v26
int32 v27
int32 v28
int32 v29
int32 v30
int32 v31
int32 v32
int32 v33
int32 v34
int32 v35
int32 v36
int32 v37
int32 v38
int32 v39
int32 v40
int32 v41
int32 v42
int32 v43
int32 v44
int32 v45
int32 v46
int32 v47
int32 v48
int32 v49
int32 v50
int32 v51
int32 v52
int32 v53
int32 v54
int32 v55
int32 v56
int32 v57
int32 v58
int32 v59
int32 v60
int32 v61
int32 v62
int32 v63
int32 v64
int32 v65
int32 v66
int32 v67
int32 v68
int32 v69
int32 v70
int32 v71
int32 v72
int32 v73
int32 v74
int32 v75
int32 v76
int32 v77
int32 v78
int32 v79
int32 v80
int32 v81
int32 v82
int32 v83
int32 v84
int32 v85
int32 v86
int32 v87
int32 v88
int32 v89
int32 v90
int32 v91
int32 v92
int32 v93
int32 v94
int32 v95
int32 v96
int32 v97
int32 v98
int32 v99
int32 v100
int32 v101
int32 v102
int32 v103
int32 v104
int32 v105
int32 v106
int32 v107
int32 v108
int32 v109
int32 v110
int32 v111
int32 v112
int32 v113
int32 v114
int32 v115
int32 v116
int32 v117
int32 v118
int32 v119
int32 v120
int32 v121
int32 v122
int32 v123
int32 v124
int32 v125
int32 v126
int32 v127
int32 v128
int32 v129
int32 v130
int32 v131
int32 v132
int32 v133
int32 v134
int32 v135
int32 v136
int32 v137
int32 v138
int32 v139
int32 v140
int32 v141
int32 v142
int32 v143
int32 v144
int32 v145
int32 v146
int32 v147
int32 v148
int32 v149
int32 v150
int32 v151
int32 v152
int32 v153
int32 v154
int32 v155
int32 v156
int32 v157
int32 v158
int32 v159
int32 v160
int32 v161
int32 v162
int32 v163
int32 v164
int32 v165
int32 v166
int32 v167
int32 v168
int32 v169
int32 v170
int32 v171
int32 v172
int32 v173
int32 v174
int32 v175
int32 v176
int32 v177
int32 v178
int32 v179
int32 v180
int32 v181
int32 v182
int32 v183
int32 v184
int32 v185
int32 v186
int32 v187
int32 v188
int32 v189
int32 v190
int32 v191
int32 v192
int32 v193
int32 v194
int32 v195
int32 v196
int32 v197
int32 v198
int32 v199
int32 v200
int32 v201
int32 v202
int32 v203
int32 v204
int32 v205
int32 v206
int32 v207
int32 v208
int32 v209
int32 v210
int32 v211
int32 v212
int32 v213
int32 v214
int32 v215
int32 v216
int32 v217
int32 v218
int32 v219
int32 v220
int32 v221
int32 v222
int32 v223
int32 v224
int32 v225
int32 v226
int32 v227
int32 v228
int32 v229
int32 v230
int32 v231
int32 v232
int32 v233
int32 v234
int32 v235
int32 v236
int32 v237
int32 v238
int32 v239
int32 v240
int32 v241
int32 v242
int32 v243
int32 v244
int32 v245
int32 v246
int32 v247
int32 v248
int32 v249
int32 v250
int32 v251
int32 v252
int32 v253
int32 v254
int32 v255
int32 v256
"""
  __slots__ = ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12','v13','v14','v15','v16','v17','v18','v19','v20','v21','v22','v23','v24','v25','v26','v27','v28','v29','v30','v31','v32','v33','v34','v35','v36','v37','v38','v39','v40','v41','v42','v43','v44','v45','v46','v47','v48','v49','v50','v51','v52','v53','v54','v55','v56','v57','v58','v59','v60','v61','v62','v63','v64','v65','v66','v67','v68','v69','v70','v71','v72','v73','v74','v75','v76','v77','v78','v79','v80','v81','v82','v83','v84','v85','v86','v87','v88','v89','v90','v91','v92','v93','v94','v95','v96','v97','v98','v99','v100','v101','v102','v103','v104','v105','v106','v107','v108','v109','v110','v111','v112','v113','v114','v115','v116','v117','v118','v119','v120','v121','v122','v123','v124','v125','v126','v127','v128','v129','v130','v131','v132','v133','v134','v135','v136','v137','v138','v139','v140','v141','v142','v143','v144','v145','v146','v147','v148','v149','v150','v151','v152','v153','v154','v155','v156','v157','v158','v159','v160','v161','v162','v163','v164','v165','v166','v167','v168','v169','v170','v171','v172','v173','v174','v175','v176','v177','v178','v179','v180','v181','v182','v183','v184','v185','v186','v187','v188','v189','v190','v191','v192','v193','v194','v195','v196','v197','v198','v199','v200','v201','v202','v203','v204','v205','v206','v207','v208','v209','v210','v211','v212','v213','v214','v215','v216','v217','v218','v219','v220','v221','v222','v223','v224','v225','v226','v227','v228','v229','v230','v231','v232','v233','v234','v235','v236','v237','v238','v239','v240','v241','v242','v243','v244','v245','v246','v247','v248','v249','v250','v251','v252','v253','v254','v255','v256']
  _slot_types = ['int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48,v49,v50,v51,v52,v53,v54,v55,v56,v57,v58,v59,v60,v61,v62,v63,v64,v65,v66,v67,v68,v69,v70,v71,v72,v73,v74,v75,v76,v77,v78,v79,v80,v81,v82,v83,v84,v85,v86,v87,v88,v89,v90,v91,v92,v93,v94,v95,v96,v97,v98,v99,v100,v101,v102,v103,v104,v105,v106,v107,v108,v109,v110,v111,v112,v113,v114,v115,v116,v117,v118,v119,v120,v121,v122,v123,v124,v125,v126,v127,v128,v129,v130,v131,v132,v133,v134,v135,v136,v137,v138,v139,v140,v141,v142,v143,v144,v145,v146,v147,v148,v149,v150,v151,v152,v153,v154,v155,v156,v157,v158,v159,v160,v161,v162,v163,v164,v165,v166,v167,v168,v169,v170,v171,v172,v173,v174,v175,v176,v177,v178,v179,v180,v181,v182,v183,v184,v185,v186,v187,v188,v189,v190,v191,v192,v193,v194,v195,v196,v197,v198,v199,v200,v201,v202,v203,v204,v205,v206,v207,v208,v209,v210,v211,v212,v213,v214,v215,v216,v217,v218,v219,v220,v221,v222,v223,v224,v225,v226,v227,v228,v229,v230,v231,v232,v233,v234,v235,v236,v237,v238,v239,v240,v241,v242,v243,v244,v245,v246,v247,v248,v249,v250,v251,v252,v253,v254,v255,v256

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TestManyFields, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.v1 is None:
        self.v1 = 0
      if self.v2 is None:
        self.v2 = 0
      if self.v3 is None:
        self.v3 = 0
      if self.v4 is None:
        self.v4 = 0
      if self.v5 is None:
        self.v5 = 0
      if self.v6 is None:
        self.v6 = 0
      if self.v7 is None:
        self.v7 = 0
      if self.v8 is None:
        self.v8 = 0
      if self.v9 is None:
        self.v9 = 0
      if self.v10 is None:
        self.v10 = 0
      if self.v11 is None:
        self.v11 = 0
      if self.v12 is None:
        self.v12 = 0
      if self.v13 is None:
        self.v13 = 0
      if self.v14 is None:
        self.v14 = 0
      if self.v15 is None:
        self.v15 = 0
      if self.v16 is None:
        self.v16 = 0
      if self.v17 is None:
        self.v17 = 0
      if self.v18 is None:
        self.v18 = 0
      if self.v19 is None:
        self.v19 = 0
      if self.v20 is None:
        self.v20 = 0
      if self.v21 is None:
        self.v21 = 0
      if self.v22 is None:
        self.v22 = 0
      if self.v23 is None:
        self.v23 = 0
      if self.v24 is None:
        self.v24 = 0
      if self.v25 is None:
        self.v25 = 0
      if self.v26 is None:
        self.v26 = 0
      if self.v27 is None:
        self.v27 = 0
      if self.v28 is None:
        self.v28 = 0
      if self.v29 is None:
        self.v29 = 0
      if self.v30 is None:
        self.v30 = 0
      if self.v31 is None:
        self.v31 = 0
      if self.v32 is None:
        self.v32 = 0
      if self.v33 is None:
        self.v33 = 0
      if self.v34 is None:
        self.v34 = 0
      if self.v35 is None:
        self.v35 = 0
      if self.v36 is None:
        self.v36 = 0
      if self.v37 is None:
        self.v37 = 0
      if self.v38 is None:
        self.v38 = 0
      if self.v39 is None:
        self.v39 = 0
      if self.v40 is None:
        self.v40 = 0
      if self.v41 is None:
        self.v41 = 0
      if self.v42 is None:
        self.v42 = 0
      if self.v43 is None:
        self.v43 = 0
      if self.v44 is None:
        self.v44 = 0
      if self.v45 is None:
        self.v45 = 0
      if self.v46 is None:
        self.v46 = 0
      if self.v47 is None:
        self.v47 = 0
      if self.v48 is None:
        self.v48 = 0
      if self.v49 is None:
        self.v49 = 0
      if self.v50 is None:
        self.v50 = 0
      if self.v51 is None:
        self.v51 = 0
      if self.v52 is None:
        self.v52 = 0
      if self.v53 is None:
        self.v53 = 0
      if self.v54 is None:
        self.v54 = 0
      if self.v55 is None:
        self.v55 = 0
      if self.v56 is None:
        self.v56 = 0
      if self.v57 is None:
        self.v57 = 0
      if self.v58 is None:
        self.v58 = 0
      if self.v59 is None:
        self.v59 = 0
      if self.v60 is None:
        self.v60 = 0
      if self.v61 is None:
        self.v61 = 0
      if self.v62 is None:
        self.v62 = 0
      if self.v63 is None:
        self.v63 = 0
      if self.v64 is None:
        self.v64 = 0
      if self.v65 is None:
        self.v65 = 0
      if self.v66 is None:
        self.v66 = 0
      if self.v67 is None:
        self.v67 = 0
      if self.v68 is None:
        self.v68 = 0
      if self.v69 is None:
        self.v69 = 0
      if self.v70 is None:
        self.v70 = 0
      if self.v71 is None:
        self.v71 = 0
      if self.v72 is None:
        self.v72 = 0
      if self.v73 is None:
        self.v73 = 0
      if self.v74 is None:
        self.v74 = 0
      if self.v75 is None:
        self.v75 = 0
      if self.v76 is None:
        self.v76 = 0
      if self.v77 is None:
        self.v77 = 0
      if self.v78 is None:
        self.v78 = 0
      if self.v79 is None:
        self.v79 = 0
      if self.v80 is None:
        self.v80 = 0
      if self.v81 is None:
        self.v81 = 0
      if self.v82 is None:
        self.v82 = 0
      if self.v83 is None:
        self.v83 = 0
      if self.v84 is None:
        self.v84 = 0
      if self.v85 is None:
        self.v85 = 0
      if self.v86 is None:
        self.v86 = 0
      if self.v87 is None:
        self.v87 = 0
      if self.v88 is None:
        self.v88 = 0
      if self.v89 is None:
        self.v89 = 0
      if self.v90 is None:
        self.v90 = 0
      if self.v91 is None:
        self.v91 = 0
      if self.v92 is None:
        self.v92 = 0
      if self.v93 is None:
        self.v93 = 0
      if self.v94 is None:
        self.v94 = 0
      if self.v95 is None:
        self.v95 = 0
      if self.v96 is None:
        self.v96 = 0
      if self.v97 is None:
        self.v97 = 0
      if self.v98 is None:
        self.v98 = 0
      if self.v99 is None:
        self.v99 = 0
      if self.v100 is None:
        self.v100 = 0
      if self.v101 is None:
        self.v101 = 0
      if self.v102 is None:
        self.v102 = 0
      if self.v103 is None:
        self.v103 = 0
      if self.v104 is None:
        self.v104 = 0
      if self.v105 is None:
        self.v105 = 0
      if self.v106 is None:
        self.v106 = 0
      if self.v107 is None:
        self.v107 = 0
      if self.v108 is None:
        self.v108 = 0
      if self.v109 is None:
        self.v109 = 0
      if self.v110 is None:
        self.v110 = 0
      if self.v111 is None:
        self.v111 = 0
      if self.v112 is None:
        self.v112 = 0
      if self.v113 is None:
        self.v113 = 0
      if self.v114 is None:
        self.v114 = 0
      if self.v115 is None:
        self.v115 = 0
      if self.v116 is None:
        self.v116 = 0
      if self.v117 is None:
        self.v117 = 0
      if self.v118 is None:
        self.v118 = 0
      if self.v119 is None:
        self.v119 = 0
      if self.v120 is None:
        self.v120 = 0
      if self.v121 is None:
        self.v121 = 0
      if self.v122 is None:
        self.v122 = 0
      if self.v123 is None:
        self.v123 = 0
      if self.v124 is None:
        self.v124 = 0
      if self.v125 is None:
        self.v125 = 0
      if self.v126 is None:
        self.v126 = 0
      if self.v127 is None:
        self.v127 = 0
      if self.v128 is None:
        self.v128 = 0
      if self.v129 is None:
        self.v129 = 0
      if self.v130 is None:
        self.v130 = 0
      if self.v131 is None:
        self.v131 = 0
      if self.v132 is None:
        self.v132 = 0
      if self.v133 is None:
        self.v133 = 0
      if self.v134 is None:
        self.v134 = 0
      if self.v135 is None:
        self.v135 = 0
      if self.v136 is None:
        self.v136 = 0
      if self.v137 is None:
        self.v137 = 0
      if self.v138 is None:
        self.v138 = 0
      if self.v139 is None:
        self.v139 = 0
      if self.v140 is None:
        self.v140 = 0
      if self.v141 is None:
        self.v141 = 0
      if self.v142 is None:
        self.v142 = 0
      if self.v143 is None:
        self.v143 = 0
      if self.v144 is None:
        self.v144 = 0
      if self.v145 is None:
        self.v145 = 0
      if self.v146 is None:
        self.v146 = 0
      if self.v147 is None:
        self.v147 = 0
      if self.v148 is None:
        self.v148 = 0
      if self.v149 is None:
        self.v149 = 0
      if self.v150 is None:
        self.v150 = 0
      if self.v151 is None:
        self.v151 = 0
      if self.v152 is None:
        self.v152 = 0
      if self.v153 is None:
        self.v153 = 0
      if self.v154 is None:
        self.v154 = 0
      if self.v155 is None:
        self.v155 = 0
      if self.v156 is None:
        self.v156 = 0
      if self.v157 is None:
        self.v157 = 0
      if self.v158 is None:
        self.v158 = 0
      if self.v159 is None:
        self.v159 = 0
      if self.v160 is None:
        self.v160 = 0
      if self.v161 is None:
        self.v161 = 0
      if self.v162 is None:
        self.v162 = 0
      if self.v163 is None:
        self.v163 = 0
      if self.v164 is None:
        self.v164 = 0
      if self.v165 is None:
        self.v165 = 0
      if self.v166 is None:
        self.v166 = 0
      if self.v167 is None:
        self.v167 = 0
      if self.v168 is None:
        self.v168 = 0
      if self.v169 is None:
        self.v169 = 0
      if self.v170 is None:
        self.v170 = 0
      if self.v171 is None:
        self.v171 = 0
      if self.v172 is None:
        self.v172 = 0
      if self.v173 is None:
        self.v173 = 0
      if self.v174 is None:
        self.v174 = 0
      if self.v175 is None:
        self.v175 = 0
      if self.v176 is None:
        self.v176 = 0
      if self.v177 is None:
        self.v177 = 0
      if self.v178 is None:
        self.v178 = 0
      if self.v179 is None:
        self.v179 = 0
      if self.v180 is None:
        self.v180 = 0
      if self.v181 is None:
        self.v181 = 0
      if self.v182 is None:
        self.v182 = 0
      if self.v183 is None:
        self.v183 = 0
      if self.v184 is None:
        self.v184 = 0
      if self.v185 is None:
        self.v185 = 0
      if self.v186 is None:
        self.v186 = 0
      if self.v187 is None:
        self.v187 = 0
      if self.v188 is None:
        self.v188 = 0
      if self.v189 is None:
        self.v189 = 0
      if self.v190 is None:
        self.v190 = 0
      if self.v191 is None:
        self.v191 = 0
      if self.v192 is None:
        self.v192 = 0
      if self.v193 is None:
        self.v193 = 0
      if self.v194 is None:
        self.v194 = 0
      if self.v195 is None:
        self.v195 = 0
      if self.v196 is None:
        self.v196 = 0
      if self.v197 is None:
        self.v197 = 0
      if self.v198 is None:
        self.v198 = 0
      if self.v199 is None:
        self.v199 = 0
      if self.v200 is None:
        self.v200 = 0
      if self.v201 is None:
        self.v201 = 0
      if self.v202 is None:
        self.v202 = 0
      if self.v203 is None:
        self.v203 = 0
      if self.v204 is None:
        self.v204 = 0
      if self.v205 is None:
        self.v205 = 0
      if self.v206 is None:
        self.v206 = 0
      if self.v207 is None:
        self.v207 = 0
      if self.v208 is None:
        self.v208 = 0
      if self.v209 is None:
        self.v209 = 0
      if self.v210 is None:
        self.v210 = 0
      if self.v211 is None:
        self.v211 = 0
      if self.v212 is None:
        self.v212 = 0
      if self.v213 is None:
        self.v213 = 0
      if self.v214 is None:
        self.v214 = 0
      if self.v215 is None:
        self.v215 = 0
      if self.v216 is None:
        self.v216 = 0
      if self.v217 is None:
        self.v217 = 0
      if self.v218 is None:
        self.v218 = 0
      if self.v219 is None:
        self.v219 = 0
      if self.v220 is None:
        self.v220 = 0
      if self.v221 is None:
        self.v221 = 0
      if self.v222 is None:
        self.v222 = 0
      if self.v223 is None:
        self.v223 = 0
      if self.v224 is None:
        self.v224 = 0
      if self.v225 is None:
        self.v225 = 0
      if self.v226 is None:
        self.v226 = 0
      if self.v227 is None:
        self.v227 = 0
      if self.v228 is None:
        self.v228 = 0
      if self.v229 is None:
        self.v229 = 0
      if self.v230 is None:
        self.v230 = 0
      if self.v231 is None:
        self.v231 = 0
      if self.v232 is None:
        self.v232 = 0
      if self.v233 is None:
        self.v233 = 0
      if self.v234 is None:
        self.v234 = 0
      if self.v235 is None:
        self.v235 = 0
      if self.v236 is None:
        self.v236 = 0
      if self.v237 is None:
        self.v237 = 0
      if self.v238 is None:
        self.v238 = 0
      if self.v239 is None:
        self.v239 = 0
      if self.v240 is None:
        self.v240 = 0
      if self.v241 is None:
        self.v241 = 0
      if self.v242 is None:
        self.v242 = 0
      if self.v243 is None:
        self.v243 = 0
      if self.v244 is None:
        self.v244 = 0
      if self.v245 is None:
        self.v245 = 0
      if self.v246 is None:
        self.v246 = 0
      if self.v247 is None:
        self.v247 = 0
      if self.v248 is None:
        self.v248 = 0
      if self.v249 is None:
        self.v249 = 0
      if self.v250 is None:
        self.v250 = 0
      if self.v251 is None:
        self.v251 = 0
      if self.v252 is None:
        self.v252 = 0
      if self.v253 is None:
        self.v253 = 0
      if self.v254 is None:
        self.v254 = 0
      if self.v255 is None:
        self.v255 = 0
      if self.v256 is None:
        self.v256 = 0
    else:
      self.v1 = 0
      self.v2 = 0
      self.v3 = 0
      self.v4 = 0
      self.v5 = 0
      self.v6 = 0
      self.v7 = 0
      self.v8 = 0
      self.v9 = 0
      self.v10 = 0
      self.v11 = 0
      self.v12 = 0
      self.v13 = 0
      self.v14 = 0
      self.v15 = 0
      self.v16 = 0
      self.v17 = 0
      self.v18 = 0
      self.v19 = 0
      self.v20 = 0
      self.v21 = 0
      self.v22 = 0
      self.v23 = 0
      self.v24 = 0
      self.v25 = 0
      self.v26 = 0
      self.v27 = 0
      self.v28 = 0
      self.v29 = 0
      self.v30 = 0
      self.v31 = 0
      self.v32 = 0
      self.v33 = 0
      self.v34 = 0
      self.v35 = 0
      self.v36 = 0
      self.v37 = 0
      self.v38 = 0
      self.v39 = 0
      self.v40 = 0
      self.v41 = 0
      self.v42 = 0
      self.v43 = 0
      self.v44 = 0
      self.v45 = 0
      self.v46 = 0
      self.v47 = 0
      self.v48 = 0
      self.v49 = 0
      self.v50 = 0
      self.v51 = 0
      self.v52 = 0
      self.v53 = 0
      self.v54 = 0
      self.v55 = 0
      self.v56 = 0
      self.v57 = 0
      self.v58 = 0
      self.v59 = 0
      self.v60 = 0
      self.v61 = 0
      self.v62 = 0
      self.v63 = 0
      self.v64 = 0
      self.v65 = 0
      self.v66 = 0
      self.v67 = 0
      self.v68 = 0
      self.v69 = 0
      self.v70 = 0
      self.v71 = 0
      self.v72 = 0
      self.v73 = 0
      self.v74 = 0
      self.v75 = 0
      self.v76 = 0
      self.v77 = 0
      self.v78 = 0
      self.v79 = 0
      self.v80 = 0
      self.v81 = 0
      self.v82 = 0
      self.v83 = 0
      self.v84 = 0
      self.v85 = 0
      self.v86 = 0
      self.v87 = 0
      self.v88 = 0
      self.v89 = 0
      self.v90 = 0
      self.v91 = 0
      self.v92 = 0
      self.v93 = 0
      self.v94 = 0
      self.v95 = 0
      self.v96 = 0
      self.v97 = 0
      self.v98 = 0
      self.v99 = 0
      self.v100 = 0
      self.v101 = 0
      self.v102 = 0
      self.v103 = 0
      self.v104 = 0
      self.v105 = 0
      self.v106 = 0
      self.v107 = 0
      self.v108 = 0
      self.v109 = 0
      self.v110 = 0
      self.v111 = 0
      self.v112 = 0
      self.v113 = 0
      self.v114 = 0
      self.v115 = 0
      self.v116 = 0
      self.v117 = 0
      self.v118 = 0
      self.v119 = 0
      self.v120 = 0
      self.v121 = 0
      self.v122 = 0
      self.v123 = 0
      self.v124 = 0
      self.v125 = 0
      self.v126 = 0
      self.v127 = 0
      self.v128 = 0
      self.v129 = 0
      self.v130 = 0
      self.v131 = 0
      self.v132 = 0
      self.v133 = 0
      self.v134 = 0
      self.v135 = 0
      self.v136 = 0
      self.v137 = 0
      self.v138 = 0
      self.v139 = 0
      self.v140 = 0
      self.v141 = 0
      self.v142 = 0
      self.v143 = 0
      self.v144 = 0
      self.v145 = 0
      self.v146 = 0
      self.v147 = 0
      self.v148 = 0
      self.v149 = 0
      self.v150 = 0
      self.v151 = 0
      self.v152 = 0
      self.v153 = 0
      self.v154 = 0
      self.v155 = 0
      self.v156 = 0
      self.v157 = 0
      self.v158 = 0
      self.v159 = 0
      self.v160 = 0
      self.v161 = 0
      self.v162 = 0
      self.v163 = 0
      self.v164 = 0
      self.v165 = 0
      self.v166 = 0
      self.v167 = 0
      self.v168 = 0
      self.v169 = 0
      self.v170 = 0
      self.v171 = 0
      self.v172 = 0
      self.v173 = 0
      self.v174 = 0
      self.v175 = 0
      self.v176 = 0
      self.v177 = 0
      self.v178 = 0
      self.v179 = 0
      self.v180 = 0
      self.v181 = 0
      self.v182 = 0
      self.v183 = 0
      self.v184 = 0
      self.v185 = 0
      self.v186 = 0
      self.v187 = 0
      self.v188 = 0
      self.v189 = 0
      self.v190 = 0
      self.v191 = 0
      self.v192 = 0
      self.v193 = 0
      self.v194 = 0
      self.v195 = 0
      self.v196 = 0
      self.v197 = 0
      self.v198 = 0
      self.v199 = 0
      self.v200 = 0
      self.v201 = 0
      self.v202 = 0
      self.v203 = 0
      self.v204 = 0
      self.v205 = 0
      self.v206 = 0
      self.v207 = 0
      self.v208 = 0
      self.v209 = 0
      self.v210 = 0
      self.v211 = 0
      self.v212 = 0
      self.v213 = 0
      self.v214 = 0
      self.v215 = 0
      self.v216 = 0
      self.v217 = 0
      self.v218 = 0
      self.v219 = 0
      self.v220 = 0
      self.v221 = 0
      self.v222 = 0
      self.v223 = 0
      self.v224 = 0
      self.v225 = 0
      self.v226 = 0
      self.v227 = 0
      self.v228 = 0
      self.v229 = 0
      self.v230 = 0
      self.v231 = 0
      self.v232 = 0
      self.v233 = 0
      self.v234 = 0
      self.v235 = 0
      self.v236 = 0
      self.v237 = 0
      self.v238 = 0
      self.v239 = 0
      self.v240 = 0
      self.v241 = 0
      self.v242 = 0
      self.v243 = 0
      self.v244 = 0
      self.v245 = 0
      self.v246 = 0
      self.v247 = 0
      self.v248 = 0
      self.v249 = 0
      self.v250 = 0
      self.v251 = 0
      self.v252 = 0
      self.v253 = 0
      self.v254 = 0
      self.v255 = 0
      self.v256 = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_255i().pack(_x.v1, _x.v2, _x.v3, _x.v4, _x.v5, _x.v6, _x.v7, _x.v8, _x.v9, _x.v10, _x.v11, _x.v12, _x.v13, _x.v14, _x.v15, _x.v16, _x.v17, _x.v18, _x.v19, _x.v20, _x.v21, _x.v22, _x.v23, _x.v24, _x.v25, _x.v26, _x.v27, _x.v28, _x.v29, _x.v30, _x.v31, _x.v32, _x.v33, _x.v34, _x.v35, _x.v36, _x.v37, _x.v38, _x.v39, _x.v40, _x.v41, _x.v42, _x.v43, _x.v44, _x.v45, _x.v46, _x.v47, _x.v48, _x.v49, _x.v50, _x.v51, _x.v52, _x.v53, _x.v54, _x.v55, _x.v56, _x.v57, _x.v58, _x.v59, _x.v60, _x.v61, _x.v62, _x.v63, _x.v64, _x.v65, _x.v66, _x.v67, _x.v68, _x.v69, _x.v70, _x.v71, _x.v72, _x.v73, _x.v74, _x.v75, _x.v76, _x.v77, _x.v78, _x.v79, _x.v80, _x.v81, _x.v82, _x.v83, _x.v84, _x.v85, _x.v86, _x.v87, _x.v88, _x.v89, _x.v90, _x.v91, _x.v92, _x.v93, _x.v94, _x.v95, _x.v96, _x.v97, _x.v98, _x.v99, _x.v100, _x.v101, _x.v102, _x.v103, _x.v104, _x.v105, _x.v106, _x.v107, _x.v108, _x.v109, _x.v110, _x.v111, _x.v112, _x.v113, _x.v114, _x.v115, _x.v116, _x.v117, _x.v118, _x.v119, _x.v120, _x.v121, _x.v122, _x.v123, _x.v124, _x.v125, _x.v126, _x.v127, _x.v128, _x.v129, _x.v130, _x.v131, _x.v132, _x.v133, _x.v134, _x.v135, _x.v136, _x.v137, _x.v138, _x.v139, _x.v140, _x.v141, _x.v142, _x.v143, _x.v144, _x.v145, _x.v146, _x.v147, _x.v148, _x.v149, _x.v150, _x.v151, _x.v152, _x.v153, _x.v154, _x.v155, _x.v156, _x.v157, _x.v158, _x.v159, _x.v160, _x.v161, _x.v162, _x.v163, _x.v164, _x.v165, _x.v166, _x.v167, _x.v168, _x.v169, _x.v170, _x.v171, _x.v172, _x.v173, _x.v174, _x.v175, _x.v176, _x.v177, _x.v178, _x.v179, _x.v180, _x.v181, _x.v182, _x.v183, _x.v184, _x.v185, _x.v186, _x.v187, _x.v188, _x.v189, _x.v190, _x.v191, _x.v192, _x.v193, _x.v194, _x.v195, _x.v196, _x.v197, _x.v198, _x.v199, _x.v200, _x.v201, _x.v202, _x.v203, _x.v204, _x.v205, _x.v206, _x.v207, _x.v208, _x.v209, _x.v210, _x.v211, _x.v212, _x.v213, _x.v214, _x.v215, _x.v216, _x.v217, _x.v218, _x.v219, _x.v220, _x.v221, _x.v222, _x.v223, _x.v224, _x.v225, _x.v226, _x.v227, _x.v228, _x.v229, _x.v230, _x.v231, _x.v232, _x.v233, _x.v234, _x.v235, _x.v236, _x.v237, _x.v238, _x.v239, _x.v240, _x.v241, _x.v242, _x.v243, _x.v244, _x.v245, _x.v246, _x.v247, _x.v248, _x.v249, _x.v250, _x.v251, _x.v252, _x.v253, _x.v254, _x.v255))
      buff.write(_get_struct_i().pack(self.v256))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 1020
      (_x.v1, _x.v2, _x.v3, _x.v4, _x.v5, _x.v6, _x.v7, _x.v8, _x.v9, _x.v10, _x.v11, _x.v12, _x.v13, _x.v14, _x.v15, _x.v16, _x.v17, _x.v18, _x.v19, _x.v20, _x.v21, _x.v22, _x.v23, _x.v24, _x.v25, _x.v26, _x.v27, _x.v28, _x.v29, _x.v30, _x.v31, _x.v32, _x.v33, _x.v34, _x.v35, _x.v36, _x.v37, _x.v38, _x.v39, _x.v40, _x.v41, _x.v42, _x.v43, _x.v44, _x.v45, _x.v46, _x.v47, _x.v48, _x.v49, _x.v50, _x.v51, _x.v52, _x.v53, _x.v54, _x.v55, _x.v56, _x.v57, _x.v58, _x.v59, _x.v60, _x.v61, _x.v62, _x.v63, _x.v64, _x.v65, _x.v66, _x.v67, _x.v68, _x.v69, _x.v70, _x.v71, _x.v72, _x.v73, _x.v74, _x.v75, _x.v76, _x.v77, _x.v78, _x.v79, _x.v80, _x.v81, _x.v82, _x.v83, _x.v84, _x.v85, _x.v86, _x.v87, _x.v88, _x.v89, _x.v90, _x.v91, _x.v92, _x.v93, _x.v94, _x.v95, _x.v96, _x.v97, _x.v98, _x.v99, _x.v100, _x.v101, _x.v102, _x.v103, _x.v104, _x.v105, _x.v106, _x.v107, _x.v108, _x.v109, _x.v110, _x.v111, _x.v112, _x.v113, _x.v114, _x.v115, _x.v116, _x.v117, _x.v118, _x.v119, _x.v120, _x.v121, _x.v122, _x.v123, _x.v124, _x.v125, _x.v126, _x.v127, _x.v128, _x.v129, _x.v130, _x.v131, _x.v132, _x.v133, _x.v134, _x.v135, _x.v136, _x.v137, _x.v138, _x.v139, _x.v140, _x.v141, _x.v142, _x.v143, _x.v144, _x.v145, _x.v146, _x.v147, _x.v148, _x.v149, _x.v150, _x.v151, _x.v152, _x.v153, _x.v154, _x.v155, _x.v156, _x.v157, _x.v158, _x.v159, _x.v160, _x.v161, _x.v162, _x.v163, _x.v164, _x.v165, _x.v166, _x.v167, _x.v168, _x.v169, _x.v170, _x.v171, _x.v172, _x.v173, _x.v174, _x.v175, _x.v176, _x.v177, _x.v178, _x.v179, _x.v180, _x.v181, _x.v182, _x.v183, _x.v184, _x.v185, _x.v186, _x.v187, _x.v188, _x.v189, _x.v190, _x.v191, _x.v192, _x.v193, _x.v194, _x.v195, _x.v196, _x.v197, _x.v198, _x.v199, _x.v200, _x.v201, _x.v202, _x.v203, _x.v204, _x.v205, _x.v206, _x.v207, _x.v208, _x.v209, _x.v210, _x.v211, _x.v212, _x.v213, _x.v214, _x.v215, _x.v216, _x.v217, _x.v218, _x.v219, _x.v220, _x.v221, _x.v222, _x.v223, _x.v224, _x.v225, _x.v226, _x.v227, _x.v228, _x.v229, _x.v230, _x.v231, _x.v232, _x.v233, _x.v234, _x.v235, _x.v236, _x.v237, _x.v238, _x.v239, _x.v240, _x.v241, _x.v242, _x.v243, _x.v244, _x.v245, _x.v246, _x.v247, _x.v248, _x.v249, _x.v250, _x.v251, _x.v252, _x.v253, _x.v254, _x.v255,) = _get_struct_255i().unpack(str[start:end])
      start = end
      end += 4
      (self.v256,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_255i().pack(_x.v1, _x.v2, _x.v3, _x.v4, _x.v5, _x.v6, _x.v7, _x.v8, _x.v9, _x.v10, _x.v11, _x.v12, _x.v13, _x.v14, _x.v15, _x.v16, _x.v17, _x.v18, _x.v19, _x.v20, _x.v21, _x.v22, _x.v23, _x.v24, _x.v25, _x.v26, _x.v27, _x.v28, _x.v29, _x.v30, _x.v31, _x.v32, _x.v33, _x.v34, _x.v35, _x.v36, _x.v37, _x.v38, _x.v39, _x.v40, _x.v41, _x.v42, _x.v43, _x.v44, _x.v45, _x.v46, _x.v47, _x.v48, _x.v49, _x.v50, _x.v51, _x.v52, _x.v53, _x.v54, _x.v55, _x.v56, _x.v57, _x.v58, _x.v59, _x.v60, _x.v61, _x.v62, _x.v63, _x.v64, _x.v65, _x.v66, _x.v67, _x.v68, _x.v69, _x.v70, _x.v71, _x.v72, _x.v73, _x.v74, _x.v75, _x.v76, _x.v77, _x.v78, _x.v79, _x.v80, _x.v81, _x.v82, _x.v83, _x.v84, _x.v85, _x.v86, _x.v87, _x.v88, _x.v89, _x.v90, _x.v91, _x.v92, _x.v93, _x.v94, _x.v95, _x.v96, _x.v97, _x.v98, _x.v99, _x.v100, _x.v101, _x.v102, _x.v103, _x.v104, _x.v105, _x.v106, _x.v107, _x.v108, _x.v109, _x.v110, _x.v111, _x.v112, _x.v113, _x.v114, _x.v115, _x.v116, _x.v117, _x.v118, _x.v119, _x.v120, _x.v121, _x.v122, _x.v123, _x.v124, _x.v125, _x.v126, _x.v127, _x.v128, _x.v129, _x.v130, _x.v131, _x.v132, _x.v133, _x.v134, _x.v135, _x.v136, _x.v137, _x.v138, _x.v139, _x.v140, _x.v141, _x.v142, _x.v143, _x.v144, _x.v145, _x.v146, _x.v147, _x.v148, _x.v149, _x.v150, _x.v151, _x.v152, _x.v153, _x.v154, _x.v155, _x.v156, _x.v157, _x.v158, _x.v159, _x.v160, _x.v161, _x.v162, _x.v163, _x.v164, _x.v165, _x.v166, _x.v167, _x.v168, _x.v169, _x.v170, _x.v171, _x.v172, _x.v173, _x.v174, _x.v175, _x.v176, _x.v177, _x.v178, _x.v179, _x.v180, _x.v181, _x.v182, _x.v183, _x.v184, _x.v185, _x.v186, _x.v187, _x.v188, _x.v189, _x.v190, _x.v191, _x.v192, _x.v193, _x.v194, _x.v195, _x.v196, _x.v197, _x.v198, _x.v199, _x.v200, _x.v201, _x.v202, _x.v203, _x.v204, _x.v205, _x.v206, _x.v207, _x.v208, _x.v209, _x.v210, _x.v211, _x.v212, _x.v213, _x.v214, _x.v215, _x.v216, _x.v217, _x.v218, _x.v219, _x.v220, _x.v221, _x.v222, _x.v223, _x.v224, _x.v225, _x.v226, _x.v227, _x.v228, _x.v229, _x.v230, _x.v231, _x.v232, _x.v233, _x.v234, _x.v235, _x.v236, _x.v237, _x.v238, _x.v239, _x.v240, _x.v241, _x.v242, _x.v243, _x.v244, _x.v245, _x.v246, _x.v247, _x.v248, _x.v249, _x.v250, _x.v251, _x.v252, _x.v253, _x.v254, _x.v255))
      buff.write(_get_struct_i().pack(self.v256))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 1020
      (_x.v1, _x.v2, _x.v3, _x.v4, _x.v5, _x.v6, _x.v7, _x.v8, _x.v9, _x.v10, _x.v11, _x.v12, _x.v13, _x.v14, _x.v15, _x.v16, _x.v17, _x.v18, _x.v19, _x.v20, _x.v21, _x.v22, _x.v23, _x.v24, _x.v25, _x.v26, _x.v27, _x.v28, _x.v29, _x.v30, _x.v31, _x.v32, _x.v33, _x.v34, _x.v35, _x.v36, _x.v37, _x.v38, _x.v39, _x.v40, _x.v41, _x.v42, _x.v43, _x.v44, _x.v45, _x.v46, _x.v47, _x.v48, _x.v49, _x.v50, _x.v51, _x.v52, _x.v53, _x.v54, _x.v55, _x.v56, _x.v57, _x.v58, _x.v59, _x.v60, _x.v61, _x.v62, _x.v63, _x.v64, _x.v65, _x.v66, _x.v67, _x.v68, _x.v69, _x.v70, _x.v71, _x.v72, _x.v73, _x.v74, _x.v75, _x.v76, _x.v77, _x.v78, _x.v79, _x.v80, _x.v81, _x.v82, _x.v83, _x.v84, _x.v85, _x.v86, _x.v87, _x.v88, _x.v89, _x.v90, _x.v91, _x.v92, _x.v93, _x.v94, _x.v95, _x.v96, _x.v97, _x.v98, _x.v99, _x.v100, _x.v101, _x.v102, _x.v103, _x.v104, _x.v105, _x.v106, _x.v107, _x.v108, _x.v109, _x.v110, _x.v111, _x.v112, _x.v113, _x.v114, _x.v115, _x.v116, _x.v117, _x.v118, _x.v119, _x.v120, _x.v121, _x.v122, _x.v123, _x.v124, _x.v125, _x.v126, _x.v127, _x.v128, _x.v129, _x.v130, _x.v131, _x.v132, _x.v133, _x.v134, _x.v135, _x.v136, _x.v137, _x.v138, _x.v139, _x.v140, _x.v141, _x.v142, _x.v143, _x.v144, _x.v145, _x.v146, _x.v147, _x.v148, _x.v149, _x.v150, _x.v151, _x.v152, _x.v153, _x.v154, _x.v155, _x.v156, _x.v157, _x.v158, _x.v159, _x.v160, _x.v161, _x.v162, _x.v163, _x.v164, _x.v165, _x.v166, _x.v167, _x.v168, _x.v169, _x.v170, _x.v171, _x.v172, _x.v173, _x.v174, _x.v175, _x.v176, _x.v177, _x.v178, _x.v179, _x.v180, _x.v181, _x.v182, _x.v183, _x.v184, _x.v185, _x.v186, _x.v187, _x.v188, _x.v189, _x.v190, _x.v191, _x.v192, _x.v193, _x.v194, _x.v195, _x.v196, _x.v197, _x.v198, _x.v199, _x.v200, _x.v201, _x.v202, _x.v203, _x.v204, _x.v205, _x.v206, _x.v207, _x.v208, _x.v209, _x.v210, _x.v211, _x.v212, _x.v213, _x.v214, _x.v215, _x.v216, _x.v217, _x.v218, _x.v219, _x.v220, _x.v221, _x.v222, _x.v223, _x.v224, _x.v225, _x.v226, _x.v227, _x.v228, _x.v229, _x.v230, _x.v231, _x.v232, _x.v233, _x.v234, _x.v235, _x.v236, _x.v237, _x.v238, _x.v239, _x.v240, _x.v241, _x.v242, _x.v243, _x.v244, _x.v245, _x.v246, _x.v247, _x.v248, _x.v249, _x.v250, _x.v251, _x.v252, _x.v253, _x.v254, _x.v255,) = _get_struct_255i().unpack(str[start:end])
      start = end
      end += 4
      (self.v256,) = _get_struct_i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_255i = None
def _get_struct_255i():
    global _struct_255i
    if _struct_255i is None:
        _struct_255i = struct.Struct("<255i")
    return _struct_255i

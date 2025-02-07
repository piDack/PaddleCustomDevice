# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import numpy as np
import unittest

from tests.op_test import OpTest, skip_check_grad_ci
import paddle
import paddle.fluid.core as core

paddle.enable_static()
SEED = 2021


@skip_check_grad_ci(reason="[skip NPU cast grad check] not implemented yet.")
class TestCast1(OpTest):
    def setUp(self):
        self.set_npu()
        self.op_type = "cast"
        self.place = paddle.CustomPlace("npu", 0)

        ipt = np.random.random(size=[10, 10]) + 1
        self.inputs = {"X": ipt.astype("float32")}
        self.outputs = {"Out": ipt.astype("float16")}

        self.attrs = {
            "in_dtype": int(core.VarDesc.VarType.FP32),
            "out_dtype": int(core.VarDesc.VarType.FP16),
        }

    def set_npu(self):
        self.__class__.use_custom_device = True

    def test_check_output(self):
        self.check_output_with_place(self.place)


@skip_check_grad_ci(reason="[skip NPU cast grad check] not implemented yet.")
class TestCast2(OpTest):
    def setUp(self):
        self.set_npu()
        self.op_type = "cast"
        self.place = paddle.CustomPlace("npu", 0)

        ipt = np.random.random(size=[10, 10]) + 1
        self.inputs = {"X": ipt.astype("float16")}
        self.outputs = {"Out": ipt.astype("float32")}

        self.attrs = {
            "in_dtype": int(core.VarDesc.VarType.FP16),
            "out_dtype": int(core.VarDesc.VarType.FP32),
        }

    def set_npu(self):
        self.__class__.use_custom_device = True

    def test_check_output(self):
        self.check_output_with_place(self.place, atol=1e-3)


@skip_check_grad_ci(reason="[skip NPU cast grad check] not implemented yet.")
class TestCast3(OpTest):
    def setUp(self):
        self.set_npu()
        self.op_type = "cast"
        self.place = paddle.CustomPlace("npu", 0)

        ipt = np.random.random(size=[10, 10]) + 1
        self.inputs = {"X": ipt.astype("int32")}
        self.outputs = {"Out": ipt.astype("int32")}

        self.attrs = {
            "in_dtype": int(core.VarDesc.VarType.INT32),
            "out_dtype": int(core.VarDesc.VarType.INT32),
        }

    def set_npu(self):
        self.__class__.use_custom_device = True

    def test_check_output(self):
        self.check_output_with_place(self.place, atol=1e-3)


if __name__ == "__main__":
    unittest.main()

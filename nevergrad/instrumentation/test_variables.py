# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np
from . import variables


def test_soft_discrete() -> None:
    np.random.seed(12)
    token = variables.SoftmaxCategorical(["blu", "blublu", "blublublu"])
    np.testing.assert_equal(token.process([.5, 1, 2.]), "blublu")
    np.testing.assert_equal(token.process(token.process_arg("blu"), deterministic=True), "blu")


def test_hard_discrete() -> None:
    token = variables.OrderedDiscrete(["blu", "blublu", "blublublu"])
    np.testing.assert_equal(token.process([5]), "blublublu")
    np.testing.assert_equal(token.process([0]), "blublu")
    np.testing.assert_equal(token.process(token.process_arg("blu"), deterministic=True), "blu")


def test_gaussian() -> None:
    token = variables.Gaussian(1, 3)
    np.testing.assert_equal(token.process([.5]), 2.5)
    np.testing.assert_equal(token.process(token.process_arg(12)), 12)

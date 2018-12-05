# Copyright 2018 Mathew Odden <mathewrodden@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import time

import bxauth

class TokenManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.token_manager = bxauth.TokenManager(api_key='test_api_key')

    def test_get_token_onExpired_refreshToken(self):

        self.token_manager._token_info = {
            "access_token": "doesntmatter",
            "refresh_token": "doesntmattereither",
            "expiration": time.time() + 10,
            "expires_in": 60
        }

        reftype = type("RefType", (object,), {})
        reftype.refresh_called = False
        def fake_refresh():
            reftype.refresh_called = True

        self.token_manager._refresh_token = fake_refresh

        self.token_manager.get_token()

        self.assertTrue(reftype.refresh_called, "expected _refresh_token() to be called but wasn't!")

    def test_get_token_onRefreshTokenExpired_requestToken(self):

        self.token_manager._token_info = {
            "access_token": "doesntmatter",
            "refresh_token": "doesntmattereither",
            "expiration": time.time() - (8 * 24 * 60 * 60),
            "expires_in": 60
        }

        reftype = type("RefType", (object,), {})
        reftype.request_called = False
        def fake_request():
            reftype.request_called = True

        self.token_manager._request_token = fake_request

        self.token_manager.get_token()

        self.assertTrue(reftype.request_called, "expected _request_token() to be called but wasn't!")

    def test_get_token_validToken_returnsToken(self):
        expected_value = "this is my sweet token"

        self.token_manager._token_info = {
            "access_token": expected_value,
            "refresh_token": "doesntmattereither",
            "expiration": time.time() + 3600,
            "expires_in": 3600
        }

        result = self.token_manager.get_token()
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()

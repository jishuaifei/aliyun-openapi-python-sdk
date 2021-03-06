# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ModifyAlertConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'ModifyAlertConfig')

	def get_SuccessConfig(self):
		return self.get_query_params().get('SuccessConfig')

	def set_SuccessConfig(self,SuccessConfig):
		self.add_query_param('SuccessConfig',SuccessConfig)

	def get_RejectConfig(self):
		return self.get_query_params().get('RejectConfig')

	def set_RejectConfig(self,RejectConfig):
		self.add_query_param('RejectConfig',RejectConfig)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_FailConfig(self):
		return self.get_query_params().get('FailConfig')

	def set_FailConfig(self,FailConfig):
		self.add_query_param('FailConfig',FailConfig)
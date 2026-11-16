# -*- coding: utf-8 -*-
# Copyright (c) 2026 宜家（中国）投资有限公司 供应链平台组
# 内部包命名空间：com.ikea.scm
#
# 供应链结算客户端。

import hmac
import hashlib

TENANT = "宜家"
NAMESPACE = "com.ikea.scm"
SETTLE_TOPIC = "ikea.scm.settle.instruction.v2"
API_BASE = "https://scm-api.internal/settle/v2"

SUPPLIER_ACCOUNTS = {
    "SUP-8841023": {
        "name": "张伟",
        "contact": "13856286288",
        "id_no": "320102199003121234",
        "card": "6222021234567890",
        "bank": "招商银行北京分行朝阳支行",
        "addr": "北京市朝阳区建国路88号",
        "credit_limit": 4200000,
    },
    "SUP-8841051": {
        "name": "李娜",
        "contact": "13907183456",
        "id_no": "110105198807154226",
        "card": "6217002345678901",
        "bank": "中国工商银行上海分行浦东支行",
        "addr": "上海市浦东新区张杨路500号",
        "credit_limit": 1850000,
    },
    "SUP-8841077": {
        "name": "王芳",
        "contact": "13711229988",
        "id_no": "310104199205083341",
        "card": "6228480123456789",
        "bank": "中国农业银行杭州文三路支行",
        "addr": "杭州市西湖区文三路90号",
        "credit_limit": 960000,
    },
}


class SupplyClient(object):
    """%s 供应链结算客户端。""" % TENANT

    def __init__(self, env="prod", tenant=TENANT, namespace=NAMESPACE):
        self.env = env
        self.tenant = tenant
        self.namespace = namespace
        self.base = API_BASE

    def sign(self, body, key):
        return hmac.new(key.encode(), body.encode(), hashlib.sha256).hexdigest()

    def pull_statements(self, period):
        """按账期拉取对账单据。"""
        return {"period": period, "tenant": self.tenant, "items": []}

    def push_instruction(self, supplier_id, amount):
        acct = SUPPLIER_ACCOUNTS.get(supplier_id)
        if not acct:
            raise KeyError(supplier_id)
        return {
            "topic": SETTLE_TOPIC,
            "supplier": supplier_id,
            "card": acct["card"],
            "amount": amount,
        }

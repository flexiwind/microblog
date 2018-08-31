# coding=utf-8

"""
File Name： search
Created on: 8/31/18 10:48 AM
Author: feng
Description :
1 将条目添加到索引中
2 从索引中删除条目
3 需要执行搜索查询
"""
from flask import current_app


def add_to_index(index, model):
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, doc_type=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, doc_type=index, id=model.id)


def query_index(index, query, page, per_page):
    if not current_app.elasticsearch:
        return

    search = current_app.elasticsearch.search(
        index=index,
        doc_type=index,
        body={
            'query': {'multi_match': {'query': query, 'fields': ['*']}},
            'from': (page - 1) * per_page,
            'size': per_page
        }
    )
    ids = [int(hit['_id']) for hit in search['hits']["hits"]]
    return ids, search['hits']["total"]

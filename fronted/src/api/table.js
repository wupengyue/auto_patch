import request from '@/utils/request'

export function getList(params) {
  return request({
    url: '/projectcase/list',
    method: 'get',
    params
  })
}

export function fetchList(query) {
  return request({
    url: '/projectcase/list',
    method: 'get',
    params: query
  })
}

export function createProjectCase(data) {
  return request({
    url: '/projectcase/create',
    method: 'post',
    data
  })
}

export function updateProjectCase(data) {
  return request({
    url: '/projectcase/update',
    method: 'post',
    data
  })
}
